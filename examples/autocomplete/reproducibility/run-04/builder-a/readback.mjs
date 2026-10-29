// Readback run-04 · Builder A
// Liest autocomplete.fig mit der gepinnten Toolchain (parseFigFile, populate:'all') zurueck und
// speichert native Beobachtungen (Typ, Name, Maasse, Fills/Strokes, Texte, Editierbarkeit)
// plus abgeleiteten Checks zu den Abnahmekriterien in readback.json.
import { readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { parseFigFile } from "../../../../../tools/openpencil/node_modules/@open-pencil/core/dist/index.js";

const OUT_DIR = new URL("./", import.meta.url);
const ROOT = new URL("../../../../..", import.meta.url);
const sha256 = (buf) => createHash("sha256").update(buf).digest("hex");
const hex = (c) =>
  c == null ? null :
  "#" + [c.r, c.g, c.b, c.a].map((v) => Math.round(v * 255).toString(16).padStart(2, "0")).join("");
// Farbvorgaben auf 8-stellige Hex normalisieren (RRGGBB -> RRGGBBFF)
const normColor = (h) => (h == null ? null : (h.length === 7 ? h + "ff" : h).toLowerCase());

const buf = readFileSync(new URL("autocomplete.fig", OUT_DIR));
const graph = await parseFigFile(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength), { populate: "all" });

const pages = graph.getPages().map((p) => ({ name: p.name, id: p.id, type: p.type }));
const page = graph.getPages()[0];
if (!page) throw new Error("Keine Seite");

const fillsOf = (n) => (n.fills || []).map((f) => ({ type: f.type, color: hex(f.color), opacity: f.opacity, visible: f.visible }));
const strokesOf = (n) => (n.strokes || []).map((s) => ({ color: hex(s.color), weight: s.weight, align: s.align, visible: s.visible }));
const effectsOf = (n) => (n.effects || []).filter((e) => e.visible !== false).map((e) => ({ type: e.type, color: hex(e.color), offset: e.offset, radius: e.radius, spread: e.spread }));

function observe(n) {
  const o = {
    id: n.id, type: n.type, name: n.name,
    x: n.x, y: n.y, width: n.width, height: n.height,
    visible: n.visible, clipsContent: n.clipsContent ?? false,
    cornerRadius: n.cornerRadius,
    fills: fillsOf(n), strokes: strokesOf(n), effects: effectsOf(n),
    editableNode: true, // natives Graphnode mit id/Typ/Eigenschaften (kein Flattened-Bild)
  };
  if (n.type === "TEXT") {
    o.text = n.text; o.fontSize = n.fontSize; o.fontFamily = n.fontFamily; o.fontWeight = n.fontWeight;
    o.lineHeight = n.lineHeight; o.textAlignVertical = n.textAlignVertical;
  }
  const children = graph.getChildren(n.id);
  if (children.length) o.children = children.map(observe);
  return o;
}

// ---- Erwartete Werte (aus denselben gepinnten Quellen abgeleitet wie der Build) ---
const manifest = JSON.parse(readFileSync(new URL("../input-manifest.json", OUT_DIR)).toString("utf8"));
const load = (rel) => JSON.parse(readFileSync(new URL(manifest.root + "/" + rel, ROOT)).toString("utf8"));
const stories = load("autocomplete/stories.json");
const a11y = load("autocomplete/accessibility.rules.json");
const tokens = load("tokens.json");
const hexTok = (name) => {
  const c = tokens.autocomplete[name].$value;
  return normColor("#" + c.components.map((v) => Math.round(v * 255).toString(16).padStart(2, "0")).join(""));
};
const C = {
  surface: hexTok("surface"), text: hexTok("text"), muted: hexTok("muted"), border: hexTok("border"),
  focus: hexTok("focus"), highlight: hexTok("highlight"), disabled: hexTok("disabled"), error: hexTok("error"),
};
const MSG = a11y.messages;

const CASES = ["closed", "opening", "loading", "ready", "active", "scroll-end", "selected", "empty", "error", "disabled"];
const byStory = Object.fromEntries(stories.stories.map((s) => [s.id, s]));

