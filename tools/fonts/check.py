#!/usr/bin/env python3
"""Bounded local font asset/token checks. Not a DTCG or universal font validator."""
import argparse
import hashlib
import json
import re
import struct
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/libraries'))
from manage import library_root


def asset(root,ref):
    value=ref.get('path');p=Path(value) if isinstance(value,str) else None
    if not p or p.is_absolute() or '..' in p.parts:raise ValueError('Asset must be library-relative without ..')
    path=root/p
    if any(x.is_symlink() for x in [path,*path.parents] if x.is_relative_to(root)) or not path.resolve().is_relative_to(root.resolve()):raise ValueError('Asset escapes library or uses symlink')
    data=path.read_bytes()
    if not re.fullmatch('[0-9a-f]{64}',str(ref.get('sha256',''))) or hashlib.sha256(data).hexdigest()!=ref['sha256']:raise ValueError('Asset hash mismatch: '+value)
    return path,data


def sfnt(data):
    if data[:4]!=b'\x00\x01\x00\x00':raise ValueError('Only static TrueType sfnt supported by this metadata check')
    n=struct.unpack_from('>H',data,4)[0];tables={}
    for i in range(n):
        tag,_,start,length=struct.unpack_from('>4sIII',data,12+i*16)
        if start+length>len(data):raise ValueError('Invalid sfnt table bounds')
        tables[tag.decode('ascii')]=data[start:start+length]
    if 'fvar' in tables:raise ValueError('Variable font metadata not supported by this checker')
    name=tables['name'];_,count,start=struct.unpack_from('>HHH',name,0);names={}
    for i in range(count):
        platform,encoding,language,ident,length,offset=struct.unpack_from('>HHHHHH',name,6+i*12)
        raw=name[start+offset:start+offset+length]
        if len(raw)!=length:raise ValueError('Invalid name record')
        if platform in [0,3]:text=raw.decode('utf-16-be')
        elif platform==1:text=raw.decode('mac_roman')
        else:continue
        if ident not in names or language==0x409:names[ident]=text
    os2=tables['OS/2'];weight=struct.unpack_from('>H',os2,4)[0];selection=struct.unpack_from('>H',os2,62)[0]
    return {'family':names.get(16,names.get(1)),'postScriptName':names.get(6),'weight':weight,
            'italic':bool(selection&1),'glyphCount':struct.unpack_from('>H',tables['maxp'],4)[0],
            'version':names.get(5),'variable':False}


def token(tokens,path,seen=None):
    seen=set() if seen is None else seen
    if path in seen:raise ValueError('Token alias cycle')
    seen.add(path);value=tokens
    for part in path.split('.'):value=value[part]
    if value.get('$type')!='fontFamily':raise ValueError('Binding must refer to a fontFamily token')
    v=value['$value']
    if isinstance(v,str) and v.startswith('{') and v.endswith('}'):return token(tokens,v[1:-1],seen)
    return v


def validate(repo,name):
    repo=repo.resolve()
    root=library_root(repo,name);manifest=json.loads((root/'fonts.json').read_text());tokens=json.loads((root/'tokens.json').read_text())
    if manifest.get('format')!='ui-contracts-font-assets/1':raise ValueError('Unsupported asset manifest format')
    license_meta=manifest.get('license')
    if license_meta is not None and not isinstance(license_meta,dict):raise ValueError('License metadata must be an object or null')
    if license_meta and ('path' in license_meta or 'sha256' in license_meta):
        _,license_data=asset(root,license_meta)
        if not license_data.strip():raise ValueError('Empty declared license file')
        license_evidence={'status':'file-present','fileIntegrity':'pass','rightsReview':'notChecked'}
        warnings=[]
    else:
        license_evidence={'status':'notChecked','reason':'No separate license file provided','rightsReview':'notChecked'}
        warnings=['No separate license file supplied. Technical font checks do not establish usage or redistribution rights.']
    families=manifest['families'];rows=[];keys=set();bound_tokens=set()
    if not families:raise ValueError('No font families bound')
    for family in families:
        fam=family['family']
        if not family['tokenPaths']:raise ValueError('No family token binding')
        for p in family['tokenPaths']:
            value=token(tokens,p)
            if (isinstance(value,str) and value!=fam) or (isinstance(value,list) and fam not in value) or not isinstance(value,(str,list)):raise ValueError('Family token mismatch: '+p)
            bound_tokens.add(p)
        if not family['faces']:raise ValueError('No faces')
        for face in family['faces']:
            key=(fam,face['weight'],face['style'])
            if key in keys:raise ValueError('Duplicate font face')
            keys.add(key)
            if face['style']!='normal' or type(face['weight']) is not int or not 1<=face['weight']<=1000:raise ValueError('Only declared normal static faces supported')
            styles={100:'Thin',200:'ExtraLight',300:'Light',400:'Regular',500:'Medium',600:'SemiBold',700:'Bold',800:'ExtraBold',900:'Black'}
            if styles.get(face['weight'])!=face['openpencilStyle']:raise ValueError('Unsupported weight or wrong OpenPencil style binding')
            formats=set();assets=[];metadata=None
            for ref in face['assets']:
                path,data=asset(root,ref);fmt=ref['format']
                if fmt in formats:raise ValueError('Duplicate font format')
                formats.add(fmt)
                if fmt=='truetype':
                    metadata=sfnt(data)
                    if metadata['family']!=fam or metadata['postScriptName']!=face['postScriptName'] or metadata['weight']!=face['weight'] or metadata['italic']:raise ValueError('TTF metadata differs from declaration')
                elif fmt=='woff2':
                    if data[:4]!=b'wOF2' or len(data)<48 or struct.unpack_from('>I',data,8)[0]!=len(data):raise ValueError('Invalid WOFF2 header')
                else:raise ValueError('Unsupported asset format')
                assets.append({'path':str(path.relative_to(repo)),'format':fmt,'sha256':ref['sha256'],'bytes':len(data)})
            if formats!={'truetype','woff2'}:raise ValueError('This bounded adapter requires TTF and WOFF2 for each face')
            rows.append({'family':fam,'style':face['style'],'weight':face['weight'],'openpencilStyle':face['openpencilStyle'],'ttfMetadata':metadata,'assets':assets})
    return {'overall':'PASS_LIMITED','release':False,'scope':'local-font-assets-and-token-binding','library':name,
            'manifestSha256':hashlib.sha256((root/'fonts.json').read_bytes()).hexdigest(),
            'boundTokens':sorted(bound_tokens),'faces':rows,'license':license_meta,'licenseEvidence':license_evidence,'warnings':warnings,
            'notChecked':['Usage and redistribution rights','Full OpenType conformance','All Unicode coverage','Renderer/browser loading (separate evidence)','Native iOS/Android embedding']}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--repo',type=Path,default=ROOT);ap.add_argument('--library',required=True);ap.add_argument('--output',type=Path);a=ap.parse_args();repo=a.repo.resolve()
    try:result=validate(repo,a.library)
    except (OSError,ValueError,TypeError,KeyError,struct.error) as e:result={'overall':'BLOCKED','release':False,'diagnostic':str(e)}
    if a.output:
        out=a.output.resolve()
        if out.is_relative_to(repo/'libraries') or out.is_relative_to(repo/'examples/autocomplete/reproducibility'):raise ValueError('Report must not overwrite sources/historical runs')
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open('x',encoding='utf-8') as f:f.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False));return 0 if result['overall']=='PASS_LIMITED' else 2

if __name__=='__main__':raise SystemExit(main())
