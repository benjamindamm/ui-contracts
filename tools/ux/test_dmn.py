"""Opt-in original DMN engine integration. Explicit runtime, no implicit /tmp or OS-specific Java path."""
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ux_dmn_choices', HERE / 'choose.py')
choice = importlib.util.module_from_spec(spec); spec.loader.exec_module(choice)


@unittest.skipUnless(os.environ.get('UX_RULE_RUNTIME'), 'Native DMN integration needs explicit UX_RULE_RUNTIME (not a passing engine check).')
class DMNTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='ux-dmn-integration-'); self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        shutil.copytree(ROOT / 'libraries/example', self.repo / 'libraries/example')
        shutil.copytree(ROOT / 'tools/validation/schemas', self.repo / 'tools/validation/schemas')
        self.context = json.loads((HERE / 'contexts/fixed-thirty.json').read_text())

    def evaluate(self):
        return choice.evaluate(self.repo, 'example', self.context, Path(os.environ['UX_RULE_RUNTIME']), os.environ.get('UX_JAVA'))

    def test_three_prefers_plain_select(self):
        self.context['options'] = self.context['options'][:3]
        result = self.evaluate(); self.assertEqual(result['choice'], 'Select')
        self.assertEqual(result['overall'], 'PASS_LIMITED'); self.assertFalse(result['release'])

    def test_thirty_prefers_separate_search_select(self):
        result = self.evaluate(); self.assertEqual(result['choice'], 'SelectWithSearch')
        self.assertEqual(result['assessment']['Autocomplete'], 'incompatible-editing')
        self.assertTrue(result['targetValidationRequired'])

    def test_search_explicitly_required_with_three(self):
        self.context['options'] = self.context['options'][:3]
        self.context['facts']['searchExplicitlyRequired'] = True
        self.assertEqual(self.evaluate()['choice'], 'SelectWithSearch')

    def test_missing_provider_cannot_satisfy_search(self):
        self.context['facts']['filteringProviderAvailable'] = False
        result = self.evaluate(); self.assertEqual(result['overall'], 'BLOCKED')
        self.assertEqual(result['assessment']['SelectWithSearch'], 'missing-filter-provider')

    def test_declared_only_does_not_become_a_recommendation(self):
        for slug in ['select', 'select-with-search']:
            p = self.repo / 'libraries/example/components' / slug / 'ux.json'
            data = json.loads(p.read_text()); data['verification']['profile'] = 'declared-only'
            p.write_text(json.dumps(data))
        result = self.evaluate(); self.assertEqual(result['overall'], 'BLOCKED')
        self.assertEqual(result['choice'], 'needs-verification')

    def test_boundary_is_explicit_project_parameter(self):
        self.context['options'] = self.context['options'][:15]
        self.assertEqual(self.evaluate()['choice'], 'Select')
        self.context = json.loads((HERE / 'contexts/fixed-thirty.json').read_text())
        self.context['options'] = self.context['options'][:16]
        self.assertEqual(self.evaluate()['choice'], 'SelectWithSearch')


if __name__ == '__main__': unittest.main()
