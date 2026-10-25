from pathlib import Path
import json,sys,platform,hashlib,importlib.metadata
import jsonschema
p=Path(__file__).parent
schemas={k:json.loads((p/'sources'/f'{k}.schema.json').read_text()) for k in ['cem','uxspec']}
validators={'cem':jsonschema.Draft7Validator,'uxspec':jsonschema.Draft202012Validator}
for k,s in schemas.items():validators[k].check_schema(s)
results=[]
for case in json.loads((p/'cases.json').read_text()):
 instance=json.loads((p/case['input']).read_text());v=validators[case['schema']](schemas[case['schema']]);errors=sorted(v.iter_errors(instance),key=lambda e:str(list(e.path)));valid=not errors
 results.append({**case,'actual_valid':valid,'expectation_met':valid==case['expected_valid'],'errors':[{'path':list(e.absolute_path),'schema_path':list(e.absolute_schema_path),'validator':e.validator,'message':e.message,'context':[{'path':list(c.absolute_path),'validator':c.validator,'message':c.message} for c in e.context]} for e in errors]})
report={'kind':'original-schema-validation','python':platform.python_version(),'platform':platform.platform(),'validator':'python-jsonschema','validator_version':importlib.metadata.version('jsonschema'),'dependencies':{n:importlib.metadata.version(n) for n in ['attrs','jsonschema-specifications','referencing','rpds-py','typing-extensions']},'network_during_validation':False,'candidate_runtime_executed':False,'cases':results,'all_expectations_met':all(x['expectation_met'] for x in results)}
(p/'schema-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
for x in results:print(x['id'],x['actual_valid'],'expected',x['expected_valid'],'OK' if x['expectation_met'] else 'MISMATCH')
sys.exit(0 if report['all_expectations_met'] else 1)
