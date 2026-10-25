from pathlib import Path
import json,hashlib
from lxml import etree
w=Path(__file__).parent;pkg=w/'package';pkg.mkdir(exist_ok=True)
def save(p,v):
 p=pkg/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n' if not isinstance(v,str) else v)
parts={'Autocomplete':['input','list','option','status'],'Overlay':['surface','content'],'ScrollArea':['viewport','content']}
slug={'Autocomplete':'autocomplete','Overlay':'overlay','ScrollArea':'scroll-area'}
sources=[];definitions=[];targets=[]
for name in parts:
 n=slug[name];definition='reference:'+name
 members=[{'kind':'field','name':'owner','type':{'text':'string'}},{'kind':'field','name':'epoch','type':{'text':'number'}}]
 events=[]
 if name=='Autocomplete':
  members=[{'kind':'field','name':k,'type':{'text':t},**({'default':d} if d is not None else {})} for k,t,d in [('query','string','""'),('value','string | undefined',None),('results','Array<{ key: string; label: string; disabled?: boolean }>','[]'),('enabled','boolean','true'),('limit','number','7')]]
  events=[{'name':'value-change','type':{'text':'CustomEvent<{value:string}>'}}]
 cem={'schemaVersion':'2.1.0','modules':[{'kind':'javascript-module','path':n+'.js','declarations':[{'kind':'class','name':name,'customElement':True,'members':members,'events':events,'cssParts':[{'name':p} for p in parts[name]]}]}]}
 save(Path(n)/'interface.json',cem)
 prior={'Autocomplete':'parent','Overlay':'overlay','ScrollArea':'scroll'}[name];tree=etree.parse(str(w.parent/'ip01-followup/unique'/(prior+'.scxml')));ns={'s':'http://www.w3.org/2005/07/scxml'}
 inv=tree.find('.//s:invoke',ns)
 if inv is not None:inv.set('src','../'+('overlay' if name=='Autocomplete' else 'scroll-area')+'/behavior.scxml')
 if name=='Autocomplete':
  dm=tree.find('s:datamodel',ns)
  for k,e in [('query',"''"),('value','undefined'),('results','[]'),('enabled','true'),('limit','7')]:etree.SubElement(dm,'{'+ns['s']+'}data',id=k,expr=e)
  st=tree.find("s:state[@id='open']",ns);tr=etree.SubElement(st,'{'+ns['s']+'}transition',event='STATIC_PORT_ONLY',cond="typeof value === 'string'");send=etree.SubElement(tr,'{'+ns['s']+'}send',event='value-change');etree.SubElement(send,'{'+ns['s']+'}param',name='value',expr='value')
 save(Path(n)/'behavior.scxml',etree.tostring(tree,encoding='unicode')+'\n')
 html={'Autocomplete':'<template><label data-part="label">Search</label><input data-part="input" role="combobox" aria-expanded="false"><ul data-part="list" role="listbox"><li data-part="option" role="option">Result</li></ul><div data-part="status" role="status" aria-live="polite" aria-atomic="true"></div></template>', 'Overlay':'<template><div data-part="surface"><div data-part="content"></div></div></template>','ScrollArea':'<template><div data-part="viewport"><div data-part="content"></div></div></template>'}[name]
 save(Path(n)/'accessibility.html',html+'\n')
 css={'Autocomplete':'[data-part="option"] { min-height: var(--row-height); flex-shrink: 0; }','Overlay':'[data-part="surface"] { position: absolute; top: anchor(bottom); margin-top: var(--gap); }','ScrollArea':'[data-part="viewport"] { max-height: var(--max-height); overflow-y: auto; }'}[name]
 save(Path(n)/'layout.css',css+'\n')
 ids=[]
 for domain,file,fmt in [('interface','interface.json','cem'),('behavior','behavior.scxml','scxml'),('accessibility','accessibility.html','html'),('visual','layout.css','css')]:
  sid=n+'.'+domain;ids.append(sid);sources.append({'id':sid,'definition':definition,'domain':domain,'format':fmt,'path':n+'/'+file,'formatVersion':{'cem':'2.1.0','scxml':'1.0','html':'html-host-fixture','css':'pinned-partial-web-css'}[fmt]})
 definitions.append({'id':definition,'sources':ids})
 for i,p in enumerate(parts[name]):targets.append({'id':n+'.'+p,'source':n+'.interface','definition':definition,'kind':'part','locator':'/modules/0/declarations/0/cssParts/'+str(i)})
