from pathlib import Path
import json,hashlib
from lxml import html
S=Path(__file__).resolve().parents[1];load=lambda p:json.loads(p.read_text());checks=[]
def check(id,ok,evidence):checks.append({'id':id,'passed':bool(ok),'evidence':evidence})
baseline=load(S/'review/browser-first.json');base={r['arm']:r['dom']['value'] for r in baseline['baseline']['value']};first={r['arm']:r['result']['value'] for r in baseline['firstActions']['value']};ac={k:v['value'] for k,v in baseline['autocomplete']['value'].items()};shared={k:v['value'] for k,v in baseline['sharedPrefix']['value'].items()};repair={k:v['value'] for k,v in load(S/'review/browser-repair.json')['value'].items()}
for arm,wanted in [('a','Select'),('b','Autocomplete')]:
 decision=load(S/f'outputs/{arm}/decision.json');check('choice-'+arm,decision['choice']==wanted,{'actual':decision['choice'],'expectedByFrozenProjectPolicy':wanted})
 check('Input-types-'+arm,{e['id']:e['type'] for e in base[arm]['fields'] if e['id'] in ['givenName','familyName','email','nationalNumber']}=={'givenName':'text','familyName':'text','email':'email','nationalNumber':'tel'},base[arm]['fields'])
 check('unique-ids-'+arm,base[arm]['idsUnique'],True)
 check('visible-labels-'+arm,all(any(l['for']==e['id'] and l['text'] for l in base[arm]['labels']) for e in base[arm]['fields'] if e['type']!='hidden'),base[arm]['labels'])
 check('string-phone-'+arm,dict(first[arm]['values'])['nationalNumber']=='0123 456789',dict(first[arm]['values'])['nationalNumber'])
 check('observed-resources-local-'+arm,base[arm]['resourceOrigins']==['http://127.0.0.1:8766'],base[arm]['resourceOrigins'])
firstSelect=html.fromstring((S/'outputs/a/index.html').read_text());keys=firstSelect.xpath('//select/option[string-length(@value)>0]/@value');check('three-native-select-options',keys==[r['key'] for r in load(S/'inputs/a.json')['options']],keys)
check('first-unknown-country-rejected',first['b']['queryValidity']['valid'] is False and dict(first['b']['values'])['country']=='',first['b']['queryValidity'])
check('actual-filter-Indien',[r['key'] for r in ac['filtered']['options']]==['IN'],ac['filtered'])
check('keyboard-active-and-focus',ac['active']['selected']==['IN'] and ac['active']['focus']=='country-query',ac['active'])
check('keyboard-commit-and-close',ac['committed']['value']=='IN' and ac['committed']['expanded']=='false',ac['committed'])
check('all-thirty-options-and-order',[r['key'] for r in ac['all']['options']]==[r['key'] for r in load(S/'inputs/b.json')['options']],ac['all']['options'])
check('scroll-to-last-key',ac['end']['active']=='SK' and ac['end']['rowVisible'] and ac['end']['scrollTop']>0,ac['end'])
check('same-prefix-distinct-keys',[r['key'] for r in shared['filtered']]==['CA','US'] and shared['selected']['key']=='US',shared)
expectedIds={'givenName','familyName','email','nationalNumber'}
check('A-Input-events',expectedIds.issubset({e['id'] for e in first['a']['audit']}),first['a']['audit'])
check('B-first-Input-events',expectedIds.issubset({e['id'] for e in first['b']['audit']}),first['b']['audit'])
defect={k:v['value'] for k,v in baseline['inputDefect']['value'].items()};check('B-first-success-invalidated',defect['before']['status']!='' and defect['after']['status']=='',defect)
check('repair-Input-events',expectedIds.issubset({e['id'] for e in repair['success']['audit']}),repair['success']['audit'])
check('repair-success-invalidated',repair['success']['status']!='' and repair['changed']['status']=='',repair['changed'])
check('repair-query-invalidates-success',repair['afterQuery']['status']=='',repair['afterQuery'])
check('repair-guard-synthetic',repair['synthetic']['disabledNoEvent'] and repair['synthetic']['readOnlyNoEvent'],repair['synthetic'])
check('repair-keeps-filter-and-key',[k for k in repair['filtered']]==['IN'] and repair['selected']['key']=='US' and repair['success']['phone']=='0123 456789',repair['selected'])
for r in load(S/'review/compiler-declared-checks.json')['rows']:check('typescript-'+r['arm'],r['exitCode']==0 and r['deliveredJsMatchesRecompiledTs'],r)
firstHashes=load(S/'review/first-deliveries.json')['files'];unchanged=all(hashlib.sha256((S/p).read_bytes()).hexdigest()==h for p,h in firstHashes.items());check('first-deliveries-unchanged',unchanged,len(firstHashes))
r={'scope':'Two controlled selection cases plus bounded form/browser checks; not general conformance','release':False,'primarySelection':{'a':{'expectedPreferred':'Select','actual':'Select','hardEligible':True,'policyPreferenceMet':True},'b':{'expectedPreferred':'Autocomplete','actual':'Autocomplete','hardEligible':True,'policyPreferenceMet':True}},'checks':checks,'checkCount':len(checks),'passed':sum(c['passed'] for c in checks),'retainedFirstFailures':['B-first-Input-events','B-first-success-invalidated'],'repair':'Separate b-repair-01 passes affected regression checks; initial failures remain failures.','notChecked':['Full screenreader/IME','Full external component API/SCXML lifecycle','Independent complete access audit','Exact model identity','Causal effect of UX docs versus prior model knowledge','Population-level reliability']}
(S/'review/results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(len(checks),'checks;',r['passed'],'passed; retained failures:',[c['id'] for c in checks if not c['passed']])
