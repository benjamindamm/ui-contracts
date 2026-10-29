#!/usr/bin/env node
/**
 * Builder A — deterministischer Export der Autocomplete-Definition (components/**)
 * in ein editierbares OpenPencil-Dokument.
 *
 * Ausführen vom Repo-Root:
 *   node examples/autocomplete/reproducibility/run-02/builder-a/generate.mjs
 *
 * Erzeugt in diesem Ordner: autocomplete.fig, preview.png, checks.json, source-sha256.json
 * Keine Netzwerkzugriffe. Schreibt ausschließlich in den eigenen Ausgabeordner.
 */
import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { fileURLToPath, pathToFileURL } from 'node:url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.resolve(HERE, '../../../../..')
const OUT = HERE
const NM = path.join(REPO, 'tools/openpencil/node_modules/@open-pencil')
const mod = (p) => import(pathToFileURL(path.join(NM, p)).href)

const { SceneGraph, setIdSession } = await mod('scene-graph/dist/index.js')
// Feste GUID-Session, damit wiederholte Läufe dieselben Knoten-IDs erzeugen.
setIdSession(1618)
const { FigmaAPI } = await mod('core/dist/figma-api/index.js')
const io = await mod('core/dist/io/index.js')
const { unzipSync, zipSync } = await import(pathToFileURL(
  path.join(REPO, 'tools/openpencil/node_modules/fflate/esm/index.mjs')).href)
const { exportFigFile, parseFigFile, headlessRenderNodes, initCanvasKit } = io

const corePkg = JSON.parse(fs.readFileSync(path.join(NM, 'core/package.json'), 'utf8'))
const WRITER = `@open-pencil/core ${corePkg.version} · exportFigFile`
const READER = `@open-pencil/core ${corePkg.version} · parseFigFile`

/* ---------------------------------------------------------------- Definition */
const COMPONENTS = path.join(REPO, 'components')
const readJSON = (rel) => JSON.parse(fs.readFileSync(path.join(COMPONENTS, rel), 'utf8'))

const tokens = readJSON('tokens.json')
const stories = readJSON('autocomplete/stories.json').stories
const a11yRules = readJSON('autocomplete/accessibility.rules.json')

function dim(group, name) {
  const v = tokens[group][name].$value
  if (typeof v === 'string' && v.startsWith('{')) {
    const [g, n] = v.slice(1, -1).split('.')
    return dim(g, n)
  }
  return v.value
}
function color(group, name) {
  const c = tokens[group][name].$value.components
  return { r: c[0], g: c[1], b: c[2] }
}
const T = {
  width: dim('autocomplete', 'width'),
  gap: dim('autocomplete', 'gap'),
  maxHeight: dim('autocomplete', 'maxHeight'),
  rowHeight: dim('autocomplete', 'rowHeight'),
  inputHeight: dim('autocomplete', 'inputHeight'),
  fontSize: dim('autocomplete', 'fontSize'),
  statusFontSize: dim('autocomplete', 'statusFontSize'),
  lineHeight: dim('autocomplete', 'lineHeight'),
  labelGap: dim('autocomplete', 'labelGap'),
  statusGap: dim('autocomplete', 'statusGap'),
  radius: dim('autocomplete', 'radius'),
  borderWidth: dim('autocomplete', 'borderWidth'),
  paddingInline: dim('autocomplete', 'paddingInline'),
  fontFamily: tokens.autocomplete.fontFamily.$value,
  surface: color('autocomplete', 'surface'),
  text: color('autocomplete', 'text'),
  muted: color('autocomplete', 'muted'),
  border: color('autocomplete', 'border'),
  focus: color('autocomplete', 'focus'),
  highlight: color('autocomplete', 'highlight'),
  disabled: color('autocomplete', 'disabled'),
  error: color('autocomplete', 'error'),
}

const byId = new Map(stories.map((s) => [s.id, s]))
const OPTIONS = byId.get('ready').results
const resultCount = OPTIONS.length
const messages = a11yRules.messages
const fillTemplate = (tpl, values) =>
  tpl.replace(/\{(\w+)\}/g, (_, k) => String(values[k] ?? `{${k}}`))

// Fälle exakt aus stories.json + accessibility.rules.json; Popup-Sichtbarkeit aus projections.
// Popup-Inhalt: loading/empty/error zeigen eine Meldungszeile, ready zeigt die Ergebnisoptionen.
const POPUP_CASES = new Set(['loading', 'ready', 'active', 'scroll-end', 'empty', 'error'])
const MESSAGE_CASES = new Set(['loading', 'empty', 'error'])

