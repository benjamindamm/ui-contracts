const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {scxml,compile,prepare,makeAdapter}=require('./adapter.cjs');
const cases=JSON.parse(fs.readFileSync(path.join(__dirname,'../ip01-lifecycle/cases.json'),'utf8')).cases;
const data=s=>s.getSnapshot()[3];
const drain=()=>new Promise(r=>setTimeout(r,12));
const wait=async(fn,label)=>{const end=Date.now()+2500;while(!fn()){if(Date.now()>end)throw Error('Deadline: '+label);await new Promise(r=>setTimeout(r,2));}};
const rejections=[];process.on('unhandledRejection',e=>rejections.push({error:String(e)}));
async function fixture(variant='unique'){
 const records=[],journal=[],roots={},controls=[],map=new WeakMap();let seq=0;
 const describe=s=>map.get(s)||'?';
 const log=(type,ctx,extra={})=>journal.push({seq:++seq,type,parent:describe(ctx.parent),localId:ctx.obj.id,params:ctx.obj.params,...extra});
 const invokers=makeAdapter({log,before:async ctx=>{const c=controls.find(c=>!c.used&&c.owner===ctx.obj.params.owner&&c.level===ctx.level);if(!c)return;c.used=true;c.ctx=ctx;log('test.barrier.reached',ctx);if(c.fail){ctx.invalid=true;return;}await new Promise(r=>c.release=r);if(c.invalidAfterRelease)ctx.invalid=true;},created:(ctx,s)=>{const id=describe(ctx.parent)+'/'+ctx.level+'@'+ctx.obj.params.epoch;map.set(s,id);records.push({id,nativeId:ctx.obj.id,relay:!!ctx.relay,level:ctx.level,parent:describe(ctx.parent),owner:ctx.obj.params.owner,epoch:ctx.obj.params.epoch,s});watch(s,id);}},variant);
 function watch(s,id){s.on('onBigStepBegin',e=>{if(e)journal.push({seq:++seq,type:'event',session:id,event:JSON.parse(JSON.stringify(e))});});s.on('onError',e=>journal.push({seq:++seq,type:'runtime.error',session:id,event:e}));s.on('onExitInterpreter',()=>journal.push({seq:++seq,type:'interpreter.exit',session:id}));s.on('onEntry',state=>journal.push({seq:++seq,type:'entry',session:id,state}));}
 for(const owner of ['A','B']){const file=path.join(__dirname,variant,'parent.scxml'),m=await compile(pathToFileURL(file).href,fs.readFileSync(file,'utf8'));const s=new scxml.core.Statechart(await prepare(m),{params:{owner},invokers});roots[owner]=s;map.set(s,owner);watch(s,owner);s.start();}
 const children=(owner,level,epoch)=>records.filter(r=>r.owner===owner&&r.level===level&&(epoch===undefined||r.epoch===epoch));
 const latest=(owner,level)=>children(owner,level).slice(-1)[0]?.s;
 async function open(owner){const n=data(roots[owner]).ready;roots[owner].gen('OPEN');await wait(()=>data(roots[owner]).ready>n,'ready '+owner);}
 const snapshot=()=>({roots:Object.fromEntries(Object.entries(roots).map(([k,s])=>[k,{configuration:s.getConfiguration(),final:s.isFinal(),data:data(s)}])),children:records.map(r=>({id:r.id,parent:r.parent,level:r.level,nativeId:r.nativeId,relay:r.relay,owner:r.owner,epoch:r.epoch,final:r.s.isFinal(),configuration:r.s.getConfiguration(),data:data(r.s)}))});
 async function cleanup(){for(const s of Object.values(roots))s.cancel();for(const c of controls)if(c.release)c.release();await drain();await drain();for(const r of records)r.s.cancel();await drain();}
 return {roots,controls,records,journal,children,latest,open,snapshot,cleanup,invokers};
}
(async()=>{const results=[];for(const c of cases){const f=await fixture(),checks={};let error;const beforeReject=rejections.length;try{
 const {roots:r}=f;
 if(c.id==='LC-01'){
  await f.open('A');await f.open('B');
  checks.fourChildren=f.records.length===4;checks.distinctObjects=new Set(f.records.map(x=>x.s)).size===4;
  checks.parameters=f.records.every(x=>data(x.s).owner===x.owner&&data(x.s).epoch===1);
  checks.parentContexts=new Set(f.records.map(x=>x.parent)).size===4;
  checks.sameLocalIds=['A','B'].every(o=>f.children(o,'overlay').length===1&&f.children(o,'scroll').length===1);
 }else if(c.id==='LC-02'){
  await f.open('A');await f.open('B');const b=JSON.stringify(f.snapshot().roots.B),n=f.journal.length;
  r.A.gen({name:'SCROLL',data:{offset:40}});await wait(()=>data(r.A).reports===1,'A report');await drain();
  checks.aUpdated=data(r.A).lastOffset===40&&data(f.latest('A','scroll')).offset===40;
  checks.bUnchanged=JSON.stringify(f.snapshot().roots.B)===b&&data(f.latest('B','scroll')).offset===0;
  checks.noBReport=!f.journal.slice(n).some(x=>x.type==='event'&&x.session==='B'&&x.event.name==='overlay.report');
 }else if(c.id==='LC-03'){
  await f.open('A');await f.open('B');
  for(const [o,v] of [['A',11],['B',22]])r[o].gen({name:'SCROLL',data:{offset:v}});
  await wait(()=>data(r.A).reports===1&&data(r.B).reports===1,'both reports');
  const a=f.latest('A','overlay');a.gen({name:'scroll.report',data:{owner:'B',epoch:1,offset:99}});
  r.A.gen({name:'overlay.report',data:{owner:'B',epoch:1,offset:99}});await drain();
  checks.nativeLocalReports=data(r.A).lastOffset===11&&data(r.B).lastOffset===22;
  checks.additionalForeignGuards=data(a).rejected===1&&data(r.A).rejected===1&&data(r.A).reports===1;
 }else if(c.id==='LC-04'||c.id==='LC-05'){
  await f.open('B');const b=JSON.stringify(f.snapshot().roots.B);const level=c.id==='LC-04'?'overlay':'scroll';const ctl={owner:'A',level};f.controls.push(ctl);r.A.gen('OPEN');await wait(()=>ctl.release,'barrier '+level);
  r.A.gen('CLOSE');ctl.release();await wait(()=>f.children('A',level).length===1,'late child creation');await drain();await drain();
  checks.aClosed=r.A.getConfiguration().includes('closed');checks.allAFinal=f.records.filter(x=>x.owner==='A').every(x=>x.s.isFinal());
  checks.noLateReady=data(r.A).ready===0;checks.bUnchanged=JSON.stringify(f.snapshot().roots.B)===b&&!f.latest('B','scroll').isFinal();
  checks.noLateDescendant=level!=='overlay'||f.children('A','scroll').length===0;
 }else if(c.id==='LC-06'){
  await f.open('B');const b=JSON.stringify(f.snapshot().roots.B),ctl={owner:'A',level:'overlay'};f.controls.push(ctl);r.A.gen('OPEN');await wait(()=>ctl.release,'old overlay held');
  r.A.gen('CLOSE');r.A.gen('OPEN');await wait(()=>data(r.A).ready===1,'new epoch ready');
  ctl.release();await wait(()=>f.children('A','overlay',1).length===1,'old child delivered');await drain();await drain();
  r.A.gen({name:'overlay.ready',data:{owner:'A',epoch:1}});r.A.gen({name:'overlay.report',data:{owner:'A',epoch:1,offset:99}});
  checks.newEpoch=data(r.A).epoch===2&&data(f.latest('A','scroll')).epoch===2;
  checks.oldChildFinal=f.children('A','overlay',1).every(x=>x.s.isFinal());checks.staleRejected=data(r.A).ready===1&&data(r.A).reports===0&&data(r.A).rejected===2;
  r.A.gen({name:'SCROLL',data:{offset:7}});try{await wait(()=>data(r.A).reports===1,'new route after old cleanup');checks.newRoute=data(r.A).lastOffset===7;}catch(e){checks.newRoute=false;error=String(e);}
  checks.bUnchanged=JSON.stringify(f.snapshot().roots.B)===b&&data(f.latest('B','scroll')).offset===0;
 }else if(c.id==='LC-07'){
  const sub=[];for(const level of ['overlay','scroll']){
   const g=await fixture();try{await g.open('B');const b=JSON.stringify(g.snapshot().roots.B),ctl={owner:'A',level,fail:true};g.controls.push(ctl);g.roots.A.gen('OPEN');await wait(()=>ctl.used,'failure delivered');try{await wait(()=>data(g.roots.A).errors===1&&g.records.filter(x=>x.owner==='A').every(x=>x.s.isFinal()),'error propagation and cleanup');}catch(e){g.journal.push({type:'test.deadline',error:String(e)});}await drain();
    const observations={level,correctRootError:data(g.roots.A).errors===1,affectedChainClosed:g.roots.A.getConfiguration().includes('closed')&&g.records.filter(x=>x.owner==='A').every(x=>x.s.isFinal()),noFalseReady:data(g.roots.A).ready===0,bUnchanged:JSON.stringify(g.snapshot().roots.B)===b,snapshot:g.snapshot(),journal:g.journal.slice()};sub.push(observations);
   }finally{await g.cleanup();if(sub.length&&sub[sub.length-1].level===level)sub[sub.length-1].cleanup=g.snapshot();}}
  checks.overlayFailurePropagated=sub[0].correctRootError&&sub[0].affectedChainClosed;checks.scrollFailurePropagated=sub[1].correctRootError&&sub[1].affectedChainClosed;checks.noFalseReady=sub.every(x=>x.noFalseReady);checks.bUnchanged=sub.every(x=>x.bUnchanged);f.journal.push({type:'failure-subcases',subcases:sub});
 }else if(c.id==='LC-08'){
  await f.open('A');await f.open('B');const b=JSON.stringify(f.snapshot().roots.B);r.A.gen('CLOSE');await drain();const once=JSON.stringify(f.snapshot().roots.A);r.A.gen('CLOSE');r.A.gen('CLOSE');await drain();
  checks.stableClosed=r.A.getConfiguration().includes('closed')&&JSON.stringify(f.snapshot().roots.A)===once;checks.allAFinal=f.records.filter(x=>x.owner==='A').every(x=>x.s.isFinal());checks.bUnchanged=JSON.stringify(f.snapshot().roots.B)===b&&!f.latest('B','scroll').isFinal();
 }
 }catch(e){error=String(e);checks.executionCompleted=false;}
 const observed=f.snapshot();const journal=f.journal.slice();await f.cleanup();results.push({...c,checks,expectationMet:Object.keys(checks).length>0&&Object.values(checks).every(Boolean),error,observed,journal,unhandledRejections:rejections.slice(beforeReject),cleanup:f.snapshot()});
 }
 const output={kind:'ip01-unique-native-id-regression',runtime:'@scion-scxml/scxml 4.3.28',node:process.version,adapter:'additional local fresh-prepare invoker; original idlocation generation; explicit error-relay actor after actual malformed preparation',cases:results};fs.writeFileSync(path.join(__dirname,'results.json'),JSON.stringify(output,null,2)+'\n');console.log(JSON.stringify(results.map(x=>({id:x.id,checks:x.checks,expectationMet:x.expectationMet,error:x.error})),null,2));process.exitCode=results.every(x=>x.expectationMet)?0:1;
})().catch(e=>{fs.writeFileSync(path.join(__dirname,'execution-error.json'),JSON.stringify({error:String(e),stack:e.stack},null,2));console.error(e);process.exitCode=2;});
