"""Exercise the installed skill helper against actual original formats and the real project gate.
No independent model/agent behavioral evaluation is claimed.
"""
import argparse,copy,hashlib,json,os,shutil,subprocess,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
BASE=ROOT/'docs/research/experiments/2026-10-25/ip01-static/reference'
CURRENT=ROOT/'tools/validation/evidence/browser-2026-10-26-run03'

def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def repin(p):
 b=json.loads((p/'bindings.json').read_text())
 for s in b['sources']:s['sha256']=h(p/s['path'])
 by={s['id']:s for s in b['sources']}
 for t in b['targets']:t['revision']=by[t['source']]['sha256']
 write(p/'bindings.json',b);files={str(f.relative_to(p)):h(f)for f in p.rglob('*')if f.is_file()and f.name!='resolved.json'}
 write(p/'resolved.json',{'files':files,'revision':hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--skill',type=Path,default=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'skills/ui-contracts');a=ap.parse_args();skill=a.skill.resolve();helper=skill/'scripts/contracts.py'
 source=ROOT/'skills/ui-contracts';source_hashes={str(p.relative_to(source)):h(p)for p in source.rglob('*')if p.is_file()};installed_hashes={str(p.relative_to(skill)):h(p)for p in skill.rglob('*')if p.is_file()};assert source_hashes==installed_hashes
 before={str(p):h(p)for root in [ROOT/'libraries/example',ROOT/'docs/research/studies',BASE]for p in root.rglob('*')if p.is_file()};rows=[]
 with tempfile.TemporaryDirectory(prefix='ui-contracts-skill-test-')as temp:
  w=Path(temp)
  def run(id,args,expected,diag=None,release=False,repo=ROOT):
   cmd=[sys.executable,str(helper),*args,'--repo',str(repo)];proc=subprocess.run(cmd,cwd=w,capture_output=True,text=True,timeout=90);r=json.loads(proc.stdout);actual=r['overall'];code=r.get('diagnostic',{}).get('code')
   ok=actual==expected and proc.returncode=={'PASS_LIMITED':0,'FAIL':1,'BLOCKED':2}[expected]and r['release']==release and(diag is None or code==diag)
   rows.append({'id':id,'expected':expected,'actual':actual,'expectedDiagnostic':diag,'diagnostic':code,'release':r['release'],'exitCode':proc.returncode,'expectationMet':ok,'report':r});print(id,actual,code,'OK'if ok else'UNEXPECTED',flush=True);return r
  run('supported-static',['validate','--scope','static'],'PASS_LIMITED')
  run('missing-browser',['validate'],'BLOCKED','BROWSER_RESULT_MISSING')
  age=time.time()-json.loads((CURRENT/'request.json').read_text())['createdAt']
  if 0<=age<=7200:run('current-bound-web',['validate','--browser-run',str(CURRENT)],'PASS_LIMITED',release=True)
  else:run('expired-bound-web',['validate','--browser-run',str(CURRENT)],'BLOCKED','BROWSER_RUN_STALE')
  changed=w/'changed-static';shutil.copytree(BASE,changed);v=json.loads((changed/'values.json').read_text());v['query']='changed by the author';write(changed/'values.json',v);repin(changed)
  run('changed-static-partial',['validate','--scope','static','--candidate',str(changed)],'PASS_LIMITED')
  run('changed-package-cannot-borrow-web',['validate','--candidate',str(changed),'--browser-run',str(CURRENT)],'BLOCKED','PACKAGE_HOST_MAPPING_UNSUPPORTED'if age<=7200 else'BROWSER_RUN_STALE')
  new=w/'new-disclosure';new.mkdir()
  cem={'schemaVersion':'2.1.0','modules':[{'kind':'javascript-module','path':'disclosure.js','declarations':[{'kind':'class','name':'Disclosure','members':[{'kind':'field','name':'expanded','type':{'text':'boolean'},'default':'false'}],'events':[{'name':'expanded-change','type':{'text':'CustomEvent<{expanded:boolean}>'}}],'cssParts':[{'name':'trigger'},{'name':'panel'}]}]}]}
  write(new/'interface.json',cem);write(new/'tokens.json',{'disclosure':{'minHeight':{'$type':'dimension','$value':{'value':44,'unit':'px'}}}})
  write(new/'component.json',{'format':'ui-contract-component-draft','id':'test:Disclosure','domains':{'interface':'interface.json','visual':{'tokens':'tokens.json','css':'layout.css'},'behavior':'behavior.scxml','accessibility':'accessibility.html'}})
  (new/'behavior.scxml').write_text('<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" initial="closed"><state id="closed"><transition event="TOGGLE" target="open"/></state><state id="open"><transition event="TOGGLE" target="closed"/></state></scxml>')
  (new/'layout.css').write_text('[data-part="trigger"] { min-height: var(--disclosure-min-height); }')
  (new/'accessibility.html').write_text('<button data-part="trigger" aria-expanded="false" aria-controls="panel">Details</button><div id="panel" data-part="panel" hidden>Details</div>')
  r=run('new-original-artifacts-not-full-approval',['inspect','--candidate',str(new)],'BLOCKED','SEMANTIC_PROFILE_UNSUPPORTED');assert all(x['status']=='PASS_LIMITED'for x in r['artifacts']);assert any(c['checker'].startswith('original CEM')and c['accepted']for x in r['artifacts']for c in x['checks']);assert any(c['checker'].startswith('original loose SCXML')and c['accepted']for x in r['artifacts']for c in x['checks'])
  raw={str(p.relative_to(new)):p.read_text()for p in new.iterdir()}
  run('new-component-cannot-use-reference-profile',['validate','--candidate',str(new),'--browser-run',str(CURRENT)],'FAIL','MALFORMED_OR_UNSUPPORTED_INPUT')
  run('existing-library-is-not-runtime-approval',['inspect','--candidate',str(ROOT/'libraries/example/components/overlay')],'BLOCKED','SEMANTIC_PROFILE_UNSUPPORTED')
  bad=w/'bad-json';bad.mkdir();(bad/'component.json').write_text('{"id":"one","id":"two"}');run('duplicate-json-rejected',['inspect','--candidate',str(bad)],'FAIL','ARTIFACT_CHECK_FAILED')
  bad=w/'bad-cem';bad.mkdir();broken=copy.deepcopy(cem);del broken['modules'][0]['declarations'][0]['kind'];write(bad/'interface.json',broken);run('original-cem-rejection',['inspect','--candidate',str(bad)],'FAIL','ARTIFACT_CHECK_FAILED')
  bad=w/'bad-scxml';bad.mkdir();(bad/'behavior.scxml').write_text(raw['behavior.scxml'].replace('version="1.0"','version="2.0"'));run('original-scxml-rejection',['inspect','--candidate',str(bad)],'FAIL','ARTIFACT_CHECK_FAILED')
  bad=w/'unsupported-version';bad.mkdir();other=copy.deepcopy(cem);other['schemaVersion']='99.0';write(bad/'interface.json',other);r=run('unsupported-version-blocks',['inspect','--candidate',str(bad)],'BLOCKED','SEMANTIC_PROFILE_UNSUPPORTED');assert r['artifacts'][0]['status']=='BLOCKED'
  fake=w/'missing-runtime';(fake/'tools/validation').mkdir(parents=True);(fake/'components').mkdir();(fake/'tools/validation/check.py').write_text('raise RuntimeError("must not execute")');write(fake/'tools/validation/profile.json',{});write(fake/'components/library.json',{});run('missing-required-runtime',['validate'],'BLOCKED','REQUIRED_VALIDATION_RUNTIME_MISSING',repo=fake)
  run('missing-project',['validate'],'BLOCKED','PROJECT_PREREQUISITE_MISSING',repo=w/'not-a-project')
  run('report-cannot-overwrite-skill',['validate','--output',str(skill/'SKILL.md')],'BLOCKED','UNSAFE_REPORT_PATH')
  run('report-cannot-overwrite-schema',['validate','--output',str(ROOT/'tools/validation/schemas/cem.schema.json')],'BLOCKED','UNSAFE_REPORT_PATH')
  stale=w/'stale-browser';shutil.copytree(CURRENT,stale);request=json.loads((stale/'request.json').read_text());request['createdAt']-=86400;write(stale/'request.json',request);run('stale-browser-never-passes',['validate','--browser-run',str(stale)],'BLOCKED','BROWSER_RUN_STALE')
  run('historical-captures-not-current',['validate','--browser-run',str(ROOT/'docs/research/experiments/2026-10-25/ip01-browser')],'BLOCKED','BROWSER_RESULT_MISSING')
 assert before=={str(p):h(p)for root in [ROOT/'libraries/example',ROOT/'docs/research/studies',BASE]for p in root.rglob('*')if p.is_file()}
 assert installed_hashes=={str(p.relative_to(skill)):h(p)for p in skill.rglob('*')if p.is_file()}
 out={'kind':'installed-ui-contracts-skill-functional-check','date':'2026-10-26','skillPath':str(skill),'sourceMatchesInstalled':True,'skillFileHashes':installed_hashes,'inputOriginalsUnchanged':True,'independentAgentForwardTestPerformed':False,'newBrowserExecutionClaimed':False,'existingBrowserEvidenceAgeAtTestSeconds':age,'newOriginalFormatFixture':raw,'cases':rows,'allExpectationsMet':all(r['expectationMet']for r in rows)};write(OUT/'results.json',out);print('TOTAL',len(rows),'MET',sum(r['expectationMet']for r in rows));return 0 if out['allExpectationsMet']else 1
if __name__=='__main__':raise SystemExit(main())
