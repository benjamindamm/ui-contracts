#!/usr/bin/env node
/**
 * Builder B — erzeugt aus components/** ein editierbares OpenPencil-Dokument.
 *
 * Ausführen vom Repo-Root:
 *   node examples/autocomplete/reproducibility/run-02/builder-b/generate.mjs
 *
 * Keine Netzwerkabhängigkeit. Nur @open-pencil/core 0.16.0 aus tools/openpencil/.
 */

import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '../../../../../');
const OUT = HERE;
const CORE_PKG = path.join(ROOT, 'tools/openpencil/node_modules/@open-pencil/core/package.json');
const CORE_ENTRY = path.join(ROOT, 'tools/openpencil/node_modules/@open-pencil/core/dist/index.js');

const core = await import(CORE_ENTRY);
const { SceneGraph, exportFigFile, parseFigFile, initCanvasKit, headlessRenderNodes, renderNodesToSVG } = core;

/* ------------------------------------------------------------------ */
/* Definition: tokens (components/tokens.json)                        */
/* ------------------------------------------------------------------ */

const T = {
  width: 320,
  inputHeight: 44,
  fontSize: 14,
  statusFontSize: 12,
  lineHeight: 20,
  labelGap: 8,
  statusGap: 8,
  radius: 8,
  borderWidth: 1,
  paddingInline: 12,
  rowHeight: 32,
  maxHeight: 160,
  gap: 8,
  fontFamily: 'Inter',
  color: {
    surface: '#FFFFFF',
    text: '#172B4D',
    muted: '#64748B',
    border: '#CBD5E2',
    focus: '#2563EB',
    highlight: '#EAF2FF',
    disabled: '#94A3B8',
    error: '#B91C1C',
  },
};

const LABEL = 'Stadt auswählen';
const PLACEHOLDER = 'Stadt suchen …';

const RESULTS = [
  { key: 'berlin', label: 'Berlin' },
  { key: 'hamburg', label: 'Hamburg' },
  { key: 'muenchen', label: 'München', disabled: true },
  { key: 'dresden', label: 'Dresden' },
  { key: 'koeln', label: 'Köln' },
  { key: 'wien', label: 'Wien' },
  { key: 'zuerich', label: 'Zürich' },
];

// Nachrichten aus components/autocomplete/accessibility.rules.json (locale de).
const MSG = {
  closed: '',
  opening: 'Suche wird geöffnet.',
  loading: 'Städte werden geladen.',
  results: (count) => `${count} Städte verfügbar.`,
  empty: 'Keine Städte gefunden.',
  error: 'Städte konnten nicht geladen werden.',
  selected: (label) => `Ausgewählt: ${label}.`,
  disabled: '',
};

/* ------------------------------------------------------------------ */
/* Zehn Fälle (stories.json + README-Zuordnung)                        */
/* ------------------------------------------------------------------ */

const CASES = [
  { id: 'closed', phase: 'closed', query: '', popup: null, status: MSG.closed },
  { id: 'opening', phase: 'opening', query: '', popup: null, status: MSG.opening, focus: true },
  { id: 'loading', phase: 'loading', query: 'Be', popup: { message: MSG.loading }, status: MSG.loading, focus: true },
  {
    id: 'ready', phase: 'ready', query: '', popup: { results: RESULTS }, status: MSG.results(RESULTS.length), focus: true,
  },
  {
    id: 'active', phase: 'ready', query: '', popup: { results: RESULTS, activeKey: 'hamburg' },
    status: MSG.results(RESULTS.length), focus: true,
  },
  {
    id: 'scroll-end', phase: 'ready', query: '', popup: { results: RESULTS, activeKey: 'zuerich', scrollToEnd: true },
    status: MSG.results(RESULTS.length), focus: true,
  },
  { id: 'selected', phase: 'closed', query: 'Berlin', value: 'berlin', popup: null, status: MSG.selected('Berlin') },
  { id: 'empty', phase: 'empty', query: 'Atlantis', popup: { message: MSG.empty }, status: MSG.empty, focus: true },
  { id: 'error', phase: 'error', query: 'Be', popup: { message: MSG.error }, status: MSG.error, statusTone: 'error', focus: true },
  { id: 'disabled', phase: 'closed', enabled: false, query: '', popup: null, status: MSG.disabled },
];

