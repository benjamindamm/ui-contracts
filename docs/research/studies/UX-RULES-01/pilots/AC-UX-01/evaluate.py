#!/usr/bin/env python3
"""Bounded candidate adapter. Metadata/bindings are own code; decisions/row trace are native DMN."""
import argparse,hashlib,json,os,subprocess
from pathlib import Path
from lxml import etree
from jsonschema import Draft7Validator
HERE=Path(__file__).resolve().parent;STUDY=HERE.parents[1];ROOT=STUDY.parents[3];CANDIDATE=HERE/'candidate'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
class Rejected(ValueError):pass
def need(test,message):
 if not test:raise Rejected(message)
def bound(base,ref):
 p=(base/ref['file']).resolve();need(p.is_relative_to(base.resolve()),'profile-path-escape');need(p.is_file() and sha(p)==ref['sha256'],'profile-artifact-stale:'+ref['file']);return p

def evaluate(request,profile=None,repo=ROOT):
 called=False
 try:
  profile=load(CANDIDATE/'ux-profile.json') if profile is None else profile
  errors=list(Draft7Validator(load(CANDIDATE/'profile.schema.json')).iter_errors(profile));need(not errors,'profile-schema:'+('; '.join(e.message for e in errors)))
  rules=profile['rules'];need(len({r['id'] for r in rules})==3,'duplicate-rule-identity');need({r['decisionId'] for r in rules}=={'creation','cardinality','labels'},'unsupported-decisions')
  need(request.get('library')==profile['library'],'wrong-library');need(request.get('componentId')==profile['componentId'],'wrong-component');need(request.get('revision')==profile['definition']['revision'],'wrong-revision')
  manifestPath=(CANDIDATE/profile['definition']['manifest']).resolve();need(manifestPath==STUDY/'baseline.json','unsupported-manifest-root');need(sha(manifestPath)==profile['definition']['sha256'],'manifest-stale')
  manifest=load(manifestPath)['definition'];need(manifest['revision']==profile['definition']['revision'],'profile-definition-revision-mismatch')
  lib=(repo/manifest['root']).resolve();need(lib.is_relative_to(repo.resolve()),'library-path-escape')
  for name,h in manifest['files'].items():
   f=(lib/name).resolve();need(f.is_relative_to(lib) and f.is_file() and sha(f)==h,'source-stale:'+name)
  index=load(lib/'library.json');need(index['components']['Autocomplete']==profile['componentPath'],'component-index-mismatch');need(load(lib/profile['componentPath'])['id']==profile['componentId'],'component-identity-mismatch')
  model=bound(CANDIDATE,profile['logic']);vocab=load(bound(CANDIDATE,profile['vocabulary']));sources=load(bound(CANDIDATE,profile['sources']))
  parser=etree.XMLParser(no_network=True,resolve_entities=False);tree=etree.parse(str(model),parser)
  schema=etree.XMLSchema(etree.parse(str(STUDY/'runs/01/schemas/DMN15.xsd'),parser));need(schema.validate(tree),'DMN-original-schema-rejected')
  rows={n.get('id'):n for n in tree.xpath('//*[local-name()="rule"]')};need(set(rows)==set(profile['nativeRows']),'native-row-map-incomplete')
  byId={r['id']:r for r in rules}
  for id,entry in profile['nativeRows'].items():
   need(entry['ruleId'] in byId,'unknown-rule-map');node=rows[id];decision=node.xpath('ancestor::*[local-name()="decision"]')[0].get('id');need(decision==byId[entry['ruleId']]['decisionId'],'row-wrong-decision')
   text=node.xpath('./*[local-name()="outputEntry"]/*[local-name()="text"]/text()');need(len(text)==1 and json.loads(text[0])==entry['outcome'],'row-outcome-mismatch')
  # Focused anchor checks, no import of unrelated engine probes or their dependencies.
  evidence={s['id']:s for s in sources['external']}
  for anchor in sources['localAnchors']:
   f=(lib/anchor['path']).resolve();need(f.is_relative_to(lib) and anchor['path'] in manifest['files'] and sha(f)==anchor['sha256'],'anchor-source-stale')
   if anchor['kind']=='literal-text':need(anchor['anchor'] in f.read_text(),'missing-text-anchor')
   else:
    if anchor['kind']=='json-pointer':
     value=load(f)
     for part in anchor['anchor'].split('/')[1:]:
      key=part.replace('~1','/').replace('~0','~');value=value[int(key)] if isinstance(value,list) else value[key]
     need(isinstance(value,str) and value==anchor['expected'],'anchor-value-mismatch:'+anchor['id'])
    elif anchor['kind']=='scxml-state':
     doc=etree.parse(str(f),parser);need(len(doc.xpath('//*[local-name()="state" and @id=$id]',id=anchor['anchor']))==1,'missing-state-anchor')
    else:need(False,'unsupported-anchor-kind')
   evidence[anchor['id']]=anchor
  for rule in rules:need(rule['evidence'] and all(id in evidence for id in rule['evidence']),'missing-rule-evidence')
  need(isinstance(request.get('facts'),dict),'facts-object-required');allowed=set(vocab['facts']);need(set(request['facts']).issubset(allowed),'unknown-fact')
  inputs={};diagnostics=[];factEvidence={}
  for name in allowed:
   if name not in request['facts']:inputs[name]=None;diagnostics.append({'fact':name,'state':'missing'});continue
   fact=request['facts'][name];need(isinstance(fact,dict) and 'value' in fact and isinstance(fact.get('source'),dict) and isinstance(fact['source'].get('reference'),str) and bool(fact['source']['reference']) and fact['source'].get('kind') in ['scenario-fixture','user-declaration','research-observation'],'fact-provenance-required:'+name)
   inputs[name]=fact['value'];factEvidence[name]=fact['source'];diagnostics.append({'fact':name,'state':'explicit-null' if fact['value'] is None else 'provided'})
  exceptions=request.get('exceptions',[]);need(isinstance(exceptions,list),'exceptions-array-required');need(len(exceptions)<=1,'duplicate-exceptions');inputs['labelExceptionApproved']=False
  for exception in exceptions:
   rule=byId.get(exception.get('ruleId'));need(rule is not None and rule['exceptionsAllowed'],'exception-cannot-waive-capability')
   need(exception.get('library')==profile['library'] and exception.get('componentId')==profile['componentId'] and exception.get('revision')==profile['definition']['revision'],'exception-scope-mismatch')
   need(exception.get('reviewer') in profile['exceptionReviewers'] and isinstance(exception.get('rationale'),str) and bool(exception['rationale'].strip()),'exception-review-required');inputs['labelExceptionApproved']=True
  runtime=Path(os.environ.get('UX_RULE_RUNTIME','/tmp/ui-contracts-ux-rules-runtime'));classpath=str(runtime/'classes-ux')+':'+(runtime/'classpath.txt').read_text().strip()
  args=['/opt/homebrew/opt/openjdk/bin/java','-cp',classpath,'UxAuditProbe',str(model),profile['logic']['decision']];called=True
  proc=subprocess.run(args,input=json.dumps(inputs),text=True,capture_output=True,timeout=30);need(proc.returncode==0,'native-process-error:'+proc.stderr)
  native=json.loads(proc.stdout);need(native.get('stage')=='evaluated','native-evaluation-error:'+str(native))
  matched=[id for entry in native['trace'] for id in entry['matchedRowIds']];need(len(matched)==3 and len(set(matched))==3,'ambiguous-native-rule-trace')
  traced=[]
  for rowId in matched:
   need(rowId in profile['nativeRows'],'unknown-native-row');mapping=profile['nativeRows'][rowId];rule=byId[mapping['ruleId']];need(native['value'][rule['decisionId']]==mapping['outcome'],'native-trace-outcome-mismatch')
   traced.append({'ruleId':rule['id'],'nativeRowId':rowId,'strength':rule['strength'],'outcome':mapping['outcome'],'status':rule['status'],'rationale':rule['rationale'],'evidence':[evidence[id] for id in rule['evidence']]})
  need({r['ruleId'] for r in traced}==set(byId),'incomplete-rule-trace')
  return {'overall':native['value']['overall'],'release':False,'scope':'research-candidate-compatibility-only','library':profile['library'],'componentId':profile['componentId'],'revision':profile['definition']['revision'],'profileSha256':sha(CANDIDATE/'ux-profile.json') if profile==load(CANDIDATE/'ux-profile.json') else None,'logicSha256':sha(model),'contextSha256':hashlib.sha256(json.dumps(request,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'decision':native['value'],'rules':traced,'factDiagnostics':diagnostics,'factEvidence':factEvidence,'declaredExceptions':exceptions,'nativeCalled':True,'native':native,'nativeStderr':proc.stderr,'notChecked':['Factual truth of declared inputs','Identity/authority of declared exception reviewer','Full UX/accessibility quality','Agent comprehension','Production suitability']}
 except (Rejected,KeyError,IndexError,TypeError,ValueError,OSError) as e:
  return {'overall':'BLOCKED','release':False,'diagnostic':str(e),'nativeCalled':called}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('context',type=Path);a=p.parse_args();result=evaluate(load(a.context));print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(2 if result['overall']=='BLOCKED' else 0)
