"""Mutation checks of freshness, provenance and actual browser-result gates.
Uses current captured evidence in disposable copies; does not simulate a new browser run.
"""
import argparse,copy,json,shutil,tempfile
from pathlib import Path
import check,browser_gate
T=check.TOOLS;BASE=check.ROOT/'docs/research/experiments/2026-10-25/ip01-static/reference'
def read(p):return json.loads(p.read_text())
def write(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def capture(run,name,fn,repin=True):
 p=run/'captures'/(name+'.json');c=read(p);fn(c);write(p,c)
 if repin:
  ledger=read(run/'collection.json');ledger['captures'][name]['sha256']=check.sha(p.read_bytes());write(run/'collection.json',ledger)
CASES=[('current-complete','PASS_LIMITED',None),('checker-file-missing','BLOCKED','REQUIRED_BROWSER_CHECKER_MISSING'),('missing-result','BLOCKED','BROWSER_RESULT_MISSING'),('missing-directory','BLOCKED','BROWSER_RESULT_MISSING'),('historical-captures','BLOCKED','BROWSER_RESULT_MISSING'),('stale','BLOCKED','BROWSER_RUN_STALE'),('future','BLOCKED','BROWSER_RUN_STALE'),('checker-changed','BLOCKED','BROWSER_CHECKER_CHANGED'),('host-revision-changed','BLOCKED','BROWSER_REVISION_MISMATCH'),('request-tamper','BLOCKED','BROWSER_REQUEST_CHANGED'),('not-sealed','BLOCKED','BROWSER_RUN_INCOMPLETE'),('missing-operation','BLOCKED','BROWSER_EXECUTION_INCOMPLETE_OR_FAILED'),('operation-failed','BLOCKED','BROWSER_EXECUTION_INCOMPLETE_OR_FAILED'),('operation-script-changed','BLOCKED','BROWSER_EXECUTION_RECEIPT_CHANGED'),('missing-capture','BLOCKED','BROWSER_CAPTURE_MISSING'),('changed-capture','BLOCKED','BROWSER_CAPTURE_CHANGED'),('foreign-run-capture','BLOCKED','BROWSER_RUN_MISMATCH'),('foreign-source-capture','BLOCKED','BROWSER_REVISION_MISMATCH'),('missing-required-case','BLOCKED','BROWSER_CASES_INCOMPLETE'),('host-source-tamper','BLOCKED','BROWSER_SOURCE_CHANGED'),('criteria-tamper','BLOCKED','BROWSER_CRITERIA_CHANGED'),('schema-preflight-missing','BLOCKED','HOST_SCHEMA_PREFLIGHT_INVALID'),('necessary-expectation-false','FAIL','BROWSER_EXPECTATION_FAILED'),('assertion-omitted','FAIL','BROWSER_EXPECTATION_FAILED'),('ax-selected-false','FAIL','BROWSER_EXPECTATION_FAILED'),('raw-focus-wrong','FAIL','BROWSER_RAW_EXPECTATION_FAILED'),('raw-scroll-zero','FAIL','BROWSER_RAW_EXPECTATION_FAILED'),('raw-duplicate-event','FAIL','BROWSER_RAW_EXPECTATION_FAILED'),('raw-lifecycle-not-final','FAIL','BROWSER_RAW_EXPECTATION_FAILED'),('result-file-ignored','PASS_LIMITED',None),('different-valid-static-package','BLOCKED','PACKAGE_HOST_MAPPING_UNSUPPORTED')]
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--run-dir',type=Path,required=True);a=ap.parse_args();original=a.run_dir.resolve();before={str(p.relative_to(original)):check.sha(p.read_bytes())for p in original.rglob('*')if p.is_file()};rows=[]
 with tempfile.TemporaryDirectory(prefix='ui-browser-gate-tests-')as temp:
  for key,status,code in CASES:
   run=Path(temp)/key;shutil.copytree(original,run);package=BASE;request=read(run/'request.json');ledger=read(run/'collection.json')
   if key=='stale':request['createdAt']-=86400;write(run/'request.json',request)
   elif key=='future':request['createdAt']+=86400;write(run/'request.json',request)
   elif key=='checker-changed':request['checker']['revision']='0'*64;write(run/'request.json',request)
   elif key=='host-revision-changed':request['hostRevision']='0'*64;write(run/'request.json',request)
   elif key=='request-tamper':request['challenge']='0'*64;write(run/'request.json',request)
   elif key=='not-sealed':ledger['status']='RUNNING';write(run/'collection.json',ledger)
   elif key=='missing-operation':del ledger['operations']['03'];write(run/'collection.json',ledger)
   elif key=='operation-failed':ledger['operations']['03']['status']='FAIL';write(run/'collection.json',ledger)
   elif key=='operation-script-changed':ledger['operations']['03']['scriptSha256']='0'*64;write(run/'collection.json',ledger)
   elif key=='missing-capture':(run/'captures/BR-04.json').unlink()
   elif key=='changed-capture':capture(run,'BR-04',lambda c:c['snapshot'].update(focus='wrong'),False)
   elif key=='foreign-run-capture':capture(run,'BR-04',lambda c:c.update(runId='old-run'))
   elif key=='foreign-source-capture':capture(run,'BR-04',lambda c:c.update(sourceRevision='0'*64))
   elif key=='missing-required-case':del ledger['captures']['BR-04'];write(run/'collection.json',ledger)
   elif key=='host-source-tamper':p=run/'host/host.js';p.write_text(p.read_text()+'\n/* changed */')
   elif key=='criteria-tamper':write(run/'cases.json',{'cases':[]})
   elif key=='schema-preflight-missing':write(run/'schema-preflight.json',[])
   elif key=='necessary-expectation-false':capture(run,'BR-04',lambda c:c['payload']['checks'].update(visible=False))
   elif key=='assertion-omitted':capture(run,'BR-03',lambda c:c['payload']['checks'].pop('focus'))
   elif key=='ax-selected-false':
    def change(c):
     for node in c['payload']['ax']['nodes']:
      for prop in node.get('properties',[]):
       if prop['name']=='selected':prop['value']['value']=False
    capture(run,'BR-05',change)
   elif key=='raw-focus-wrong':capture(run,'BR-03',lambda c:c['snapshot'].update(focus='B-input'))
   elif key=='raw-scroll-zero':capture(run,'BR-04',lambda c:c['snapshot']['A']['viewport'].update(scrollTop=0))
   elif key=='raw-duplicate-event':capture(run,'BR-06',lambda c:c['snapshot']['events']['A'].append(copy.deepcopy(c['snapshot']['events']['A'][0])))
   elif key=='raw-lifecycle-not-final':capture(run,'BR-20',lambda c:c['snapshot']['actors'][0].update(final=False))
   elif key=='result-file-ignored':write(run/'results.json',{'cases':[],'allPassed':True})
   elif key=='different-valid-static-package':
    import test_chain
    package=Path(temp)/'changed-static';shutil.copytree(BASE,package);v=read(package/'values.json');v['query']='different';write(package/'values.json',v);test_chain.repin(package)
   if key=='missing-result':run=None
   elif key=='missing-directory':run=Path(temp)/'not-present'
   elif key=='historical-captures':run=check.ROOT/'docs/research/experiments/2026-10-25/ip01-browser'
   if key=='checker-file-missing':
    from unittest.mock import patch
    toolcopy=Path(temp)/'incomplete-checker';shutil.copytree(T,toolcopy,ignore=shutil.ignore_patterns('.venv','node_modules','evidence','__pycache__'));(toolcopy/'browser/evaluate.py').unlink()
    with patch.object(browser_gate,'T',toolcopy):result=check.run(package,'web',browser_run=run)
   else:result=check.run(package,'web',browser_run=run)
   diag=next((s['diagnostic']['code']for s in result['stages']if'diagnostic'in s),None)
   release=(status=='PASS_LIMITED');ok=result['overall']==status and diag==code and result['release']==release
   rows.append({'id':key,'expected':status,'actual':result['overall'],'expectedDiagnostic':code,'diagnostic':diag,'release':result['release'],'expectationMet':ok,'stages':[{'id':s['id'],'status':s['status']}for s in result['stages']]});print(key,result['overall'],diag,'OK'if ok else'UNEXPECTED',flush=True)
 assert before=={str(p.relative_to(original)):check.sha(p.read_bytes())for p in original.rglob('*')if p.is_file()}
 out={'kind':'browser-gate-countercases','browserRunId':read(original/'request.json')['runId'],'newBrowserExecutions':0,'rawEvidenceUnchanged':True,'notNewCandidateMatrixEvaluations':True,'cases':rows,'allExpectationsMet':all(c['expectationMet']for c in rows)};write(T/'evidence/browser-countercases.json',out);print('TOTAL',len(rows),'MET',sum(c['expectationMet']for c in rows));return 0 if out['allExpectationsMet']else 1
if __name__=='__main__':raise SystemExit(main())
