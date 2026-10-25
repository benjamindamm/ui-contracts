from pathlib import Path
import json
import jsonschema
p=Path(__file__).parent;s=json.loads((p/'sources/cem.schema.json').read_text());bad=json.loads((p/'inputs/cem-03-invalid-event-name.json').read_text());decl=bad['modules'][0]['declarations'][0];event=decl['events'][0]
results=[]
for name,instance,definition,expected in [('event-definition',event,'Event',False),('custom-element-definition',decl,'CustomElementDeclaration',False),('class-definition',decl,'ClassDeclaration',True)]:
 wrapper={'$schema':s['$schema'],'definitions':s['definitions'],'$ref':'#/definitions/'+definition};v=jsonschema.Draft7Validator(wrapper);errs=list(v.iter_errors(instance));result={'id':name,'diagnostic_wrapper':True,'original_definition':definition,'input':instance,'expected_valid':expected,'actual_valid':not errs,'errors':[{'path':list(e.path),'message':e.message} for e in errs]};results.append(result);print(name,not errs,'expected',expected)
(p/'cem-diagnosis.json').write_text(json.dumps({'kind':'original-definition-projection','original_root_changed':False,'wrapper_is_additional_test_harness':True,'results':results},indent=2)+'\n');assert all(x['actual_valid']==x['expected_valid'] for x in results)
