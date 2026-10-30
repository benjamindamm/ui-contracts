import json,hashlib,subprocess,os
from pathlib import Path
HERE=Path(__file__).resolve().parent;prior=HERE.parent/'01';out=HERE/'results';out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,v:p.write_text(json.dumps(v,indent=2)+'\n')
contexts=json.loads((prior/'fixtures/contexts.json').read_text())
# Revised profile after the disclosed run-01 fault. Not a blind reproduction.
expected={'complete':'candidate','excluded':'unsuitable','missing':'unknown','explicit-null':'unknown','explicit-false':'unsuitable','wrong-type':'invalid-input'}
freeze={'inputs':{str(p.relative_to(HERE.parent)):sha(p) for p in [HERE/'policy.rego',HERE/'probe.py',prior/'fixtures/contexts.json']},'expected':expected,'scope':'Own Rego policy repair only, native engine unchanged'};write(HERE/'freeze.json',freeze)
opa=os.environ.get('OPA','/tmp/ui-contracts-ux-rules-runtime/opa');rows=[]
for c in contexts:
 p=subprocess.run([opa,'eval','--format=json','--data',str(HERE/'policy.rego'),'--stdin-input','data.uxprobe'],input=json.dumps(c['input']),text=True,capture_output=True,timeout=15)
 value=json.loads(p.stdout)['result'][0]['expressions'][0]['value'] if p.returncode==0 else None
 rows.append({'id':c['id'],'input':c['input'],'expected':expected[c['id']],'value':value,'met':value is not None and value['decision']==expected[c['id']],'exitCode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
write(out/'observations.json',rows)
summary={'overall':'PASS_LIMITED' if all(r['met'] for r in rows) else 'FAIL','release':False,'checks':len(rows),'expectationsMet':sum(r['met'] for r in rows),'repair':'Explicit object.get missing/null guards before is_boolean and invalid-input classification','opaSha256':sha(Path(opa)),'nativeFrameworkFeatureClaim':False,'priorRunUnmodified':True}
write(out/'summary.json',summary);print(json.dumps(summary));raise SystemExit(0 if summary['overall']=='PASS_LIMITED' else 1)
