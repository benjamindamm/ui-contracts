from pathlib import Path
import json,hashlib,copy,collections,math,xml.etree.ElementTree as ET
w=Path(__file__).parent;dump=lambda n,d:(w/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');h=lambda s:hashlib.sha256(s.encode()).hexdigest();base=json.loads((w/'baseline.json').read_text());policy=json.loads((w/'policy.json').read_text());revision=json.loads((w/'revision.json').read_text());ns={'s':'http://www.w3.org/2005/07/scxml'}
def changes(a,b,path=''):
 if type(a)!=type(b):return {path}
 if isinstance(a,dict):return set().union(*(changes(a.get(k),b.get(k),path+'/'+k) for k in a.keys()|b.keys()))
 if isinstance(a,list):
  if len(a)!=len(b):return {path}
  return set().union(*(changes(x,y,path+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))))
 return set() if a==b else {path}
def event(c):return json.loads(c)['modules'][0]['declarations'][0]['events'][0]['name']
def behaviorEvent(c):return ET.fromstring(c).find('.//s:send',ns).get('event')
def css(doc):
 t=json.loads(doc);values={}
 for name,key in [('gap','--autocomplete-gap'),('maxHeight','--autocomplete-max-height'),('rowHeight','--autocomplete-option-height')]:
  tok=t['base'][name];v=tok['$value']
  if tok['$type']!='dimension' or not isinstance(v,dict) or type(v.get('value')) not in [int,float] or not math.isfinite(v['value']):raise ValueError('dimension-value')
  if v.get('unit') not in ['px','rem']:raise ValueError('dimension-unit')
  # The unchanged fixture aliases are explicitly pinned, not a general alias resolver.
  semantic={'gap':'gap','maxHeight':'popupMaxHeight','rowHeight':'optionHeight'}[name]
  if t['autocomplete'][semantic]['$value']!='{base.'+name+'}':raise ValueError('unmodeled-alias')
  values[key]=v
 return ':root{'+ ';'.join(k+':'+str(v['value'])+v['unit'] for k,v in values.items())+'}\n'
