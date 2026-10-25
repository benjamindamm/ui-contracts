const fs=require('fs'),path=require('path');const {fixture,data,wait,drain,rejections}=require('./harness.cjs');
const plan=JSON.parse(fs.readFileSync(path.join(__dirname,'cases.json'),'utf8'));
(async()=>{const results=[];for(const c of plan.new_cases){const f=await fixture(c.variant),checks={};let error;const begin=rejections.length;
 try{const r=f.roots;await f.open('B');const b=JSON.stringify(f.snapshot().roots.B);
 if(c.id==='F-01'||c.id==='F-02'){
  const level=c.id==='F-01'?'overlay':'scroll',ctl={owner:'A',level};f.controls.push(ctl);r.A.gen('OPEN');await wait(()=>ctl.release,'held child');r.A.gen('CLOSE');const epoch=data(r.A).epoch;
  let hostPhase='closing',queued=true;
  f.journal.push({type:'host.reopen.queued',epoch});
  const pending=f.invokers.researchDrain('A',epoch).then(()=>{hostPhase='drained';queued=false;f.journal.push({type:'host.drain.complete',epoch});r.A.gen('OPEN');});
  await drain();checks.reopenWaited=queued&&hostPhase==='closing'&&data(r.A).epoch===1&&r.A.getConfiguration().includes('closed');
  ctl.release();await pending;await wait(()=>data(r.A).ready===1,'ready after drain');
  checks.oldChainFinal=f.records.filter(x=>x.owner==='A'&&x.epoch===1).every(x=>x.s.isFinal());
  checks.sameLocalNativeId=f.children('A','overlay').every(x=>x.nativeId==='overlay');
  r.A.gen({name:'SCROLL',data:{offset:5}});await wait(()=>data(r.A).reports===1,'route after drain');checks.routeWorks=data(r.A).lastOffset===5;
 }else if(c.id==='F-03'||c.id==='F-06'){
  const ctl={owner:'A',level:'overlay',invalidAfterRelease:c.id==='F-06'};f.controls.push(ctl);r.A.gen('OPEN');await wait(()=>ctl.release,'old held overlay');r.A.gen('CLOSE');r.A.gen('OPEN');await wait(()=>data(r.A).ready===1,'immediate new ready');
  checks.reopenedBeforeRelease=data(r.A).epoch===2&&!f.children('A','overlay',1).length;
  ctl.release();await wait(()=>f.children('A','overlay',1).length===1,'old completion');await drain();await drain();
  const old=f.children('A','overlay',1)[0],fresh=f.children('A','overlay',2)[0];checks.differentNativeIds=old.nativeId!==fresh.nativeId;
  checks.stableLogicalPath=old.level===fresh.level&&old.owner===fresh.owner;
  checks.oldFinal=old.s.isFinal();checks.currentStillOpen=r.A.getConfiguration().includes('open')&&data(r.A).errors===0&&data(r.A).ready===1;
  if(c.id==='F-06'){checks.errorRetained=f.journal.some(x=>x.type==='init.error'&&x.params.owner==='A'&&x.params.epoch===1);checks.oldErrorRelay=old.relay===true;}
  r.A.gen({name:'SCROLL',data:{offset:9}});await wait(()=>data(r.A).reports===1,'new route preserved');checks.routeWorks=data(r.A).lastOffset===9;
 }else{
  const level=c.id==='F-04'?'overlay':'scroll',ctl={owner:'A',level,fail:true};f.controls.push(ctl);r.A.gen('OPEN');
  await wait(()=>data(r.A).errors===1,'root received actual initialization error');await wait(()=>f.records.filter(x=>x.owner==='A').every(x=>x.s.isFinal()),'all affected actors final');
  checks.realParserFailure=f.journal.some(x=>x.type==='init.error'&&/Unexpected end/.test(x.error));checks.relayExplicit=f.records.some(x=>x.owner==='A'&&x.relay);
  checks.correctRootClosed=r.A.getConfiguration().includes('closed')&&data(r.A).errors===1&&data(r.B).errors===0;
  checks.allAffectedFinal=f.records.filter(x=>x.owner==='A').every(x=>x.s.isFinal());checks.noFalseReady=data(r.A).ready===0;
  checks.faultAtRoot=f.journal.some(x=>x.type==='event'&&x.session==='A'&&x.event.name==='init.failed'&&/Unexpected end/.test(x.event.data.fault));
 }
 checks.bUnchanged=JSON.stringify(f.snapshot().roots.B)===b&&!f.latest('B','scroll').isFinal();checks.noUnhandledRejection=rejections.length===begin;
 }catch(e){error=String(e);checks.executionCompleted=false;}
 const observed=f.snapshot(),journal=f.journal.slice();await f.cleanup();results.push({...c,checks,expectationMet:Object.keys(checks).length>0&&Object.values(checks).every(Boolean),error,observed,journal,cleanup:f.snapshot(),unhandledRejections:rejections.slice(begin)});
 }
 const out={kind:'ip01-specific-lifecycle-variants',package:'@scion-scxml/scxml',version:'4.3.28',node:process.version,new_conditions:6,regressions_counted_again:0,cases:results};fs.writeFileSync(path.join(__dirname,'variant-results.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(results.map(c=>({id:c.id,expectationMet:c.expectationMet,checks:c.checks,error:c.error})),null,2));process.exitCode=results.every(c=>c.expectationMet)?0:1;
})().catch(e=>{fs.writeFileSync(path.join(__dirname,'execution-error.json'),JSON.stringify({error:String(e),stack:e.stack},null,2));console.error(e);process.exitCode=2});
