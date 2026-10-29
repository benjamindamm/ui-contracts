// Generator run-04 · Builder A
// Erzeugt autocomplete.fig aus den hashgebundenen Originalquellen (input-manifest.json, run-04).
// Toolchain: gepinnte @open-pencil/core + @open-pencil/scene-graph unter tools/openpencil/ (Laufblatt run-04).
//
// Quellbezug der Werte:
// - tokens.json (components/tokens.json): alle Farben, Maesse, Gaepen, Typografie (dieses Skript liest sie
//   zur Laufzeit ein und veroeffentlicht keine neu erfundenen Werte).
// - stories.json: zehn Faelle, Inputs, Ergebnisrecords, activeKey, value.
// - accessibility.rules.json: Projektion (popupVisible), Meldungsvorlagen (messages).
// - layout.css (autocomplete/): Geometrie-Konstanten, die im Skript als dokumentierte Konstanten stehen:
//   * Label: display block; height lineHeight; margin-bottom labelGap            (layout.css:9-13)
//   * Input: border-box; height inputHeight; padding 0 paddingInline; border borderWidth solid; radius; surface (layout.css:14-24)
//   * Input-Text start: border(1) + paddingInline(12) = 13px; vertikal zentriert (44-20)/2 = 12px
//   * Fokus-Rand (focus) in den Zustaenden opening/loading/ready/empty/error     (layout.css:25-31)
//   * placeholder-Farbe muted                                                    (layout.css:32)
//   * disabled: color disabled; border-color border                              (layout.css:33)
//   * Option: border-box; height rowHeight; padding 6px paddingInline            (layout.css:34-40)
//   * aktive Option: background highlight                                        (layout.css:41)
//   * deaktivierte Option: color disabled                                         (layout.css:42)
//   * Status: height lineHeight; margin-top statusGap; font-size statusFontSize; color muted (layout.css:43-48)
//   * Status bei error: color error                                               (layout.css:49)
// - overlay/layout.css: Surface am Inputende plus gap, gleiche Breite/linke Kante, surface, radius,
//   box-shadow 0 2px 8px #0003 (= rgba(0,0,0,0.2)), kein border (overlay/layout.css:2-13)
// - scroll-area/layout.css: viewport max-height maxHeight; content/list ohne Margin/Padding (scroll-area/layout.css:1-9)
// - README (components/autocomplete/README.md):
//   * Viewporthoehe = min(Ergebnisanzahl x rowHeight, maxHeight); loading/empty/error: eine Zeile Meldung
//   * Status unter dem sichtbaren Popup, sonst unter dem Input; ohne Meldung leer
//   * scroll-end: aktive letzte Option im Viewport, Inhalt versetzt, alle Ergebnislayer erhalten
//   * selected = closed mit value; disabled = closed mit enabled=false; bei disabled keine Popupteile sichtbar
//   * verborgener Popup belegt keinen Platz
//
// Designentscheidungen (in REPORT.md dokumentiert):
// - Jeder Fall ist ein benannter FRAME. Verborgene Popups (closed/opening/selected/disabled) bleiben als
//   unsichtbare (visible=false) Layer erhalten, damit alle Teile in allen FaelLEN editierbar sind;
//   sie belegen keinen Platz (Status steht in allen FaelLEN unter Input bzw. sichtbarem Popup).
// - disabled-Input: Die :disabled-Regel (layout.css:33) setzt color: disabled fuer eingegebenen Text;
//   der leere Query-Fall zeigt jedoch den Placeholder, und die explizite ::placeholder-Regel
//   (layout.css:32) legt seine Farbe muted fest - im CSS-Cascade bleibt der Platzhalter muted.
// - Aussenanordnung (2 Spalten), Seitentitel und Fall-Kaptionen sind frei und nutzen nur Token-Farben.

import { readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { SceneGraph } from "../../../../../tools/openpencil/node_modules/@open-pencil/scene-graph/dist/index.js";
import { exportFigFile } from "../../../../../tools/openpencil/node_modules/@open-pencil/core/dist/index.js";

const OUT_DIR = new URL("./", import.meta.url);
const ROOT = new URL("../../../../..", import.meta.url); // Repositorywurzel

const sha256 = (buf) => createHash("sha256").update(buf).digest("hex");
function readPinned(relPath) {
  const buf = readFileSync(new URL("../input-manifest.json", OUT_DIR));
  const manifest = JSON.parse(buf.toString("utf8"));
  // Manifest-Hash gegen task.json (src-Referenz) pruefen: 74aa9eab...
  const expectedManifest = "74aa9eabcfe7301a0845d230cc1ff4acd6ce14cf0435ec1ed0e6cba0b6e25eb2";
  if (sha256(buf) !== expectedManifest) throw new Error("input-manifest.json weicht vom task.json-Hash ab");
  const entry = manifest.files[relPath];
  if (!entry) throw new Error("Quelle nicht im Manifest: " + relPath);
  const data = readFileSync(new URL(manifest.root + "/" + relPath, ROOT));
  if (sha256(data) !== entry) throw new Error("Hashabweichung bei " + relPath);
  return JSON.parse(data.toString("utf8"));
}

// ---- Quellen laden (hashgeprueft) -------------------------------------------
const tokens = readPinned("tokens.json");
const stories = readPinned("autocomplete/stories.json");
const a11y = readPinned("autocomplete/accessibility.rules.json");

// ---- Token auflösen (autocomplete.*, Aliase {base.*}) -------------------------
const A = tokens.autocomplete;
const dim = (name) => {
  const v = A[name].$value;
  if (typeof v === "string") {
    const m = v.match(/^\{base\.([a-zA-Z]+)\}$/);
    if (!m) throw new Error("Alias nicht geloest: " + name);
    const b = tokens.base[m[1]].$value;
    if (typeof b === "string") throw new Error("Doppelalias: " + name);
    return b.value;
  }
  return v.value;
};
const color = (name) => {
  const c = A[name].$value;
  if (c.colorSpace !== "srgb") throw new Error("Unerwarteter Farbraum: " + name);
  return { r: c.components[0], g: c.components[1], b: c.components[2], a: c.alpha };
};
const hex = (c) =>
  "#" + [c.r, c.g, c.b, c.a].map((v) => Math.round(v * 255).toString(16).padStart(2, "0")).join("");

const T = {
  width: dim("width"), inputHeight: dim("inputHeight"), rowHeight: dim("rowHeight"),
  maxHeight: dim("maxHeight"), gap: dim("gap"), labelGap: dim("labelGap"), statusGap: dim("statusGap"),
  lineHeight: dim("lineHeight"), fontSize: dim("fontSize"), statusFontSize: dim("statusFontSize"),
  radius: dim("radius"), borderWidth: dim("borderWidth"), paddingInline: dim("paddingInline"),
  fontFamily: A.fontFamily.$value,
  surface: color("surface"), text: color("text"), muted: color("muted"), border: color("border"),
  focus: color("focus"), highlight: color("highlight"), disabled: color("disabled"), error: color("error"),
};
console.log("Tokens:", JSON.stringify({ width: T.width, inputHeight: T.inputHeight, rowHeight: T.rowHeight, maxHeight: T.maxHeight, gap: T.gap, labelGap: T.labelGap, statusGap: T.statusGap, lineHeight: T.lineHeight, fontSize: T.fontSize, statusFontSize: T.statusFontSize, radius: T.radius, borderWidth: T.borderWidth, paddingInline: T.paddingInline, fontFamily: T.fontFamily }));
for (const k of ["surface", "text", "muted", "border", "focus", "highlight", "disabled", "error"]) console.log("  " + k, hex(T[k]));

// ---- Geometrie-Konstanten aus den layout.css-Dateien (dok. oben) -------------
const OPTION_PAD_V = 6;      // autocomplete/layout.css:38 (padding: 6px var(--ac-padding-inline))
const SURFACE_SHADOW = { offset: { x: 0, y: 2 }, radius: 8, color: { r: 0, g: 0, b: 0, a: 0.2 } }; // overlay/layout.css:11 (#0003)
const INPUT_TEXT_X = T.borderWidth + T.paddingInline; // 13
const INPUT_TEXT_Y = (T.inputHeight - T.lineHeight) / 2; // 12
const OPTION_TEXT_X = T.paddingInline;   // 12
const OPTION_TEXT_Y = OPTION_PAD_V;      // 6
const LABEL_Y = 0;
const INPUT_Y = LABEL_Y + T.lineHeight + T.labelGap;             // 28
const INPUT_BOTTOM = INPUT_Y + T.inputHeight;                    // 72
const POPUP_TOP = INPUT_BOTTOM + T.gap;                          // 80

// ---- Graph --------------------------------------------------------------------
const g = new SceneGraph();
const defaultPage = g.getPages()[0]; // "Page 1" aus dem Konstrutor
const page = g.addPage("Autocomplete");

const solid = (c, opacity = 1) => ({ type: "SOLID", color: c, opacity, visible: true });
const stroke = (c, weight, align = "INSIDE") => ({ type: "SOLID", color: c, opacity: 1, visible: true, weight, align });

function text(parentId, name, x, y, w, h, content, size, colorValue, opts = {}) {
  const t = g.createNode("TEXT", parentId, {
    name, x, y, width: w, height: h, text: content,
    fontFamily: T.fontFamily, fontSize: size, fontWeight: 400, italic: false,
    lineHeight: T.lineHeight, textAlignVertical: "CENTER", textDirection: "LTR",
    textAutoResize: "NONE", fills: [solid(colorValue)],
    ...opts,
  });
  return t;
}

// ---- Falldaten -----------------------------------------------------------------
const MSG = a11y.messages;
const PROJ = a11y.projections;

function statusMessage(story) {
  const { phase } = story;
  if (story.value) return MSG.selected.replaceAll("{label}", story.results.find((r) => r.key === story.value).label);
  switch (phase) {
    case "closed": return MSG.closed;
    case "opening": return MSG.opening;
    case "loading": return MSG.loading;
    case "ready": return MSG.results.replaceAll("{count}", String(story.results.length));
    case "empty": return MSG.empty;
    case "error": return MSG.error;
    default: throw new Error("Phase ohne Meldung: " + phase);
  }
}

const caseSpecs = stories.stories.map((story) => {
  const enabled = story.inputs.enabled !== false; // stories.json: inputs.enabled (disabled-Fall: false)
  const popupVisible = !!PROJ[story.phase]?.popupVisible && enabled;
  const hasResults = story.results.length > 0;
  const isMessage = story.phase === "loading" || story.phase === "empty" || story.phase === "error";
  const listHeight = hasResults ? Math.min(story.results.length * T.rowHeight, T.maxHeight) : 0;
  const popupH = isMessage ? T.rowHeight : listHeight;
  const contentH = hasResults ? story.results.length * T.rowHeight : (isMessage ? T.rowHeight : 0);
  const contentOffset = story.id === "scroll-end" ? -(contentH - T.maxHeight) : 0; // -64
  const borderFocus = ["opening", "loading", "ready", "empty", "error"].includes(story.phase) && enabled;
  const hasQuery = story.inputs.query !== "";
  const inputText = hasQuery ? story.inputs.query : story.inputs.placeholder;
  const inputColor = hasQuery ? (enabled ? T.text : T.disabled) : T.muted;
  const statusY = popupVisible ? POPUP_TOP + popupH + T.statusGap : INPUT_BOTTOM + T.statusGap;
  return { story, popupVisible, isMessage, popupH, contentH, contentOffset, borderFocus, inputText, inputColor, statusY, statusText: statusMessage(story) };
});

// ---- Fall rendern ---------------------------------------------------------------
function renderCase(spec, x, y) {
  const { story, popupVisible, isMessage, popupH, contentH, contentOffset, borderFocus, inputText, inputColor, statusY, statusText } = spec;
  const caseH = statusY + T.lineHeight;
  const frame = g.createNode("FRAME", page.id, {
    name: story.id, x, y, width: T.width, height: caseH,
    fills: [], strokes: [],
  });

  // Label (data-part="label")
  text(frame.id, "label", 0, LABEL_Y, T.width, T.lineHeight, story.inputs.label, T.fontSize, T.text);

  // Input (data-part="input")
  const input = g.createNode("FRAME", frame.id, {
    name: "input", x: 0, y: INPUT_Y, width: T.width, height: T.inputHeight,
    cornerRadius: T.radius, fills: [solid(T.surface)],
    strokes: [stroke(borderFocus ? T.focus : T.border, T.borderWidth)],
  });
  text(input.id, "input.text", INPUT_TEXT_X, INPUT_TEXT_Y, T.width - 2 * T.borderWidth - 2 * T.paddingInline, T.lineHeight, inputText, T.fontSize, inputColor);

  // Popup: overlay.surface > overlay.scroll.viewport > listbox > option/<key> | message
  const surface = g.createNode("FRAME", frame.id, {
    name: "overlay.surface", x: 0, y: POPUP_TOP, width: T.width, height: popupH,
    cornerRadius: T.radius, fills: [solid(T.surface)],
    effects: [{ type: "DROP_SHADOW", color: SURFACE_SHADOW.color, offset: { ...SURFACE_SHADOW.offset }, radius: SURFACE_SHADOW.radius, spread: 0, visible: true }],
    visible: popupVisible,
  });
  const viewport = g.createNode("FRAME", surface.id, {
    name: "overlay.scroll.viewport", x: 0, y: 0, width: T.width, height: popupH,
    clipsContent: true,
  });
  const listbox = g.createNode("FRAME", viewport.id, {
    name: "listbox", x: 0, y: contentOffset, width: T.width, height: contentH,
  });
  story.results.forEach((result, i) => {
    const active = story.activeKey === result.key;
    const opt = g.createNode("FRAME", listbox.id, {
      name: "option/" + result.key, x: 0, y: i * T.rowHeight, width: T.width, height: T.rowHeight,
      fills: active ? [solid(T.highlight)] : [],
    });
    text(opt.id, "option.text", OPTION_TEXT_X, OPTION_TEXT_Y, T.width - 2 * T.paddingInline, T.lineHeight, result.label, T.fontSize, result.disabled ? T.disabled : T.text);
  });
  if (isMessage) {
    const line = g.createNode("FRAME", listbox.id, { name: "message", x: 0, y: 0, width: T.width, height: T.rowHeight });
    text(line.id, "message.text", OPTION_TEXT_X, OPTION_TEXT_Y, T.width - 2 * T.paddingInline, T.lineHeight, statusText, T.fontSize, T.text);
  }

  // Status (data-part="status"): unter sichtbarem Popup, sonst unter Input
  text(frame.id, "status", 0, statusY, T.width, T.lineHeight, statusText, T.statusFontSize, story.phase === "error" ? T.error : T.muted);

  return { frame, caseH };
}

// ---- Seite: Titel + Kaptionen + zehn Faelle in zwei Spalten --------------------
text(page.id, "page-title", 0, 0, 800, 28, "Autocomplete · die zehn Faelle", 20, T.text);
text(page.id, "page-subtitle", 0, 36, 860, 16,
  "Definition autocomplete-openpencil-0.1.0 · run-04 · Komponentenwerte aus tokens.json, layout.css, stories.json, accessibility.rules.json", 12, T.muted);

const COL_X = [0, 384];
const ROW_GAP = 48;
const CAPTION_H = 16;
const CAPTION_GAP = 8;
const TOP = 80;
const colOrder = [
  ["closed", "opening", "loading", "ready", "active"],
  ["scroll-end", "selected", "empty", "error", "disabled"],
];
const byId = Object.fromEntries(caseSpecs.map((s) => [s.story.id, s]));

let layoutLog = [];
for (let col = 0; col < 2; col++) {
  let cy = TOP;
  for (const id of colOrder[col]) {
    const spec = byId[id];
    const cap = text(page.id, "case-caption/" + id, COL_X[col], cy, T.width, CAPTION_H, id, 12, T.muted);
    const { frame, caseH } = renderCase(spec, COL_X[col], cy + CAPTION_H + CAPTION_GAP);
    layoutLog.push({ id, x: COL_X[col], y: cy + CAPTION_H + CAPTION_GAP, caseH });
    cy += CAPTION_H + CAPTION_GAP + caseH + ROW_GAP;
  }
}
g.deleteNode(defaultPage.id);

// ---- Export ----------------------------------------------------------------------
const bytes = await exportFigFile(g);
writeFileSync(new URL("autocomplete.fig", OUT_DIR), bytes);
console.log("Layout:", JSON.stringify(layoutLog, null, 1));
console.log("OK: autocomplete.fig geschrieben, Bytes =", bytes.byteLength);
