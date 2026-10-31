#!/usr/bin/env python3
"""Adapt future UX-selection work to the existing task/handoff v1 contract.
No agent launch, model grading, UI generation or rewriting of historical studies.
"""
import argparse,importlib.util,json,shutil,sys
from pathlib import Path
REVIEW_GROUPS=['requirements-ux','interface','visual','behavior','accessibility','integration']
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/libraries'))
from manage import manifest,library_root

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
handoffs=module('workflow_handoffs',ROOT/'skills/ui-contracts/scripts/handoffs.py')

def write(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2);out.write('\n')
def ref(repo,path,**extra):return {'path':str(path.resolve().relative_to(repo)), 'sha256':handoffs.digest(path),**extra}
def source(repo,path,id,kind,purpose):return {**ref(repo,path),'id':id,'kind':kind,'purpose':purpose}
def safe_output(repo,path):
 path=path.resolve();handoffs.need(path.is_relative_to(repo) and path!=repo,'output must be a new directory inside the selected repo')
 handoffs.need(not any(path.is_relative_to(repo/p) for p in ['libraries','skills','tools','.git']),'output overlaps implementation or definitions')
 handoffs.need(not path.exists(),'output already exists; do not overwrite a previous workflow')
 return path

def sources(repo,library):
 root=library_root(repo,library);index=handoffs.read(root/'library.json');selection=index.get('selection');handoffs.need(bool(selection),'library has no selection binding')
 paths=[root/'library.json',root/selection['policy'],root/selection['capabilitiesSchema']]
 policy=handoffs.read(paths[1]);paths.append(root/policy['logic'])
 # This is a source map, not an inline dump of four domains. Domain links stay in component.json.
 return [source(repo,p,'contract-'+str(i),'original','Relevant library/policy/capability entry; follow needed domain links') for i,p in enumerate(dict.fromkeys(paths))]

def task(repo,flow,name,role,phase,inputs,criteria):
 return {'format':'ui-contracts-task/1','taskId':flow['id']+'-'+name,'revision':1,'role':role,'phase':phase,
  'goal':{'selection':'Determine a source-supported component choice from the supplied facts and brief. Save the native decision and its limits.',
          'build':'Build the requested target from the selected original contracts; use the decision artifact, not predecessor prose as authority.',
          'review':'Independently inspect the delivered artifacts against original contracts and requirements. Freeze first-review before reading any builder report.',
          'report-check':'Compare the builder report with the already frozen first-review and actual artifact. Preserve all first-review bytes.'}[name],
  'scope':'Explicit library '+flow['library']+'; target '+flow['target']+'. Read task and assigned role first, then only needed linked sources/inputs. No model identity research, historical example output, extra agents, commit or push. No production approval.',
  'definition':flow['definition'],'sources':flow['sources'], 'inputs':inputs,
  'outputs':[flow['root']+'/work/'+name],
  'acceptance':[{'id':id,'required':True,'description':text} for id,text in criteria],
  'context':{'maxBootstrapChars':2000,'maxInlineChars':8000,'maxHandoffChars':16000}}

def prepare(repo,library,context,brief,out,target,identifier):
 repo=repo.resolve();out=safe_output(repo,out);root=library_root(repo,library)
 handoffs.need(target in {'web','openpencil'},'target must be explicit: web or openpencil')
 # Verify before writing; the adapter never translates old task formats silently.
 context=context.resolve();brief=brief.resolve();handoffs.need(handoffs.read(context).get('library')==library,'context library mismatch');handoffs.read(brief)
 src=sources(repo,library);m=manifest(repo,library)
 out.mkdir(parents=True);write(out/'inputs/definition.json',m)
 for name,path in [('context.json',context),('brief.json',brief)]:shutil.copyfile(path,out/'inputs'/name)
 flow={'format':'ui-contracts-ux-workflow/1','id':identifier,'revision':1,'library':library,'target':target,'root':str(out.relative_to(repo)),
       'definition':{'revision':m['revision'],'manifest':ref(repo,out/'inputs/definition.json')},'sources':src,
       'sharedInputs':[ref(repo,out/'inputs'/name,id=id,kind='artifact') for name,id in [('context.json','context'),('brief.json','brief')]],
       'activeStep':'selection','completed':[], 'tasks':{},'researchMetadata':None,'reviewGroups':REVIEW_GROUPS,
       'notice':'Research metadata is optional. Ready handoff/process completion is not a target-quality pass or model-performance guarantee.'}
 t=task(repo,flow,'selection','mapper','normal',flow['sharedInputs'],[
  ('decision-recorded','Save decision.json with the current native policy result; artifact id decision. Unknown facts remain unknown.'),
  ('scope-recorded','Record actual sources, assumptions and limits in the handoff; no invented runtime checks.')])
 tp=out/'tasks/selection-v1.json';handoffs.validate_task(repo,t);write(tp,t);flow['tasks']['selection']=ref(repo,tp)
 fp=out/'workflow-v1.json';write(fp,flow);return {'overall':'TASK_READY','release':False,'workflow':str(fp.relative_to(repo)),'task':str(tp.relative_to(repo))}