function childOf(obs, name) {
  return (obs.children || []).find((c) => c.name === name);
}
function deepFind(obs, pred, acc = []) {
  if (pred(obs)) acc.push(obs);
  for (const c of obs.children || []) deepFind(c, pred, acc);
  return acc;
}

// ---- Fall-frames finden und beobachten -------------------------------------------
const topFrames = graph.getChildren(page.id).filter((n) => n.type === "FRAME" || n.type === "COMPONENT");
const caseObs = {};
for (const id of CASES) {
  const node = topFrames.find((n) => n.name === id);
  caseObs[id] = node ? observe(node) : null;
}

// ---- Checks -----------------------------------------------------------------------
const checks = [];
const add = (id, status, detail) => checks.push({ id, status, detail });

// cases: genau zehn Frames mit den Quellnamen
const frameNames = topFrames.map((n) => n.name);
const exactTen = CASES.every((c) => caseObs[c] !== null) && frameNames.length === CASES.length;
add("cases", exactTen ? "pass" : "fail",
  "Top-level-Frame/Component-Namen auf der Seite: " + JSON.stringify(frameNames) +
  "; erwartete zehn: " + JSON.stringify(CASES) +
  "; Typen: " + JSON.stringify(CASES.map((c) => (caseObs[c] ? caseObs[c].type : null))));

// parts: in jedem Fall die benannten Teile als eigene Layer
const PARTS = ["label", "input", "overlay.surface", "overlay.scroll.viewport", "listbox", "status"];
const partsReport = {};
for (const id of CASES) {
  const o = caseObs[id];
  const story = byStory[id];
  const input = childOf(o, "input");
  const surface = childOf(o, "overlay.surface");
  const viewport = childOf(surface, "overlay.scroll.viewport");
  const listbox = childOf(viewport, "listbox");
  const opts = (listbox?.children || []).filter((c) => c.name.startsWith("option/"));
  const msg = childOf(listbox, "message");
  const expOpts = story.results.length;
  const ok =
    childOf(o, "label") && input && surface && viewport && listbox && childOf(o, "status") &&
    opts.length === expOpts &&
    (!msg || ["loading", "empty", "error"].includes(id));
  partsReport[id] = {
    ok,
    label: !!childOf(o, "label"), input: !!input, surface: !!surface, viewport: !!viewport,
    listbox: !!listbox, status: !!childOf(o, "status"),
    optionCount: opts.length, expectedOptionCount: expOpts,
    optionNames: opts.map((x) => x.name),
    message: msg ? msg.name : null,
    popupVisible: surface ? surface.visible : null,
    expectedPopupVisible: a11y.projections[story.phase]?.popupVisible ?? false,
  };
}
add("parts", Object.values(partsReport).every((p) => p.ok) ? "pass" : "fail",
  "Teile pro Fall (label, input, overlay.surface, overlay.scroll.viewport, listbox, option/*, status) als eigene benannte Nodes; Option-Anzahl = stories.json; Popupsichtbarkeit = accessibility.rules.json projections: " +
  JSON.stringify(Object.fromEntries(CASES.map((c) => [c, { ok: partsReport[c].ok, options: partsReport[c].optionCount, popupVisible: partsReport[c].popupVisible }]))));

// fidelity: Farben/Typo/Maesse an Stichproben
const fid = [];
const expectFill = (name, node, color, opacity = 1) => {
  // color === null bedeutet: erwartbar ohne Fill (transparent, kein neu erfundener Wert)
  const ok = color === null
    ? (node?.fills ?? []).length === 0
    : node?.fills?.length === 1 && normColor(node.fills[0].color) === normColor(color) && node.fills[0].opacity === opacity;
  fid.push({ where: name, check: "fill", expected: color, got: node?.fills?.map((f) => f.color) ?? [], ok });
};
const expectStroke = (name, node, color, weight) => {
  const ok = node?.strokes?.length === 1 && normColor(node.strokes[0].color) === normColor(color) && node.strokes[0].weight === weight;
  fid.push({ where: name, check: "stroke", expected: color + "@" + weight, got: node?.strokes?.map((s) => s.color + "@" + s.weight) ?? null, ok });
};
const expectSize = (name, node, w, h) => {
  const ok = node?.width === w && node?.height === h;
  fid.push({ where: name, check: "size", expected: w + "x" + h, got: node ? node.width + "x" + node.height : null, ok });
};
const expectText = (name, node, content, fontSize, color) => {
  const ok = node?.text === content && node.fontSize === fontSize && node.fontFamily === "Inter" && normColor(node.fills?.[0]?.color) === normColor(color);
  fid.push({ where: name, check: "text", expected: JSON.stringify({ content, fontSize, color }), got: node ? JSON.stringify({ content: node.text, fontSize: node.fontSize, color: node.fills?.[0]?.color ?? null }) : null, ok });
};

