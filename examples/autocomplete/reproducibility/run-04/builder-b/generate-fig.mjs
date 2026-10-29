#!/usr/bin/env node
/**
 * Builder B · run-04 · Autocomplete → editierbares OpenPencil-Design
 *
 * Erzeugt autocomplete.fig ausschliesslich aus den eingefrorenen, hashgebundenen
 * Quellen (input-manifest.json, Revisionslabel 1d83935f…) mit der gepinnten
 * Toolchain tools/openpencil/ (@open-pencil/core 0.16.0, exportFigFile).
 *
 * Regeln:
 *  - Keine neuen Definitionswerte; alle Designwerte werden aus tokens.json
 *    aufgelöst, Geometrie/Zustandsregeln zitiert aus den layout.css-Dateien
 *    (Zeilenzahlen in den Kommentaren), Meldungen aus accessibility.rules.json,
 *    Fälle aus stories.json.
 *  - Aussenanordnung und Seitentitel sind frei (README "Exportrahmen").
 *  - Fehlende Angaben werden nicht still ergänzt; sie sind in REPORT.md
 *    als Lücken dokumentiert (Meldungszeilenfarbe, FontWeight).
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { pathToFileURL } from 'node:url';

const REPO = '/Users/kcnpxcp/Dev/GitHub/ui-contracts';
const OUT_DIR = REPO + '/examples/autocomplete/reproducibility/run-04/builder-b';
const CORE = pathToFileURL(REPO + '/tools/openpencil/node_modules/@open-pencil/core/dist/index.js').href;

const { SceneGraph, exportFigFile } = await import(CORE);

const sha256 = (p) => createHash('sha256').update(readFileSync(p)).digest('hex');

// ---------------------------------------------------------------------------
// 1) Quellrevision verifizieren: alle 22 Manifest-Dateien + Revisionslabel
//    (Algorithmus: runsheet-technical.md "Definitionsrevision").
// ---------------------------------------------------------------------------
const manifestPath = REPO + '/examples/autocomplete/reproducibility/run-04/input-manifest.json';
const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
const EXPECTED_REVISION = '1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727';

const fileHashes = {};
for (const [rel, expected] of Object.entries(manifest.files)) {
  const actual = sha256(`${REPO}/${manifest.root}/${rel}`);
  if (actual !== expected) throw new Error(`Quellhash weicht ab: ${rel} erwartet ${expected}, ist ${actual}`);
  fileHashes[rel] = actual;
}
const sorted = {};
for (const k of Object.keys(fileHashes).sort()) sorted[k] = fileHashes[k];
const revision = createHash('sha256').update(JSON.stringify(sorted), 'utf8').digest('hex');
if (revision !== EXPECTED_REVISION) throw new Error(`Revisionslabel weicht ab: ${revision} !== ${EXPECTED_REVISION}`);
console.log(`revision OK: ${revision} (${Object.keys(fileHashes).length} Dateien verifiziert)`);

// ---------------------------------------------------------------------------
// 2) Designwerte auflösen — ausschließlich components/tokens.json
//    (autocomplete.*; {base.*}-Referenzen rekursiv aufgelöst).
// ---------------------------------------------------------------------------
const TOKENS = JSON.parse(readFileSync(`${REPO}/components/tokens.json`, 'utf8'));
function tokenValue(key) {
  const obj = key.split('.').reduce((o, k) => o[k], TOKENS);
  if (typeof obj.$value === 'string') {
    // "{base.gap}" = Tokenreferenz; sonst platter Wert (z. B. fontFamily "Inter")
    if (obj.$value.startsWith('{') && obj.$value.endsWith('}')) return tokenValue(obj.$value.slice(1, -1));
    return obj.$value;
  }
  return obj.$value.value;
}
function tokenColor(key) {
  const v = key.split('.').reduce((o, k) => o[k], TOKENS).$value;
  return { r: v.components[0], g: v.components[1], b: v.components[2], a: v.alpha };
}

const W = tokenValue('autocomplete.width');            // 320
const INPUT_H = tokenValue('autocomplete.inputHeight'); // 44
const LH = tokenValue('autocomplete.lineHeight');        // 20
const LABEL_GAP = tokenValue('autocomplete.labelGap');   // 8
const STATUS_GAP = tokenValue('autocomplete.statusGap'); // 8
const GAP = tokenValue('autocomplete.gap');              // 8
const ROW = tokenValue('autocomplete.rowHeight');        // 32
const MAX_H = tokenValue('autocomplete.maxHeight');      // 160
const RADIUS = tokenValue('autocomplete.radius');        // 8
const BORDER_W = tokenValue('autocomplete.borderWidth'); // 1
const PAD_X = tokenValue('autocomplete.paddingInline');  // 12
const FONT = tokenValue('autocomplete.fontFamily');      // 'Inter'
const FS = tokenValue('autocomplete.fontSize');          // 14
const FS_STATUS = tokenValue('autocomplete.statusFontSize'); // 12
// Literal aus autocomplete/layout.css Zeile 38: [data-part="option"] { padding: 6px var(--ac-padding-inline); }
const OPTION_PAD_Y = 6;

const C = {
  surface: tokenColor('autocomplete.surface'),
  text: tokenColor('autocomplete.text'),
  muted: tokenColor('autocomplete.muted'),
  border: tokenColor('autocomplete.border'),
  focus: tokenColor('autocomplete.focus'),
  highlight: tokenColor('autocomplete.highlight'),
  disabled: tokenColor('autocomplete.disabled'),
  error: tokenColor('autocomplete.error'),
};

// ---------------------------------------------------------------------------
// 3) Falldaten: stories.json (Zehnfälle) + accessibility.rules.json
//    (Meldungen, Zustandsprojektion popupVisible).
// ---------------------------------------------------------------------------
const STORIES = JSON.parse(readFileSync(`${REPO}/components/autocomplete/stories.json`, 'utf8')).stories;
const RULES = JSON.parse(readFileSync(`${REPO}/components/autocomplete/accessibility.rules.json`, 'utf8'));

function statusMessage(s) {
  if (s.value) {
    // README: "Bei selected steht das zu value gehörige Label im Input, und der Status nutzt die selected-Vorlage."
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

// ---------------------------------------------------------------------------
// 4) Szenengraph aufbauen
// ---------------------------------------------------------------------------
const graph = new SceneGraph();
// Der Konstruktor legt eine leere Seite "Page 1" an — entfernen, damit das
// Dokument genau eine Seite enthält (sonst wäre der Export zweiseitig).
graph.deleteNode(graph.getPages()[0].id);
const page = graph.addPage('Autocomplete');

const solid = (c) => ({ type: 'SOLID', color: c, opacity: 1, visible: true });

function addText(parentId, name, { x, y, w, h, text, color, fontSize = FS, alignVertical = 'TOP' }) {
  return graph.createNode('TEXT', parentId, {
    name, x, y, width: w, height: h,
    text,
    fills: [solid(color)],
    fontSize,
    fontFamily: FONT,
    fontWeight: 400, // Lücke: FontWeight nicht in den Quellen definiert → Default 400 (REPORT.md)
    lineHeight: LH,
    textAlignHorizontal: 'LEFT',
    textAlignVertical: alignVertical,
    textAutoResize: 'NONE',
  });
}

/**
 * Baut einen Falle-Frame. Geometrie (autocomplete/layout.css + README "Sichtbare Geometrie"):
 *  label: Höhe lineHeight(20), margin-bottom labelGap(8)          → y 0..20
 *  input: Höhe inputHeight(44), width 100%, border 1px, radius 8  → y 28..72
 *  popup: Oberkante = Inputende + gap(8), Breite = Inputbreite    → y 80
 *         Viewporthöhe = min(Ergebnisanzahl × rowHeight, maxHeight);
 *         loading/empty/error zeigen eine Zeile (rowHeight 32)
 *  status: Höhe lineHeight, margin-top statusGap(8), font 12;
 *          unter dem tatsächlich sichtbaren Popup, sonst unter dem Input
 *  Ein verborgener Popup belegt keinen Platz (Layer bleibt editierbar erhalten).
 */