def load(repo,workflow):
 flow=handoffs.read(workflow);handoffs.need(flow.get('format')=='ui-contracts-ux-workflow/1','unsupported workflow')
 handoffs.version(flow.get('revision'),'workflow revision');handoffs.need(flow.get('activeStep') in {'selection','build','review','report-check','complete'},'unknown step')
 handoffs.bound(repo,flow['definition']['manifest'])
 for item in flow['tasks'].values():handoffs.validate_task(repo,handoffs.read(handoffs.bound(repo,item)))
 for item in flow['completed']:
  t=handoffs.read(handoffs.bound(repo,flow['tasks'][item['step']]));h=handoffs.read(handoffs.bound(repo,item['handoff']));handoffs.validate_handoff(repo,t,h)
 return flow

def verify_decision(repo,flow,h):
 decision=next((a for a in h['artifacts'] if a['id']=='decision'),None);handoffs.need(decision is not None,'selection delivery needs artifact id decision')
 saved=handoffs.read(handoffs.bound(repo,decision));choice=module('workflow_choice',ROOT/'tools/ux/choose.py')
 context=next(i for i in flow['sharedInputs'] if i['id']=='context');fresh=choice.evaluate(repo,flow['library'],handoffs.read(handoffs.bound(repo,context)))
 handoffs.need(fresh['overall']=='PASS_LIMITED' and fresh.get('choice') in handoffs.read(library_root(repo,flow['library'])/'library.json')['components'],'selection remains unresolved; do not advance consumers')
 for key in ['overall','library','libraryRevision','contextSha256','logicSha256','choice','assessment','inputs']:
  handoffs.need(saved.get(key)==fresh.get(key),'decision differs from current native policy: '+key)
 handoffs.need(saved.get('release') is False and saved.get('targetValidationRequired') is True,'decision scope missing')
 return decision

