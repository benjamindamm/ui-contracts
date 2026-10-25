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

module.exports={fixture,data,drain,wait,rejections};
