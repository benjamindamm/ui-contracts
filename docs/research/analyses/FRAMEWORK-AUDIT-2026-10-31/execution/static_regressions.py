from pathlib import Path
import sys,json,contextlib
R=Path('/Users/kcnpxcp/Dev/GitHub/ui-contracts');O=Path('/tmp/ui-contracts-framework-audit-20261031');sys.path.insert(0,str(R/'tools/validation'));import test_chain
original=test_chain.dump
# Redirect only the aggregate output; all original mutations/assertions execute unchanged in their disposable copies.
def output_redirect(path,obj):
 if Path(path).resolve()==(R/'tools/validation/evidence/countercases.json').resolve():path=O/'static-countercases.json'
 return original(path,obj)
test_chain.dump=output_redirect
with (O/'static-countercases.stdout').open('w') as log,contextlib.redirect_stdout(log):code=test_chain.main()
d=json.loads((O/'static-countercases.json').read_text());print(json.dumps({'exitCode':code,'count':len(d['cases']),'met':sum(c['expectationMet'] for c in d['cases']),'historicalFixtureUnchanged':d['historicalFixtureUnchanged']}));raise SystemExit(code)