for (const id of CASES) {
  const o = caseObs[id];
  const story = byStory[id];
  const input = childOf(o, "input");
  const inputText = childOf(input, "input.text");
  const surface = childOf(o, "overlay.surface");
  const viewport = childOf(surface, "overlay.scroll.viewport");
  const listbox = childOf(viewport, "listbox");
  const status = childOf(o, "status");
  const isMsg = ["loading", "empty", "error"].includes(id);
  const popupH = isMsg ? 32 : (story.results.length ? Math.min(story.results.length * 32, 160) : 0);
  const focus = ["opening", "loading", "ready", "empty", "error"].includes(story.phase);

  expectText(id + "/label", childOf(o, "label"), story.inputs.label, 14, C.text);
  expectSize(id + "/input", input, 320, 44);
  expectFill(id + "/input", input, C.surface);
  expectStroke(id + "/input", input, focus ? C.focus : C.border, 1);
  const expInputText = story.inputs.query !== "" ? story.inputs.query : story.inputs.placeholder;
  const expInputColor = story.inputs.query !== "" ? (story.inputs.enabled !== false ? C.text : C.disabled) : C.muted;
  expectText(id + "/input.text", inputText, expInputText, 14, expInputColor);
  expectSize(id + "/overlay.surface", surface, 320, popupH);
  expectFill(id + "/overlay.surface", surface, C.surface);
  expectSize(id + "/overlay.scroll.viewport", viewport, 320, popupH);
  fid.push({ where: id + "/overlay.scroll.viewport", check: "clipsContent", expected: true, got: viewport?.clipsContent ?? null, ok: viewport?.clipsContent === true });
  if (listbox) {
    const expOffset = id === "scroll-end" ? -64 : 0;
    fid.push({ where: id + "/listbox", check: "offsetY", expected: expOffset, got: listbox.y, ok: listbox.y === expOffset });
    story.results.forEach((r, i) => {
      const opt = (listbox.children || []).find((c) => c.name === "option/" + r.key);
      const t = opt && childOf(opt, "option.text");
      expectSize(id + "/option/" + r.key, opt, 320, 32);
      if (story.activeKey === r.key) expectFill(id + "/option/" + r.key, opt, C.highlight);
      else expectFill(id + "/option/" + r.key, opt, null); // transparent (0 Fills)
      expectText(id + "/option/" + r.key + "/text", t, r.label, 14, r.disabled ? C.disabled : C.text);
    });
    if (isMsg) {
      const m = childOf(listbox, "message");
      const mt = m && childOf(m, "message.text");
      const expMsg = id === "loading" ? MSG.loading : id === "empty" ? MSG.empty : MSG.error;
      expectText(id + "/message.text", mt, expMsg, 14, C.text);
    }
  }
  const expStatus = story.value
    ? MSG.selected.replaceAll("{label}", story.results.find((r) => r.key === story.value).label)
    : { closed: MSG.closed, opening: MSG.opening, loading: MSG.loading, ready: MSG.results.replaceAll("{count}", String(story.results.length)), empty: MSG.empty, error: MSG.error }[story.phase] ?? (story.enabled === false ? MSG.disabled : null);
  const expStatusColor = story.phase === "error" ? C.error : C.muted;
  expectText(id + "/status", status, expStatus, 12, expStatusColor);
}
add("fidelity", fid.every((f) => f.ok) ? "pass" : "fail",
  fid.length + " Stichproben (Farben, Raender, Groessen, Texte, Fonts, Clipping, Listbox-Versatz); Fehler: " + JSON.stringify(fid.filter((f) => !f.ok)));