sources.append({'id':'tokens','definition':None,'domain':'visual','format':'dtcg','formatVersion':'2025.10','path':'visual/tokens.json'})
save(Path('visual/tokens.json'),{'base':{'gap':{'$type':'dimension','$value':{'value':8,'unit':'px'}},'max':{'$type':'dimension','$value':{'value':160,'unit':'px'}},'row':{'$type':'dimension','$value':{'value':32,'unit':'px'}}},'autocomplete':{'gap':{'$type':'dimension','$value':'{base.gap}'},'maxHeight':{'$type':'dimension','$value':'{base.max}'},'rowHeight':{'$type':'dimension','$value':'{base.row}'}}})
uses=[]
for root in ['A','B']:
 for segments,d in [([root],'reference:Autocomplete'),([root,'overlay'],'reference:Overlay'),([root,'overlay','scroll'],'reference:ScrollArea')]:uses.append({'path':segments,'definition':d})
relations=[];body=[]
for root in ['A','B']:
 prefix=root+'-';body.append(f'<section data-root="{root}"><label id="{prefix}label">Search {root}</label><input id="{prefix}input" data-instance="{root}" data-part="input" role="combobox" aria-labelledby="{prefix}label" aria-controls="{prefix}list" aria-expanded="false"><div id="{prefix}overlay" data-instance="{root}/overlay" data-part="surface"><div data-instance="{root}/overlay" data-part="content"><div id="{prefix}viewport" data-instance="{root}/overlay/scroll" data-part="viewport"><div data-instance="{root}/overlay/scroll" data-part="content"><ul id="{prefix}list" data-instance="{root}" data-part="list" role="listbox" aria-labelledby="{prefix}label"><li id="{prefix}option" data-instance="{root}" data-part="option" role="option">First</li></ul></div></div></div></div><div id="{prefix}status" data-instance="{root}" data-part="status" role="status" aria-live="polite" aria-atomic="true"></div></section>')
 for part in ['input','list','option','status']:
  relations.append({'id':root+'.'+part,'kind':'host-part','target':'autocomplete.'+part,'use':[root],'hostId':prefix+part,'role':{'input':'combobox','list':'listbox','option':'option','status':'status'}[part]})
 for part,t,use in [('overlay','overlay.surface',[root,'overlay']),('viewport','scroll-area.viewport',[root,'overlay','scroll'])]:relations.append({'id':root+'.'+part,'kind':'host-part','target':t,'use':use,'hostId':prefix+part,'role':None})
save(Path('host.html'),'<!doctype html><html lang="en"><head><title>IP-01 static research host</title></head><body>'+''.join(body)+'</body></html>\n')
relations.append({'id':'event.value','kind':'event-type','interfaceSource':'autocomplete.interface','event':'value-change','behaviorSource':'autocomplete.behavior','locator':"//s:send[@event='value-change']/s:param[@name='value']",'field':'value'})
for token,source,variable,prop in [('gap','overlay.visual','--gap','margin-top'),('maxHeight','scroll-area.visual','--max-height','max-height'),('rowHeight','autocomplete.visual','--row-height','min-height')]:
 relations.append({'id':'visual.'+token,'kind':'token-css','tokenSource':'tokens','tokenPath':'autocomplete.'+token,'cssSource':source,'variable':variable,'property':prop})
binding={'kind':'research-binding-fixture','version':'0.1-research','status':'provisional-static-only','namespace':'reference','sources':sources,'definitions':definitions,'targets':targets,'uses':uses,'relations':relations,'host':'host.html','requiredRelations':[x['id'] for x in relations],'policy':{'types':'T0-plus-T1-closed-record','allowedRecursiveUses':False,'allowedDimensionUnits':['px','rem'],'extraRecordFields':'reject','runtimeCandidate':'native-idlocation-plus-explicit-error-relay-not-executed-here'}}
binding['runtimeCandidate']={'package':'@scion-scxml/scxml','version':'4.3.28','adapter':'../../ip01-followup/adapter.cjs','adapterSha256':hashlib.sha256((w.parent/'ip01-followup/adapter.cjs').read_bytes()).hexdigest(),'usage':'provenance-only; existing adapter whitelist does not accept this new static package; no runtime execution claimed'}
save(Path('bindings.json'),binding)
save(Path('values.json'),{'query':'abc','value':'k1','results':[{'key':'k1','label':'One'},{'key':'k2','label':'Two','disabled':True}],'enabled':True,'limit':7})
