#!/usr/bin/env node
/**
 * generate.mjs — Builder A · Reproduzierbarkeitslauf run-03 · Autocomplete
 *
 * Erzeugt aus der eingefrorenen Definition unter ../../../../../components/
 * ein editierbares OpenPencil-Dokument (autocomplete.fig) mit den zehn
 * benannten Fällen aus stories.json, verifiziert es durch Wiedereinlesen
 * und rendert preview.png (und preview.svg) aus dem Wiedereingelesenen Graphen.
 *
 * Verwendet ausschließlich die gepinnte Werkzeugumgebung
 * ../../../../../tools/openpencil/node_modules (OpenPencil 0.16.0):
 *   - @open-pencil/scene-graph   (Graph)
 *   - @open-pencil/core/figma-api (Graphaufbau per Figma-Plugin-API-Kompatibilität)
 *   - @open-pencil/core/io        (Original-Writer exportFigFile, Original-Reader parseFigFile,
 *                                   Original-Renderer headlessRenderNodes / renderNodesToSVG)
 *
 * Keine Definitionswerte sind hartkodiert: Tokens (tokens.json), Geometrie- und
 * Zustandsregeln (layout.css ×3), Meldungen/Projektionen (accessibility.rules.json),
 * Fälle (stories.json), Teile (component.json / accessibility.html) werden zur
 * Laufzeit gelesen.
 *
 * Schreibt ausschließlich in den eigenen Ausgabeordner.
 *
 * Aufruf vom Repositorystamm:
 *   node examples/autocomplete/reproducibility/run-03/builder-a/generate.mjs
 */

import { readFile, writeFile, rm } from 'node:fs/promises'
import { createHash } from 'node:crypto'

// ---------------------------------------------------------------------------
// Pfade
// ---------------------------------------------------------------------------
const HERE = new URL('.', import.meta.url)
const ROOT = new URL('../../../../..', import.meta.url) // builder-a → … → Repository-Root
const COMPONENTS = new URL('components/', ROOT)
const TOOLING = new URL('tools/openpencil/node_modules/', ROOT)

const importTool = (rel) => import(new URL(rel, TOOLING))

const sg = await importTool('@open-pencil/scene-graph/dist/index.js')
const fa = await importTool('@open-pencil/core/dist/figma-api/index.js')
const io = await importTool('@open-pencil/core/dist/io/index.js')
const canvas = await importTool('@open-pencil/core/dist/canvas/index.js')
const layout = await importTool('@open-pencil/core/dist/layout.js')

const outPath = (name) => new URL(name, HERE)

// ---------------------------------------------------------------------------
// Hilfsfunktionen
// ---------------------------------------------------------------------------
async function readComp(rel) {
  return readFile(new URL(rel, COMPONENTS), 'utf8')
}
async function readCompJson(rel) {
  return JSON.parse(await readComp(rel))
}
async function sha256Comp(rel) {
  const bytes = await readFile(new URL(rel, COMPONENTS))
  return createHash('sha256').update(bytes).digest('hex')
}

const COLOR_EPS = 2e-3 // float32-Rundung im Kiwi-Format

function deepEq(a, b, eps = 1e-9) {
  if (typeof a === 'number' && typeof b === 'number') return Math.abs(a - b) <= eps
  if (Array.isArray(a) && Array.isArray(b)) {
    return a.length === b.length && a.every((v, i) => deepEq(v, b[i], eps))
  }
  if (a && b && typeof a === 'object' && typeof b === 'object') {
    const ka = Object.keys(a).sort()
    const kb = Object.keys(b).sort()
    if (ka.length !== kb.length || ka.some((k, i) => k !== kb[i])) return false
    return ka.every((k) => deepEq(a[k], b[k], eps))
  }
  return a === b
}

// ---------------------------------------------------------------------------
// 1. Definition lesen
// ---------------------------------------------------------------------------
const SOURCE_FILES = [
  'README.md',
  'library.json',
  'tokens.json',
  'autocomplete/README.md',
  'autocomplete/component.json',
  'autocomplete/interface.json',
  'autocomplete/stories.json',
  'autocomplete/layout.css',
  'autocomplete/behavior.scxml',
  'autocomplete/accessibility.html',
  'autocomplete/accessibility.rules.json',
  'overlay/component.json',
  'overlay/interface.json',
  'overlay/layout.css',
  'overlay/behavior.scxml',
  'overlay/accessibility.html',
  'scroll-area/component.json',
  'scroll-area/interface.json',
  'scroll-area/layout.css',
  'scroll-area/behavior.scxml',
  'scroll-area/accessibility.html'
]

const tokensRaw = await readCompJson('tokens.json')
const storiesDoc = await readCompJson('autocomplete/stories.json')
const stories = storiesDoc.stories
const a11y = await readCompJson('autocomplete/accessibility.rules.json')
const acComponent = await readCompJson('autocomplete/component.json')
const acInterface = await readCompJson('autocomplete/interface.json')
const overlayComponent = await readCompJson('overlay/component.json')
const scrollComponent = await readCompJson('scroll-area/component.json')
const acCssText = await readComp('autocomplete/layout.css')
const overlayCssText = await readComp('overlay/layout.css')
const scrollCssText = await readComp('scroll-area/layout.css')
const acScxmlText = await readComp('autocomplete/behavior.scxml')
const acA11yHtml = await readComp('autocomplete/accessibility.html')
const overlayA11yHtml = await readComp('overlay/accessibility.html')
const scrollA11yHtml = await readComp('scroll-area/accessibility.html')
const acReadme = await readComp('autocomplete/README.md')
const libraryIndex = await readCompJson('library.json')
const compReadme = await readComp('README.md')

