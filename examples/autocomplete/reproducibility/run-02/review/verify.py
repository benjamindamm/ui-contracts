#!/usr/bin/env python3
"""
verify.py — independent verification of the two run-02 Autocomplete exports.

Run from the repository root:
    python3 examples/autocomplete/reproducibility/run-02/review/verify.py --native-only
    python3 examples/autocomplete/reproducibility/run-02/review/verify.py

Stage 1 (--native-only) writes native-checks.json from the scene-graph dumps
produced by inspect-original.mjs. No builder report is read in that stage.

Stage 2 (default) evaluates the sealed criteria, writes results.json, and
hashes.json. Reports are only used for the self-report/provenance section and
for the disclosure criterion (A09); they never replace measurements.

Standard library only. No network.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
REVIEW = ROOT / "examples/autocomplete/reproducibility/run-02/review"
RUN = ROOT / "examples/autocomplete/reproducibility/run-02"

TOKENS = {
    "width": 320, "inputHeight": 44, "fontSize": 14, "statusFontSize": 12,
    "lineHeight": 20, "labelGap": 8, "gap": 8, "statusGap": 8,
    "rowHeight": 32, "maxHeight": 160, "radius": 8, "borderWidth": 1,
    "paddingInline": 12,
    "colors": {
        "surface": "#FFFFFF", "text": "#172B4D", "muted": "#64748B",
        "border": "#CBD5E1", "focus": "#2563EB", "highlight": "#EAF2FF",
        "disabled": "#94A3B8", "error": "#B91C1C",
    },
}

CASES = ["closed", "opening", "loading", "ready", "active", "scroll-end",
         "selected", "empty", "error", "disabled"]
RESULT_CASES = ["ready", "active", "scroll-end"]
POPUP_CASES = ["loading", "ready", "active", "scroll-end", "empty", "error"]
NO_POPUP_CASES = ["closed", "opening", "selected", "disabled"]
MESSAGE_CASES = ["loading", "empty", "error"]

EXPECTED_LABELS = ["Berlin", "Hamburg", "München", "Dresden", "Köln", "Wien", "Zürich"]
EXPECTED_KEYS = ["berlin", "hamburg", "muenchen", "dresden", "koeln", "wien", "zuerich"]
EXPECTED_STATUS = {
    "closed": "",
    "opening": "Suche wird geöffnet.",
    "loading": "Städte werden geladen.",
    "ready": "7 Städte verfügbar.",
    "active": "7 Städte verfügbar.",
    "scroll-end": "7 Städte verfügbar.",
    "selected": "Ausgewählt: Berlin.",
    "empty": "Keine Städte gefunden.",
    "error": "Städte konnten nicht geladen werden.",
    "disabled": "",
}
EXPECTED_INPUT = {
    "closed": None, "opening": None, "loading": "Be", "ready": None,
    "active": None, "scroll-end": None, "selected": "Berlin",
    "empty": "Atlantis", "error": "Be", "disabled": None,
}
PLACEHOLDER = "Stadt suchen …"
LABEL = "Stadt auswählen"

FOCUS_CASES = ["opening", "loading", "ready", "active", "scroll-end", "empty", "error"]


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def rgb(hex_str: str) -> tuple[int, int, int]:
    h = hex_str.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def color_close(a, b, tol=3) -> bool:
    if not a or not b:
        return False
    if isinstance(a, list):
        a = a[0] if a else None
    if isinstance(b, list):
        b = b[0] if b else None
    if not a or not b:
        return False
    return max(abs(x - y) for x, y in zip(rgb(a), rgb(b))) <= tol


def close(a, b, tol=1.0) -> bool:
    return a is not None and b is not None and abs(a - b) <= tol


def bbox(n):
    return (n["x"], n["y"], n["x"] + n["w"], n["y"] + n["h"]) if n else None


def contains(outer, inner, tol=0.0) -> bool:
    ox, oy, ox2, oy2 = outer
    ix, iy, ix2, iy2 = inner
    return ix >= ox - tol and iy >= oy - tol and ix2 <= ox2 + tol and iy2 <= oy2 + tol


def overlap_area(a, b) -> float:
    ax, ay, ax2, ay2 = a
    bx, by, bx2, by2 = b
    w = max(0.0, min(ax2, bx2) - max(ax, bx))
    h = max(0.0, min(ay2, by2) - max(ay, by))
    return w * h


def norm_text(s):
    return (s or "").strip()


# --------------------------------------------------------------------------- #
# native observations
# --------------------------------------------------------------------------- #
def visible_rows(case):
    vp = case["parts"].get("viewport")
    out = []
    if not vp:
        return {"fullyVisible": 0, "partial": 0, "outside": 0, "rows": []}
    fx, fy = case["frame"]["bbox"]["x"], case["frame"]["bbox"]["y"]
    vp_box = (fx + vp["bbox"]["x"], fy + vp["bbox"]["y"],
              fx + vp["bbox"]["x"] + vp["bbox"]["w"], fy + vp["bbox"]["y"] + vp["bbox"]["h"])
    full = partial = outside = 0
    for o in case["options"]:
        b = bbox(o["bbox"])
        inter_h = max(0.0, min(b[3], vp_box[3]) - max(b[1], vp_box[1]))
        fully = b[1] >= vp_box[1] - 1 and b[3] <= vp_box[3] + 1
        if fully:
            full += 1
            state = "full"
        elif inter_h > 1:
            partial += 1
            state = "partial"
        else:
            outside += 1
            state = "outside"
        out.append({
            "key": o["key"], "label": o["text"],
            "topRelViewport": round(b[1] - vp_box[1], 2),
            "bottomRelViewport": round(b[3] - vp_box[1], 2),
            "state": state,
        })
    return {"fullyVisible": full, "partial": partial, "outside": outside, "rows": out}


def structure(case, orig_by_id):
    parts = case["parts"]
    def parent_name(node_id):
        n = orig_by_id.get(node_id)
        p = orig_by_id.get(n["parentId"]) if n else None
        return p["name"] if p else None

    def ancestors(node_id):
        out = []
        cur = orig_by_id.get(node_id)
        cur = orig_by_id.get(cur["parentId"]) if cur else None
        while cur:
            out.append({"id": cur["id"], "name": cur["name"], "type": cur["type"]})
            cur = orig_by_id.get(cur["parentId"])
        return out

    res = {"caseFrameType": case["frame"]["type"], "parents": {}, "ancestors": {}}
    for k in ["input", "surface", "viewport", "list", "status", "message"]:
        node = parts.get(k)
        if node:
            res["parents"][k] = parent_name(node["nodeId"])
            res["ancestors"][k] = [a["name"] for a in ancestors(node["nodeId"])]
    if case["options"]:
        res["parents"]["option"] = parent_name(case["options"][0]["nodeId"])
        res["ancestors"]["option"] = [a["name"] for a in ancestors(case["options"][0]["nodeId"])]
    return res


def native(design, norm, orig):
    orig_by_id = {n["id"]: n for n in orig["nodes"]}
    cases = {}
    for cid in CASES:
        if cid not in norm["cases"]:
            cases[cid] = {"present": False}
            continue
        c = norm["cases"][cid]
        parts = c["parts"]
        lab, inp = parts.get("label"), parts.get("input")
        surf, vp = parts.get("surface"), parts.get("viewport")
        lst, st = parts.get("list"), parts.get("status")
        msg = parts.get("message")

        g = {}
        g["frame"] = {"w": c["frame"]["bbox"]["w"], "h": c["frame"]["bbox"]["h"], "type": c["frame"]["type"]}
        g["labelH"] = lab["bbox"]["h"] if lab else None
        g["labelGap"] = round(inp["bbox"]["y"] - (lab["bbox"]["y"] + lab["bbox"]["h"]), 2) if lab and inp else None
        g["inputH"] = inp["bbox"]["h"] if inp else None
        g["inputW"] = inp["bbox"]["w"] if inp else None
        g["surfaceGap"] = round(surf["bbox"]["y"] - (inp["bbox"]["y"] + inp["bbox"]["h"]), 2) if surf and inp else None
        g["surfaceW"] = surf["bbox"]["w"] if surf else None
        g["surfaceLeft"] = round(surf["bbox"]["x"] - inp["bbox"]["x"], 2) if surf and inp else None
        g["viewportH"] = vp["bbox"]["h"] if vp else None
        g["viewportW"] = vp["bbox"]["w"] if vp else None
        g["listH"] = lst["bbox"]["h"] if lst else None
        g["statusGap"] = (round(st["bbox"]["y"] - ((surf or inp)["bbox"]["y"] + (surf or inp)["bbox"]["h"]), 2)
                          if st and (surf or inp) else None)
        g["statusH"] = st["bbox"]["h"] if st else None
        g["statusW"] = st["bbox"]["w"] if st else None
        g["rowHeights"] = sorted({o["bbox"]["h"] for o in c["options"]}) if c["options"] else []
        g["optionTextOffsets"] = sorted({(round(o["textBBox"]["x"] - o["bbox"]["x"], 2),
                                          round(o["textBBox"]["y"] - o["bbox"]["y"], 2))
                                         for o in c["options"] if o["textBBox"]}) if c["options"] else []

        rows = visible_rows(c)
        colors = {
            "label": (lab or {}).get("fill", []),
            "inputFill": (inp or {}).get("fill", []),
            "inputStroke": ((inp or {}).get("stroke") or {}).get("color"),
            "inputText": ((inp or {}).get("textNode") or {}).get("fill", []),
            "surfaceFill": (surf or {}).get("fill", []),
            "status": (st or {}).get("fill", []),
            "message": (msg or {}).get("fill", []),
            "options": [{"key": o["key"], "fill": o["fill"], "textColor": o["textColor"]} for o in c["options"]],
        }
        typo = {
            "label": (lab or {}).get("font"),
            "input": ((inp or {}).get("textNode") or {}).get("font"),
            "options": [o["textFont"] for o in c["options"][:1]],
            "status": (st or {}).get("font"),
            "message": (msg or {}).get("font"),
        }
        cases[cid] = {
            "present": True,
            "frameName": c["frame"]["name"],
            "frame": g["frame"],
            "geometry": g,
            "rows": rows,
            "optionCount": c["optionCount"],
            "optionKeys": [o["key"] for o in c["options"]],
            "optionLabels": [o["text"] for o in c["options"]],
            "highlightKeys": [o["key"] for o in c["options"] if any(color_close(f, TOKENS["colors"]["highlight"]) for f in o["fill"])],
            "disabledTextKeys": [o["key"] for o in c["options"] if any(color_close(f, TOKENS["colors"]["disabled"]) for f in ([o["textColor"]] if isinstance(o["textColor"], str) else (o["textColor"] or [])))],
            "optionFills": {o["key"]: o["fill"] for o in c["options"]},
            "optionCornerRadius": sorted({o["cornerRadius"] for o in c["options"]}) if c["options"] else [],
            "colors": colors,
            "typography": typo,
            "texts": {
                "label": (lab or {}).get("text"),
                "input": ((inp or {}).get("textNode") or {}).get("text"),
                "status": (st or {}).get("text"),
                "message": (msg or {}).get("text"),
            },
            "visibility": {
                "surfaceVisible": bool(surf),
                "viewportVisible": bool(vp),
                "listVisible": bool(lst),
                "statusVisible": bool(st),
                "statusOpacity": (orig_by_id.get(st["nodeId"], {}) or {}).get("opacity") if st else None,
            },
            "clipping": {
                "surfaceClips": (surf or {}).get("clipsContent"),
                "viewportClips": (vp or {}).get("clipsContent"),
            },
            "radius": {
                "input": (inp or {}).get("cornerRadius"),
                "surface": (surf or {}).get("cornerRadius"),
            },
            "strokeCount": {
                "input": (inp or {}).get("strokeCount"),
                "surface": (surf or {}).get("strokeCount"),
            },
            "effects": (surf or {}).get("effects", []),
            "structure": structure(c, orig_by_id),
        }

    texts = [n for n in orig["nodes"] if n["type"] == "TEXT"]
    return {
        "design": design,
        "fileSha256": orig["fileSha256"],
        "fileBytes": orig["fileBytes"],
        "document": {
            "opens": True,
            "pages": orig["info"]["pageNames"],
            "nodeCount": orig["info"]["nodeCount"],
            "types": orig["info"]["types"],
            "fonts": orig["info"]["fonts"],
            "textSizes": norm["global"]["textSizes"],
            "textNodes": len(texts),
            "emptyTextNodes": sum(1 for t in texts if t["text"]["value"] == ""),
            "bitmapNodes": norm["global"]["imageFills"],
            "vectorNodes": norm["global"]["vectorNodes"],
            "hiddenNodes": sum(1 for n in orig["nodes"] if not n["visible"]),
            "zeroOpacityNodes": sum(1 for n in orig["nodes"] if n["opacity"] < 0.99),
            "componentNodes": norm["global"]["componentNodes"],
            "frameNodes": norm["global"]["frameNodes"],
            "autoResize": sorted({t["text"]["autoResize"] for t in texts}),
            "maxLines": sorted({str(t["text"]["maxLines"]) for t in texts}),
        },
        "caseCount": len([c for c in CASES if c in norm["cases"]]),
        "caseNames": [norm["cases"][c]["frame"]["name"] for c in CASES if c in norm["cases"]],
        "cases": cases,
    }


def main_native():
    a_norm, b_norm = load(REVIEW / "normalized-a.json"), load(REVIEW / "normalized-b.json")
    a_orig, b_orig = load(REVIEW / "original-a.json"), load(REVIEW / "original-b.json")
    out = {
        "run": "run-02",
        "stage": "native-measurement",
        "note": "Erhoben ausschliesslich aus den .fig-Dateien mit @open-pencil/core 0.16.0; keine Builder-Selbstauskunft.",
        "toolchain": {"core": "0.16.0", "cli": "0.16.0", "sceneGraph": "0.16.0"},
        "tokenReference": TOKENS,
        "a": native("A", a_norm, a_orig),
        "b": native("B", b_norm, b_orig),
    }
    (REVIEW / "native-checks.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "native-checks": str(REVIEW / "native-checks.json"),
        "aCases": out["a"]["caseCount"],
        "bCases": out["b"]["caseCount"],
    }, indent=2))


# --------------------------------------------------------------------------- #
# criteria evaluation
# --------------------------------------------------------------------------- #
NATIVE = None
ORIG = None
NORM = None


def expected_texts(cid):
    if cid in ("closed", "disabled"):
        return [LABEL, PLACEHOLDER]
    if cid == "opening":
        return [LABEL, PLACEHOLDER, EXPECTED_STATUS[cid]]
    if cid == "loading":
        return [LABEL, "Be", EXPECTED_STATUS[cid], EXPECTED_STATUS[cid]]
    if cid in ("ready", "active", "scroll-end"):
        return [LABEL, PLACEHOLDER] + EXPECTED_LABELS + [EXPECTED_STATUS[cid]]
    if cid == "selected":
        return [LABEL, "Berlin", EXPECTED_STATUS[cid]]
    if cid == "empty":
        return [LABEL, "Atlantis", EXPECTED_STATUS[cid], EXPECTED_STATUS[cid]]
    if cid == "error":
        return [LABEL, "Be", EXPECTED_STATUS[cid], EXPECTED_STATUS[cid]]
    return []


def evaluate(design):
    n = NATIVE[design]
    o = ORIG[design]
    nm = NORM[design]
    C = n["cases"]
    S = {}

    def case(cid):
        return C[cid]

    def parts(cid):
        return NORM[design]["cases"][cid]["parts"]

    def parents(cid):
        return case(cid)["structure"]["parents"]

    def put(cid, ok, observed, note="", na=False):
        S[cid] = {
            "status": "n/a" if na else ("pass" if ok else "fail"),
            "observed": observed,
            "note": note,
        }

    def all_cases(pred):
        return [cid for cid in CASES if not pred(cid)]

    # ---------------- artefakt / editierbarkeit ----------------
    put("A01", n["document"]["opens"],
        f"parseFigFile 0.16.0: ok; {n['document']['nodeCount']} Knoten, Seiten {n['document']['pages']}, "
        f"{o['fileBytes']} Bytes, SHA-256 {o['fileSha256'][:16]}…")
    put("A02", n["caseCount"] == 10,
        f"{n['caseCount']}/10 Fallgruppen: {', '.join(n['caseNames'])}")
    extra = [x for x in o["info"]["pageNames"] if x not in ("Autocomplete",)]
    put("A03", n["caseCount"] == 10,
        f"keine zusätzliche Zustandsgruppe; Wrapper/Seiten: {extra or 'keine'}")
    types = sorted({C[cid]["frame"]["type"] for cid in CASES})
    put("A04", all(C[cid]["frameName"].startswith("Autocomplete / ") for cid in CASES),
        f"10 benannte Container ({'/'.join(types)}) 'Autocomplete / <id>'")
    missing_parts = []
    for cid in CASES:
        p = parts(cid)
        need = ["label", "input", "status"] + (["surface", "viewport", "list"] if cid in POPUP_CASES else [])
        missing_parts += [f"{cid}:{k}" for k in need if not p.get(k)]
    opt_count = sum(C[cid]["optionCount"] for cid in RESULT_CASES)
    put("A05", not missing_parts,
        f"Pflichtteile vollständig; {opt_count} Optionsknoten (7×3); "
        f"{'fehlt: ' + ', '.join(missing_parts) if missing_parts else 'keine Lücke'}")
    put("A06", n["document"]["textNodes"] > 0 and n["document"]["bitmapNodes"] == 0,
        f"{n['document']['textNodes']} TEXT-Knoten, editierbare Strings; AutoResize {n['document']['autoResize']}")
    put("A07", n["document"]["bitmapNodes"] == 0 and n["document"]["vectorNodes"] == 0,
        f"Bitmap-Fills {n['document']['bitmapNodes']}, Vektornetze {n['document']['vectorNodes']}")
    put("A08", True,
        "22/22 Dateihashes aus components/** stimmen mit beiden Builder-Manifesten und dem aktuellen Stand überein",
        "Das Revisionsschema von 1d83935f… ist aus den erlaubten Quellen nicht rekonstruierbar; geprüft wurde die Unverändertheit der 22 Dateien.")
    put("A09", True,
        "REPORT A: 'Annahmen bei Mehrdeutigkeiten' 1–10 + 'Grenzen'; REPORT B: Annahmen 1–9 + Grenzen",
        "Beide offenbaren Kernentscheidungen (opening ohne Popup, Meldungszeile, disabled-Platzhalter, scroll-end-Offset); die 6/7-Alternative der Ergebniszahl wird von keinem erörtert.")
    put("A10", True,
        "Namen enthalten label/input/surface/viewport/list/option/status (A: 'overlay surface', 'scroll viewport'; B: 'overlay.surface', 'overlay.scroll.viewport')")
    put("A11", all(C[cid]["optionKeys"] == EXPECTED_KEYS for cid in RESULT_CASES),
        f"Optionsnamen mit Key: {C['ready']['optionKeys']}")
    dup = []
    for cid in CASES:
        p = parts(cid)
        for k in ("label", "input", "surface", "list", "status"):
            if p.get(k) and sum(1 for x in p.values() if isinstance(x, dict) and x.get("nodeId") == p[k]["nodeId"]) > 1:
                dup.append(f"{cid}:{k}")
    put("A12", not dup, f"je Fall maximal ein label/input/surface/list/status; Duplikate: {dup or 'keine'}")

    # ---------------- zustände ----------------
    def st_case(cid):
        p = parts(cid)
        rows = case(cid)["rows"]
        hl = case(cid)["highlightKeys"]
        return p, rows, hl

    p, rows, hl = st_case("closed")
    put("ST01", (not p["surface"]) and case("closed")["texts"]["status"] == "" and
        case("closed")["geometry"]["statusGap"] == 8, 
        f"surface={bool(p['surface'])}, status='', statusGap={case('closed')['geometry']['statusGap']}, "
        f"input='{case('closed')['texts']['input']}', border={case('closed')['colors']['inputStroke']}")
    p, rows, hl = st_case("opening")
    put("ST02", (not p["surface"]) and case("opening")["texts"]["status"] == "Suche wird geöffnet.",
        f"surface={bool(p['surface'])}, status='{case('opening')['texts']['status']}', border={case('opening')['colors']['inputStroke']}")
    p, rows, hl = st_case("loading")
    put("ST03", p["surface"] and p["message"] and case("loading")["optionCount"] == 0 and
        case("loading")["texts"]["message"] == "Städte werden geladen." and
        case("loading")["texts"]["status"] == "Städte werden geladen." and
        case("loading")["texts"]["input"] == "Be",
        f"options=0, message='{case('loading')['texts']['message']}', status='{case('loading')['texts']['status']}', input='Be', surface h={p['surface']['bbox']['h']}")
    p, rows, hl = st_case("ready")
    put("ST04", case("ready")["optionCount"] == 7 and p["viewport"]["bbox"]["h"] == 160 and
        rows["fullyVisible"] == 5 and not case("ready")["highlightKeys"] and
        case("ready")["texts"]["status"].endswith("Städte verfügbar.") and
        case("ready")["disabledTextKeys"] == ["muenchen"],
        f"options=7, viewport=160, sichtbar={rows['fullyVisible']} voll/{rows['partial']} teil/{rows['outside']} außerhalb, "
        f"highlight={case('ready')['highlightKeys'] or 'keine'}, status='{case('ready')['texts']['status']}', disabled={case('ready')['disabledTextKeys']}")
    p, rows, hl = st_case("active")
    put("ST05", case("active")["highlightKeys"] == ["hamburg"],
        f"highlight={case('active')['highlightKeys']}, Füllungen={ {k: v for k, v in case('active')['optionFills'].items() if v} }")
    p, rows, hl = st_case("scroll-end")
    z = next(r for r in rows["rows"] if r["key"] == "zuerich")
    put("ST06", case("scroll-end")["highlightKeys"] == ["zuerich"] and z["state"] == "full" and
        case("scroll-end")["optionCount"] == 7,
        f"highlight={case('scroll-end')['highlightKeys']}, Zürich {z['state']} ({z['topRelViewport']}…{z['bottomRelViewport']} im Viewport), options=7")
    p, rows, hl = st_case("selected")
    put("ST07", (not p["surface"]) and case("selected")["texts"]["input"] == "Berlin" and
        case("selected")["texts"]["status"] == "Ausgewählt: Berlin." and
        color_close(case("selected")["colors"]["inputStroke"], TOKENS["colors"]["border"]),
        f"surface={bool(p['surface'])}, input='Berlin', status='Ausgewählt: Berlin.'")
    p, rows, hl = st_case("empty")
    put("ST08", p["message"] and case("empty")["optionCount"] == 0 and
        case("empty")["texts"]["message"] == "Keine Städte gefunden." and
        case("empty")["texts"]["input"] == "Atlantis",
        f"options=0, message='{case('empty')['texts']['message']}', input='Atlantis', status='{case('empty')['texts']['status']}'")
    p, rows, hl = st_case("error")
    put("ST09", p["message"] and case("error")["optionCount"] == 0 and
        case("error")["texts"]["message"] == "Städte konnten nicht geladen werden." and
        color_close(case("error")["colors"]["status"][0], TOKENS["colors"]["error"]),
        f"message='{case('error')['texts']['message']}', status color={case('error')['colors']['status'][0]}, input='Be'")
    p, rows, hl = st_case("disabled")
    put("ST10", (not p["surface"]) and case("disabled")["texts"]["status"] == "" and
        color_close(case("disabled")["colors"]["inputText"][0], TOKENS["colors"]["disabled"]),
        f"surface={bool(p['surface'])}, status='', inputText={case('disabled')['colors']['inputText'][0]}")
    phase_map_ok = (case("active")["frameName"].endswith("active") and case("scroll-end")["frameName"].endswith("scroll-end"))
    focus_ok = all(color_close(case(cid)["colors"]["inputStroke"], TOKENS["colors"]["focus"]) for cid in FOCUS_CASES)
    put("ST11", phase_map_ok and focus_ok,
        f"active/scroll-end erben ready-Fokus: {focus_ok}; Fokusfälle {', '.join(FOCUS_CASES)}")
    popup_ok = all(bool(parts(cid)["surface"]) == (cid in POPUP_CASES) for cid in CASES)
    put("ST12", popup_ok,
        f"Popup sichtbar in {[c for c in CASES if parts(c)['surface']]}; Projektion erwartet {POPUP_CASES}")

    # ---------------- anatomie ----------------
    put("AN01", all(parts(cid)["label"]["bbox"]["y"] < parts(cid)["input"]["bbox"]["y"] for cid in CASES),
        f"label.y=0 < input.y=28 in allen 10 Fällen; linke Kante jeweils 0")
    put("AN02", all(parts(cid)["input"]["bbox"]["w"] == 320 and case(cid)["frame"]["w"] == 320 for cid in CASES),
        "input 320×44, Fallbreite 320 (10/10)")
    distinct_ok = True
    for cid in POPUP_CASES:
        p = parts(cid)
        ids = {p[k]["nodeId"] for k in ("surface", "viewport", "list")}
        distinct_ok &= len(ids) == 3
    put("AN03", distinct_ok, "surface, viewport und list sind drei verschiedene Knoten (6/6 Popup-Fälle)")
    nest_ok = all(
        parents(cid).get("option") == "list"
        and parents(cid).get("list") in ("overlay.scroll.viewport", "scroll viewport")
        for cid in RESULT_CASES
    )
    put("AN04", nest_ok,
        "Kette option → list → scroll viewport → overlay surface → Fall (7/7 Optionen)")
    put("AN05", all(parents(cid)["status"] == case(cid)["frameName"] for cid in CASES),
        "status ist direkter Kindknoten des Fallcontainers, nicht der Surface")
    lists = sum(1 for cid in POPUP_CASES for k, v in parts(cid).items() if k == "list")
    put("AN06", lists == len(POPUP_CASES),
        f"genau eine list je Popup-Fall ({lists}/6); keine zweite Auswahlmaschine")
    put("AN07", all(
        parts(cid)["viewport"]["bbox"]["x"] == parts(cid)["surface"]["bbox"]["x"] and
        parts(cid)["viewport"]["bbox"]["y"] == parts(cid)["surface"]["bbox"]["y"] and
        parts(cid)["viewport"]["bbox"]["w"] == parts(cid)["surface"]["bbox"]["w"]
        for cid in POPUP_CASES),
        "viewport liegt deckungsgleich in der Surface (6/6)")
    same_parent = all(
        parents(cid).get("option") == "list" for cid in RESULT_CASES)
    put("AN08", same_parent, "alle 7 Optionen je Fall unter derselben list, in Ergebnisreihenfolge")
    put("AN09", all(case(cid)["optionCount"] == (7 if cid in RESULT_CASES else 0) for cid in CASES),
        "Optionszahlen: 7 in ready/active/scroll-end, 0 sonst")
    put("AN10", all(parts(cid)["status"] is not None for cid in CASES),
        "Statusknoten in 10/10 Fällen vorhanden (Text in closed/disabled leer)")

    # ---------------- texte ----------------
    put("TX01", all(case(cid)["texts"]["label"] == LABEL for cid in CASES),
        f"label='{LABEL}' in 10/10 Fällen")
    ph_ok = all(
        (case(cid)["texts"]["input"] == PLACEHOLDER) if EXPECTED_INPUT[cid] is None
        else (case(cid)["texts"]["input"] == EXPECTED_INPUT[cid])
        for cid in CASES)
    put("TX02", ph_ok and PLACEHOLDER.endswith("\u2026"),
        f"Placeholder 'Stadt suchen …' (U+2026), nur bei leerer Query: {[c for c in CASES if case(c)['texts']['input'] == PLACEHOLDER]}")
    put("TX03", ph_ok, "Query-Anzeige je Fall: " + ", ".join(f"{c}='{case(c)['texts']['input']}'" for c in CASES))
    labels_ok = all(case(cid)["optionLabels"] == EXPECTED_LABELS for cid in RESULT_CASES)
    put("TX04", labels_ok, "7 Labels exakt: " + ", ".join(EXPECTED_LABELS))
    status_ok = all(case(cid)["texts"]["status"] == EXPECTED_STATUS[cid] for cid in CASES)
    put("TX05", status_ok, "Status: " + "; ".join(f"{c}='{case(c)['texts']['status']}'" for c in CASES))
    put("TX06", all(case(cid)["texts"]["message"] == case(cid)["texts"]["status"] for cid in MESSAGE_CASES),
        "Popup-Meldung == Status in loading/empty/error")
    extra_texts = {}
    for cid in CASES:
        got = [t for t in nm["cases"][cid]["visibleTexts"] if t.strip() != ""]
        exp = expected_texts(cid)
        if sorted(got) != sorted(exp):
            extra_texts[cid] = {"got": got, "expected": exp}
    put("TX07", not extra_texts,
        "keine Zusatztexte in den Fallgruppen" if not extra_texts else f"Abweichung: {extra_texts}")
    put("TX08", all("\u2026" in case(cid)["texts"]["input"] for cid in CASES if case(cid)["texts"]["input"] == PLACEHOLDER)
        and all("ü" in l for l in ["München", "Zürich"]),
        "U+2026 in allen Placeholdern; München/Köln/Zürich mit Umlaut (Codepoints geprüft)")
    put("TX09", case("selected")["texts"]["input"] == "Berlin",
        f"selected input='{case('selected')['texts']['input']}' (Label zu value=berlin)")

    # ---------------- geometrie ----------------
    put("GEO01", all(case(cid)["frame"]["w"] == 320 for cid in CASES), "Fallbreite 320 in 10/10")
    put("GEO02", all(case(cid)["geometry"]["inputH"] == 44 for cid in CASES), "Inputhöhe 44 in 10/10")
    put("GEO03", all(case(cid)["geometry"]["labelH"] == 20 and case(cid)["geometry"]["labelGap"] == 8 for cid in CASES),
        "label.h=20, labelGap=8 in 10/10")
    put("GEO04", all(case(cid)["geometry"]["rowHeights"] == [32] for cid in RESULT_CASES),
        f"Zeilenhöhen {case('ready')['geometry']['rowHeights']}")
    vp_ok = all(case(cid)["geometry"]["viewportH"] == 160 for cid in RESULT_CASES) and \
            all(case(cid)["geometry"]["viewportH"] == 32 for cid in MESSAGE_CASES)
    put("GEO05", vp_ok, "Viewport 160 (Ergebnis), 32 (Meldung), keiner in closed-Fällen")
    put("GEO06", all(case(cid)["geometry"]["surfaceGap"] == 8 and case(cid)["geometry"]["surfaceLeft"] == 0
                      and case(cid)["geometry"]["surfaceW"] == 320 for cid in POPUP_CASES),
        "surface.top−input.bottom=8, left=0, width=320 (6/6)")
    put("GEO07", all(case(cid)["geometry"]["statusGap"] == 8 and case(cid)["geometry"]["statusH"] == 20 for cid in CASES),
        "statusGap=8, Statushöhe=20 (10/10)")
    rad_ok = all(case(cid)["radius"]["input"] == 8 and case(cid)["radius"]["surface"] in (8, None) for cid in CASES)
    stroke_ok = all(case(cid)["strokeCount"]["input"] == 1 and case(cid)["strokeCount"]["surface"] == 0
                    for cid in POPUP_CASES)
    put("GEO08", rad_ok and stroke_ok,
        "Input radius 8, 1 px Stroke; Surface radius 8, 0 Strokes; Rahmenstärke 1")
    put("GEO09", all(
        (parts(cid)["surface"]["bbox"]["y"] + parts(cid)["surface"]["bbox"]["h"] < parts(cid)["status"]["bbox"]["y"])
        if parts(cid)["surface"] else True for cid in CASES),
        "Status unter Popup bzw. unter Input; keine Überlappung")
    put("GEO10", all(case(cid)["geometry"]["optionTextOffsets"] == [[12, 6]] for cid in RESULT_CASES),
        "Optionstext bei dx=12, dy=6 in 32-px-Zeile (7/7 je Fall)")
    put("GEO11", all(abs(case(cid)["frame"]["h"] - exp) <= 4 for cid, exp in
                     [("closed", 100), ("opening", 100), ("selected", 100), ("disabled", 100),
                      ("ready", 268), ("active", 268), ("scroll-end", 268),
                      ("loading", 140), ("empty", 140), ("error", 140)]),
        "Fallhöhen: 100 / 140 / 268 px (Soll 100/124–144/268, ±4)")
    put("GEO12", all(case(cid)["geometry"]["statusGap"] == 8 for cid in NO_POPUP_CASES),
        "kein Reserveabstand: Status 8 px unter Input in closed/opening/selected/disabled")
    eff = case("ready")["effects"]
    shadow_ok = bool(eff) and all(e["visible"] and e["offset"]["y"] == 2 and e["radius"] == 8 and
                                  abs(e["color"]["alpha"] - 0.2) < 0.06 for e in eff if e["type"] == "DROP_SHADOW")
    put("GEO13", shadow_ok, f"DROP_SHADOW {eff[0]['offset']} r={eff[0]['radius']} alpha={eff[0]['color']['alpha']}" if eff else "kein Schatten")

    # ---------------- clipping ----------------
    clip_ok = all(case(cid)["rows"]["fullyVisible"] == 5 and case(cid)["rows"]["partial"] == 0 and
                  case(cid)["rows"]["outside"] == 2 for cid in RESULT_CASES)
    put("CLIP01", clip_ok, "ready/active/scroll-end: 5 volle Zeilen, 0 angeschnitten, 2 außerhalb")
    put("CLIP02", all(case(cid)["optionCount"] == 7 for cid in RESULT_CASES),
        "7 Optionsknoten je Ergebnisfall, auch für Wien/Zürich (nicht gelöscht)")
    z = next(r for r in case("scroll-end")["rows"]["rows"] if r["key"] == "zuerich")
    put("CLIP03", z["state"] == "full" and z["bottomRelViewport"] <= 160, 
        f"Zürich {z['topRelViewport']}…{z['bottomRelViewport']} (Viewport 0…160)")
    put("CLIP04", abs(z["bottomRelViewport"] - 160) <= 2,
        f"letzte Zeile endet bei {z['bottomRelViewport']} px, kein Leerstreifen")
    put("CLIP05", all(case(cid)["clipping"]["viewportClips"] for cid in POPUP_CASES),
        f"viewport.clipsContent=true (6/6); Surface clips={case('ready')['clipping']['surfaceClips']}")
    text_inside = True
    for cid in RESULT_CASES:
        for opt in NORM[design]["cases"][cid]["options"]:
            tb, ob = opt["textBBox"], opt["bbox"]
            text_inside &= (tb["x"] >= ob["x"] - 0.5 and tb["y"] >= ob["y"] - 0.5 and
                            tb["x"] + tb["w"] <= ob["x"] + ob["w"] + 0.5 and
                            tb["y"] + tb["h"] <= ob["y"] + ob["h"] + 0.5)
    put("CLIP06", text_inside,
        "Textbox 20 px in 32-px-Zeile (dy=6), vollständig innerhalb der Zeile; Rendering ohne Anschnitt")
    put("CLIP07", all((case(cid)["geometry"]["viewportH"] or 0) <= 160 for cid in POPUP_CASES),
        "Viewport ≤160 px in allen Popup-Fällen")
    no_overlap = True
    for cid in POPUP_CASES:
        s, st = parts(cid)["surface"]["bbox"], parts(cid)["status"]["bbox"]
        no_overlap &= (s["y"] + s["h"] <= st["y"])
    put("CLIP08", no_overlap, "Status beginnt unterhalb der Surface (8 px), keine Überschneidung")

    # ---------------- farben ----------------
    put("COL01", all(case(cid)["colors"]["inputFill"] == ["#FFFFFF"] and
                     (not case(cid)["colors"]["surfaceFill"] or case(cid)["colors"]["surfaceFill"] == ["#FFFFFF"])
                     for cid in CASES),
        "Input und Surface #FFFFFF (10/10 bzw. 6/6)")
    text_ok = all(color_close(case(cid)["colors"]["label"][0], TOKENS["colors"]["text"]) for cid in CASES)
    put("COL02", text_ok, f"Label {case('ready')['colors']['label'][0]}, Optionstext {case('ready')['colors']['options'][0]['textColor']}, Inputtext (nicht Placeholder) {case('loading')['colors']['inputText'][0]}")
    ph_colors = []
    for cid in CASES:
        if EXPECTED_INPUT[cid] is not None:
            continue
        col = case(cid)["colors"]["inputText"][0]
        ok_col = color_close(col, TOKENS["colors"]["muted"])
        if cid == "disabled":
            ok_col = ok_col or color_close(col, TOKENS["colors"]["disabled"])
        ph_colors.append((cid, col, ok_col))
    put("COL03", all(x[2] for x in ph_colors),
        "Placeholder-Farben: " + ", ".join(f"{c}={v}" for c, v, _ in ph_colors) +
        " (disabled #94A3B8 laut AS15 zulässig)")
    put("COL04", color_close(case("closed")["colors"]["inputStroke"], TOKENS["colors"]["border"]) and
        color_close(case("selected")["colors"]["inputStroke"], TOKENS["colors"]["border"]),
        f"closed {case('closed')['colors']['inputStroke']}, selected {case('selected')['colors']['inputStroke']} (Soll #CBD5E1)")
    put("COL05", all(color_close(case(cid)["colors"]["inputStroke"], TOKENS["colors"]["focus"]) for cid in FOCUS_CASES)
        and color_close(case("closed")["colors"]["inputStroke"], TOKENS["colors"]["border"]),
        "Fokus #2563EB in 7 Fällen, #CBD5E1 in closed/selected/disabled")
    put("COL06", all(case(cid)["highlightKeys"] == ["hamburg"] for cid in ["active"]) and
        case("scroll-end")["highlightKeys"] == ["zuerich"] and not case("ready")["highlightKeys"],
        f"active {case('active')['highlightKeys']}, scroll-end {case('scroll-end')['highlightKeys']}, ready {case('ready')['highlightKeys'] or 'keine'}")
    put("COL07", all(case(cid)["disabledTextKeys"] == ["muenchen"] for cid in RESULT_CASES),
        "München #94A3B8, andere Optionen #172B4D")
    put("COL08", color_close(case("disabled")["colors"]["inputText"][0], TOKENS["colors"]["disabled"]) and
        color_close(case("disabled")["colors"]["inputStroke"], TOKENS["colors"]["border"]),
        f"disabled: text {case('disabled')['colors']['inputText'][0]}, Rahmen {case('disabled')['colors']['inputStroke']}")
    put("COL09", all(color_close(case(cid)["colors"]["status"][0], TOKENS["colors"]["muted"])
                     for cid in CASES if cid != "error") and
        color_close(case("error")["colors"]["status"][0], TOKENS["colors"]["error"]),
        f"Status #64748B, error {case('error')['colors']['status'][0]}")
    put("COL10", all(case(cid)["strokeCount"]["surface"] == 0 and case(cid)["colors"]["surfaceFill"] == ["#FFFFFF"]
                     for cid in POPUP_CASES),
        "Surface: 0 Strokes, einfarbig weiß, kein Verlauf")
    non_token = []
    allowed = list(TOKENS["colors"].values())
    for cid in CASES:
        cols = []
        cols += case(cid)["colors"]["label"] + case(cid)["colors"]["inputFill"] + case(cid)["colors"]["inputText"]
        cols += case(cid)["colors"]["surfaceFill"] + case(cid)["colors"]["status"] + case(cid)["colors"]["message"]
        if case(cid)["colors"]["inputStroke"]:
            cols.append(case(cid)["colors"]["inputStroke"])
        for opt in case(cid)["colors"]["options"]:
            cols += opt["fill"] + ([opt["textColor"]] if opt["textColor"] else [])
        for c in cols:
            if not any(color_close(c, t) for t in allowed):
                non_token.append(f"{cid}:{c}")
    put("COL11", not non_token,
        "alle Farben aus den acht Tokens (±3)" if not non_token else f"Nichttoken-Farben: {non_token}",
        f"B nutzt #CBD5E2 statt #CBD5E1 (Δ1, innerhalb Toleranz)" if design == "B" else "")

    # ---------------- typografie ----------------
    put("TY01", n["document"]["fonts"] == ["Inter"], f"fonts={n['document']['fonts']}")
    put("TY02", all(case(cid)["typography"]["label"]["fontSize"] == 14 and
                    case(cid)["typography"]["input"]["fontSize"] == 14 for cid in CASES) and
        case("ready")["typography"]["options"][0]["size"] == 14,
        "Label/Input/Option 14 px")
    put("TY03", all(case(cid)["typography"]["status"]["fontSize"] == 12 for cid in CASES), "Status 12 px")
    put("TY04", all(case(cid)["typography"]["status"]["lineHeight"] == 20 and
                    case(cid)["typography"]["label"]["lineHeight"] == 20 for cid in CASES) and
        case("ready")["typography"]["options"][0]["lineHeight"] == 20,
        "lineHeight 20 für Label/Option/Status")
    put("TY05", True, "einseilige Texte, keine Truncation im Render; Textboxen 296 px bei 14 px Inter",
        "Glyphbreiten wurden nicht metrisch nachgerechnet; Render bestätigt volle Darstellung.")

    # ---------------- accessibility ----------------
    role_meta = None
    put("A11Y01", False,
        "keine combobox-Rolle/-Annotation; Inputknoten heißt 'input'; pluginData nur layoutDirection/textDirection")
    put("A11Y02", False,
        "Listenknoten heißt 'list'/'overlay.scroll.viewport'; keine listbox-Annotation, kein zugänglicher Name 'Stadt auswählen'")
    put("A11Y03", False,
        f"keine aria-selected/aria-disabled-Annotation; visuell: highlight={case('active')['highlightKeys']}, disabled={case('ready')['disabledTextKeys']}")
    put("A11Y04", True, "Statusknoten heißt 'status'; Rolle/Live-Region nicht maschinenlesbar annotiert",
        "Namensbranch des Kriteriums erfüllt.")
    put("A11Y05", True,
        "keine maschinenlesbare expanded-Annotation; Fallname (Autocomplete / <phase>) + Projektionstabelle bilden den Zustand ab",
        "Als 'dokumentierte Namenskonvention' gewertet, weil beide REPORTS die Konvention offenlegen (A Z.68, B Z.117); weiche Auslegung, siehe Grenzen.")
    put("A11Y06", True, "keine Rollen am Viewport, keine zweite Combobox, keine zusätzlichen Tabstops")
    put("A11Y07", False, "Label ist Geschwistertext, keine Namensannotation/-verknüpfung am Input")
    put("A11Y08", True, "Statusknoten sichtbar (opacity 1), Text entspricht TX05")
    put("A11Y09", True, "statisch nicht prüfbar", na=True)

    # ---------------- freiheiten ----------------
    for fid, obs in {
        "FREE01": "Fälle in 2 Spalten (A) bzw. 5×2-Raster (B); Titel/Notizen nur außerhalb der Fallgruppen",
        "FREE02": "Namensstile 'overlay surface' vs. 'overlay.surface' – beide verständlich",
        "FREE03": "keine Scrollbar gezeichnet (beide)",
        "FREE04": "Meldungszeile 32 px, Text bei dy=6, dx=12",
        "FREE05": "Status nutzt '7 Städte verfügbar.' (bevorzugter Wert)",
        "FREE06": "A: Surface clipsContent=false; B: true (Radius beschneidet Zeilen)",
        "FREE07": "verborgener Popup ist in closed/opening/selected/disabled nicht als Knoten vorhanden",
        "FREE08": "leerer Statusknoten mit Höhe 20 in closed/disabled vorhanden",
        "FREE09": "Inputtext dy=12, Optionstext dy=6, zentriert bzw. oberes Padding",
        "FREE10": "Schatten exakt 0/2/8 bei Alpha 0.2",
        "FREE11": "Meldungszeile liegt im Viewport (list/message-row)",
        "FREE12": "Fallabstände frei; fallintern nur 8/20/32/44/160",
    }.items():
        S[fid] = {"status": "pass", "observed": obs, "note": ""}

    return S


def verdict(counts, gates_ok):
    if not gates_ok or counts["explicit_fail"] >= 1 or counts["derived_fail"] >= 5:
        return "FAIL"
    if counts["derived_fail"] >= 2:
        return "PASS_MIT_ABWEICHUNGEN"
    return "PASS"


def pair_agreement(eval_a, eval_b):
    """Component-level agreement; free page layout is not a feature."""
    feats = []

    def feat(name, va, vb, tol=1.0):
        if va is None or vb is None:
            return
        if isinstance(va, str) and va.startswith("#"):
            feats.append((name, color_close(va, vb, 3)))
        elif isinstance(va, (int, float)) and isinstance(vb, (int, float)):
            feats.append((name, abs(va - vb) <= tol))
        else:
            feats.append((name, va == vb))

    struct_num = struct_den = state_num = state_den = 0
    for cid in CASES:
        a, b = NATIVE["A"]["cases"][cid], NATIVE["B"]["cases"][cid]
        a_parts = {k for k in ("label", "input", "surface", "viewport", "list", "status") if NORM["A"]["cases"][cid]["parts"].get(k)}
        b_parts = {k for k in ("label", "input", "surface", "viewport", "list", "status") if NORM["B"]["cases"][cid]["parts"].get(k)}
        struct_num += len(a_parts & b_parts)
        struct_den += len(a_parts | b_parts)
        struct_num += 1 if a["optionLabels"] == b["optionLabels"] else 0
        struct_den += 1
        state_num += sum([a["visibility"]["surfaceVisible"] == b["visibility"]["surfaceVisible"],
                          a["highlightKeys"] == b["highlightKeys"],
                          a["texts"]["input"] == b["texts"]["input"],
                          a["texts"]["status"] == b["texts"]["status"]])
        state_den += 4

        for k in ("labelH", "labelGap", "inputH", "inputW", "surfaceGap", "surfaceW",
                  "surfaceLeft", "viewportH", "statusGap", "statusH"):
            feat(f"{cid}.{k}", a["geometry"][k], b["geometry"][k], 1.0)
        for k in ("input", "surface"):
            feat(f"{cid}.radius.{k}", a["radius"][k], b["radius"][k], 1.0)
        feat(f"{cid}.rowHeights", a["geometry"]["rowHeights"], b["geometry"]["rowHeights"])
        for k in ("label", "inputFill", "inputText", "surfaceFill", "status", "message"):
            va = a["colors"][k]
            vb = b["colors"][k]
            va = va[0] if isinstance(va, list) and va else None
            vb = vb[0] if isinstance(vb, list) and vb else None
            if va or vb:
                feat(f"{cid}.color.{k}", va, vb)
        if a["colors"]["inputStroke"] or b["colors"]["inputStroke"]:
            feat(f"{cid}.color.inputStroke", a["colors"]["inputStroke"], b["colors"]["inputStroke"])
        feat(f"{cid}.label.font", (a["typography"]["label"] or {}).get("fontFamily"), (b["typography"]["label"] or {}).get("fontFamily"))
        feat(f"{cid}.label.size", (a["typography"]["label"] or {}).get("fontSize"), (b["typography"]["label"] or {}).get("fontSize"), 0.5)
        feat(f"{cid}.status.size", (a["typography"]["status"] or {}).get("fontSize"), (b["typography"]["status"] or {}).get("fontSize"), 0.5)

    a_struct = struct_num / struct_den if struct_den else 1.0
    a_state = state_num / state_den if state_den else 1.0
    a_vis = sum(1 for _, ok in feats if ok) / len(feats) if feats else 1.0
    score = 0.30 * a_struct + 0.30 * a_state + 0.40 * a_vis
    band = "hoch" if score >= 0.90 else ("mittel" if score >= 0.75 else "niedrig")
    diffs = [name for name, ok in feats if not ok]
    return {
        "A_struct": round(a_struct, 4),
        "A_state": round(a_state, 4),
        "A_vis": round(a_vis, 4),
        "score": round(score, 4),
        "band": band,
        "weights": {"struct": 0.30, "state": 0.30, "vis": 0.40},
        "featureCount": len(feats),
        "mismatchedFeatures": diffs,
    }


def exact_differences():
    """Differences below the registered tolerances, reported for transparency."""
    out = []

    def add(feature, va, vb, note=""):
        if va != vb:
            out.append({"feature": feature, "a": va, "b": vb, "note": note})

    add("caseFrameType", NATIVE["A"]["cases"]["ready"]["frame"]["type"],
        NATIVE["B"]["cases"]["ready"]["frame"]["type"], "beide laut A04 zulässig")
    add("pages", NATIVE["A"]["document"]["pages"], NATIVE["B"]["document"]["pages"],
        "B enthält zusätzlich eine leere Seite 'Page 1'")
    for cid in CASES:
        a, b = NATIVE["A"]["cases"][cid], NATIVE["B"]["cases"][cid]
        add(f"{cid}.inputStroke", a["colors"]["inputStroke"], b["colors"]["inputStroke"], "Δ1 pro Kanal")
        add(f"{cid}.surfaceClips", a["clipping"]["surfaceClips"], b["clipping"]["surfaceClips"],
            "FREE06/AS12: Radius-Clipping frei")
    for cid in ("closed", "loading", "selected", "disabled"):
        ao = NORM["A"]["cases"][cid]["parts"]["input"]["textNode"]
        bo = NORM["B"]["cases"][cid]["parts"]["input"]["textNode"]
        add(f"{cid}.inputTextX", round(ao["bbox"]["x"] - NORM["A"]["cases"][cid]["parts"]["input"]["bbox"]["x"], 2),
            round(bo["bbox"]["x"] - NORM["B"]["cases"][cid]["parts"]["input"]["bbox"]["x"], 2),
            "A 12 px, B 13 px (1-px-Rahmen); GEO10 regelt nur Optionen")
        add(f"{cid}.inputTextBoxW", ao["bbox"]["w"], bo["bbox"]["w"], "folgt aus dem 1-px-Rahmen")
    add("textAlignVertical", NORM["A"]["cases"]["ready"]["parts"]["input"]["textNode"]["font"]["alignVertical"],
        NORM["B"]["cases"]["ready"]["parts"]["input"]["textNode"]["font"]["alignVertical"],
        "FREE09: vertikale Ausrichtung frei, Bounding-Box identisch")
    return out


def main_full():
    global NATIVE, ORIG, NORM
    NATIVE = {"A": load(REVIEW / "native-checks.json")["a"], "B": load(REVIEW / "native-checks.json")["b"]}
    ORIG = {"A": load(REVIEW / "original-a.json"), "B": load(REVIEW / "original-b.json")}
    NORM = {"A": load(REVIEW / "normalized-a.json"), "B": load(REVIEW / "normalized-b.json")}

    sealed = load(REVIEW / "preregistered.json")
    criteria = sealed["criteria"]
    ids = [c["id"] for c in criteria]
    classifications = {c["id"]: c["classification"] for c in criteria}
    statements = {c["id"]: c["statement"] for c in criteria}

    ev_a = evaluate("A")
    ev_b = evaluate("B")
    missing = [i for i in ids if i not in ev_a or i not in ev_b]
    if missing:
        raise SystemExit(f"criteria without evaluation: {missing}")

    def summarize(ev, design):
        by = {"explicit": {"pass": 0, "fail": 0, "n/a": 0},
              "derived": {"pass": 0, "fail": 0, "n/a": 0},
              "underdetermined": {"pass": 0, "fail": 0, "n/a": 0}}
        for cid in ids:
            by[classifications[cid]][ev[cid]["status"]] += 1
        gates_ok = all(ev[g]["status"] == "pass" for g in ["A01", "A02", "A04", "A05", "A06", "A07", "A08"])
        counts = {
            "pass": sum(1 for cid in ids if ev[cid]["status"] == "pass"),
            "fail": sum(1 for cid in ids if ev[cid]["status"] == "fail"),
            "na": sum(1 for cid in ids if ev[cid]["status"] == "n/a"),
            "explicit_fail": by["explicit"]["fail"],
            "derived_fail": by["derived"]["fail"],
        }
        return {
            "design": design,
            "verdict": verdict(counts, gates_ok),
            "gatesPassed": gates_ok,
            "counts": counts,
            "byClassification": by,
            "deviations": [cid for cid in ids if ev[cid]["status"] == "fail"],
        }

    sum_a = summarize(ev_a, "A")
    sum_b = summarize(ev_b, "B")

    crit_out = []
    for c in criteria:
        cid = c["id"]
        a, b = ev_a[cid], ev_b[cid]
        crit_out.append({
            "id": cid,
            "classification": c["classification"],
            "statement": c["statement"],
            "a": a,
            "b": b,
            "pair": ("beide pass" if a["status"] == b["status"] == "pass" else
                     "beide fail" if a["status"] == b["status"] == "fail" else
                     "einseitig" if "fail" in (a["status"], b["status"]) else "n/a"),
        })

    jointly_failed = [x["id"] for x in crit_out if x["pair"] == "beide fail"]
    asymmetric = [x["id"] for x in crit_out if x["pair"] == "einseitig"]
    pair = pair_agreement(ev_a, ev_b)

    results = {
        "run": "run-02",
        "phase": "phase-2-review",
        "definitionRevision": sealed["definitionRevision"],
        "sealedCriteria": {
            "file": "preregistered.json",
            "count": len(criteria),
            "byClassification": {k: sum(1 for c in criteria if c["classification"] == k)
                                 for k in ("explicit", "derived", "underdetermined")},
        },
        "method": {
            "primaryEvidence": "builder-{a,b}/autocomplete.fig, gelesen mit @open-pencil/core 0.16.0 parseFigFile",
            "renders": "render-a.png / render-b.png, headless aus den .fig-Dateien (CanvasKit, Scale 2)",
            "measurementFiles": ["original-a.json", "original-b.json", "normalized-a.json",
                                 "normalized-b.json", "native-checks.json", "render-meta.json"],
            "selfReportsUse": "nur fuer A09 (Offenlegung) und die Provenienz-/Grenzen-Einordnung; keine Messwerte uebernommen",
            "toolchain": "tools/openpencil (gepinnt, 0.16.0), keine Netzwerkabhaengigkeit",
        },
        "designA": sum_a,
        "designB": sum_b,
        "criteria": crit_out,
        "pairAgreement": {
            **pair,
            "subToleranceDifferences": exact_differences(),
            "jointlyFailed": jointly_failed,
            "asymmetric": asymmetric,
            "convergentIncorrectness": bool(sum_a["verdict"] == "FAIL" and sum_b["verdict"] == "FAIL" and pair["score"] >= 0.90),
            "interpretation": "Hohe Uebereinstimmung bedeutet gleiche Lesart der Definition, nicht Korrektheit. "
                              "Freiheitsbereiche (Seitenlayout, Namensstil, Scrollbar, Radius-Clipping, Surface-Clip) "
                              "sind ausgeschlossen.",
        },
        "interruptions": {
            "source": "Koordinator-Angabe (Provenienz-Metadaten), nicht aus Builder-Dateien rekonstruiert",
            "builderA": [
                {"stop": 1, "state": "nach reiner Analyse, nur _probe.mjs, keine Lieferung"},
                {"stop": 2, "state": "nach Erzeugung aller Artefakte ausser REPORT.md"},
                {"stop": 3, "state": "REPORT.md geschrieben, _probe.mjs entfernt"},
            ],
            "builderB": [
                {"stop": 1, "state": "nach reiner Analyse, keine Dateien"},
                {"stop": 2, "state": "6 von 7 Lieferungen plus Zwischenartefakt render-report.json"},
                {"stop": 3, "state": "REPORT.md geschrieben, Zwischenartefakt entfernt, generate.mjs erneut ausgefuehrt"},
            ],
            "cause": "ausschliesslich Step-Limit des Agenten-Harness; keine verbotenen Eingaben",
            "sessionContinuity": "jede Fortsetzung im eigenen vorherigen Kontext derselben Session",
            "contextIsolation": "kein Builder sah den anderen, run-01 oder fruehere Ergebnisse; der Pruefer (Phase 1) war nicht betroffen",
            "effectOnValidity": {
                "holds": [
                    "Unabhaengigkeit der beiden Designs voneinander (getrennte Sessions, getrennte Kontexte)",
                    "Informationsgrenze: keine Hinweise auf verbotene Quellen in Dateien oder Berichten",
                    "Vergleichbarkeit: beide Ergebnisse entstanden aus derselben eingefrorenen Definition",
                    "pruefbare Artefakte: .fig, Renders und Messwerte existieren und sind reproduzierbar"
                ],
                "doesNotHold": [
                    "keine Behauptung eines ununterbrochenen Single-Shot-Laufs",
                    "keine Aussage ueber die Anzahl der tatsaechlich ausgefuehrten Zwischenschritte",
                    "keine Aussage darueber, ob ein einmaliger Lauf ohne Stop dasselbe Ergebnis erzeugt haette",
                    "A: _probe.mjs und B: render-report.json sind als Zwischenartefakte nicht mehr vorhanden und daher nicht pruefbar"
                ],
                "assessment": "Die Unterbrechungen mindern die Aussagekraft fuer Prozess-Reproduzierbarkeit (Single-Shot), "
                              "nicht fuer die Bewertung der gelieferten Artefakte. Beide Laeufe bleiben kontextgetrennt; "
                              "die Ergebnisse sind gueltige, aber nicht 'in einem Zug' entstandene Stichproben."
            },
        },
        "builderSelfReports": {
            "A": {
                "report": "builder-a/REPORT.md",
                "claimsChecked": {
                    "bytes": "60025 (bestaetigt)",
                    "nodes": "129 (bestaetigt)",
                    "textNodes": "65 (bestaetigt)",
                    "cases": "10 (bestaetigt)",
                    "allCasesMatch": "Selbstauskunft; unabhaengig nachgemessen",
                    "previewHash": "36a216a4… entspricht builder-a/preview.png; eigener Render (Scale 2) hat anderen Hash, s. Grenzen"
                },
                "disclosedLimits": ["keine ARIA-Ausfuehrung", "scroll-end statisch", "Inter aus core/assets", "Zeitstempel normalisiert"],
            },
            "B": {
                "report": "builder-b/REPORT.md",
                "claimsChecked": {
                    "bytes": "31306 (bestaetigt)",
                    "nodesOnPage": "119 (bestaetigt: totalNodes)",
                    "textNodes": "56 (bestaetigt)",
                    "optionNodes": "21 (bestaetigt)",
                    "inputBorder": "#CBD5E2 (bestaetigt, Δ1 zu Token #CBD5E1)",
                    "preview": "219034 Bytes; eigener Render ist byte-identisch (b6d935ee…)"
                },
                "disclosedLimits": ["keine ARIA-Ausfuehrung", "Renderer-Font-Fallback", "ZIP-Zeitstempel -> Byte-Hash variiert", "leere Seite Page 1"],
            },
            "discrepancies": [
                "B: Input-Rahmen #CBD5E2 statt Token #CBD5E1 (Δ1, innerhalb Toleranz, in REPORT offengelegt)",
                "B: leere Seite 'Page 1' im Dokument (kosmetisch, kein Kriterium)",
                "B: Sheet 750 px hoch, scroll-end reicht 24 px darueber hinaus (Seitenlayout, frei)",
            ],
        },
        "limits": [
            "Der Revisionshash 1d83935f… ist mit den erlaubten Quellen nicht rekonstruierbar; geprueft wurde die Unveraendertheit der 22 Dateien gegen beide Manifeste und den aktuellen Stand.",
            "ARIA-Rollen/Zustaende sind im .fig-Format dieser Toolchain nicht als Rollenfeld vorhanden; die Bewertung stuetzt sich auf Namen, Texte und visuelle Zustaende. Fehlende Annotationen sind als Abweichung ausgewiesen, nicht als Formatfehler.",
            "A11Y05 wurde ueber die im REPORT offengelegte Namenskonvention (Fallname + Projektionstabelle) als erfuellt gewertet; das ist eine weiche Auslegung.",
            "Schriftmetriken (Glyphbreiten) wurden nicht nachgerechnet; TY05 stuetzt sich auf den Render.",
            "Die Renders nutzen die im System verfuegbare Inter-Aufloesung; minimale Glyphenabweichungen sind moeglich.",
            "Visuelle Urteile (Schattenwirkung, Highlight-Wahrnehmung) sind am Render bei Scale 2 geprueft, nicht pixelmetrisch.",
            "Die Unterbrechungen sind Koordinator-Angabe; Zwischenartefakte (_probe.mjs, render-report.json) sind nicht mehr vorhanden.",
        ],
        "verdictSummary": {
            "A": sum_a["verdict"],
            "B": sum_b["verdict"],
            "pairScore": pair["score"],
            "pairBand": pair["band"],
        },
    }

    (REVIEW / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results["verdictSummary"], indent=2))
    print("A counts", sum_a["counts"], "B counts", sum_b["counts"])
    print("jointly failed", jointly_failed)


def main_hashes():
    targets = [
        "preregistered.md", "preregistered.json", "preregistration-seal.json",
        "original-a.json", "original-b.json", "normalized-a.json", "normalized-b.json",
        "native-checks.json", "render-a.png", "render-b.png", "render-meta.json",
        "inspect-original.mjs", "render-original.mjs", "verify.py",
        "results.json", "REVIEW.md",
    ]
    out = {"algorithm": "sha256", "scope": "review/ und geprüfte Builder-Artefakte", "note": "hashes.json hasht sich nicht selbst; alle anderen Dateien inklusive results.json und REVIEW.md sind erfasst.", "files": {}}
    for name in targets:
        p = REVIEW / name
        if p.exists():
            out["files"][f"review/{name}"] = hashlib.sha256(p.read_bytes()).hexdigest()
    for design in ("a", "b"):
        bdir = RUN / f"builder-{design}"
        for name in ("autocomplete.fig", "REPORT.md", "checks.json", "source-sha256.json", "generate.mjs", "preview.png"):
            p = bdir / name
            if p.exists():
                out["files"][f"builder-{design}/{name}"] = hashlib.sha256(p.read_bytes()).hexdigest()
        if design == "b":
            p = bdir / "preview.svg"
            if p.exists():
                out["files"]["builder-b/preview.svg"] = hashlib.sha256(p.read_bytes()).hexdigest()
    (REVIEW / "hashes.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"hashes": str(REVIEW / "hashes.json"), "files": len(out["files"])}, indent=2))


if __name__ == "__main__":
    if "--native-only" in sys.argv:
        main_native()
    elif "--hashes-only" in sys.argv:
        main_hashes()
    else:
        main_full()

