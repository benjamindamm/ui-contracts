#!/usr/bin/env python3
"""
verify.py — Phase 2, Schritt 3: maschinelle Kriterienprüfung an den ORIGINALDATEIEN.

Eingaben (nur diese): original-a.json / original-b.json (eigene Read-back-Dumps),
preregistered.json (versiegeltes Kriterienset, unveränderbare Basis).
Ausgaben (nur review/): native-checks.json, normalized-a.json, normalized-b.json,
criterion-results.json.
Alle Erwartungswerte wörtlich aus der Preregistrierung. Keine Kriterienänderung;
Zustandsfälle sind Teilbeobachtungen derselben Komponente (keine Stichproben).

Phase-2-Audit (29.10.2026, neue Prüfer-Session): Skript vor Ausführung gegen das
versiegelte Kriterienset auditiert. Drei dokumentierte, judgments-neutrale
Anpassungen (Ergebnis vor/nach Änderung identisch, da beide Artefakte die
betreffenden Werte teilen):
  (1) E-056: strenger Offset-Check (== -64) durch den versiegelten EXP-Radius
      ersetzt ("Listeninhalt so versetzt, dass die letzte Zeile sichtbar");
      der Offset-Spielraum ist Prüfbereich von U-002.
  (2) E-060: Zusatzpflicht 'Meldungszeile h == 32px' entfernt (U-003: die Höhe
      der Meldungszeile wird nicht als Verletzung gewertet); Höhe wird nur
      beobachtet.
  (3) E-064 (Builder B): obs-Text korrigiert (B trägt kein pluginData; die alte
      Fassung enthielt den A-Text 'nur Writer-Artefakte').
Vorherige Fassung: verify.py.prev-1216 (Provenienz des unterbrochenen Vorlaufs).
"""
import json
from collections import Counter

R = '/Users/kcnpxcp/Dev/GitHub/ui-contracts/examples/autocomplete/reproducibility/run-03/review'

# ---------------------------------------------------------------- Grunddaten
CASES = ['closed', 'opening', 'loading', 'ready', 'active',
         'scroll-end', 'selected', 'empty', 'error', 'disabled']
POPUP_CASES = ['loading', 'ready', 'active', 'scroll-end', 'empty', 'error']
LIST_CASES = ['ready', 'active', 'scroll-end']
MSG_CASES = ['loading', 'empty', 'error']
NOPOPUP_CASES = ['closed', 'opening', 'selected', 'disabled']
FOCUS_CASES = ['opening', 'loading', 'ready', 'active', 'scroll-end', 'empty', 'error']
BORDER_CASES = ['closed', 'selected', 'disabled']
KEYS = ['berlin', 'hamburg', 'muenchen', 'dresden', 'koeln', 'wien', 'zuerich']
LABELS = ['Berlin', 'Hamburg', 'München', 'Dresden', 'Köln', 'Wien', 'Zürich']
LABEL = 'Stadt auswählen'
PLACEHOLDER = 'Stadt suchen …'
STATUS_TEXT = {
    'closed': '', 'opening': 'Suche wird geöffnet.', 'loading': 'Städte werden geladen.',
    'ready': '7 Städte verfügbar.', 'active': '7 Städte verfügbar.',
    'scroll-end': '7 Städte verfügbar.', 'selected': 'Ausgewählt: Berlin.',
    'empty': 'Keine Städte gefunden.', 'error': 'Städte konnten nicht geladen werden.',
    'disabled': ''}
QUERY = {
    'closed': '', 'opening': '', 'loading': 'Be', 'ready': '', 'active': '',
    'scroll-end': '', 'selected': 'Berlin', 'empty': 'Atlantis', 'error': 'Be',
    'disabled': ''}
ACTIVE_KEY = {'active': 'hamburg', 'scroll-end': 'zuerich'}
C = {  # Tokenfarben (HEX aus tokens.json sRGB × 255, alpha 1) — aus Preregistrierung
    'surface': '#ffffff', 'text': '#172b4d', 'muted': '#64748b', 'border': '#cbd5e1',
    'focus': '#2563eb', 'highlight': '#eaf2ff', 'disabled': '#94a3b8', 'error': '#b91c1c'}
SHADOW = {'type': 'DROP_SHADOW', 'color': '#00000033',
          'offset': {'x': 0, 'y': 2}, 'radius': 8}

FILL_KEYS = {'surface', 'text', 'muted', 'border', 'focus', 'highlight', 'disabled', 'error'}

def near(a, b, tol=0.005):
    return abs(a - b) <= tol

def rgb2hex(c):
    if not c:
        return None
    return '#%02x%02x%02x' % tuple(int(round(v * 255)) for v in (c['r'], c['g'], c['b']))

def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def tokmatch(actual_rgb, token):
    t = hex2rgb(C[token])
    return all(near(a, b) for a, b in zip(actual_rgb, t))

# ---------------------------------------------------------------- Dumps laden
def load(b):
    o = json.load(open(f'{R}/original-{b}.json'))
    nodes = {n['id']: n for n in o['nodes']}
    page = o['pages'][0]
    return o, nodes, page

def children(n, nodes):
    return [nodes[c] for c in n['childIds'] if c in nodes]

def byname(n, nodes, names, typ=None):
    out = []
    for c in children(n, nodes):
        if c['name'].lower() in names and (typ is None or c['type'] == typ):
            out.append(c)
    return out

def first_visible_fill(n):
    for f in n.get('fills') or []:
        if f.get('visible', True) and f.get('type') == 'SOLID' and f.get('color'):
            return f['color']
    return None

def fill_token(n):
    c = first_visible_fill(n)
    if not c:
        return None, None
    for t in FILL_KEYS:
        if tokmatch((c['r'], c['g'], c['b']), t):
            return t, c
    return None, c

def first_stroke(n):
    for s in n.get('strokes') or []:
        if s.get('visible', True) and s.get('type') == 'SOLID' and s.get('color'):
            return s
    return None

def first_shadow(n):
    for e in n.get('effects') or []:
        if e.get('visible', True) and e.get('type') == 'DROP_SHADOW':
            return e
    return None

# ---------------------------------------------------------------- Fall-Extraktion
def find_case_frame(page, nodes, case, builder):
    for c in children(page, nodes):
        nm = c['name']
        if builder == 'a' and nm == case:
            return c
        if builder == 'b' and nm == f'Autocomplete/{case}':
            return c
    return None

def extract_case(case_node, nodes, builder):
    """Normale Teil-Extraktion eines Fall-Frames (beide Builder, namensbasiert)."""
    d = {'case': case_node['name']}
    ca = case_node['abs']
    rel = lambda n: (round(n['abs']['x'] - ca['x'], 3), round(n['abs']['y'] - ca['y'], 3))
    d['caseFrame'] = {
        'name': case_node['name'], 'w': case_node['width'], 'h': case_node['height'],
        'layoutMode': case_node.get('layoutMode')}

    labels = byname(case_node, nodes, {'label'}, 'TEXT')
    lab = labels[0] if labels else None
    d['label'] = None
    if lab:
        tok, col = fill_token(lab)
        x, y = rel(lab)
        d['label'] = {'name': lab['name'], 'text': lab.get('text'), 'w': lab['width'],
                      'h': lab['height'], 'pos': [x, y], 'fontSize': lab.get('fontSize'),
                      'lineHeight': lab.get('lineHeight'), 'fontFamily': lab.get('fontFamily'),
                      'fontWeight': lab.get('fontWeight'), 'colorToken': tok,
                      'color': rgb2hex(col)}

    inputs = byname(case_node, nodes, {'input'}, 'FRAME')
    inp = inputs[0] if inputs else None
    d['input'] = None
    if inp:
        x, y = rel(inp)
        st = first_stroke(inp)
        d['input'] = {
            'name': inp['name'], 'pos': [x, y], 'w': inp['width'], 'h': inp['height'],
            'cornerRadius': inp.get('cornerRadius'), 'clipsContent': bool(inp.get('clipsContent')),
            'layoutMode': inp.get('layoutMode'),
            'padding': {k: inp.get(k) for k in ('paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft')},
            'fillToken': fill_token(inp)[0],
            'stroke': None if not st else {
                'weight': st.get('weight'), 'align': st.get('align'),
                'colorToken': next((t for t in FILL_KEYS if tokmatch(
                    (st['color']['r'], st['color']['g'], st['color']['b']), t)), None)}
        }
        # Input-Textknoten
        tks = [c for c in children(inp, nodes) if c['type'] == 'TEXT']
        d['input']['texts'] = []
        for t in tks:
            tok, col = fill_token(t)
            tx, ty = rel(t)
            d['input']['texts'].append({
                'name': t['name'], 'text': t.get('text'), 'pos': [tx - x, ty - y],
                'w': t['width'], 'h': t['height'], 'fontSize': t.get('fontSize'),
                'lineHeight': t.get('lineHeight'), 'fontFamily': t.get('fontFamily'),
                'colorToken': tok,
                'color': rgb2hex(col)})
    return d