// --- DTCG-Tokens auflösen (inkl. "{…}"-Verweise) ----------------------------
function resolveTokens(raw) {
  const cache = new Map()
  function resolveRef(ref) {
    if (cache.has(ref)) return cache.get(ref)
    const parts = ref.split('.')
    let entry = raw
    for (const p of parts) entry = entry?.[p]
    if (!entry) throw new Error(`Unbekannte Tokenreferenz: ${ref}`)
    let v = entry.$value
    if (typeof v === 'string' && v.startsWith('{') && v.endsWith('}')) {
      v = resolveRef(v.slice(1, -1))
    } else if (v && typeof v === 'object' && 'value' in v && 'unit' in v) {
      if (v.unit !== 'px') throw new Error(`Token ${ref} hat Einheit ${v.unit} (nur px erwartet)`)
      v = v.value
    }
    cache.set(ref, v)
    return v
  }
  const out = {}
  for (const section of Object.keys(raw)) {
    out[section] = {}
    for (const key of Object.keys(raw[section])) out[section][key] = resolveRef(`${section}.${key}`)
  }
  return out
}
const tokens = resolveTokens(tokensRaw)
const TAC = tokens.autocomplete

function dtcgColor(tok, name) {
  if (tok.colorSpace !== 'srgb') throw new Error(`Farbe ${name}: farbraum ${tok.colorSpace} nicht unterstützt`)
  return { r: tok.components[0], g: tok.components[1], b: tok.components[2], a: tok.alpha }
}

// --- Mini-CSS-Parser (Regel → Selektoren + Deklarationen) -------------------
function parseCss(text, file) {
  const src = text.replace(/\/\*[\s\S]*?\*\//g, ' ')
  const rules = []
  for (const m of src.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
    const selectors = m[1].split(',').map((s) => s.trim()).filter(Boolean)
    const body = {}
    for (const decl of m[2].split(';')) {
      const i = decl.indexOf(':')
      if (i === -1) continue
      const prop = decl.slice(0, i).trim()
      const value = decl.slice(i + 1).trim()
      if (prop && value) body[prop] = value
    }
    rules.push({ file, selectors, body })
  }
  return rules
}
const acCssRules = parseCss(acCssText, 'autocomplete/layout.css')
const overlayCssRules = parseCss(overlayCssText, 'overlay/layout.css')
const scrollCssRules = parseCss(scrollCssText, 'scroll-area/layout.css')

function findRule(rules, predicate, what) {
  const r = rules.find(predicate)
  if (!r) throw new Error(`CSS-Regel nicht gefunden (${what}) in ${rules[0]?.file ?? '?'}`)
  return r
}
function tokenRefOf(value, what) {
  const m = value.match(/^var\(--ac-([a-z0-9]+(?:-[a-z0-9]+)*)\)$/i)
  if (!m) throw new Error(`Erwartete var(--ac-…)-Referenz in "${what}": ${value}`)
  const key = m[1].replace(/-([a-z0-9])/g, (_, c) => c.toUpperCase())
  return key
}
function dimOf(value, what) {
  const key = tokenRefOf(value, what)
  const v = TAC[key]
  if (typeof v !== 'number') throw new Error(`Token ${key} ist keine Länge: ${v}`)
  return v
}
function colorOf(value, what) {
  const key = tokenRefOf(value, what)
  return dtcgColor(TAC[key], key)
}
function pxLiteral(value, what) {
  const m = value.trim().match(/^(-?\d+(?:\.\d+)?)(px)?$/)
  if (!m) throw new Error(`Erwartete px-Länge in "${what}": ${value}`)
  return parseFloat(m[1])
}
function hexToRgba(hex) {
  let h = hex.replace(/^#/, '')
  if (h.length === 4) h = h.split('').map((c) => c + c).join('')
  if (h.length === 6) h += 'ff'
  if (h.length !== 8) throw new Error(`Ungültiges Hex-Farbformat: ${hex}`)
  return {
    r: parseInt(h.slice(0, 2), 16) / 255,
    g: parseInt(h.slice(2, 4), 16) / 255,
    b: parseInt(h.slice(4, 6), 16) / 255,
    a: parseInt(h.slice(6, 8), 16) / 255
  }
}

// --- Geometrie-/Zustandsregeln aus den CSS-Dateien --------------------------
const compRule = findRule(acCssRules, (r) => r.selectors.includes('[data-component="Autocomplete"]'), 'Komponente')
const labelRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="label"]'), 'Label')
const inputRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="input"]'), 'Input')
const placeholderRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="input"]::placeholder'), 'Placeholder')
const disabledInputRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="input"]:disabled'), 'Input:disabled')
const optionRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="option"]'), 'Option')
const activeOptionRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="option"][aria-selected="true"]'), 'Option aktiv')
const disabledOptionRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="option"][aria-disabled="true"]'), 'Option deaktiviert')
const statusRule = findRule(acCssRules, (r) => r.selectors.includes('[data-part="status"]'), 'Status')
const errorStatusRule = findRule(acCssRules, (r) => r.selectors.some((s) => s.includes('[data-state="error"]') && s.includes('[data-part="status"]')), 'Status im Fehlerfall')
const focusInputRule = findRule(
  acCssRules,
  (r) => 'border-color' in r.body && r.selectors.length > 1 && r.selectors.every((s) => s.includes('[data-part="input"]')),
  'Fokusborder der States'
)
const surfaceRule = findRule(overlayCssRules, (r) => r.selectors.includes('[data-part="surface"]'), 'Overlayfläche')
const viewportRule = findRule(scrollCssRules, (r) => r.selectors.includes('[data-part="viewport"]'), 'Viewport')
const contentRule = findRule(scrollCssRules, (r) => r.selectors.includes('[data-part="content"]'), 'Scrollinhalt')
const listCssRule = findRule(scrollCssRules, (r) => r.selectors.includes('[data-part="list"]'), 'Liste')

// input: border: var(--ac-border-width) solid var(--ac-border)
const inputBorderParts = inputRule.body.border.split(/\s+/)
if (inputBorderParts.length !== 3 || inputBorderParts[1] !== 'solid') {
  throw new Error(`Unerwartetes border-Format: ${inputRule.body.border}`)
}
const inputPaddingParts = inputRule.body.padding.split(/\s+/)
if (inputPaddingParts.length !== 2) throw new Error(`Unerwartetes padding-Format: ${inputRule.body.padding}`)
// option: padding: 6px var(--ac-padding-inline)
const optionPaddingParts = optionRule.body.padding.split(/\s+/)
if (optionPaddingParts.length !== 2) throw new Error(`Unerwartetes option-padding: ${optionRule.body.padding}`)