/* ------------------------------------------------------------------ */
/* Farb- und Texthelfer                                               */
/* ------------------------------------------------------------------ */

function hexToColor(hex) {
  const h = hex.replace('#', '');
  return {
    r: parseInt(h.slice(0, 2), 16) / 255,
    g: parseInt(h.slice(2, 4), 16) / 255,
    b: parseInt(h.slice(4, 6), 16) / 255,
    a: 1,
  };
}

const solid = (hex) => ({ type: 'SOLID', color: hexToColor(hex), opacity: 1, visible: true });

let idSeq = 0;
const nextId = () => `b${(++idSeq).toString(36).padStart(6, '0')}`;

const graph = new SceneGraph(nextId);
const page = graph.addPage('Autocomplete');

function node(type, parentId, props) {
  return graph.createNode(type, parentId, props);
}

function textNode(parentId, name, props) {
  return node('TEXT', parentId, {
    name,
    fills: [solid(props.color ?? T.color.text)],
    fontSize: props.fontSize ?? T.fontSize,
    fontFamily: T.fontFamily,
    fontWeight: 400,
    lineHeight: props.lineHeight ?? T.lineHeight,
    textAlignHorizontal: 'LEFT',
    textAlignVertical: 'CENTER',
    textAutoResize: 'NONE',
    text: props.text,
    ...props.extra,
  });
}

/* ------------------------------------------------------------------ */
/* Sheetrahmen (freie Außenanordnung)                                 */
/* ------------------------------------------------------------------ */

const COL_W = T.width;
const COL_GAP = 72;
const ROW_GAP = 64;
const SHEET_PAD = 40;
const HEADER = 110;

const caseHeights = CASES.map((c) => {
  if (!c.popup) return T.lineHeight + T.labelGap + T.inputHeight + T.statusGap + T.lineHeight;
  const viewport = c.popup.results ? Math.min(c.popup.results.length * T.rowHeight, T.maxHeight) : T.rowHeight;
  return T.lineHeight + T.labelGap + T.inputHeight + T.gap + viewport + T.statusGap + T.lineHeight;
});
const rowHeights = [Math.max(...caseHeights.slice(0, 5)), Math.max(...caseHeights.slice(5))];

const cols = 5;
const sheetW = SHEET_PAD * 2 + cols * COL_W + (cols - 1) * COL_GAP;
const sheetH = HEADER + rowHeights[0] + ROW_GAP + rowHeights[1] + SHEET_PAD;

const sheet = node('FRAME', page.id, {
  name: 'Autocomplete · Übersicht',
  x: 0,
  y: 0,
  width: sheetW,
  height: sheetH,
  fills: [solid('#F2F4F7')],
  clipsContent: false,
});

textNode(sheet.id, 'sheet-title', {
  text: 'Autocomplete — zehn benannte Zustände',
  fontSize: 20,
  lineHeight: 28,
  color: T.color.text,
  extra: { x: SHEET_PAD, y: 36, width: sheetW - SHEET_PAD * 2, height: 28 },
});

textNode(sheet.id, 'sheet-note', {
  text: 'ui-contracts:Autocomplete 0.1.0 · statische Darstellung aus components/** · editierbare Teile: label, input, overlay.surface, overlay.scroll.viewport, list, option, status',
  fontSize: 12,
  lineHeight: 20,
  color: T.color.muted,
  extra: { x: SHEET_PAD, y: 68, width: sheetW - SHEET_PAD * 2, height: 20 },
});

