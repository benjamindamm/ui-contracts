"""Workflow integrity, blind handoffs and honest result scope. No model-quality study."""
import copy,importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('ux_workflow_tests',ROOT/'tools/ux/workflow.py');flow=importlib.util.module_from_spec(spec);spec.loader.exec_module(flow)

class WorkflowTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.repo=Path(self.temp.name).resolve();self.lib=self.repo/'libraries/consumer'
  shutil.copytree(ROOT/'libraries/example',self.lib);shutil.copytree(ROOT/'tools/validation/schemas',self.repo/'tools/validation/schemas')
  ctx=json.loads((ROOT/'tools/ux/contexts/fixed-three.json').read_text());ctx['library']='consumer'
  self.ctx=self.repo/'context.json';self.ctx.write_text(json.dumps(ctx));self.brief=self.repo/'brief.json';self.brief.write_text(json.dumps({'goal':'Local personnel form','fields':['givenName','familyName','nationalNumber'],'requirements':['listed key only','keep phone as string']}))
  self.out=self.repo/'work/new';flow.prepare(self.repo,'consumer',self.ctx,self.brief,self.out,'web','case')
 def read(self,p):return json.loads(p.read_text())
 def task(self,step):return self.read(self.out/'tasks'/(step+'-v1.json'))
 def handoff(self,step,artifacts=None,status='ready'):
  t=self.task(step);folder=self.repo/t['outputs'][0];folder.mkdir(parents=True,exist_ok=True);p=folder/'receipt.json';flow.write(p,{'fixture':True,'notARealTargetValidation':True})
  arts=[flow.ref(self.repo,p,id='receipt',kind='evidence')]+(artifacts or [])
  h={'format':'ui-contracts-handoff/1','taskId':t['taskId'],'taskRevision':1,'role':t['role'],'revision':1,'definitionRevision':t['definition']['revision'],'status':status,'summary':'Structural test fixture; not a model or UI quality result.','inputs':[{'id':i['id'],'sha256':i['sha256'],**({'taskId':i['taskId'],'revision':i['revision']} if i['kind']=='handoff' else {})} for i in t['inputs']], 'artifacts':arts,'claims':[],'questions':[],'checks':[{'id':a['id'],'status':'pass','method':'automatic','evidenceRefs':['receipt']} for a in t['acceptance']],'limitations':['Structural fixture only'],'nextAction':'Inspect next task'}
  hp=folder/'handoff-v1.json';flow.write(hp,h);return hp
 def select(self):
  choice=flow.module('workflow_choice_test',ROOT/'tools/ux/choose.py');result=choice.evaluate(self.repo,'consumer',self.read(self.ctx));self.assertEqual(result['overall'],'PASS_LIMITED')
  path=self.out/'work/selection/decision.json';flow.write(path,result);h=self.handoff('selection',[flow.ref(self.repo,path,id='decision',kind='decision')]);flow.advance(self.repo,self.out/'workflow-v1.json',h);return h
 def build(self):
  self.select();p=self.out/'work/build/index.html';flow.write(p,{'fixture':'not a generated UI'});r=p.parent/'REPORT.md';r.write_text('Fixture report, not real validation.')
  h=self.handoff('build',[flow.ref(self.repo,p,id='target',kind='target'),flow.ref(self.repo,r,id='report',kind='builder-report')]);flow.advance(self.repo,self.out/'workflow-v2.json',h);return h
 def test_native_task_and_small_bootstrap_without_model_metadata(self):
  t=self.task('selection');self.assertEqual(t['format'],'ui-contracts-task/1');self.assertEqual(flow.load(self.repo,self.out/'workflow-v1.json')['researchMetadata'],None)
  packet=flow.handoffs.bootstrap_packet(self.repo,self.out/'tasks/selection-v1.json');self.assertLess(len(json.dumps(packet,ensure_ascii=False,indent=2)),2000)
 def test_context_names_consumer_not_example(self):
  t=self.task('selection');self.assertTrue(all('libraries/consumer/' in s['path'] for s in t['sources']));self.assertEqual(t['definition']['revision'],flow.manifest(self.repo,'consumer')['revision'])
 def test_existing_workflow_cannot_be_overwritten(self):
  before=(self.out/'workflow-v1.json').read_bytes()
  with self.assertRaisesRegex(ValueError,'already exists'):flow.prepare(self.repo,'consumer',self.ctx,self.brief,self.out,'web','case')
  self.assertEqual((self.out/'workflow-v1.json').read_bytes(),before)
 def test_wrong_library_context_blocks_before_write(self):
  self.ctx.write_text(json.dumps({'library':'different'}))
  with self.assertRaisesRegex(ValueError,'context library mismatch'):flow.prepare(self.repo,'consumer',self.ctx,self.brief,self.repo/'other','web','case')
  self.assertFalse((self.repo/'other').exists())
 def test_source_change_invalidates_old_task(self):
  p=self.lib/'components/input/behavior.scxml';p.write_text(p.read_text()+'\n')
  with self.assertRaisesRegex(ValueError,'changed definition'):flow.load(self.repo,self.out/'workflow-v1.json')
 def test_partial_delivery_blocks_dependent_builder(self):
  h=self.handoff('selection',status='partial')
  with self.assertRaisesRegex(ValueError,'partial or blocked'):flow.advance(self.repo,self.out/'workflow-v1.json',h)
  self.assertFalse((self.out/'tasks/build-v1.json').exists())
 def test_forged_choice_cannot_advance_native_policy(self):
  choice=flow.module('workflow_choice_countercase',ROOT/'tools/ux/choose.py');r=choice.evaluate(self.repo,'consumer',self.read(self.ctx));r['choice']='Autocomplete';p=self.out/'work/selection/decision.json';flow.write(p,r);h=self.handoff('selection',[flow.ref(self.repo,p,id='decision',kind='decision')])
  with self.assertRaisesRegex(ValueError,'decision differs'):flow.advance(self.repo,self.out/'workflow-v1.json',h)
  self.assertFalse((self.out/'workflow-v2.json').exists())
 def test_oversized_handoff_is_rejected(self):
  hp=self.handoff('selection',status='partial');h=self.read(hp);h['summary']='x'*17000;hp.write_text(json.dumps(h))
  with self.assertRaisesRegex(ValueError,'too large'):flow.advance(self.repo,self.out/'workflow-v1.json',hp)
 def test_new_builder_uses_explicit_handoff_and_artifact(self):
  self.select();t=self.task('build');kinds={i['kind'] for i in t['inputs']};self.assertIn('handoff',kinds);self.assertIn('artifact',kinds);self.assertEqual(next(i for i in t['inputs'] if i['kind']=='handoff')['claimIds'],[])
 def test_blind_review_excludes_builder_report_and_claims(self):
  self.build();t=self.task('review');self.assertEqual(t['phase'],'blind');self.assertNotIn('builder-report',[i['kind'] for i in t['inputs']]);self.assertNotIn('handoff',[i['kind'] for i in t['inputs']]);self.assertFalse(any(i['path'].endswith('REPORT.md') for i in t['inputs']))
 def test_report_access_requires_first_review(self):
  self.build();p=self.out/'work/review/first-review.json';flow.write(p,{'definitionRevision':self.task('review')['definition']['revision'],'targetHashes':{'target':'wrong'},'checks':[{'id':'c1','status':'fail'}],'notChecked':['Runtime']});h=self.handoff('review',[flow.ref(self.repo,p,id='first-review',kind='first-review')])
  with self.assertRaisesRegex(ValueError,'target binding'):flow.advance(self.repo,self.out/'workflow-v3.json',h)
  self.assertFalse((self.out/'tasks/report-check-v1.json').exists())
 def test_completed_review_with_failure_does_not_become_target_pass(self):
  self.build();bt=self.read(self.out/'work/build/handoff-v1.json');expected={a['id']:a['sha256'] for a in bt['artifacts'] if a['kind']=='target'}
  p=self.out/'work/review/first-review.json';flow.write(p,{'definitionRevision':self.task('review')['definition']['revision'],'targetHashes':expected,'checks':[{'id':g,'group':g,'status':'not-checked','reason':'Structural fixture; no actual target review'} for g in flow.REVIEW_GROUPS],'notChecked':['All actual UI behavior']});before=p.read_bytes()
  h=self.handoff('review',[flow.ref(self.repo,p,id='first-review',kind='first-review')]);flow.advance(self.repo,self.out/'workflow-v3.json',h)
  t=self.task('report-check');self.assertEqual(t['phase'],'report-check');self.assertIn('first-review',[i['kind'] for i in t['inputs']]);self.assertIn('builder-report',[i['kind'] for i in t['inputs']])
  hp=self.handoff('report-check');result=flow.advance(self.repo,self.out/'workflow-v4.json',hp);self.assertEqual(result['overall'],'WORKFLOW_COMPLETE');self.assertEqual(result['targetApproval'],'not-inferred');self.assertFalse(result['release']);self.assertEqual(p.read_bytes(),before)
 def test_end_review_cannot_silently_omit_domains(self):
  self.build();bt=self.read(self.out/'work/build/handoff-v1.json');expected={a['id']:a['sha256'] for a in bt['artifacts'] if a['kind']=='target'};p=self.out/'work/review/first-review.json';flow.write(p,{'definitionRevision':self.task('review')['definition']['revision'],'targetHashes':expected,'checks':[{'id':'x','group':'visual','status':'not-checked','reason':'fixture'}],'notChecked':['All other domains']});hp=self.handoff('review',[flow.ref(self.repo,p,id='first-review',kind='first-review')])
  with self.assertRaisesRegex(ValueError,'omits integration/domain'):flow.advance(self.repo,self.out/'workflow-v3.json',hp)
 def test_claimed_review_pass_needs_leading_source_and_separate_evidence(self):
  self.build();bt=self.read(self.out/'work/build/handoff-v1.json');expected={a['id']:a['sha256'] for a in bt['artifacts'] if a['kind']=='target'};p=self.out/'work/review/first-review.json';checks=[{'id':g,'group':g,'status':'not-checked','reason':'fixture'} for g in flow.REVIEW_GROUPS];checks[0]['status']='pass';flow.write(p,{'definitionRevision':self.task('review')['definition']['revision'],'targetHashes':expected,'checks':checks,'notChecked':['Other groups']});hp=self.handoff('review',[flow.ref(self.repo,p,id='first-review',kind='first-review')])
  with self.assertRaisesRegex(ValueError,'without leading source'):flow.advance(self.repo,self.out/'workflow-v3.json',hp)
 def checked_review(self,mode):
  self.build();bt=self.read(self.out/'work/build/handoff-v1.json');expected={a['id']:a['sha256'] for a in bt['artifacts'] if a['kind']=='target'};p=self.out/'work/review/first-review.json'
  checks=[{'id':g,'group':g,'status':'not-checked','reason':'Structural fixture; no target claim'} for g in flow.REVIEW_GROUPS]
  brief=next(i for i in self.task('review')['inputs'] if i['id']=='brief')
  checks[0]={'id':'brief-shape','group':'requirements-ux','status':'pass','sourceRefs':[{**{k:brief[k] for k in ['path','sha256']},'locator':'$.fields'}],'evidenceRefs':['receipt']}
  if mode=='missing-evidence':checks[0]['evidenceRefs']=[]
  if mode=='foreign-source':
   foreign=self.repo/'unrelated.json';flow.write(foreign,{'unrelated':True});checks[0]['sourceRefs']=[flow.ref(self.repo,foreign,locator='$')]
  flow.write(p,{'definitionRevision':self.task('review')['definition']['revision'],'targetHashes':expected,'checks':checks,'notChecked':['All actual target properties']});hp=self.handoff('review',[flow.ref(self.repo,p,id='first-review',kind='first-review')]);return hp
 def test_source_and_evidence_bound_review_can_advance_with_explicit_gaps(self):
  hp=self.checked_review('valid');r=flow.advance(self.repo,self.out/'workflow-v3.json',hp);self.assertEqual(r['activeStep'],'report-check');self.assertEqual(r['targetApproval'],'not-inferred')
 def test_bound_source_does_not_replace_measurement_evidence(self):
  hp=self.checked_review('missing-evidence')
  with self.assertRaisesRegex(ValueError,'without separate bound evidence'):flow.advance(self.repo,self.out/'workflow-v3.json',hp)
 def test_unrelated_rule_source_does_not_substitute_contract(self):
  hp=self.checked_review('foreign-source')
  with self.assertRaisesRegex(ValueError,'outside contract/requirements'):flow.advance(self.repo,self.out/'workflow-v3.json',hp)
 def test_illegal_phase_and_output_overlap_still_use_common_gate(self):
  t=self.task('selection');t['phase']='blind'
  with self.assertRaisesRegex(ValueError,'review phases reserved'):flow.handoffs.validate_task(self.repo,t)
  t=self.task('selection');t['outputs']=['libraries/consumer/components']
  with self.assertRaises(ValueError):flow.handoffs.validate_task(self.repo,t)
if __name__=='__main__':unittest.main()
