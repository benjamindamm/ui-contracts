// Additional bounded research binding; original modules unmodified.
// Failed preparation becomes a distinct original-interpreter error-relay actor,
// never a successful overlay/scroll child or a swallowed diagnostic.
const fs=require('fs'),path=require('path'),{fileURLToPath}=require('url');
const scxml=require('../scxml-runtime/tool/node_modules/@scion-scxml/scxml');
const compile=(url,text)=>new Promise((res,rej)=>scxml.documentStringToModel(url,text,(e,m)=>e?rej(e):res(m)));
const prepare=m=>new Promise((res,rej)=>m.prepare((e,f)=>e?rej(e):res(f)));
function makeAdapter(hooks,variant='unique'){
 const tokens=[],invokers={};
 function invoke(parent,obj,_inherited,cb){
  const ctx={parent,obj,level:path.basename(obj.src,'.scxml')};const token={ctx,settled:false,child:null};tokens.push(token);
  async function build(file,params,relay){
   const url=new URL('file://'+file),text=fs.readFileSync(file,'utf8');
   const f=await prepare(await compile(url.href,text));const child=new scxml.core.Statechart(f,{parentSession:parent,invokeid:obj.id,params,invokers});token.child=child;ctx.relay=relay;
   hooks.created(ctx,child);cb(null,child);
   setImmediate(()=>{try{const d=parent.getSnapshot()[3];if(parent.isFinal()||!parent.getConfiguration().some(s=>['open','active'].includes(s))||d.epoch!==obj.params.epoch){child.cancel();hooks.log('start.cancelled',ctx);return;}hooks.log(relay?'error-relay.start':'start.allowed',ctx);child.start();}finally{token.settled=true;}});
  }
  (async()=>{const url=new URL(obj.src,obj.docUrl),file=path.resolve(fileURLToPath(url));
   if(url.protocol!=='file:'||!['overlay.scxml','scroll.scxml'].some(n=>file===path.resolve(__dirname,variant,n)))throw Error('Unsupported research source');
   hooks.log('invoke.begin',ctx);await hooks.before(ctx);
   await build(ctx.invalid?path.resolve(__dirname,'invalid.scxml'):file,obj.params,false);
  })().catch(async error=>{
   hooks.log('init.error',ctx,{error:String(error)});
   try{await build(path.resolve(__dirname,'error-relay.scxml'),{...obj.params,fault:String(error)},true);}
   catch(relayError){hooks.log('error-relay.failed',ctx,{error:String(relayError)});token.settled=true;cb(relayError);}
  });
 }
 for(const t of ['scxml','http://www.w3.org/TR/scxml/','http://www.w3.org/TR/scxml'])invokers[t]=invoke;
 // Host-side bounded drain protocol; no writes into native invocation maps.
 // Includes outstanding descendant preparations for this owner and epoch.
 invokers.researchDrain=async(owner,epoch)=>{const end=Date.now()+2500;while(tokens.some(t=>t.ctx.obj.params.owner===owner&&t.ctx.obj.params.epoch===epoch&&(!t.settled||!t.child?.isFinal()))){if(Date.now()>end)throw Error('Drain deadline');await new Promise(r=>setTimeout(r,2));}await new Promise(r=>setImmediate(r));};
 return invokers;
}
module.exports={scxml,compile,prepare,makeAdapter};