const CASES = stories.map((story) => {
  const input = story.inputs
  const id = story.id
  const results = story.results || []
  const hasPopup = POPUP_CASES.has(id)
  let status = ''
  let statusError = false
  if (id === 'opening') status = messages.opening
  else if (id === 'loading') status = messages.loading
  else if (results.length > 0 && story.phase === 'ready') {
    status = fillTemplate(messages.results, { count: results.length })
  } else if (id === 'empty') status = messages.empty
  else if (id === 'error') { status = messages.error; statusError = true }
  else if (id === 'selected') {
    const v = results.find((r) => r.key === story.value)
    status = fillTemplate(messages.selected, { label: v ? v.label : '' })
  } else if (id === 'disabled') status = messages.disabled
  else status = messages.closed

  return {
    id,
    phase: story.phase,
    input,
    results,
    value: story.value,
    activeKey: story.activeKey,
    enabled: input.enabled !== false,
    hasPopup,
    usesMessageRow: MESSAGE_CASES.has(id) && hasPopup,
    rowMessage: MESSAGE_CASES.has(id) ? status : null,
    status,
    statusError,
    popupVisible: hasPopup,
  }
})

/* ------------------------------------------------------------------- Helpers */
const api = new FigmaAPI(new SceneGraph())
const solid = (c) => ({ type: 'SOLID', color: { r: c.r, g: c.g, b: c.b }, opacity: 1 })

function frame(parent, name, x, y, w, h) {
  const n = api.createFrame()
  n.name = name
  n.resize(w, h)
  n.fills = []
  n.strokes = []
  n.clipsContent = false
  parent.appendChild(n)
  n.x = x
  n.y = y
  return n
}

function rect(parent, name, x, y, w, h, opts = {}) {
  const n = frame(parent, name, x, y, w, h)
  if (opts.fill) n.fills = [solid(opts.fill)]
  if (opts.stroke) {
    n.strokes = [solid(opts.stroke)]
    n.strokeWeight = T.borderWidth
    n.strokeAlign = 'INSIDE'
  }
  if (opts.radius) n.cornerRadius = opts.radius
  if (opts.clip) n.clipsContent = true
  if (opts.shadow) {
    n.effects = [{
      type: 'DROP_SHADOW',
      color: { r: 0, g: 0, b: 0, a: 0.2 },
      offset: { x: 0, y: 2 },
      radius: 8,
      spread: 0,
      visible: true,
      blendMode: 'NORMAL',
    }]
  }
  return n
}

function text(parent, name, str, x, y, w, opts = {}) {
  const n = api.createText()
  n.name = name
  n.fontName = { family: T.fontFamily, style: 'Regular' }
  const lh = opts.lineHeight ?? T.lineHeight
  n.fontSize = opts.size ?? T.fontSize
  n.lineHeight = { unit: 'PIXELS', value: lh }
  n.letterSpacing = { unit: 'PIXELS', value: 0 }
  n.textAutoResize = 'NONE'
  n.fills = [solid(opts.color ?? T.text)]
  n.characters = str
  n.resize(w, lh)
  parent.appendChild(n)
  n.x = x
  n.y = y
  return n
}

/* ------------------------------------------------------------------ Dokument */
const page = api.currentPage
page.name = 'Autocomplete'
api.root.name = 'Autocomplete · 0.1.0'

const COL_X = [80, 560]
const START_Y = 180
const COL_GAP = 96
const cursor = [START_Y, START_Y]

text(page, 'page title', 'Autocomplete · 0.1.0 · 10 Darstellungsfälle', 80, 56, 900, {
  size: 24,
  lineHeight: 32,
  color: T.text,
})

const MARGIN_TOP = T.lineHeight + T.labelGap // label + gap
const INPUT_TOP = MARGIN_TOP
const POPUP_TOP = INPUT_TOP + T.inputHeight + T.gap
const ROW_TEXT_Y = 6

const built = []

