from pathlib import Path
import json,hashlib
w=Path(__file__).parent
cases=[('zag-original-connect','zag','base',True,None),('zag-custom-root-ids','zag','rename',True,None),('zag-colliding-content-ids','zag','collision',False,'duplicate-host-id'),('zag-external-role-conflict','zag','role',False,'external-role-conflict'),('ark-original-context','ark','base',True,None),('ark-custom-root-ids','ark','rename',True,None),('ark-input-prop-id-override','ark','input-override',False,'missing-controlled-input'),('ark-content-prop-id-override','ark','content-override',False,'missing-controls-target')]
(w/'cases.json').write_text(json.dumps([{'id':id,'candidate':candidate,'kind':kind,'expected':{'accepted':ok,'error':error}}for id,candidate,kind,ok,error in cases],indent=2)+'\n')
