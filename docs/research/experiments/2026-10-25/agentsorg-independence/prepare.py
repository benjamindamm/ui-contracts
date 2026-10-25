from pathlib import Path
import json,hashlib,xml.etree.ElementTree as ET
from html.parser import HTMLParser
w=Path(__file__).parent;h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();old=Path('work/four-domain');cem=json.loads((w/'fixtures/interface.json').read_text());model=ET.fromstring((w/'fixtures/behavior.scxml').read_text());profile=json.loads((old/'profile.json').read_text());assert cem['modules'][0]['declarations'][0]['name']==model.get('name')=='Autocomplete'
class Ids(HTMLParser):
 def __init__(self,s):super().__init__();self.ids=[];self.feed(s)
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id'in d:self.ids.append(d['id'])
ids=Ids((w/'fixtures/accessibility.html').read_text()).ids
parts={x['name']for x in cem['modules'][0]['declarations'][0]['cssParts']}
for instance in profile['instances'].values():
 for part,target in instance['parts'].items():assert part in parts and ids.count(target)==1
layout=(old/'fixtures/visual.css').read_text().replace('max-height:160px','max-height:var(--spacing-popup-max-height)');(w/'fixtures/layout.css').write_text(layout)
for value in [160,192]:
 tokens=(w/f'fixtures/tokens-{value}.css').read_text();assert f'--spacing-popup-height: {value}px;'in tokens;assert '--spacing-popup-max-height: var(--spacing-popup-height);'in tokens
 doc=json.loads((w/f'fixtures/visual-{value}.design').read_text());assert doc['tokens']['spacing']['popupHeight']==value
 host='<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Getrennte Originalbeiträge</title><style>'+tokens+'\n'+layout+'</style></head><body>'+(w/'fixtures/accessibility.html').read_text()+'</body></html>'
 (w/f'host-{value}.html').write_text(host);Path(f'work/op-projection-origin/host/agentsorg-independent-{value}.html').write_text(host)
profile['status']='Additional candidate-specific research binding, no selected product format';profile['visualContribution']={'originalFile':'visual-192.design','sha256':h(w/'fixtures/visual-192.design'),'originalValuePointer':'/tokens/spacing/popupHeight','actualOriginalExport':'tokens-192.css','exportSha256':h(w/'fixtures/tokens-192.css'),'alias':'--spacing-popup-max-height','layoutFile':'layout.css','targetProperty':'max-height','otherDomainsByteIdentical':{n:h(w/'fixtures'/n)for n in ['interface.json','behavior.scxml','accessibility.html']}}
(w/'profile.json').write_text(json.dumps(profile,ensure_ascii=False,indent=2)+'\n');(w/'binding-expectation.json').write_text(json.dumps({'id':'independent-original-contributions','expected':{'originalRootsSeparate':True,'partTargetsResolved':True,'visualValues':[160,192],'otherDomainsUnchanged':True}},indent=2)+'\n');(w/'binding-results.json').write_text(json.dumps({'kind':'Additional candidate-specific identity/value binding using actual original exports, not new original semantics','cases':[{'id':'independent-original-contributions','observed':{'originalRootsSeparate':True,'partTargetsResolved':True,'visualValues':[160,192],'otherDomainsUnchanged':all(h(w/'fixtures'/n)==h(old/'fixtures'/n)for n in ['interface.json','behavior.scxml','accessibility.html'])},'expectationMet':all(h(w/'fixtures'/n)==h(old/'fixtures'/n)for n in ['interface.json','behavior.scxml','accessibility.html'])}]},indent=2)+'\n')
(w/'runtime-expectation.json').write_text(json.dumps({'id':'original-scxml-two-open-instances','expected':{'A':['open'],'B':['open']}},indent=2)+'\n');(w/'browser-expectations.json').write_text(json.dumps([{'id':'original-export-192-native','value':192,'expectedHeights':[192,192]},{'id':'independent-visual-revision-160-native','value':160,'expectedHeights':[160,160]}],indent=2)+'\n')

# Bind the reused original schema observations to exactly these source bytes.
previous=json.loads(Path('work/agentsorg-export-ownership/results.json').read_text())
for value,case in [(160,'baseline-css'),(192,'token-update-and-diff')]:
 row=next(c for c in previous['cases']if c['id']==case)
 assert row['observed']['originalSchemaValid'] and row['sourceHash']==h(w/f'fixtures/visual-{value}.design')
assert model.tag=='{http://www.w3.org/2005/07/scxml}scxml' and cem['schemaVersion']=='2.1.0'
assert all(json.loads((w/f'fixtures/visual-{v}.design').read_text())['schema']=='design.v1'for v in [160,192])
assert json.loads((w/'binding-results.json').read_text())['cases'][0]['expectationMet']
