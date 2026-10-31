#!/usr/bin/env python3
"""Local thin-entrypoint checks; never measure or claim a host's full context/token count."""
import argparse,hashlib,importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]

def inspect(repo,skill):
 spec=importlib.util.spec_from_file_location('shared_entrypoints',ROOT/'tools/skill-tests/ui-contracts/check_entrypoints.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 shared=m.inspect(repo);errors=list(shared['errors']);files={}
 targets=[(skill/'SKILL.md',3200)]+[(p,3500) for p in sorted((skill/'references/roles').glob('*.md'))]
 for path,cap in targets:
  if not path.is_file():errors.append('Missing '+str(path));continue
  text=path.read_text();name=str(path.relative_to(skill));files[name]={'characters':len(text),'utf8Bytes':len(path.read_bytes()),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'characterBudget':cap}
  if len(text)>cap:errors.append(name+' exceeds local thin-entry budget')
  if re.search(r'(?m)^\s*@\S+',text):errors.append(name+' contains an eager file import')
  for ref in re.findall(r'\]\(([^)]+)\)',text):
   if '://' not in ref and not ref.startswith('#') and not (path.parent/ref.split('#')[0]).exists():errors.append(name+' has missing route '+ref)
 return {'overall':'PASS_LIMITED' if not errors else 'FAIL','release':False,'scope':'Static routing/link/character guard for core skill and one-role-at-a-time entrypoints','errors':errors,'sharedEntrypoints':shared,'skillFiles':files,'notChecked':['Actual platform/system/tool prompt','Automatic global memory','Actual initial request tokens','Whether an agent follows lazy loading','Model quality']}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=ROOT);p.add_argument('--skill',type=Path,default=ROOT/'skills/ui-contracts');p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=inspect(a.repo,a.skill)
 with a.output.open('x') as f:json.dump(r,f,ensure_ascii=False,indent=2)
 print(json.dumps({'overall':r['overall'],'coreCharacters':r['skillFiles'].get('SKILL.md',{}).get('characters'),'errors':r['errors'],'release':False}));raise SystemExit(0 if not r['errors'] else 1)