def advance(repo,workflow,delivery):
 repo=repo.resolve();flow=load(repo,workflow);step=flow['activeStep'];handoffs.need(step!='complete','workflow already complete')
 tp=handoffs.bound(repo,flow['tasks'][step]);t=handoffs.read(tp);delivery=delivery.resolve();h=handoffs.read(delivery)
 status=handoffs.validate_handoff(repo,t,h);handoffs.need(status=='HANDOFF_READY','necessary delivery is partial or blocked')
 arts={a['id']:a for a in h['artifacts']};inputs=list(flow['sharedInputs']);next_step={'selection':'build','build':'review','review':'report-check','report-check':'complete'}[step]
 if step=='selection':
  decision=verify_decision(repo,flow,h)
  inputs+=[ref(repo,handoffs.bound(repo,decision),id='decision',kind='artifact'),
           ref(repo,delivery,id='selection-handoff',kind='handoff',taskId=t['taskId'],revision=h['revision'],producerRole=t['role'],producerTask=flow['tasks'][step],claimIds=[])]
  next_task=task(repo,flow,'build','builder','normal',inputs,[('target-exported','Save a readable target artifact, id target; supporting target files also declare kind target.'),('report-saved','Save a factual report, id report and kind builder-report; distinguish tested and untested scope.')])
 elif step=='build':
  handoffs.need('target' in arts and arts['target']['kind']=='target','build needs target artifact')
  handoffs.need('report' in arts and arts['report']['kind']=='builder-report','build needs separately classified report')
  targets=[a for a in h['artifacts'] if a['kind']=='target']
  handoffs.need(all(a['id']!='report' for a in targets),'report mislabeled as target')
  inputs += [ref(repo,handoffs.bound(repo,a),id='target-'+a['id'],kind='artifact') for a in targets]
  next_task=task(repo,flow,'review','reviewer','blind',inputs,[('first-review-sealed','Save first-review JSON as artifact id first-review, kind first-review; include target hashes, source revision, checks and notChecked. Cover requirements-ux, interface, visual, behavior, accessibility, integration explicitly; pass/fail need bound sourceRefs and artifact evidenceRefs, other statuses a reason. Review completion is not target approval.')])
 elif step=='review':
  handoffs.need('first-review' in arts and arts['first-review']['kind']=='first-review','review needs frozen first-review artifact')
  first=handoffs.bound(repo,arts['first-review']);report_task=next(c for c in flow['completed'] if c['step']=='build');build=handoffs.read(handoffs.bound(repo,report_task['handoff']));report=next(a for a in build['artifacts'] if a['id']=='report')
  # Bind the native first-review structure before giving any report access.
  first_data=handoffs.read(first);handoffs.need(first_data.get('definitionRevision')==flow['definition']['revision'],'first-review source revision mismatch')
  expected={a['id']:a['sha256'] for a in build['artifacts'] if a['kind']=='target'}
  handoffs.need(first_data.get('targetHashes')==expected,'first-review target binding mismatch')
  handoffs.need(isinstance(first_data.get('checks'),list) and bool(first_data['checks']) and isinstance(first_data.get('notChecked'),list),'first-review needs checks and explicit notChecked')
  checks=first_data['checks']
  handoffs.need(all(c.get('status') in {'pass','fail','not-checked','undetermined'} and isinstance(c.get('id'),str) and bool(c['id'].strip()) and c.get('group') in REVIEW_GROUPS for c in checks),'invalid first-review status/group')
  handoffs.need(len({c['id'] for c in checks})==len(checks) and {c['group'] for c in checks}==set(REVIEW_GROUPS),'first-review omits integration/domain coverage or duplicates criteria')
  definition=handoffs.read(handoffs.bound(repo,flow['definition']['manifest']));definition_root=handoffs.resolve(repo,definition['root'])
  allowed={str((definition_root/rel).resolve()):sha for rel,sha in definition['files'].items()}
  allowed.update({str(handoffs.bound(repo,i)):i['sha256'] for i in flow['sharedInputs']})
  for check in checks:
   if check['status'] in {'pass','fail'}:
    source_refs=check.get('sourceRefs');evidence=check.get('evidenceRefs')
    handoffs.need(isinstance(source_refs,list) and bool(source_refs),'review verdict without leading source')
    for source in source_refs:
     path=handoffs.bound(repo,source);handoffs.need(allowed.get(str(path))==source['sha256'] and isinstance(source.get('locator'),str) and bool(source['locator'].strip()),'review source outside contract/requirements or missing locator')
    handoffs.need(isinstance(evidence,list) and bool(evidence) and all(e in arts and e!='first-review' for e in evidence),'review verdict without separate bound evidence')
   else:handoffs.need(isinstance(check.get('reason'),str) and bool(check['reason'].strip()),'unverified review status needs reason')
  inputs+=[ref(repo,first,id='first-review',kind='first-review'),ref(repo,handoffs.bound(repo,report),id='builder-report',kind='builder-report')]
  inputs += [ref(repo,handoffs.bound(repo,a),id='target-'+a['id'],kind='artifact') for a in build['artifacts'] if a['kind']=='target']
  next_task=task(repo,flow,'report-check','reviewer','report-check',inputs,[('claims-compared','Save report/target contradictions separately; do not overwrite first-review or turn untested properties into pass.')])
 # Immutable coordinator versions. Previous tasks, deliveries and first-review are never edited.
 flow['completed'].append({'step':step,'handoff':ref(repo,delivery),'status':status})
 flow['activeStep']=next_step;flow['revision']+=1
 folder=handoffs.resolve(repo,flow['root']);new_flow=folder/f"workflow-v{flow['revision']}.json"
 handoffs.need(not new_flow.exists(),'next workflow version already exists')
 if next_step!='complete':
  path=folder/'tasks'/(next_step+'-v1.json');handoffs.need(not path.exists(),'next task already exists');handoffs.validate_task(repo,next_task);write(path,next_task);flow['tasks'][next_step]=ref(repo,path)
 write(new_flow,flow)
 return {'overall':'WORKFLOW_COMPLETE' if next_step=='complete' else 'TASK_READY','release':False,'workflow':str(new_flow.relative_to(repo)), 'activeStep':next_step,'targetApproval':'not-inferred'}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=ROOT);s=p.add_subparsers(dest='cmd',required=True)
 a=s.add_parser('prepare');a.add_argument('--library',required=True);a.add_argument('--context',type=Path,required=True);a.add_argument('--brief',type=Path,required=True);a.add_argument('--out',type=Path,required=True);a.add_argument('--target',choices=['web','openpencil'],required=True);a.add_argument('--id',required=True)
 a=s.add_parser('advance');a.add_argument('--workflow',type=Path,required=True);a.add_argument('--handoff',type=Path,required=True)
 a=s.add_parser('inspect');a.add_argument('--workflow',type=Path,required=True)
 a=p.parse_args()
 try:
  if a.cmd=='prepare':r=prepare(a.repo,a.library,a.context,a.brief,a.out,a.target,a.id)
  elif a.cmd=='advance':r=advance(a.repo,a.workflow,a.handoff)
  else:
   f=load(a.repo.resolve(),a.workflow);r={'overall':'WORKFLOW_VALID','release':False,'activeStep':f['activeStep'],'completed':len(f['completed']),'researchMetadataRequired':False,'targetApproval':'not-inferred'}
  print(json.dumps(r));return 0
 except Exception as e:print(json.dumps({'overall':'BLOCKED','release':False,'diagnostic':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