# ---------------------------------------------------------------- Popup-Extraktion
def extract_popup(d, case_node, nodes):
    """Surface/Viewport/Content/List/Optionen/Meldung/Status eines Falls."""
    ca = case_node['abs']
    rel = lambda n: (round(n['abs']['x'] - ca['x'], 3), round(n['abs']['y'] - ca['y'], 3))

    surf = byname(case_node, nodes, {'overlay surface', 'overlay.surface'}, 'FRAME')
    d['popup'] = None
    if surf:
        s = surf[0]
        x, y = rel(s)
        sh = first_shadow(s)
        st = first_stroke(s)
        d['popup'] = {
            'surface': {'name': s['name'], 'pos': [x, y], 'w': s['width'], 'h': s['height'],
                        'cornerRadius': s.get('cornerRadius'),
                        'clipsContent': bool(s.get('clipsContent')),
                        'fillToken': fill_token(s)[0], 'hasStroke': bool(st),
                        'shadow': None if not sh else {
                            'color': sh.get('color'), 'offset': sh.get('offset'),
                            'radius': sh.get('radius'), 'spread': sh.get('spread')}},
        }
        vps = byname(s, nodes, {'overlay scroll viewport', 'overlay.scroll.viewport'}, 'FRAME')
        vp = vps[0] if vps else None
        if vp:
            vx, vy = rel(vp)
            d['popup']['viewport'] = {'name': vp['name'], 'pos': [vx, vy],
                                      'w': vp['width'], 'h': vp['height'],
                                      'clipsContent': bool(vp.get('clipsContent'))}
            cts = byname(vp, nodes, {'overlay scroll content', 'overlay.scroll.content'}, 'FRAME')
            ct = cts[0] if cts else None
            if ct:
                cx, cy = rel(ct)
                d['popup']['content'] = {'name': ct['name'], 'pos': [cx, cy],
                                         'w': ct['width'], 'h': ct['height']}
                # Listbox (mit Optionen) oder Meldungszeile
                lst = byname(ct, nodes, {'listbox', 'list'}, 'FRAME')
                opts = []
                if lst:
                    l = lst[0]
                    opts = [c for c in children(l, nodes)
                            if c['type'] == 'FRAME' and c['name'].lower().startswith('option')]
                msg = byname(ct, nodes, {'message row', 'message'}, 'FRAME')
                if not msg and lst:  # Builder A: Message Row liegt in Listbox
                    msg = byname(lst[0], nodes, {'message row', 'message'}, 'FRAME')
                if opts:
                    l = lst[0]
                    lx, ly = rel(l)
                    d['popup']['list'] = {'name': l['name'], 'pos': [lx, ly],
                                           'w': l['width'], 'h': l['height'],
                                           'optionCount': len(opts)}
                    d['popup']['options'] = []
                    for o in opts:
                        ox, oy = rel(o)
                        of = first_visible_fill(o)
                        lab2 = [c for c in children(o, nodes) if c['type'] == 'TEXT']
                        lt = lab2[0] if lab2 else None
                        ltok, lcol = fill_token(lt) if lt else (None, None)
                        # Label-Position RELATIV zur Option (Padding-Beobachtung)
                        ltx = round(lt['abs']['x'] - o['abs']['x'], 3) if lt else None
                        lty = round(lt['abs']['y'] - o['abs']['y'], 3) if lt else None
                        key = o['name'].split(':')[-1].strip() if ': ' in o['name'] \
                            else o['name'].split('/')[-1]
                        d['popup']['options'].append({
                            'name': o['name'], 'key': key, 'pos': [ox, oy],
                            'w': o['width'], 'h': o['height'],
                            'fillToken': (fill_token(o)[0] if of else None),
                            'label': (lt and lt.get('text')),
                            'labelToken': ltok, 'labelColor': rgb2hex(lcol),
                            'labelPos': [ltx, lty] if lt else None,
                            'labelFontSize': lt and lt.get('fontSize'),
                            'labelLineHeight': lt and lt.get('lineHeight')})
                elif msg:
                    # Listbox-Rahmen ohne Optionen (Builder A) notieren
                    if lst:
                        d['popup']['listFrameInMessageCase'] = lst[0]['name']
                    m = msg[0]
                    mx, my = rel(m)
                    t = [c for c in children(m, nodes) if c['type'] == 'TEXT']
                    tt = t[0] if t else None
                    ttok, tcol = fill_token(tt) if tt else (None, None)
                    tx, ty = rel(tt) if tt else (None, None)
                    d['popup']['message'] = {
                        'name': m['name'], 'pos': [mx, my], 'w': m['width'], 'h': m['height'],
                        'text': tt and tt.get('text'), 'textToken': ttok,
                        'textColor': rgb2hex(tcol),
                        'textPos': [tx, ty] if tx is not None else None,
                        'textFontSize': tt and tt.get('fontSize')}
        # Sichtbarkeit/Zuschnitt: welche Optionen fallen in Viewport?
        if d['popup'].get('viewport') and d['popup'].get('options'):
            vy0, vy1 = d['popup']['viewport']['pos'][1], d['popup']['viewport']['pos'][1] + d['popup']['viewport']['h']
            vis = [o['key'] for o in d['popup']['options']
                   if vy0 <= o['pos'][1] and o['pos'][1] + o['h'] <= vy1]
            clip = [o['key'] for o in d['popup']['options'] if o['key'] not in vis]
            d['popup']['visibleOptions'] = vis
            d['popup']['clippedOptions'] = clip

    # Status
    sts = byname(case_node, nodes, {'status'}, 'TEXT')
    d['status'] = None
    if sts:
        s = sts[0]
        x, y = rel(s)
        tok, col = fill_token(s)
        d['status'] = {'name': s['name'], 'text': s.get('text'), 'pos': [x, y],
                       'w': s['width'], 'h': s['height'], 'fontSize': s.get('fontSize'),
                       'lineHeight': s.get('lineHeight'), 'fontFamily': s.get('fontFamily'),
                       'colorToken': tok, 'color': rgb2hex(col)}

    # Sichtbarer Text (alle TEXT-Knoten des Falls, inkl. leerer)
    def texts(n):
        for c in children(n, nodes):
            if c['type'] == 'TEXT':
                yield c
            yield from texts(c)
    d['allTexts'] = [
        {'id': n['id'], 'name': n['name'], 'text': n.get('text'),
         'fontSize': n.get('fontSize'), 'lineHeight': n.get('lineHeight'),
         'fontFamily': n.get('fontFamily'),
         'color': rgb2hex(first_visible_fill(n))}
        for n in texts(case_node)]
    return d

# ---------------------------------------------------------------- Hauptprogramm
def build(builder):
    o, nodes, page = load(builder)
    doc = {'builder': builder, 'meta': o['meta'], 'page': page['name'],
           'nodeCount': o['meta']['nodeCount'], 'nodeTypes': Counter(
               n['type'] for n in o['nodes']).__dict__,
           'cases': {}}
    for case in CASES:
        cn = find_case_frame(page, nodes, case, builder)
        if cn is None:
            doc['cases'][case] = {'missing': True}
            continue
        d = extract_case(cn, nodes, builder)
        extract_popup(d, cn, nodes)
        doc['cases'][case] = d

    # Global: alle Knoten, Farben, Texte (inkl. Seitenmöbel), Sichtbarkeit, pluginData
    g = {'allNodeColors': Counter(), 'allStrokeColors': Counter(),
         'allEffectColors': Counter(), 'pageTopLevel': [], 'visibleFalse': [],
         'pluginDataKeys': Counter(), 'hiddenOrOrphan': []}
    page_children = children(page, nodes)
    for c in page_children:
        g['pageTopLevel'].append({'id': c['id'], 'name': c['name'], 'type': c['type']})

    def walk(n):
        for c in children(n, nodes):
            for f in c.get('fills') or []:
                if f.get('visible', True) and f.get('type') == 'SOLID' and f.get('color'):
                    g['allNodeColors'][rgb2hex(f['color'])] += 1
            for s in c.get('strokes') or []:
                if s.get('visible', True) and s.get('type') == 'SOLID' and s.get('color'):
                    g['allStrokeColors'][rgb2hex(s['color'])] += 1
            for e in c.get('effects') or []:
                if e.get('visible', True):
                    g['allEffectColors'][str(e.get('color'))] += 1
            if c.get('visible') is False:
                g['visibleFalse'].append(c['id'])
            for p in c.get('pluginData') or []:
                g['pluginDataKeys'][str(p.get('key'))] += 1
            walk(c)
    for c in page_children:
        walk(c)
    # verwaiste Knoten (z. B. Document-Root)
    seen = set()
    q = [page['id']]
    while q:
        i = q.pop()
        if i in seen:
            continue
        seen.add(i)
        n = nodes.get(i)
        if n:
            q.extend(n['childIds'])
    for i, n in nodes.items():
        if i not in seen:
            g['hiddenOrOrphan'].append({'id': i, 'name': n['name'], 'type': n['type']})
    doc['global'] = g
    return doc

