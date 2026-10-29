/**
 * render-original.mjs — Phase 2, Schritt 1: aus den Wiedereingelesenen Graphen rendern.
 *
 * Liest eine .fig-Datei mit dem Original-Reader der gepinnten Werkzeugumgebung ein
 * (materializeFigArchive) und rendert die gesamte Seite (alle Top-Level-Kinder)
 * per headlessRenderNodes (CanvasKit, @open-pencil/core 0.16.0) als PNG.
 *
 * Aufruf: node render-original.mjs <einfuegung.autocomplete.fig> <ausgabe.png> [scale]
 * Reines Lesen der Eingabe; schreibt nur die eine PNG-Ausgabedatei.
 */
import { readFileSync, writeFileSync } from 'node:fs'

const NM = 'file:///Users/kcnpxcp/Dev/GitHub/ui-contracts/tools/openpencil/node_modules'
const fig = await import(`${NM}/@open-pencil/fig/dist/index.js`)
const headless = await import(`${NM}/@open-pencil/core/dist/io/formats/raster/headless.js`)

const [figPath, outPath, scaleArg] = process.argv.slice(2)
const scale = Number(scaleArg || 2)
if (!figPath || !outPath) {
  console.error('usage: node render-original.mjs <input.fig> <output.png> [scale]')
  process.exit(2)
}

const bytes = readFileSync(figPath)
const buffer = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength)
const assembly = fig.materializeFigArchive(buffer)
const graph = assembly.graph
const pages = graph.getPages(true)
if (pages.length !== 1) {
  console.error(`unexpected page count: ${pages.length}`)
  process.exit(3)
}
const page = pages[0]
const nodeIds = page.childIds

await headless.initCanvasKit()
const png = await headless.headlessRenderNodes(graph, page.id, nodeIds, {
  scale,
  format: 'PNG',
  quality: 100,
  trimTransparent: false,
})
if (!png) {
  console.error('render failed (null)')
  process.exit(4)
}
writeFileSync(outPath, Buffer.from(png))
console.log(`wrote ${outPath}: ${png.length} bytes, ${page.childIds.length} top-level nodes, scale=${scale}`)
