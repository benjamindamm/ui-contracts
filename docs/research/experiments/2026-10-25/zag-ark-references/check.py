from pathlib import Path
from html.parser import HTMLParser
import json,hashlib,collections
w=Path(__file__).parent;h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
class Nodes(HTMLParser):
 def __init__(self,text):super().__init__();self.nodes=[];self.feed(text)
 def handle_starttag(self,tag,attrs):self.nodes.append({'tag':tag,'attrs':dict(attrs)})
def indexed(text):
 nodes=Nodes(text).nodes;return nodes,{n['attrs']['id']:n for n in nodes if 'id'in n['attrs']}
cem=json.loads((w/'fixtures/interface.json').read_text());parts=cem['modules'][0]['declarations'][0]['cssParts'];mapping={'input':('input',0),'content':('popup',1),'item':('option',3)};records=[]
for c in json.loads((w/'render-results.json').read_text())['cases']:
 error=None;resolved=[]
 try:
  if c['executionError']:raise ValueError('original-ssr-error')
  nodes,actual=indexed((w/c['actual']).read_text());_,source=indexed((w/c['external']).read_text());ids=[n['attrs']['id']for n in nodes if'id'in n['attrs']]
  if len(ids)!=len(set(ids)):raise ValueError('duplicate-host-id')
  suffix='-v2'if c['kind']=='rename'else''
  for instance in ['a','b']:
   expectedInput='input-'+instance+suffix;expectedPopup='popup-'+instance+suffix;expectedLabel='label-'+instance+suffix
   label=actual.get(expectedLabel)
   if not label or label['attrs'].get('for')not in actual:raise ValueError('missing-controlled-input')
   input=actual.get(expectedInput)
   if not input:raise ValueError('missing-controlled-input')
   controls=input['attrs'].get('aria-controls')
   if controls not in actual:raise ValueError('missing-controls-target')
   popup=actual[controls]
   if controls!=expectedPopup:raise ValueError('foreign-instance-target')
   if source[expectedPopup]['attrs'].get('role')!=popup['attrs'].get('role'):raise ValueError('external-role-conflict')
   for part,targetId in [('input',expectedInput),('content',expectedPopup),('item','option-'+instance+'-alpha'+suffix)]:
    node=actual.get(targetId);src=source.get(targetId);externalPart,index=mapping[part]
    if parts[index].get('name')!=externalPart:raise ValueError('cem-part-target')
    if not node or node['attrs'].get('data-scope')!='combobox'or node['attrs'].get('data-part')!=part:raise ValueError('original-part-target')
    if node['attrs'].get('role')!=src['attrs'].get('role'):raise ValueError('external-role-conflict')
    if part=='input':
     if node['attrs'].get('aria-controls')!=src['attrs'].get('aria-controls')or node['attrs'].get('aria-expanded')!=src['attrs'].get('aria-expanded'):raise ValueError('external-input-relation')
    if part=='content':
     if node['attrs'].get('aria-labelledby')!=src['attrs'].get('aria-labelledby')or node['attrs'].get('aria-labelledby')not in actual:raise ValueError('external-popup-name')
    resolved.append({'instance':instance,'originalPart':part,'actualId':targetId,'actualRole':node['attrs'].get('role'),'interfaceTarget':{'file':'interface.json','pointer':f'/modules/0/declarations/0/cssParts/{index}','name':externalPart,'contextualNodeType':'CEM cssParts entry'},'accessibilityTarget':{'file':c['external'],'id':targetId,'role':src['attrs'].get('role')},'sources':{'interfaceSha256':h(w/'fixtures/interface.json'),'accessibilitySha256':h(w/c['external']),'actualSsrSha256':h(w/c['actual'])},'method':'additional typed part/role/relation binder; not a native CEM reader'})
 except ValueError as e:error=str(e)
 observed={'accepted':error is None,'error':error,'originalSsrAccepted':c['executionError']is None,'resolved':resolved if error is None else[]};records.append({k:c[k]for k in ['id','candidate','kind','expected']}|{'observed':observed,'expectationMet':all(observed.get(k)==v for k,v in c['expected'].items())})
(w/'results.json').write_text(json.dumps({'scope':'Additional CEM part and external HTML/ARIA semantic relation binding over actual original SSR; original renderer does not reject these four negative inputs','cases':records},indent=2)+'\n');print(json.dumps([{'id':r['id'],'observed':r['observed']['error'],'met':r['expectationMet']}for r in records]));assert all(r['expectationMet']for r in records)
