// Additional research adapter. Only the controlled local child fixture is supported.
// Each invocation uses a fresh original SCXML preparation context; no model cache.
const fs=require('fs'),path=require('path'),{fileURLToPath}=require('url');
const scxml=require('../scxml-runtime/tool/node_modules/@scion-scxml/scxml');
function isolatedInvoker(parent,obj,_inheritedContext,cb){
 let url,text;
 try {url=new URL(obj.src,obj.docUrl);if(url.protocol!=='file:'||path.resolve(fileURLToPath(url))!==path.resolve(__dirname,'child.scxml'))throw Error('Unsupported research child source');text=fs.readFileSync(fileURLToPath(url),'utf8');}
 catch(e){cb(e);return;}
 scxml.documentStringToModel(url.href,text,(err,model)=>{if(err)return cb(err);
  // Deliberately no inherited shared parent execution context. Inputs use original params.
  model.prepare((err,factory)=>{if(err)return cb(err);let child;try{child=new scxml.core.Statechart(factory,{parentSession:parent,invokeid:obj.id,params:obj.params});}catch(e){cb(e);return;}cb(null,child);setImmediate(()=>child.start());});
 });
}
module.exports={scxml:isolatedInvoker,'http://www.w3.org/TR/scxml/':isolatedInvoker,'http://www.w3.org/TR/scxml':isolatedInvoker};
