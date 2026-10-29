#!/usr/bin/env python3
"""Validate comparability metadata for FUTURE runs; never backfill provenance.

File references are relative to the metadata file. Recorded hashes prove present
file integrity, not historic timing, access isolation or authenticity of statements.
"""
import argparse
import hashlib
import json
from pathlib import Path

def verify(data, base):
    errors=[]
    def require(ok,code):
        if not ok:errors.append(code)
    def bound_file(ref,code):
        if not isinstance(ref,dict):
            errors.append(code+':missing');return
        p=(base/ref.get('path','')).resolve()
        require(p.is_file(),code+':file-missing')
        if p.is_file():
            require(hashlib.sha256(p.read_bytes()).hexdigest()==ref.get('sha256'),code+':hash-mismatch')
    for k in ['runId','definitionRevision','toolchainLockSha256','harnessVersion','comparisonPolicyId']:
        require(bool(data.get(k)),k+':missing')
    for k in ['definitionRevision','toolchainLockSha256']:
        v=data.get(k)
        require(isinstance(v,str) and len(v)==64 and all(c in '0123456789abcdef' for c in v),k+':not-sha256')
    bound_file(data.get('comparisonPolicy'),'comparisonPolicy')
    roles=data.get('roles',{})
    require(isinstance(roles,dict),'roles:not-object')
    if not isinstance(roles,dict):roles={}
    for name in ['builderA','builderB','reviewer']:
        r=roles.get(name) or {}
        for k in ['model','modelRevision','reasoning','harnessStepLimit','contextPolicy']:
            require(r.get(k) is not None and r.get(k)!='',name+'.'+k+':missing')
        bound_file(r.get('initialPrompt'),name+'.initialPrompt')
        # Skill omission must be explicit, not guessed from final artifacts.
        require(isinstance(r.get('skills'),list),name+'.skills:not-recorded')
        for i,s in enumerate(r.get('skills') or []):bound_file(s,name+f'.skill{i}')
    events=data.get('events')
    require(isinstance(events,list),'events:not-recorded')
    ids=set();open_stops={};last_time=''
    for i,e in enumerate(events or []):
        prefix=f'event{i}'
        require(e.get('id') is not None and e['id'] not in ids,prefix+':missing-or-duplicate-id')
        ids.add(e.get('id'))
        stamp=e.get('at')
        require(isinstance(stamp,str) and stamp.endswith('Z'),prefix+':utc-time-required')
        if isinstance(stamp,str):
            require(stamp>=last_time,prefix+':not-chronological');last_time=stamp
        actor=e.get('actor');require(actor in roles,prefix+':unknown-actor')
        kind=e.get('kind');require(kind in ['start','stop','resume','complete'],prefix+':unknown-kind')
        if kind=='stop':
            require(actor not in open_stops,prefix+':stop-already-open')
            open_stops[actor]=e.get('id')
            require(bool(e.get('cause')),prefix+':cause-missing')
            require(isinstance(e.get('stepsUsed'),int),prefix+':steps-missing')
            bound_file(e.get('checkpoint'),prefix+'.checkpoint')
        elif kind=='resume':
            require(actor in open_stops and e.get('stopId')==open_stops.get(actor),prefix+':stop-link-mismatch')
            require(e.get('sameSession') is True,prefix+':context-continuity-not-confirmed')
            bound_file(e.get('message'),prefix+'.message')
            require(e.get('semanticCoaching') is False,prefix+':changed-prompt-condition')
            open_stops.pop(actor,None)
        elif kind=='complete':
            require(actor not in open_stops,prefix+':completion-without-resume')
    require(not open_stops,'unresolved-stop')
    for name in roles:
        kinds=[e.get('kind') for e in events or [] if e.get('actor')==name]
        require(kinds.count('start')==1 and kinds.count('complete')==1,name+':start-complete-not-recorded')
        require(bool(kinds) and kinds[0]=='start' and kinds[-1]=='complete',name+':event-boundaries-invalid')
    return {'overall':'BLOCKED' if errors else 'METADATA_COMPLETE', 'release':False,
            'errors':errors,'scope':'Recorded comparability metadata and referenced file integrity only; not artifact quality or an access/timing audit.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--metadata',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    a=p.parse_args()
    if a.metadata.resolve()==a.output.resolve():p.error('Input must not be overwritten')
    r=verify(json.loads(a.metadata.read_text()),a.metadata.resolve().parent)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({'overall':r['overall'],'errors':len(r['errors'])}))
    return 2 if r['errors'] else 0

if __name__=='__main__':raise SystemExit(main())
