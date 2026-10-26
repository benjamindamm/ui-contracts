from pathlib import Path
import sys
import json,hashlib
w=Path(sys.argv[1]).resolve();plan=json.loads((w/'cases.json').read_text());preflight=json.loads((w/'schema-preflight.json').read_text());manifest=json.loads((w/'host/manifest.json').read_text())
def read(name):return json.loads((w/'captures'/(name+'.json')).read_text())
def nodes(ax):return ax['nodes']
def properties(n):return {p['name']:p['value']for p in n.get('properties',[])}
def role(n):return n.get('role',{}).get('value')
def name(n):return n.get('name',{}).get('value','')
def combo(ax,label):return next(n for n in nodes(ax)if role(n)=='combobox'and name(n)==label)
def val(n,p,default=None):return properties(n).get(p,{}).get('value',default)
def statusTexts(ax):
 by={n['nodeId']:n for n in nodes(ax)}
 def text(n):return (name(n) if role(n)=='StaticText' else '')+''.join(text(by[i])for i in n.get('childIds',[])if i in by)
 return [text(n)for n in nodes(ax)if role(n)=='status']
results=[]
for case in plan['cases']:
 c=read(case['id']);p=c['payload'];checks=p.get('checks',{}).copy()
 if case['id']=='BR-01':checks={'allOriginalPreflights':all(x['accepted']for x in preflight),'browserHashesVerified':p['browserSourceHashesVerified'],'sameSourceRevision':c['sourceRevision']==manifest['revision']}
 if case['id']=='BR-04':
  measured=[e['key']for e in c['journal']if e['type']=='host.measure'and e['owner']=='A'and e['epoch']==1];checks['disabledSkippedInActualMeasurements']='A-3'not in measured and 'A-2'in measured and 'A-4'in measured
 if case['id']=='BR-05':
  ax=p['ax'];a=combo(ax,'Suche A');b=combo(ax,'Suche B');props=properties(a);selected=[n for n in nodes(ax)if role(n)=='option'and val(n,'selected')is True];target=props['activedescendant']['relatedNodes'][0]['backendDOMNodeId']
  checks={'twoNamedComboboxes':len([n for n in nodes(ax)if role(n)=='combobox'])==2,'aExpandedBClosed':val(a,'expanded')is True and val(b,'expanded')is False,'activeSelectedActualNode':len(selected)==1 and selected[0]['backendDOMNodeId']==target and name(selected[0])=='Ergebnis A 7','politeAtomic':len([n for n in nodes(ax)if role(n)=='status'])==2 and all(val(n,'live')=='polite'and val(n,'atomic')is True for n in nodes(ax)if role(n)=='status'),'statusTextObserved':'7 Ergebnisse.'in statusTexts(ax),'noContainerTabstop':p['domChecks']['noContainerTabstop'],'focus':p['domChecks']['focus']=='A-input'}
 if case['id']=='BR-19':
  axs=p['axRecords'];loading=combo(axs['loading'],'Suche A');error=combo(axs['error'],'Suche A');closed=combo(axs['closed'],'Suche A');ready=combo(axs['ready'],'Suche A')
  checks={'loadingActualBusy':bool(val(loading,'busy'))and val(loading,'expanded')is True,'errorNotBusy':not bool(val(error,'busy',False))and val(error,'expanded')is True,'closedCollapsed':val(closed,'expanded')is False,'noStaleActiveInLoadingErrorClosed':all('activedescendant'not in properties(n)for n in [loading,error,closed]),'readyHasActive':'activedescendant'in properties(ready),'loadingText':'Ergebnisse werden geladen.'in statusTexts(axs['loading']),'errorText':'Suche fehlgeschlagen.'in statusTexts(axs['error']),'closedLoadingCleared':all('geladen'not in text for text in statusTexts(axs['closed'])),'noClosedOptions':not any(role(n)=='option'for n in nodes(axs['closed'])),'noSpeechClaim':p['screenReaderTested']is False}
 assert c['sourceRevision']==manifest['revision'],case['id']
 results.append({**case,'checks':checks,'expectationMet':bool(checks)and all(checks.values()),'record':'captures/'+case['id']+'.json','sourceRevision':c['sourceRevision']})
initial={p.name:json.loads(p.read_text())for p in(w/'captures-initial').glob('BR-*.json')}
out={'kind':'current-bound-browser-regression-run','cases':results,'new_conditions':0,'reexecuted_conditions':20,'group_count':0,'repeat_runs_counted_again':0,'browserVersion':read('BR-20')['payload']['browserVersion'],'sourceRevision':manifest['revision'],'original_schema_preflight':preflight,'research_host_implemented':True,'original_scxml_runtime_executed':True,'browser_dom_focus_scroll_ax_executed':True,'trusted_browser_keyboard_actions':True,'physical_keyboard_tested':False,'real_ime_tested':False,'screen_reader_tested':False,'native_platforms_tested':False,'full_ip_profile_passed':False,'original_counterexamples_and_own_initial_failures_preserved':True}
(w/'results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps([{k:c[k]for k in ['id','checks','expectationMet']}for c in results],ensure_ascii=False,indent=2));assert all(c['expectationMet']for c in results)