/* ------------------------------------------------------------------ */
/* Ein Fall                                                           */
/* ------------------------------------------------------------------ */

function buildCase(spec, index) {
  const col = index % cols;
  const row = Math.floor(index / cols);
  const x = SHEET_PAD + col * (COL_W + COL_GAP);
  const y = HEADER + (row === 0 ? 0 : rowHeights[0] + ROW_GAP);
  const height = caseHeights[index];

  const root = node('COMPONENT', sheet.id, {
    name: `Autocomplete / ${spec.id}`,
    x,
    y,
    width: T.width,
    height,
    fills: [],
    clipsContent: false,
  });

  // label
  textNode(root.id, 'label', {
    text: LABEL,
    color: T.color.text,
    extra: { x: 0, y: 0, width: T.width, height: T.lineHeight },
  });

  // input
  const inputY = T.lineHeight + T.labelGap;
  const disabled = spec.enabled === false;
  const borderColor = disabled
    ? T.color.border
    : spec.focus
      ? T.color.focus
      : T.color.border;

  const input = node('FRAME', root.id, {
    name: 'input',
    x: 0,
    y: inputY,
    width: T.width,
    height: T.inputHeight,
    fills: [solid(T.color.surface)],
    cornerRadius: T.radius,
    topLeftRadius: T.radius,
    topRightRadius: T.radius,
    bottomLeftRadius: T.radius,
    bottomRightRadius: T.radius,
    clipsContent: true,
    strokes: [{
      type: 'SOLID',
      color: hexToColor(borderColor),
      opacity: 1,
      visible: true,
      weight: T.borderWidth,
      align: 'INSIDE',
    }],
  });

  const hasValue = spec.query !== '';
  const inputTextColor = disabled
    ? T.color.disabled
    : hasValue
      ? T.color.text
      : T.color.muted;

  textNode(input.id, hasValue ? 'input/value' : 'input/placeholder', {
    text: hasValue ? spec.query : PLACEHOLDER,
    color: inputTextColor,
    extra: {
      x: T.borderWidth + T.paddingInline,
      y: (T.inputHeight - T.lineHeight) / 2,
      width: T.width - 2 * (T.borderWidth + T.paddingInline),
      height: T.lineHeight,
    },
  });

  const inputBottom = inputY + T.inputHeight;
  let popupBottom = inputBottom;

  if (spec.popup) {
    const rows = spec.popup.results ? spec.popup.results.length : 1;
    const contentH = rows * T.rowHeight;
    const viewportH = Math.min(contentH, T.maxHeight);
    const offset = spec.popup.scrollToEnd ? contentH - viewportH : 0;

    const surface = node('FRAME', root.id, {
      name: 'overlay.surface',
      x: 0,
      y: inputBottom + T.gap,
      width: T.width,
      height: viewportH,
      fills: [solid(T.color.surface)],
      cornerRadius: T.radius,
      topLeftRadius: T.radius,
      topRightRadius: T.radius,
      bottomLeftRadius: T.radius,
      bottomRightRadius: T.radius,
      clipsContent: true,
      effects: [{
        type: 'DROP_SHADOW',
        color: { r: 0, g: 0, b: 0, a: 0.2 },
        offset: { x: 0, y: 2 },
        radius: 8,
        spread: 0,
        visible: true,
        blendMode: 'NORMAL',
        showShadowBehindNode: false,
      }],
    });

    const viewport = node('FRAME', surface.id, {
      name: 'overlay.scroll.viewport',
      x: 0,
      y: 0,
      width: T.width,
      height: viewportH,
      fills: [],
      clipsContent: true,
    });

    const list = node('FRAME', viewport.id, {
      name: 'list',
      x: 0,
      y: -offset,
      width: T.width,
      height: contentH,
      fills: [],
      clipsContent: false,
    });

    if (spec.popup.results) {
      spec.popup.results.forEach((result) => {
        const selected = spec.popup.activeKey === result.key;
        const option = node('FRAME', list.id, {
          name: `option/${result.key}`,
          x: 0,
          y: RESULTS.indexOf(result) * T.rowHeight,
          width: T.width,
          height: T.rowHeight,
          fills: selected ? [solid(T.color.highlight)] : [],
          clipsContent: false,
        });
        textNode(option.id, `option/${result.key}/label`, {
          text: result.label,
          color: result.disabled ? T.color.disabled : T.color.text,
          extra: {
            x: T.paddingInline,
            y: (T.rowHeight - T.lineHeight) / 2,
            width: T.width - 2 * T.paddingInline,
            height: T.lineHeight,
          },
        });
      });
    } else {
      const rowNode = node('FRAME', list.id, {
        name: 'list/message-row',
        x: 0,
        y: 0,
        width: T.width,
        height: T.rowHeight,
        fills: [],
        clipsContent: false,
      });
      textNode(rowNode.id, 'list/message', {
        text: spec.popup.message,
        color: T.color.muted,
        extra: {
          x: T.paddingInline,
          y: (T.rowHeight - T.lineHeight) / 2,
          width: T.width - 2 * T.paddingInline,
          height: T.lineHeight,
        },
      });
    }

    popupBottom = inputBottom + T.gap + viewportH;
  }

  // status: unter sichtbarem Popup, sonst unter dem Input
  const statusY = popupBottom + T.statusGap;
  textNode(root.id, 'status', {
    text: spec.status ?? '',
    color: spec.statusTone === 'error' ? T.color.error : T.color.muted,
    fontSize: T.statusFontSize,
    lineHeight: T.lineHeight,
    extra: { x: 0, y: statusY, width: T.width, height: T.lineHeight },
  });

  return root;
}