for (let i = 0; i < CASES.length; i++) {
  const c = CASES[i]
  const col = i % 2
  const viewportH = c.hasPopup
    ? Math.min((c.usesMessageRow ? 1 : c.results.length) * T.rowHeight, T.maxHeight)
    : 0
  const statusTop = c.hasPopup ? POPUP_TOP + viewportH + T.statusGap : POPUP_TOP
  const frameH = statusTop + T.lineHeight
  const x = COL_X[col]
  const y = cursor[col]

  text(page, `caption ${c.id}`, c.id, x, y - 28, T.width, { size: 12, lineHeight: 16, color: T.muted })

  const art = frame(page, `Autocomplete / ${c.id}`, x, y, T.width, frameH)

  text(art, 'label', c.input.label, 0, 0, T.width)
  const input = rect(art, 'input', 0, INPUT_TOP, T.width, T.inputHeight, {
    fill: T.surface,
    stroke: c.enabled && c.phase !== 'closed' ? T.focus : T.border,
    radius: T.radius,
    clip: true,
  })

  const showsPlaceholder = c.input.query === ''
  text(input, 'input text',
    showsPlaceholder ? c.input.placeholder : c.input.query,
    T.paddingInline, (T.inputHeight - T.lineHeight) / 2,
    T.width - T.paddingInline * 2,
    { color: !c.enabled ? T.disabled : showsPlaceholder ? T.muted : T.text })

  if (c.hasPopup) {
    const surface = rect(art, 'overlay surface', 0, POPUP_TOP, T.width, viewportH, {
      fill: T.surface,
      radius: T.radius,
      shadow: true,
    })
    const viewport = rect(surface, 'scroll viewport', 0, 0, T.width, viewportH, { clip: true })
    const rows = c.usesMessageRow ? 1 : c.results.length
    // scroll-end: die aktive letzte Option muss im Viewport sichtbar sein, Inhalt wird versetzt.
    const activeIndex = c.activeKey === undefined
      ? -1
      : c.results.findIndex((r) => r.key === c.activeKey)
    const offset = activeIndex >= 0
      ? Math.max(0, Math.min(
          rows * T.rowHeight - T.maxHeight,
          activeIndex * T.rowHeight - (T.maxHeight - T.rowHeight)))
      : 0
    const list = frame(viewport, 'list', 0, -offset, T.width, rows * T.rowHeight)

    if (c.usesMessageRow) {
      const row = frame(list, 'message row', 0, 0, T.width, T.rowHeight)
      text(row, 'message text', c.rowMessage,
        T.paddingInline, ROW_TEXT_Y, T.width - T.paddingInline * 2,
        { color: T.muted })
    } else {
      for (let r = 0; r < c.results.length; r++) {
        const opt = c.results[r]
        const active = c.activeKey !== undefined && opt.key === c.activeKey
        const row = rect(list, `option ${opt.key}`, 0, r * T.rowHeight, T.width, T.rowHeight, {
          fill: active ? T.highlight : undefined,
        })
        text(row, 'option label', opt.label,
          T.paddingInline, ROW_TEXT_Y, T.width - T.paddingInline * 2,
          { color: opt.disabled ? T.disabled : T.text })
      }
    }
  }

  const status = text(art, 'status', c.status, 0, statusTop, T.width, {
    size: T.statusFontSize,
    color: c.statusError ? T.error : T.muted,
  })

  built.push({ c, art, status, viewportH, statusTop, frameH })
  cursor[col] = y + frameH + COL_GAP
}

/* -------------------------------------------------------------------- Export */
const ck = await initCanvasKit()
const exported = await exportFigFile(api.graph, ck, undefined, page.id, true)

// Reproduzierbare Bytes: exportFigFile schreibt in meta.json einen createdAt-Zeitstempel und
// ZIP-mtimes der aktuellen Uhrzeit. Beides wird hier auf feste Werte normalisiert; die
// Designinhalte (canvas.fig, thumbnail.png) bleiben unverändert.
const FIXED_DATE = new Date('2026-01-01T00:00:00.000Z')
function stabilizeFig(bytes) {
  const entries = unzipSync(bytes)
  const meta = JSON.parse(new TextDecoder().decode(entries['meta.json']))
  meta.createdAt = FIXED_DATE.toISOString()
  const out = {}
  for (const name of Object.keys(entries)) {
    const data = name === 'meta.json' ? new TextEncoder().encode(JSON.stringify(meta)) : entries[name]
    out[name] = [data, { level: 0, mtime: FIXED_DATE }]
  }
  return zipSync(out)
}
const figBytes = stabilizeFig(exported)
fs.writeFileSync(path.join(OUT, 'autocomplete.fig'), figBytes)

