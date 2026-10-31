#!/usr/bin/env python3
"""Recompute bounded browser assertions from raw captures; never accept a page's pass flag."""
import argparse,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/libraries'))
from manage import manifest as library_manifest

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(run,repo=ROOT):
 checks=[]
 def require(id,test):checks.append({'id':id,'passed':bool(test)})
 try:
  m=json.loads((run/'manifest.json').read_text());cases=json.loads((run/'cases.json').read_text());captures={}
  require('fresh-run-within-two-hours',0 <= (datetime.now(timezone.utc)-datetime.fromisoformat(m['preparedAt'])).total_seconds() <= 7200)
  require('current-library-revision',library_manifest(repo,m['library'])['revision']==m['revision'])
  for name,h in m['files'].items():require('bound-file:'+name,sha(run/name)==h)
  for name,h in m['tools'].items():require('bound-tool:'+name,sha(repo/name)==h)
  for name in cases['cases']:
   c=json.loads((run/'captures'/(name+'.json')).read_text());captures[name]=c
   require(name+':binding',c['name']==name and c['challenge']==m['challenge'] and c['sourceRevision']==m['revision'])
   require(name+':no-runtime-errors',not c['snapshot']['errors'] and not c['controls']['errors'])
  def c(n):return captures[n]
  def a(n):return c(n)['snapshot']['A']
  def state(n,k):return c(n)['controls']['states'][k]
  require('initial-closed',a('initial')['phase']=='closed' and a('initial')['expanded']=='false')
  require('loading-busy',a('ac-loading')['phase']=='loading' and a('ac-loading')['busy']=='true' and a('ac-loading')['expanded']=='true')
  require('provider-supplied-order', [r['key'] for r in a('ac-ready')['data']['results']]==['A-'+str(i) for i in range(1,13)])
  require('ready-without-commit',a('ac-ready')['phase']=='ready' and not a('ac-ready')['data'].get('value') and not c('ac-ready')['snapshot']['events']['A'])
  require('scroll-focus-retained',a('ac-scroll')['data']['activeKey']=='A-12' and c('ac-scroll')['snapshot']['focus']=='A-input' and a('ac-scroll')['viewport']['scrollTop']>0)
  measures=[r for r in c('ac-scroll')['journal'] if r['type']=='host.measure' and r['key']=='A-12']
  require('actual-scroll-geometry',bool(measures) and measures[-1]['visible'] and measures[-1]['offset']>0 and measures[-1]['option']['top']>=measures[-1]['viewport']['top']-.5 and measures[-1]['option']['bottom']<=measures[-1]['viewport']['bottom']+.5)
  ev=c('ac-commit')['snapshot']['events']['A']
  require('actual-public-commit',len(ev)==1 and ev[0]['detail']=={'value':'A-12'} and ev[0]['focus']=='A-input' and a('ac-commit')['phase']=='closed' and a('ac-commit')['inputValue']=='Stadt 12')
  require('isolation',c('ac-isolation')['snapshot']['B']['phase']=='ready' and a('ac-isolation')['data'].get('value')=='A-12' and len(c('ac-isolation')['snapshot']['events']['A'])==1)
  require('stale-result-rejected',a('ac-stale')['data']['results'][0]['key']=='fresh' and a('ac-stale')['data']['stale']>0)
  require('empty',a('ac-empty')['phase']=='empty' and a('ac-empty')['status']=='Keine Städte gefunden.')
  require('invalid-provider',a('ac-invalid')['phase']=='error' and any(d['rule']=='provider.type' for d in c('ac-invalid')['snapshot']['diagnostics']))
  require('disabled-closes',a('ac-disabled')['phase']=='closed' and c('ac-disabled')['payload']['disabled'] is True)
  require('input-preserves-text',state('input-edit','Input')['value']=='0123 Straße' and any(e['detail']=={'value':'0123 Straße'} for e in c('input-edit')['controls']['events']['Input']))
  require('readonly',state('input-readonly','Input')['readOnly'] and state('input-readonly','Input')['value']=='0123 Straße')
  require('native-select-commit',state('select-commit','Select')['value']=='K3' and c('select-commit')['controls']['events']['Select'][-1]['detail']=={'value':'K3','reason':'user'})
  require('actual-query-filter', [o['key'] for o in state('search-filter','SelectWithSearch')['options']]==['K30'] and not state('search-filter','SelectWithSearch')['value'])
  s=state('search-navigation','SelectWithSearch')
  require('search-navigates-uncommitted',s['phase']=='opened' and s['data']['activeKey']=='K30' and not s['value'] and s['scrollTop']>0 and s['focus']=='SelectWithSearch-option-K30')
  require('search-commit-restores-focus',state('search-commit','SelectWithSearch')['value']=='K30' and state('search-commit','SelectWithSearch')['phase']=='closed' and state('search-commit','SelectWithSearch')['focus']=='SelectWithSearch-trigger' and c('search-commit')['controls']['events']['SelectWithSearch'][-1]['detail']=={'value':'K30','reason':'user'})
  require('escape-keeps-selection',state('search-escape','SelectWithSearch')['phase']=='closed' and state('search-escape','SelectWithSearch')['value']=='K30' and len(c('search-escape')['controls']['events']['SelectWithSearch'])==1)
  # Actual browser accessibility tree is separate from HTML attributes.
  ax=c('ac-scroll')['payload']['ax'];nodes=ax.get('nodes',[])
  combos=[n for n in nodes if n.get('role',{}).get('value')=='combobox']
  require('browser-AX-combobox-present',bool(combos))
  require('browser-AX-expanded-focused',any(any(p['name']=='expanded' and p['value'].get('value') is True for p in n.get('properties',[])) and any(p['name']=='focused' and p['value'].get('value') is True for p in n.get('properties',[])) for n in combos))
  require('trusted-key-events',any(r['type']=='dom.key' and r.get('isTrusted') and r.get('key')=='ArrowDown' for r in c('ac-scroll')['journal']))
  require('trusted-input-events',any(r['type']=='dom.input' and r.get('isTrusted') for r in c('ac-ready')['journal']))
  return {'overall':'PASS_LIMITED' if all(r['passed'] for r in checks) else 'FAIL','release':False,'checks':checks,'sourceRevision':m['revision'],'captureHashes':{n:sha(run/'captures'/(n+'.json')) for n in cases['cases']},'notChecked':cases['notChecked']}
 except Exception as e:return {'overall':'BLOCKED','release':False,'checks':checks,'diagnostic':str(e)}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',type=Path,required=True);p.add_argument('--output',type=Path);a=p.parse_args();r=check(a.run.resolve())
 if a.output:
  with a.output.open('x') as out:json.dump(r,out,indent=2)
 print(json.dumps({'overall':r['overall'],'checks':len(r['checks']),'failed':[x['id'] for x in r['checks'] if not x['passed']],'diagnostic':r.get('diagnostic'),'release':False}));sys.exit(0 if r['overall']=='PASS_LIMITED' else 1)
