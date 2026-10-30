import copy,json,hashlib
from pathlib import Path
from evaluate import evaluate,HERE
out=HERE/'review/policy-checks.json';assert not out.exists()
a=json.loads((HERE/'inputs/a.json').read_text());b=json.loads((HERE/'inputs/b.json').read_text());checks=[]
def probe(id,context,wanted,selectStatus=None):
 r=evaluate(context);ok=r['overall']=='PASS_LIMITED' and r['assessment']['choice']==wanted
 if selectStatus:ok=ok and r['assessment']['Select']==selectStatus
 checks.append({'id':id,'passed':ok,'expectedChoice':wanted,'actual':r})
probe('three-options-project-preference',a,'Select')
probe('thirty-options-search-required',b,'Autocomplete','incompatible-search')
c=copy.deepcopy(b);c['facts']['queryEditingAllowed']=False;probe('read-only-display-and-search-reveals-missing-variant',c,'no-defined-candidate')
c=copy.deepcopy(b);c['facts']['filteringProviderAvailable']=False;probe('no-filter-provider-not-pretended-present',c,'no-defined-candidate')
c=copy.deepcopy(b);c['facts']['searchExplicitlyRequired']=False;probe('explicit-no-search-overrides-count-rule',c,'Select')
c=copy.deepcopy(a);c['facts']['searchExplicitlyRequired']=True;probe('explicit-search-on-small-list',c,'Autocomplete')
for context in [a,b]:
 records=context['options'];priority=context['orderingPolicy']['priorityKeys'];expected=[r['key'] for k in priority for r in records if r['key']==k]+[r['key'] for r in sorted([r for r in records if r['key'] not in priority],key=lambda r:(int(r['dialCode'][1:]),r['key']))]
 checks.append({'id':'explicit-order-'+context['scenarioId'],'passed':[r['key'] for r in records]==expected,'keys':expected})
checks.append({'id':'shared-dial-code-keeps-two-countries','passed':len([r for r in b['options'] if r['dialCode']=='+1'])==2})
out.write_text(json.dumps({'overall':'PASS_LIMITED' if all(r['passed'] for r in checks) else 'FAIL','release':False,'checks':checks,'scope':'Project policy and dataset invariants, not the independent builders'},ensure_ascii=False,indent=2)+'\n');print(len(checks),'checks',all(r['passed'] for r in checks))
