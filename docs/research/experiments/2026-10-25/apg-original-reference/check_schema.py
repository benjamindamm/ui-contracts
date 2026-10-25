from pathlib import Path
import json,hashlib
from jsonschema import Draft7Validator
w=Path(__file__).parent;schema=Path('work/validation-probes/sources/cem.schema.json');v=Draft7Validator(json.loads(schema.read_text()));records=[]
for c in json.loads((w/'schema-expectations.json').read_text()):
 errors=[str(e)for e in v.iter_errors(json.loads((w/c['file']).read_text()))];records.append({**c,'valid':not errors,'errors':errors,'expectationMet':(not errors)==c['expected']})
(w/'schema-results.json').write_text(json.dumps({'originalSchemaSha256':hashlib.sha256(schema.read_bytes()).hexdigest(),'cases':records},indent=2)+'\n');print(json.dumps(records));assert all(c['expectationMet']for c in records)