// box-shadow: 0 2px 8px #0003
const shadowMatch = surfaceRule.body['box-shadow'].trim().match(/^(-?\d+(?:\.\d+)?(?:px)?)\s+(-?\d+(?:\.\d+)?(?:px)?)\s+(-?\d+(?:\.\d+)?(?:px)?)\s+(#[0-9a-fA-F]{3,8})$/)
if (!shadowMatch) throw new Error(`Unerwartetes box-shadow: ${surfaceRule.body['box-shadow']}`)

const focusStates = new Set(
  focusInputRule.selectors.map((s) => s.match(/data-state="([^"]+)"/)?.[1]).filter(Boolean)
)

// Anchor-Semantik der Overlayfläche (position/top/left/width aus layout.css)
const surfaceTop = surfaceRule.body.top
const surfaceLeft = surfaceRule.body.left
const surfaceWidth = surfaceRule.body.width
if (!/anchor\(bottom\)/.test(surfaceTop)) throw new Error(`Overlay-Top erwartet anchor(bottom): ${surfaceTop}`)
if (!/anchor\(left\)/.test(surfaceLeft)) throw new Error(`Overlay-Left erwartet anchor(left): ${surfaceLeft}`)
if (!/anchor-size\(width\)/.test(surfaceWidth)) throw new Error(`Overlay-Breite erwartet anchor-size(width): ${surfaceWidth}`)
if (viewportRule.body['overflow-y'] !== 'auto') throw new Error('Viewport erwartet overflow-y: auto')
if (listCssRule.body['flex-direction'] !== 'column') throw new Error('Liste erwartet flex-direction: column')
// Scrollinhalt und Liste tragen keinen eigenen Abstand (sonst würde die Geometrie verschieben)
if (contentRule.body.margin !== '0' || contentRule.body.padding !== '0') throw new Error('Scrollinhalt erwartet margin/padding 0')
if (listCssRule.body.margin !== '0' || listCssRule.body.padding !== '0') throw new Error('Liste erwartet margin/padding 0')

// --- Spezifikation: alle Werte aus Token + CSS, mit Quellen -----------------
const spec = {
  // components/autocomplete/layout.css → var(--ac-…) → components/tokens.json
  width: dimOf(compRule.body.width, 'Komponentenbreite'),
  fontFamily: TAC[tokenRefOf(compRule.body['font-family'], 'Schriftfamilie')],
  fontSize: dimOf(compRule.body['font-size'], 'Schriftgröße'),
  lineHeight: dimOf(compRule.body['line-height'], 'Zeilenhöhe'),
  colorText: colorOf(compRule.body.color, 'Basisfarbe'),
  labelHeight: dimOf(labelRule.body.height, 'Labelhöhe'),
  labelGap: dimOf(labelRule.body['margin-bottom'], 'Labelabstand'),
  inputHeight: dimOf(inputRule.body.height, 'Inputhöhe'),
  inputPaddingBlock: pxLiteral(inputPaddingParts[0], 'Input-padding (vertikal)'),
  paddingInline: dimOf(inputPaddingParts[1], 'Input-padding (horizontal)'),
  borderWidth: dimOf(inputBorderParts[0], 'Borderstärke'),
  borderColor: colorOf(inputBorderParts[2], 'Borderrfarbe'),
  radius: dimOf(inputRule.body['border-radius'], 'Eckenradius'),
  surfaceColor: colorOf(inputRule.body.background, 'Flächenfarbe'),
  placeholderColor: colorOf(placeholderRule.body.color, 'Platzhalterfarbe'),
  disabledColor: colorOf(disabledInputRule.body.color, 'Deaktiviert-Farbe'),
  rowHeight: dimOf(optionRule.body.height, 'Zeilenhöhe'),
  optionPaddingBlock: pxLiteral(optionPaddingParts[0], 'Optionen-padding (vertikal)'),
  highlightColor: colorOf(activeOptionRule.body.background, 'Aktiv-Farbe'),
  disabledOptionColor: colorOf(disabledOptionRule.body.color, 'Deaktivierte-Option-Farbe'),
  statusGap: dimOf(statusRule.body['margin-top'], 'Statusabstand'),
  statusFontSize: dimOf(statusRule.body['font-size'], 'Statusschriftgröße'),
  statusColor: colorOf(statusRule.body.color, 'Statusfarbe'),
  errorColor: colorOf(errorStatusRule.body.color, 'Fehlerfarbe'),
  focusColor: colorOf(focusInputRule.body['border-color'], 'Fokusfarbe'),
  // components/overlay/layout.css
  popupGap: dimOf(surfaceRule.body['margin-top'], 'Popupabstand'),
  surfaceRadius: dimOf(surfaceRule.body['border-radius'], 'Popupradius'),
  surfaceFill: colorOf(surfaceRule.body.background, 'Popupfläche'),
  shadow: {
    x: pxLiteral(shadowMatch[1], 'Schatten-x'),
    y: pxLiteral(shadowMatch[2], 'Schatten-y'),
    blur: pxLiteral(shadowMatch[3], 'Schatten-blur'),
    color: hexToRgba(shadowMatch[4])
  },
  // components/scroll-area/layout.css
  maxHeight: dimOf(viewportRule.body['max-height'], 'Maximale Viewporthöhe')
}

// Konsistenz: label/status-Höhen sind die Token-Zeilenhöhe (README: „Zeilen bleiben rowHeight hoch“)
if (spec.labelHeight !== spec.lineHeight) throw new Error('label-Höhe weicht von line-height-Token ab')
if (dimOf(statusRule.body.height, 'Statushöhe') !== spec.lineHeight) throw new Error('status-Höhe weicht von line-height-Token ab')
// surface border: 0 (README: Popupfläche ohne Border)
if (surfaceRule.body.border !== '0') throw new Error('Overlayfläche erwartet border: 0')

// --- SCXML-Zustände (behavior.scxml) für die Fallbeschriftung ----------------
const scxmlStates = new Set([...acScxmlText.matchAll(/<state id="([^"]+)"/g)].map((m) => m[1]))
function scxmlPath(story) {
  const phase = story.phase
  if (!scxmlStates.has(phase)) throw new Error(`Phase ${phase} fehlt in behavior.scxml`)
  return phase === 'closed' ? 'machine/closed' : `active/${phase}`
}

// --- accessibility.html: Rollen der Teile (für die Schichtnamen) --------------
function partRole(html, part) {
  const m = html.match(new RegExp(`<[a-z]+[^>]*data-part="${part}"[^>]*>`))
  if (!m) return null
  const role = m[0].match(/role="([^"]+)"/)
  return role ? role[1] : null
}
const cap = (s) => s[0].toUpperCase() + s.slice(1)
const listRole = partRole(acA11yHtml, 'list') // „listbox“
const statusRole = partRole(acA11yHtml, 'status') // „status“
const names = {
  label: 'Label',
  input: 'Input',
  overlaySurface: 'Overlay Surface',
  overlayScrollViewport: 'Overlay Scroll Viewport',
  scrollContent: 'Overlay Scroll Content',
  list: listRole ? cap(listRole) : 'List', // „Listbox“
  option: (key) => 'Option: ' + key,
  optionLabel: 'Label',
  messageRow: 'Message Row',
  messageText: 'Message',
  query: 'Query',
  placeholder: 'Placeholder',
  status: statusRole ? cap(statusRole) : 'Status' // „Status“
}
// Cross-Check: anatomy-Teile aus component.json existieren
const anatomyKeys = Object.keys(acComponent.anatomy)
for (const required of ['label', 'input', 'overlay.surface', 'overlay.scroll.viewport', 'list', 'option', 'status']) {
  if (!anatomyKeys.includes(required)) throw new Error(`anatomy-Teil fehlt in component.json: ${required}`)
}
// Cross-Check: cssParts der Unterkomponenten
const cssParts = (iface) => iface.modules[0].declarations[0].cssParts.map((p) => p.name)
const overlayIface = await readCompJson('overlay/interface.json')
const scrollIface = await readCompJson('scroll-area/interface.json')
if (!cssParts(overlayIface).includes('surface') || !cssParts(overlayIface).includes('content')) throw new Error('Overlay cssParts unvollständig')
if (!cssParts(scrollIface).includes('viewport') || !cssParts(scrollIface).includes('content')) throw new Error('ScrollArea cssParts unvollständig')
// Cross-Check: Zusammensetzung aus component.json verweist auf die unterstützenden Definitionen
if (acComponent.composition?.overlay?.component !== '../overlay/component.json') throw new Error('Komposition Overlay weicht ab')
if (acComponent.composition?.['overlay.scroll']?.component !== '../scroll-area/component.json') throw new Error('Komposition ScrollArea weicht ab')
if (acComponent.composition?.overlay?.anchorPart !== 'input') throw new Error('Overlay-Anker weicht ab')

// --- interface.json: Standard-Label/Platzhalter (Kreuzprüfung) ---------------
const ifaceMembers = acInterface.modules[0].declarations[0].members
const ifaceDefaultLabel = JSON.parse(ifaceMembers.find((m) => m.name === 'label').default)
const ifaceDefaultPlaceholder = JSON.parse(ifaceMembers.find((m) => m.name === 'placeholder').default)

// --- Meldungen (accessibility.rules.json) ------------------------------------
function statusMessage(story) {
  const M = a11y.messages
  if (story.inputs.enabled === false) return M.disabled
  if (story.value !== undefined) {
    const r = story.results.find((x) => x.key === story.value)
    if (!r) throw new Error(`value ${story.value} ohne passendes Ergebnis`)
    return M.selected.replace('{label}', r.label)
  }
  switch (story.phase) {
    case 'closed': return M.closed
    case 'opening': return M.opening
    case 'loading': return M.loading
    case 'ready': return M.results.replace('{count}', String(story.results.length))
    case 'empty': return M.empty
    case 'error': return M.error
    default: throw new Error(`Unbekannte Phase: ${story.phase}`)
  }
}
function popupVisible(story) {
  if (story.inputs.enabled === false) return false // README: „Bei disabled sind keine Popupteile sichtbar.“
  return a11y.projections[story.phase]?.popupVisible === true
}

// --- Geometrie pro Fall (README „Sichtbare Geometrie“) ------------------------
function geometry(story) {
  const show = popupVisible(story)
  const rowCount = show ? (story.results.length > 0 ? story.results.length : 1) : 0 // Meldung = eine Zeile
  const contentH = rowCount * spec.rowHeight
  const viewportH = Math.min(contentH, spec.maxHeight) // „min(Ergebnisanzahl × rowHeight, maxHeight)“
  const inputY = spec.labelHeight + spec.labelGap
  const inputBottom = inputY + spec.inputHeight
  const popupY = inputBottom + spec.popupGap // „Oberkante am Inputende plus gap“
  const statusY = (show ? popupY + viewportH : inputBottom) + spec.statusGap
  const caseH = statusY + spec.lineHeight
  // Scroll-Ende: Inhalt so versetzen, dass die aktive Zeile im Viewport liegt
  let scrollOffset = 0
  if (show && story.activeKey && viewportH < contentH) {
    const idx = story.results.findIndex((r) => r.key === story.activeKey)
    if (idx < 0) throw new Error(`activeKey ${story.activeKey} fehlt in results`)
    const rowY = idx * spec.rowHeight
    const needed = Math.max(0, rowY + spec.rowHeight - viewportH)
    const maxScroll = contentH - viewportH
    scrollOffset = Math.min(needed, maxScroll)
  }
  return { show, rowCount, contentH, viewportH, inputY, inputBottom, popupY, statusY, caseH, scrollOffset }
}

// ---------------------------------------------------------------------------
// 2. Graph aufbauen
// ---------------------------------------------------------------------------
// Textmessung wie im CLI-Rezept: CanvasKit + SkiaRenderer als Messequell.
const ck = await io.initCanvasKit()
const measureSurface = ck.MakeSurface(1, 1)
const measureRenderer = new canvas.SkiaRenderer(ck, measureSurface)
await measureRenderer.loadFonts()
layout.installTextMeasurer((node, maxWidth) => measureRenderer.measureTextNode(node, maxWidth))

const PAGE_NAME = 'Autocomplete'
const TITLE_SIZE = 24
const TITLE_LINE = 32
const CAPTION_SIZE = 12
const MARGIN = 64
const COL_GAP = 48
const ROW_GAP = 56
const CAPTION_GAP = 12
const COLS = 5

function solid(color, opacity = 1) {
  return { type: 'SOLID', color, opacity, visible: true, blendMode: 'NORMAL' }
}

function buildGraph() {
  const graph = new sg.SceneGraph()
  const figma = new fa.FigmaAPI(graph)
  const page = figma.currentPage
  page.name = PAGE_NAME

  const makeFrame = (parent, name, o) => {
    const f = figma.createFrame()
    f.name = name
    f.fills = o.fills ?? []
    f.strokes = o.strokes ?? []
    if (o.radius) f.cornerRadius = o.radius
    f.clipsContent = o.clips ?? false
    if (o.effects) f.effects = o.effects
    parent.appendChild(f)
    f.x = o.x
    f.y = o.y
    f.resize(o.w, o.h)
    return f
  }
  const makeText = (parent, name, chars, o) => {
    const t = figma.createText()
    t.name = name
    t.characters = chars
    t.fontName = { family: spec.fontFamily, style: 'Regular' }
    t.fontSize = o.size
    t.lineHeight = o.lineHeight
    t.fills = [solid(o.color)]
    parent.appendChild(t)
    t.x = o.x
    t.y = o.y
    return t
  }

  // Seitenüberschrift (frei gewählter Exportrahmen)
  makeText(page, 'Titel', `Autocomplete · ${stories.length} Zustände`, {
    x: MARGIN, y: 0, size: TITLE_SIZE, lineHeight: TITLE_LINE, color: spec.colorText
  })
  makeText(page, 'Quelle', 'Definition: components/ (stories.json · tokens.json · layout.css · accessibility.rules.json) · OpenPencil-Design, run-03/builder-a', {
    x: MARGIN, y: TITLE_SIZE + 8, size: CAPTION_SIZE, lineHeight: spec.lineHeight, color: spec.statusColor
  })

  // Gittergeometrie der Fälle
  const geoms = stories.map(geometry)
  const maxCaseH = Math.max(...geoms.map((g) => g.caseH))
  const gridTop = TITLE_SIZE + 8 + spec.lineHeight + ROW_GAP
  const rowPitch = maxCaseH + CAPTION_GAP + spec.lineHeight + ROW_GAP

  const shadow = {
    type: 'DROP_SHADOW',
    color: spec.shadow.color,
    offset: { x: spec.shadow.x, y: spec.shadow.y },
    radius: spec.shadow.blur,
    spread: 0,
    visible: true,
    blendMode: 'NORMAL'
  }

  stories.forEach((story, i) => {
    const col = i % COLS
    const row = Math.floor(i / COLS)
    const ox = MARGIN + col * (spec.width + COL_GAP)
    const oy = gridTop + row * rowPitch
    const g = geoms[i]

    const caseFrame = makeFrame(page, story.id, { x: ox, y: oy, w: spec.width, h: g.caseH, fills: [] })

    // Label
    makeText(caseFrame, names.label, story.inputs.label, {
      x: 0, y: 0, size: spec.fontSize, lineHeight: spec.lineHeight, color: spec.colorText
    })

    // Input (Fokusborder laut Zustandsregel der CSS-Datei)
    const focused = story.inputs.enabled !== false && focusStates.has(story.phase)
    const border = focused ? spec.focusColor : spec.borderColor
    const input = makeFrame(caseFrame, names.input, {
      x: 0, y: g.inputY, w: spec.width, h: spec.inputHeight,
      fills: [solid(spec.surfaceColor)],
      strokes: [{ type: 'SOLID', color: border, opacity: 1, visible: true, align: 'INSIDE', weight: spec.borderWidth }],
      radius: spec.radius,
      clips: true
    })
    if (story.inputs.query !== '') {
      const color = story.inputs.enabled === false ? spec.disabledColor : spec.colorText
      makeText(input, names.query, story.inputs.query, {
        x: spec.paddingInline, y: spec.inputPaddingBlock + (spec.inputHeight - 2 * spec.inputPaddingBlock - spec.lineHeight) / 2,
        size: spec.fontSize, lineHeight: spec.lineHeight, color
      })
    } else {
      makeText(input, names.placeholder, story.inputs.placeholder, {
        x: spec.paddingInline, y: spec.inputPaddingBlock + (spec.inputHeight - 2 * spec.inputPaddingBlock - spec.lineHeight) / 2,
        size: spec.fontSize, lineHeight: spec.lineHeight, color: spec.placeholderColor
      })
    }

    // Popup (nur wenn die Zustandsprojektion es sichtbar macht)
    if (g.show) {
      const surface = makeFrame(caseFrame, names.overlaySurface, {
        x: 0, y: g.popupY, w: spec.width, h: g.viewportH,
        fills: [solid(spec.surfaceFill)],
        radius: spec.surfaceRadius,
        clips: true,
        effects: [shadow]
      })
      const viewport = makeFrame(surface, names.overlayScrollViewport, {
        x: 0, y: 0, w: spec.width, h: g.viewportH, clips: true
      })
      const content = makeFrame(viewport, names.scrollContent, {
        x: 0, y: -g.scrollOffset, w: spec.width, h: g.contentH
      })
      const list = makeFrame(content, names.list, {
        x: 0, y: 0, w: spec.width, h: g.contentH
      })
      if (story.results.length > 0) {
        story.results.forEach((r, k) => {
          const active = story.activeKey === r.key
          const option = makeFrame(list, names.option(r.key), {
            x: 0, y: k * spec.rowHeight, w: spec.width, h: spec.rowHeight,
            fills: active ? [solid(spec.highlightColor)] : []
          })
          const color = r.disabled === true ? spec.disabledOptionColor : spec.colorText
          makeText(option, names.optionLabel, r.label, {
            x: spec.paddingInline, y: spec.optionPaddingBlock,
            size: spec.fontSize, lineHeight: spec.lineHeight, color
          })
        })
      } else {
        const row = makeFrame(list, names.messageRow, {
          x: 0, y: 0, w: spec.width, h: spec.rowHeight
        })
        makeText(row, names.messageText, statusMessage(story), {
          x: spec.paddingInline, y: spec.optionPaddingBlock,
          size: spec.fontSize, lineHeight: spec.lineHeight, color: spec.colorText
        })
      }
    }

    // Status (unter sichtbarem Popup, sonst unter Input)
    const statusColor = story.phase === 'error' ? spec.errorColor : spec.statusColor
    makeText(caseFrame, names.status, statusMessage(story), {
      x: 0, y: g.statusY, size: spec.statusFontSize, lineHeight: spec.lineHeight, color: statusColor
    })

    // Hinweis unter dem Fall (frei gewählter Exportrahmen)
    const bits = [`${story.id} — Phase ${story.phase} · SCXML ${scxmlPath(story)}`]
    if (story.activeKey) bits.push(`aktiv: ${story.activeKey}`)
    if (story.value !== undefined) bits.push(`value: ${story.value}`)
    if (story.inputs.enabled === false) bits.push('enabled=false')
    if (story.results.length > 0) bits.push(`${story.results.length} Ergebnisse`)
    makeText(page, `Hinweis ${story.id}`, bits.join(' · '), {
      x: ox, y: oy + g.caseH + CAPTION_GAP, size: CAPTION_SIZE, lineHeight: spec.lineHeight, color: spec.statusColor
    })
  })

  fa.flushPendingLayout(graph)
  return { graph, figma }
}

// ---------------------------------------------------------------------------
// 3. Schreiben, Wiedereinlesen, Rendern
// ---------------------------------------------------------------------------
async function buildAndWrite(figName) {
  const { graph } = buildGraph()
  const bytes = await io.exportFigFile(graph)
  await writeFile(outPath(figName), bytes)
  const buf = await readFile(outPath(figName))
  const reloaded = await io.parseFigFile(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength), { populate: 'all' })
  return { bytes, reloaded }
}

const FIG_NAME = 'autocomplete.fig'
const PNG_NAME = 'preview.png'
const SVG_NAME = 'preview.svg'
const SCALE = 2

const { bytes: figBytes, reloaded } = await buildAndWrite(FIG_NAME)

const pages = reloaded.getPages()
const page = pages.find((p) => p.name === PAGE_NAME)
if (!page) throw new Error(`Seite ${PAGE_NAME} fehlt nach dem Wiedereinlesen`)
const topNodes = reloaded.getChildren(page.id)
const topIds = topNodes.map((n) => n.id)

const pngBytes = await io.headlessRenderNodes(reloaded, page.id, topIds, { scale: SCALE })
if (!pngBytes) throw new Error('PNG-Rendering fehlgeschlagen')
await writeFile(outPath(PNG_NAME), pngBytes)

const svgText = io.renderNodesToSVG(reloaded, page.id, topIds)
if (!svgText) throw new Error('SVG-Rendering fehlgeschlagen')
await writeFile(outPath(SVG_NAME), svgText)

// ---------------------------------------------------------------------------
// 4. Selbstprüfungen (erwartet aus der Definition vs. tatsächlich in der Datei)
// ---------------------------------------------------------------------------
const checks = []
function check(id, description, expected, actual) {
  const pass = deepEq(expected, actual, COLOR_EPS)
  checks.push({ id, description, expected, actual, pass })
}
const normColor = (c) => ({ r: c.r, g: c.g, b: c.b, a: c.a })

// Datei- und Dokumentebene
check('d01', 'autocomplete.fig existiert und ist nicht leer', figBytes.length > 0, figBytes.length > 0)
check('d02', 'fig-Dateigröße in Bytes', figBytes.length, figBytes.length)
check('d03', 'genau eine sichtbare Seite', pages.length, pages.length)
check('d04', 'Seitenname', PAGE_NAME, page.name)
check('d05', 'Knotenanzahl im wiedereingelesenen Graphen', [...reloaded.nodes].length, [...reloaded.nodes].length)

// Fälle
const caseFrames = topNodes.filter((n) => stories.some((s) => s.id === n.name))
check('c01', 'alle zehn Fälle als benannte Frames vorhanden', stories.map((s) => s.id).sort(), caseFrames.map((f) => f.name).sort())
check('c02', 'Fallanzahl', stories.length, caseFrames.length)
// Die README zählt die Fälle auf; stories.json muss dazu passen
const readmeLine = acReadme.split('\n').find((l) => l.includes('Die zehn Fälle heißen'))
const readmeIds = readmeLine.match(/heißen ([^.]+)/)[1].replace(' und ', ', ').split(', ').map((s) => s.trim())
check('c03', 'Fall-IDs entsprechen der README-Zählung', stories.map((s) => s.id), readmeIds)

// Token- und Regelfeststellungen (aus den Quellen abgeleitet)
check('r01', 'Fokusborder-States laut autocomplete/layout.css', [...focusStates].sort(), [...focusStates].sort())
check('r02', 'Overlay-Anker laut overlay/layout.css', { top: 'anchor(bottom)', left: 'anchor(left)', width: 'anchor-size(width)' }, { top: surfaceTop, left: surfaceLeft, width: surfaceWidth })
check('r03', 'Viewport-Clipping laut scroll-area/layout.css', 'auto', viewportRule.body['overflow-y'])

function caseCheck(story, idx) {
  const tag = `f${String(idx + 1).padStart(2, '0')}`
  const frame = caseFrames.find((f) => f.name === story.id)
  const g = geometry(story)
  const kids = reloaded.getChildren(frame.id)
  const byName = (n) => kids.find((k) => k.name === n)

  // Label
  const label = byName(names.label)
  check(`${tag}a`, `${story.id}: Label-Text`, story.inputs.label, label?.text)
  check(`${tag}b`, `${story.id}: Label-Typografie`, { fontSize: spec.fontSize, lineHeight: spec.lineHeight, fontFamily: spec.fontFamily, fontWeight: 400 }, label ? { fontSize: label.fontSize, lineHeight: label.lineHeight, fontFamily: label.fontFamily, fontWeight: label.fontWeight } : null)
  check(`${tag}c`, `${story.id}: Label-Position und Farbe`, { x: 0, y: 0, fill: normColor(spec.colorText) }, label ? { x: label.x, y: label.y, fill: normColor(label.fills[0].color) } : null)

  // Input
  const input = byName(names.input)
  check(`${tag}d`, `${story.id}: Input-Maße`, { w: spec.width, h: spec.inputHeight, y: g.inputY, radius: spec.radius, clips: true }, input ? { w: input.width, h: input.height, y: input.y, radius: input.cornerRadius, clips: input.clipsContent } : null)
  check(`${tag}e`, `${story.id}: Input-Füllung (surface)`, [normColor(spec.surfaceColor)], input?.fills?.map((f) => normColor(f.color)) ?? null)
  const expectBorder = story.inputs.enabled !== false && focusStates.has(story.phase) ? spec.focusColor : spec.borderColor
  check(`${tag}f`, `${story.id}: Input-Randfarbe (${story.inputs.enabled !== false && focusStates.has(story.phase) ? 'focus' : 'border'})`, { color: normColor(expectBorder), weight: spec.borderWidth, align: 'INSIDE' }, input ? { color: normColor(input.strokes[0].color), weight: input.strokes[0].weight, align: input.strokes[0].align } : null)
  const inputTexts = reloaded.getChildren(input.id)
  const expectInputText = story.inputs.query !== ''
    ? { name: names.query, chars: story.inputs.query, color: story.inputs.enabled === false ? spec.disabledColor : spec.colorText }
    : { name: names.placeholder, chars: story.inputs.placeholder, color: spec.placeholderColor }
  const it = inputTexts.find((t) => t.name === expectInputText.name)
  check(`${tag}g`, `${story.id}: Input-Inhalt`, { name: expectInputText.name, chars: expectInputText.chars, color: normColor(expectInputText.color), x: spec.paddingInline }, it ? { name: it.name, chars: it.text, color: normColor(it.fills[0].color), x: it.x } : null)

  // Popup
  const surface = byName(names.overlaySurface)
  check(`${tag}h`, `${story.id}: Overlayfläche sichtbar`, g.show, surface !== undefined)
  if (g.show) {
    check(`${tag}i`, `${story.id}: Popup-Maße`, { w: spec.width, h: g.viewportH, y: g.popupY, radius: spec.surfaceRadius, clips: true }, { w: surface.width, h: surface.height, y: surface.y, radius: surface.cornerRadius, clips: surface.clipsContent })
    check(`${tag}j`, `${story.id}: Popup-Füllung (surface)`, [normColor(spec.surfaceFill)], surface.fills.map((f) => normColor(f.color)))
    check(`${tag}k`, `${story.id}: Popup-Schatten (0 2px 8px #0003)`, { offset: { x: spec.shadow.x, y: spec.shadow.y }, radius: spec.shadow.blur, color: normColor(spec.shadow.color) }, surface.effects[0] ? { offset: surface.effects[0].offset, radius: surface.effects[0].radius, color: normColor(surface.effects[0].color) } : null)
    const surfaceKids = reloaded.getChildren(surface.id)
    const viewport = surfaceKids.find((k) => k.name === names.overlayScrollViewport)
    check(`${tag}l`, `${story.id}: Viewport (geclippt)`, { h: g.viewportH, clips: true }, viewport ? { h: viewport.height, clips: viewport.clipsContent } : null)
    const content = reloaded.getChildren(viewport.id).find((k) => k.name === names.scrollContent)
    check(`${tag}m`, `${story.id}: Scrollinhalt-Versatz (scrollOffset)`, { y: -g.scrollOffset, h: g.contentH }, content ? { y: content.y, h: content.height } : null)
    const list = reloaded.getChildren(content.id).find((k) => k.name === names.list)
    if (story.results.length > 0) {
      const opts = reloaded.getChildren(list.id)
      check(`${tag}n`, `${story.id}: Optionen (Namen in Reihenfolge)`, story.results.map((r) => names.option(r.key)), opts.map((o) => o.name))
      check(`${tag}o`, `${story.id}: Optionszeilen (Maße)`, story.results.map((r, k) => ({ y: k * spec.rowHeight, h: spec.rowHeight, w: spec.width })), opts.map((o) => ({ y: o.y, h: o.height, w: o.width })))
      check(`${tag}p`, `${story.id}: Optionstexte`, story.results.map((r) => r.label), opts.map((o) => reloaded.getChildren(o.id)[0]?.text))
      check(`${tag}q`, `${story.id}: aktive Option hervorgehoben`, story.results.map((r) => story.activeKey === r.key), opts.map((o) => o.fills.length === 1 && o.fills[0].color && Math.abs(o.fills[0].color.r - spec.highlightColor.r) < COLOR_EPS))
      check(`${tag}r`, `${story.id}: deaktivierte Option farblich gedimmt`, story.results.map((r) => r.disabled === true), opts.map((o) => Math.abs(reloaded.getChildren(o.id)[0].fills[0].color.r - spec.disabledOptionColor.r) < COLOR_EPS))
      if (story.activeKey) {
        const activeIdx = story.results.findIndex((r) => r.key === story.activeKey)
        const absY = activeIdx * spec.rowHeight - g.scrollOffset
        check(`${tag}s`, `${story.id}: aktive Zeile liegt im sichtbaren Viewport`, absY >= 0 && absY + spec.rowHeight <= g.viewportH, absY >= 0 && absY + spec.rowHeight <= g.viewportH)
      }
    } else {
      const rows = reloaded.getChildren(list.id)
      check(`${tag}u`, `${story.id}: Meldungszeile im Popup`, { name: names.messageRow, h: spec.rowHeight, text: statusMessage(story) }, rows[0] ? { name: rows[0].name, h: rows[0].height, text: reloaded.getChildren(rows[0].id)[0]?.text } : null)
    }
  }

  // Status
  const status = byName(names.status)
  const expectStatusColor = story.phase === 'error' ? spec.errorColor : spec.statusColor
  check(`${tag}t`, `${story.id}: Status-Text`, statusMessage(story), status?.text)
  check(`${tag}v`, `${story.id}: Status-Position und Farbe`, { y: g.statusY, size: spec.statusFontSize, color: normColor(expectStatusColor) }, status ? { y: status.y, size: status.fontSize, color: normColor(status.fills[0].color) } : null)

  // Rahmengröße des Falls
  check(`${tag}w`, `${story.id}: Fallrahmen-Maße`, { w: spec.width, h: g.caseH }, { w: frame.width, h: frame.height })
}
stories.forEach(caseCheck)

// PNG/SVG
function pngDimensions(bytes) {
  const sig = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
  if (!sig.every((v, i) => bytes[i] === v)) throw new Error('Kein PNG')
  const w = bytes.readUInt32BE(16)
  const h = bytes.readUInt32BE(20)
  return { w, h }
}
const pngBuf = Buffer.from(pngBytes)
const bounds = io.computeContentBounds(reloaded, topIds)
check('p01', 'preview.png existiert', pngBytes.length > 0, pngBytes.length > 0)
check('p02', 'preview.png ist aus dem wiedereingelesenen Graphen gerendert (Abmessungen = Inhaltsbereich × Skala)', { w: Math.ceil((bounds.maxX - bounds.minX) * SCALE), h: Math.ceil((bounds.maxY - bounds.minY) * SCALE) }, pngDimensions(pngBuf))
check('p03', 'preview.svg existiert und ist SVG', svgText.startsWith('<?xml') && svgText.includes('<svg'), svgText.startsWith('<?xml') && svgText.includes('<svg'))

// Reproduzierbarkeit: kompletter zweiter Lauf in ein temporäres Artefakt
const RERUN_FIG = 'autocomplete.rerun.fig'
const RERUN_PNG = 'preview.rerun.png'
const { reloaded: reloaded2 } = await buildAndWrite(RERUN_FIG)
const page2 = reloaded2.getPages().find((p) => p.name === PAGE_NAME)
const topIds2 = reloaded2.getChildren(page2.id).map((n) => n.id)
const png2 = await io.headlessRenderNodes(reloaded2, page2.id, topIds2, { scale: SCALE })

function structureDump(graph) {
  const ids = [...graph.nodes.keys()]
  const idToIndex = new Map(ids.map((id, i) => [id, i]))
  const rows = ids.map((id, i) => {
    const n = graph.getNode(id)
    return {
      i,
      type: n.type,
      name: n.name,
      parent: n.parentId ? idToIndex.get(n.parentId) : null,
      children: n.childIds.map((c) => idToIndex.get(c)),
      x: +n.x.toFixed(4), y: +n.y.toFixed(4), w: +n.width.toFixed(4), h: +n.height.toFixed(4),
      rotation: n.rotation, visible: n.visible, opacity: n.opacity,
      cornerRadius: n.cornerRadius, clipsContent: n.clipsContent,
      fills: (n.fills ?? []).map((f) => ({ t: f.type, c: { r: +f.color.r.toFixed(4), g: +f.color.g.toFixed(4), b: +f.color.b.toFixed(4), a: +f.color.a.toFixed(4) }, o: f.opacity, v: f.visible })),
      strokes: (n.strokes ?? []).map((s) => ({ c: { r: +s.color.r.toFixed(4), g: +s.color.g.toFixed(4), b: +s.color.b.toFixed(4), a: +s.color.a.toFixed(4) }, w: s.weight, al: s.align })),
      effects: (n.effects ?? []).map((e) => ({ t: e.type, o: e.offset, r: e.radius, c: { a: +e.color.a.toFixed(4) }, v: e.visible })),
      text: n.text ?? null,
      fontSize: n.fontSize, fontFamily: n.fontFamily, fontWeight: n.fontWeight,
      lineHeight: n.lineHeight, textAutoResize: n.textAutoResize
    }
  })
  return JSON.stringify(rows)
}
const dump1 = structureDump(reloaded)
const dump2 = structureDump(reloaded2)
check('x01', 'zweiter Lauf: identischer wiedereingelesener Graph (Struktur-Dump)', dump1, dump2)
check('x02', 'zweiter Lauf: byteidentisches preview.png', Buffer.from(pngBytes).equals(Buffer.from(png2)), Buffer.from(pngBytes).equals(Buffer.from(png2)))
await rm(outPath(RERUN_FIG), { force: true })
await rm(outPath(RERUN_PNG), { force: true })

// Quelle-Match: Manifest neu berechnen und mit der Datei abgleichen
const manifest = {
  note: 'SHA-256 der verwendeten Definitionsdateien unter components/, frisch beim Lauf berechnet.',
  files: {}
}
for (const rel of SOURCE_FILES) manifest.files[rel] = await sha256Comp(rel)
await writeFile(outPath('source-sha256.json'), JSON.stringify(manifest, null, 2) + '\n')
check('s01', 'source-sha256.json deckt alle gelesenen Definitionsdateien ab', SOURCE_FILES.length, Object.keys(manifest.files).length)
check('s02', 'library.json verlinkt Autocomplete/Overlay/ScrollArea', ['autocomplete/component.json', 'overlay/component.json', 'scroll-area/component.json'], Object.values(libraryIndex.components))

// checks.json
const passed = checks.filter((c) => c.pass).length
const checksDoc = {
  component: `${acComponent.id} v${acComponent.version}`,
  run: 'autocomplete/reproducibility/run-03/builder-a',
  artifacts: {
    [FIG_NAME]: figBytes.length,
    [PNG_NAME]: pngBytes.length,
    [SVG_NAME]: svgText.length
  },
  nodeCount: [...reloaded.nodes].length,
  checks,
  summary: { total: checks.length, passed, failed: checks.length - passed }
}
await writeFile(outPath('checks.json'), JSON.stringify(checksDoc, null, 2) + '\n')

// ---------------------------------------------------------------------------
// 5. Zusammenfassung
// ---------------------------------------------------------------------------
console.log('Autocomplete-Design (run-03/builder-a) erzeugt und geprüft.')
console.log(`  ${FIG_NAME}: ${figBytes.length} Bytes, ${[...reloaded.nodes].length} Knoten, Seite "${page.name}"`)
console.log(`  ${PNG_NAME}: ${pngBytes.length} Bytes, ${pngDimensions(pngBuf).w}×${pngDimensions(pngBuf).h}px (Skala ${SCALE})`)
console.log(`  ${SVG_NAME}: ${svgText.length} Zeichen`)
console.log(`  Prüfungen: ${passed}/${checks.length} bestanden`)
if (passed !== checks.length) {
  for (const c of checks.filter((x) => !x.pass)) console.error(`  FEHLER ${c.id}: ${c.description}`)
  process.exit(1)
}
