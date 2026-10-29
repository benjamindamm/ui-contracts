#!/usr/bin/env python3
"""Static startup-file guard; does not claim any host loaded these files."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

def inspect(root):
    limits={'AGENTS.md':1800,'CLAUDE.md':500,'GEMINI.md':500}
    files={};errors=[]
    for name,cap in limits.items():
        path=root/name
        if not path.is_file():errors.append('Missing '+name);continue
        text=path.read_text()
        files[name]={'characters':len(text),'utf8Bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
        if len(text)>cap:errors.append(name+' exceeds local startup-file budget')
        if re.search(r'(?m)^\s*@\S+',text):errors.append(name+' contains an eager file import')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if '://' not in target and not (root/target).exists():errors.append(name+' missing target: '+target)
        if name!='AGENTS.md' and '[AGENTS.md](AGENTS.md)' not in text:errors.append(name+' lacks common entry reference')
    return {'scope':'Static repository entrypoint guard; no host startup/runtime test',
            'passed':not errors,'errors':errors,'files':files,'limitsInCharacters':limits,
            'combinedCharacters':sum(f['characters'] for f in files.values()),
            'actualHostRecognitionVerified':False,'globalMemoryInspected':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--repo',type=Path,default=ROOT)
    parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    report=inspect(args.repo.resolve());args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report));raise SystemExit(0 if report['passed'] else 1)