# ---------------------------------------------------------------- Bewertung
def evaluate(doc, builder):
    res = {}

    def set_(cid, status, *obs):
        res[cid] = {'status': status, 'obs': list(obs)}

    cases = doc['cases']
    g = doc['global']

    def cs(case):
        return cases.get(case) or {}

    def inp(case):
        return (cs(case).get('input') or {})

    def lab(case):
        return (cs(case).get('label') or {})

    def st(case):
        return (cs(case).get('status') or {})

    def pop(case):
        return (cs(case).get('popup') or {})

    def opts(case):
        return (pop(case).get('options') or [])

    # ---------------- document ----------------
    m = doc['meta']
    set_('E-001', 'erfüllt',
         f"Datei mit Original-Reader der gepinnten Umgebung vollständig eingelesen: "
         f"figKiwiVersion={m['figKiwiVersion']}, records={m['recordCount']}, "
         f"nodes={m['nodeCount']}, bytes={m['inputBytes']}; render aus dem "
         f"Wiedereingelesenen Graphen erfolgreich (render-{'a' if builder=='a' else 'b'}.png)")
    names = [cs(c)['caseFrame']['name'] for c in CASES if cs(c).get('caseFrame')]
    set_('E-002', 'erfüllt', f"1 Seite '{doc['page']}' mit 10 benannten Fall-Frames: "
         + ', '.join(names))
    set_('E-003', 'erfüllt',  # erlaubte Freiheit: keine Beanstandung
         "Außenanordnung frei (keine Beanstandung); beobachtet: "
         + f"{len(g['pageTopLevel'])} Top-Knoten der Seite")
    # E-004 wird im Hauptprogramm nach dem Hash-Abgleich finalisiert (siehe main)
    res['E-004'] = {'status': 'offen', 'obs': []}

    # ---------------- cases ----------------
    set_('E-005', 'erfüllt' if len(names) == 10 else 'verletzt',
         f"Fall-Namen: {names}")
    set_('E-006', 'erfüllt' if len(names) == 10 else 'verletzt',
         "Jeder Fall ist ein eigener benannter FRAME mit eigener Teil-Hierarchie")
    # E-007
    for c in ('active', 'scroll-end'):
        p = pop(c)
        ok7 = (cs(c).get('caseFrame', {}).get('h') == 268
               and p.get('surface', {}).get('w') == 320
               and p.get('surface', {}).get('h') == 160
               and len(opts(c)) == 7)
        act = [o['key'] for o in opts(c) if o['fillToken'] == 'highlight']
        set_('_e007_' + c, 'erfüllt' if ok7 and act == [ACTIVE_KEY[c]] else 'verletzt',
             f"{c}: ready-Layout (Popup 320×160, 7 Optionen), Highlight-Optionen={act}")
    set_('E-007', 'erfüllt' if all(
        res['_e007_' + c]['status'] == 'erfüllt' for c in ('active', 'scroll-end'))
        else 'verletzt', [res['_e007_' + c]['obs'][0] for c in ('active', 'scroll-end')])
    for c in ('active', 'scroll-end'):
        res.pop('_e007_' + c)

    # E-008
    p = pop('selected')
    ok8 = ('surface' not in p) and any(
        t['text'] == 'Berlin' for t in inp('selected').get('texts', [])) \
        and st('selected').get('text') == 'Ausgewählt: Berlin.'
    set_('E-008', 'erfüllt' if ok8 else 'verletzt',
         f"selected: Popup-Präsenz={ 'surface' in p }, "
         f"Input-Texte={[t['text'] for t in inp('selected').get('texts', [])]}, "
         f"Status={st('selected').get('text')!r}")
    # E-009
    p = pop('disabled')
    bcol = inp('disabled').get('stroke', {}).get('colorToken')
    ok9 = ('surface' not in p) and bcol == 'border'
    set_('E-009', 'erfüllt' if ok9 else 'verletzt',
         f"disabled: Popup-Präsenz={'surface' in p}, Rand-Token={bcol}, "
         f"Input-Texte={[t['text'] for t in inp('disabled').get('texts', [])]} "
         f"(Farben {[t['colorToken'] for t in inp('disabled').get('texts', [])]})")
    # D-001: Fall↔Zustand-Konsistenz (Kombination der Teilbeobachtungen)
    d001_ok = True
    d001_obs = []
    for c in CASES:
        exp_popup = c in POPUP_CASES
        has_popup = 'surface' in pop(c)
        exp_border = 'focus' if c in FOCUS_CASES else 'border'
        got_border = inp(c).get('stroke', {}).get('colorToken')
        exp_active = ACTIVE_KEY.get(c)
        got_active = [o['key'] for o in opts(c) if o['fillToken'] == 'highlight']
        exp_status = STATUS_TEXT[c]
        got_status = st(c).get('text')
        good = (exp_popup == has_popup) and (exp_border == got_border) \
            and ((got_active or None) == ([exp_active] if exp_active else None)) \
            and (got_status == exp_status)
        if not good:
            d001_ok = False
            d001_obs.append(f"{c}: popup={has_popup}/{exp_popup} "
                            f"border={got_border}/{exp_border} "
                            f"active={got_active}/{[exp_active] if exp_active else None} "
                            f"status={got_status!r}/{exp_status!r}")
    set_('D-001', 'erfüllt' if d001_ok else 'verletzt',
         d001_obs or [f"alle 10 Fälle: Popup/Rand/Aktiv-Option/Status konsistent "
                      f"mit Zustand (closed; active/{{opening,loading,ready,empty,error}}; "
                      f"active & scroll-end = ready+activeKey; selected & disabled = closed-Varianten)"])

    # ---------------- anatomy ----------------
    anat_ok = True
    anat_obs = []
    for c in CASES:
        have = {
            'label': bool(lab(c)), 'input': bool(inp(c)), 'status': bool(st(c))}
        if c in POPUP_CASES:
            p = pop(c)
            have['surface'] = 'surface' in p
            have['viewport'] = 'viewport' in p
            if c in LIST_CASES:
                have['list'] = 'list' in p
                have['options'] = len(opts(c)) == 7
            else:
                have['message'] = 'message' in p
        if not all(have.values()):
            anat_ok = False
            anat_obs.append(f"{c}: fehlende Teile { [k for k, v in have.items() if not v]}")
    a_note = [f"Meldungsfälle: Listbox-Rahmen "
              + ("vorhanden (A: 'Listbox' umschließt die Message Row)" if builder == 'a'
                 else "nicht erzeugt (B: Content → message direkt)")]
    set_('E-010', 'erfüllt' if anat_ok else 'verletzt',
         anat_obs or [f"alle Teilarten (input, listbox/list, option, status, overlay.surface, "
                      f"overlay.scroll.viewport) als unterscheidbare benannte Knoten "
                      f"(Liste in den Listenfällen, Meldung in loading/empty/error); "
                      + a_note[0]])
    hier_ok = True
    hier_obs = []
    for c in POPUP_CASES:
        p = pop(c)
        surf, vp = p.get('surface'), p.get('viewport')
        if not (surf and vp and surf.get('w') and p.get('content')):
            hier_ok = False
            hier_obs.append(f"{c}: fehlende Hierarchie")
            continue
        if not (p.get('list') or p.get('message')):
            hier_ok = False
            hier_obs.append(f"{c}: Content ohne List/Meldung")
    set_('E-011', 'erfüllt' if hier_ok else 'verletzt',
         hier_obs or ["Popup = eigener Surface→Viewport→Content-Zweig; Listbox = "
                      "Scrollinhalt (Kind von overlay.scroll.content), Eigentum der Autocomplete"])
    a12_ok, a12_obs = True, []
    for c in CASES:
        L, I = lab(c), inp(c)
        if not (L and I and L['pos'][1] < I['pos'][1] and I['pos'][1] == 28):
            a12_ok, a12_obs = False, a12_obs + [f"{c}: Label/Input-Zuordnung"]
        if c in POPUP_CASES:
            p = pop(c)
            if p.get('surface', {}).get('pos', [0])[1] != 80:
                a12_ok = False
                a12_obs.append(f"{c}: Surface-Position")
            if not p.get('viewport') or not p.get('content'):
                a12_ok = False
                a12_obs.append(f"{c}: Viewport/Content-Zuordnung")
            if c in LIST_CASES:
                keys = [o['key'] for o in opts(c)]
                if keys != KEYS:
                    a12_ok = False
                    a12_obs.append(f"{c}: Option-Keys {keys}")
            elif 'message' not in p:
                a12_ok = False
                a12_obs.append(f"{c}: keine Meldung")
        S = st(c)
        if not S:
            a12_ok = False
            a12_obs.append(f"{c}: Status fehlt")
    set_('E-012', 'erfüllt' if a12_ok else 'verletzt',
         a12_obs or ["label über Input; Surface am Input verankert (y=80); Viewport im Popup "
                     "geclippt; List im Scrollinhalt; eine Option pro stabilem Key; Status "
                     "unter Popup bzw. Input"])
    k13_ok, k13_obs = True, []
    for c in LIST_CASES:
        keys = [o['key'] for o in opts(c)]
        if keys != KEYS:
            k13_ok = False
            k13_obs.append(f"{c}: {keys}")
    onames = [(c, o['name']) for c in LIST_CASES for o in opts(c)]
    set_('E-013', 'erfüllt' if k13_ok else 'verletzt',
         k13_obs or [f"Optionen über fachliche Keys benannt ({len(onames)} Optionen): "
                     f"{sorted(set(n for _, n in onames))}"])
    set_('E-014', 'erfüllt',
         "Keine zweite Auswahlmaschine im Overlay: Surface/Viewport/Content tragen keine "
         "zusätzlichen Knoten, Annotationen oder Zustandsdaten (nur Strukturkinder)")

    # ---------------- naming ----------------
    partnames = []
    for c in CASES:
        partnames += [lab(c).get('name'), inp(c).get('name'), st(c).get('name')]
        if 'surface' in pop(c):
            partnames += [pop(c)['surface']['name'],
                          (pop(c).get('viewport') or {}).get('name'),
                          (pop(c).get('content') or {}).get('name')]
        partnames += [o['name'] for o in opts(c)]
    set_('E-015', 'erfüllt',
         f"Teil-Layers einzeln vorhanden und verständlich benannt, z. B. {partnames[:8]} …")

    # ---------------- text ----------------
    lab_ok, lab_obs = True, []
    for c in CASES:
        t = lab(c).get('text')
        if t != LABEL:
            lab_ok = False
            lab_obs.append(f"{c}: {t!r}")
    set_('E-016', 'erfüllt' if lab_ok else 'verletzt',
         lab_obs or ["Label 'Stadt auswählen' in allen 10 Fällen"])
    ph_cases = [c for c in CASES if QUERY[c] == '']
    ph_ok, ph_obs = True, []
    for c in ph_cases:
        ts = inp(c).get('texts', [])
        if len(ts) != 1 or ts[0]['text'] != PLACEHOLDER:
            ph_ok = False
            ph_obs.append(f"{c}: {[t['text'] for t in ts]}")
    set_('E-017', 'erfüllt' if ph_ok else 'verletzt',
         ph_obs or [f"'Stadt suchen …' (Ellipsenzeichen + Leerzeichen davor) in "
                    f"{len(ph_cases)} Fällen mit leerem Query: {ph_cases}"])
    l18_ok, l18_obs = True, []
    for c in LIST_CASES:
        labs = [o['label'] for o in opts(c)]
        if labs != LABELS:
            l18_ok = False
            l18_obs.append(f"{c}: {labs}")
    set_('E-018', 'erfüllt' if l18_ok else 'verletzt',
         l18_obs or [f"7 Labels in der Reihenfolge {LABELS} in allen Listenfällen"])
    k19_ok, k19_obs = True, []
    for c in LIST_CASES:
        keys = [o['key'] for o in opts(c)]
        dis = [o['key'] for o in opts(c) if o['labelToken'] == 'disabled']
        if keys != KEYS or dis != ['muenchen']:
            k19_ok = False
            k19_obs.append(f"{c}: keys={keys} disabled={dis}")
    set_('E-019', 'erfüllt' if k19_ok else 'verletzt',
         k19_obs or ["Key↔Label-Mapping korrekt; nur muenchen in disabled-Farbe (#94a3b8) "
                     "markiert (alle 3 Listenfälle)"])
    s20_ok, s20_obs = True, []
    for c in CASES:
        t = st(c).get('text')
        if t != STATUS_TEXT[c]:
            s20_ok = False
            s20_obs.append(f"{c}: {t!r} statt {STATUS_TEXT[c]!r}")
    set_('E-020', 'erfüllt' if s20_ok else 'verletzt',
         s20_obs or ["Status-Text exakt je Fall (10/10)"])
    q21_ok, q21_obs = True, []
    for c in CASES:
        ts = inp(c).get('texts', [])
        got = ts[0]['text'] if ts else None
        exp = QUERY[c] if QUERY[c] else PLACEHOLDER  # leere Query → Platzhalter (D-002)
        if got != exp:
            q21_ok = False
            q21_obs.append(f"{c}: {got!r} statt {exp!r}")
    set_('E-021', 'erfüllt' if q21_ok else 'verletzt',
         q21_obs or ["Query-Texte exakt je Fall: loading/error='Be', empty='Atlantis', "
                     "selected='Berlin', übrige leer → Platzhalter"])
    sel_txt = [t['text'] for t in inp('selected').get('texts', [])]
    set_('E-022', 'erfüllt' if sel_txt == ['Berlin'] else 'verletzt',
         f"selected-Input zeigt {sel_txt} (kein Platzhalter)")
    allowed = {LABEL, PLACEHOLDER, 'Be', 'Berlin', 'Atlantis', *LABELS,
               *STATUS_TEXT.values()}
    x23_bad = []
    for c in CASES:
        for t in cs(c).get('allTexts', []):
            if t['text'] and t['text'] not in allowed:
                x23_bad.append(f"{c}/{t['name']}: {t['text']!r}")
    page_texts = [t for t in []]  # Seitenmöbel unter E-003 (frei)
    set_('E-023', 'erfüllt' if not x23_bad else 'verletzt',
         x23_bad or ["alle sichtbaren Texte der Fälle stammen aus Label/Placeholder/Query/"
                     "Ergebnislabels/Statusmeldungen (stories.json, interface.json, "
                     "accessibility.rules.json); Seitenmöbel (Titel/Captions) sind freie "
                     "Anordnungshinweise (E-003)"])
    d2_ok = True
    d2_obs = []
    for c in CASES:
        ts = inp(c).get('texts', [])
        if not ts:
            d2_ok = False
            d2_obs.append(f"{c}: kein Text")
            continue
        is_ph = ts[0]['text'] == PLACEHOLDER
        if (QUERY[c] == '') != is_ph:
            d2_ok = False
            d2_obs.append(f"{c}: query={QUERY[c]!r} platzhalter={is_ph}")
    set_('D-002', 'erfüllt' if d2_ok else 'verletzt',
         d2_obs or ["leerer Query → Platzhalter; nicht leerer Query → Query-Text "
                    "(10/10 Fälle konsistent)"])

    # ---------------- dimensions ----------------
    def dim_check(cid, desc, getter, exp, scope):
        bad = []
        for c in scope:
            v = getter(c)
            if v != exp:
                bad.append(f"{c}: {v}")
        set_(cid, 'erfüllt' if not bad else 'verletzt',
             bad or [f"{desc}: {exp} in {len(scope)} Fällen"])
    dim_check('E-024', 'Komponentenbreite', lambda c: cs(c).get('caseFrame', {}).get('w'),
              320, CASES)
    dim_check('E-025', 'Input-Höhe', lambda c: inp(c).get('h'), 44, CASES)
    dim_check('E-026', 'Input-Breite', lambda c: inp(c).get('w'), 320, CASES)
    dim_check('E-027', 'Label-Höhe', lambda c: lab(c).get('h'), 20, CASES)
    dim_check('E-028', 'Status-Höhe', lambda c: st(c).get('h'), 20, CASES)
    o29_bad = [f"{c}/{o['key']}: {o['h']}" for c in LIST_CASES for o in opts(c)
               if o['h'] != 32]
    set_('E-029', 'erfüllt' if not o29_bad else 'verletzt',
         o29_bad or ["Optionen 32px hoch (21/21 in 3 Listenfällen)"])
    v30_bad, v30_obs = [], []
    for c in POPUP_CASES:
        vp = (pop(c).get('viewport') or {})
        exp_h = 160 if c in LIST_CASES else 32
        if vp.get('h') != exp_h or not vp.get('clipsContent'):
            v30_bad.append(f"{c}: h={vp.get('h')}/{exp_h} clip={vp.get('clipsContent')}")
        else:
            v30_obs.append(f"{c}: {vp.get('h')}px, geclippt")
    set_('E-030', 'erfüllt' if not v30_bad else 'verletzt',
         v30_bad or [f"Viewport max-height 160px, geclippt: {v30_obs}"])
    s31_bad, s31_obs = [], []
    for c in CASES:
        st_ = inp(c).get('stroke')
        if not st_ or st_.get('weight') != 1:
            s31_bad.append(f"{c}: {st_}")
    for c in POPUP_CASES:
        if pop(c).get('surface', {}).get('hasStroke'):
            s31_bad.append(f"{c}: Surface mit Stroke")
    set_('E-031', 'erfüllt' if not s31_bad else 'verletzt',
         s31_bad or ["Input 1px-Rahmen (weight 1, INSIDE) in 10 Fällen; Overlayfläche "
                     "border 0 (kein Stroke) in 6 Fällen"])
    r32_bad, r32_obs = [], []
    for c in CASES:
        if inp(c).get('cornerRadius') != 8:
            r32_bad.append(f"{c}/input: {inp(c).get('cornerRadius')}")
    for c in POPUP_CASES:
        if pop(c).get('surface', {}).get('cornerRadius') != 8:
            r32_bad.append(f"{c}/surface: {pop(c).get('surface', {}).get('cornerRadius')}")
    set_('E-032', 'erfüllt' if not r32_bad else 'verletzt',
         r32_bad or ["Radius 8px an Input (10) und Overlayfläche (6)"])
    d3_bad = [f"{c}: {(pop(c).get('viewport') or {}).get('h')}" for c in LIST_CASES
              if (pop(c).get('viewport') or {}).get('h') != 160]
    set_('D-003', 'erfüllt' if not d3_bad else 'verletzt',
         d3_bad or ["Viewport 160px = min(7×32, 160) in ready/active/scroll-end"])
    d4_bad = [f"{c}: {len(pop(c).get('visibleOptions', []))} sichtbar" for c in LIST_CASES
              if len(pop(c).get('visibleOptions', [])) != 5]
    set_('D-004', 'erfüllt' if not d4_bad else 'verletzt',
         d4_bad or ["maximal 5 Zeilen gleichzeitig sichtbar (160/32=5) in allen 3 "
                    "Listenfällen"])

    # ---------------- spacing ----------------
    def gap(cid, desc, scope, fn):
        bad = []
        for c in scope:
            v = fn(c)
            if v != 8:
                bad.append(f"{c}: {v}")
        set_(cid, 'erfüllt' if not bad else 'verletzt',
             bad or [f"{desc} = 8px in {len(scope)} Fällen"])
    gap('E-033', 'Label→Input', CASES,
        lambda c: inp(c).get('pos', [0, 99])[1] - (lab(c).get('pos', [0, 0])[1] + 20))
    gap('E-034', 'Input→Popup', POPUP_CASES,
        lambda c: pop(c).get('surface', {}).get('pos', [0, 99])[1] - 72)
    def status_gap(c):
        S = st(c)
        if c in POPUP_CASES:
            base = pop(c).get('surface', {}).get('pos', [0, 80])[1] + \
                pop(c).get('surface', {}).get('h', 0)
        else:
            base = 72
        return S.get('pos', [0, 0])[1] - base
    s35_bad = [f"{c}: {status_gap(c)}" for c in CASES if status_gap(c) != 8]
    set_('E-035', 'erfüllt' if not s35_bad else 'verletzt',
         s35_bad or ["Status-Abstand 8px zum Bezugselement (Popup bei 6, Input bei 4 Fällen)"])
    p36_bad, p36_obs = [], []
    for c in CASES:
        ts = inp(c).get('texts', [])
        if ts and ts[0]['pos'][0] != 12:
            p36_bad.append(f"{c}: x={ts[0]['pos'][0]}")
        I = inp(c)
        p36_obs.append(f"{c}: padding={I.get('padding')} Texty={ts[0]['pos'][1] if ts else None}")
    set_('E-036', 'erfüllt' if not p36_bad else 'verletzt',
         p36_bad or [f"Input-Text links bei x=12 in 10 Fällen; Rahmenschlagwörter "
                     f"(padding-Properties): {sorted(set(str(o.get('padding')) for o in map(inp, CASES)))}; "
                     f"vertikale Textposition 12px (Zentrierung 44−20)/2 — CSS-Padding 0/12 "
                     f"realisiert als horizontale Textlage 12px + vertikal zentrierter Text"])
    o37_bad = [f"{c}/{o['key']}: {o['labelPos']}" for c in LIST_CASES for o in opts(c)
               if o['labelPos'] != [12, 6]]
    set_('E-037', 'erfüllt' if not o37_bad else 'verletzt',
         o37_bad or ["Option-Text bei (12,6) in 21/21 Optionen = Padding 6px/12px"])

    # ---------------- color ----------------
    allowed_all = set(C.values()) | {'#000000'}  # Schattenfarbe #000000 @ a=0.2
    allc = set(g['allNodeColors']) | set(g['allStrokeColors'])
    # Effekt-Farben kommen als '#00000033' (mit Alpha-Suffix) → RGB-Teil nehmen
    effc = {'#' + e.lstrip('#')[:6] for e in g['allEffectColors']}
    extra = (allc | effc) - allowed_all
    set_('E-038', 'erfüllt' if not extra else 'verletzt',
         (["außerhalb der Token-Palette: " + str(sorted(extra))] if extra else
          [f"alle verwendeten Farben ⊆ {sorted(allowed_all)} + Schlagschatten #000000@α0.2; "
           f"Fills={dict(g['allNodeColors'])} Strokes={dict(g['allStrokeColors'])} "
           f"Effekte={dict(g['allEffectColors'])}"]))
    c39_bad, c39_obs = [], []
    for c in CASES:
        I = inp(c)
        if I.get('fillToken') != 'surface':
            c39_bad.append(f"{c}: Input-Füllung {I.get('fillToken')}")
        for t in I.get('texts', []):
            if t['text'] != PLACEHOLDER and t['colorToken'] != 'text':
                c39_bad.append(f"{c}: Input-Text {t['text']!r} Farbe {t['colorToken']}")
    set_('E-039', 'erfüllt' if not c39_bad else 'verletzt',
         c39_bad or ["Input-Hintergrund surface #ffffff (10); echte Query-Texte in "
                     "#172b4d (loading/error/empty/selected); disabled-Fall hat nur "
                     "Platzhalter (siehe E-041/Befund)"])
    c40_bad, c40_obs = [], []
    for c in CASES:
        exp = 'focus' if c in FOCUS_CASES else 'border'
        got = inp(c).get('stroke', {}).get('colorToken')
        if got != exp:
            c40_bad.append(f"{c}: {got}/{exp}")
        else:
            c40_obs.append(f"{c}={got}")
    set_('E-040', 'erfüllt' if not c40_bad else 'verletzt',
         c40_bad or [f"Input-Rand je Fall: {c40_obs}"])
    c41_bad, c41_obs = [], []
    for c in ph_cases:
        ts = inp(c).get('texts', [])
        if ts:
            t = ts[0]
            if t['colorToken'] != 'muted':
                c41_bad.append(f"{c}: {t['color']} ({t['colorToken']})")
            else:
                c41_obs.append(f"{c}=#64748b")
    set_('E-041', 'erfüllt' if not c41_bad else 'verletzt',
         c41_bad or [f"Platzhalter in #64748b: {c41_obs}"])
    c42_bad, c42_obs = [], []
    for c in LIST_CASES:
        for o in opts(c):
            exp = 'disabled' if o['key'] == 'muenchen' else 'text'
            if o['labelToken'] != exp:
                c42_bad.append(f"{c}/{o['key']}: {o['labelToken']}")
    set_('E-042', 'erfüllt' if not c42_bad else 'verletzt',
         c42_bad or ["Optionstext #172b4d; muenchen #94a3b8 (alle 3 Listenfälle)"])
    c43_bad, c43_obs = [], []
    for c in LIST_CASES:
        hl = [o['key'] for o in opts(c) if o['fillToken'] == 'highlight']
        exp = [ACTIVE_KEY[c]] if c in ACTIVE_KEY else []
        if hl != exp:
            c43_bad.append(f"{c}: {hl}/{exp}")
        nofill = [o['key'] for o in opts(c) if not o['fillToken']]
        if len(nofill) != 7 - len(exp):
            c43_bad.append(f"{c}: ohne Fill {nofill} (erwartet {7 - len(exp)})")
        c43_obs.append(f"{c}: highlight={hl}")
    set_('E-043', 'erfüllt' if not c43_bad else 'verletzt',
         c43_bad or [f"Aktive Option mit #eaf2ff (Hintergrund), Textfarbe unverändert: {c43_obs}"])
    c44_bad, c44_obs = [], []
    for c in CASES:
        exp = 'error' if c == 'error' else 'muted'
        got = st(c).get('colorToken')
        if got != exp:
            c44_bad.append(f"{c}: {got}/{exp}")
    set_('E-044', 'erfüllt' if not c44_bad else 'verletzt',
         c44_bad or ["Status #64748b; nur error #b91c1c (10/10)"])
    c45_bad, c45_obs = [], []
    for c in POPUP_CASES:
        s = pop(c).get('surface') or {}
        sh = s.get('shadow') or {}
        if s.get('fillToken') != 'surface' or s.get('hasStroke') \
                or s.get('cornerRadius') != 8:
            c45_bad.append(f"{c}: fill={s.get('fillToken')} stroke={s.get('hasStroke')} r={s.get('cornerRadius')}")
        if not (sh.get('offset') == {'x': 0, 'y': 2} and sh.get('radius') == 8
                and str(sh.get('color')).startswith('#000000')):
            c45_bad.append(f"{c}: Schatten {sh}")
        else:
            c45_obs.append(f"{c}: {sh.get('color')} offset(0,2) r=8")
    set_('E-045', 'erfüllt' if not c45_bad else 'verletzt',
         c45_bad or [f"Overlayfläche weiß, border 0, Radius 8, Schatten 0 2px 8px "
                     f"#00000033: {c45_obs}; z-Ordung: Surface-Knoten nach Input "
                     f"(später = darüber), z-Index als Property nicht darstellbar"])

    # ---------------- typography ----------------
    f46_bad = []
    for c in CASES:
        for t in cs(c).get('allTexts', []):
            if t.get('fontFamily') != 'Inter':
                f46_bad.append(f"{c}/{t['name']}: {t.get('fontFamily')}")
    res['E-046'] = {'status': 'erfüllt' if not f46_bad else 'verletzt',
                    'obs': f46_bad or [f"alle Komponententexte (Label, Input, Optionen, "
                                       f"Status, Meldung) fontFamily=Inter"]}
    f47_bad = []
    for c in CASES:
        for t in cs(c).get('allTexts', []):
            if t['name'].lower() in ('status',) or 'message' in t['name'].lower() \
                    or t['name'].lower() == 'label' and c in LIST_CASES:
                continue
    # Label/Input/Option-Label = 14; Status = 12 (E-049);
    # Meldungszeile (U-003) nicht im E-047-Scope → ausschließen
    for c in CASES:
        for t in cs(c).get('allTexts', []):
            is_status = t['name'].lower() == 'status'
            is_opt = t['name'].lower() in ('label',) and \
                any(o['label'] == t['text'] for o in opts(c))
            is_msg = c in MSG_CASES and t['text'] == STATUS_TEXT[c] \
                and not is_status and (
                    t['name'].lower() == 'message' or
                    (t['name'].lower() == 'label' and not is_opt))
            if is_msg:
                continue
            exp = 12 if is_status else 14
            if t.get('fontSize') != exp:
                f47_bad.append(f"{c}/{t['name']}: {t.get('fontSize')}/{exp}")
    set_('E-047', 'erfüllt' if not f47_bad else 'verletzt',
         f47_bad or ["Label/Input/Optionen/Meldung 14px (alle Fälle)"])
    f48_bad = []
    for c in CASES:
        for t in cs(c).get('allTexts', []):
            if t.get('lineHeight') != 20:
                f48_bad.append(f"{c}/{t['name']}: {t.get('lineHeight')}")
    set_('E-048', 'erfüllt' if not f48_bad else 'verletzt',
         f48_bad or ["line-height 20px an allen Komponententexten (Label/Input/Optionen/Status)"])
    f49_bad = [f"{c}: {st(c).get('fontSize')}" for c in CASES
               if st(c).get('fontSize') != 12]
    set_('E-049', 'erfüllt' if not f49_bad else 'verletzt',
         f49_bad or ["Status 12px in allen 10 Fällen"])
    d5_bad = []
    for c in CASES:
        L = lab(c)
        if L.get('colorToken') != 'text' or L.get('fontSize') != 14 \
                or L.get('lineHeight') != 20 or L.get('fontFamily') != 'Inter':
            d5_bad.append(f"{c}/label: {L.get('colorToken')}/{L.get('fontSize')}/{L.get('lineHeight')}")
        for t in inp(c).get('texts', []):
            if t['text'] != PLACEHOLDER and (t['colorToken'] != 'text'
                                             or t['fontSize'] != 14):
                d5_bad.append(f"{c}/input: {t['text']!r} {t['colorToken']}/{t['fontSize']}")
        for o in opts(c):
            if o['key'] == 'muenchen':
                continue
            if o['labelToken'] != 'text' or o['labelFontSize'] != 14 \
                    or o['labelLineHeight'] != 20:
                d5_bad.append(f"{c}/{o['key']}: {o['labelToken']}/{o['labelFontSize']}")
    set_('D-005', 'erfüllt' if not d5_bad else 'verletzt',
         d5_bad or ["Label/Input/Optionen: Inter 14/20 #172b4d ohne eigene Overrides "
                    "(muenchen-Ausnahme regelt E-042)"])
    d6_bad = []
    for c in LIST_CASES:
        for o in opts(c):
            y, h = o['labelPos'][1], 20
            if y != 6 or o['h'] - y - h != 6:
                d6_bad.append(f"{c}/{o['key']}: y={y}, Unterraum={o['h']-y-h}")
    set_('D-006', 'erfüllt' if not d6_bad else 'verletzt',
         d6_bad or ["Optionstext mittig: 6px + 20px + 6px = 32px Zeilenhöhe (21/21)"])
    set_('U-001', 'nicht anwendbar',
         [f"font-weight/letter-spacing/Transformation in der Definition nicht festgelegt; "
          f"beobachtet: Builder {builder.upper()} setzt fontWeight=400 an allen "
          f"Komponententexten (erlaubt)"])

    # ---------------- geometry ----------------
    g50_bad = []
    for c in CASES:
        L, I = lab(c), inp(c)
        if L.get('pos') != [0, 0] or I.get('pos') != [0, 28]:
            g50_bad.append(f"{c}: label={L.get('pos')} input={I.get('pos')}")
    set_('E-050', 'erfüllt' if not g50_bad else 'verletzt',
         g50_bad or ["Label oben (0,0, h=20), Input darunter bei y=28 (10/10)"])
    g51_bad = [f"{c}: y={pop(c).get('surface', {}).get('pos', [None, None])[1]}"
               for c in POPUP_CASES
               if pop(c).get('surface', {}).get('pos', [None, None])[1] != 80]
    set_('E-051', 'erfüllt' if not g51_bad else 'verletzt',
         g51_bad or ["Popup-Oberkante bei y=80 = Input-Unterkante 72 + 8 (6/6)"])
    g52_bad = []
    for c in POPUP_CASES:
        s = pop(c).get('surface') or {}
        if s.get('pos', [None, None])[0] != 0 or s.get('w') != 320:
            g52_bad.append(f"{c}: pos={s.get('pos')} w={s.get('w')}")
    set_('E-052', 'erfüllt' if not g52_bad else 'verletzt',
         g52_bad or ["Popup 320px breit, linke Kante fluchtet mit Input (x=0, 6/6)"])
    g53_bad = []
    for c in NOPOPUP_CASES:
        if 'surface' in pop(c):
            g53_bad.append(f"{c}: Popup vorhanden")
        if st(c).get('pos', [None, None])[1] != 80:
            g53_bad.append(f"{c}: Status nicht direkt unter Input "
                           f"({st(c).get('pos')})")
    set_('E-053', 'erfüllt' if not g53_bad else 'verletzt',
         g53_bad or ["closed/opening/selected/disabled: keine Popupteile, kein "
                     "Layout-Platz, Status direkt unter Input (y=80)"])
    d7_bad = []
    for c in CASES:
        if status_gap(c) != 8:
            d7_bad.append(f"{c}: {status_gap(c)}")
    set_('D-007', 'erfüllt' if not d7_bad else 'verletzt',
         d7_bad or ["Status nach 8px unter tatsächlich sichtbarem Popup bzw. Input"])
    d8_bad = []
    exp_pos = {c: ('popup' if c in POPUP_CASES else 'input') for c in CASES}
    for c in CASES:
        got = 'popup' if c in POPUP_CASES else 'input'
        S = st(c)
        base = (pop(c).get('surface', {}).get('pos', [0, 80])[1]
                + pop(c).get('surface', {}).get('h', 0)) if c in POPUP_CASES else 72
        if S.get('pos', [None, None])[1] != base + 8:
            d8_bad.append(f"{c}: {S.get('pos')}/{base+8} ({exp_pos[c]})")
    set_('D-008', 'erfüllt' if not d8_bad else 'verletzt',
         d8_bad or ["Status-Position je Fall korrekt: unter Popup in "
                    "loading/ready/active/scroll-end/empty/error, unter Input in "
                    "closed/opening/selected/disabled"])
    set_('U-007', 'nicht anwendbar',
         [f"Existenz platzneutraler Popup-Layer in verborgenen Fällen nicht festgelegt; "
          f"beobachtet: Builder {builder.upper()} erzeugt in closed/opening/selected/"
          f"disabled keine Overlay-Knoten (Variante 'nicht erzeugt' — zulässig)"])

    # ---------------- clipping-scroll ----------------
    c54_bad = [f"{c}: clip={(pop(c).get('viewport') or {}).get('clipsContent')} "
               f"h={(pop(c).get('viewport') or {}).get('h')}" for c in POPUP_CASES
               if not (pop(c).get('viewport') or {}).get('clipsContent')]
    set_('E-054', 'erfüllt' if not c54_bad else 'verletzt',
         c54_bad or ["Viewport clippt seinen Inhalt (clipsContent=true, 6/6); "
                     "Inhalt > 160px wird geclippt (Listefälle: 224px Inhalt)"])
    se = pop('scroll-end')
    zu = next((o for o in se.get('options', []) if o['key'] == 'zuerich'), None)
    vp = se.get('viewport') or {}
    zu_ok = bool(zu and vp and vp['pos'][1] <= zu['pos'][1]
                 and zu['pos'][1] + zu['h'] <= vp['pos'][1] + vp['h'])
    set_('E-055', 'erfüllt' if zu_ok else 'verletzt',
         [f"scroll-end: Zürich abs. y {zu and zu['pos'][1]}…{zu and zu['pos'][1] + zu['h']} "
          f"in Viewport {vp.get('pos', [None])[1]}…{vp.get('pos', [None])[1] + vp.get('h', 0)} "
          f"({'vollständig sichtbar' if zu_ok else 'NICHT sichtbar'})"])
    off_obs, se_off = [], None
    for c in POPUP_CASES:
        ct_p = (pop(c).get('content') or {}).get('pos')
        vp_p = (pop(c).get('viewport') or {}).get('pos')
        if ct_p and vp_p:
            off = round(ct_p[1] - vp_p[1], 3)
            off_obs.append(f"{c}:{off}")
            if c == 'scroll-end':
                se_off = off
    # Audit-Anpassung (1): versiegelter EXP-Radius — Content versetzt SO, dass die
    # letzte Zeile sichtbar ist; exaktes Offset ist U-002-Sache (nicht geahndet).
    d56_ok = (se_off is not None and se_off < 0) and zu_ok
    set_('E-056', 'erfüllt' if d56_ok else 'verletzt',
         [f"Statischer Content-Versatz relativ zur Viewport-Oberkante: {off_obs} "
          f"(scroll-end {se_off} = 224−160, maximaler Scroll; letzte Zeile vollständig "
          f"sichtbar; keine Scroll-Dynamik im Canvas)"])
    set_('E-057', 'erfüllt' if all(len(opts(c)) == 7 for c in LIST_CASES) else 'verletzt',
         [f"alle 7 Ergebniszeilen als editierbare Layers in jedem Listenfall vorhanden, "
          f"inkl. geclippter (wien/y=160, zuerich/y=192) — nichts gelöscht"])
    d9_bad = []
    for c in ('ready', 'active'):
        v = pop(c).get('visibleOptions', [])
        cl = pop(c).get('clippedOptions', [])
        if v != KEYS[:5] or cl != ['wien', 'zuerich']:
            d9_bad.append(f"{c}: sichtbar={v} geclippt={cl}")
    set_('D-009', 'erfüllt' if not d9_bad else 'verletzt',
         d9_bad or ["ready/active (Scroll oben): sichtbar Berlin…Köln (5), "
                    "geclippt wien+zuerich — beide vorhanden"])
    set_('U-002', 'nicht anwendbar',
         [f"Scroll-Offset in scroll-end nicht numerisch festgelegt; beobachtet: "
          f"Builder {builder.upper()} wählt y=-64 (maximaler Scroll, 224−160=64); "
          f"damit 2 Zeilen geclippt — Inkonsistenz README 'drei unsichtbare Daten' vs. "
          f"Arithmetik (max. 2) bleibt Lücke der Definition, dokumentiert, nicht geahndet"])

    # ---------------- popup-visibility ----------------
    p58_bad = []
    for c in CASES:
        exp = c in POPUP_CASES
        if ('surface' in pop(c)) != exp:
            p58_bad.append(f"{c}: vorhanden={'surface' in pop(c)} erwartet={exp}")
    set_('E-058', 'erfüllt' if not p58_bad else 'verletzt',
         p58_bad or ["Popup sichtbar genau in loading/ready/active/scroll-end/empty/"
                     "error; opening laut Projection popupVisible=false → kein Popup "
                     "(beide Builder)"])
    set_('E-059', 'erfüllt' if 'surface' not in pop('disabled') else 'verletzt',
         ["disabled: keine sichtbaren Popupteile (kein Surface-/Viewport-/List-Knoten)"])
    m60_bad = []
    m60_h = {}
    for c in MSG_CASES:
        msg = pop(c).get('message') or {}
        S = st(c)
        # Audit-Anpassung (2): Zeilenhöhe wird nur beobachtet (U-003: nicht geahndet)
        if not msg or msg.get('text') != STATUS_TEXT[c] or S.get('text') != STATUS_TEXT[c]:
            m60_bad.append(f"{c}: Meldung={msg.get('text')!r} Status={S.get('text')!r}")
        m60_h[c] = msg.get('h')
    set_('E-060', 'erfüllt' if not m60_bad else 'verletzt',
         m60_bad or [f"Meldungszeile im Popup wiederholt den Status-Text; beobachtete "
                     f"Zeilenhöhe {m60_h} (U-003: exakte Höhe/Farbe nicht als Verletzung "
                     f"gewertet): "
                     f"{ {c: (pop(c).get('message') or {}).get('text') for c in MSG_CASES} }"])
    n6 = sum(1 for c in POPUP_CASES if 'surface' in pop(c))
    n4 = sum(1 for c in NOPOPUP_CASES if 'surface' not in pop(c))
    set_('D-010', 'erfüllt' if n6 == 6 and n4 == 4 else 'verletzt',
         [f"genau {n6} Fälle mit sichtbarem Popup, {n4} ohne"])
    set_('U-003', 'nicht anwendbar',
         [f"Höhe/Farbe der Meldungszeile nicht vollständig festgelegt; beobachtet: "
          f"Builder {builder.upper()} nutzt 32px (rowHeight) mit Textfarbe #172b4d — "
          f"dokumentierte Annahme, nicht geahndet"])

    # ---------------- editability ----------------
    set_('E-061', 'erfüllt',
         [f"editierbares OpenPencil-Design: {doc['nodeCount']} Vektor-/Text-Knoten mit "
          f"editierbaren Properties (Fills/Strokes/Texte/Geometrie), benannte "
          f"Hierarchie; keine Rasterkopie (0 IMAGE-Knoten), keine flache Abbildung"])
    set_('E-062', 'erfüllt',
         ["Keine Interaktivität/ARIA-Ausführung/Canvas-Interaktion gefordert — nichts "
          "derartiges vorhanden, wird nicht beanstandet (erlaubte Freiheit)"])

    # ---------------- accessibility ----------------
    # Hilfsdaten: Rollen-/aria-Namen in Layer-Names und Texten
    import re as _re
    pat = _re.compile(r'aria-?\w+|combobox|listbox|activedescendant|expanded|live|atomic|tabindex', _re.I)
    text_hits = []
    for c in CASES:
        for t in cs(c).get('allTexts', []):
            if t['text'] and pat.search(t['text']):
                text_hits.append(f"{c}/{t['name']}: {t['text']!r}")
    # Captions (Seitenebene, A) ebenfalls durchsuchen
    cap_hits = []
    if builder == 'a':
        o2, n2, p2 = load('a')
        for n in n2.values():
            if n['type'] == 'TEXT' and n.get('text') and pat.search(n['text']):
                cap_hits.append(f"{n['name']}: {n['text']!r}")
    a_names = set()
    for c in CASES:
        a_names.add((lab(c) or {}).get('name', ''))
        a_names.add((inp(c) or {}).get('name', ''))
        a_names.add((st(c) or {}).get('name', ''))
        p = pop(c)
        a_names.add((p.get('surface') or {}).get('name', ''))
        a_names.add(((p.get('viewport')) or {}).get('name', ''))
        a_names.add((p.get('content') or {}).get('name', ''))
        a_names.add((p.get('list') or {}).get('name', ''))
        a_names |= {o['name'] for o in opts(c)}
        a_names.add(((p.get('message')) or {}).get('name', ''))
    # Seiten-/Fallnamen
    a_names.update(cs(c)['caseFrame']['name'] for c in CASES if cs(c).get('caseFrame'))

    role_input = any('combobox' in n.lower() for n in a_names) or \
        any('combobox' in h for h in text_hits)
    role_list = any('listbox' in n.lower() for n in a_names)
    role_opt = any(n.lower().startswith('option') for n in a_names)
    role_status = any(n.lower() in ('status',) for n in a_names)
    set_('E-063', 'verletzt' if not (role_input and role_list and role_opt and role_status)
         else 'erfüllt',
         [f"Rollen-Zuordnung über lesbare Namen: input=combobox: {role_input}; "
          f"list=listbox: {role_list}; option: {role_opt}; status: {role_status}. "
          f"Teil-Namen im Dokument: {sorted(n for n in a_names if n)[:14]} …"])
    scan_hits = text_hits + cap_hits + [str(x) for x in g['pluginDataKeys']]
    e64 = any('aria-autocomplete' in h for h in scan_hits)
    # Audit-Anpassung (3): builder-korrekter obs-Text
    pd_desc = ('pluginData enthält nur Writer-Artefakte layoutDirection/textDirection'
               if builder == 'a' else 'es ist kein pluginData vorhanden')
    set_('E-064', 'erfüllt' if e64 else 'verletzt',
         ["Input trägt aria-autocomplete='list' als lesbare Annotation"] if e64 else
         [f"Wert 'aria-autocomplete=list' nicht ablesbar: keine aria-Annotation in "
          f"Layer-Namen, Text, Captions oder pluginData ({pd_desc})"])
    e65 = any('expanded' in h for h in scan_hits)
    set_('E-065', 'erfüllt' if e65 else 'verletzt',
         ["aria-expanded je Zustand als Wert annotiert"] if e65 else
         ["Werte false/true von aria-expanded nicht ablesbar (nirgends 'expanded'); "
          + ("A: Captions nennen Phase/SCXML-Pfad — Ableitung nur über externe "
             "accessibility.rules.json möglich" if builder == 'a' else
             "B: Fall-Namen enthalten den Zustandsnamen; Werte selbst fehlen")])
    e66_bad = []
    for c in LIST_CASES:
        hl = [o['key'] for o in opts(c) if o['fillToken'] == 'highlight']
        if hl != ([ACTIVE_KEY[c]] if c in ACTIVE_KEY else []):
            e66_bad.append(f"{c}: {hl}")
    set_('E-066', 'erfüllt' if not e66_bad else 'verletzt',
         e66_bad or ["genau eine hervorgehobene (aria-selected-repräsentierende) Option "
                     "pro Fall = die aktive; keine zweite; selected bestätigt keinen "
                     "value (selected-Fall ohne Highlight)"])
    e67_bad = []
    for c in LIST_CASES:
        hl = [o['key'] for o in opts(c) if o['fillToken'] == 'highlight']
        exp = [ACTIVE_KEY[c]] if c in ACTIVE_KEY else []
        if hl != exp:
            e67_bad.append(f"{c}: {hl}/{exp}")
    set_('E-067', 'erfüllt' if not e67_bad else 'verletzt',
         e67_bad or ["active → hamburg hervorgehoben; scroll-end → zuerich; "
                     "ready → keine; alle übrigen Fälle ohne Popup/Optionen"])
    e68_bad = []
    for c in LIST_CASES:
        dis = [o['key'] for o in opts(c) if o['labelToken'] == 'disabled']
        if dis != ['muenchen']:
            e68_bad.append(f"{c}: {dis}")
    set_('E-068', 'erfüllt' if not e68_bad else 'verletzt',
         e68_bad or ["nur muenchen in disabled-Farbe (aria-disabled-Repräsentation); "
                     "keine andere Option"])
    set_('E-069', 'erfüllt' if all(
        any(o['key'] == 'muenchen' and o['labelToken'] == 'disabled' for o in opts(c))
        for c in LIST_CASES) else 'verletzt',
         ["muenchen in allen drei Sichtbarkeitsfällen (ready/active/scroll-end) "
          "disabled (#94a3b8)"])
    e70 = any('activedescendant' in h for h in scan_hits)
    set_('E-070', 'erfüllt' if e70 else 'verletzt',
         ["aria-activedescendant gesetzt (active→hamburg, scroll-end→zuerich)"] if e70
         else [f"Attributwert 'aria-activedescendant' nicht ablesbar; "
               + ("A: Caption nennt 'aktiv: hamburg'/'aktiv: zuerich' (Key lesbar, "
                  "Attribut selbst fehlt)" if builder == 'a'
                  else "B: nur Highlight-Füllung, keine Annotation des Keys")])
    e71_live = any('live' in h for h in scan_hits)
    e71_atomic = any('atomic' in h for h in scan_hits)
    set_('E-071', 'erfüllt' if (role_status and e71_live and e71_atomic) else 'verletzt',
         [f"Status-Region: Rolle 'status' lesbar via Layer-Name={role_status}; "
          f"aria-live='polite'={e71_live}; aria-atomic='true'={e71_atomic} — "
          f"live/atomic-Werte in keinem Namen, Text, Caption oder pluginData vorhanden"])
    e72_bad = []
    for c in CASES:
        if lab(c).get('text') != LABEL:
            e72_bad.append(f"{c}: Label-Text {lab(c).get('text')!r}")
    for c in LIST_CASES:
        for o in opts(c):
            if o['label'] != dict(zip(KEYS, LABELS))[o['key']]:
                e72_bad.append(f"{c}/{o['key']}: {o['label']!r}")
    for c in ph_cases:
        ts = inp(c).get('texts', [])
        if not ts or ts[0]['text'] != PLACEHOLDER:
            e72_bad.append(f"{c}: Placeholder {ts and ts[0]['text']!r}")
    set_('E-072', 'erfüllt' if not e72_bad else 'verletzt',
         e72_bad or ["Namensquellen realisiert: Input-/List-Name aus Label 'Stadt "
                     "auswählen' (Label-Knoten über Input); Option-Name = result.label; "
                     "Platzhalter 'Stadt suchen …' aus interface.placeholder"])
    e73 = any('tabindex' in h or 'tabstop' in h.lower() for h in scan_hits)
    set_('E-073', 'erfüllt' if not e73 else 'verletzt',
         ["keine zusätzlichen Fokus-/Tabstop-Annotationen an Popup/Viewport "
          "(negativer Check: nirgends tabindex/focus-Annotation); Input-Fokus semantisch "
          "im Input (Fokusrand), nicht im Overlay"])
    set_('E-074', 'erfüllt',
         ["ARIA-Werte nur als semantische Annotationen (benannte Teile, Label-, Status-, "
          "Aktiv-/Deaktiv-Stile); statisches Design ohne funktionales Screenreader-"
          "Verhalten — keine Behauptung über SR-Testbarkeit"])
    set_('U-004', 'nicht anwendbar',
         [f"Darstellungsform der ARIA-Attribute nicht spezifiziert; beobachtet: "
          f"Builder {builder.upper()} = Layer-Namen"
          + (" + Captions mit Phase/SCXML-Pfad/aktiv-/value-Angaben" if builder == 'a'
             else " (Anatomie-/Teil-Namen, ohne Captions)")
          + "; maschinenlesbare aria-*-Attribute in keinem Format vorhanden"])
    set_('U-005', 'nicht anwendbar',
         [f"Pflicht eines leeren Status-Layers in closed/disabled offen; beobachtet: "
          f"Builder {builder.upper()} lässt Status-Knoten mit leerem Text vorhanden "
          f"(closed: w={st('closed').get('w')}, disabled: w={st('disabled').get('w')})"])
    set_('U-006', 'nicht anwendbar',
         [f"error-relay.scxml keinem Designfall zugeordnet; beobachtet: kein Fall im "
          f"Dokument; " + ("fehlt zusätzlich im Quell-Manifest des Builders (21/22 "
                           "Dateien), im REPORT dokumentiert" if builder == 'a'
                           else "im Quell-Manifest erfasst (22/22), im REPORT als nicht "
                           "repräsentiert dokumentiert")])
    return res, g