function buildCase(s, x, y) {
  const phase = s.phase;
  const { label, placeholder, query, enabled } = s.inputs;
  const results = s.results ?? [];
  const projection = RULES.projections[phase];
  const popupVisible = projection.popupVisible;

  const message = statusMessage(s);
  const statusColor = phase === 'error' ? C.error : C.muted;

  const hasRows = results.length > 0;
  const isMessageCase = ['loading', 'empty', 'error'].includes(phase) && popupVisible;
  const rowCount = hasRows ? results.length : isMessageCase ? 1 : 0;
  const contentH = rowCount * ROW;
  // README: "Die Viewporthöhe ist bei Ergebnislisten min(Ergebnisanzahl × rowHeight, maxHeight)."
  const viewportH = hasRows ? Math.min(contentH, MAX_H) : isMessageCase ? ROW : 0;

  const inputTop = LH + LABEL_GAP;          // 28
  const inputBottom = inputTop + INPUT_H;   // 72
  const popupTop = inputBottom + GAP;       // 80
  const statusY = popupVisible ? popupTop + viewportH + STATUS_GAP : inputBottom + STATUS_GAP;
  const frameH = statusY + LH;

  const frame = graph.createNode('FRAME', page.id, {
    name: s.id, x, y, width: W, height: frameH, fills: [],
  });

  // label (data-part="label": block, height lineHeight, margin-bottom labelGap)
  addText(frame.id, 'label', { x: 0, y: 0, w: W, h: LH, text: label, color: C.text });

  // input (data-part="input": border 1px, radius 8, background surface, padding 0 12px)
  // Border-Farbe: layout.css Zeilen 25–31 (opening/loading/ready/empty/error → focus);
  // Zeile 33 (:disabled → border); default border.
  const focusStates = ['opening', 'loading', 'ready', 'empty', 'error'];
  const borderColor = !enabled ? C.border : focusStates.includes(phase) ? C.focus : C.border;
  const input = graph.createNode('FRAME', frame.id, {
    name: 'input', x: 0, y: inputTop, width: W, height: INPUT_H,
    fills: [solid(C.surface)],
    cornerRadius: RADIUS,
    strokes: [{ ...solid(borderColor), weight: BORDER_W, align: 'INSIDE' }],
  });
  // Text: Query (text; disabled → disabled-Farbe) bzw. Placeholder (layout.css Zeile 32 → muted)
  const showQuery = query.length > 0;
  addText(input.id, showQuery ? 'input/query' : 'input/placeholder', {
    x: PAD_X, y: (INPUT_H - LH) / 2, w: W - 2 * PAD_X, h: LH,
    text: showQuery ? query : placeholder,
    color: showQuery ? (enabled ? C.text : C.disabled) : C.muted,
    alignVertical: 'CENTER',
  });

  // Overlay-Teilbaum (overlay/component.json + scroll-area/component.json +
  // accessibility.html-Templates: surface > content > viewport > content > list)
  const surface = graph.createNode('FRAME', frame.id, {
    name: 'overlay/surface', x: 0, y: popupTop, width: W, height: viewportH,
    visible: popupVisible,
    fills: [solid(C.surface)],
    cornerRadius: RADIUS,
    clipsContent: true,
    // overlay/layout.css Zeile 11: box-shadow: 0 2px 8px #0003 → Drop-Shadow 1:1
    effects: [{ type: 'DROP_SHADOW', color: { r: 0, g: 0, b: 0, a: 0.2 }, offset: { x: 0, y: 2 }, radius: 8, spread: 0, visible: true }],
  });
  const ovContent = graph.createNode('FRAME', surface.id, {
    name: 'overlay/content', x: 0, y: 0, width: W, height: viewportH, fills: [],
  });
  // scroll-area/layout.css Zeile 1: [data-part="viewport"] { max-height; overflow-y: auto } → clippen
  const viewport = graph.createNode('FRAME', ovContent.id, {
    name: 'scroll/viewport', x: 0, y: 0, width: W, height: viewportH, fills: [], clipsContent: true,
  });
  // scroll-area/layout.css Zeile 2: [data-part="content"] { margin: 0; padding: 0 }
  const scrollContent = graph.createNode('FRAME', viewport.id, {
    name: 'scroll/content', x: 0, y: 0, width: W, height: contentH, fills: [],
  });
  // README "Sichtbare Geometrie": scroll-end zeigt die aktive letzte Option im Viewport;
  // "darf dazu der Inhalt des geclippten Viewports entsprechend versetzt werden".
  // Versatz = viewportH − contentH = 160 − 7×32 = −64 (alle 7 Layer bleiben erhalten).
  if (s.id === 'scroll-end') scrollContent.y = viewportH - contentH;

  // list (data-part="list", role=listbox; scroll-area/layout.css Zeilen 3–9: kein Padding/Margin)
  const list = graph.createNode('FRAME', scrollContent.id, {
    name: 'list', x: 0, y: 0, width: W, height: contentH, fills: [],
  });

  if (isMessageCase) {
    // README: "Bei loading, empty und error zeigt der Popupinhalt eine Zeile mit der
    // entsprechenden Meldung." Zeilenfarbe ist in den Quellen nicht definiert →
    // ererbte Komponententextfarbe (color: var(--ac-text), layout.css Zeile 7) — Lücke, REPORT.md.
    const row = graph.createNode('FRAME', list.id, {
      name: 'message-row', x: 0, y: 0, width: W, height: ROW, fills: [],
    });
    addText(row.id, 'text', {
      x: PAD_X, y: (ROW - LH) / 2, w: W - 2 * PAD_X, h: LH,
      text: message, color: C.text, alignVertical: 'CENTER',
    });
  }

  // Optionen (data-part="option": Höhe rowHeight, padding 6px 12px; aria-selected → highlight;
  // aria-disabled → disabled-Farbe; layout.css Zeilen 34–42)
  results.forEach((r, i) => {
    const isActive = s.activeKey === r.key;
    const row = graph.createNode('FRAME', list.id, {
      name: `option/${r.key}`, x: 0, y: i * ROW, width: W, height: ROW,
      fills: isActive ? [solid(C.highlight)] : [],
    });
    addText(row.id, 'text', {
      x: PAD_X, y: (ROW - LH) / 2, w: W - 2 * PAD_X, h: LH,
      text: r.label,
      color: r.disabled ? C.disabled : C.text,
      alignVertical: 'CENTER',
    });
  });

  // status (data-part="status": Höhe lineHeight, margin-top statusGap, font 12, muted;
  // error-Zustand → error-Farbe, layout.css Zeilen 43–49). Ohne Meldung: Text leer.
  addText(frame.id, 'status', {
    x: 0, y: statusY, w: W, h: LH,
    text: message, color: statusColor, fontSize: FS_STATUS,
  });

  return { frame, frameH, viewportH, contentH, popupVisible, message };
}