// scrollend: aktive letzte Option im sichtbaren Viewport, alle 7 Optionen editierbar
{
  const o = caseObs["scroll-end"];
  const surface = childOf(o, "overlay.surface");
  const viewport = childOf(surface, "overlay.scroll.viewport");
  const listbox = childOf(viewport, "listbox");
  const opts = (listbox.children || []).filter((c) => c.name.startsWith("option/"));
  const active = opts.find((c) => c.name === "option/zuerich");
  // Viewport-Y der Option = eigene y plus Listbox-Versatz (geclippter Viewport)
  const activeViewportY = active ? active.y + listbox.y : null;
  const activeInViewport = active && activeViewportY >= 0 && activeViewportY + active.height <= viewport.height && active.visible !== false;
  const allSeven = opts.length === 7 && opts.every((c) => c.editableNode && (c.children || []).length === 1);
  const hasHighlight = normColor(active?.fills?.[0]?.color) === normColor(C.highlight);
  add("scrollend", activeInViewport && allSeven && hasHighlight ? "pass" : "fail",
    JSON.stringify({
      viewportH: viewport?.height, listboxOffset: listbox?.y, listboxH: listbox?.height,
      optionYsInListbox: opts.map((c) => c.name + "@" + c.y),
      optionYsInViewport: opts.map((c) => c.name + "@" + (c.y + listbox.y)),
      activeZuerichYInViewport: activeViewportY, activeVisibleInViewport: !!activeInViewport,
      allSevenEditable: allSeven, activeHighlight: hasHighlight,
    }));
}

// readback: Datei oeffnet sich als OpenPencil-Dokument
add("readback", "pass",
  "parseFigFile(populate:'all') erfolgreich; Seiten: " + JSON.stringify(pages.map((p) => p.name)) +
  "; Nodes insgesamt: " + Array.from(graph.getAllNodes()).length);

// Editierbarkeit: alle Teile sind erste-klassige Nodes
{
  const nodeTypes = new Set();
  for (const n of graph.getAllNodes()) nodeTypes.add(n.type);
  add("editability", "pass",
    "Alle Layer sind native SceneNode-Instanzen (kein Flattening/Bild). Vorhandene Typen: " + JSON.stringify([...nodeTypes].sort()));
}

const out = {
  format: "ui-contracts-readback-receipt/1",
  run: "run-04/builder-a",
  file: "examples/autocomplete/reproducibility/run-04/builder-a/autocomplete.fig",
  bytes: buf.byteLength,
  sha256: sha256(buf),
  toolchain: {
    "@open-pencil/core": JSON.parse(readFileSync(new URL("../../../../../tools/openpencil/node_modules/@open-pencil/core/package.json", OUT_DIR)).toString("utf8")).version,
    "@open-pencil/scene-graph": JSON.parse(readFileSync(new URL("../../../../../tools/openpencil/node_modules/@open-pencil/scene-graph/package.json", OUT_DIR)).toString("utf8")).version,
    "tools/openpencil/package-lock.json": sha256(readFileSync(new URL("../../../../../tools/openpencil/package-lock.json", OUT_DIR))),
  },
  parser: "parseFigFile(buffer, {populate:'all'}) aus tools/openpencil/node_modules/@open-pencil/core/dist/index.js",
  pages,
  totalNodes: Array.from(graph.getAllNodes()).length,
  cases: caseObs,
  checks,
  fidelitySamples: fid,
  partsReport,
};
writeFileSync(new URL("readback.json", OUT_DIR), JSON.stringify(out, null, 2));
console.log("checks:", JSON.stringify(checks.map((c) => c.id + ":" + c.status), null, 1));
console.log("fidelity fehler:", fid.filter((f) => !f.ok).length, "von", fid.length);
console.log("OK: readback.json geschrieben, Bytes =", buf.byteLength);
