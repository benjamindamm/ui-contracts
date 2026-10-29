#!/usr/bin/env node
/**
 * Builder B · run-04 · Readback-Receipt für autocomplete.fig
 *
 * Liest autocomplete.fig mit der gepinnten Toolchain (@open-pencil/core 0.16.0,
 * parseFigFile mit populate:"all") zurück, beobachtet alle Layer nativ
 * (Typ, Name, Geometrie, Fills/Strokes, Texte, Editierbarkeit) und prüft die
 * Beobachtungen gegen die aus den hashgebundenen Quellen neu berechneten
 * Erwartungswerte (tokens.json, stories.json, accessibility.rules.json,
 * layout.css-Regeln — siehe generate-fig.mjs). Ergebnis: readback.json.
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { pathToFileURL } from 'node:url';

const REPO = '/Users/kcnpxcp/Dev/GitHub/ui-contracts';
const OUT_DIR = REPO + '/examples/autocomplete/reproducibility/run-04/builder-b';
const CORE = pathToFileURL(REPO + '/tools/openpencil/node_modules/@open-pencil/core/dist/index.js').href;
const CORE_VERSION = JSON.parse(readFileSync(`${REPO}/tools/openpencil/node_modules/@open-pencil/core/package.json`, 'utf8')).version;

const { parseFigFile } = await import(CORE);

// ---------------------------------------------------------------------------
// 1) Definition erneut verifizieren (gleiche 22 Manifest-Dateien, Revisionslabel)
// ---------------------------------------------------------------------------
const manifest = JSON.parse(readFileSync(`${REPO}/examples/autocomplete/reproducibility/run-04/input-manifest.json`, 'utf8'));
const EXPECTED_REVISION = '1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727';
const sha256File = (p) => createHash('sha256').update(readFileSync(p)).digest('hex');
const fileHashes = {};
for (const [rel, expected] of Object.entries(manifest.files)) {
  const actual = sha256File(`${REPO}/${manifest.root}/${rel}`);
  if (actual !== expected) throw new Error(`Quellhash weicht ab: ${rel}`);
  fileHashes[rel] = actual;
}
const sorted = {};
for (const k of Object.keys(fileHashes).sort()) sorted[k] = fileHashes[k];
const revision = createHash('sha256').update(JSON.stringify(sorted), 'utf8').digest('hex');
if (revision !== EXPECTED_REVISION) throw new Error(`Revisionslabel weicht ab: ${revision}`);

// ---------------------------------------------------------------------------
// 2) Fig-Datei lesen und mit der gepinnten Toolchain parsen
// ---------------------------------------------------------------------------
const FIG = `${OUT_DIR}/autocomplete.fig`;
const figBuf = readFileSync(FIG);
const figBytes = new Uint8Array(figBuf.byteLength);
figBytes.set(figBuf);
const figSha256 = createHash('sha256').update(figBytes).digest('hex');

const graph = await parseFigFile(figBytes.buffer, { populate: 'all' });
const page = graph.getPages().find((p) => p.name === 'Autocomplete');
if (!page) throw new Error('Seite "Autocomplete" nicht gefunden');

// ---------------------------------------------------------------------------
// 3) Designwerte und Falldaten aus den Quellen neu berechnen (unabhängig vom
//    Generator: gleiche Token-Auflösung, gleiche Geometrieregeln)
// ---------------------------------------------------------------------------
const TOKENS = JSON.parse(readFileSync(`${REPO}/components/tokens.json`, 'utf8'));
const STORIES = JSON.parse(readFileSync(`${REPO}/components/autocomplete/stories.json`, 'utf8')).stories;
const RULES = JSON.parse(readFileSync(`${REPO}/components/autocomplete/accessibility.rules.json`, 'utf8'));

function tokenValue(key) {
  const obj = key.split('.').reduce((o, k) => o[k], TOKENS);
  if (typeof obj.$value === 'string') {
    // "{base.gap}" = Tokenreferenz; sonst platter Wert (z. B. fontFamily "Inter")
    if (obj.$value.startsWith('{') && obj.$value.endsWith('}')) return tokenValue(obj.$value.slice(1, -1));
    return obj.$value;
  }
  return obj.$value.value;
}
function tokenHex(key) {
  const v = key.split('.').reduce((o, k) => o[k], TOKENS).$value;
  const h = (n) => Math.round(n * 255).toString(16).padStart(2, '0');
  return `#${h(v.components[0])}${h(v.components[1])}${h(v.components[2])}`;
}
const hexOf = (c) => {
  const h = (n) => Math.round(n * 255).toString(16).padStart(2, '0');
  return `#${h(c.r)}${h(c.g)}${h(c.b)}` + (c.a < 1 ? h(c.a) : '');
};

const W = tokenValue('autocomplete.width');
const INPUT_H = tokenValue('autocomplete.inputHeight');
const LH = tokenValue('autocomplete.lineHeight');
const LABEL_GAP = tokenValue('autocomplete.labelGap');
const STATUS_GAP = tokenValue('autocomplete.statusGap');
const GAP = tokenValue('autocomplete.gap');
const ROW = tokenValue('autocomplete.rowHeight');
const MAX_H = tokenValue('autocomplete.maxHeight');
const RADIUS = tokenValue('autocomplete.radius');
const BORDER_W = tokenValue('autocomplete.borderWidth');
const FS = tokenValue('autocomplete.fontSize');
const FS_STATUS = tokenValue('autocomplete.statusFontSize');
const FONT = tokenValue('autocomplete.fontFamily');

const HX = {
  surface: tokenHex('autocomplete.surface'),
  text: tokenHex('autocomplete.text'),
  muted: tokenHex('autocomplete.muted'),
  border: tokenHex('autocomplete.border'),
  focus: tokenHex('autocomplete.focus'),
  highlight: tokenHex('autocomplete.highlight'),
  disabled: tokenHex('autocomplete.disabled'),
  error: tokenHex('autocomplete.error'),
};

function statusMessage(s) {
  if (s.value) {
    const rec = s.results.find((r) => r.key === s.value);
    return RULES.messages.selected.replace('{label}', rec ? rec.label : s.value);
  }
  if (!s.inputs.enabled) return RULES.messages.disabled;
  switch (s.phase) {
    case 'closed': return RULES.messages.closed;
    case 'opening': return RULES.messages.opening;
    case 'loading': return RULES.messages.loading;
    case 'ready': return RULES.messages.results.replace('{count}', String(s.results.length));
    case 'empty': return RULES.messages.empty;
    case 'error': return RULES.messages.error;
    default: return '';
  }
}

// Erwartungsmodell pro Fall (Regeln: generate-fig.mjs, aus layout.css/README)
function expectedCase(s, x, y) {
  const phase = s.phase;
  const results = s.results ?? [];
  const popupVisible = RULES.projections[phase].popupVisible;
  const hasRows = results.length > 0;
  const isMsg = ['loading', 'empty', 'error'].includes(phase) && popupVisible;
  const rowCount = hasRows ? results.length : isMsg ? 1 : 0;
  const contentH = rowCount * ROW;
  const viewportH = hasRows ? Math.min(contentH, MAX_H) : isMsg ? ROW : 0;
  const inputTop = LH + LABEL_GAP;
  const inputBottom = inputTop + INPUT_H;
  const popupTop = inputBottom + GAP;
  const statusY = popupVisible ? popupTop + viewportH + STATUS_GAP : inputBottom + STATUS_GAP;
  const frameH = statusY + LH;
  const focusStates = ['opening', 'loading', 'ready', 'empty', 'error'];
  const strokeHex = !s.inputs.enabled ? HX.border : focusStates.includes(phase) ? HX.focus : HX.border;
  const showQuery = s.inputs.query.length > 0;
  return {
    name: s.id, x, y, w: W, frameH,
    input: { y: inputTop, h: INPUT_H, radius: RADIUS, strokeHex, strokeW: BORDER_W, strokeAlign: 'INSIDE', fill: HX.surface },
    inputText: {
      name: showQuery ? 'input/query' : 'input/placeholder',
      text: showQuery ? s.inputs.query : s.inputs.placeholder,
      hex: showQuery ? (s.inputs.enabled ? HX.text : HX.disabled) : HX.muted,
      y: (INPUT_H - LH) / 2, h: LH, fontSize: FS,
    },
    surface: { y: popupTop, h: viewportH, visible: popupVisible, fill: HX.surface, radius: RADIUS, clips: true, shadow: { x: 0, y: 2, radius: 8, hex: '#000000', alpha: 0.2 } },
    viewport: { h: viewportH, clips: true },
    scrollContent: { h: contentH, y: s.id === 'scroll-end' ? viewportH - contentH : 0 },
    list: { h: contentH },
    options: results.map((r, i) => ({
      name: `option/${r.key}`, y: i * ROW, h: ROW,
      fill: s.activeKey === r.key ? HX.highlight : null,
      text: r.label, hex: r.disabled ? HX.disabled : HX.text,
    })),
    messageRow: isMsg ? { h: ROW, text: statusMessage(s), hex: HX.text } : null,
    label: { text: s.inputs.label, hex: HX.text, y: 0, h: LH, fontSize: FS },
    status: { text: statusMessage(s), hex: phase === 'error' ? HX.error : HX.muted, y: statusY, h: LH, fontSize: FS_STATUS },
  };
}

const COL_X = [40, 480];
const ROW_Y = [120, 440, 760, 1080, 1400];
const expected = STORIES.map((s, i) => expectedCase(s, COL_X[i % 2], ROW_Y[Math.floor(i / 2)]));

// ---------------------------------------------------------------------------
// 4) Natives Observieren des zurückgelesenen Graphen
// ---------------------------------------------------------------------------
function fillOut(f) {
  const o = { type: f.type };
  if (f.type === 'SOLID' && f.color) o.hex = hexOf(f.color);
  if (f.opacity < 1) o.opacity = f.opacity;
  if (f.visible === false) o.visible = false;
  return o;
}
function strokeOut(st) {
  const o = fillOut(st);
  o.weight = st.weight;
  o.align = st.align;
  return o;
}
function effectOut(e) {
  const o = { type: e.type };
  if (e.color) o.hex = hexOf(e.color);
  if (e.offset) o.offset = { x: e.offset.x, y: e.offset.y };
  if (e.radius) o.radius = e.radius;
  if (e.spread) o.spread = e.spread;
  return o;
}
function obs(node, path) {
  const o = {
    path, name: node.name, type: node.type,
    x: node.x, y: node.y, width: node.width, height: node.height,
    visible: node.visible, locked: node.locked,
  };
  if (node.clipsContent) o.clipsContent = true;
  if (node.cornerRadius) o.cornerRadius = node.cornerRadius;
  if (node.opacity < 1) o.opacity = node.opacity;
  if (node.fills?.length) o.fills = node.fills.map(fillOut);
  if (node.strokes?.length) o.strokes = node.strokes.map(strokeOut);
  if (node.effects?.length) o.effects = node.effects.map(effectOut);
  if (node.type === 'TEXT') {
    o.text = node.text ?? '';
    o.fontSize = node.fontSize;
    o.fontFamily = node.fontFamily;
    o.fontWeight = node.fontWeight;
    o.lineHeight = node.lineHeight;
    o.textAlignVertical = node.textAlignVertical;
  }
  const kids = node.childIds.map((id) => graph.getNode(id)).filter(Boolean);
  if (kids.length) o.children = kids.map((k) => obs(k, `${path}/${k.name}`));
  return o;
}
function findNode(node, name) {
  if (node.name === name) return node;
  for (const id of node.childIds) {
    const r = findNode(graph.getNode(id), name);
    if (r) return r;
  }
  return null;
}
const childText = (node) => node.childIds.map((id) => graph.getNode(id)).find((c) => c.name === 'text');

// ---------------------------------------------------------------------------
// 5) Prüfungen (evidence aus den zurückgelesenen Werten, nicht aus dem Generator)
// ---------------------------------------------------------------------------
const allNodes = [...graph.getAllNodes()];
const checks = [];
const addCheck = (id, description, status, evidence) =>
  checks.push({ id, description, status, evidence });

// --- readback -------------------------------------------------------------
{
  const types = [...new Set(allNodes.map((n) => n.type))].sort();
  const locked = allNodes.filter((n) => n.locked).map((n) => n.name);
  const status = types.every((t) => ['FRAME', 'TEXT', 'CANVAS', 'DOCUMENT'].includes(t)) && locked.length === 0 ? 'pass' : 'fail';
  addCheck('readback',
    'autocomplete.fig öffnet sich als OpenPencil-Dokument (parseFigFile, populate:"all"); alle Layer sind normale, nicht gesperrte FRAME/TEXT-Layer.',
    status,
    `Seite "${page.name}" ${page.width}×${page.height}; ${allNodes.length} Nodes; Typen: ${types.join(', ')}; gesperrt: ${locked.length ? locked.join(', ') : 'keine'}`);
}

// --- cases -----------------------------------------------------------------
const pageChildren = page.childIds.map((id) => graph.getNode(id)).filter(Boolean);
const caseFrames = pageChildren.filter((n) => STORIES.some((s) => s.id === n.name));
const titleNode = pageChildren.find((n) => n.name === 'Seitentitel');
{
  const orderOk = caseFrames.length === 10 && caseFrames.every((f, i) => f.name === STORIES[i].id);
  const namesOk = STORIES.every((s) => caseFrames.some((f) => f.name === s.id)) && caseFrames.length === 10;
  const typeOk = caseFrames.every((f) => f.type === 'FRAME' || f.type === 'COMPONENT');
  const wOk = caseFrames.every((f) => f.width === W);
  const status = orderOk && namesOk && typeOk && wOk ? 'pass' : 'fail';
  addCheck('cases',
    'Genau zehn Fall-frames mit den Quellnamen closed…disabled, in stories.json-Reihenfolge, je FRAME, 320 px breit.',
    status,
    `Frame-Reihenfolge: ${caseFrames.map((f) => f.name).join(', ')}; Typen: ${[...new Set(caseFrames.map((f) => f.type))].join(', ')}; Breite: ${[...new Set(caseFrames.map((f) => f.width))].join(', ')}; freier Seitentitel: ${titleNode ? titleNode.text : 'fehlt'}`);
}

// --- parts + fidelity (pro Fall beobachtet und verglichen) ------------------
const caseObservations = [];
const partFailures = [];
const fidelityFailures = [];
const near = (a, b) => Math.abs(a - b) < 1e-9;
const rectOk = (node, x, y, w, h) => node && near(node.x, x) && near(node.y, y) && near(node.width, w) && near(node.height, h);
const fillHexes = (node) => (node.fills ?? []).map((f) => hexOf(f.color));

expected.forEach((ex) => {
  const frame = caseFrames.find((f) => f.name === ex.name);
  if (!frame) { partFailures.push(`${ex.name}: Frame fehlt`); return; }
  const tree = obs(frame, ex.name);
  caseObservations.push({ name: ex.name, x: ex.x, y: ex.y, frameH: ex.frameH, popupVisible: ex.surface.visible, nodes: tree });

  const label = findNode(frame, 'label');
  const input = findNode(frame, 'input');
  const inputText = input && findNode(input, ex.inputText.name);
  const surface = findNode(frame, 'overlay/surface');
  const ovContent = findNode(frame, 'overlay/content');
  const viewport = findNode(frame, 'scroll/viewport');
  const scrollContent = findNode(frame, 'scroll/content');
  const list = findNode(frame, 'list');
  const status = findNode(frame, 'status');

  // parts: alle Teil-Layer vorhanden, benannt, nicht gesperrt
  for (const [n, req] of [
    [label, 'label'], [input, 'input'], [surface, 'overlay/surface'], [ovContent, 'overlay/content'],
    [viewport, 'scroll/viewport'], [scrollContent, 'scroll/content'], [list, 'list'], [status, 'status'],
    [inputText, ex.inputText.name],
  ]) {
    if (!n) partFailures.push(`${ex.name}: Teil "${req}" fehlt`);
    else if (n.locked) partFailures.push(`${ex.name}: Teil "${req}" ist gesperrt`);
  }
  ex.options.forEach((o) => {
    const row = findNode(frame, o.name);
    if (!row) partFailures.push(`${ex.name}: Option "${o.name}" fehlt`);
    else if (!childText(row)) partFailures.push(`${ex.name}: "${o.name}" hat kein Text-Kind "text"`);
    else if (row.locked || childText(row).locked) partFailures.push(`${ex.name}: "${o.name}" gesperrt`);
  });
  const messageRow = findNode(frame, 'message-row');
  if (ex.messageRow && !messageRow) partFailures.push(`${ex.name}: message-row fehlt`);
  if (!ex.messageRow && messageRow) partFailures.push(`${ex.name}: unerwartete message-row`);
  if (messageRow && !childText(messageRow)) partFailures.push(`${ex.name}: message-row ohne Text`);

  // fidelity: Geometrie, Farben, Typografie, Meldungen
  if (!rectOk(frame, ex.x, ex.y, ex.w, ex.frameH)) fidelityFailures.push(`${ex.name}: Frame ${frame.x},${frame.y} ${frame.width}×${frame.height} ≠ erwartet ${ex.x},${ex.y} ${ex.w}×${ex.frameH}`);
  if (!rectOk(input, 0, ex.input.y, ex.w, ex.input.h)) fidelityFailures.push(`${ex.name}: input-Geometrie ${input ? `${input.x},${input.y} ${input.width}×${input.height}` : 'n/a'} ≠ erwartet 0,${ex.input.y} ${ex.w}×${ex.input.h}`);
  if (input) {
    if (input.cornerRadius !== ex.input.radius) fidelityFailures.push(`${ex.name}: input cornerRadius ${input.cornerRadius} ≠ ${ex.input.radius}`);
    const st = (input.strokes ?? [])[0];
    if (!st || hexOf(st.color) !== ex.input.strokeHex || st.weight !== ex.input.strokeW || st.align !== ex.input.strokeAlign)
      fidelityFailures.push(`${ex.name}: input-Stroke ${st ? `${hexOf(st.color)} w=${st.weight} ${st.align}` : 'fehlend'} ≠ erwartet ${ex.input.strokeHex} w=${ex.input.strokeW} ${ex.input.strokeAlign}`);
    if (!fillHexes(input).includes(ex.input.fill)) fidelityFailures.push(`${ex.name}: input-Fill ${fillHexes(input).join(',') || 'leer'} ≠ ${ex.input.fill}`);
  }
  if (label && (label.text !== ex.label.text || !fillHexes(label).includes(ex.label.hex) || label.fontSize !== ex.label.fontSize || label.fontFamily !== FONT))
    fidelityFailures.push(`${ex.name}: label ${JSON.stringify(label.text)} ${fillHexes(label).join(',')} fs=${label.fontSize} ≠ erwartet ${JSON.stringify(ex.label.text)} ${ex.label.hex} fs=${ex.label.fontSize}`);
  if (inputText) {
    if (inputText.text !== ex.inputText.text) fidelityFailures.push(`${ex.name}: input-Text ${JSON.stringify(inputText.text)} ≠ ${JSON.stringify(ex.inputText.text)}`);
    if (!fillHexes(inputText).includes(ex.inputText.hex)) fidelityFailures.push(`${ex.name}: input-Textfarbe ${fillHexes(inputText).join(',')} ≠ ${ex.inputText.hex}`);
    if (inputText.fontSize !== ex.inputText.fontSize || inputText.fontFamily !== FONT) fidelityFailures.push(`${ex.name}: input-Text fs/family ≠ ${ex.inputText.fontSize}/${FONT}`);
    if (!near(inputText.y, ex.inputText.y) || !near(inputText.height, ex.inputText.h)) fidelityFailures.push(`${ex.name}: input-Text-Position ${inputText.y} ≠ ${ex.inputText.y}`);
  }
  if (surface) {
    if (!near(surface.y, ex.surface.y) || !near(surface.height, ex.surface.h)) fidelityFailures.push(`${ex.name}: surface ${surface.y}×${surface.height} ≠ ${ex.surface.y}×${ex.surface.h}`);
    if (surface.visible !== ex.surface.visible) fidelityFailures.push(`${ex.name}: surface visible=${surface.visible} ≠ ${ex.surface.visible}`);
    if (surface.clipsContent !== ex.surface.clips) fidelityFailures.push(`${ex.name}: surface clipsContent=${surface.clipsContent} ≠ ${ex.surface.clips}`);
    if (!fillHexes(surface).includes(ex.surface.fill)) fidelityFailures.push(`${ex.name}: surface-Fill ≠ ${ex.surface.fill}`);
    const sh = (surface.effects ?? []).find((e) => e.type === 'DROP_SHADOW');
    if (!sh) fidelityFailures.push(`${ex.name}: surface ohne DROP_SHADOW`);
    else if (hexOf(sh.color) !== `${ex.surface.shadow.hex}${Math.round(ex.surface.shadow.alpha * 255).toString(16).padStart(2, '0')}` || sh.offset?.y !== ex.surface.shadow.y || sh.radius !== ex.surface.shadow.radius)
      fidelityFailures.push(`${ex.name}: surface-Schatten ${sh ? `${hexOf(sh.color)} dy=${sh.offset?.y} r=${sh.radius}` : 'n/a'} ≠ 0 2 8 #00000033`);
  }
  if (viewport) {
    if (!near(viewport.height, ex.viewport.h)) fidelityFailures.push(`${ex.name}: viewport-höhe ${viewport.height} ≠ ${ex.viewport.h}`);
    if (viewport.clipsContent !== ex.viewport.clips) fidelityFailures.push(`${ex.name}: viewport clipsContent ≠ ${ex.viewport.clips}`);
  }
  if (scrollContent && (!near(scrollContent.height, ex.scrollContent.h) || !near(scrollContent.y, ex.scrollContent.y)))
    fidelityFailures.push(`${ex.name}: scroll/content y=${scrollContent.y} h=${scrollContent.height} ≠ y=${ex.scrollContent.y} h=${ex.scrollContent.h}`);
  if (list && !near(list.height, ex.list.h)) fidelityFailures.push(`${ex.name}: list-höhe ${list.height} ≠ ${ex.list.h}`);
  ex.options.forEach((o) => {
    const row = findNode(frame, o.name);
    if (!row) return;
    const t = childText(row);
    const rowFill = row.fills?.length ? fillHexes(row) : null;
    if (o.fill && (!rowFill || !rowFill.includes(o.fill))) fidelityFailures.push(`${ex.name}: ${o.name} ohne Highlight-Fill ${o.fill} (ist ${rowFill?.join(',') ?? 'leer'})`);
    if (!o.fill && rowFill) fidelityFailures.push(`${ex.name}: ${o.name} unerwarteter Fill ${rowFill.join(',')}`);
    if (t && (t.text !== o.text || !fillHexes(t).includes(o.hex))) fidelityFailures.push(`${ex.name}: ${o.name} Text ${JSON.stringify(t.text)} ${fillHexes(t).join(',')} ≠ ${JSON.stringify(o.text)} ${o.hex}`);
    if (!near(row.y, o.y) || !near(row.height, o.h)) fidelityFailures.push(`${ex.name}: ${o.name} y=${row.y} h=${row.height} ≠ ${o.y}/${o.h}`);
  });
  if (messageRow) {
    const t = childText(messageRow);
    if (t && (t.text !== ex.messageRow.text || !fillHexes(t).includes(ex.messageRow.hex)))
      fidelityFailures.push(`${ex.name}: message-row ${JSON.stringify(t?.text)} ${t ? fillHexes(t).join(',') : 'n/a'} ≠ ${JSON.stringify(ex.messageRow.text)} ${ex.messageRow.hex}`);
  }
  if (status) {
    if (status.text !== ex.status.text) fidelityFailures.push(`${ex.name}: status ${JSON.stringify(status.text)} ≠ ${JSON.stringify(ex.status.text)}`);
    if (!fillHexes(status).includes(ex.status.hex)) fidelityFailures.push(`${ex.name}: status-Farbe ${fillHexes(status).join(',')} ≠ ${ex.status.hex}`);
    if (status.fontSize !== ex.status.fontSize || status.fontFamily !== FONT) fidelityFailures.push(`${ex.name}: status fs/family ≠ ${ex.status.fontSize}/${FONT}`);
    if (!near(status.y, ex.status.y)) fidelityFailures.push(`${ex.name}: status-y ${status.y} ≠ ${ex.status.y}`);
  }
});
addCheck('parts',
  'Innerhalb jedes Falls bleiben label, input, overlay/surface, overlay/content, scroll/viewport, scroll/content, list, option/<key>, message-row (falls definiert) und status als getrennte, benannte, nicht gesperrte Layer erhalten.',
  partFailures.length ? 'fail' : 'pass',
  partFailures.length ? partFailures : 'Alle 10 Fälle enthalten alle Teil-Layer; keine gesperrten Layer; message-row nur in loading/empty/error; option-Zeilen mit Text-Kind.');
addCheck('fidelity',
  'Farben, Typografie, Maße und Meldungen stimmen mit den aus tokens.json/layout.css/stories.json/accessibility.rules.json berechneten Werten überein.',
  fidelityFailures.length ? 'fail' : 'pass',
  fidelityFailures.length ? fidelityFailures : `Alle Geometrie-/Farb-/Text-/Meldungswerte identisch (Farben: surface ${HX.surface}, text ${HX.text}, muted ${HX.muted}, border ${HX.border}, focus ${HX.focus}, highlight ${HX.highlight}, disabled ${HX.disabled}, error ${HX.error}; Inter 14/12, lineHeight 20; Radius 8; Shadow 0 2 8 #00000033).`);

// --- scrollend --------------------------------------------------------------
{
  const frame = caseFrames.find((f) => f.name === 'scroll-end');
  const fails = [];
  if (frame) {
    const viewport = findNode(frame, 'scroll/viewport');
    const scrollContent = findNode(frame, 'scroll/content');
    const list = findNode(frame, 'list');
    const options = list ? list.childIds.map((id) => graph.getNode(id)) : [];
    const active = findNode(frame, 'option/zuerich');
    const last = options.at(-1);
    const lastTop = last && scrollContent ? last.y + scrollContent.y : null;
    if (!viewport || !near(viewport.height, 160)) fails.push(`viewport-höhe ${viewport?.height} ≠ 160`);
    if (viewport && !viewport.clipsContent) fails.push('viewport clippt nicht');
    if (!scrollContent || !near(scrollContent.y, -64)) fails.push(`scroll/content y=${scrollContent?.y} ≠ -64`);
    if (options.length !== 7) fails.push(`${options.length} Optionen ≠ 7`);
    if (!active || !fillHexes(active).includes(HX.highlight)) fails.push('option/zuerich nicht hervorgehoben');
    if (lastTop !== 128 || !near(last.height, 32)) fails.push(`letzte Option in Viewport bei y=${lastTop} (erwartet 128..160)`);
  } else fails.push('Frame scroll-end fehlt');
  addCheck('scrollend',
    'scroll-end zeigt die aktive letzte Option (option/zuerich) im geclippten Viewport; Inhalt um -64 px versetzt; alle 7 Ergebnislayer erhalten.',
    fails.length ? 'fail' : 'pass',
    fails.length ? fails : 'scroll/content y=-64 h=224 in viewport 320×160 (geclippt); 7 option/-Layer; option/zuerich fill #EAF2FF; letzte Option bei 128..160 (untere Viewportkante).');
}

// ---------------------------------------------------------------------------
// 6) Receipt schreiben
// ---------------------------------------------------------------------------
const receipt = {
  format: 'ui-contracts-readback/1',
  createdAt: new Date().toISOString(),
  toolchain: { package: '@open-pencil/core', version: CORE_VERSION, api: 'parseFigFile(arrayBuffer, { populate: "all" })' },
  file: { path: 'autocomplete.fig', bytes: figBytes.byteLength, sha256: figSha256 },
  definition: {
    revision,
    manifest: { path: 'examples/autocomplete/reproducibility/run-04/input-manifest.json', sha256: sha256File(`${REPO}/examples/autocomplete/reproducibility/run-04/input-manifest.json`) },
    verifiedFiles: Object.keys(fileHashes).length,
  },
  page: {
    name: page.name,
    width: page.width,
    height: page.height,
    topLevelChildren: pageChildren.length,
    title: titleNode ? { name: titleNode.name, text: titleNode.text } : null,
  },
  editability: {
    rule: 'Alle Layer sind normale FRAME/TEXT-Nodes des Dokuments (keine Instanzen), keiner ist locked; damit ist jeder Layer im OpenPencil-Editor einzeln anwählbar und editierbar.',
    typesUsed: [...new Set(allNodes.map((n) => n.type))].sort(),
    allUnlocked: allNodes.every((n) => !n.locked),
    nodeCount: allNodes.length,
  },
  checks,
  cases: caseObservations,
};

const outPath = `${OUT_DIR}/readback.json`;
writeFileSync(outPath, JSON.stringify(receipt, null, 2) + '\n');
console.log(JSON.stringify({
  file: outPath,
  fig: { bytes: figBytes.byteLength, sha256: figSha256 },
  checks: checks.map((c) => ({ id: c.id, status: c.status })),
}, null, 2));
process.exitCode = checks.every((c) => c.status === 'pass') ? 0 : 1;
