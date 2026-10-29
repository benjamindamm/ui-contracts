#!/usr/bin/env node
/**
 * Builder B — autocomplete-reproducibility-03
 *
 * Erzeugt aus der Definition unter components/ eine echte, editierbare
 * OpenPencil-Design-Datei (autocomplete.fig) mit den zehn benannten
 * Zuständen aus components/autocomplete/stories.json.
 *
 * Vorgehen:
 *   1. Definition lesen (tokens.json, stories.json, accessibility.rules.json,
 *      component.json, layout.css × 3) — keine Definitionswerte hartkodiert.
 *   2. Pro Story eine Fall-Spezifikation ableiten (Geometrie, Farben, Texte,
 *      Scroll-Offset) aus den CSS-Regeln und den a11y-Projektionen.
 *   3. Designgraph im Speicher aufbauen (renderJSX aus @open-pencil/core/design-jsx,
 *      Original-Layout, benannte Frames/Texte/Fills).
 *   4. .fig mit dem Original-Writer (exportFigFile) schreiben.
 *   5. .fig mit dem Original-Reader (parseFigFile, populate: 'all') wieder einlesen.
 *   6. preview.png / preview.svg aus dem Wiedereingelesenen Graphen rendern.
 *   7. Selbstprüfungen (erwartet vs. tatsächlich) in checks.json schreiben.
 *   8. source-sha256.json mit SHA-256 aller Definitionsdateien schreiben.
 *
 * Es werden ausschließlich Dateien in diesem Ordner geschrieben.
 */

import { createHash } from 'node:crypto'
import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs'
import { createRequire } from 'node:module'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

// ---------------------------------------------------------------------------
// Pfade und Werkzeugauflösung (gepinnte Umgebung unter tools/openpencil)
// ---------------------------------------------------------------------------

const OUT_DIR = path.dirname(fileURLToPath(import.meta.url))
const REPO_ROOT = path.resolve(OUT_DIR, '..', '..', '..', '..', '..')
const TOOLS_MANIFEST = path.join(REPO_ROOT, 'tools', 'openpencil', 'package.json')
const COMPONENTS_DIR = path.join(REPO_ROOT, 'components')

const req = createRequire(TOOLS_MANIFEST)
const load = (name) => import(pathToFileURL(req.resolve(name)).href)

const { SceneGraph } = await load('@open-pencil/scene-graph')
const { parseColor } = await load('@open-pencil/scene-graph/color')
const { parseCSSShadows } = await load('@open-pencil/scene-graph/css')
const { renderJSX } = await load('@open-pencil/core/design-jsx')
const {
  exportFigFile,
  parseFigFile,
  headlessRenderNodes,
  renderNodesToSVG
} = await load('@open-pencil/core/io')

const toolPkg = JSON.parse(readFileSync(TOOLS_MANIFEST, 'utf8'))
const TOOL_VERSIONS = Object.fromEntries(
  Object.entries(toolPkg.dependencies)
    .filter(([name]) => name.startsWith('@open-pencil/'))
    .map(([name, version]) => [name, version])
)

// ---------------------------------------------------------------------------
// 1. Definition einlesen
// ---------------------------------------------------------------------------

const readComp = (p) => readFileSync(path.join(COMPONENTS_DIR, p), 'utf8')
const readCompJson = (p) => JSON.parse(readComp(p))

const tokensRaw = readCompJson('tokens.json')
const storiesDoc = readCompJson('autocomplete/stories.json')
const stories = storiesDoc.stories
const a11y = readCompJson('autocomplete/accessibility.rules.json')
const component = readCompJson('autocomplete/component.json')
const cssAutocomplete = readComp('autocomplete/layout.css')
const cssOverlay = readComp('overlay/layout.css')
const cssScrollArea = readComp('scroll-area/layout.css')

// --- DTCG-Token-Auflösung (Referenzen wie "{base.gap}") --------------------

const tokenCache = new Map()
function tokenAt(dotPath) {
  if (tokenCache.has(dotPath)) return tokenCache.get(dotPath)
  let cur = tokensRaw
  for (const part of dotPath.split('.')) cur = cur?.[part]
  if (!cur || cur.$type === undefined) throw new Error(`Token nicht gefunden: ${dotPath}`)
  let value = cur.$value
  if (typeof value === 'string') {
    const ref = value.match(/^\{(.+)\}$/)
    if (ref) value = tokenAt(ref[1])
  }
  tokenCache.set(dotPath, value)
  return value
}
const acFont = (name) => tokenAt(`autocomplete.${name}`)

// --- Mini-CSS-Parser (genug für die flachen Regeln der Definition) ---------

