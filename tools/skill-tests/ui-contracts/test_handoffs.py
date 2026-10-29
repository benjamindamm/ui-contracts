#!/usr/bin/env python3
"""Functional contract tests in temporary repos; no historical artifact writes."""
import argparse
import copy
import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT/'skills/ui-contracts'
MODULE = None

class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name).resolve()
        self.source = self.put('components/part.css', 'SOURCE-BODY-NOT-INLINE: placeholder uses muted')
        files = {'part.css': self.hash(self.source)}
        self.manifest = self.put('plan/input-manifest.json', {'root':'components','files':files})
        self.revision = hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self.task = {'format':'ui-contracts-task/1','taskId':'visual-map','revision':1,'role':'mapper','phase':'normal',
          'goal':'Map colors of one part','scope':'visual source only; no generation',
          'definition':{'revision':self.revision,'manifest':self.ref(self.manifest)},
          'sources':[{'id':'visual-css',**self.ref(self.source),'kind':'original','purpose':'Own placeholder rule'}],
          'inputs':[],'outputs':['work/visual'],
          'acceptance':[{'id':'mapped','required':True,'description':'Source mapping with receipt'}],
          'context':{'maxInlineChars':8000,'maxHandoffChars':16000}}
        self.artifact = self.put('work/visual/source-map.json', {'rule':'muted','privateNotes':'NOT-INLINE-ARTIFACT'})
        self.h = {'format':'ui-contracts-handoff/1','taskId':'visual-map','taskRevision':1,'role':'mapper','revision':1,
          'definitionRevision':self.revision,'status':'ready','summary':'Mapped one source rule','inputs':[],
          'artifacts':[{'id':'map',**self.ref(self.artifact),'kind':'source-map'}],
          'claims':[{'id':'placeholder','classification':'explicit','statement':'Placeholder has own muted color',
                     'sourceRefs':[{'sourceId':'visual-css','locator':'::placeholder'}],'evidenceRefs':[]}],
          'questions':[],'checks':[{'id':'mapped','status':'pass','method':'manual','evidenceRefs':['map']}],
          'limitations':['No native rendering or runtime proof'],'nextAction':'Generate from original rules'}

    def put(self,name,value):
        p=self.repo/name; p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(value,ensure_ascii=False,indent=2) if not isinstance(value,str) else value)
        return p
    def hash(self,p):return hashlib.sha256(p.read_bytes()).hexdigest()
    def ref(self,p):return {'path':str(p.relative_to(self.repo)),'sha256':self.hash(p)}
    def check(self):return MODULE.validate_handoff(self.repo,self.task,self.h)
    def consumer(self):
        tfile=self.put('plan/visual-task.json',self.task)
        hfile=self.put('work/visual/handoff-v1.json',self.h)
        t=copy.deepcopy(self.task)
        t.update(taskId='build',role='builder',outputs=['work/build'])
        t['inputs']=[{'id':'visual',**self.ref(hfile),'kind':'handoff','taskId':'visual-map','revision':1,
                      'producerRole':'mapper','producerTask':self.ref(tfile),'claimIds':['placeholder']}]
        return t

    def test_bootstrap_has_pointers_without_claims_or_file_bodies(self):
        t=self.consumer();path=self.put('plan/build-task.json',t)
        packet=MODULE.bootstrap_packet(self.repo,path);raw=json.dumps(packet)
        for forbidden in ['Placeholder has own muted color','SOURCE-BODY-NOT-INLINE','NOT-INLINE-ARTIFACT']:
            self.assertNotIn(forbidden,raw)
        for key in ['claims','acceptance','sources','inputs']:
            self.assertNotIn(key,packet)
        self.assertEqual(packet['taskReference']['sha256'],self.hash(path))
        self.assertEqual(Path(packet['skillRoleReference']['path']).name,'builder.md')
        self.assertFalse(packet['release'])
    def test_bootstrap_checks_stale_dependency_even_without_inlining_it(self):
        path=self.put('plan/build-task.json',self.consumer());self.artifact.write_text('stale')
        with self.assertRaises(MODULE.Invalid):MODULE.bootstrap_packet(self.repo,path)
    def test_bootstrap_budget_counts_full_pretty_wrapper(self):
        path=self.put('plan/task.json',self.task)
        packet=MODULE.bootstrap_packet(self.repo,path)
        wire=json.dumps({'overall':'BOOTSTRAP_READY','release':False,'bootstrap':packet},ensure_ascii=False,indent=2)+'\n'
        self.task['context']['maxBootstrapChars']=len(wire)-1;self.put('plan/task.json',self.task)
        with self.assertRaises(MODULE.Invalid):MODULE.bootstrap_packet(self.repo,path)
        self.task['context']['maxBootstrapChars']=len(wire);self.put('plan/task.json',self.task)
        self.assertEqual(MODULE.bootstrap_packet(self.repo,path)['taskId'],self.task['taskId'])
    def test_bootstrap_rejects_invalid_budget(self):
        for value in [True,0,-1,'2000']:
            self.task['context']['maxBootstrapChars']=value
            path=self.put('plan/task.json',self.task)
            with self.assertRaises(MODULE.Invalid):MODULE.bootstrap_packet(self.repo,path)
    def test_cli_bootstrap_within_actual_file_budget(self):
        path=self.put('plan/task.json',self.task);out=self.repo/'bootstrap.json'
        result=subprocess.run(['python3',str(SKILL/'scripts/handoffs.py'),'bootstrap','--repo',str(self.repo),
                               '--task',str(path),'--output',str(out)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertLessEqual(len(out.read_text()),2000)
        self.assertEqual(json.loads(out.read_text())['overall'],'BOOTSTRAP_READY')

    def test_ready_is_not_release(self):self.assertEqual(self.check(),'HANDOFF_READY')
    def test_context_does_not_inline_source_or_artifact(self):
        packet=MODULE.context_packet(self.repo,self.consumer())
        s=json.dumps(packet)
        self.assertNotIn('SOURCE-BODY-NOT-INLINE',s);self.assertNotIn('NOT-INLINE-ARTIFACT',s)
        self.assertEqual(packet['inputs'][0]['claims'][0]['id'],'placeholder')
        self.assertEqual(packet['inputs'][0]['claimSources'][0]['path'],'components/part.css')
    def test_only_selected_claims_transferred(self):
        t=self.consumer();t['inputs'][0]['claimIds']=[]
        self.assertEqual(MODULE.context_packet(self.repo,t)['inputs'][0]['claims'],[])
    def test_context_points_to_selected_role_only(self):
        self.task['domain']='visual'
        packet=MODULE.context_packet(self.repo,self.task)
        self.assertEqual(packet['domain'],'visual')
        self.assertEqual(Path(packet['skillRoleReference']['path']).name,'mapper.md')
        self.assertEqual(packet['skillRoleReference']['sha256'],self.hash(Path(packet['skillRoleReference']['path'])))
    def test_changed_definition_blocks(self):
        self.source.write_text('changed rule')
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_stale_artifact_hash_blocks(self):
        self.artifact.write_text('new artifact')
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_wrong_definition_revision_blocks(self):
        self.h['definitionRevision']='a'*64
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_old_dependency_revision_blocks(self):
        t=self.consumer();t['inputs'][0]['revision']=2
        with self.assertRaises(MODULE.Invalid):MODULE.context_packet(self.repo,t)
    def test_partial_is_not_ready(self):
        self.h['status']='partial';self.h['checks']=[]
        self.assertEqual(self.check(),'HANDOFF_PARTIAL')
    def test_partial_dependency_blocks_successor(self):
        self.h['status']='partial';self.h['checks']=[]
        with self.assertRaises(MODULE.Invalid):MODULE.context_packet(self.repo,self.consumer())
    def test_rule_needs_original_source(self):
        self.h['claims'][0]['sourceRefs']=[]
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_observation_needs_evidence(self):
        self.h['claims'][0]['classification']='observation'
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_observation_with_evidence_allowed(self):
        self.h['claims'][0].update(classification='observation',evidenceRefs=['map'])
        self.assertEqual(self.check(),'HANDOFF_READY')
    def test_assumption_stays_labeled(self):
        self.h['claims'][0].update(classification='assumption',sourceRefs=[])
        t=self.consumer();packet=MODULE.context_packet(self.repo,t)
        self.assertEqual(packet['inputs'][0]['claims'][0]['classification'],'assumption')
    def test_blocking_question_prevents_ready(self):
        self.h['questions']=[{'id':'unknown','question':'Who owns value?','blocking':True}]
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_pass_needs_receipt(self):
        self.h['checks'][0]['evidenceRefs']=[]
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_unchecked_required_criterion_prevents_ready(self):
        self.h['checks'][0]['status']='not-checked'
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_duplicate_ids_block(self):
        self.h['claims'].append(copy.deepcopy(self.h['claims'][0]))
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_blind_reviewer_rejects_handoff(self):
        t=self.consumer();t.update(role='reviewer',phase='blind')
        with self.assertRaises(MODULE.Invalid):MODULE.context_packet(self.repo,t)
    def test_blind_reviewer_rejects_builder_report(self):
        t=copy.deepcopy(self.task);t.update(role='reviewer',phase='blind',outputs=['work/review'])
        t['inputs']=[{'id':'report',**self.ref(self.artifact),'kind':'builder-report'}]
        with self.assertRaises(MODULE.Invalid):MODULE.context_packet(self.repo,t)
    def test_blind_reviewer_can_read_target(self):
        t=copy.deepcopy(self.task);t.update(role='reviewer',phase='blind',outputs=['work/review'])
        t['inputs']=[{'id':'design',**self.ref(self.artifact),'kind':'artifact'}]
        self.assertEqual(MODULE.context_packet(self.repo,t)['phase'],'blind')
    def test_report_check_requires_frozen_first_review(self):
        t=copy.deepcopy(self.task);t.update(role='reviewer',phase='report-check')
        with self.assertRaises(MODULE.Invalid):MODULE.context_packet(self.repo,t)
    def test_report_check_after_first_review(self):
        t=copy.deepcopy(self.task);t.update(role='reviewer',phase='report-check',outputs=['work/report-review'])
        t['inputs']=[{'id':'first',**self.ref(self.artifact),'kind':'first-review'}]
        self.assertEqual(MODULE.context_packet(self.repo,t)['phase'],'report-check')
    def test_context_overflow_blocks_instead_of_truncation(self):
        t=self.consumer();t['context']['maxInlineChars']=100
        with self.assertRaises(MODULE.Invalid):MODULE.context_packet(self.repo,t)
    def test_handoff_overflow_blocks(self):
        self.task['context']['maxHandoffChars']=100
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_foreign_output_blocks(self):
        self.h['artifacts'][0]=dict(self.h['artifacts'][0],**self.ref(self.source))
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_output_cannot_overlap_source(self):
        self.task['outputs']=['components']
        with self.assertRaises(MODULE.Invalid):self.check()
    def test_receipts_bound_to_inputs(self):
        t=self.consumer();h=copy.deepcopy(self.h)
        h.update(taskId='build',role='builder',inputs=[{'id':'visual','sha256':'a'*64,'taskId':'visual-map','revision':1}])
        with self.assertRaises(MODULE.Invalid):MODULE.validate_handoff(self.repo,t,h)
    def test_unknown_requested_claim_blocks(self):
        t=self.consumer();t['inputs'][0]['claimIds']=['missing']
        with self.assertRaises(MODULE.Invalid):MODULE.context_packet(self.repo,t)
    def test_paths_do_not_escape_repo(self):
        for value in ['../escape','/tmp/escape']:
            with self.assertRaises(MODULE.Invalid):MODULE.resolve(self.repo,value)
    def test_cli_refuses_existing_output_without_modification(self):
        t=self.put('plan/task.json',self.task);o=self.put('already.json','original receipt')
        p=subprocess.run(['python3',str(SKILL/'scripts/handoffs.py'),'context','--repo',str(self.repo),
                          '--task',str(t),'--output',str(o)],capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0);self.assertEqual(o.read_text(),'original receipt')
    def test_cli_emits_context_and_no_release(self):
        t=self.put('plan/task.json',self.task);o=self.repo/'context.json'
        p=subprocess.run(['python3',str(SKILL/'scripts/handoffs.py'),'context','--repo',str(self.repo),
                          '--task',str(t),'--output',str(o)],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        result=json.loads(o.read_text());self.assertEqual(result['overall'],'CONTEXT_READY');self.assertFalse(result['release'])

class RecordingResult(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.cases=[]
    def addSuccess(self,test):super().addSuccess(test);self.cases.append({'test':test.id(),'status':'pass'})
    def addFailure(self,test,err):super().addFailure(test,err);self.cases.append({'test':test.id(),'status':'fail'})
    def addError(self,test,err):super().addError(test,err);self.cases.append({'test':test.id(),'status':'error'})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--skill',type=Path,default=SKILL);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();SKILL=args.skill.resolve()
    spec=importlib.util.spec_from_file_location('handoffs',SKILL/'scripts/handoffs.py')
    MODULE=importlib.util.module_from_spec(spec);spec.loader.exec_module(MODULE)
    result=unittest.TextTestRunner(verbosity=1,resultclass=RecordingResult).run(unittest.defaultTestLoader.loadTestsFromTestCase(HandoffTests))
    report={'skillPath':str(SKILL),'helperSha256':hashlib.sha256((SKILL/'scripts/handoffs.py').read_bytes()).hexdigest(),
            'passed':result.wasSuccessful(),'count':result.testsRun,'cases':result.cases,
            'scope':'Functional data/context routing tests, not an independent model forward-test or a security sandbox.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
