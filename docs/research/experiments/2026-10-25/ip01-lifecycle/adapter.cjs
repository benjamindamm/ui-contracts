// Additional bounded research adapter, not original runtime code.
// Extends the prior fresh-prepare adapter to two allowed local sources.
const fs=require('fs'),path=require('path'),{fileURLToPath}=require('url');
const scxml=require('../scxml-runtime/tool/node_modules/@scion-scxml/scxml');
const compile=(url,text)=>new Promise((res,rej)=>scxml.documentStringToModel(url,text,(e,m)=>e?rej(e):res(m)));
const prepare=m=>new Promise((res,rej)=>m.prepare((e,f)=>e?rej(e):res(f)));
function makeAdapter(hooks){
 const invokers={};
 function invoke(parent,obj,_inherited,cb){
  const ctx={parent,obj};
  (async()=>{
   const url=new URL(obj.src,obj.docUrl),file=path.resolve(fileURLToPath(url));
   if(url.protocol!=='file:'||!['overlay.scxml','scroll.scxml'].some(n=>file===path.resolve(__dirname,n)))throw Error('Unsupported research child');
   hooks.log('invoke.begin',ctx);
   await hooks.before(ctx); // Controlled test barrier/fault; not a production scheduler.
   const factory=await prepare(await compile(url.href,fs.readFileSync(file,'utf8')));
   const child=new scxml.core.Statechart(factory,{parentSession:parent,invokeid:obj.id,params:obj.params,invokers});
   hooks.created(ctx,child);cb(null,child);
   setImmediate(()=>{
    const d=parent.getSnapshot()[3];
    if(parent.isFinal()||!parent.getConfiguration().some(s=>['open','active'].includes(s))||d.epoch!==obj.params.epoch){child.cancel();hooks.log('start.cancelled',ctx);return;}
    hooks.log('start.allowed',ctx);child.start();
   });
  })().catch(e=>{hooks.log('init.error',ctx,{error:String(e)});cb(e);});
 }
 for(const t of ['scxml','http://www.w3.org/TR/scxml/','http://www.w3.org/TR/scxml'])invokers[t]=invoke;
 return invokers;
}
module.exports={scxml,compile,prepare,makeAdapter};
