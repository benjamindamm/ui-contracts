from pathlib import Path
import json
w=Path(__file__).parent
cases=[('local-output-control','control',True),('missing-output-target','missing-output',False),('wrong-output-kind','wrong-kind',False),('external-output-uri','external-output',False),('unknown-source-path','missing-source',True),('missing-source-file-uri','missing-file',True),('changed-external-source','changed-source',True),('output-semantic-type-conflict','wrong-type',False)]
(w/'cases.json').write_text(json.dumps([{'id':id,'kind':kind,'expectedOk':ok}for id,kind,ok in cases],indent=2)+'\n')
