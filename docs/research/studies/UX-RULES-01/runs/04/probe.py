"""ODRL JSON-LD encoding boundary only. NOT an ODRL evaluator/conformance validator."""
from pathlib import Path
import json,hashlib
from rdflib import Graph,Namespace,URIRef,RDF
HERE=Path(__file__).resolve().parent;OUT=HERE/'results';OUT.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ODRL=Namespace('http://www.w3.org/ns/odrl/2/')
base={'@context':{'odrl':str(ODRL)},'@id':'urn:ux-probe:policy','@type':'odrl:Set','odrl:permission':[{'@type':'odrl:Permission','odrl:target':{'@id':'urn:ui-contracts:example:Autocomplete'},'odrl:action':{'@id':'odrl:use'}}],'odrl:prohibition':[{'@type':'odrl:Prohibition','odrl:target':{'@id':'urn:ui-contracts:example:Autocomplete'},'odrl:action':{'@id':'odrl:use'}}]}
policies=[{**base,'odrl:conflict':{'@id':'odrl:'+strategy}} for strategy in ['invalid','perm','prohibit']]
inputs=HERE/'policies.json';inputs.write_text(json.dumps(policies,indent=2)+'\n')
(HERE/'freeze.json').write_text(json.dumps({'files':{'policies.json':sha(inputs),'probe.py':sha(HERE/'probe.py')},'phase':'before JSON-LD parse observations, no policy evaluation'},indent=2)+'\n')
rows=[]
for strategy,p in zip(['invalid','perm','prohibit'],policies):
 g=Graph().parse(data=json.dumps(p),format='json-ld');permissions=list(g.objects(URIRef(base['@id']),ODRL.permission));prohibitions=list(g.objects(URIRef(base['@id']),ODRL.prohibition));terms=list(g.objects(URIRef(base['@id']),ODRL.conflict));ok=len(permissions)==1 and len(prohibitions)==1 and terms==[ODRL[strategy]]
 g.serialize(destination=str(OUT/(strategy+'.ttl')),format='turtle');rows.append({'strategy':strategy,'tripleCount':len(g),'encodingExpectationMet':ok,'parsedConflictTerm':str(terms[0]),'evaluationOutcome':None,'nativeResolverOrConflictEvaluationExecuted':False})
(OUT/'observations.json').write_text(json.dumps(rows,indent=2)+'\n')
summary={'overall':'ENCODING_ONLY','release':False,'encodingChecks':len(rows),'expectationsMet':sum(r['encodingExpectationMet'] for r in rows),'policyEvaluations':0,'scope':'Native rdflib JSON-LD parse only; no automatic enforcement, component hash resolution, obligation or recommendation semantics'}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary));raise SystemExit(0 if all(r['encodingExpectationMet'] for r in rows) else 1)