function parseCss(text) {
  const clean = text.replace(/\/\*[\s\S]*?\*\//g, '')
  const rules = []
  const re = /([^{}]+)\{([^{}]*)\}/g
  let m
  while ((m = re.exec(clean))) {
    const selectors = m[1].split(',').map((s) => s.trim()).filter(Boolean)
    const decls = {}
    for (const d of m[2].split(';')) {
      const i = d.indexOf(':')
      if (i < 0) continue
      decls[d.slice(0, i).trim()] = d.slice(i + 1).trim()
    }
    rules.push({ selectors, decls })
  }
  return rules
}
const rulesAc = parseCss(cssAutocomplete)
const rulesOverlay = parseCss(cssOverlay)
const rulesScroll = parseCss(cssScrollArea)

function ruleFor(rules, selector) {
  const rule = rules.find((r) => r.selectors.includes(selector))
  if (!rule) throw new Error(`CSS-Regel nicht gefunden: ${selector}`)
  return rule.decls
}

// --- Werte aus CSS-Ausdrücken (var(--ac-*) → Token, Einheiten, Farben) -----

const camel = (s) => s.replace(/-([a-z])/g, (_, c) => c.toUpperCase())
function varValue(expr) {
  const m = String(expr).match(/var\(--ac-([a-zA-Z][a-zA-Z0-9-]*)\)/)
  if (m) return tokenAt(`autocomplete.${camel(m[1])}`)
  return String(expr).trim()
}
function lengthPx(expr) {
  const v = varValue(expr)
  if (typeof v === 'object' && 'unit' in v) {
    if (v.unit !== 'px') throw new Error(`Länge ohne px-Einheit: ${expr} → ${v.unit}`)
    return v.value
  }
  if (v === '0' || v === '0px') return 0
  const m = String(v).match(/^(-?\d+(?:\.\d+)?)px$/)
  if (!m) throw new Error(`Länge nicht lesbar: ${expr} → ${v}`)
  return Number(m[1])
}
function colorExpr(expr) {
  const v = varValue(expr)
  if (typeof v === 'object' && 'components' in v) {
    return { r: v.components[0], g: v.components[1], b: v.components[2], a: v.alpha }
  }
  const c = parseColor(String(v))
  return { r: c.r, g: c.g, b: c.b, a: c.a ?? 1 }
}
function parseBorder(expr) {
  const parts = String(expr).trim().split(/\s+/)
  return { width: lengthPx(parts[0]), style: parts[1] ?? 'solid', color: colorExpr(parts.slice(2).join(' ')) }
}
function parsePadding(expr) {
  const parts = String(expr).trim().split(/\s+/)
  const px = (s) => lengthPx(s)
  if (parts.length === 1) { const a = px(parts[0]); return { top: a, right: a, bottom: a, left: a } }
  if (parts.length === 2) { const t = px(parts[0]); const l = px(parts[1]); return { top: t, right: l, bottom: t, left: l } }
  if (parts.length === 4) return { top: px(parts[0]), right: px(parts[1]), bottom: px(parts[2]), left: px(parts[3]) }
  throw new Error(`Padding nicht lesbar: ${expr}`)
}
// box-shadow wird nicht selbst geparst: Der Rohwert aus der Definition geht
// an die JSX-Prop `shadow`, die der Original-Parser (parseCSSShadows) liest.

// --- Aus den Regeln der Definition gelesene Visualwerte --------------------

const rootR = ruleFor(rulesAc, '[data-component="Autocomplete"]')
const labelR = ruleFor(rulesAc, '[data-part="label"]')
const inputR = ruleFor(rulesAc, '[data-part="input"]')
const placeholderR = ruleFor(rulesAc, '[data-part="input"]::placeholder')
const inputDisabledR = ruleFor(rulesAc, '[data-part="input"]:disabled')
const optionR = ruleFor(rulesAc, '[data-part="option"]')
const optionActiveR = ruleFor(rulesAc, '[data-part="option"][aria-selected="true"]')
const optionDisabledR = ruleFor(rulesAc, '[data-part="option"][aria-disabled="true"]')
const statusR = ruleFor(rulesAc, '[data-part="status"]')
const statusErrorR = ruleFor(rulesAc, '[data-state="error"] [data-part="status"]')
const surfaceR = ruleFor(rulesOverlay, '[data-part="surface"]')
const viewportR = ruleFor(rulesScroll, '[data-part="viewport"]')

// Zustände, in denen der Input die Fokusrandfarbe trägt (aus den Selectoren).
const focusStates = new Set()
let focusColor = null
for (const rule of rulesAc) {
  for (const sel of rule.selectors) {
    const m = sel.match(/^\[data-state="([\w-]+)"\] \[data-part="input"\]$/)
    if (m && rule.decls['border-color']) {
      focusStates.add(m[1])
      focusColor = colorExpr(rule.decls['border-color'])
    }
  }
}

const V = {
  width: lengthPx(rootR.width),
  fontFamily: String(acFont('fontFamily')),
  fontSize: lengthPx(rootR['font-size']),
  lineHeight: lengthPx(rootR['line-height']),
  color: colorExpr(rootR.color),
  label: {
    height: lengthPx(labelR.height),
    gap: lengthPx(labelR['margin-bottom'])
  },
  input: {
    height: lengthPx(inputR.height),
    padding: parsePadding(inputR.padding),
    border: parseBorder(inputR.border),
    radius: lengthPx(inputR['border-radius']),
    bg: colorExpr(inputR.background)
  },
  placeholderColor: colorExpr(placeholderR.color),
  inputDisabled: {
    color: colorExpr(inputDisabledR.color),
    borderColor: colorExpr(inputDisabledR['border-color'])
  },
  option: {
    height: lengthPx(optionR.height),
    padding: parsePadding(optionR.padding),
    activeBg: colorExpr(optionActiveR.background),
    disabledColor: colorExpr(optionDisabledR.color)
  },
  status: {
    height: lengthPx(statusR.height),
    gap: lengthPx(statusR['margin-top']),
    fontSize: lengthPx(statusR['font-size']),
    color: colorExpr(statusR.color),
    errorColor: colorExpr(statusErrorR.color)
  },
  surface: {
    gap: lengthPx(surfaceR['margin-top']),
    bg: colorExpr(surfaceR.background),
    radius: lengthPx(surfaceR['border-radius']),
    shadowRaw: surfaceR['box-shadow'],
    shadow: null
  },
  viewportMaxHeight: lengthPx(viewportR['max-height'])
}

// Der box-shadow der Overlayfläche: Rohwert aus der Definition, geparst vom
// Original-Parser (parseCSSShadows). Erwartet wird genau ein Drop-Shadow.
{
  const shadows = parseCSSShadows(V.surface.shadowRaw)
  if (shadows.length !== 1 || shadows[0].type !== 'DROP_SHADOW') {
    throw new Error(`box-shadow der Overlayfläche liest sich nicht als einzelner Drop-Shadow: ${V.surface.shadowRaw}`)
  }
  V.surface.shadow = shadows[0]
}

// --- Teilnamen aus component.json (Anatomie) --------------------------------
// Die Keys von anatomy sind die Teilnamen, die Werte ihre Beschreibung.
const anatomy = component.anatomy
for (const required of ['label', 'input', 'overlay.surface', 'overlay.scroll.viewport', 'list', 'option', 'status']) {
  if (!(required in anatomy)) throw new Error(`Anatomie-Teil fehlt in component.json: ${required}`)
}
const AN = {
  label: 'label',
  input: 'input',
  surface: 'overlay.surface',
  viewport: 'overlay.scroll.viewport',
  list: 'list',
  option: 'option',
  status: 'status',
  content: 'overlay.scroll.content',
  inputText: 'input.query',
  message: 'message'
}

// ---------------------------------------------------------------------------
// 2. Fall-Spezifikation pro Story ableiten
// ---------------------------------------------------------------------------

function renderTemplate(template, vars) {
  return template.replace(/\{(count|label)\}/g, (_, k) => String(vars[k] ?? ''))
}

function deriveCase(story) {
  const phase = story.phase
  const projection = a11y.projections[phase]
  if (!projection) throw new Error(`Keine a11y-Projektion für Phase "${phase}" (Story ${story.id})`)

  const results = story.results ?? []
  const query = story.inputs.query ?? ''
  const disabled = story.inputs.enabled === false
  const popupVisible = projection.popupVisible
  const focused = focusStates.has(phase)

  // Meldung: Phase als Template-Schlüssel; ready → Vorlage "results"
  // ({count}); selected → Vorlage "selected" (label des zu value gehörenden
  // Ergebnisses); disabled → Vorlage "disabled".
  let msgKey = phase
  if (msgKey === 'ready') msgKey = 'results'
  if (story.id === 'selected') msgKey = 'selected'
  if (story.id === 'disabled') msgKey = 'disabled'
  if (!(msgKey in a11y.messages)) throw new Error(`Kein Meldetemplate für "${msgKey}" (Story ${story.id})`)
  const valueLabel = story.value ? results.find((r) => r.key === story.value)?.label : undefined
  const message = renderTemplate(a11y.messages[msgKey], { count: results.length, label: valueLabel })

  const borderColor = disabled ? V.inputDisabled.borderColor : focused ? focusColor : V.input.border.color
  const inputTextColor = disabled
    ? V.inputDisabled.color
    : query !== ''
      ? V.color
      : V.placeholderColor
  const statusColor = phase === 'error' ? V.status.errorColor : V.status.color

  // Geometrie (README "Sichtbare Geometrie" + layout.css):
  // Label oben, danach Input; Popup am Inputende + gap, gleiche Breite/Kante;
  // Viewport min(Anzahl × rowHeight, maxHeight); Meldungszustände eine Zeile;
  // Status nach statusGap unter dem sichtbaren Popup, sonst unter dem Input.
  const w = V.width
  const labelY = 0
  const inputY = V.label.height + V.label.gap
  const inputBottom = inputY + V.input.height
  const popupY = inputBottom + V.surface.gap
  const n = results.length
  const hasList = n > 0
  const listH = n * V.option.height
  const viewportH = hasList ? Math.min(listH, V.viewportMaxHeight) : V.option.height
  const contentH = hasList ? listH : V.option.height
  // scroll-end: Inhalt des geclippten Viewports so versetzen, dass die aktive
  // letzte Option im sichtbaren Viewport liegt (README, Sichtbare Geometrie).
  const offset = story.id === 'scroll-end' && hasList ? Math.max(0, listH - viewportH) : 0
  const statusY = (popupVisible ? popupY + viewportH : inputBottom) + V.status.gap
  const caseH = statusY + V.status.height

  return {
    story,
    id: story.id,
    phase,
    disabled,
    popupVisible,
    results,
    query,
    message,
    label: story.inputs.label,
    placeholder: story.inputs.placeholder,
    value: story.value,
    activeKey: story.activeKey,
    borderColor,
    inputTextColor,
    statusColor,
    w,
    caseH,
    labelY,
    inputY,
    inputBottom,
    popupY,
    listH,
    viewportH,
    contentH,
    offset,
    statusY
  }
}

const specs = stories.map(deriveCase)
for (const s of specs) {
  if (!s.popupVisible && s.offset !== 0) throw new Error(`scroll-end ohne sichtbares Popup? ${s.id}`)
}

// ---------------------------------------------------------------------------
// 3. Designgraph im Speicher aufbauen
// ---------------------------------------------------------------------------

const hex = (c) => {
  const h = (v) => Math.round(v * 255).toString(16).padStart(2, '0')
  return `#${h(c.r)}${h(c.g)}${h(c.b)}${c.a < 1 ? h(c.a) : ''}`
}
const num = (v) => (Number.isInteger(v) ? String(v) : String(Number(v.toFixed(3))))

function caseJsx(spec, x, y) {
  const L = []
  L.push(`<Frame name="Autocomplete/${spec.id}" x={${num(x)}} y={${num(y)}} w={${num(spec.w)}} h={${num(spec.caseH)}}>`)
  L.push(
    `  <Text name="${AN.label}" x={0} y={${num(spec.labelY)}} size={${num(V.fontSize)}} font="${V.fontFamily}" lineHeight={${num(V.lineHeight)}} color="${hex(V.color)}">${spec.label}</Text>`
  )
  L.push(
    `  <Frame name="${AN.input}" x={0} y={${num(spec.inputY)}} w={${num(spec.w)}} h={${num(V.input.height)}} bg="${hex(V.input.bg)}" stroke="${hex(spec.borderColor)}" strokeWidth={${num(V.input.border.width)}} rounded={${num(V.input.radius)}}>`
  )
  L.push(
    `    <Text name="${AN.inputText}" x={${num(V.input.padding.left)}} y={${num((V.input.height - V.lineHeight) / 2)}} size={${num(V.fontSize)}} font="${V.fontFamily}" lineHeight={${num(V.lineHeight)}} color="${hex(spec.inputTextColor)}">${spec.query !== '' ? spec.query : spec.placeholder}</Text>`
  )
  L.push(`  </Frame>`)

  if (spec.popupVisible) {
    L.push(
      `  <Frame name="${AN.surface}" x={0} y={${num(spec.popupY)}} w={${num(spec.w)}} h={${num(spec.viewportH)}} bg="${hex(V.surface.bg)}" rounded={${num(V.surface.radius)}} shadow="${V.surface.shadowRaw}">`
    )
    L.push(
      `    <Frame name="${AN.viewport}" x={0} y={0} w={${num(spec.w)}} h={${num(spec.viewportH)}} overflow="hidden">`
    )
    L.push(
      `      <Frame name="${AN.content}" x={0} y={${num(-spec.offset)}} w={${num(spec.w)}} h={${num(spec.contentH)}}>`
    )
    if (spec.results.length > 0) {
      L.push(`        <Frame name="${AN.list}" x={0} y={0} w={${num(spec.w)}} h={${num(spec.listH)}}>`)
      spec.results.forEach((r, i) => {
        const isActive = spec.activeKey === r.key
        const isDisabled = r.disabled === true
        const bg = isActive ? ` bg="${hex(V.option.activeBg)}"` : ''
        const color = isDisabled ? V.option.disabledColor : V.color
        L.push(
          `          <Frame name="${AN.option}/${r.key}" x={0} y={${num(i * V.option.height)}} w={${num(spec.w)}} h={${num(V.option.height)}}${bg}>`
        )
        L.push(
          `            <Text name="${AN.label}" x={${num(V.option.padding.left)}} y={${num(V.option.padding.top)}} size={${num(V.fontSize)}} font="${V.fontFamily}" lineHeight={${num(V.lineHeight)}} color="${hex(color)}">${r.label}</Text>`
        )
        L.push(`          </Frame>`)
      })
      L.push(`        </Frame>`)
    } else {
      // loading/empty/error: eine Zeile mit der Meldung im Popupinhalt.
      L.push(`        <Frame name="${AN.message}" x={0} y={0} w={${num(spec.w)}} h={${num(V.option.height)}}>`)
      L.push(
        `          <Text name="${AN.label}" x={${num(V.option.padding.left)}} y={${num(V.option.padding.top)}} size={${num(V.fontSize)}} font="${V.fontFamily}" lineHeight={${num(V.lineHeight)}} color="${hex(V.color)}">${spec.message}</Text>`
      )
      L.push(`        </Frame>`)
    }
    L.push(`      </Frame>`)
    L.push(`    </Frame>`)
    L.push(`  </Frame>`)
  }

  L.push(
    `  <Text name="${AN.status}" x={0} y={${num(spec.statusY)}} size={${num(V.status.fontSize)}} font="${V.fontFamily}" lineHeight={${num(V.lineHeight)}} color="${hex(spec.statusColor)}">${spec.message}</Text>`
  )
  L.push(`</Frame>`)
  return L.join('\n')
}

const graph = new SceneGraph()
const page = graph.getPages()[0]
graph.updateNode(page.id, { name: 'Autocomplete' })

// Seitenlayout (frei): Titel oben, Fälle in einem Raster von 5 Spalten.
const MARGIN = 48
const GAP = 64
const TITLE_Y = 48
const TITLE_H = 40
const CASE_START_Y = TITLE_Y + TITLE_H + GAP
const ROW_H = Math.max(...specs.map((s) => s.caseH))
const COLS = 5
const titleJsx = `<Text name="page.title" x={${MARGIN}} y={${TITLE_Y}} size={16} font="${V.fontFamily}" weight={600} color="${hex(V.color)}">Autocomplete — 10 benannte Zustände aus components/autocomplete/stories.json</Text>`

const jsxWarnings = []
const caseRoots = []

{
  const titleResult = await renderJSX(graph, titleJsx, {})
  jsxWarnings.push(...(titleResult.warnings ?? []).map((w) => `title: ${w}`))
}

for (let i = 0; i < specs.length; i++) {
  const spec = specs[i]
  const col = i % COLS
  const row = Math.floor(i / COLS)
  const x = MARGIN + col * (spec.w + GAP)
  const y = CASE_START_Y + row * (ROW_H + GAP)
  const result = await renderJSX(graph, caseJsx(spec, x, y), { x, y })
  jsxWarnings.push(...(result.warnings ?? []).map((w) => `${spec.id}: ${w}`))
  caseRoots.push({ spec, id: result[0].id })
}

function countNodes(g, node) {
  let n = 1
  for (const cid of node.childIds) n += countNodes(g, g.getNode(cid))
  return n
}
const inMemoryNodeCount = graph
  .getPages()
  .reduce((acc, p) => acc + 1 + p.childIds.reduce((a, cid) => a + countNodes(graph, graph.getNode(cid)), 0), 0)

// ---------------------------------------------------------------------------
// 4. .fig mit dem Original-Writer schreiben
// ---------------------------------------------------------------------------

const figBytes = await exportFigFile(graph)
writeFileSync(path.join(OUT_DIR, 'autocomplete.fig'), figBytes)

// ---------------------------------------------------------------------------
// 5. .fig mit dem Original-Reader wieder einlesen (vollständige Population)
// ---------------------------------------------------------------------------

const figBuffer = new ArrayBuffer(figBytes.byteLength)
new Uint8Array(figBuffer).set(figBytes)
const loaded = await parseFigFile(figBuffer, { populate: 'all' })
const loadedPage = loaded.getPages()[0]

// ---------------------------------------------------------------------------
// 6. preview.png (und preview.svg) aus dem Wiedereingelesenen Graphen rendern
// ---------------------------------------------------------------------------

const topIds = loadedPage.childIds
const png = await headlessRenderNodes(loaded, loadedPage.id, topIds, { scale: 2, format: 'PNG' })
if (!png) throw new Error('PNG-Render fehlgeschlagen')
writeFileSync(path.join(OUT_DIR, 'preview.png'), png)

let svg = null
try {
  svg = renderNodesToSVG(loaded, loadedPage.id, topIds)
  if (svg) writeFileSync(path.join(OUT_DIR, 'preview.svg'), svg)
} catch (err) {
  svg = null
}

// ---------------------------------------------------------------------------
// 7. Selbstprüfungen (erwartet vs. tatsächlich, Werte aus der Datei)
// ---------------------------------------------------------------------------

const COLOR_TOL = (1 / 255) * 1.5
const approx = (a, b) => Math.abs(a - b) <= COLOR_TOL
const colorEq = (a, b) => a && b && approx(a.r, b.r) && approx(a.g, b.g) && approx(a.b, b.b) && approx(a.a, b.a)
const colorJson = (c) => c && `${(c.r * 255).toFixed(1)},${(c.g * 255).toFixed(1)},${(c.b * 255).toFixed(1)},${(c.a * 255).toFixed(1)}`

const checks = []
function check(id, description, expected, actual, pass) {
  checks.push({ id, description, expected, actual, pass: Boolean(pass) })
}

const childByName = (node, name) => node.childIds.map((cid) => loaded.getNode(cid)).find((c) => c.name === name)

const figMagic = figBytes[0] === 0x50 && figBytes[1] === 0x4b // "PK" — ZIP-Archiv (.fig-Container)
check('fig.magic', 'autocomplete.fig beginnt mit ZIP-Signatur (PK)', 'PK (0x50 0x4b)', figMagic ? 'PK (0x50 0x4b)' : `Bytes: ${Array.from(figBytes.slice(0, 4)).join(',')}`, figMagic)
check('fig.bytes', 'autocomplete.fig nicht leer', '> 0 Bytes', `${figBytes.byteLength} Bytes`, figBytes.byteLength > 0)

const reimportPages = loaded.getPages()
check('reimport.pages', 'Wiedereingelest: Seitenanzahl', 1, reimportPages.length, reimportPages.length === 1)
check('reimport.page-name', 'Wiedereingelest: Seitename', 'Autocomplete', reimportPages[0]?.name ?? null, reimportPages[0]?.name === 'Autocomplete')

const loadedNodeCount = reimportPages.reduce(
  (acc, p) => acc + 1 + p.childIds.reduce((a, cid) => a + countNodes(loaded, loaded.getNode(cid)), 0),
  0
)
check('reimport.nodes', 'Wiedereingelest: Knotenanzahl entspricht dem Schreibgraphen', inMemoryNodeCount, loadedNodeCount, loadedNodeCount === inMemoryNodeCount)

let imageCount = 0
{
  const walk = (n) => {
    if (n.type === 'IMAGE') imageCount++
    for (const cid of n.childIds) walk(loaded.getNode(cid))
  }
  for (const cid of loadedPage.childIds) walk(loaded.getNode(cid))
}
check('reimport.no-images', 'Keine eingebetteten Rasternodes (echtes editierbares Design)', 0, imageCount, imageCount === 0)

let frameCount = 0
let textCount = 0
{
  const walk = (n) => {
    if (n.type === 'FRAME') frameCount++
    if (n.type === 'TEXT') textCount++
    for (const cid of n.childIds) walk(loaded.getNode(cid))
  }
  for (const cid of loadedPage.childIds) walk(loaded.getNode(cid))
}
check('reimport.types', 'Design besteht aus Frames und Texten (editierbar)', { FRAME: `>= 10`, TEXT: `>= 20` }, { FRAME: frameCount, TEXT: textCount }, frameCount >= 10 && textCount >= 20)

const caseRootByName = (id) => loadedPage.childIds.map((cid) => loaded.getNode(cid)).find((c) => c.name === `Autocomplete/${id}`)

for (const spec of specs) {
  const prefix = `case.${spec.id}`
  const root = caseRootByName(spec.id)
  if (!root) {
    check(`${prefix}.frame`, 'Fall-Frame vorhanden', `Autocomplete/${spec.id}`, 'fehlt', false)
    continue
  }
  const expPos = { x: MARGIN + (specs.indexOf(spec) % COLS) * (spec.w + GAP), y: CASE_START_Y + Math.floor(specs.indexOf(spec) / COLS) * (ROW_H + GAP) }
  check(
    `${prefix}.frame`,
    'Fall-Frame: Größe und Position',
    { w: spec.w, h: spec.caseH, x: expPos.x, y: expPos.y },
    { w: root.width, h: root.height, x: root.x, y: root.y },
    root.width === spec.w && root.height === spec.caseH && root.x === expPos.x && root.y === expPos.y
  )

  const label = childByName(root, AN.label)
  check(
    `${prefix}.label`,
    'Label: Text, Position, Typo, Farbe',
    { text: spec.label, x: 0, y: spec.labelY, h: V.label.height, fontSize: V.fontSize, fontFamily: V.fontFamily, color: colorJson(V.color) },
    label && { text: label.text, x: label.x, y: label.y, h: label.height, fontSize: label.fontSize, fontFamily: label.fontFamily, color: label.fills[0] ? colorJson(label.fills[0].color) : null },
    label && label.text === spec.label && label.x === 0 && label.y === spec.labelY && label.height === V.label.height && label.fontSize === V.fontSize && label.fontFamily === V.fontFamily && (label.fills[0] ? colorEq(label.fills[0].color, V.color) : false)
  )

  const input = childByName(root, AN.input)
  const inputStroke = input?.strokes?.[0]
  check(
    `${prefix}.input`,
    'Input: Box, Randfarbe (Zustand), Radius, Füllung',
    { x: 0, y: spec.inputY, w: spec.w, h: V.input.height, radius: V.input.radius, borderWidth: V.input.border.width, borderColor: colorJson(spec.borderColor), fill: colorJson(V.input.bg) },
    input && { x: input.x, y: input.y, w: input.width, h: input.height, radius: input.cornerRadius, borderWidth: inputStroke?.weight ?? null, borderColor: inputStroke ? colorJson(inputStroke.color) : null, fill: input.fills[0] ? colorJson(input.fills[0].color) : null },
    input &&
      input.x === 0 &&
      input.y === spec.inputY &&
      input.width === spec.w &&
      input.height === V.input.height &&
      input.cornerRadius === V.input.radius &&
      inputStroke?.weight === V.input.border.width &&
      (inputStroke ? colorEq(inputStroke.color, spec.borderColor) : false) &&
      (input.fills[0] ? colorEq(input.fills[0].color, V.input.bg) : false)
  )

  const inputText = input ? childByName(input, AN.inputText) : null
  const expectedInputText = spec.query !== '' ? spec.query : spec.placeholder
  check(
    `${prefix}.input.text`,
    'Input-Text: Inhalt (Query oder Placeholder) und Farbe',
    { text: expectedInputText, color: colorJson(spec.inputTextColor), x: V.input.padding.left, y: (V.input.height - V.lineHeight) / 2 },
    inputText && { text: inputText.text, color: inputText.fills[0] ? colorJson(inputText.fills[0].color) : null, x: inputText.x, y: inputText.y },
    inputText &&
      inputText.text === expectedInputText &&
      inputText.x === V.input.padding.left &&
      inputText.y === (V.input.height - V.lineHeight) / 2 &&
      (inputText.fills[0] ? colorEq(inputText.fills[0].color, spec.inputTextColor) : false)
  )

  if (spec.popupVisible) {
    const surface = childByName(root, AN.surface)
    const shadow = surface?.effects?.find((e) => e.type === 'DROP_SHADOW')
    check(
      `${prefix}.surface`,
      'Overlayfläche: Position (Inputende + gap), Größe, Radius, Füllung, Schatten',
      { x: 0, y: spec.popupY, w: spec.w, h: spec.viewportH, radius: V.surface.radius, fill: colorJson(V.surface.bg), shadow: { x: V.surface.shadow.offset.x, y: V.surface.shadow.offset.y, radius: V.surface.shadow.radius, color: colorJson(V.surface.shadow.color) } },
      surface && { x: surface.x, y: surface.y, w: surface.width, h: surface.height, radius: surface.cornerRadius, fill: surface.fills[0] ? colorJson(surface.fills[0].color) : null, shadow: shadow ? { x: shadow.offset?.x, y: shadow.offset?.y, radius: shadow.radius, color: colorJson(shadow.color) } : null },
      surface &&
        surface.x === 0 &&
        surface.y === spec.popupY &&
        surface.width === spec.w &&
        surface.height === spec.viewportH &&
        surface.cornerRadius === V.surface.radius &&
        (surface.fills[0] ? colorEq(surface.fills[0].color, V.surface.bg) : false) &&
        shadow &&
        shadow.offset?.x === V.surface.shadow.offset.x &&
        shadow.offset?.y === V.surface.shadow.offset.y &&
        shadow.radius === V.surface.shadow.radius &&
        colorEq(shadow.color, V.surface.shadow.color)
    )

    const viewport = surface ? childByName(surface, AN.viewport) : null
    check(
      `${prefix}.viewport`,
      'Scrollviewport: Clipping aktiv, Größe min(n × rowHeight, maxHeight) bzw. eine Zeile',
      { clips: true, w: spec.w, h: spec.viewportH },
      viewport && { clips: viewport.clipsContent, w: viewport.width, h: viewport.height },
      viewport && viewport.clipsContent === true && viewport.width === spec.w && viewport.height === spec.viewportH
    )

    const content = viewport ? childByName(viewport, AN.content) : null
    check(
      `${prefix}.content`,
      'Scrollinhalt: Versatz (scroll-end zeigt die letzte Option), Größe',
      { x: 0, y: -spec.offset, w: spec.w, h: spec.contentH },
      content && { x: content.x, y: content.y, w: content.width, h: content.height },
      content && content.x === 0 && content.y === -spec.offset && content.width === spec.w && content.height === spec.contentH
    )

    if (spec.results.length > 0) {
      const list = content ? childByName(content, AN.list) : null
      const options = list ? list.childIds.map((cid) => loaded.getNode(cid)) : []
      check(
        `${prefix}.list`,
        'Listbox: Höhe = n × rowHeight, alle Optionen vorhanden (auch geclippte)',
        { w: spec.w, h: spec.listH, options: spec.results.length },
        list && { w: list.width, h: list.height, options: options.length },
        list && list.width === spec.w && list.height === spec.listH && options.length === spec.results.length
      )
      spec.results.forEach((r, i) => {
        const opt = options.find((o) => o.name === `${AN.option}/${r.key}`)
        const isActive = spec.activeKey === r.key
        const isDisabled = r.disabled === true
        const optFill = opt?.fills?.[0]
        const optText = opt ? childByName(opt, AN.label) : null
        const expFill = isActive ? V.option.activeBg : null
        const expTextColor = isDisabled ? V.option.disabledColor : V.color
        const optAbsY = surface.y + content.y + i * V.option.height
        const visible = optAbsY >= surface.y && optAbsY + V.option.height <= surface.y + spec.viewportH
        check(
          `${prefix}.option.${r.key}`,
          `Option ${r.key}: Position, ${isActive ? 'aktive Hervorhebung' : 'keine Hervorhebung'}${isDisabled ? ', deaktivierte Farbe' : ''}${spec.id === 'scroll-end' && i === spec.results.length - 1 ? ', im sichtbaren Viewport' : ''}`,
          { y: i * V.option.height, h: V.option.height, text: r.label, fill: expFill ? colorJson(expFill) : null, textColor: colorJson(expTextColor) },
          opt && { y: opt.y, h: opt.height, text: optText?.text ?? null, fill: optFill ? colorJson(optFill.color) : null, textColor: optText?.fills?.[0] ? colorJson(optText.fills[0].color) : null },
          opt &&
            opt.y === i * V.option.height &&
            opt.height === V.option.height &&
            optText?.text === r.label &&
            (expFill ? (optFill ? colorEq(optFill.color, expFill) : false) : (optFill ? false : true)) &&
            (optText?.fills?.[0] ? colorEq(optText.fills[0].color, expTextColor) : false) &&
            (spec.id === 'scroll-end' && i === spec.results.length - 1 ? visible === true : true)
        )
      })
    } else {
      const message = content ? childByName(content, AN.message) : null
      const messageText = message ? childByName(message, AN.label) : null
      check(
        `${prefix}.message`,
        'Meldungszeile im Popup: Inhalt und Zeilenhöhe',
        { text: spec.message, h: V.option.height },
        message && { text: messageText?.text ?? null, h: message.height },
        message && message.height === V.option.height && messageText?.text === spec.message
      )
    }
  } else {
    check(
      `${prefix}.no-popup`,
      'Kein Popup in diesem Zustand (keine Popupteile)',
      'keine Kinder surface',
      childByName(root, AN.surface) ? 'surface vorhanden' : 'keine surface',
      !childByName(root, AN.surface)
    )
  }

  const status = childByName(root, AN.status)
  check(
    `${prefix}.status`,
    'Status: Text (Meldung), Farbe, Position unter Popup bzw. Input',
    { text: spec.message, color: colorJson(spec.statusColor), x: 0, y: spec.statusY, h: V.status.height, fontSize: V.status.fontSize },
    status && { text: status.text, color: status.fills[0] ? colorJson(status.fills[0].color) : null, x: status.x, y: status.y, h: status.height, fontSize: status.fontSize },
    status &&
      status.text === spec.message &&
      status.x === 0 &&
      status.y === spec.statusY &&
      status.height === V.status.height &&
      status.fontSize === V.status.fontSize &&
      (status.fills[0] ? colorEq(status.fills[0].color, spec.statusColor) : false)
  )
}

const pngOk = png[0] === 0x89 && png[1] === 0x50 && png[2] === 0x4e && png[3] === 0x47
check('preview.png', 'preview.png: PNG aus dem wiedereingelesenen Graphen (Scale 2)', 'PNG-Magic + > 0 Bytes', `${png.length} Bytes`, pngOk && png.length > 0)
check('preview.svg', 'preview.svg: SVG-Render aus dem wiedereingelesenen Graphen', svg ? `> 0 Zeichen` : 'nicht erzeugt (nicht kritisch)', svg ? `${svg.length} Zeichen` : 'fehlt', Boolean(svg))

if (jsxWarnings.length > 0) {
  check('render.warnings', 'renderJSX-Warnungen (unbekannte Props u. a.)', 'keine', jsxWarnings, false)
} else {
  check('render.warnings', 'renderJSX-Warnungen (unbekannte Props u. a.)', 'keine', 'keine', true)
}

const failed = checks.filter((c) => !c.pass)
const checksDoc = {
  component: { id: component.id, version: component.version },
  tool: { versions: TOOL_VERSIONS, writer: 'exportFigFile (@open-pencil/core/io)', reader: 'parseFigFile (@open-pencil/core/io, populate=all)' },
  summary: { total: checks.length, passed: checks.length - failed.length, failed: failed.length },
  artifacts: {
    'autocomplete.fig': `${figBytes.byteLength} Bytes`,
    'preview.png': `${png.length} Bytes`,
    'preview.svg': svg ? `${svg.length} Zeichen` : null
  },
  nodes: { written: inMemoryNodeCount, reimported: loadedNodeCount, frames: frameCount, texts: textCount },
  checks
}
writeFileSync(path.join(OUT_DIR, 'checks.json'), JSON.stringify(checksDoc, null, 2) + '\n')

// ---------------------------------------------------------------------------
// 8. source-sha256.json (frisch berechnete SHA-256 der Definitionsdateien)
// ---------------------------------------------------------------------------

function walkDir(dir) {
  const out = []
  for (const entry of readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) out.push(...walkDir(full))
    else if (entry.isFile()) out.push(full)
  }
  return out
}
const defFiles = walkDir(COMPONENTS_DIR).map((full) => ({
  path: path.relative(REPO_ROOT, full).split(path.sep).join('/'),
  sha256: createHash('sha256').update(readFileSync(full)).digest('hex'),
  bytes: statSync(full).size
}))
writeFileSync(
  path.join(OUT_DIR, 'source-sha256.json'),
  JSON.stringify({ root: 'components/', files: defFiles }, null, 2) + '\n'
)

// ---------------------------------------------------------------------------
// Zusammenfassung
// ---------------------------------------------------------------------------

console.log('component:', component.id, component.version)
console.log('stories:', stories.length)
console.log('fig:', figBytes.byteLength, 'Bytes')
console.log('nodes (geschrieben / wiedereingelesen):', inMemoryNodeCount, '/', loadedNodeCount)
console.log('preview.png:', png.length, 'Bytes; preview.svg:', svg ? `${svg.length} Zeichen` : 'nicht erzeugt')
console.log('checks:', checksDoc.summary.passed, 'bestanden,', checksDoc.summary.failed, 'fehlgeschlagen von', checksDoc.summary.total)
for (const c of failed) console.log('  FEHLSCHLAG:', c.id, JSON.stringify(c.expected), '≠', JSON.stringify(c.actual))
if (failed.length > 0) process.exit(1)