/* ------------------------------------------------------- Rücklesen + Prüfen */
// Rückleseprüfung ausschließlich über die geschriebene Datei (Originalreader).
const figOnDisk = fs.readFileSync(path.join(OUT, 'autocomplete.fig'))
const parsed = await parseFigFile(
  figOnDisk.buffer.slice(figOnDisk.byteOffset, figOnDisk.byteOffset + figOnDisk.byteLength),
  { populate: 'all' })
const pApi = new FigmaAPI(parsed)

const hex = (c) => '#' + [c.r, c.g, c.b]
  .map((v) => Math.round(Math.max(0, Math.min(1, v)) * 255).toString(16).padStart(2, '0'))
  .join('').toUpperCase()
const fillHex = (n) => {
  const f = n.fills && n.fills[0]
  if (!f || f.type !== 'SOLID') return null
  return hex(f.color)
}
const strokeHex = (n) => {
  const s = n.strokes && n.strokes[0]
  if (!s || s.type !== 'SOLID') return null
  return hex(s.color)
}

const pPage = pApi.currentPage
const allNodes = [...parsed.nodes.values()]
const textNodes = allNodes.filter((n) => n.type === 'TEXT')
const editableText = textNodes.filter((n) => {
  const proxy = pApi.getNodeById(n.id)
  return !!proxy &&
    typeof proxy.characters === 'string' &&
    proxy.fontName && typeof proxy.fontName === 'object' && !!proxy.fontName.family &&
    typeof proxy.fontSize === 'number' && proxy.fontSize > 0
})

const findChild = (parent, name) => (parent.children || []).find((n) => n.name === name) || null
const descendants = (node, acc = []) => {
  for (const ch of node.children || []) { acc.push(ch); descendants(ch, acc) }
  return acc
}

const caseChecks = []
for (const { c } of built) {
  const art = pPage.children.find((n) => n.name === `Autocomplete / ${c.id}`)
  const input = findChild(art, 'input')
  const inputText = findChild(input, 'input text')
  const surface = findChild(art, 'overlay surface')
  const viewport = surface ? findChild(surface, 'scroll viewport') : null
  const list = viewport ? findChild(viewport, 'list') : null
  const status = findChild(art, 'status')
  const options = list
    ? (list.children || []).filter((n) => n.name.startsWith('option ')).map((o) => ({
        name: o.name,
        key: o.name.slice('option '.length),
        label: (findChild(o, 'option label') || {}).characters ?? null,
        height: o.height,
        y: o.y,
        fill: fillHex(o),
        textColor: findChild(o, 'option label') ? fillHex(findChild(o, 'option label')) : null,
      }))
    : []
  const messageRow = list ? findChild(list, 'message row') : null
  const measured = {
    id: c.id,
    frame: { name: art.name, width: art.width, height: art.height },
    popupVisible: !!surface && surface.height > 0,
    popup: surface ? { width: surface.width, height: surface.height, y: surface.y, radius: surface.cornerRadius, fill: fillHex(surface), stroke: strokeHex(surface) } : null,
    input: {
      width: input.width,
      height: input.height,
      y: input.y,
      borderColor: strokeHex(input),
      strokeWeight: input.strokeWeight,
      radius: input.cornerRadius,
      fill: fillHex(input),
    },
    inputText: {
      characters: inputText.characters,
      color: fillHex(inputText),
      fontSize: inputText.fontSize,
      isPlaceholder: inputText.characters === c.input.placeholder && c.input.query === '',
    },
    viewport: viewport ? { width: viewport.width, height: viewport.height, clip: viewport.clipsContent } : null,
    contentOffsetY: list ? list.y : null,
    contentHeight: list ? list.height : null,
    options,
    messageRow: messageRow ? { text: findChild(messageRow, 'message text').characters, height: messageRow.height } : null,
    status: {
      characters: status.characters,
      fontSize: status.fontSize,
      color: fillHex(status),
      y: status.y,
      height: status.height,
    },
  }

  const expect = {
    popupVisible: c.popupVisible,
    inputBorder: c.enabled && c.phase !== 'closed' ? hex(T.focus) : hex(T.border),
    inputText: c.input.query === '' ? c.input.placeholder : c.input.query,
    status: c.status,
    statusColor: c.statusError ? hex(T.error) : hex(T.muted),
    optionCount: c.hasPopup && !c.usesMessageRow ? c.results.length : null,
    activeOption: c.activeKey ?? null,
    viewportHeight: c.hasPopup
      ? Math.min((c.usesMessageRow ? 1 : c.results.length) * T.rowHeight, T.maxHeight)
      : null,
    frameWidth: T.width,
  }
  const match =
    measured.popupVisible === expect.popupVisible &&
    measured.input.borderColor === expect.inputBorder &&
    measured.inputText.characters === expect.inputText &&
    measured.status.characters === expect.status &&
    measured.status.color === expect.statusColor &&
    measured.frame.width === expect.frameWidth &&
    (expect.optionCount === null || measured.options.length === expect.optionCount) &&
    (expect.activeOption === null ||
      measured.options.some((o) => o.key === expect.activeOption && o.fill === hex(T.highlight))) &&
    (expect.viewportHeight === null || (measured.viewport && measured.viewport.height === expect.viewportHeight))

  caseChecks.push({ ...measured, expectation: expect, match })
}

