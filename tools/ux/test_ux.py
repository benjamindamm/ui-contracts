"""Meaningful source/capability counterexamples in disposable libraries; no historical edits."""
import copy
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

def module(name, file):
    spec = importlib.util.spec_from_file_location(name, file)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

ux = module('ux_check_tests', HERE / 'check.py')
choice = module('ux_choice_tests', HERE / 'choose.py')


class UXTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='ux-regression-')
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.lib = self.repo / 'libraries/consumer'
        shutil.copytree(ROOT / 'libraries/example', self.lib)
        shutil.copytree(ROOT / 'tools/validation/schemas', self.repo / 'tools/validation/schemas')
        self.context = json.loads((HERE / 'contexts/fixed-thirty.json').read_text())
        self.context['library'] = 'consumer'

    def change(self, rel, fn):
        path = self.lib / rel
        data = json.loads(path.read_text()); fn(data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

    def repin(self, slug):
        path = self.lib / 'components' / slug / 'ux.json'
        data = json.loads(path.read_text())
        for source in data['sources']:
            source['sha256'] = ux.digest(path.parent / source['path'])
        path.write_text(json.dumps(data, indent=2) + '\n')

    def verify(self):
        return ux.verify(self.repo, 'consumer')

    def prepare(self):
        return choice.evaluate(self.repo, 'consumer', self.context, prepare_only=True)

    def test_real_profiles_run_without_example_library_id(self):
        result = self.verify()
        self.assertEqual(result['overall'], 'PASS_LIMITED')
        self.assertEqual(result['components']['SelectWithSearch']['status'], 'verified-limited')
        self.assertEqual(result['components']['Autocomplete']['status'], 'verified-limited')
        self.assertNotIn('interactionIntent', result['components']['Select']['verifiedProperties'])
        self.assertGreater(len(result['components']['SelectWithSearch']['native']['checks']), 10)
        self.assertFalse(result['release'])

    def test_disabled_host_guard_regression(self):
        path=self.lib/'components/autocomplete/behavior.scxml'
        path.write_text(path.read_text().replace(" &amp;&amp; !x.disabled;", ";"))
        self.repin('autocomplete')
        result=self.verify()['components']['Autocomplete']
        self.assertEqual(result['status'],'invalid')
        self.assertIn('OFF',result['native']['diagnostic'])

    def test_composition_model_must_be_source_bound(self):
        self.change('components/autocomplete/ux.json',lambda d:d.update(sources=[r for r in d['sources'] if r['path']!='../overlay/behavior.scxml']))
        self.assertEqual(self.verify()['components']['Autocomplete']['status'],'invalid')

    def test_false_search_claim_rejected_with_honest_new_sources(self):
        self.change('components/select/ux.json', lambda d: d['capabilities'].update(searchMode='query-provider'))
        self.repin('select')
        result = self.verify()
        self.assertEqual(result['overall'], 'FAIL')
        self.assertEqual(result['components']['Select']['errors'][0]['code'], 'UX_PROFILE_CAPABILITY_CONFLICT')

    def test_false_search_profile_cannot_be_adopted_by_plain_select(self):
        data = json.loads((self.lib / 'components/select-with-search/ux.json').read_text())
        self.change('components/select/ux.json', lambda d: d.update(capabilities=data['capabilities'], verification=data['verification']))
        result = self.verify()
        self.assertEqual(result['components']['Select']['errors'][0]['code'], 'UX_PROFILE_TYPE_CONFLICT')

    def test_fake_markup_and_signature_do_not_replace_native_search(self):
        search = self.lib / 'components/select-with-search'
        plain = self.lib / 'components/select'
        data = json.loads((search / 'ux.json').read_text())
        self.change('components/select/ux.json', lambda d: d.update(capabilities=data['capabilities'], verification=data['verification']))
        self.change('components/select/interface.json', lambda d: d['modules'][0]['declarations'][0]['members'].append({'kind': 'field', 'name': 'query', 'type': {'text': 'string'}}))
        (plain / 'accessibility.html').write_bytes((search / 'accessibility.html').read_bytes())
        self.repin('select')
        result = self.verify()
        self.assertEqual(result['components']['Select']['errors'][0]['code'], 'UX_NATIVE_CONTRACT_FAILED')

    def test_contenteditable_selected_label_is_not_readonly_structure(self):
        from lxml import html, etree
        path = self.lib / 'components/select-with-search/accessibility.html'
        tree = html.fromstring(path.read_text())
        trigger = tree.xpath('.//button[@data-part="trigger"]')[0]
        trigger.set('contenteditable', '')
        path.write_bytes(etree.tostring(tree, method='html'))
        self.repin('select-with-search')
        self.assertEqual(self.verify()['components']['SelectWithSearch']['errors'][0]['code'], 'UX_PROFILE_SOURCE_CONFLICT')

    def test_forged_pass_metadata_is_not_accepted(self):
        self.change('components/select/ux.json', lambda d: d['verification'].update(status='verified-limited'))
        self.assertEqual(self.verify()['components']['Select']['errors'][0]['code'], 'UX_SCHEMA_INVALID')

    def test_native_membership_guard_removal_is_caught_after_honest_repin(self):
        path = self.lib / 'components/select-with-search/behavior.scxml'
        from lxml import etree
        tree = etree.parse(str(path))
        transition = tree.xpath('//*[local-name()="transition" and @event="USER_SELECT"]')[0]
        transition.set('cond', 'true')
        path.write_bytes(etree.tostring(tree))
        self.repin('select-with-search')
        result = self.verify()
        self.assertEqual(result['components']['SelectWithSearch']['errors'][0]['code'], 'UX_NATIVE_CONTRACT_FAILED')

    def test_wrong_event_payload_type_rejected_after_honest_repin(self):
        self.change('components/select/interface.json', lambda d: d['modules'][0]['declarations'][0]['events'][0]['type'].update(text='CustomEvent<{value:number}>'))
        self.repin('select')
        self.assertEqual(self.verify()['components']['Select']['errors'][0]['code'], 'UX_PROFILE_TYPE_CONFLICT')

    def test_equivalent_record_field_and_literal_order_is_accepted(self):
        self.change('components/select/interface.json', lambda d: d['modules'][0]['declarations'][0]['events'][0]['type'].update(text="CustomEvent<{reason:'options-change'|'user';value:undefined|string}>"))
        self.repin('select')
        self.assertEqual(self.verify()['components']['Select']['status'], 'verified-limited')

    def test_silent_option_sorting_is_caught_after_honest_repin(self):
        path = self.lib / 'components/select/behavior.scxml'
        original = path.read_text()
        self.assertIn('_event.data.options.slice()', original)
        path.write_text(original.replace('_event.data.options.slice()', '_event.data.options.slice().sort(function(a,b){return a.key.localeCompare(b.key);})'))
        self.repin('select')
        self.assertEqual(self.verify()['components']['Select']['errors'][0]['code'], 'UX_NATIVE_CONTRACT_FAILED')

    def test_missing_source_hash_is_not_silently_ignored(self):
        self.change('components/select/ux.json', lambda d: d.update(sources=[s for s in d['sources'] if s['path'] != 'behavior.scxml']))
        self.assertEqual(self.verify()['components']['Select']['status'], 'invalid')

    def test_stale_sources_block_before_native_claim(self):
        self.change('components/select/component.json', lambda d: d.update(version='99.0.0'))
        self.assertEqual(self.verify()['components']['Select']['status'], 'invalid')

    def test_unknown_profile_stays_unverified_in_prepared_facts(self):
        self.change('components/select/ux.json', lambda d: d['verification'].update(profile='future-profile/99'))
        result = self.prepare()
        self.assertEqual(result['inputs']['selectVerification'], 'unverified')
        self.assertIsNone(result['choice'])
        self.assertEqual(result['decisionStatus'], 'prepared-only-not-evaluated')

    def test_incomplete_facts_prompt_clarification_instead_of_false(self):
        del self.context['facts']['filteringProviderAvailable']
        result = self.prepare()
        self.assertEqual(result['overall'], 'BLOCKED')
        self.assertEqual(result['choice'], 'needs-clarification')

    def test_string_boolean_rejected(self):
        self.context['facts']['queryEditingAllowed'] = 'true'
        with self.assertRaises(choice.Blocked): self.prepare()

    def test_free_text_address_does_not_get_fixed_choice_recommendation(self):
        self.context['facts']['fixedValuesRequired'] = False
        result = self.prepare()
        self.assertEqual(result['choice'], 'no-supported-policy')
        self.assertEqual(result['overall'], 'BLOCKED')

    def test_wrong_library_context_rejected(self):
        self.context['library'] = 'example'
        with self.assertRaises(choice.Blocked): self.prepare()

    def test_duplicate_keys_rejected_but_shared_prefixes_allowed(self):
        self.context['options'][4]['key'] = self.context['options'][3]['key']
        with self.assertRaises(choice.Blocked): self.prepare()

    def test_missing_runtime_is_explicit_not_platform_guess(self):
        with patch.object(choice, 'ROOT', self.repo), self.assertRaises(choice.Blocked) as error:
            choice.native(Path('/unused.dmn'), 'choice', {}, None)
        self.assertEqual(error.exception.code, 'UX_ENGINE_NOT_CONFIGURED')

    def test_bad_engine_hashes_rejected(self):
        rt = self.repo / 'runtime'; rt.mkdir()
        jar = rt / 'different.jar'; jar.write_text('wrong')
        (rt / 'classpath.txt').write_text(str(jar))
        with self.assertRaises(choice.Blocked) as error:
            choice.native(Path('/unused.dmn'), 'choice', {}, rt)
        self.assertEqual(error.exception.code, 'UX_ENGINE_LOCK_MISMATCH')

    def test_cli_keeps_context_small_and_saves_full_bound_evidence(self):
        output = self.repo / 'new-proof.json'
        args = [sys.executable, str(HERE / 'check.py'), '--repo', str(self.repo), '--library', 'consumer', '--output', str(output)]
        p = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        summary = json.loads(p.stdout)
        self.assertLess(len(p.stdout.encode()), 3500)
        self.assertNotIn('structure', summary)
        self.assertEqual(Path(summary['report']['path']), output.resolve())
        full = json.loads(output.read_text())
        self.assertGreater(len(full['components']['Select']['native']['checks']), 5)
        self.assertEqual(summary['report']['sha256'], ux.digest(output))
        original = output.read_bytes()
        repeated = subprocess.run(args, capture_output=True, text=True)
        self.assertNotEqual(repeated.returncode, 0)
        self.assertEqual(output.read_bytes(), original)

    def test_prepare_cli_works_and_does_not_shadow_stdlib_select(self):
        p = subprocess.run([sys.executable, str(HERE / 'choose.py'), '--repo', str(self.repo), '--library', 'consumer',
                            '--context', str(HERE / 'contexts/fixed-three.json'), '--prepare-only'], capture_output=True, text=True)
        self.assertEqual(p.returncode, 2, p.stderr)  # Context explicitly names example, not consumer.
        self.assertEqual(json.loads(p.stdout)['diagnostic']['code'], 'UX_CONTEXT_LIBRARY_MISMATCH')


if __name__ == '__main__':
    unittest.main()