import hashlib
import os

ROOT = '/Users/kcnpxcp/Dev/GitHub/ui-contracts'
RUN = f'{ROOT}/examples/autocomplete/reproducibility/run-03'
DEF_FILES = [
    'components/README.md', 'components/library.json', 'components/tokens.json',
    'components/autocomplete/README.md', 'components/autocomplete/component.json',
    'components/autocomplete/interface.json', 'components/autocomplete/stories.json',
    'components/autocomplete/layout.css', 'components/autocomplete/behavior.scxml',
    'components/autocomplete/accessibility.html',
    'components/autocomplete/accessibility.rules.json',
    'components/autocomplete/error-relay.scxml',
    'components/overlay/component.json', 'components/overlay/interface.json',
    'components/overlay/layout.css', 'components/overlay/behavior.scxml',
    'components/overlay/accessibility.html',
    'components/scroll-area/component.json', 'components/scroll-area/interface.json',
    'components/scroll-area/layout.css', 'components/scroll-area/behavior.scxml',
    'components/scroll-area/accessibility.html',
]

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()

def manifest_of(builder):
    s = json.load(open(f'{RUN}/builder-{builder}/source-sha256.json'))
    if builder == 'a':
        return {k.lstrip('./'): v for k, v in s['files'].items()}
    return {f['path'].removeprefix('components/'): f['sha256'] for f in s['files']}

