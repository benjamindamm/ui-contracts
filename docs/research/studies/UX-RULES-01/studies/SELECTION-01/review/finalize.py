from pathlib import Path
import json,datetime,importlib.util
S=Path(__file__).resolve().parents[1];STUDY=S.parents[1]
spec=importlib.util.spec_from_file_location('acux',STUDY/'pilots/AC-UX-01/evaluate.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
context=json.loads((STUDY/'pilots/AC-UX-01/contexts/existing-single.json').read_text());live=m.evaluate(context);old=m.evaluate(context,repo=(S/'prior-library').resolve())
(S/'review/previous-pilot-reproduction.json').write_text(json.dumps({'liveLibraryResult':{'overall':live['overall'],'diagnostic':live.get('diagnostic'),'nativeCalled':live['nativeCalled']},'snapshotResult':{'overall':old['overall'],'nativeCalled':old['nativeCalled'],'rules':[{'id':r['ruleId'],'row':r['nativeRowId']} for r in old.get('rules',[])]},'interpretation':'Live manifest is intentionally stale after authorized library extension; original snapshot reproduces an earlier positive pilot without changing its code, sources or receipts.'},indent=2)+'\n')
assert live['overall']=='BLOCKED' and old['overall']=='compatible'
p=S/'study.json';data=json.loads(p.read_text());data['status']='completed-bounded-with-preserved-first-defects-and-separate-repair';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for arm in ['a','b']:data['arms'][arm].update({'status':'first-delivery-reviewed','completedObservedAt':now,'choice':'Select' if arm=='a' else 'Autocomplete','hardEligibilityMet':True,'projectPreferenceMet':True})
data['repair']={'arm':'b','path':'outputs/b-repair-01','sameBuilderContext':True,'firstDeliveryUnchanged':True,'issues':['SEL-B01','SEL-B02'],'browserRegression':'passed in bounded checks'}
data['review']={'criteria':'review/criteria.json','firstAssessment':'review/first-assessment.json','results':'review/results.json','browser':'BrowserOS neo over MCP; actual local pages, synthetic data','reviewer':'coordinator, no separate blind reviewer','independentFullAccessAudit':False}
data['interruptions']=[];data['interruptionEvidence']='No limit/provider interruption reported or observed in task notifications. Pre-delivery compiler corrections were reported by both builders; no claim about unknown internal provider events.'
data['ancillaryAgent']={'purpose':'README evolution and shorter diagram','agent':'/root/readme_evolution','notStudyBuilder':True,'readStudyOutputs':False,'source':'agent-reported boundary; not independently path-audited'}
data['limitations']=['One builder per condition; no repeated trials or randomized/crossed assignment.','No ablation proving UX rules alone caused choices.','Search threshold is a declared study/product policy.','Requiredness and combined phone layout were not specified; host choices differ.','No full component API/SCXML, screenreader or native-platform qualification.','No exact model identity or complete independent access audit.']
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Prior pilot snapshot reproduced; live revision correctly rejected; study register completed.')
