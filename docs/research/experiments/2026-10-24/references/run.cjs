const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const ts=require(process.env.PROBE_TYPESCRIPT||'../ts-tool/node_modules/typescript');
const root=__dirname,src=path.join(root,'sources'),build=path.join(root,'build'),fixtures=path.join(root,'fixtures');
fs.mkdirSync(build,{recursive:true});fs.mkdirSync(fixtures,{recursive:true});fs.writeFileSync(path.join(build,'package.json'),JSON.stringify({type:'commonjs'}));
const compiled=[];
for(const name of fs.readdirSync(src).filter(s=>s.endsWith('.ts'))){const code=fs.readFileSync(path.join(src,name),'utf8');const r=ts.transpileModule(code,{fileName:name,reportDiagnostics:true,compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.CommonJS,esModuleInterop:true}});assert.equal(r.diagnostics?.length??0,0);fs.writeFileSync(path.join(build,name.replace(/\.ts$/,'.js')),r.outputText);compiled.push(name);}
const {resolveDocument}=require('./build/resolve.js'),{resolveImports}=require('./build/import-resolver.js'),{bundle}=require('./build/bundler.js');
const clone=x=>JSON.parse(JSON.stringify(x));
const doc=(id)=>({'$schema':'https://raw.githubusercontent.com/johnlindquist/uxspec/20dfae0e7224d952e198afdf4ffed26d6fd67180/schema/uxspec.schema.json','$description':'Isolated reference proof fixture','$machine':{id,initial:'idle',states:{idle:{}}}});
const library=doc('library');library.$elements={Outer:{type:'group',children:[{$ref:'Inner'}]},Inner:{type:'text',content:'LIBRARY'}};library.$machine.$visual={slots:{content:[{$ref:'Outer'}]}};
const app=doc('app');app.$imports={lib:{from:'./library.json',elements:true,tokens:true}};app.$elements={Inner:{type:'text',content:'APP'}};app.$machine.$visual={slots:{content:[{$ref:'lib:Outer'}]}};
const records=[];
const store=(name,data)=>fs.writeFileSync(path.join(fixtures,name),JSON.stringify(data,null,2)+'\n');
function normal(x){return JSON.parse(JSON.stringify(x,(_k,v)=>v instanceof Map?Object.fromEntries(v):v).replaceAll(root,'<probe-root>'));}
async function run(id,inputFiles,fn,observe){const dir=path.join(fixtures,id);fs.mkdirSync(dir,{recursive:true});for(const [n,d] of Object.entries(inputFiles))fs.writeFileSync(path.join(dir,n),typeof d==='string'?d:JSON.stringify(d,null,2)+'\n');let output;try{output=await fn(dir);}catch(e){output={thrown:{name:e.name,message:e.message}};}const observation=observe(output);records.push({id,inputs:Object.keys(inputFiles).map(n=>'fixtures/'+id+'/'+n),output:normal(output),observation:normal(observation)});console.log(id,JSON.stringify(observation));}
async function resolveFile(dir){const document=JSON.parse(fs.readFileSync(path.join(dir,'app.json'),'utf8')),issues=[],trace=[];const imports=await resolveImports(document,path.join(dir,'app.json'),issues,trace);const resolved=resolveDocument(document,issues,trace,imports);return{resolved,issues,trace,namespaces:imports.namespaces};}
const content=o=>o.resolved?.$machine?.$visual?.slots?.content?.[0]?.children?.[0]?.content;
(async()=>{
 await run('ref-01-local-control',{'app.json':library},resolveFile,o=>({childContent:content(o),issueCodes:o.issues?.map(x=>x.code)}));
 await run('ref-02-imported-shadowing',{'app.json':app,'library.json':library},resolveFile,o=>({childContent:content(o),issueCodes:o.issues?.map(x=>x.code)}));
 const noLocal=clone(app);delete noLocal.$elements;
 await run('ref-03-imported-no-local',{'app.json':noLocal,'library.json':library},resolveFile,o=>({childContent:content(o)??null,issueCodes:o.issues?.map(x=>x.code)}));
 const missingArea=doc('app');missingArea.$imports={lib:{from:'./empty.json',tokens:true}};
 await run('ref-04-missing-import-area',{'app.json':missingArea,'empty.json':doc('empty')},resolveFile,o=>({issueCodes:o.issues?.map(x=>x.code),namespaceHasTokens:!!o.namespaces.get('lib')?.tokens}));
 const missingFile=clone(missingArea);missingFile.$imports.lib.from='./missing.json';
 await run('ref-05-missing-file-control',{'app.json':missingFile},resolveFile,o=>({issueCodes:o.issues?.map(x=>x.code)}));
 const foreign=doc('app');foreign.$imports={api:{from:'./cem.json',elements:true}};foreign.$machine.$visual={slots:{content:[{$ref:'api:Autocomplete'}]}};
 const cem=JSON.parse(fs.readFileSync(path.join(root,'cem-control.json'),'utf8'));
 await run('ref-06-original-cem-target',{'app.json':foreign,'cem.json':cem},resolveFile,o=>({issueCodes:o.issues?.map(x=>x.code),namespaceHasElements:!!o.namespaces.get('api')?.elements}));
 const unit=doc('app');unit.$tokens={gap:{$type:'dimension',$value:{value:1,unit:'rem'}}};unit.$machine.$visual={container:{padding:'{gap}'}};
 await run('ref-07-unit-value',{'app.json':unit},resolveFile,o=>({resolvedPadding:o.resolved?.$machine?.$visual?.container?.padding,issueCodes:o.issues?.map(x=>x.code)}));
 const params=doc('app');params.$elements={Label:{type:'text',params:['label'],content:['param','label']}};params.$machine.$visual={slots:{content:[{$ref:'Label',label:'A'},{$ref:'Label',label:'B'}]}};
 await run('ref-08-separate-expansions',{'app.json':params},async dir=>{const x=await resolveFile(dir);const nodes=x.resolved.$machine.$visual.slots.content;x.before=clone(nodes);nodes[0].content='changed-A';x.after=clone(nodes);return x;},o=>({before:o.before,after:o.after,issueCodes:o.issues?.map(x=>x.code)}));
 const entry=doc('root');entry.$imports={a:{from:'./a.json',machine:true},b:{from:'./b.json',machine:true}};const a=doc('child-a'),b=doc('child-b');a.$context={label:{type:'string',default:'A'}};b.$context={label:{type:'string',default:'B'}};
 await run('bundle-01-unique-ids',{'app.json':entry,'a.json':a,'b.json':b},dir=>bundle(path.join(dir,'app.json'),{trace:true}),o=>({ok:o.ok,moduleIds:Object.keys(o.bundled?.modules??{}),issueCodes:o.issues?.map(x=>x.code)}));
 const da=clone(a),db=clone(b);da.$machine.id='shared';db.$machine.id='shared';
 await run('bundle-02-duplicate-child-id',{'app.json':entry,'a.json':da,'b.json':db},dir=>bundle(path.join(dir,'app.json'),{trace:true}),o=>({ok:o.ok,moduleIds:Object.keys(o.bundled?.modules??{}),sharedDefault:o.bundled?.modules?.shared?.contextSchema?.label?.default,issueCodes:o.issues?.map(x=>x.code)}));
 const collide=doc('shared');collide.$context={label:{type:'string',default:'ROOT'}};collide.$imports={a:{from:'./a.json',machine:true}};
 await run('bundle-03-entry-id-collision',{'app.json':collide,'a.json':da},dir=>bundle(path.join(dir,'app.json'),{trace:true}),o=>({ok:o.ok,entry:o.bundled?.entry,moduleIds:Object.keys(o.bundled?.modules??{}),entryDefault:o.bundled?.modules?.shared?.contextSchema?.label?.default,issueCodes:o.issues?.map(x=>x.code)}));
 const parent=doc('parent');parent.$imports={child:{from:'./child.json',machine:true}};const child=doc('child');child.$imports={grand:{from:'./grand.json',machine:true}};child.$machine.states.idle.invoke=[{kind:'machine',src:'grand',id:'grand-use'}];const grand=doc('grand');
 await run('bundle-04-transitive-child',{'app.json':parent,'child.json':child,'grand.json':grand},dir=>bundle(path.join(dir,'app.json'),{trace:true}),o=>({ok:o.ok,moduleIds:Object.keys(o.bundled?.modules??{}),childDependencies:o.bundled?.modules?.child?.dependencies,issueCodes:o.issues?.map(x=>x.code)}));
 const cyc=doc('app');cyc.$elements={Self:{$ref:'Self'}};cyc.$machine.$visual={slots:{content:[{$ref:'Self'}]}};
 await run('ref-09-element-cycle',{'app.json':cyc},resolveFile,o=>({thrown:o.thrown,issueCodes:o.issues?.map(x=>x.code)}));
 const self=doc('app');self.$imports={self:{from:'./app.json',machine:true}};
 await run('ref-10-file-self-cycle-control',{'app.json':self},resolveFile,o=>({issueCodes:o.issues?.map(x=>x.code)}));
 const report={node:process.version,typescript:ts.version,sourceModified:false,transpilation:{target:'ES2022',module:'CommonJS',esModuleInterop:true,files:compiled,semantic_typecheck:false},pathNormalization:'Absolute fixture-root paths replaced with <probe-root> in recorded output; contents and diagnostics otherwise preserved',uiRendered:false,actorRuntimeExecuted:false,cases:records};
 fs.writeFileSync(path.join(root,'results.json'),JSON.stringify(report,null,2)+'\n');
})();
