"""General library binding regressions, including missing/wrong/cyclic cross-file references."""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('library_structural_tests', ROOT / 'tools/libraries/check.py')
check = importlib.util.module_from_spec(spec); spec.loader.exec_module(check)


class BindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='library-bindings-'); self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name); self.lib = self.repo / 'libraries/consumer'
        shutil.copytree(ROOT / 'libraries/example', self.lib)
        shutil.copytree(ROOT / 'tools/validation/schemas', self.repo / 'tools/validation/schemas')

    def edit(self, rel, fn):
        p = self.lib / rel; data = json.loads(p.read_text()); fn(data); p.write_text(json.dumps(data))

    def run_check(self): return check.inspect(self.lib, self.repo)

    def codes(self): return {e['code'] for e in self.run_check()['errors']}

    def test_new_library_is_structurally_checked_without_historical_reference(self):
        result = self.run_check(); self.assertEqual(result['overall'], 'PASS_LIMITED')
        self.assertEqual(result['componentCount'], 6); self.assertFalse(result['release'])

    def test_inspection_readiness_does_not_execute_historical_reference(self):
        sys.path.insert(0, str(ROOT / 'tools/validation'))
        import check as validation
        from unittest.mock import patch
        spec = importlib.util.spec_from_file_location('contracts_inspection_test', ROOT / 'skills/ui-contracts/scripts/contracts.py')
        helper = importlib.util.module_from_spec(spec); spec.loader.exec_module(helper)
        with patch.object(validation, 'run', side_effect=AssertionError('Historical reference must not execute')):
            result = helper.inspect(ROOT, self.lib / 'components/input')
        self.assertEqual(result['overall'], 'BLOCKED')
        self.assertEqual(result['bindings']['overall'], 'PASS_LIMITED')
        self.assertEqual(result['diagnostic']['code'], 'SEMANTIC_PROFILE_UNSUPPORTED')

    def test_missing_domain_file_has_specific_error(self):
        self.edit('components/input/component.json', lambda d: d['domains'].update(interface='missing.json'))
        self.assertIn('REFERENCE_MISSING', self.codes())

    def test_wrong_domain_target_kind_rejected(self):
        self.edit('components/input/component.json', lambda d: d['domains'].update(interface='accessibility.html'))
        self.assertIn('REFERENCE_KIND_MISMATCH', self.codes())

    def test_escaping_source_rejected(self):
        self.edit('components/input/component.json', lambda d: d['domains'].update(interface='../../../../outside.json'))
        self.assertIn('REFERENCE_ESCAPES_LIBRARY', self.codes())

    def test_symlink_source_rejected(self):
        p = self.lib / 'components/input/copied.json'; p.symlink_to(self.lib / 'components/input/interface.json')
        self.edit('components/input/component.json', lambda d: d['domains'].update(interface='copied.json'))
        self.assertIn('REFERENCE_SYMLINK', self.codes())

    def test_duplicate_component_identity_rejected(self):
        self.edit('components/input/component.json', lambda d: d.update(id='ui-contracts:Select'))
        self.edit('components/input/ux.json', lambda d: d.update(componentId='ui-contracts:Select'))
        self.assertIn('COMPONENT_DUPLICATE_ID', self.codes())

    def test_missing_state_target_is_concrete_failure(self):
        p = self.lib / 'components/select/behavior.scxml'; p.write_text(p.read_text().replace('target="disabled"', 'target="missingState"'))
        self.assertIn('SCXML_TARGET_MISSING', self.codes())

    def test_missing_invoked_component_rejected(self):
        p = self.lib / 'components/autocomplete/behavior.scxml'; p.write_text(p.read_text().replace('../overlay/behavior.scxml', '../overlay/missing.scxml'))
        self.assertIn('REFERENCE_MISSING', self.codes())

    def test_missing_composition_part_rejected(self):
        self.edit('components/autocomplete/component.json', lambda d: d['composition']['overlay'].update(anchorPart='missingPart'))
        self.assertIn('COMPOSITION_PART_MISSING', self.codes())

    def test_recursive_composition_rejected(self):
        self.edit('components/input/component.json', lambda d: d.update(composition={'child': {'component': '../select/component.json'}}))
        self.edit('components/select/component.json', lambda d: d.update(composition={'child': {'component': '../input/component.json'}}))
        self.assertIn('COMPOSITION_CYCLE', self.codes())

    def test_token_alias_cycle_rejected(self):
        self.edit('tokens.json', lambda d: d['base']['gap'].update({'$value': '{autocomplete.gap}'}))
        self.assertIn('TOKEN_ALIAS_CYCLE', self.codes())

    def test_token_alias_type_conflict_rejected(self):
        self.edit('tokens.json', lambda d: d['base']['gap'].update({'$type': 'color'}))
        self.assertIn('TOKEN_ALIAS_TYPE_MISMATCH', self.codes())

    def test_nested_aliases_in_objects_and_arrays(self):
        cases = [
            ({'color': '{missing.color}'}, 'TOKEN_ALIAS_MISSING'),
            ([{'color': '{missing.color}'}], 'TOKEN_ALIAS_MISSING'),
            ({'color': '{probe}'}, 'TOKEN_ALIAS_CYCLE'),
            ([{'color': '{probe}'}], 'TOKEN_ALIAS_CYCLE'),
            ({'color': '{chain}'}, 'TOKEN_ALIAS_CYCLE'),
            ([{'color': '{validColor}'}], None),
            ('{validColor}', 'TOKEN_ALIAS_TYPE_MISMATCH'),
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                data = {
                    'validColor': {'$type': 'color', '$value': '#000000'},
                    'probe': {'$type': 'shadow', '$value': value},
                    'chain': {'$type': 'shadow', '$value': '{probe}'},
                }
                path = self.repo / 'tokens-probe.json'
                path.write_text(json.dumps(data))
                inspector = check.Inspector(self.lib, self.repo)
                if expected:
                    with self.assertRaises(check.Invalid) as caught:
                        inspector.tokens(path)
                    self.assertEqual(caught.exception.code, expected)
                    self.assertFalse(inspector.checks)
                else:
                    inspector.tokens(path)
                    self.assertEqual(inspector.checks[0]['kind'], 'token-alias-closure')

    def test_nested_missing_alias_fails_full_library_check(self):
        self.edit('tokens.json', lambda d: d.update(probe={
            '$type': 'shadow', '$value': [{'color': '{does.not.exist}'}]}))
        result = self.run_check()
        self.assertEqual(result['overall'], 'FAIL')
        self.assertIn('TOKEN_ALIAS_MISSING', {e['code'] for e in result['errors']})
        self.assertFalse(result['release'])

    def test_duplicate_story_identity_rejected(self):
        self.edit('components/input/stories.json', lambda d: d['stories'].append(d['stories'][0]))
        self.assertIn('STORY_DUPLICATE_ID', self.codes())

    def test_bad_primitive_default_rejected(self):
        self.edit('components/input/interface.json', lambda d: d['modules'][0]['declarations'][0]['members'][0].update(default='42'))
        self.assertIn('CEM_DEFAULT_TYPE_MISMATCH', self.codes())

    def test_failed_schema_is_not_masked_by_unsupported_font_root(self):
        self.edit('components/input/interface.json', lambda d: d['modules'][0]['declarations'][0].pop('kind'))
        output = self.repo / 'inspection.json'
        p = subprocess.run([sys.executable, str(ROOT / 'skills/ui-contracts/scripts/contracts.py'), 'inspect', '--repo', str(ROOT),
                            '--candidate', str(self.lib), '--output', str(output)], capture_output=True, text=True)
        result = json.loads(p.stdout)
        self.assertEqual(result['overall'], 'FAIL'); self.assertEqual(p.returncode, 1)
        self.assertEqual(result['diagnostic']['code'], 'ARTIFACT_CHECK_FAILED')
        self.assertTrue(any(r['status'] == 'FAIL' for r in result['artifacts']))
        self.assertTrue(any(r['code'] == 'FONT_LIBRARY_ROOT_UNSUPPORTED' for r in result['additionalDiagnostics']))


if __name__ == '__main__': unittest.main()
