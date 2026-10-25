from pathlib import Path
import json,copy
w=Path(__file__).parent;dump=lambda n,d:(w/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');base={'schemaVersion':1,'categories':{'colors':[0,1]},'paths':['colors.red'],'tokens':{'colors.red':{'category':'colors','cssVar':'--colors-red'}},'conditions':{},'themes':{},'values':[{'token':'colors.red','value':'#f00'}]};cases=[]
def add(id,change,typed,reader=True):
 value=copy.deepcopy(base);change(value);cases.append({'id':id,'input':value,'expectedTypedAccepted':typed,'expectedReaderAccepted':reader})
add('valid-export',lambda d:None,True)
add('categories-number',lambda d:d.update(categories=7),False)
add('tokens-boolean',lambda d:d.update(tokens=False),False)
add('null-value-row',lambda d:d.update(values=[None]),False)
add('missing-conditions-themes',lambda d:(d.pop('conditions'),d.pop('themes')),False)
add('numeric-value-string-field',lambda d:d['values'][0].update(value=42),False)
add('missing-reference-target',lambda d:d['values'][0].update(refs=['colors.missing']),True)
add('category-range-outside-paths',lambda d:d.update(categories={'colors':[0,999]}),True)
add('negative-schema-number',lambda d:d.update(schemaVersion=-1),True)
dump('cases.json',cases)
for c in cases:(w/(c['id']+'.ts')).write_text("import type { DesignSystemSpec } from '../panda-reader/sources/panda/packages/compiler-shared/src/design-system-spec/types';\nconst value: DesignSystemSpec = "+json.dumps(c['input'],ensure_ascii=False,indent=2)+";\n")
print({'predefinedPairedConditions':len(cases)})
