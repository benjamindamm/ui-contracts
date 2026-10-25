from pathlib import Path
import json,hashlib,sys
w=Path(__file__).parent;h=lambda s:hashlib.sha256(s.encode()).hexdigest();expected=json.loads((w/'revision-expectation.json').read_text());revision=json.loads((w/'revision.json').read_text());result=json.loads((w/'results.json').read_text());observed=[]
for c in result['cases']:
 if c['accepted']:
  digest=h(json.dumps({'files':c['resultHashes'],'policyHash':revision['policySha256']},sort_keys=True,separators=(',',':')));observed.append({'id':c['id'],'expectedRevision':digest,'actualRevision':c['newRevision'],'matches':digest==c['newRevision']})
out={**expected,'observed':observed,'expectationMet':all(x['matches'] for x in observed)};(w/(sys.argv[1] if len(sys.argv)>1 else 'revision-results.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));raise SystemExit(0 if out['expectationMet'] else 1)
