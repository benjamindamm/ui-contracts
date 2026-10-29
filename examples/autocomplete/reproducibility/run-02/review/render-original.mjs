#!/usr/bin/env node
/**
 * render-original.mjs — renders the two builder .fig files with the pinned
 * OpenPencil headless renderer (CanvasKit WASM, no network).
 *
 * Run from the repository root:
 *   node examples/autocomplete/reproducibility/run-02/review/render-original.mjs
 *
 * Writes render-a.png and render-b.png (whole page, scale 2) plus a small
 * render-meta.json with page ids, bounds and byte sizes.
 */
import { readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

const ROOT = process.cwd();
const REVIEW = join(ROOT, 'examples/autocomplete/reproducibility/run-02/review');
const BUILDER = join(ROOT, 'examples/autocomplete/reproducibility/run-02');

const core = await import(pathToFileURL(join(ROOT, 'tools/openpencil/node_modules/@open-pencil/core/dist/index.js')).href);

async function renderOne(label) {
  const file = join(BUILDER, `builder-${label}/autocomplete.fig`);
  const buf = await readFile(file);
  const graph = await core.parseFigFile(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength), { populate: 'all' });

  const pages = graph.getPages(true);
  // The page that actually holds the component (B also ships an empty "Page 1").
  const page = pages.find((p) => (p.childIds ?? []).length > 0) ?? pages[0];
  const childIds = [...(page.childIds ?? [])];

  // Bounding box of the page content, used only for logging.
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  const walk = (id) => {
    const n = graph.getNode(id);
    if (!n) return;
    minX = Math.min(minX, n.x ?? 0);
    minY = Math.min(minY, n.y ?? 0);
    maxX = Math.max(maxX, (n.x ?? 0) + (n.width ?? 0));
    maxY = Math.max(maxY, (n.y ?? 0) + (n.height ?? 0));
    for (const c of n.childIds ?? []) walk(c);
  };
  childIds.forEach(walk);

  const png = await core.headlessRenderNodes(graph, page.id, childIds, { scale: 2, format: 'png' });
  if (!png) throw new Error(`render returned null for ${label}`);
  await writeFile(join(REVIEW, `render-${label}.png`), png);

  return {
    design: label.toUpperCase(),
    file,
    pageId: page.id,
    pageName: page.name,
    pages: pages.map((p) => ({ id: p.id, name: p.name, children: (p.childIds ?? []).length })),
    contentBounds: { x: minX, y: minY, w: maxX - minX, h: maxY - minY },
    scale: 2,
    pngBytes: png.length,
    pngSignature: Array.from(png.slice(0, 8))
  };
}

const a = await renderOne('a');
const b = await renderOne('b');
await writeFile(join(REVIEW, 'render-meta.json'), JSON.stringify({ a, b }, null, 2) + '\n');
console.log(JSON.stringify({ a, b }, null, 2));