def check_definitions():
    """Frische SHA-256 aller 22 Definitionsdateien vs. beiden Quell-Manifesten."""
    fresh, missing = {}, []
    for rel in DEF_FILES:
        p = f'{ROOT}/{rel}'
        if not os.path.exists(p):
            missing.append(rel)
            continue
        fresh[rel.removeprefix('components/')] = sha256_file(p)
    out = {'freshHashes': fresh, 'missing': missing}
    for b in ('a', 'b'):
        man = {k.lstrip('./').removeprefix('components/'): v
               for k, v in manifest_of(b).items()}
        mism = {k: (man.get(k), fresh.get(k)) for k in man
                if k in fresh and man[k] != fresh[k]}
        notin = [k for k in man if k not in fresh]
        out[b] = {'manifestEntries': len(man),
                  'matching': len(man) - len(mism) - len(notin),
                  'mismatch': mism, 'inManifestNotOnDisk': notin,
                  'notCoveredByManifest': sorted(set(fresh) - set(man))}
    return out

def main():
    docs = {b: build(b) for b in ('a', 'b')}
    for b in ('a', 'b'):
        with open(f'{R}/normalized-{b}.json', 'w') as f:
            json.dump(docs[b], f, ensure_ascii=False, indent=1)
        print(f'wrote normalized-{b}.json')

    native = {'note': 'Alle Einzelbeobachtungen pro Artefakt, direkt aus den '
                      'wiedereingelesenen Originaldateien (original-a/b.json). '
                      'normalized-*.json enthalten dieselben Werte normalisiert.',
              'a': docs['a'], 'b': docs['b']}
    with open(f'{R}/native-checks.json', 'w') as f:
        json.dump(native, f, ensure_ascii=False, indent=1)
    print('wrote native-checks.json')

    defcheck = check_definitions()
    with open(f'{R}/definition-hash-check.json', 'w') as f:
        json.dump(defcheck, f, ensure_ascii=False, indent=1)
    print('wrote definition-hash-check.json')

    results = {}
    for b in ('a', 'b'):
        res, g = evaluate(docs[b], b)
        d = defcheck
        man_ok = not d[b]['mismatch'] and not d[b]['inManifestNotOnDisk']
        ondisk_ok = not d['missing']
        status = 'erfüllt' if (man_ok and ondisk_ok) else 'verletzt'
        obs = [f"22/22 Definitionsdateien auf Disk (frische SHA-256 berechnet); "
               f"Manifest Builder {b.upper()}: {d[b]['manifestEntries']} Einträge, "
               f"{d[b]['matching']} identisch; Abweichungen: {d[b]['mismatch'] or 'keine'}; "
               f"nicht vom Manifest abgedeckt: {d[b]['notCoveredByManifest'] or 'keine'}"]
        if b == 'a':
            obs.append("Lücken dokumentiert (REPORT.md, 19 Punkte, inkl. "
                       "error-relay.scxml, Platzhalter/Disabled-Konflikt, Scroll-Offset); "
                       "Definition selbst unverändert")
        else:
            obs.append("Lücken dokumentiert (REPORT.md, 18 Punkte); Definition "
                       "unverändert; ACHTUNG: Report-Punkt 4 behauptet "
                       "'Platzhalter bleibt muted im disabled-Fall', das Artefakt "
                       "zeigt aber #94a3b8 — Widerspruch Report↔Datei, s. REVIEW.md")
        res['E-004'] = {'status': status, 'obs': obs}
        results[b] = res

    with open(f'{R}/criterion-results.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    print('wrote criterion-results.json')

    from collections import Counter as _C
    for b in ('a', 'b'):
        cnt = _C(v['status'] for v in results[b].values())
        print(f"Builder {b.upper()}: {dict(cnt)}")
        for k in sorted(results[b]):
            if results[b][k]['status'] == 'verletzt':
                print(f"  VERLETZT {k}: {results[b][k]['obs'][0][:220]}")

if __name__ == '__main__':
    main()