results=[]
for case in json.loads((w/'cases.json').read_text()):
 req=case['request'];errors=[];staged=copy.deepcopy(base);edits=req['edits'];ledger=[]
 if req['baseRevision']!=revision['id']:errors.append('stale-base')
 if req['policySha256']!=revision['policySha256']:errors.append('policy-revision')
 for name,n in collections.Counter(e['artifact'] for e in edits).items():
  if n>1:errors.append('concurrent-source-conflict')
 leading={e['information'] for e in edits if e.get('information') in policy['authority'] and e['artifact']==policy['authority'][e['information']]['artifact']}
 for e in edits:
  name=e['artifact'];info=e.get('information');rule=policy['authority'].get(info);actor=e.get('actor')
  if not actor:errors.append('missing-origin');continue
  if not rule:errors.append('unknown-information');continue
  if rule['actorRole'] not in policy['roles'].get(actor,[]):
   # Editing a derived behavior reference as a behavior author does not change its leading signature owner.
   errors.append('non-leading-target' if name!=rule['artifact'] else 'wrong-role');continue
  if name not in base or e.get('beforeSha256')!=h(base.get(name,'')):errors.append('stale-source');continue
  isleading=name==rule['artifact']
  allowedDerived={'publicEventName':{'behavior.scxml','profile.json'}}.get(info,set())
  if not isleading:
   if name not in allowedDerived or e.get('derivedFrom')!=info:errors.append('non-leading-target');continue
   if info not in leading:errors.append('missing-leading-change');continue
  new=e['newContent'];allowed=False
  try:
   if name=='tokens.json':allowed=changes(json.loads(base[name]),json.loads(new)) <= {'/base/maxHeight/$value/value','/base/maxHeight/$value/unit'}
   elif name=='interface.json':allowed=changes(json.loads(base[name]),json.loads(new)) <= {'/modules/0/declarations/0/events/0/name'}
   elif name=='profile.json':allowed=changes(json.loads(base[name]),json.loads(new)) <= {'/publicEvent'}
   elif name=='behavior.scxml':
    oldEvent=behaviorEvent(base[name]);newEvent=behaviorEvent(new);allowed=new==base[name].replace('send event="'+oldEvent+'"','send event="'+newEvent+'"')
  except (ValueError,KeyError,TypeError,ET.ParseError):allowed=False
  if not allowed:errors.append('undeclared-edit');continue
  staged[name]=new;ledger.append({'transaction':req['id'],'actorRole':rule['actorRole'],'actorLabel':actor,'information':info,'source':{'artifact':rule['artifact'],'pointer':rule['pointer']},'changedArtifact':name,'beforeSha256':h(base[name]),'afterSha256':h(new),'changeKind':'leading' if isleading else 'derived','derivedFrom':e.get('derivedFrom'),'policySha256':revision['policySha256'],'baseRevision':revision['id']})
 if not errors:
  try:
   if len({event(staged['interface.json']),behaviorEvent(staged['behavior.scxml']),json.loads(staged['profile.json'])['publicEvent']})!=1:errors.append('public-event-conflict')
   generated=css(staged['tokens.json'])
  except ValueError as e:errors.append(str(e))
 if not errors:
  if generated!=base['generated-vars.css']:ledger.append({'transaction':req['id'],'information':'popupMaxHeight','source':{'artifact':'tokens.json','pointer':'/base/maxHeight/$value'},'changedArtifact':'generated-vars.css','beforeSha256':h(base['generated-vars.css']),'afterSha256':h(generated),'changeKind':'derived','policySha256':revision['policySha256'],'baseRevision':revision['id']});staged['generated-vars.css']=generated
  # Hash-addressed dependency pin refresh is explicit derived metadata, never a stealth authored semantic edit.
  profile=json.loads(staged['profile.json']);oldProfile=staged['profile.json']
  for role,binding in profile['artifacts'].items():binding['sha256']=h(staged[binding['file']])
  profile['visualLayout']['sha256']=h(staged['layout.css']);staged['profile.json']=json.dumps(profile,ensure_ascii=False,indent=2)+'\n'
  if staged['profile.json']!=oldProfile:ledger.append({'transaction':req['id'],'information':'revision-pins','changedArtifact':'profile.json','changeKind':'derived-hash-refresh','beforeSha256':h(oldProfile),'afterSha256':h(staged['profile.json']),'policySha256':revision['policySha256'],'baseRevision':revision['id']})
 rules=sorted(set(errors));accepted=not errors
 # Any failed condition discards the entire staged candidate and its successful-prefix ledger.
 final=staged if accepted else copy.deepcopy(base);finalLedger=ledger if accepted else []
 results.append({'id':case['id'],'expectedRules':case['expectedRules'],'actualRules':rules,'expectationMet':rules==sorted(case['expectedRules']),'accepted':accepted,'rollbackPreservesAllBaselineBytes':not accepted and final==base,'ledger':finalLedger,'resultHashes':{n:h(s) for n,s in final.items()},'newRevision':h(json.dumps({'files':{n:h(s) for n,s in final.items()},'policyHash':revision['policySha256']},sort_keys=True,separators=(',',':'))) if accepted else revision['id']})
 if accepted and case['id'] in ['leading-token-change','coordinated-public-name-change']:dump('accepted-'+case['id']+'.json',{'artifacts':final,'ledger':ledger})
dump('results.json',{'method':'Additional research policy; in-memory staging and provenance assertions, no filesystem/database atomic commit, no authenticated identity','cases':results});print(json.dumps([{'id':c['id'],'rules':c['actualRules'],'met':c['expectationMet']} for c in results]));raise SystemExit(0 if all(c['expectationMet'] for c in results) else 1)
