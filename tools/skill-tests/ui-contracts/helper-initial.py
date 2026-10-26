#!/usr/bin/env python3
"""Delegate the UI-Contracts gate, or inspect original artifacts without claiming full validation."""
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
SKILL=Path(__file__).resolve().parents[1]

def blocked(code,detail):return {'kind':'ui-contracts-skill-result','overall':'BLOCKED','release':False,'diagnostic':{'code':code,'detail':detail},'passedScope':[]}
def repository(explicit):
 if explicit:return explicit.resolve()
 for p in [Path.cwd(),*Path.cwd().parents]:
  if(p/'tools/validation/check.py').is_file()and(p/'components/library.json').is_file():return p
 return None

def inspect(repo,candidate):
 sys.path.insert(0,str(repo/'tools/validation'));import check
 readiness=check.run(repo/'docs/research/experiments/2026-10-25/ip01-static/reference','static')
 if readiness['overall']!='PASS_LIMITED':
  r=blocked('REQUIRED_PROJECT_CHECKER_UNAVAILABLE','The existing reference check did not establish tool readiness.');r['toolReadinessNotCandidateValidation']=readiness;return r
 from lxml import etree,html
 import jsonschema
 schemas=repo/'tools/validation/schemas'
 cv=jsonschema.Draft7Validator(check.strict((schemas/'cem.schema.json').read_text()))
 parser=etree.XMLParser(resolve_entities=False,no_network=True)
 xsd=etree.XMLSchema(etree.parse(str(schemas/'scxml/scxml.xsd'),parser));rows=[]
 if not candidate or not candidate.exists():return blocked('CANDIDATE_MISSING',str(candidate))
 candidates=[candidate]if candidate.is_file()else sorted(candidate.rglob('*'))
 for p in candidates:
  if any(part in ['.git','node_modules','.venv','__pycache__']for part in p.parts)or not p.is_file():continue
  suffix=p.suffix.lower()
  if suffix not in ['.json','.scxml','.xml','.css','.html']:continue
  row={'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checks':[],'status':'PASS_LIMITED'}
  try:
   if p.is_symlink():raise ValueError('Symlink candidates are not inspected.')
   text=p.read_text(encoding='utf-8')
   if suffix=='.json':
    obj=check.strict(text);row['checks'].append({'checker':'strict JSON syntax','accepted':True})
    if p.name=='interface.json'or isinstance(obj,dict)and'schemaVersion'in obj and'modules'in obj:
     if not isinstance(obj,dict)or obj.get('schemaVersion')!='2.1.0':row.update(status='BLOCKED',diagnostic='UNSUPPORTED_CEM_VERSION')
     else:
      errors=[e.message for e in cv.iter_errors(obj)];row['checks'].append({'checker':'original CEM 2.1.0 schema / Draft 7','accepted':not errors,'errors':errors})
      if errors:row['status']='FAIL'
    else:row['unchecked']='JSON meaning, token types/aliases, own component/projection rules and cross-file semantics'
   elif suffix in ['.scxml','.xml']:
    if '<!DOCTYPE'in text or'<!ENTITY'in text:raise ValueError('XML DTD/entity declarations are unsupported.')
    obj=etree.fromstring(text.encode(),parser);row['checks'].append({'checker':'XML well-formedness without external entities','accepted':True})
    if suffix=='.scxml'or obj.tag=='{http://www.w3.org/2005/07/scxml}scxml':
     ok=xsd.validate(obj);row['checks'].append({'checker':'original loose SCXML 1.0 XSD','accepted':ok,'errors':str(xsd.error_log)})
     if not ok:row['status']='FAIL'
    else:row.update(status='BLOCKED',diagnostic='UNSUPPORTED_XML_SEMANTICS')
   elif suffix=='.css':
    run=subprocess.run(['node',str(repo/'tools/validation/css.cjs')],input=json.dumps({p.name:text}),capture_output=True,text=True,timeout=15)
    data=check.strict(run.stdout);row['checks'].append({'checker':'css-tree syntax, additional checker','accepted':run.returncode==0,'evidence':data})
    if run.returncode:row['status']='FAIL'
   elif suffix=='.html':
    html.fromstring(text);row['checks'].append({'checker':'recovering HTML parser; NOT a conformance validator','accepted':True});row['unchecked']='HTML/ARIA/APG conformance and runtime accessibility'
  except Exception as e:row.update(status='FAIL',diagnostic=type(e).__name__+': '+str(e))
  rows.append(row)
 if not rows:return blocked('CANDIDATE_EMPTY','No supported original-format artifacts found.')
 errors=[r for r in rows if r['status']=='FAIL'];r=blocked('SEMANTIC_PROFILE_UNSUPPORTED','Only syntax and the available original schemas were inspected. This candidate has no general semantic/profile/runtime acceptance through this helper.')
 if errors:r.update(overall='FAIL',diagnostic={'code':'ARTIFACT_CHECK_FAILED','detail':'Candidate syntax or an available original schema was rejected.'})
 r.update(kind='ui-contracts-original-artifact-inspection',candidate=str(candidate),artifacts=rows,passedScope=[{'file':r['file'],'checks':r['checks']}for r in rows if r['status']=='PASS_LIMITED'],warnings=['Original SCXML schema is loose; HTML parsing is not conformance.','DTCG/CSS/HTML/ARIA/APG are not fully original-validated.'],unverified=['General cross-file references, ownership and composition for this candidate','Runtime events, focus, scrolling, AX, lifecycle','Target generation, screenreader, real IME and native platforms'],productionRelease=False)
 return r

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('action',choices=['inspect','validate']);ap.add_argument('--repo',type=Path);ap.add_argument('--candidate',type=Path);ap.add_argument('--scope',choices=['static','web'],default='web');ap.add_argument('--browser-run',type=Path);ap.add_argument('--output',type=Path);a=ap.parse_args();repo=repository(a.repo)
 candidate=a.candidate.resolve()if a.candidate else None
 protected=[SKILL]+([candidate]if candidate else[])+([repo/p for p in ['components','docs/research','tools/validation','skills','examples']]if repo else[])
 if a.output and any(a.output.resolve().is_relative_to(p.resolve())for p in protected):
  print(json.dumps(blocked('UNSAFE_REPORT_PATH','Reports must not overwrite candidate, checker, skill or historical evidence.')));return 2
 if not repo or not all((repo/p).is_file()for p in ['tools/validation/check.py','tools/validation/profile.json','components/library.json']):r=blocked('PROJECT_PREREQUISITE_MISSING','Select the UI-Contracts project with its existing validation tools and component library.')
 else:
  runtime=repo/'tools/validation/.venv/bin/python'
  if not runtime.is_file():r=blocked('REQUIRED_VALIDATION_RUNTIME_MISSING',str(runtime))
  elif a.action=='validate':
   cmd=[str(runtime),str(repo/'tools/validation/check.py'),'--scope',a.scope]
   if candidate:cmd+=['--package',str(candidate)]
   if a.browser_run:cmd+=['--browser-run',str(a.browser_run.resolve())]
   try:
    out=subprocess.run(cmd,capture_output=True,text=True,timeout=90);r=json.loads(out.stdout)
    if out.returncode!={'PASS_LIMITED':0,'FAIL':1,'BLOCKED':2}.get(r.get('overall')) or not isinstance(r.get('release'),bool):r=blocked('CHECKER_EXECUTION_FAILED',out.stderr[-1500:])
   except Exception as e:r=blocked('CHECKER_EXECUTION_FAILED',str(e))
  else:
   if Path(sys.prefix).resolve()!=runtime.parent.parent.resolve():os.execv(str(runtime),[str(runtime),str(Path(__file__).resolve()),*sys.argv[1:]])
   try:r=inspect(repo,candidate)
   except Exception as e:r=blocked('INSPECTION_CHECKER_FAILED',type(e).__name__+': '+str(e))
 r['skill']={'name':'ui-contracts','skillSha256':hashlib.sha256((SKILL/'SKILL.md').read_bytes()).hexdigest(),'helperSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 text=json.dumps(r,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
 if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
 print(text,end='');return {'PASS_LIMITED':0,'FAIL':1,'BLOCKED':2}[r['overall']]
if __name__=='__main__':raise SystemExit(main())
