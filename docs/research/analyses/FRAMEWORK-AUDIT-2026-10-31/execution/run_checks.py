from pathlib import Path
import subprocess,json,concurrent.futures,time,hashlib
R=Path('/Users/kcnpxcp/Dev/GitHub/ui-contracts');O=Path('/tmp/ui-contracts-framework-audit-20261031');py=str(R/'tools/validation/.venv/bin/python')
checks=[('libraries',[py,'-m','unittest','discover','-s','tools/libraries','-p','test_libraries.py']),('fonts',[py,'-m','unittest','discover','-s','tools/fonts','-p','test_fonts.py']),('handoffs',[py,'tools/skill-tests/ui-contracts/test_handoffs.py','--skill','skills/ui-contracts','--output',str(O/'handoffs-result.json')]),('design-review',[py,'-m','unittest','discover','-s','tools/design-review','-p','test_review.py']),('process',[py,'-m','unittest','discover','-s','tools/design-review','-p','test_process.py']),('charts',['node','--test','tools/charts/test_pie.mjs']),('presentation',['node','--test','tools/openpencil/test_layout.mjs','tools/openpencil/test_themes.mjs'])]
def run(pair):
 name,cmd=pair;t=time.monotonic()
 try:
  p=subprocess.run(cmd,cwd=R,capture_output=True,text=True,timeout=150);row={'id':name,'command':cmd,'exitCode':p.returncode,'elapsedSeconds':round(time.monotonic()-t,2),'stdout':p.stdout,'stderr':p.stderr}
 except subprocess.TimeoutExpired as e:row={'id':name,'command':cmd,'timeout':True,'elapsedSeconds':round(time.monotonic()-t,2)}
 (O/(name+'.json')).write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n');return {k:v for k,v in row.items() if k not in ['stdout','stderr','command']}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 rows=list(ex.map(run,checks))
(O/'test-summary.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
