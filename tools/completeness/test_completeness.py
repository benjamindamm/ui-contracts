import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location('completeness_under_test', HERE / 'check.py')
checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)


class CompletenessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        shutil.copytree(HERE / 'examples', self.repo, dirs_exist_ok=True)
        self.component = 'components/choice/component.json'
        self.comp = self.repo / 'libraries/demo' / self.component
        self.record = self.repo / 'mapped.json'

    def run_check(self):
        return checker.inspect(self.repo, 'demo', self.component, self.record)

    def edit(self, path, fn):
        data = json.loads(path.read_text()); fn(data); path.write_text(json.dumps(data))

    def bind(self, rid):
        record = checker.strict(self.record)
        requirement = next(r for r in checker.profiles()[record['profile']]['requirements'] if r['id'] == rid)
        source = self.comp.parent / checker.sources(checker.strict(self.comp))[requirement['domain']]
        self.edit(self.record, lambda d: d['requirements'][rid]['evidence'][0].update(sha256=checker.sha(source)))

    def test_mapped_is_coverage_only_never_release_or_ready(self):
        r = self.run_check()
        self.assertEqual(r['overall'], 'COVERAGE_RECORDED')
        self.assertFalse(r['release']); self.assertEqual(r['componentStatus'], 'draft')
        self.assertTrue(r['semanticReviewRequired']); self.assertTrue(r['targetValidationRequired'])
        self.assertEqual(len(r['checks']), 11); self.assertFalse(r['questions'])

    def test_design_import_keeps_nine_specific_questions(self):
        self.record = self.repo / 'design-import.json'; r = self.run_check()
        self.assertEqual(r['overall'], 'DRAFT_INCOMPLETE')
        self.assertEqual({x['id'] for x in r['checks'] if x['status'] == 'mapped'}, {'VIS-001','VIS-002'})
        self.assertEqual(len(r['questions']), 9)
        self.assertIn('Escape', next(q['question'] for q in r['questions'] if q['id']=='BEH-003'))
        self.assertTrue(all(q['blocking'] for q in r['questions']))

    def test_resolving_one_question_does_not_close_others(self):
        full=checker.strict(self.record)
        self.record=self.repo/'design-import.json'
        before=self.run_check()
        self.edit(self.record,lambda d:d['requirements'].update({'BEH-003':full['requirements']['BEH-003']}))
        after=self.run_check()
        self.assertEqual(len(before['questions']),9);self.assertEqual(len(after['questions']),8)
        self.assertEqual({q['id'] for q in after['questions']},{q['id'] for q in before['questions']}-{'BEH-003'})

    def test_code_import_does_not_infer_accessibility_or_ux(self):
        self.record=self.repo/'code-import.json';r=self.run_check()
        self.assertEqual(len(r['questions']),6)
        self.assertTrue({'A11Y-001','A11Y-002','A11Y-003','UX-001'}.issubset({q['id'] for q in r['questions']}))
        self.assertEqual(r['componentStatus'],'draft')

    def test_partial_component_without_behavior_is_a_valid_draft(self):
        self.component='components/design-only/component.json'; self.record=self.repo/'design-only.json'
        r=self.run_check(); self.assertEqual(r['overall'],'DRAFT_INCOMPLETE')
        self.assertFalse(r['errors']); self.assertEqual(len(r['questions']),11)

    def test_empty_mapping_is_not_inferred_from_existing_files(self):
        self.edit(self.record,lambda d:d.update(requirements={}))
        self.assertEqual(len(self.run_check()['questions']),11)

    def test_missing_file_reopens_each_dependent_requirement(self):
        self.comp.with_name('behavior.scxml').unlink(); r=self.run_check()
        self.assertEqual({q['id'] for q in r['questions']},{'BEH-001','BEH-002','BEH-003','A11Y-003'})
        self.assertTrue(all(q['reason']=='SOURCE_MISSING' for q in r['questions']))

    def test_changed_source_reopens_coverage_until_fresh_mapping(self):
        p=self.comp.with_name('behavior.scxml');p.write_text(p.read_text()+'\n')
        self.assertEqual(len(self.run_check()['questions']),4)
        for rid in ['BEH-001','BEH-002','BEH-003','A11Y-003']:self.bind(rid)
        self.assertEqual(self.run_check()['overall'],'COVERAGE_RECORDED')

    def test_changed_component_reopens_all_requirements(self):
        self.edit(self.comp,lambda d:d.update(version='new'))
        self.assertEqual(len(self.run_check()['questions']),11)

    def test_placeholder_and_empty_decision_cannot_close_gap(self):
        p=self.comp.with_name('ux.json')
        for value in ['TODO: fragen', '', {}, None, '???']:
            with self.subTest(value=value):
                p.write_text(json.dumps({'purpose':value}));self.bind('UX-001')
                q=next(q for q in self.run_check()['questions'] if q['id']=='UX-001')
                self.assertEqual(q['reason'],'EVIDENCE_EMPTY_OR_PLACEHOLDER')

    def test_false_and_zero_are_values_but_wrong_field_shape_stays_open(self):
        self.assertTrue(checker.meaningful(False));self.assertTrue(checker.meaningful(0))
        p=self.comp.with_name('ux.json');p.write_text('{"purpose":false}');self.bind('UX-001')
        self.assertEqual(self.run_check()['questions'][0]['reason'],'EVIDENCE_SHAPE_MISMATCH')

    def test_metadata_cannot_replace_commit_transition(self):
        self.edit(self.record,lambda d:d['requirements']['BEH-002']['evidence'][0]['selector'].update(value='/s:scxml/@initial'))
        self.assertEqual(self.run_check()['questions'][0]['reason'],'EVIDENCE_SHAPE_MISMATCH')

    def test_cem_missing_value_type_stays_open(self):
        p=self.comp.with_name('interface.json')
        self.edit(p,lambda d:d['modules'][0]['declarations'][0]['members'][0].pop('type'))
        self.bind('IF-001');self.bind('IF-002')
        self.assertEqual(self.run_check()['questions'][0]['id'],'IF-001')

    def test_unbound_label_and_missing_initial_state_remain_gaps(self):
        p=self.comp.with_name('accessibility.html');p.write_text(p.read_text().replace('for="choice"','for="missing"'))
        self.bind('A11Y-001');self.bind('A11Y-002')
        self.assertIn('A11Y-002',{q['id'] for q in self.run_check()['questions']})
        p=self.comp.with_name('behavior.scxml');p.write_text(p.read_text().replace('initial="idle"','initial="missing"'))
        self.bind('BEH-001')
        self.assertIn('BEH-001',{q['id'] for q in self.run_check()['questions']})

    def test_conflict_is_a_blocking_question(self):
        self.record=self.repo/'conflict.json';r=self.run_check()
        self.assertEqual(r['questions'][0]['id'],'BEH-003')
        self.assertEqual(r['checks'][6]['status'],'conflict')

    def test_unknown_profile_does_not_fallback(self):
        self.edit(self.record,lambda d:d.update(profile='unknown/1'))
        self.assertEqual(self.run_check()['overall'],'BLOCKED')

    def test_unknown_requirement_does_not_disappear(self):
        self.edit(self.record,lambda d:d['requirements'].update(UNKNOWN={'status':'open'}))
        self.assertEqual(self.run_check()['overall'],'BLOCKED')

    def test_arbitrary_pass_or_not_applicable_cannot_bypass(self):
        for status in ['pass','not-applicable']:
            with self.subTest(status=status):
                self.edit(self.record,lambda d:d['requirements']['BEH-003'].update(status=status))
                self.assertEqual(self.run_check()['overall'],'BLOCKED')

    def test_bad_locator_reopens_question(self):
        self.edit(self.record,lambda d:d['requirements']['BEH-003']['evidence'][0]['selector'].update(value='//s:transition[@event="MISSING"]'))
        self.assertEqual(self.run_check()['questions'][0]['reason'],'LOCATOR_EMPTY')

    def test_css_comment_is_not_a_layout_decision(self):
        p=self.comp.with_name('layout.css');p.write_text('/* layout later */\n');self.bind('VIS-002')
        self.assertIn('VIS-002',{q['id'] for q in self.run_check()['questions']})

    def test_xml_dtd_and_wrong_selector_domain_rejected(self):
        self.edit(self.record,lambda d:d['requirements']['BEH-003']['evidence'][0]['selector'].update(kind='lines',value='1:1'))
        self.assertEqual(self.run_check()['questions'][0]['reason'],'SELECTOR_DOMAIN_MISMATCH')
        p=self.comp.with_name('behavior.scxml');p.write_text('<!DOCTYPE scxml><scxml/>');self.bind('BEH-002')
        self.assertIn('XML_DTD_UNSUPPORTED',{q['reason'] for q in self.run_check()['questions']})

    def test_escaping_path_and_symlink_cannot_supply_evidence(self):
        for ref in ['../../../../outside.json','/tmp/outside.json']:
            with self.subTest(ref=ref):
                self.edit(self.comp,lambda d:d.update(ux=ref))
                self.edit(self.record,lambda d:d.update(componentSha256=checker.sha(self.comp)))
                self.assertIn('UX-001',{q['id'] for q in self.run_check()['questions']})

    def test_symlink_source_is_not_accepted(self):
        source=self.comp.with_name('ux.json')
        link=source.with_name('linked-ux.json');link.symlink_to(source)
        self.edit(self.comp,lambda d:d.update(ux='linked-ux.json'))
        self.edit(self.record,lambda d:d.update(componentSha256=checker.sha(self.comp)))
        self.assertEqual(self.run_check()['questions'][0]['reason'],'REFERENCE_SYMLINK')

    def test_decorative_profile_has_its_own_explicit_questions(self):
        data=checker.init_record(self.comp,'decorative-visual/1')
        self.record.write_text(json.dumps(data))
        r=self.run_check();self.assertEqual(len(r['questions']),4)
        self.assertIn('A11Y-004',{q['id'] for q in r['questions']})
        self.assertTrue(r['semanticReviewRequired'])

    def test_mapped_undeclared_domain_stays_open(self):
        self.edit(self.comp,lambda d:d['domains'].pop('behavior'))
        self.edit(self.record,lambda d:d.update(componentSha256=checker.sha(self.comp)))
        self.assertEqual({q['reason'] for q in self.run_check()['questions']},{'DOMAIN_NOT_DEFINED'})

    def test_duplicate_keys_block_instead_of_silently_replacing(self):
        self.record.write_text('{"format":"one","format":"two"}')
        self.assertEqual(self.run_check()['overall'],'BLOCKED')

    def test_empty_scxml_element_is_not_decision_evidence(self):
        p=self.comp.with_name('behavior.scxml')
        p.write_text('<scxml xmlns="http://www.w3.org/2005/07/scxml"><state id="empty"/></scxml>')
        self.edit(self.record,lambda d:d['requirements']['BEH-003']['evidence'][0]['selector'].update(value='//s:state'))
        self.bind('BEH-003')
        self.assertEqual(next(q['reason'] for q in self.run_check()['questions'] if q['id']=='BEH-003'),'LOCATOR_EMPTY')

    def test_init_cannot_write_into_another_library(self):
        dest=self.repo/'libraries/other/record.json'
        args=[sys.executable,str(HERE/'check.py'),'--repo',str(self.repo),'--library','demo','--component',self.component,'--record',str(dest),'--init','--profile','interactive-control/1']
        run=subprocess.run(args,capture_output=True,text=True)
        self.assertEqual(run.returncode,2);self.assertFalse(dest.exists())

    def test_inherited_token_type_is_accepted(self):
        p=self.repo/'libraries/demo/tokens.json'
        p.write_text('{"$type":"color","surface":{"$value":"#FFFFFF"}}')
        self.bind('VIS-001')
        self.assertEqual(self.run_check()['overall'],'COVERAGE_RECORDED')

    def test_decorative_hidden_must_be_explicitly_true(self):
        original=checker.strict(self.record)
        data=checker.init_record(self.comp,'decorative-visual/1')
        for rid in ['VIS-001','VIS-002','UX-001']:data['requirements'][rid]=original['requirements'][rid]
        p=self.comp.with_name('accessibility.html');p.write_text('<span aria-hidden="false"></span>')
        data['requirements']['A11Y-004']={'status':'mapped','evidence':[{'sha256':checker.sha(p),'selector':{'kind':'xpath','value':'//span'}}]}
        self.record.write_text(json.dumps(data))
        self.assertEqual(self.run_check()['questions'][0]['id'],'A11Y-004')
        p.write_text('<span aria-hidden="true"></span>');self.bind('A11Y-004')
        self.assertEqual(self.run_check()['overall'],'COVERAGE_RECORDED')

    def test_init_rejects_invalid_component_identity(self):
        self.edit(self.comp,lambda d:d.update(id=42))
        with self.assertRaises(checker.CoverageError):
            checker.init_record(self.comp,'interactive-control/1')

    def test_stale_profile_binding_blocks_without_new_checklist_fallback(self):
        self.edit(self.record,lambda d:d.update(profileSha256='0'*64))
        r=self.run_check();self.assertEqual(r['overall'],'BLOCKED')
        self.assertIn('PROFILE_BINDING_STALE',r['errors'][0]['detail'])

    def test_repeat_is_deterministic_and_read_only(self):
        before={str(p.relative_to(self.repo)):checker.sha(p) for p in self.repo.rglob('*') if p.is_file()}
        self.assertEqual(self.run_check(),self.run_check())
        after={str(p.relative_to(self.repo)):checker.sha(p) for p in self.repo.rglob('*') if p.is_file()}
        self.assertEqual(before,after)

    def test_cli_questions_exit_and_exclusive_output(self):
        output=self.repo/'out/report.json'
        args=[sys.executable,str(HERE/'check.py'),'--repo',str(self.repo),'--library','demo','--component',self.component,'--record',str(self.repo/'design-import.json'),'--output',str(output)]
        run=subprocess.run(args,capture_output=True,text=True);self.assertEqual(run.returncode,1)
        self.assertEqual(len(json.loads(run.stdout)['questions']),9)
        self.assertIn('BEH-003',run.stdout);self.assertEqual(len(json.loads(output.read_text())['questions']),9)
        self.assertNotEqual(subprocess.run(args,capture_output=True).returncode,0)

    def test_init_never_overwrites_and_all_requirements_open(self):
        output=self.repo/'new-record.json'
        args=[sys.executable,str(HERE/'check.py'),'--repo',str(self.repo),'--library','demo','--component',self.component,'--record',str(output),'--init','--profile','interactive-control/1']
        self.assertEqual(subprocess.run(args,capture_output=True).returncode,0)
        self.assertTrue(all(r['status']=='open' for r in checker.strict(output)['requirements'].values()))
        self.assertEqual(subprocess.run(args,capture_output=True).returncode,2)


if __name__=='__main__':unittest.main()
