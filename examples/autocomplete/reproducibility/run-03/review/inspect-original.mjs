/**
 * inspect-original.mjs — Phase 2, Schritt 1: Originaldateien selbst messen.
 *
 * Liest eine .fig-Datei mit dem Original-Reader der gepinnten Werkzeugumgebung
 * (tools/openpencil/node_modules, @open-pencil/fig 0.16.0) vollständig ein
 * (materializeFigArchive: alle Seiten in einen Graphen) und schreibt einen
 * strukturierten JSON-Auszug: alle Knoten mit geometrie-, text-, farbe-,
 * layout- und annotationsrelevanten Feldern plus absoluten Positionen.
 *
 * Aufruf: node inspect-original.mjs <einfuegung.autocomplete.fig> <ausgabe.json>
 * Reines Lesen der Eingabe; schreibt nur die eine Ausgabedatei.
 */
import { readFileSync, writeFileSync } from 'node:fs'
import { createHash } from 'node:crypto'

const NM = 'file:///Users/kcnpxcp/Dev/GitHub/ui-contracts/tools/openpencil/node_modules'
const fig = await import(`${NM}/@open-pencil/fig/dist/index.js`)

const [figPath, outPath] = process.argv.slice(2)
if (!figPath || !outPath) {
  console.error('usage: node inspect-original.mjs <input.fig> <output.json>')
  process.exit(2)
}

const bytes = readFileSync(figPath)
const buffer = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength)

// Parse-Metadaten (Protokoll-ebene) und vollständige Population (Graph-Ebene)
const parsed = fig.parseFigBuffer(buffer)
const assembly = fig.materializeFigArchive(buffer)
const graph = assembly.graph

function hex(color) {
  if (!color || typeof color !== 'object') return null
  const c = (v) => Math.round((Number(v) || 0) * 255).toString(16).padStart(2, '0')
  const a = color.a === undefined ? 1 : color.a
  return `#${c(color.r)}${c(color.g)}${c(color.b)}${a < 1 ? c(a) : ''}`
}

function fillInfo(f) {
  if (!f) return null
  return {
    type: f.type,
    color: f.color ? { r: f.color.r, g: f.color.g, b: f.color.b, a: f.color.a, hex: hex(f.color) } : null,
    opacity: f.opacity,
    visible: f.visible,
  }
}

function strokeInfo(s) {
  if (!s) return null
  return { ...fillInfo(s), weight: s.weight, align: s.align, dashPattern: s.dashPattern || null }
}

function effectInfo(e) {
  if (!e) return null
  return {
    type: e.type,
    color: e.color ? hex(e.color) : null,
    offset: e.offset,
    radius: e.radius,
    spread: e.spread,
    visible: e.visible,
  }
}

const RELEVANT = [
  'type', 'name', 'parentId', 'childIds',
  'x', 'y', 'width', 'height', 'rotation',
  'visible', 'locked', 'opacity', 'clipsContent',
  'cornerRadius', 'independentCorners',
  'topLeftRadius', 'topRightRadius', 'bottomRightRadius', 'bottomLeftRadius',
  'text', 'fontSize', 'fontFamily', 'fontWeight', 'italic',
  'lineHeight', 'letterSpacing', 'textCase', 'textDecoration',
  'textAlignHorizontal', 'textAlignVertical', 'textAutoResize', 'maxLines',
  'layoutMode', 'layoutDirection', 'itemSpacing',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'primaryAxisAlign', 'counterAxisAlign', 'primaryAxisSizing', 'counterAxisSizing',
  'layoutPositioning', 'layoutGrow',
  'componentId', 'autoRename',
  'isMask',
]

function nodeOut(id) {
  const n = graph.getNode(id)
  if (!n) return null
  const abs = graph.getAbsolutePosition(id)
  const out = { id }
  for (const k of RELEVANT) out[k] = n[k] ?? null
  out.abs = { x: abs.x, y: abs.y, width: n.width, height: n.height }
  out.fills = (n.fills || []).map(fillInfo)
  out.strokes = (n.strokes || []).map(strokeInfo)
  out.effects = (n.effects || []).map(effectInfo)
  out.styleRuns = (n.styleRuns || []).map((r) => ({
    text: r.text ?? null,
    fontSize: r.fontSize ?? null,
    fontFamily: r.fontFamily ?? null,
    fontWeight: r.fontWeight ?? null,
    color: r.color ? hex(r.color) : null,
  }))
  out.pluginData = (n.pluginData || []).map((p) => ({
    pluginId: p.pluginId ?? null,
    pluginName: p.pluginName ?? null,
    key: p.key ?? null,
    value: p.value ?? null,
  }))
  out.boundVariables = n.boundVariables && Object.keys(n.boundVariables).length
    ? Object.fromEntries(Object.entries(n.boundVariables).map(([k, v]) => [k, String(v)]))
    : null
  const src = n.source
  out.source = src ? { format: src.format, editedFields: src.editedFields || [] } : null
  return out
}

// Knoten-Reihenfolge: BFS ab den Seiten (deterministisch), danach verwaiste Knoten
const pages = graph.getPages(true)
const seen = new Set()
const ordered = []
const queue = pages.map((p) => p.id)
for (const pid of queue) seen.add(pid)
while (queue.length) {
  const id = queue.shift()
  ordered.push(id)
  const n = graph.getNode(id)
  if (n) for (const c of n.childIds) if (!seen.has(c)) { seen.add(c); queue.push(c) }
}
for (const id of graph.nodes.keys()) if (!seen.has(id)) ordered.push(id)

const nodeDump = ordered.map(nodeOut).filter(Boolean)

// Variablen (Design-Token) zusammenfassen
const variables = []
for (const [vid, v] of graph.variables.entries()) {
  variables.push({
    id: vid,
    name: v.name ?? null,
    type: v.type ?? null,
    values: v.values ? Object.fromEntries(Object.entries(v.values).map(([m, val]) => [m, val && typeof val === 'object' && 'hex' in val ? hex(val) : val])) : null,
  })
}
const collections = []
for (const [cid, c] of graph.variableCollections.entries()) {
  collections.push({ id: cid, name: c.name ?? null, modes: c.modes ? Object.fromEntries(c.modes) : null })
}

const result = {
  meta: {
    tool: '@open-pencil/fig 0.16.0 (pinned tools/openpencil) + @open-pencil/scene-graph 0.16.0',
    input: figPath,
    inputBytes: bytes.length,
    inputSha256: createHash('sha256').update(bytes).digest('hex'),
    figKiwiVersion: parsed.figKiwiVersion,
    recordCount: parsed.nodeChanges.length,
    blobCount: parsed.blobs.length,
    pageCount: pages.length,
    nodeCount: graph.nodes.size,
    materialized: ordered.length,
  },
  pages: pages.map((p) => ({
    id: p.id, name: p.name, childIds: p.childIds,
    fills: (p.fills || []).map(fillInfo),
  })),
  variables,
  variableCollections: collections,
  components: assembly.componentIds ? [...assembly.componentIds.entries()].map(([k, v]) => [k, v]) : null,
  nodes: nodeDump,
}

writeFileSync(outPath, JSON.stringify(result, null, 2) + '\n')
console.log(`wrote ${outPath}: pages=${pages.length} nodes=${graph.nodes.size} records=${parsed.nodeChanges.length} kiwiVersion=${parsed.figKiwiVersion}`)