// ---------------------------------------------------------------------------
// 5) Aussenanordnung (frei nach README "Exportrahmen"): 2 Spalten, Reihung wie
//    in stories.json. Seitentitel frei.
// ---------------------------------------------------------------------------
graph.createNode('TEXT', page.id, {
  name: 'Seitentitel', x: 40, y: 40, width: 720, height: 28,
  text: 'Autocomplete · 10 Fälle (stories.json, Definition 0.1.0)',
  fills: [solid(C.text)],
  fontSize: 24,
  fontFamily: FONT,
  fontWeight: 400,
  lineHeight: 28,
  textAlignHorizontal: 'LEFT',
  textAlignVertical: 'CENTER',
  textAutoResize: 'NONE',
});

const COL_X = [40, 480];
const ROW_Y = [120, 440, 760, 1080, 1400];
const built = STORIES.map((s, i) => {
  const res = buildCase(s, COL_X[i % 2], ROW_Y[Math.floor(i / 2)]);
  res.story = s;
  return res;
});

graph.updateNode(page.id, { width: 880, height: 1720 });

// ---------------------------------------------------------------------------
// 6) Export über die gepinnte Toolchain
// ---------------------------------------------------------------------------
const outPath = `${OUT_DIR}/autocomplete.fig`;
const bytes = await exportFigFile(graph);
writeFileSync(outPath, bytes);
const sha = createHash('sha256').update(bytes).digest('hex');
console.log(JSON.stringify({
  file: outPath,
  bytes: bytes.length,
  sha256: sha,
  cases: built.map((b) => ({
    id: b.story.id, phase: b.story.phase,
    frameH: b.frameH, viewportH: b.viewportH, contentH: b.contentH,
    popupVisible: b.popupVisible, status: b.message,
  })),
}, null, 2));
