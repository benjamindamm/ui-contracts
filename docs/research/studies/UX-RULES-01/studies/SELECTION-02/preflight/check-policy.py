from pathlib import Path
import json,hashlib,subprocess
from jsonschema import Draft7Validator
S=Path(__file__).resolve().parents[1];L=S/'candidate-library/libraries/example'
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

schema=json.loads((L/'ux-capabilities.schema.json').read_text());idx=json.loads((L/'library.json').read_text());caps={}
for name in ['Select','SelectWithSearch','Autocomplete','Input']:
 d=L/idx['components'][name];u=json.loads((d.parent/'ux.json').read_text());Draft7Validator(schema).validate(u)
 for s in u['sources']:assert hashlib.sha256((d.parent/s['path']).read_bytes()).hexdigest()==s['sha256']
 caps[name]=u['capabilities']
rt=Path('/tmp/ui-contracts-ux-rules-runtime');cp=str(rt/'classes')+':'+(rt/'classpath.txt').read_text().strip()
cases=[]
for name,arm,changes,wanted in [('few','a',{},'Select'),('many','b',{},'SelectWithSearch'),('no-search-input','b',{'queryEditingAllowed':False},'no-defined-candidate'),('no-provider','b',{'filteringProviderAvailable':False},'no-defined-candidate')]:
 d=json.loads((S/f'inputs/{arm}.json').read_text());facts={**d['facts'],**changes,'optionCount':len(d['options']),'searchRequiredAbove':15,'selectCapabilities':caps['Select'],'searchSelectCapabilities':caps['SelectWithSearch'],'autocompleteCapabilities':caps['Autocomplete']};p=subprocess.run(['/opt/homebrew/opt/openjdk/bin/java','-cp',cp,'DmnProbe',str(L/'selection-policy.dmn'),'choice'],input=json.dumps(facts),capture_output=True,text=True);n=json.loads(p.stdout);assert p.returncode==0 and n['stage']=='evaluated',n;assert n['value']['choice']==wanted,n;cases.append({'id':name,'expected':wanted,'native':n})
dump(S/'preflight/policy-recheck.json',{'overall':'PASS_LIMITED','release':False,'cases':cases,'capabilitySourcesValidated':4})
print('4 native DMN cases and 4 capability source profiles checked')
