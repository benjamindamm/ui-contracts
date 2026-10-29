// Unabhängiges natives Readback des Reviewers (run-04, Blindphase).
// Muster: tools/design-review/read-fig.mjs (parseFigFile, populate:'all').
// Prüfladung: eigene Logik; Soll-Werte direkt aus den Originalquellen (tokens.json, stories.json,
// accessibility.rules.json; CSS-Regeln mit Locator hartkodiert). Keinerlei Builder-Dateien.
import { readFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';
import { join } from 'node:path';

const REPO = '/Users/kcnpxcp/Dev/GitHub/ui-contracts';
const FIGS = {
  a: join(REPO, 'examples/autocomplete/reproducibility/run-04/builder-a/autocomplete.fig'),
  b: join(REPO, 'examples/autocomplete/reproducibility/run-04/builder-b/autocomplete.fig'),
};
const OUT = process.argv[2];

const core = await import(pathToFileURL(join(REPO, 'tools/openpencil/node_modules/@open-pencil/core/dist/index.js')));

// ---------- Quellen laden und eigenständig auflösen ----------
const tokens = JSON.parse(await readFile(join(REPO, 'components/tokens.json'), 'utf8'));
function resolveToken(name) {
  let cur = tokens;
  for (const k of name.split('.')) cur = cur[k];
  const v = cur['$value'];
  if (typeof v === 'string' && v.startsWith('{')) return resolveToken(v.slice(1, -1));
  return v;
}
const px = (n) => resolveToken('autocomplete.' + n);
const dim = (n) => {
  const v = px(n);
  if (v.unit !== 'px') throw new Error('unit ' + v.unit);
  return v.value;
};
const col = (n) => {
  const t = px(n);
  if (t.colorSpace !== 'srgb' || t.alpha !== 1) throw new Error('color ' + n);
  return '#' + t.components.map((x) => Math.round(x * 255).toString(16).padStart(2, '0')).join('').toUpperCase();
};
const C = {
  surface: col('surface'), text: col('text'), muted: col('muted'), border: col('border'),
  focus: col('focus'), highlight: col('highlight'), disabled: col('disabled'), error: col('error'),
};
const D = {
  width: dim('width'), inputHeight: dim('inputHeight'), rowHeight: dim('rowHeight'), maxHeight: dim('maxHeight'),
  labelGap: dim('labelGap'), statusGap: dim('statusGap'), radius: dim('radius'), borderWidth: dim('borderWidth'),
  gap: dim('gap'), fontSize: dim('fontSize'), statusFontSize: dim('statusFontSize'), lineHeight: dim('lineHeight'),
  fontFamily: px('fontFamily'),
};
const stories = JSON.parse(await readFile(join(REPO, 'components/autocomplete/stories.json'), 'utf8'));
const storyById = Object.fromEntries(stories.stories.map((s) => [s.id, s]));
const rules = JSON.parse(await readFile(join(REPO, 'components/autocomplete/accessibility.rules.json'), 'utf8'));

const CASES = ['closed', 'opening', 'loading', 'ready', 'active', 'scroll-end', 'selected', 'empty', 'error', 'disabled'];
const POPUP = new Set(['loading', 'ready', 'active', 'scroll-end', 'empty', 'error']);
const RESULTS = new Set(['ready', 'active', 'scroll-end']);
const FOCUS = new Set([...RESULTS, 'loading', 'empty', 'error', 'opening']);
const PLACEHOLDER = 'Stadt suchen …';
const expectedStatusText = (cid) => {
  if (RESULTS.has(cid)) return rules.messages.results.replace('{count}', '7');
  if (cid === 'selected') return rules.messages.selected.replace('{label}', 'Berlin');
  return rules.messages[cid];
};
const expectedInputText = (cid) => {
  if (cid === 'selected') return 'Berlin';
  const q = storyById[cid].inputs.query || '';
  return q || PLACEHOLDER;
};

// ---------- FIG parsen ----------
function hexOf(paint) {
  if (!paint || paint.visible === false || paint.type !== 'SOLID') return null;
  const c = paint.color || {};
  return '#' + ['r', 'g', 'b'].map((k) => Math.round(c[k] * 255).toString(16).padStart(2, '0')).join('').toUpperCase();
}
const fillOf = (n) => {
  const ps = (n.fills || []).filter((p) => p.visible !== false);
  return ps.length === 1 ? hexOf(ps[0]) : ps.length > 1 ? 'MULTI(' + ps.map(hexOf).filter(Boolean).join('+') + ')' : null;
};

async function readFig(path) {
  const bytes = await readFile(path);
  const graph = await core.parseFigFile(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), { populate: 'all' });
  const fields = ['id', 'type', 'name', 'parentId', 'childIds', 'x', 'y', 'width', 'height',
    'visible', 'locked', 'opacity', 'clipsContent', 'cornerRadius', 'fills', 'strokes',
    'text', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'effects'];
  return [...graph.getAllNodes()].map((n) => Object.fromEntries(fields.map((k) => [k, n[k] ?? null])));
}

