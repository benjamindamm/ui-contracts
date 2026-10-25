const fs=require('fs'),path=require('path'),crypto=require('crypto');
const w=__dirname,tool=path.resolve(w,'../xstate-validator/tool/node_modules/xstate'),x=require(tool),profile=JSON.parse(fs.readFileSync(path.join(w,'profile.json'))),cases=JSON.parse(fs.readFileSync(path.join(w,'cases.json'))),hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const original=Object.fromEntries(Object.entries(profile.artifacts).map(([d,a])=>[d,fs.readFileSync(path.join(w,'fixtures',a.file))]));
function bind(p,inputs){
 if(new Set(Object.values(p.artifacts).map(a=>a.file)).size!==4)throw Error('domain-file-alias');
 for(const [d,a] of Object.entries(p.artifacts))if(hash(inputs[d])!==a.sha256)throw Error('stale-'+d);
 const cem=JSON.parse(inputs.interface),decl=cem.modules.flatMap(m=>m.declarations||[]).find(d=>d.name===p.interfaceDeclaration);if(!decl)throw Error('missing-interface');
 const config=require(path.join(w,'fixtures',p.artifacts.behavior.file));if(config.id!==p.behaviorDefinition)throw Error('definition-mismatch');
 const names=new Set(decl.cssParts.map(p=>p.name)),html=inputs.accessibility.toString();
 for(const [instance,parts] of Object.entries(p.instances))for(const [part,id]of Object.entries(parts)){
  if(!names.has(part)||!id.startsWith(part+'-'+instance.toLowerCase())||!html.includes('id="'+id+'"'))throw Error('instance-part-mismatch');
 }
 for(const state of Object.keys(config.states))if(!p.stateView[state])throw Error('unmapped-state');
 return x.createMachine(config);
}
const results=[];let a,b;
function record(id,observation,met){results.push({...cases.find(c=>c.id===id),observation,expectationMet:met})}
try{
 const machine=bind(profile,original);record('separate-original-inputs',{domains:Object.keys(original),machineId:machine.id,behaviorForeignImports:require.cache[require.resolve(path.join(w,'fixtures/behavior.cjs'))].children.length>0},machine.id==='Autocomplete'&&Object.keys(original).length===4&&require.cache[require.resolve(path.join(w,'fixtures/behavior.cjs'))].children.length===0);
 a=x.createActor(machine);b=x.createActor(machine);a.start();b.start();const states=()=>({A:a.getSnapshot().value,B:b.getSnapshot().value});let s=states();record('actor-initial',s,s.A==='closed'&&s.B==='closed');
 a.send({type:'OPEN'});s=states();record('open-A',s,s.A==='open'&&s.B==='closed');b.send({type:'OPEN'});a.send({type:'CLOSE'});s=states();record('open-B-close-A',s,s.A==='closed'&&s.B==='open');
 const changed={...original,visual:Buffer.from(original.visual.toString().replaceAll('max-height:160px','max-height:192px'))},p=structuredClone(profile);p.artifacts.visual.sha256=hash(changed.visual);const otherStable=['interface','behavior','accessibility'].every(d=>hash(changed[d])===profile.artifacts[d].sha256);const alt=bind(p,changed);record('visual-change-independent',{onlyVisualHashChanged:otherStable&&p.artifacts.visual.sha256!==profile.artifacts.visual.sha256,initial:x.getInitialSnapshot(alt).value,changedMaxHeight:changed.visual.toString().includes('max-height:192px')},otherStable&&changed.visual.toString().includes('max-height:192px')&&x.getInitialSnapshot(alt).value==='closed');
 for(const[id,mutate,expected]of[
 ['foreign-domain-alias',p=>p.artifacts.behavior={...p.artifacts.visual},'domain-file-alias'],
 ['stale-behavior-hash',p=>p.artifacts.behavior.sha256='0'.repeat(64),'stale-behavior'],
 ['foreign-instance-part',p=>p.instances.A.popup='popup-b','instance-part-mismatch']]){const p=structuredClone(profile);mutate(p);let error=null;try{bind(p,original)}catch(e){error=e.message}record(id,{rejected:!!error,error,checker:'additional own research binder'},error===expected)}
}finally{a?.stop();b?.stop()}
const pkg=JSON.parse(fs.readFileSync(path.join(tool,'package.json')));const out={package:'xstate@'+pkg.version,node:process.version,scope:'SDK behavior contribution with byte-identical CEM/CSS/HTML fixtures; additional own binding; no neutral XState schema, UI/AT or complete autocomplete contract',cases:results};fs.writeFileSync(path.join(w,'results.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out,null,2));if(results.length!==8||results.some(r=>!r.expectationMet))process.exitCode=1;
