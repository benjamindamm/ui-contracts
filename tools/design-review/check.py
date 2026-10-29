#!/usr/bin/env python3
"""Bounded AC static counter-check. Does not replace historical run reviews.

Exit: 0 PASS_LIMITED, 1 measured FAIL, 2 BLOCKED. No production/AX release.
Only the exact profile-bound definition/toolchain is supported. Reads real FIGs.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CASES = ['closed', 'opening', 'loading', 'ready', 'active', 'scroll-end', 'selected', 'empty', 'error', 'disabled']
RESULTS = {'ready', 'active', 'scroll-end'}
POPUP = RESULTS | {'loading', 'empty', 'error'}
FOCUS = POPUP | {'opening'}

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load(p):
    return json.loads(p.read_text())

def example_root(repo):
    migrated = repo/'libraries/example'
    return migrated if (migrated/'library.json').is_file() else repo/'components'

def profile_gate(repo, profile):
    errors = []
    for name, expected in profile['definitionFiles'].items():
        p = example_root(repo) / name
        if not p.is_file() or digest(p) != expected:
            errors.append('SOURCE_PROFILE_MISMATCH:' + name)
    lock = repo / 'tools/openpencil/package-lock.json'
    if not lock.is_file() or digest(lock) != profile['toolchainPackageLockSha256']:
        errors.append('TOOLCHAIN_PROFILE_MISMATCH')
    return errors

def token(tokens, name):
    cur = tokens
    for key in name.split('.'):
        cur = cur[key]
    v = cur['$value']
    if isinstance(v, str) and v.startswith('{'):
        return token(tokens, v[1:-1])
    return v

def color(paint):
    if not paint or paint.get('visible') is False or paint.get('type') != 'SOLID':
        return None
    c = paint.get('color') or {}
    return '#' + ''.join(f'{round(c[k]*255):02X}' for k in 'rgb')

def fill(n):
    paints = [p for p in (n.get('fills') or []) if p.get('visible') is not False]
    return color(paints[0]) if len(paints) == 1 else None

def assess(nodes, tokens, stories, rules):
    by_id = {n['id']: n for n in nodes}
    checks, features = [], {}
    def put(key, actual, expected, kind='exact', source='components/'):
        status = 'pass' if actual == expected else 'fail'
        if kind == 'dimension' and isinstance(actual, (int, float)) and abs(actual-expected) <= 0.01:
            status = 'pass'
        # Token channels are discrete inputs; retain even one-channel drift as warning.
        if kind == 'color' and status == 'fail' and isinstance(actual, str) and re.fullmatch(r'#[0-9A-F]{6}', actual):
            delta = max(abs(int(actual[i:i+2],16)-int(expected[i:i+2],16)) for i in (1,3,5))
            if delta <= 3:
                status = 'warning'
        features[key] = actual
        checks.append({'id': key, 'actual': actual, 'expected': expected, 'status': status, 'source': source})
    def desc(n):
        out = []
        def walk(p, seen):
            if p['id'] in seen:
                raise ValueError('Cycle in native tree')
            seen = seen | {p['id']}
            for cid in p.get('childIds') or []:
                child = by_id[cid]
                out.append(child)
                walk(child, seen)
        walk(n, set())
        return out
    def visible(n):
        seen = set()
        while n:
            if n['id'] in seen:
                return False
            seen.add(n['id'])
            if n.get('visible') is False or (n.get('opacity') is not None and n['opacity'] <= 0):
                return False
            n = by_id.get(n.get('parentId'))
        return True
    def dim(key):
        v = token(tokens, 'autocomplete.' + key)
        if v['unit'] != 'px':
            raise ValueError('Unsupported unit')
        return v['value']
    def col(key):
        t = token(tokens, 'autocomplete.' + key)
        if t['colorSpace'] != 'srgb' or t['alpha'] != 1:
            raise ValueError('Unsupported color')
        return '#' + ''.join(f'{round(x*255):02X}' for x in t['components'])
    def one(seq, key):
        put(key + '.count', len(seq), 1)
        return seq[0] if len(seq) == 1 else None
    all_frames = [n for n in nodes if n['type'] in ('FRAME', 'COMPONENT')]
    case_nodes = {c: [n for n in all_frames if n['name'].lower().strip() in (c, 'autocomplete / '+c)] for c in CASES}
    for cid in CASES:
        frame = one(case_nodes[cid], cid)
        if not frame:
            continue
        ns = desc(frame)
        put(cid+'.visible', visible(frame), True)
        put(cid+'.width', frame['width'], dim('width'), 'dimension')
        put(cid+'.lockedNodeCount', sum(bool(n.get('locked')) for n in [frame]+ns), 0)
        inp = one([n for n in ns if n['type'] != 'TEXT' and re.match(r'^input(?:$|\s|[·])', n['name'], re.I)], cid+'.input')
        label = one([n for n in ns if n['type'] == 'TEXT' and n['name'] == 'label'], cid+'.label')
        status = one([n for n in ns if n['type'] == 'TEXT' and re.match(r'^status(?:$|\s|[·])', n['name'], re.I)], cid+'.status')
        if not inp or not label or not status:
            continue
        for part, node in [('input', inp), ('label', label), ('status', status)]:
            put(cid+'.'+part+'.visible', visible(node), True)
        texts = [n for n in desc(inp) if n['type'] == 'TEXT']
        text = one(texts, cid+'.inputText')
        story = stories[cid]
        query = story['inputs'].get('query', '')
        expected_input = query or 'Stadt suchen …'
        if cid == 'selected':
            expected_input = 'Berlin'
        put(cid+'.label.text', label['text'], 'Stadt auswählen')
        put(cid+'.input.height', inp['height'], dim('inputHeight'), 'dimension')
        put(cid+'.input.radius', inp['cornerRadius'], dim('radius'), 'dimension')
        put(cid+'.input.fill', fill(inp), col('surface'), 'color')
        strokes = [s for s in inp.get('strokes') or [] if s.get('visible') is not False]
        put(cid+'.input.stroke.count', len(strokes), 1)
        if len(strokes) == 1:
            put(cid+'.input.stroke.weight', strokes[0].get('weight'), dim('borderWidth'), 'dimension')
            put(cid+'.input.stroke.color', color(strokes[0]), col('focus' if cid in FOCUS else 'border'), 'color')
        if text:
            put(cid+'.inputText.visible', visible(text), True)
            put(cid+'.inputText.text', text['text'], expected_input)
            # Explicit ::placeholder applies independently of :disabled's own color.
            put(cid+'.inputText.color', fill(text), col('muted' if not query and cid != 'selected' else 'text'), 'color', 'components/autocomplete/layout.css:32-33')
        case_texts = [n for n in ns if n['type'] == 'TEXT']
        features[cid+'.textCount'] = len(case_texts)
        for index, t in enumerate(case_texts):
            key = cid+f'.text{index}'
            put(key+'.fontFamily', t['fontFamily'], token(tokens, 'autocomplete.fontFamily'))
            put(key+'.fontSize', t['fontSize'], dim('statusFontSize' if t['id'] == status['id'] else 'fontSize'), 'dimension')
            put(key+'.lineHeight', t['lineHeight'], dim('lineHeight'), 'dimension')
        put(cid+'.label.color', fill(label), col('text'), 'color')
        put(cid+'.status.color', fill(status), col('error' if cid == 'error' else 'muted'), 'color')
        expected_status = rules['messages'].get(cid)
        if cid in RESULTS:
            expected_status = rules['messages']['results'].replace('{count}', '7')
        if cid == 'selected':
            expected_status = rules['messages']['selected'].replace('{label}', 'Berlin')
        put(cid+'.status.text', status['text'], expected_status)
        surfaces = [n for n in ns if n['type'] != 'TEXT' and 'surface' in n['name'].lower() and visible(n)]
        put(cid+'.surface.visibleCount', len(surfaces), int(cid in POPUP))
        if cid not in POPUP:
            continue
        viewport = one([n for n in ns if n['type'] != 'TEXT' and 'viewport' in n['name'].lower() and visible(n)], cid+'.viewport')
        if viewport:
            put(cid+'.viewport.clipsContent', viewport['clipsContent'], True)
            put(cid+'.viewport.height', viewport['height'], dim('maxHeight') if cid in RESULTS else dim('rowHeight'), 'dimension')
        options = [n for n in ns if n['type'] != 'TEXT' and re.match(r'^option(?:\s|/)', n['name'], re.I)]
        put(cid+'.options.count', len(options), 7 if cid in RESULTS else 0)
        if cid in RESULTS:
            records = story['results']
            for index, opt in enumerate(options):
                ot = one([n for n in desc(opt) if n['type'] == 'TEXT'], cid+f'.option{index}.text')
                if index >= len(records):
                    continue
                record = records[index]
                put(cid+f'.option{index}.visible', visible(opt), True)
                put(cid+f'.option{index}.height', opt['height'], dim('rowHeight'), 'dimension')
                if ot:
                    put(cid+f'.option{index}.label', ot['text'], record['label'])
                    put(cid+f'.option{index}.color', fill(ot), col('disabled' if record.get('disabled') else 'text'), 'color')
    # No score: compare every recorded observation by its semantic key in compare().
    failures = [c for c in checks if c['status'] == 'fail']
    warnings = [c for c in checks if c['status'] == 'warning']
    return {'overall': 'FAIL' if failures else 'PASS_LIMITED', 'release': False,
            'covered': ['case/part presence', 'native locks', 'visible popup projection', 'input sizes/radius/stroke',
                        'text/placeholder/status colors', 'every text font/size/lineHeight', 'option records/heights', 'viewport clipping flag/height'],
            'notChecked': ['full geometry and scroll offsets', 'shadows', 'rendered glyph metrics', 'static semantic annotations',
                           'GUI edit-save roundtrip', 'runtime behavior and accessibility', 'process independence'],
            'checks': checks, 'failures': failures, 'warnings': warnings, 'features': features}

def compare(a, b):
    keys = sorted(set(a) | set(b))
    different = [{'key': k, 'aPresent': k in a, 'bPresent': k in b, 'a': a.get(k), 'b': b.get(k)}
                 for k in keys if k not in a or k not in b or a[k] != b[k]]
    return {'compared': len(keys), 'matched': len(keys)-len(different), 'differences': different,
            'meaning': 'Exact equality of covered semantic observations only; missing fields are differences, not skipped. No overall similarity score.'}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--repo', type=Path, default=ROOT)
    p.add_argument('--run', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    repo, run = args.repo.resolve(), args.run.resolve()
    output = args.output.resolve()
    if (output.is_relative_to(run) or output.is_relative_to(repo/'components') or output.is_relative_to(repo/'libraries') or
            output.is_relative_to(repo/'examples/autocomplete/reproducibility')):
        p.error('Output must be outside the historical run and frozen definitions')
    profile = load(HERE/'profile.json')
    errors = profile_gate(repo, profile)
    runmeta = load(run/'run.json')
    if runmeta['definitionFiles'] != profile['definitionFiles']:
        errors.append('RUN_INPUT_PROFILE_MISMATCH')
    out = {'profile': profile['id'], 'release': False, 'scope': 'bounded-static-autocomplete-countercheck', 'definitionRoot': str(example_root(repo)), 'sourceLocatorConvention': 'components/ locators retained from the frozen historical profile; see definitionRoot for current location', 'blocked': errors}
    if not errors:
        try:
            stories_data = load(example_root(repo)/'autocomplete/stories.json')
            stories = {s['id']: s for s in stories_data['stories']}
            tokens = load(example_root(repo)/'tokens.json')
            rules = load(example_root(repo)/'autocomplete/accessibility.rules.json')
            out['designs'] = {}
            for x in 'ab':
                fig = run/f'builder-{x}/autocomplete.fig'
                proc = subprocess.run(['node', str(HERE/'read-fig.mjs'), str(repo), str(fig)], capture_output=True, text=True, check=True, timeout=60)
                result = assess(json.loads(proc.stdout)['nodes'], tokens, stories, rules)
                result['artifactSha256'] = digest(fig)
                out['designs'][x] = result
            out['pair'] = compare(*(out['designs'][x]['features'] for x in 'ab'))
        except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as e:
            out['blocked'].append(str(e))
    out['overall'] = 'BLOCKED' if out['blocked'] else ('FAIL' if any(d['overall']=='FAIL' for d in out['designs'].values()) else 'PASS_LIMITED')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'overall':out['overall'], 'release':False, 'output':str(output), 'blocked':out['blocked']}))
    return {'PASS_LIMITED':0,'FAIL':1,'BLOCKED':2}[out['overall']]

if __name__ == '__main__':
    raise SystemExit(main())
