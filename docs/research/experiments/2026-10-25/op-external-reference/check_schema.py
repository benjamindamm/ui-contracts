from pathlib import Path
import json,copy,hashlib
from jsonschema import Draft7Validator
w=Path(__file__).parent;schema=Path('work/validation-probes/sources/cem.schema.json');validator=Draft7Validator(json.loads(schema.read_text()));base=json.loads((w/'interface.json').read_text());out=[]
for c in json.loads((w/'schema-expectations.json').read_text()):
 d=copy.deepcopy(base);d['modules'][0]['declarations'][0]['members'][0]['type']['text']=c['type'];errors=[str(e)for e in validator.iter_errors(d)];out.append({**c,'valid':not errors,'errors':errors,'expectationMet':(not errors)==c['expectedValid']})
(w/'schema-results.json').write_text(json.dumps({'originalSchemaSha256':hashlib.sha256(schema.read_bytes()).hexdigest(),'kind':'Original CEM structural validation, not cross-domain type binding','cases':out},indent=2)+'\n');print(json.dumps(out));assert all(c['expectationMet']for c in out)
