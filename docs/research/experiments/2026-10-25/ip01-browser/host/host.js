/* Additional research host: original SCXML owns state/data/navigation;
   this file binds typed I/O, source templates, actual DOM and measurements. */
(async()=>{
 const log=[],diagnostics=[],requests=[],actors=[],events={A:[],B:[]},roots={},parents={},views={},gates=[];let sequence=0,mode='auto';
 const journal=(type,data={})=>log.push({sequence:++sequence,type,...data});
 const errors=[];window.addEventListener('error',e=>errors.push({message:e.message}));window.addEventListener('unhandledrejection',e=>errors.push({rejection:String(e.reason)}));
 const hash=async bytes=>[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(x=>x.toString(16).padStart(2,'0')).join('');
 const manifest=await(await fetch('/manifest.json',{cache:'no-store'})).json(),texts={};
 for(const [file,sha]of Object.entries(manifest.files)){const r=await fetch('/'+file,{cache:'no-store'}),bytes=await r.arrayBuffer();if(!r.ok||await hash(bytes)!==sha)throw Error('Source fingerprint mismatch '+file);texts[file]=new TextDecoder().decode(bytes);}
 const api=window.scion.scxml,core=window.scion.core;
 const compile=(url,text)=>new Promise((yes,no)=>{try{api.documentStringToModel(url,text,(e,m)=>e?no(e):yes(m));}catch(e){no(e)}}),prepare=m=>new Promise((yes,no)=>m.prepare((e,f)=>e?no(e):yes(f)));
 const factory=async(file,override)=>prepare(await compile(location.origin+'/'+file,override===undefined?texts[file]:override));
 const data=s=>s.getSnapshot()[3],phase=s=>s.getConfiguration()[0];
 const token=path=>{let x=JSON.parse(texts['sources/visual/tokens.json']);for(const part of path.split('.'))x=x[part];return typeof x.$value==='string'?token(x.$value.slice(1,-1)):x.$value;};
 for(const [name,path]of [['gap','autocomplete.gap'],['max-height','autocomplete.maxHeight'],['row-height','autocomplete.rowHeight']]){const d=token(path);document.documentElement.style.setProperty('--'+name,d.value+d.unit);}
 for(const kind of ['autocomplete','overlay','scroll-area']){const style=document.createElement('style');style.textContent=texts['sources/'+kind+'/layout.css'];document.head.append(style);}
 const types=JSON.parse(texts['interface-types.json']);
 function typed(value,t){if(t.kind==='optional')return typed(value,t.item);if(t.kind==='string')return typeof value==='string';if(t.kind==='number')return typeof value==='number'&&Number.isFinite(value);if(t.kind==='boolean')return typeof value==='boolean';if(t.kind==='array')return Array.isArray(value)&&value.every(x=>typed(x,t.item));if(t.kind==='record')return value!==null&&typeof value==='object'&&!Array.isArray(value)&&Object.keys(value).every(k=>k in t.fields)&&Object.entries(t.fields).every(([k,v])=>k in value?typed(value[k],v.type):v.optional);return false;}
 function validResults(results){return typed(results,types.members.results)&&results.every(x=>x.key.length>0)&&new Set(results.map(x=>x.key)).size===results.length;}
 function template(kind){const holder=document.createElement('div');holder.innerHTML=texts['sources/'+kind+'/accessibility.html'];return holder.querySelector('template').content.cloneNode(true);}
 function watch(s,owner,level,epoch){s.on('onBigStepBegin',e=>{if(e)journal('native.event',{owner,level,epoch,event:JSON.parse(JSON.stringify(e))});});s.on('onError',e=>errors.push({owner,level,event:e}));}
 function current(owner,epoch){return data(roots[owner]).epoch===epoch&&phase(roots[owner])!=='closed';}
 function attach(owner,epoch,level){const v=views[owner];if(!current(owner,epoch))return;
  if(level==='overlay'){const fragment=template('overlay'),surface=fragment.querySelector('[data-part="surface"]');surface.id=owner+'-overlay-'+epoch;surface.style.positionAnchor='--'+owner+'-input';surface.hidden=true;surface.dataset.epoch=String(epoch);v.section.append(fragment);v.surface=surface;v.overlayContent=surface.querySelector('[data-part="content"]');}
  if(level==='scroll-area'){const fragment=template('scroll-area'),viewport=fragment.querySelector('[data-part="viewport"]');viewport.id=owner+'-viewport-'+epoch;v.overlayContent.append(fragment);v.viewport=viewport;v.scrollContent=viewport.querySelector('[data-part="content"]');const list=v.listTemplate.cloneNode(false);list.id=owner+'-list-'+epoch;list.setAttribute('aria-labelledby',owner+'-label');v.scrollContent.append(list);v.list=list;}
 }
 function detach(owner){const v=views[owner];v.input.removeAttribute('aria-activedescendant');v.input.removeAttribute('aria-controls');if(v.surface)v.surface.remove();v.surface=null;v.viewport=null;v.list=null;}
 function render(owner){const s=roots[owner],d=data(s),p=phase(s),v=views[owner];v.section.dataset.phase=p;v.section.dataset.epoch=d.epoch;v.input.value=d.query;
  const previousPhase=v.lastPhase;v.lastPhase=p;const open=['loading','ready','empty','error'].includes(p);v.input.setAttribute('aria-expanded',String(open));v.input.setAttribute('aria-busy',String(p==='loading'));
  if(p==='closed'){detach(owner);if(d.fault)v.status.textContent='Suche fehlgeschlagen.';else if(previousPhase!=='closed')v.status.textContent='';return;}
  if(!v.surface||!v.list)return;v.surface.hidden=!open;v.input.setAttribute('aria-controls',v.list.id);
  if(p==='ready'){
   const signature=JSON.stringify(d.results);if(v.list.dataset.rows!==signature){v.input.removeAttribute('aria-activedescendant');v.list.replaceChildren();for(const row of d.results){const li=v.optionTemplate.cloneNode(false);li.id=owner+'-option-'+d.epoch+'-'+encodeURIComponent(row.key);li.textContent=row.label;li.dataset.key=row.key;li.setAttribute('aria-disabled',String(!!row.disabled));v.list.append(li);}v.list.dataset.rows=signature;}
   for(const li of v.list.children)li.setAttribute('aria-selected',String(li.dataset.key===d.activeKey));const active=[...v.list.children].find(n=>n.dataset.key===d.activeKey);if(active)v.input.setAttribute('aria-activedescendant',active.id);else v.input.removeAttribute('aria-activedescendant');v.status.textContent=d.results.length+' Ergebnisse.';
  }else{v.input.removeAttribute('aria-activedescendant');v.list.replaceChildren();delete v.list.dataset.rows;v.status.textContent=p==='loading'?'Ergebnisse werden geladen.':p==='empty'?'Keine Ergebnisse.':p==='error'?'Suche fehlgeschlagen.':'';}
 }
 const invokers={};
 async function measure(actor,event){await new Promise(requestAnimationFrame);const {owner,epoch}=actor,v=views[owner];if(!current(owner,epoch)||!v.viewport||phase(roots[owner])!=='ready')return;const node=[...v.list.children].find(n=>n.dataset.key===event.data.key);if(!node)return;
  const vp=v.viewport.getBoundingClientRect(),box=node.getBoundingClientRect();if(box.top<vp.top)v.viewport.scrollTop-=vp.top-box.top;else if(box.bottom>vp.bottom)v.viewport.scrollTop+=box.bottom-vp.bottom;
  const after=node.getBoundingClientRect(),bounds=v.viewport.getBoundingClientRect(),visible=after.top>=bounds.top-.5&&after.bottom<=bounds.bottom+.5;
  journal('host.measure',{owner,epoch,key:event.data.key,offset:v.viewport.scrollTop,visible,viewport:{top:bounds.top,bottom:bounds.bottom,height:bounds.height},option:{top:after.top,bottom:after.bottom}});
  actor.session.gen({name:'MEASURED',data:{key:event.data.key,requestId:event.data.requestId,visible,offset:v.viewport.scrollTop}});
 }
 function invoke(parent,obj,_inherited,cb){const url=new URL(obj.src,obj.docUrl),file=url.pathname.slice(1),owner=obj.params.owner,epoch=obj.params.epoch,level=file.includes('/overlay/')?'overlay':'scroll-area';
  if(!['sources/overlay/behavior.scxml','sources/scroll-area/behavior.scxml'].includes(file)){cb(Error('Unsupported local source'));return;}
  (async()=>{const gate=gates.find(x=>!x.used&&x.owner===owner&&x.level===level);if(gate){gate.used=true;journal('test.gate',{owner,epoch,level});if(gate.hold)await new Promise(r=>gate.release=r);}
   let f,relay=false;try{f=await factory(file,gate?.invalid?'<scxml':undefined);}catch(e){diagnostics.push({rule:'init.failed',owner,epoch,level,error:String(e)});f=await factory('sources/error-relay.scxml');relay=true;}
   const session=new core.Statechart(f,{parentSession:parent,invokeid:obj.id,params:{...obj.params,...(relay?{fault:'Initialisierung fehlgeschlagen.'}:{})},invokers});const actor={owner,epoch,level,nativeId:obj.id,parentLevel:parent===roots[owner]?'autocomplete':'overlay',relay,session};actors.push(actor);watch(session,owner,level,epoch);cb(null,session);
   setTimeout(()=>{if(parent.isFinal()||data(parent).epoch!==epoch||!current(owner,epoch)){session.cancel();journal('child.late.cancel',{owner,epoch,level,relay});return;}
    if(!relay)attach(owner,epoch,level);
    if(level==='scroll-area'&&!relay)session.on('onBigStepEnd',e=>{if(e?.name==='REVEAL')measure(actor,e).catch(err=>errors.push({message:String(err)}));});
    session.start();render(owner);journal('child.start',{owner,epoch,level,relay,nativeId:obj.id});
   },0);
  })().catch(e=>{errors.push({message:String(e)});cb(e);});
 }
 for(const type of ['scxml','http://www.w3.org/TR/scxml/','http://www.w3.org/TR/scxml'])invokers[type]=invoke;
 const defaultRows=owner=>Array.from({length:7},(_,i)=>({key:owner+'-'+(i+1),label:'Ergebnis '+owner+' '+(i+1),...(i===2?{disabled:true}:{})}));
 function deliver(request,results,message){const r=requests.find(r=>r.id===request);if(!r)throw Error('Unknown request');let event;if(message)event={name:'FAILURE',data:{...r,message}};else if(!validResults(results)){diagnostics.push({rule:'provider.type',owner:r.owner,id:r.id});event={name:'FAILURE',data:{...r,message:'Ungültige Ergebnisdaten.'}};}else event={name:'DATA',data:{...r,results}};roots[r.owner].gen(event);journal('provider.deliver',{id:r.id,owner:r.owner,epoch:r.epoch,seq:r.seq,event:event.name});}
 for(const owner of ['A','B']){
  const section=document.createElement('section');section.className='search';section.dataset.owner=owner;section.innerHTML='<h2>Suche '+owner+'</h2>';const f=template('autocomplete'),input=f.querySelector('[data-part="input"]'),label=f.querySelector('label'),status=f.querySelector('[data-part="status"]'),list=f.querySelector('[data-part="list"]'),option=f.querySelector('[data-part="option"]');label.id=owner+'-label';label.textContent='Suche '+owner;label.htmlFor=owner+'-input';input.id=owner+'-input';input.setAttribute('aria-labelledby',label.id);input.setAttribute('aria-autocomplete','list');input.style.anchorName='--'+owner+'-input';status.id=owner+'-status';list.remove();section.append(f);document.querySelector('main').append(section);views[owner]={section,input,status,listTemplate:list,optionTemplate:option,surface:null,viewport:null,list:null};
  section.addEventListener('value-change',e=>events[owner].push({name:e.type,detail:e.detail,bubbles:e.bubbles,isTrusted:e.isTrusted,focus:document.activeElement.id}));
  const parentSource='<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" initial="listening"><state id="listening"/></scxml>';
  const parent=parents[owner]=new core.Statechart(await prepare(await compile(location.origin+'/host-parent.scxml',parentSource)));parent.on('onBigStepBegin',e=>{
   if(!e)return;if(e.invokeid!==owner){diagnostics.push({rule:'root.route',owner,event:e.name});return;}
   if(e.name==='provider.request'){const r={...e.data,id:owner+':'+e.data.epoch+':'+e.data.seq};requests.push(r);journal('provider.request',r);if(mode==='auto')deliver(r.id,defaultRows(owner));}
   if(e.name==='value-change'){const payload=types.events['value-change'].payload;if(!typed(e.data,payload)){diagnostics.push({rule:'public.type',owner});return;}const d=data(roots[owner]);views[owner].section.dispatchEvent(new CustomEvent('value-change',{detail:e.data,bubbles:true}));views[owner].status.textContent='Ausgewählt: '+d.query+'.';journal('public.event',{owner,name:e.name,detail:e.data});}
  });parent.start();const root=roots[owner]=new core.Statechart(await factory('sources/autocomplete/behavior.scxml'),{params:{owner},parentSession:parent,invokeid:owner,invokers});watch(root,owner,'autocomplete',0);root.on('onBigStepEnd',()=>render(owner));root.start();
  input.addEventListener('input',e=>{journal('dom.input',{owner,isTrusted:e.isTrusted,composing:e.isComposing||false});root.gen({name:'INPUT',data:{query:input.value}});});
  input.addEventListener('keydown',e=>{journal('dom.key',{owner,key:e.key,isTrusted:e.isTrusted,isComposing:e.isComposing});if(['ArrowDown','ArrowUp'].includes(e.key)){if(!e.isComposing&&!data(root).composing)e.preventDefault();root.gen({name:'NAV',data:{direction:e.key==='ArrowDown'?1:-1}});}if(e.key==='Enter'){if(!e.isComposing&&!data(root).composing)e.preventDefault();root.gen('ENTER');}if(e.key==='Escape')root.gen('CLOSE');});
  input.addEventListener('blur',()=>root.gen('BLUR'));input.addEventListener('compositionstart',()=>root.gen('COMPOSITION_START'));input.addEventListener('compositionend',()=>root.gen('COMPOSITION_END'));
 }
 function snapshot(){const output={focus:document.activeElement.id,events:JSON.parse(JSON.stringify(events)),requests:requests.map(r=>({...r})),diagnostics:JSON.parse(JSON.stringify(diagnostics)),errors:JSON.parse(JSON.stringify(errors)),actors:actors.map(a=>({owner:a.owner,epoch:a.epoch,level:a.level,nativeId:a.nativeId,relay:a.relay,final:a.session.isFinal(),configuration:a.session.getConfiguration(),data:data(a.session)}))};for(const owner of ['A','B']){const v=views[owner],d=data(roots[owner]);output[owner]={phase:phase(roots[owner]),data:JSON.parse(JSON.stringify(d)),expanded:v.input.getAttribute('aria-expanded'),busy:v.input.getAttribute('aria-busy'),activeDescendant:v.input.getAttribute('aria-activedescendant'),controls:v.input.getAttribute('aria-controls'),inputValue:v.input.value,status:v.status.textContent,viewport:v.viewport?{scrollTop:v.viewport.scrollTop,clientHeight:v.viewport.clientHeight,scrollHeight:v.viewport.scrollHeight}:null,options:v.list?[...v.list.children].map(n=>({id:n.id,key:n.dataset.key,selected:n.getAttribute('aria-selected'),disabled:n.getAttribute('aria-disabled')})):[]};}return output;}
 window.research={snapshot,log,manifest,events,roots,actors,requests,diagnostics,errors,
  providerMode:value=>{mode=value;},deliver,
  program(owner,value){if(typeof value!=='string'||!data(roots[owner]).results.some(r=>r.key===value)){diagnostics.push({rule:'program.value',owner});return false;}roots[owner].gen({name:'SET_VALUE',data:{value}});return true;},
  holdNext(owner,level,invalid=false){gates.push({owner,level,hold:true,invalid});return gates.length-1;},release:index=>gates[index].release(),failNext(owner,level){gates.push({owner,level,invalid:true});},
  capture:async(name,payload)=>{const body={name,payload,snapshot:snapshot(),journal:log.slice(),environment:{userAgent:navigator.userAgent,platform:navigator.platform,language:navigator.language},sourceRevision:manifest.revision};const response=await fetch('/capture',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!response.ok)throw Error('Capture rejected');return {name,saved:true};}
 };
 document.body.dataset.ready='true';document.querySelector('#state').textContent='Forschungs-Host bereit';journal('host.ready',{revision:manifest.revision});
})().catch(e=>{document.body.dataset.failed='true';document.querySelector('#state').textContent=String(e);console.error(e);});