const bytes = fs.statSync(path.join(OUT, 'autocomplete.fig')).size
const checks = {
  component: 'Autocomplete 0.1.0 (ui-contracts:Autocomplete)',
  writer: WRITER,
  reader: READER,
  figFile: 'autocomplete.fig',
  bytes,
  pageName: pPage.name,
  nodeCount: parsed.nodes.size,
  pageCount: parsed.getPages().length,
  frameCount: built.length,
  textNodeCount: textNodes.length,
  editableTextNodeCount: editableText.length,
  allTextNodesEditable: editableText.length === textNodes.length,
  tokens: {
    width: T.width, inputHeight: T.inputHeight, rowHeight: T.rowHeight, maxHeight: T.maxHeight,
    gap: T.gap, labelGap: T.labelGap, statusGap: T.statusGap, lineHeight: T.lineHeight,
    radius: T.radius, borderWidth: T.borderWidth, paddingInline: T.paddingInline,
    fontSize: T.fontSize, statusFontSize: T.statusFontSize, fontFamily: T.fontFamily,
    colors: Object.fromEntries(Object.entries(T).filter(([k]) => typeof T[k] === 'object' && 'r' in T[k]).map(([k, v]) => [k, hex(v)])),
  },
  cases: caseChecks,
  allCasesMatch: caseChecks.every((c) => c.match),
}
fs.writeFileSync(path.join(OUT, 'checks.json'), JSON.stringify(checks, null, 2) + '\n')

/* ------------------------------------------------------------------- Preview */
const topLevel = pPage.children.map((n) => n.id)
let preview = await headlessRenderNodes(parsed, pPage.id, topLevel, { scale: 1, format: 'PNG' })
if (!preview) {
  preview = await headlessRenderNodes(parsed, pPage.id, topLevel, { scale: 1 })
}
if (!preview) throw new Error('headlessRenderNodes lieferte kein PNG')
fs.writeFileSync(path.join(OUT, 'preview.png'), preview)

/* ------------------------------------------------------------------- Hashes */
const SOURCES = [
  'components/README.md',
  'components/library.json',
  'components/tokens.json',
  ...['README.md', 'component.json', 'interface.json', 'layout.css', 'stories.json',
    'behavior.scxml', 'error-relay.scxml', 'accessibility.html', 'accessibility.rules.json']
    .map((f) => `components/autocomplete/${f}`),
  ...['component.json', 'interface.json', 'layout.css', 'behavior.scxml', 'accessibility.html']
    .map((f) => `components/overlay/${f}`),
  ...['component.json', 'interface.json', 'layout.css', 'behavior.scxml', 'accessibility.html']
    .map((f) => `components/scroll-area/${f}`),
]
const hashes = {}
for (const rel of SOURCES) {
  hashes[rel] = crypto.createHash('sha256').update(fs.readFileSync(path.join(REPO, rel))).digest('hex')
}
fs.writeFileSync(path.join(OUT, 'source-sha256.json'), JSON.stringify({
  algorithm: 'sha256',
  filesReadFromDefinition: hashes,
  count: Object.keys(hashes).length,
}, null, 2) + '\n')

console.log(JSON.stringify({
  fig: path.join(OUT, 'autocomplete.fig'),
  bytes,
  nodes: parsed.nodes.size,
  textNodes: textNodes.length,
  editableTextNodes: editableText.length,
  cases: caseChecks.map((c) => ({ id: c.id, match: c.match })),
  allCasesMatch: checks.allCasesMatch,
}, null, 2))
