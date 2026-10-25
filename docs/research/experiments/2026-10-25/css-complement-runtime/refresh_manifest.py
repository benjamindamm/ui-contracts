from pathlib import Path
import json,hashlib,shutil
w=Path('work/css-complement-runtime');p=Path('/Users/kcnpxcp/Dev/GitHub/ui-contracts/docs/research');dest=p/'experiments/2026-10-25/css-complement-runtime';h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();m=json.loads((w/'source-manifest.json').read_text());exclude={'integrate.py','source-manifest.json','original-scxml.min.js','original-polyfill.min.js','apg-pattern-original.html','apg-source-review.json','apg-source-review-original-excerpts.json','aria-status-source-capture.json','verify_export.py'};m['own_files']=[{'file':str(f.relative_to(w)),'sha256':h(f)}for f in sorted(w.rglob('*'))if f.is_file()and f.name not in exclude];m['original_web_sources']=json.loads((w/'source-review.json').read_text());m['own_document_path_error_preserved']=True;(w/'source-manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
for f in [w/x['file']for x in m['own_files']]+[w/'source-manifest.json']:
 target=dest/f.relative_to(w);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f,target)
print('Final owned research inputs, baseline/remainder, observations and source/own-role corrections hashed and mirrored.')