CASES.forEach((spec, i) => buildCase(spec, i));

/* ------------------------------------------------------------------ */
/* Export                                                             */
/* ------------------------------------------------------------------ */

const figPath = path.join(OUT, 'autocomplete.fig');
const figBytes = await exportFigFile(graph, undefined, undefined, page.id, false);
fs.writeFileSync(figPath, figBytes);

/* ------------------------------------------------------------------ */
/* Selbstprüfung: mit dem Originalreader zurücklesen                  */
/* ------------------------------------------------------------------ */

const buf = figBytes.buffer.slice(figBytes.byteOffset, figBytes.byteOffset + figBytes.byteLength);
const read = await parseFigFile(buf, { populate: 'all' });

const coreVersion = JSON.parse(fs.readFileSync(CORE_PKG, 'utf8')).version;

function allNodes(g, rootId) {
  const out = [];
  const walk = (id) => {
    const n = g.getNode(id);
    if (!n) return;
    out.push(n);
    for (const c of n.childIds) walk(c);
  };
  walk(rootId);
  return out;
}

const pages = read.getPages();
const readPage = pages.find((p) => p.name === 'Autocomplete') ?? pages[0];
const readSheet = allNodes(read, readPage.id).find((n) => n.name === 'Autocomplete · Übersicht');

const rgba255 = (c) => ({
  r: Math.round(c.r * 255),
  g: Math.round(c.g * 255),
  b: Math.round(c.b * 255),
  a: Number(c.a.toFixed(3)),
});
const hex = (c) => `#${[c.r, c.g, c.b].map((v) => Math.round(v * 255).toString(16).padStart(2, '0')).join('').toUpperCase()}`;

