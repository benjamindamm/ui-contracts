from pathlib import Path
import json
w=Path(__file__).parent;x=json.loads((w/'native-capture.json').read_text());cases=[c['value']for c in x['cases']];expected=json.loads((w/'cases.json').read_text());assert len(cases)==len(expected)==16
for c,e in zip(cases,expected):assert c['id']==e['id']and c['expected']==e['expected']and c['expectationMet'];assert all(c['observed'].get(k)==v for k,v in e['expected'].items())
result={'scope':'Actual original UXSpec compiler/full style-map or uSpec canonical builder/full original clipping-function output mapped through explicit extra CEM/context/anchor/overflow/fixed-row policy to native own DOM; no original UX Runner/editor/Figma SDK or platform renderer claimed','cases':cases};(w/'results.json').write_text(json.dumps(result,indent=2)+'\n')
for candidate,criterion,file in [('UXSpec','V04','ux-anchor-results.json'),('UXSpec','V06','ux-overflow-results.json'),('uSpec','V04','us-anchor-results.json'),('uSpec','V06','us-overflow-results.json')]:
 d=dict(result);d['cases']=[c for c in cases if c['candidate']==candidate and c['criterion']==criterion];(w/file).write_text(json.dumps(d,indent=2)+'\n')
initial=json.loads((w/'initial-native-capture.json').read_text());assert sum(not c['value']['expectationMet']for c in initial['cases'])==1
print('16 final native conditions fulfilled; initial own fixed-row/flex premise failure preserved as1 mismatch, not additional test.')
