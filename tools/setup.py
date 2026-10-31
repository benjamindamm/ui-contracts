#!/usr/bin/env python3
"""Provision pinned project dependencies in the checkout; no pre-built /tmp runtime required."""
import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def command(args, log):
    proc = subprocess.run([str(x) for x in args], cwd=ROOT, capture_output=True, text=True, timeout=600)
    log.append({'command': [str(x) for x in args], 'exitCode': proc.returncode,
                'stdout': proc.stdout[-5000:], 'stderr': proc.stderr[-5000:]})
    if proc.returncode: raise ValueError('Dependency command failed: ' + str(args[0]) + '\n' + proc.stderr[-1200:])
    return (proc.stdout + proc.stderr).strip()

def jars(dest, downloader=None):
    lock = json.loads((ROOT/'tools/ux/runtime.lock.json').read_text())
    urls = json.loads((ROOT/'tools/ux/runtime-artifacts.json').read_text())['urls']
    if set(urls) != set(lock['jars']): raise ValueError('Download recipe differs from engine lock')
    dest.mkdir(parents=True, exist_ok=True); (dest/'jars').mkdir(exist_ok=True)
    result=[]
    for name, expected in lock['jars'].items():
        target=dest/'jars'/name
        if target.exists():
            if sha(target) != expected: raise ValueError('Existing runtime file has wrong hash: '+name)
            result.append({'name':name,'sha256':expected,'cached':True});continue
        url=urls[name]
        if not url.startswith('https://repo.maven.apache.org/maven2/'): raise ValueError('Unsupported artifact registry')
        # Standard HTTPS verification stays enabled. Hash lock verifies downloaded bytes before use.
        data=downloader(url) if downloader else urllib.request.urlopen(url,timeout=90).read(50_000_001)
        if len(data)>50_000_000 or hashlib.sha256(data).hexdigest()!=expected: raise ValueError('Downloaded artifact hash mismatch: '+name)
        with target.open('xb') as out:out.write(data)
        result.append({'name':name,'sha256':expected,'cached':False})
        print('Fetched pinned engine artifact: '+name,flush=True)
    (dest/'classpath.txt').write_text(os.pathsep.join(str((dest/'jars'/name).resolve()) for name in lock['jars'])+'\n')
    write(dest/'receipt.json',{'format':'ui-contracts-runtime-install/1','lockSha256':sha(ROOT/'tools/ux/runtime.lock.json'),'artifacts':result})
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--java',help='Java 17+ executable; otherwise JAVA_HOME/PATH')
    parser.add_argument('--dmn-only',action='store_true')
    args=parser.parse_args();local=ROOT/'.runtime';local.mkdir(exist_ok=True);log=[]
    try:
        explicit=args.java or (str(Path(os.environ['JAVA_HOME'])/'bin/java') if os.environ.get('JAVA_HOME') else None)
        java=shutil.which(explicit or 'java')
        if not java:raise ValueError('Install a JDK 17+ or supply --java; setup does not change system package managers.')
        version=command([java,'-version'],log)
        match=re.search(r'version \"(\d+)',version)
        if not match or int(match.group(1))<17:raise ValueError('JDK 17+ required')
        compiler=Path(java).resolve().parent/'javac'
        if not compiler.is_file():compiler=Path(shutil.which('javac') or '/missing-javac')
        if not compiler.is_file():raise ValueError('JDK compiler javac missing')
        if not args.dmn_only:
            print('Preparing isolated Python environment',flush=True)
            env=ROOT/'tools/validation/.venv';python=env/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
            if not python.is_file():command([sys.executable,'-m','venv',env],log)
            command([python,'-m','pip','install','--disable-pip-version-check','-r',ROOT/'tools/validation/requirements.lock.txt'],log)
            node=shutil.which('node');npm=shutil.which('npm')
            if not node or not npm:raise ValueError('Install Node.js/npm; Node 22+ is required, Node 24 is the tested baseline')
            node_version=command([node,'--version'],log)
            if int(node_version.lstrip('v').split('.')[0])<22:raise ValueError('Node 22+ required')
            for directory in ['tools/validation','tools/openpencil','tools/charts']:
                print('Installing locked Node dependencies: '+directory,flush=True)
                command([npm,'ci','--prefix',ROOT/directory,'--ignore-scripts','--no-audit','--no-fund'],log)
        engine=jars(local/'dmn')
        config={'format':'ui-contracts-local-runtime/1','java':str(Path(java).resolve()),'javac':str(compiler.resolve()),'dmn':'dmn'}
        write(local/'config.json',config)
        receipt={'overall':'READY','release':False,'scope':'pinned local dependency provisioning','python':sys.version,'platform':platform.platform(),
                 'javaVersion':version,'engineArtifacts':engine,'commands':log,
                 'locks':{name:sha(ROOT/name) for name in ['tools/validation/requirements.lock.txt','tools/validation/package-lock.json','tools/openpencil/package-lock.json','tools/charts/package-lock.json','tools/ux/runtime.lock.json','tools/ux/runtime-artifacts.json']}}
        write(local/'setup.json',receipt);print(json.dumps({'overall':'READY','release':False,'receipt':str(local/'setup.json')}));return 0
    except Exception as error:
        write(local/'setup-failed.json',{'overall':'BLOCKED','diagnostic':str(error),'commands':log})
        print(json.dumps({'overall':'BLOCKED','release':False,'diagnostic':str(error)}));return 2

if __name__=='__main__':raise SystemExit(main())
