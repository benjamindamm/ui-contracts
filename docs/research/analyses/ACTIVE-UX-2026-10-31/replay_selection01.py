"""External replay of the unchanged SELECTION-01 helper against its preserved library input.
The historical helper retains its original runtime prerequisites and locator labels.
"""
from pathlib import Path
import importlib.util
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
STUDY = ROOT / 'docs/research/studies/UX-RULES-01/studies/SELECTION-01'
SNAPSHOT = ROOT / 'docs/libraries/frozen/example-selection-01'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def replay():
    freeze = json.loads((STUDY / 'freeze.json').read_text())
    helper = STUDY / 'evaluate.py'
    if sha(helper) != freeze['files'][str(helper.relative_to(ROOT))]:
        raise ValueError('Historical helper changed')
    manifest = json.loads((STUDY / 'library-manifest.json').read_text())
    if any(sha(SNAPSHOT / name) != h for name, h in manifest['files'].items()):
        raise ValueError('Preserved input changed')
    spec = importlib.util.spec_from_file_location('historical_selection01', helper)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    # Relocate the data root only, not policy, assertions, helper code or expected outcomes.
    module.LIB = SNAPSHOT
    results = {arm: module.evaluate(json.loads((STUDY / f'inputs/{arm}.json').read_text())) for arm in ['a', 'b']}
    expected = {'a': 'Select', 'b': 'Autocomplete'}
    for arm in results:
        if results[arm].get('assessment', {}).get('choice') != expected[arm]:
            raise ValueError('Historical replay failed: ' + arm + str(results[arm]))
    return {'scope': 'Historical policy replay with relocated byte-identical data only', 'release': False,
            'helperUnchanged': True, 'snapshotRoot': str(SNAPSHOT.relative_to(ROOT)), 'filesMatched': len(manifest['files']),
            'locatorNote': 'policySource labels in original results keep the historical library locator; effective root is snapshotRoot.',
            'results': results}


if __name__ == '__main__': print(json.dumps(replay(), ensure_ascii=False, indent=2))
