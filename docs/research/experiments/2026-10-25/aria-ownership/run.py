from pathlib import Path
from html.parser import HTMLParser
from html import escape
import json,hashlib,copy
w=Path(__file__).parent;h=lambda s:hashlib.sha256(s.encode()).hexdigest();base=(w/'fixtures/accessibility.html').read_text();policyText=(w/'policy.json').read_text();policy=json.loads(policyText)
class Elements(HTMLParser):
 def __init__(self,text):
  super().__init__();self.elements=[];self.feed(text)
 def handle_starttag(self,tag,attrs):self.elements.append((tag,dict(attrs),self.get_starttag_text()))
def target(text,id):
 matches=[t for t in Elements(text).elements if t[1].get('id')==id]
 if len(matches)!=1:raise ValueError('nonunique-target')
 return matches[0]
def label(text,id,value):
 tag,attrs,raw=target(text,id)
 if tag!='div' or attrs.get('role')!='listbox':raise ValueError('wrong-role-target')
 if 'aria-labelledby'in attrs:raise ValueError('unsupported-name-precedence')
 old='aria-label="'+escape(attrs['aria-label'],quote=True)+'"';assert old in raw
 return text.replace(raw,raw.replace(old,'aria-label="'+escape(value,quote=True)+'"',1),1)
def revision(source,host):return h(json.dumps({'source':h(source),'host':h(host),'policy':h(policyText)},sort_keys=True,separators=(',',':')))
cem=json.loads((w/'fixtures/interface.json').read_text());assert 'list'in {x['name']for x in cem['modules'][0]['declarations'][0]['cssParts']};assert target(base,'list-a')[1]['role']=='listbox'
results=[]
for c in json.loads((w/'cases.json').read_text()):
 q=c['request'];errors=[]
 for check,rule in [(q['beforeSourceHash']!=h(base),'stale-source'),(q['beforeHostHash']!=h(base),'stale-host'),(q['policyHash']!=h(policyText),'stale-policy'),(q['actorRole']!=policy['allowedActorRole'],'wrong-owner'),(q['targetId']!='list-a','foreign-instance'),(bool(q['otherEdits']),'unrelated-edit'),(bool(q.get('addLabelledby')),'unsupported-name-precedence'),(q.get('competingSourceLabel',q['sourceLabel'])!=q['sourceLabel'],'source-conflict'),(q['sourceLabel']=='Ergebnisse A' and q['hostLabel']!='Ergebnisse A','non-leading-edit'),(q['sourceLabel']!='Ergebnisse A' and q['sourceLabel']!=q['hostLabel'],'derived-conflict')]:
  if check:errors.append(rule)
 source=host=base;journal=[]
 if not errors:
  source=label(base,'list-a',q['sourceLabel']);host=label(base,'list-a',q['hostLabel']);assert source==host
  journal=[{'information':policy['information'],'actorLabel':q['actorLabel'],'declaredRole':q['actorRole'],'source':policy['leading'],'target':policy['derived'],'sourceBefore':h(base),'sourceAfter':h(source),'hostBefore':h(base),'hostAfter':h(host),'policyHash':h(policyText),'revisionBefore':revision(base,base),'revisionAfter':revision(source,host),'kind':'authored source and declared derived host copy'}]
  (w/'accepted.json').write_text(json.dumps({'source':source,'host':host,'journal':journal},ensure_ascii=False,indent=2)+'\n')
 observed={'errors':sorted(errors),'accepted':not errors,'journal':journal,'revision':revision(source,host),'sourceHash':h(source),'hostHash':h(host),'rejectedPreservesSourceAndHost':bool(errors)and source==base and host==base,'otherDomainHashes':{n:hashlib.sha256((w/'fixtures'/n).read_bytes()).hexdigest()for n in policy['otherDomainHashes']}}
 assert observed['otherDomainHashes']==policy['otherDomainHashes']
 results.append({**c,'observed':observed,'expectationMet':sorted(errors)==sorted(c['expectedErrors'])})
(w/'results.json').write_text(json.dumps({'scope':'Additional explicit ARIA-name research ownership policy; source/host staged in memory, role labels not authenticated; no universal standard feature','cases':results},ensure_ascii=False,indent=2)+'\n')
hostDir=Path('work/op-projection-origin/host');hostDir.mkdir(exist_ok=True)
for id,text in [('before',base),('after',json.loads((w/'accepted.json').read_text())['host'])]:(hostDir/f'aria-ownership-{id}.html').write_text('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>ARIA-Quellenbindung '+id+'</title></head><body>'+text+'</body></html>')
print(json.dumps([{'id':c['id'],'errors':c['observed']['errors'],'met':c['expectationMet']}for c in results]));assert all(c['expectationMet']for c in results)
