#!/usr/bin/env node
/**
 * inspect-original.mjs — reads ONLY the two builder .fig files with the pinned
 * OpenPencil toolchain, dumps the scene graph, and normalizes component values.
 *
 * Run from the repository root:
 *   node examples/autocomplete/reproducibility/run-02/review/inspect-original.mjs
 *
 * No network access. Writes original-a.json, original-b.json,
 * normalized-a.json, normalized-b.json into the review directory.
 */
import { readFile, writeFile, stat } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { join, dirname, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const ROOT = process.cwd();
const REVIEW = join(ROOT, 'examples/autocomplete/reproducibility/run-02/review');
const BUILDER = join(ROOT, 'examples/autocomplete/reproducibility/run-02');

const coreEntry = join(ROOT, 'tools/openpencil/node_modules/@open-pencil/core/dist/index.js');
const core = await import(pathToFileURL(coreEntry).href);

const CASE_IDS = ['closed', 'opening', 'loading', 'ready', 'active', 'scroll-end', 'selected', 'empty', 'error', 'disabled'];
const TOKENS = {
  width: 320, inputHeight: 44, fontSize: 14, statusFontSize: 12, lineHeight: 20,
  labelGap: 8, gap: 8, statusGap: 8, rowHeight: 32, maxHeight: 160,
  radius: 8, borderWidth: 1, paddingInline: 12,
  colors: {
    surface: '#FFFFFF', text: '#172B4D', muted: '#64748B', border: '#CBD5E1',
    focus: '#2563EB', highlight: '#EAF2FF', disabled: '#94A3B8', error: '#B91C1C'
  }
};

const sha256 = (buf) => createHash('sha256').update(buf).digest('hex');
const r2 = (n) => Math.round(n * 100) / 100;

function chan(v) {
  // Scene colors are 0..1 floats; tolerate 0..255 input.
  return v > 1 ? v / 255 : v;
}
function colorInfo(c) {
  if (!c) return null;
  const r = Math.round(chan(c.r) * 255);
  const g = Math.round(chan(c.g) * 255);
  const b = Math.round(chan(c.b) * 255);
  const a = c.a === undefined ? 1 : r2(chan(c.a));
  const hex = '#' + [r, g, b].map((v) => v.toString(16).padStart(2, '0').toUpperCase()).join('');
  return { hex, rgb: [r, g, b], alpha: a };
}
function fillInfo(f) {
  return {
    type: f.type,
    visible: f.visible !== false,
    opacity: r2(f.opacity ?? 1),
    color: colorInfo(f.color),
    hasImage: Boolean(f.imageHash),
    gradientStops: f.gradientStops ? f.gradientStops.length : 0
  };
}
function strokeInfo(s) {
  return {
    visible: s.visible !== false,
    color: colorInfo(s.color),
    weight: r2(s.weight ?? 0),
    align: s.align ?? null,
    opacity: r2(s.opacity ?? 1)
  };
}
function effectInfo(e) {
  return {
    type: e.type,
    visible: e.visible !== false,
    color: colorInfo(e.color),
    offset: { x: r2(e.offset?.x ?? 0), y: r2(e.offset?.y ?? 0) },
    radius: r2(e.radius ?? 0),
    spread: r2(e.spread ?? 0)
  };
}

function absPosition(graph, node, cache) {
  if (cache.has(node.id)) return cache.get(node.id);
  let x = node.x ?? 0;
  let y = node.y ?? 0;
  let p = node.parentId;
  const guard = new Set([node.id]);
  while (p) {
    const parent = graph.getNode(p);
    if (!parent || guard.has(parent.id)) break;
    guard.add(parent.id);
    x += parent.x ?? 0;
    y += parent.y ?? 0;
    p = parent.parentId;
  }
  const out = { x: r2(x), y: r2(y) };
  cache.set(node.id, out);
  return out;
}

function clipAncestors(graph, node) {
  const out = [];
  let p = node.parentId;
  while (p) {
    const parent = graph.getNode(p);
    if (!parent) break;
    if (parent.clipsContent) {
      const a = absPosition(graph, parent, new Map());
      out.push({ id: parent.id, name: parent.name, x: a.x, y: a.y, w: r2(parent.width), h: r2(parent.height) });
    }
    p = parent.parentId;
  }
  return out;
}

function visibleChain(graph, node) {
  let p = node.parentId;
  const chain = [];
  while (p) {
    const parent = graph.getNode(p);
    if (!parent) break;
    if (parent.visible === false) chain.push(parent.id);
    p = parent.parentId;
  }
  return chain;
}

async function inspect(label, file) {
  const buf = await readFile(file);
  const graph = await core.parseFigFile(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength), { populate: 'all' });
  const info = await core.getSceneInfo ? null : null;
  const pages = graph.getPages(true).map((p) => ({ id: p.id, name: p.name }));
  const absCache = new Map();
  const nodes = [];
  for (const node of graph.getAllNodes()) {
    if (!node || node.type === 'DOCUMENT') continue;
    const a = absPosition(graph, node, absCache);
    nodes.push({
      id: node.id,
      type: node.type,
      name: node.name,
      parentId: node.parentId,
      childIds: [...(node.childIds ?? [])],
      local: { x: r2(node.x ?? 0), y: r2(node.y ?? 0) },
      abs: a,
      size: { w: r2(node.width ?? 0), h: r2(node.height ?? 0) },
      rotation: r2(node.rotation ?? 0),
      visible: node.visible !== false,
      hiddenByAncestor: visibleChain(graph, node),
      opacity: r2(node.opacity ?? 1),
      clipsContent: Boolean(node.clipsContent),
      cornerRadius: r2(node.cornerRadius ?? 0),
      independentCorners: Boolean(node.independentCorners),
      fills: (node.fills ?? []).map(fillInfo),
      strokes: (node.strokes ?? []).map(strokeInfo),
      effects: (node.effects ?? []).map(effectInfo),
      layout: {
        mode: node.layoutMode ?? 'NONE',
        direction: node.layoutDirection ?? null,
        primaryAxisAlign: node.primaryAxisAlign ?? null,
        counterAxisAlign: node.counterAxisAlign ?? null,
        itemSpacing: r2(node.itemSpacing ?? 0),
        padding: [r2(node.paddingTop ?? 0), r2(node.paddingRight ?? 0), r2(node.paddingBottom ?? 0), r2(node.paddingLeft ?? 0)],
        primaryAxisSizing: node.primaryAxisSizing ?? null,
        counterAxisSizing: node.counterAxisSizing ?? null,
        position: node.layoutPositioning ?? null
      },
      text: node.type === 'TEXT' ? {
        value: node.text ?? '',
        fontFamily: node.fontFamily ?? null,
        fontSize: r2(node.fontSize ?? 0),
        fontWeight: node.fontWeight ?? null,
        italic: Boolean(node.italic),
        lineHeight: node.lineHeight === null || node.lineHeight === undefined ? null : r2(node.lineHeight),
        letterSpacing: r2(node.letterSpacing ?? 0),
        align: node.textAlignHorizontal ?? null,
        alignVertical: node.textAlignVertical ?? null,
        autoResize: node.textAutoResize ?? null,
        maxLines: node.maxLines ?? null,
        case: node.textCase ?? null,
        styleRuns: (node.styleRuns ?? []).length
      } : null,
      isText: node.type === 'TEXT',
      hasImageFill: (node.fills ?? []).some((f) => Boolean(f.imageHash)),
      vectorNetwork: node.vectorNetwork ? { vertices: node.vectorNetwork.vertices?.length ?? 0 } : null
    });
  }

  // ---------- case grouping ----------
  const pageTypes = new Set(['PAGE', 'CANVAS']);
  const frames = nodes.filter((n) => n.parentId && pageTypes.has(nodes.find((p) => p.id === n.parentId)?.type));
  const caseFrames = nodes.filter((n) => (n.type === 'FRAME' || n.type === 'COMPONENT') && /^Autocomplete\s*\/\s*/i.test(n.name));
  const cases = {};
  for (const cf of caseFrames) {
    const id = cf.name.split('/').pop().trim();
    cases[id] = { frameId: cf.id, name: cf.name, frame: cf, children: [] };
  }
  const byId = new Map(nodes.map((n) => [n.id, n]));
  const descendants = (id) => {
    const out = [];
    const walk = (nid) => {
      const n = byId.get(nid);
      if (!n) return;
      for (const cid of n.childIds) {
        const c = byId.get(cid);
        if (!c) continue;
        out.push(c);
        walk(cid);
      }
    };
    walk(id);
    return out;
  };

  const norm = { design: label, sourceFile: file, caseOrder: [], cases: {}, global: {} };
  const allCaseIds = Object.keys(cases);
  norm.caseOrder = CASE_IDS.filter((c) => cases[c]).concat(allCaseIds.filter((c) => !CASE_IDS.includes(c)));

  for (const cid of allCaseIds) {
    const c = cases[cid];
    const nodesIn = descendants(c.frameId);
    c.nodes = nodesIn.map((n) => n.id);
    const pick = (pred) => nodesIn.filter(pred);
    const byName = (re) => pick((n) => re.test(n.name));

    const label = pick((n) => n.type === 'TEXT' && /(^|[^a-z])label($|[^a-z])/i.test(n.name) && !/option/i.test(n.name))[0] ?? null;
    const input = pick((n) => n.type !== 'TEXT' && /(^|[^.\s])input$/i.test(n.name.trim()))[0]
      ?? pick((n) => n.type !== 'TEXT' && /^input/i.test(n.name) && !/text|placeholder|value/i.test(n.name))[0]
      ?? null;
    const surface = byName(/surface/i)[0] ?? null;
    const viewport = byName(/viewport/i)[0] ?? null;
    const list = pick((n) => /^list$/i.test(n.name.trim()))[0]
      ?? pick((n) => /(^|[^a-z])list([^a-z]|$)/i.test(n.name) && !/message|option/i.test(n.name))[0]
      ?? null;
    const optionNodes = pick((n) => /option/i.test(n.name) && n.type !== 'TEXT' && !/label$/i.test(n.name));
    const optionTexts = pick((n) => n.type === 'TEXT' && /option/i.test(n.name));
    const status = pick((n) => n.type === 'TEXT' && /status/i.test(n.name))[0] ?? null;
    const message = pick((n) => n.type === 'TEXT' && /message/i.test(n.name))[0] ?? null;
    const inputText = input ? pick((n) => n.type === 'TEXT' && n.parentId === input.id)[0] ?? null : null;

    const options = optionNodes
      .map((o) => {
        const t = pick((n) => n.type === 'TEXT' && n.parentId === o.id)[0]
          ?? optionTexts.find((x) => x.parentId === o.id) ?? null;
        const keyMatch = o.name.match(/option[\/\s_-]+([a-zäöüß]+)/i);
        return {
          nodeId: o.id,
          name: o.name,
          key: keyMatch ? keyMatch[1].toLowerCase() : null,
          text: t ? t.text.value : null,
          textNodeId: t ? t.id : null,
          bbox: { x: o.abs.x, y: o.abs.y, w: o.size.w, h: o.size.h },
          fill: o.fills.filter((f) => f.visible && f.type === 'SOLID').map((f) => f.color.hex),
          cornerRadius: o.cornerRadius,
          opacity: o.opacity,
          visible: o.visible,
          clipsContent: o.clipsContent,
          textColor: t ? (t.fills.filter((f) => f.visible).map((f) => f.color.hex)[0] ?? null) : null,
          textBBox: t ? { x: t.abs.x, y: t.abs.y, w: t.size.w, h: t.size.h } : null,
          textFont: t ? { family: t.text.fontFamily, size: t.text.fontSize, weight: t.text.fontWeight, lineHeight: t.text.lineHeight } : null
        };
      })
      .sort((a, b) => a.bbox.y - b.bbox.y);

    const rel = (n) => n ? { x: r2(n.abs.x - c.frame.abs.x), y: r2(n.abs.y - c.frame.abs.y), w: n.size.w, h: n.size.h } : null;
    const fillsOf = (n) => n ? n.fills.filter((f) => f.visible) : [];
    const strokeOf = (n) => {
      if (!n) return null;
      const s = n.strokes.find((x) => x.visible);
      return s ? { color: s.color.hex, weight: s.weight, align: s.align } : null;
    };

    const entry = {
      caseId: cid,
      frame: {
        nodeId: c.frameId,
        name: c.frame.name,
        type: c.frame.type,
        bbox: { x: c.frame.abs.x, y: c.frame.abs.y, w: c.frame.size.w, h: c.frame.size.h },
        fills: fillsOf(c.frame).map((f) => f.color.hex),
        clipsContent: c.frame.clipsContent,
        layoutMode: c.frame.layout.mode,
        itemSpacing: c.frame.layout.itemSpacing,
        padding: c.frame.layout.padding,
        childOrder: c.frame.childIds.map((id) => byId.get(id)?.name)
      },
      parts: {
        label: label ? { nodeId: label.id, name: label.name, bbox: rel(label), text: label.text.value, font: label.text, fill: fillsOf(label).map((f) => f.color.hex), visible: label.visible } : null,
        input: input ? {
          nodeId: input.id, name: input.name, bbox: rel(input), fill: fillsOf(input).map((f) => f.color.hex),
          stroke: strokeOf(input), strokeCount: input.strokes.filter((s) => s.visible).length,
          cornerRadius: input.cornerRadius, opacity: input.opacity,
          textNode: inputText ? { nodeId: inputText.id, text: inputText.text.value, font: inputText.text, fill: fillsOf(inputText).map((f) => f.color.hex), bbox: rel(inputText) } : null
        } : null,
        surface: surface ? { nodeId: surface.id, name: surface.name, bbox: rel(surface), fill: fillsOf(surface).map((f) => f.color.hex), stroke: strokeOf(surface), strokeCount: surface.strokes.filter((s) => s.visible).length, cornerRadius: surface.cornerRadius, effects: surface.effects, clipsContent: surface.clipsContent, visible: surface.visible } : null,
        viewport: viewport ? { nodeId: viewport.id, name: viewport.name, bbox: rel(viewport), fill: fillsOf(viewport).map((f) => f.color.hex), clipsContent: viewport.clipsContent, cornerRadius: viewport.cornerRadius, maxHeight: viewport.maxHeight, visible: viewport.visible } : null,
        list: list ? { nodeId: list.id, name: list.name, bbox: rel(list), layoutMode: list.layout.mode, itemSpacing: list.layout.itemSpacing, padding: list.layout.padding, visible: list.visible, childCount: list.childIds.length } : null,
        status: status ? { nodeId: status.id, name: status.name, bbox: rel(status), text: status.text.value, font: status.text, fill: fillsOf(status).map((f) => f.color.hex), visible: status.visible } : null,
        message: message ? { nodeId: message.id, name: message.name, bbox: rel(message), text: message.text.value, font: message.text, fill: fillsOf(message).map((f) => f.color.hex) } : null
      },
      options,
      optionCount: options.length,
      textInventory: nodesIn.filter((n) => n.type === 'TEXT').map((n) => ({ id: n.id, name: n.name, text: n.text.value, fontSize: n.text.fontSize, fontFamily: n.text.fontFamily, fill: fillsOf(n).map((f) => f.color.hex) })),
      visibleTexts: nodesIn.filter((n) => n.type === 'TEXT' && n.visible && n.hiddenByAncestor.length === 0 && n.opacity > 0.01).map((n) => n.text.value)
    };
    norm.cases[cid] = entry;
  }

  norm.global = {
    pages,
    nodeCount: nodes.length,
    textNodes: nodes.filter((n) => n.type === 'TEXT').length,
    frameNodes: nodes.filter((n) => n.type === 'FRAME').length,
    componentNodes: nodes.filter((n) => n.type === 'COMPONENT').length,
    imageFills: nodes.filter((n) => n.hasImageFill).length,
    vectorNodes: nodes.filter((n) => n.vectorNetwork).length,
    fonts: [...new Set(nodes.filter((n) => n.type === 'TEXT').map((n) => n.text.fontFamily))],
    textSizes: [...new Set(nodes.filter((n) => n.type === 'TEXT').map((n) => n.text.fontSize))].sort((a, b) => a - b),
    pageNames: pages.map((p) => p.name)
  };

  const original = {
    design: label,
    file,
    fileSha256: sha256(buf),
    fileBytes: (await stat(file)).size,
    toolchain: { core: '0.16.0', cli: '0.16.0', sceneGraph: '0.16.0' },
    info: {
      pages: pages.length,
      pageNames: pages.map((p) => p.name),
      nodeCount: nodes.length,
      types: nodes.reduce((acc, n) => { acc[n.type] = (acc[n.type] ?? 0) + 1; return acc; }, {}),
      fonts: norm.global.fonts
    },
    nodes
  };
  return { original, norm };
}

const a = await inspect('A', join(BUILDER, 'builder-a/autocomplete.fig'));
const b = await inspect('B', join(BUILDER, 'builder-b/autocomplete.fig'));

await writeFile(join(REVIEW, 'original-a.json'), JSON.stringify(a.original, null, 2) + '\n');
await writeFile(join(REVIEW, 'original-b.json'), JSON.stringify(b.original, null, 2) + '\n');
await writeFile(join(REVIEW, 'normalized-a.json'), JSON.stringify(a.norm, null, 2) + '\n');
await writeFile(join(REVIEW, 'normalized-b.json'), JSON.stringify(b.norm, null, 2) + '\n');

console.log(JSON.stringify({
  a: { nodes: a.original.nodes.length, cases: Object.keys(a.norm.cases), bytes: a.original.fileBytes, sha: a.original.fileSha256 },
  b: { nodes: b.original.nodes.length, cases: Object.keys(b.norm.cases), bytes: b.original.fileBytes, sha: b.original.fileSha256 }
}, null, 2));