function measureCase(component) {
  const nodes = allNodes(read, component.id);
  const byName = (name) => nodes.find((n) => n.name === name && n.id !== component.id);
  const input = byName('input');
  const inputText = input ? nodes.find((n) => n.name === 'input/value' || n.name === 'input/placeholder') : undefined;
  const surface = byName('overlay.surface');
  const viewport = byName('overlay.scroll.viewport');
  const list = byName('list');
  const status = byName('status');
  const optionFrames = nodes.filter((n) => /^option\//.test(n.name) && !/\/label$/.test(n.name));
  const messageRow = byName('list/message-row');
  const message = byName('list/message');

  let visibleOptions = [];
  if (viewport && list) {
    const vpTop = read.getAbsolutePosition(viewport.id).y;
    const vpBottom = vpTop + viewport.height;
    visibleOptions = optionFrames
      .map((o) => {
        const top = read.getAbsolutePosition(o.id).y;
        return { name: o.name, top, bottom: top + o.height, visible: top >= vpTop - 0.001 && top + o.height <= vpBottom + 0.001 };
      })
      .map((o) => ({ ...o, name: o.name.replace(/^option\//, '') }));
  }

  const optionLabels = optionFrames.map((o) => {
    const label = read.getNode(o.childIds[0]);
    return { key: o.name.replace(/^option\//, ''), text: label?.text ?? null, color: label && label.fills[0] ? hex(label.fills[0].color) : null, fill: o.fills.length ? hex(o.fills[0].color) : null };
  });

  const anchorBottom = surface ? surface.y + surface.height : input ? input.y + input.height : 0;

  return {
    id: component.name.replace('Autocomplete / ', ''),
    name: component.name,
    bounds: { x: component.x, y: component.y, width: component.width, height: component.height },
    statusOffsetFromAnchor: status ? status.y - anchorBottom : null,
    input: input
      ? {
          width: input.width,
          height: input.height,
          cornerRadius: input.cornerRadius,
          borderColor: input.strokes[0] ? hex(input.strokes[0].color) : null,
          borderWidth: input.strokes[0]?.weight ?? null,
          text: inputText?.text ?? null,
          textColor: inputText?.fills[0] ? hex(inputText.fills[0].color) : null,
          fontSize: inputText?.fontSize ?? null,
        }
      : null,
    popup: surface
      ? {
          visible: true,
          height: surface.height,
          width: surface.width,
          cornerRadius: surface.cornerRadius,
          shadow: surface.effects[0]
            ? { type: surface.effects[0].type, offsetY: surface.effects[0].offset.y, blur: surface.effects[0].radius, alpha: surface.effects[0].color.a }
            : null,
          viewportHeight: viewport?.height ?? null,
          viewportClipsContent: viewport?.clipsContent ?? null,
          contentHeight: list?.height ?? null,
          contentOffsetY: list?.y ?? null,
          message: message?.text ?? null,
          optionCount: optionFrames.length,
          optionRowHeight: optionFrames[0]?.height ?? null,
          options: optionLabels,
          highlighted: optionFrames.filter((o) => o.fills.length > 0).map((o) => o.name.replace(/^option\//, '')),
          visibleOptions: visibleOptions.filter((o) => o.visible).map((o) => o.name),
          clippedOptions: visibleOptions.filter((o) => !o.visible).map((o) => o.name),
        }
      : { visible: false },
    status: status
      ? {
          text: status.text,
          color: status.fills[0] ? hex(status.fills[0].color) : null,
          fontSize: status.fontSize,
          height: status.height,
          y: status.y,
        }
      : null,
    parts: nodes.filter((n) => n.id !== component.id).map((n) => ({ name: n.name, type: n.type })),
  };
}

const caseComponents = allNodes(read, readPage.id).filter((n) => /^Autocomplete \/ /.test(n.name));

const allReadNodes = allNodes(read, readPage.id);
const textNodes = allReadNodes.filter((n) => n.type === 'TEXT');

// Textknoten müssen editierbar sein: Zeicheninhalt kommt aus dem Reader, nicht aus einem Bild.
const editableText = textNodes.every((n) => typeof n.text === 'string');

const checks = {
  writer: { package: '@open-pencil/core', version: coreVersion, api: 'exportFigFile' },
  reader: { package: '@open-pencil/core', version: coreVersion, api: 'parseFigFile' },
  file: {
    path: 'autocomplete.fig',
    bytes: figBytes.byteLength,
    sha256: crypto.createHash('sha256').update(figBytes).digest('hex'),
  },
  counts: {
    // nodesInFile zählt den Seitenknoten mit; nodesOnPage entspricht der CLI-Anzeige.
    nodesInFile: allReadNodes.length,
    nodesOnPage: allReadNodes.length - 1,
    textNodes: textNodes.length,
    editableTextNodes: textNodes.filter((n) => typeof n.text === 'string').length,
    allTextNodesEditable: editableText,
    caseComponents: caseComponents.length,
    optionNodes: allReadNodes.filter((n) => /^option\//.test(n.name) && !/\/label$/.test(n.name)).length,
  },
  page: { name: readPage.name },
  sheet: { name: readSheet?.name ?? null, width: sheetW, height: sheetH },
  cases: caseComponents.map(measureCase),
};

/* ------------------------------------------------------------------ */
/* Vorschauen                                                         */
/* ------------------------------------------------------------------ */

const renderReport = { png: 'skipped', svg: 'skipped', note: '' };
try {
  const ck = await initCanvasKit();
  const png = await headlessRenderNodes(read, readPage.id, [readSheet.id], { scale: 2, format: 'PNG', trimTransparent: false });
  if (!png) throw new Error('headlessRenderNodes returned null');
  fs.writeFileSync(path.join(OUT, 'preview.png'), png);
  renderReport.png = `ok (${png.byteLength} bytes, scale 2)`;
} catch (err) {
  renderReport.png = `failed: ${err.message}`;
  console.error('PNG rendering failed:', err);
}

try {
  const svg = renderNodesToSVG(read, readPage.id, [readSheet.id]);
  if (!svg) throw new Error('renderNodesToSVG returned null');
  fs.writeFileSync(path.join(OUT, 'preview.svg'), svg);
  renderReport.svg = `ok (${Buffer.byteLength(svg)} bytes)`;
} catch (err) {
  renderReport.svg = `failed: ${err.message}`;
  console.error('SVG rendering failed:', err);
}

checks.render = renderReport;
fs.writeFileSync(path.join(OUT, 'checks.json'), JSON.stringify(checks, null, 2) + '\n');

/* ------------------------------------------------------------------ */
/* Hashes der gelesenen Definitionsdateien                            */
/* ------------------------------------------------------------------ */

const DEFINITION_FILES = [
  'components/README.md',
  'components/library.json',
  'components/tokens.json',
  'components/autocomplete/README.md',
  'components/autocomplete/accessibility.html',
  'components/autocomplete/accessibility.rules.json',
  'components/autocomplete/behavior.scxml',
  'components/autocomplete/component.json',
  'components/autocomplete/error-relay.scxml',
  'components/autocomplete/interface.json',
  'components/autocomplete/layout.css',
  'components/autocomplete/stories.json',
  'components/overlay/accessibility.html',
  'components/overlay/behavior.scxml',
  'components/overlay/component.json',
  'components/overlay/interface.json',
  'components/overlay/layout.css',
  'components/scroll-area/accessibility.html',
  'components/scroll-area/behavior.scxml',
  'components/scroll-area/component.json',
  'components/scroll-area/interface.json',
  'components/scroll-area/layout.css',
];

const hashes = {};
for (const rel of DEFINITION_FILES) {
  const abs = path.join(ROOT, rel);
  hashes[rel] = crypto.createHash('sha256').update(fs.readFileSync(abs)).digest('hex');
}
fs.writeFileSync(path.join(OUT, 'source-sha256.json'), JSON.stringify(hashes, null, 2) + '\n');

console.log(JSON.stringify({
  fig: figPath,
  bytes: figBytes.byteLength,
  nodes: checks.counts.nodesInFile,
  textNodes: checks.counts.textNodes,
  cases: checks.cases.map((c) => c.id),
  png: renderReport.png,
  svg: renderReport.svg,
}, null, 2));
