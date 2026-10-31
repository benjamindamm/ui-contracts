#!/usr/bin/env python3
"""Inventory the information architecture and check active routes, without rewriting evidence."""
import argparse,json,os,re,subprocess
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ENTRIES=['README.md','AGENTS.md','CLAUDE.md','GEMINI.md','docs/README.md','docs/ARCHITECTURE.md','docs/STATUS.md','docs/skills/README.md','docs/research/README.md','skills/ui-contracts/SKILL.md']
SKIP={'.git','node_modules','.venv','.runtime','__pycache__'}
def tier(name):
 if name in ['README.md','AGENTS.md','CLAUDE.md','GEMINI.md','skills/ui-contracts/SKILL.md']:return '1-essence'
 if name in ENTRIES or name in ['TASKS.md','libraries/README.md','docs/research/DOCUMENT-INDEX.md']:return '2-routes'
 if name.startswith('libraries/'):return '4-original-definitions'
 if name.startswith(('docs/research/','examples/','docs/libraries/frozen/')) or '/evidence/' in name:return '5-research-and-evidence'
 return '3-task-details-and-tooling'
def scan(repo,entries=None):
 repo=repo.resolve();catalog=[];links=[];errors=[];entries=ENTRIES if entries is None else entries
 listed=subprocess.run(['git','-C',str(repo),'ls-files','--cached','--others','--exclude-standard','-z'],capture_output=True)
 if listed.returncode==0:
  paths=[repo/n for n in listed.stdout.decode().split('\0') if n];method='git-nonignored-files'
 else:
  paths=[];method='filesystem-pruned'
  for folder,dirs,files in os.walk(repo):
   dirs[:]=sorted(d for d in dirs if d not in SKIP)
   paths += [Path(folder)/f for f in sorted(files)]
 for p in paths:
  if p.is_symlink() or not p.is_file():continue
  name=str(p.relative_to(repo));catalog.append({'path':name,'tier':tier(name),'bytes':p.stat().st_size})
 for name in entries:
  p=repo/name
  if not p.is_file():errors.append('Missing active entry '+name);continue
  for ref in re.findall(r'\]\(([^)\n]+)\)',p.read_text()):
   if '://' in ref or ref.startswith(('#','mailto:')):continue
   path=ref.strip('<>').split('#')[0]
   if not path:continue
   target=(p.parent/path).resolve();ok=target.is_relative_to(repo) and target.exists();links.append({'from':name,'to':str(target.relative_to(repo)) if target.is_relative_to(repo) else 'outside-repo','exists':ok})
   if not ok:errors.append(name+' has missing/escaping route '+ref)
 return {'overall':'PASS_LIMITED' if not errors else 'FAIL','release':False,'scope':'Filesystem inventory and active entrypoint link graph; historical file contents not rewritten or recursively validated','errors':errors,'inventoryMethod':method,'counts':dict(Counter(p['tier'] for p in catalog)),'activeEntries':entries,'links':links,'files':catalog,'notChecked':['Semantic completeness of all knowledge','Every historical copied link','Host automatic loading','Model token usage','Model quality']}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=ROOT);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=scan(a.repo)
 with a.output.open('x') as out:json.dump(r,out,ensure_ascii=False,indent=2)
 print(json.dumps({'overall':r['overall'],'counts':r['counts'],'errors':r['errors'],'release':False}));raise SystemExit(0 if not r['errors'] else 1)