// ---------- Baum-Operationen ----------
function buildTree(nodes) {
  const byId = Object.fromEntries(nodes.map((n) => [n.id, n]));
  const absPos = {};
  function abs(n) {
    if (absPos[n.id] !== undefined) return absPos[n.id];
    const p = byId[n.parentId];
    const r = p ? { x: abs(p).x + n.x, y: abs(p).y + n.y } : { x: n.x, y: n.y };
    absPos[n.id] = r;
    return r;
  }
  function desc(n) {
    const out = [];
    const seen = new Set();
    (function walk(p) {
      if (seen.has(p.id)) throw new Error('Cycle');
      seen.add(p.id);
      for (const cid of p.childIds || []) {
        const c = byId[cid];
        out.push(c);
        walk(c);
      }
    })(n);
    return out;
  }
  const visibleChain = (n) => {
    let cur = n;
    const seen = new Set();
    while (cur) {
      if (seen.has(cur.id)) return false;
      seen.add(cur.id);
      if (cur.visible === false || (cur.opacity !== null && cur.opacity !== undefined && cur.opacity <= 0)) return false;
      cur = cur.parentId ? byId[cur.parentId] : null;
    }
    return true;
  };
  return { byId, abs, desc, visibleChain };
}

// ---------- Fallprüfungen ----------
function assessCase(cid, frame, T, notes) {
  const { byId, abs, desc, visibleChain } = T;
  const checks = [];
  const feat = {};
  const put = (id, actual, expected, tol = null) => {
    let status = 'pass';
    if (tol !== null) {
      if (typeof actual === 'number' && Math.abs(actual - expected) <= tol) status = 'pass';
      else if (typeof actual === 'number') status = 'fail';
      else status = 'fail';
    } else {
      status = actual === expected ? 'pass' : 'fail';
    }
    if (status === 'fail' && id.endsWith('.fill') || status === 'fail' && id.includes('.stroke.color') ||
        status === 'fail' && id.includes('inputText.color') || status === 'fail' && id.includes('status.color') ||
        status === 'fail' && id.includes('.option') && id.includes('.textColor')) {
      const m = actual, e = expected;
      if (typeof m === 'string' && m.startsWith('#') && typeof e === 'string' && e.startsWith('#')) {
        const delta = Math.max(...[1, 3, 5].map((i) => Math.abs(parseInt(m.slice(i, i + 2), 16) - parseInt(e.slice(i, i + 2), 16))));
        if (delta <= 3) status = 'warning';
      }
    }
    feat[id] = actual;
    checks.push({ id, actual, expected, status });
  };

  const ns = desc(frame);
  const frameAbs = abs(frame);
  put('frame.width', frame.width, D.width, 0.01);
  put('lockedNodeCount', [frame, ...ns].filter((n) => n.locked).length, 0);

  // Teile
  const input = ns.filter((n) => n.type !== 'TEXT' && /^input(?:$|\s|[·])/.test(n.name)).filter(visibleChain);
  const label = ns.filter((n) => n.type === 'TEXT' && n.name === 'label');
  const status = ns.filter((n) => n.type === 'TEXT' && /^status(?:$|\s|[·])/.test(n.name));
  put('parts.input.count', input.length, 1);
  put('parts.label.count', label.length, 1);
  put('parts.status.count', status.length, 1);
  const inp = input[0], lab = label[0], stat = status[0];
  if (!inp || !lab || !stat) { notes.push(cid + ': fehlendes Teil, weitere Teilprüfungen übersprungen'); return { checks, feat }; }

  // Label
  put('label.text', lab.text, storyById[cid].inputs.label);
  put('label.color', fillOf(lab), C.text);
  put('label.fontSize', lab.fontSize, D.fontSize, 0.01);
  put('label.lineHeight', lab.lineHeight, D.lineHeight, 0.01);
  put('label.fontFamily', lab.fontFamily, D.fontFamily);
  put('labelGap', abs(inp).y - (abs(lab).y + (lab.height || D.lineHeight)), D.labelGap, 0.01);

  // Input-Geometrie/Farben
  put('input.height', inp.height, D.inputHeight, 0.01);
  put('input.radius', inp.cornerRadius, D.radius, 0.01);
  put('input.fill', fillOf(inp), C.surface);
  const strokes = (inp.strokes || []).filter((s) => s.visible !== false);
  put('input.stroke.count', strokes.length, 1);
  if (strokes.length === 1) {
    put('input.stroke.weight', strokes[0].weight, D.borderWidth, 0.01);
    put('input.stroke.color', hexOf(strokes[0]), FOCUS.has(cid) ? C.focus : C.border);
  }
  const inpTexts = desc(inp).filter((n) => n.type === 'TEXT');
  put('inputText.count', inpTexts.length, 1);
  const t = inpTexts[0];
  if (t) {
    put('inputText.text', t.text, expectedInputText(cid));
    put('inputText.color', fillOf(t), (!storyById[cid].inputs.query && cid !== 'selected') ? C.muted : C.text, );
    put('inputText.fontFamily', t.fontFamily, D.fontFamily);
    put('inputText.fontSize', t.fontSize, D.fontSize, 0.01);
    put('inputText.lineHeight', t.lineHeight, D.lineHeight, 0.01);
  }

  // Status (README:24: Status-Region in allen Fällen benannt, leer ohne Meldung)
  put('status.text', stat.text, expectedStatusText(cid));
  put('status.color', fillOf(stat), cid === 'error' ? C.error : C.muted);
  put('status.fontSize', stat.fontSize, D.statusFontSize, 0.01);
  put('status.lineHeight', stat.lineHeight, D.lineHeight, 0.01);
  put('status.fontFamily', stat.fontFamily, D.fontFamily);
  put('status.visible', visibleChain(stat), true);

  // Popup
  const surfaces = ns.filter((n) => n.type !== 'TEXT' && /surface/i.test(n.name));
  const visSurfaces = surfaces.filter(visibleChain);
  put('surface.visibleCount', visSurfaces.length, POPUP.has(cid) ? 1 : 0);
  const sur = visSurfaces[0];
  if (POPUP.has(cid) && sur) {
    const sAbs = abs(sur);
    put('surface.width', sur.width, D.width, 0.01);
    put('surface.leftAligned', Math.round((sAbs.x - abs(inp).x) * 100) / 100, 0, 0.01);
    put('surface.topGap', Math.round((sAbs.y - (abs(inp).y + inp.height)) * 100) / 100, D.gap, 0.01);
    put('surface.fill', fillOf(sur), C.surface);
    put('surface.radius', sur.cornerRadius, D.radius, 0.01);
    const shadow = (sur.effects || []).filter((e) => e.type === 'DROP_SHADOW');
    notes.push(`${cid}: surface effects: ${JSON.stringify((sur.effects || []).map((e) => e.type))} (Beobachtung, Schatten nicht Gegenprüfer-Scope)`);
    void shadow;

    const viewports = ns.filter((n) => n.type !== 'TEXT' && /viewport/i.test(n.name)).filter(visibleChain);
    put('viewport.count', viewports.length, 1);
    const vp = viewports[0];
    if (vp) {
      put('viewport.clipsContent', vp.clipsContent, true);
      const expH = RESULTS.has(cid) ? Math.min(7 * D.rowHeight, D.maxHeight) : D.rowHeight;
      put('viewport.height', vp.height, expH, 0.01);
      const listNodes = ns.filter((n) => n.type !== 'TEXT' && /^list(?:$|\s|[·])/i.test(n.name));
      notes.push(`${cid}: list-Teilung: ${listNodes.map((n) => n.name).join(', ') || 'kein Name mit list-Präfix (Beobachtung)'}`);

      // Optionen
      const options = ns.filter((n) => n.type !== 'TEXT' && /^option(\s|\/)/i.test(n.name));
      put('options.count', options.length, RESULTS.has(cid) ? 7 : 0);
      if (RESULTS.has(cid)) {
        const records = storyById[cid].results;
        const vpAbs = abs(vp);
        const activeKey = storyById[cid].activeKey;
        const highlightFills = [];
        options.forEach((opt, i) => {
          const ot = desc(opt).filter((n) => n.type === 'TEXT');
          const record = records[i];
          if (!record) return;
          put(`option${i}.height`, opt.height, D.rowHeight, 0.01);
          put(`option${i}.text`, ot[0] ? ot[0].text : null, record.label);
          put(`option${i}.textColor`, ot[0] ? fillOf(ot[0]) : null, record.disabled ? C.disabled : C.text);
          const oAbs = abs(opt);
          const inViewport = oAbs.y >= vpAbs.y - 0.01 && oAbs.y + opt.height <= vpAbs.y + vp.height + 0.01;
          if (i === 6 && cid === 'scroll-end') put('scrollEnd.lastOptionInViewport', inViewport, true);
          feat[`option${i}.absY`] = Math.round(oAbs.y * 100) / 100;
          feat[`option${i}.inViewport`] = inViewport;
          const of = fillOf(opt);
          if (of === C.highlight) highlightFills.push(i);
          feat[`option${i}.fill`] = of;
        });
        const expActive = records.findIndex((r) => r.key === activeKey);
        feat[`${cid === 'active' ? 'activeHighlight' : cid === 'scroll-end' ? 'scrollEndHighlight' : 'readyNoHighlight'}.indexes`] = highlightFills;
        if (activeKey !== undefined) put(`${cid}.highlightOption.index`, highlightFills.length === 1 ? highlightFills[0] : (highlightFills.length === 0 ? 'none' : 'multiple'), expActive);
      }
      // Meldung-Zeile im Popup (loading/empty/error) — README:24: "zeigt der Popupinhalt eine Zeile mit der entsprechenden Meldung"
      if (!RESULTS.has(cid)) {
        const msg = rules.messages[cid];
        const lines = desc(sur).filter((n) => n.type === 'TEXT' && n.text === msg);
        put('popup.messageLine.count', lines.length, 1);
        const ml = lines[0];
        if (ml) {
          put('popup.messageLine.text', ml.text, msg);
          put('popup.messageLine.visible', visibleChain(ml), true);
          const mAbs = abs(ml);
          feat['popup.messageLine.name'] = ml.name;
          feat['popup.messageLine.color'] = fillOf(ml);
          feat['popup.messageLine.height'] = ml.height;
          feat['popup.messageLine.absY'] = Math.round(mAbs.y * 100) / 100;
        }
      }
      // Status-Position: nach sichtbarem Popup mit statusGap
      put('statusGap.afterPopup', Math.round((abs(stat).y - (sAbs.y + sur.height)) * 100) / 100, D.statusGap, 0.01);
    }
  } else if (!POPUP.has(cid)) {
    put('statusGap.afterInput', Math.round((abs(stat).y - (abs(inp).y + inp.height)) * 100) / 100, D.statusGap, 0.01);
  }

  // Typografie aller Texte
  const allText = [frame, ...ns].filter((n) => n.type === 'TEXT');
  feat[`${cid === 'closed' ? '' : ''}textCount`] = allText.length;
  const badFonts = [];
  for (const t of allText) {
    if (t.fontFamily !== D.fontFamily) badFonts.push({ name: t.name, text: t.text, font: t.fontFamily });
    const expSize = (t.id === stat.id) ? D.statusFontSize : D.fontSize;
    if (Math.abs((t.fontSize || 0) - expSize) > 0.01) badFonts.push({ name: t.name, text: t.text, fontSize: t.fontSize, expected: expSize });
    if (Math.abs((t.lineHeight || 0) - D.lineHeight) > 0.01) badFonts.push({ name: t.name, text: t.text, lineHeight: t.lineHeight, expected: D.lineHeight });
  }
  put('typography.allText', badFonts.length === 0 ? 'ok' : JSON.stringify(badFonts), 'ok');

  return { checks, feat };
}

// ---------- Hauptlauf ----------
const out = { tool: 'reviewer-independent-readback', run: 'run-04', generatedBy: 'reviewer-blind', sources: {
  tokens: 'components/tokens.json', stories: 'components/autocomplete/stories.json', rules: 'components/autocomplete/accessibility.rules.json',
  css: 'components/autocomplete/layout.css (Regeln mit Locator hartkodiert)', overlayCss: 'components/overlay/layout.css (Anker/Gap)' },
  expected: { colors: C, dims: D, status: Object.fromEntries(CASES.map((c) => [c, expectedStatusText(c)])), input: Object.fromEntries(CASES.map((c) => [c, expectedInputText(c)])) },
  designs: {} };

for (const [x, path] of Object.entries(FIGS)) {
  const nodes = await readFig(path);
  const T = buildTree(nodes);
  const caseNodes = {};
  for (const n of nodes) {
    if (n.type === 'FRAME' || n.type === 'COMPONENT') {
      const key = n.name.toLowerCase().trim();
      if (CASES.includes(key) || CASES.includes(key.replace(/^autocomplete\s*\/\s*/, ''))) {
        const cid = CASES.includes(key) ? key : key.replace(/^autocomplete\s*\/\s*/, '');
        (caseNodes[cid] ||= []).push(n);
      }
    }
  }
  const notes = [];
  const result = { frameNames: Object.fromEntries(Object.entries(caseNodes).map(([k, v]) => [k, v.map((n) => ({ name: n.name, type: n.type }))])), cases: {} };
  for (const cid of CASES) {
    const list = caseNodes[cid] || [];
    if (list.length !== 1) {
      result.cases[cid] = { checks: [{ id: 'frame.count', actual: list.length, expected: 1, status: list.length === 1 ? 'pass' : 'fail' }], feat: {} };
      notes.push(`${x}/${cid}: Frame-Zählung ${list.length}`);
      continue;
    }
    const r = assessCase(cid, list[0], T, notes);
    result.cases[cid] = r;
  }
  const lockedAll = nodes.filter((n) => n.locked);
  result.docLockedNodes = lockedAll.length;
  result.totalNodes = nodes.length;
  result.notes = notes;
  const allChecks = Object.values(result.cases).flatMap((c) => c.checks);
  result.summary = {
    checks: allChecks.length,
    pass: allChecks.filter((c) => c.status === 'pass').length,
    warning: allChecks.filter((c) => c.status === 'warning').length,
    fail: allChecks.filter((c) => c.status === 'fail').length,
    failures: allChecks.filter((c) => c.status === 'fail'),
    warnings: allChecks.filter((c) => c.status === 'warning'),
  };
  out.designs[x] = result;
}

await (await import('node:fs/promises')).writeFile(OUT, JSON.stringify(out, null, 2) + '\n');
console.log(JSON.stringify(Object.fromEntries(Object.entries(out.designs).map(([x, r]) => [x, r.summary]))));
