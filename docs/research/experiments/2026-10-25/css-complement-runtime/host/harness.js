'use strict';
(async()=>{
 const paths=['interface.json','behavior.scxml','visual.css','accessibility.html'],sources={};for(const name of paths){const r=await fetch('sources/'+name);if(!r.ok)throw Error('source-load '+name);sources[name]=await r.text();}
 const profile=await(await fetch('profile.json')).json(),signature=await(await fetch('interface-binding.json')).json(),cases=await(await fetch('cases.json')).json();
 const sha=async text=>[...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(text)))].map(x=>x.toString(16).padStart(2,'0')).join('');
 for(const x of Object.values(profile.sources))if(await sha(sources[x.file])!==x.sha256)throw Error('source-hash '+x.file);
 if(await sha(sources['interface.json'])!==signature.sourceSha256)throw Error('signature-source-hash');
 const root=document.getElementById('research-root'),style=document.createElement('style');style.textContent=sources['visual.css'];document.head.append(style);
 const sourceDoc=new DOMParser().parseFromString(sources['accessibility.html'],'text/html'),originalLabels=Object.fromEntries(['a','b'].map(i=>[i,sourceDoc.getElementById('label-'+i).textContent]));
 const api=window.scion.scxml,core=window.scion.core,compile=(text,id)=>new Promise((resolve,reject)=>api.documentStringToModel('http://127.0.0.1/research/'+id+'.scxml',text,(err,m)=>err?reject(err):resolve(m))),prepare=m=>new Promise((resolve,reject)=>m.prepare((err,f)=>err?reject(err):resolve(f))),compiled=await compile(sources['behavior.scxml'],'child'),parentCompiled=await compile('<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" initial="listening"><state id="listening"><transition event="value-change"/></state></scxml>','parent');
 function fail(name){throw Error(name)}
 let activeRun=null;
 async function create({foreignParent=false}={}){
  if(activeRun)activeRun.destroy();root.innerHTML=sources['accessibility.html'];const children={},parents={},views={},raw=[],publicEvents=[],diagnostics=[],trace=[],waiters=[];
  const keyMap=structuredClone(profile.keys);
  for(const id of ['A','B']){const b=profile.instances[id],i=id.toLowerCase(),view=views[id]=Object.fromEntries(Object.entries(b).map(([k,v])=>[k,Array.isArray(v)?v.map(x=>document.getElementById(x)):document.getElementById(v)]));view.root.dataset.machineState='closed';
   view.root.addEventListener(signature.publicEvent,event=>publicEvents.push({instance:id,name:event.type,detail:structuredClone(event.detail)}));
   const parent=parents[id]=new core.Statechart(await prepare(parentCompiled));parent.on('onBigStepBegin',event=>{if(!event||event.name!==signature.publicEvent)return;const item={receiver:id,name:event.name,data:structuredClone(event.data),invokeid:event.invokeid};raw.push(item);let error=null;
    if(event.invokeid!==id)error='public-instance-route';
    else for(const [name,p]of Object.entries(signature.payload))if(p.type!=='StringKeyword'||typeof event.data?.[name]!=='string'){error='public-payload-type';break;}
    if(error)diagnostics.push(error);else{view.input.value=event.data.value;view.root.dispatchEvent(new CustomEvent(event.name,{detail:structuredClone(event.data),bubbles:true}));view.status.textContent=view.status.dataset.messagePrefix+event.data.value;}
    for(const resolve of waiters.splice(0))resolve({raw:item,error});
   });parent.start();
  }
  for(const id of ['A','B']){const view=views[id],child=children[id]=new core.Statechart(await prepare(compiled),{invokeid:id,parentSession:parents[foreignParent&&id==='A'?'B':id]});child.on('onError',e=>diagnostics.push('original-runtime-error '+String(e)));child.on('onEntry',state=>{trace.push({instance:id,state});if(profile.stateView[state]){view.root.dataset.machineState=state;view.input.setAttribute('aria-expanded',String(profile.stateView[state].expanded));if(state!=='open')view.input.removeAttribute('aria-activedescendant');}});child.start();
   view.input.addEventListener('input',()=>send(id,{name:'QUERY',data:{query:view.input.value}}));view.input.addEventListener('keydown',event=>{if(!Object.hasOwn(keyMap,event.key))return;event.preventDefault();const action=keyMap[event.key];if(action==='OPEN_OR_NEXT'){const activeId=view.input.getAttribute('aria-activedescendant'),index=view.options.findIndex(o=>o.id===activeId);if(state(id)!=='open')send(id,{name:'OPEN',data:{query:view.input.value}});if(state(id)==='open')activate(id,Math.min(index+1,view.options.length-1));}else if(action==='CLOSE')send(id,'CLOSE');else if(action==='COMMIT'&&state(id)==='open'){const option=document.getElementById(view.input.getAttribute('aria-activedescendant'));send(id,{name:'COMMIT',data:{value:option?.textContent??view.options[0].textContent}});}});
  }
  function state(id){return children[id].getConfiguration()[0]}
  function send(id,event){children[id].gen(event)}
  function key(id,key){views[id].input.dispatchEvent(new KeyboardEvent('keydown',{key,bubbles:true,cancelable:true}))}
  function activate(id,index){const v=views[id];v.input.setAttribute('aria-activedescendant',v.options[index].id);v.options.forEach((o,j)=>o.setAttribute('aria-selected',String(index===j)));v.options[index].scrollIntoView({block:'nearest',inline:'nearest'});}
  function property(id,name,value){if(typeof value!==signature.properties[name])fail('public-property-type');if(name==='query')send(id,{name:'QUERY',data:{query:value}});else if(name==='enabled')send(id,{name:'SET_ENABLED',data:{enabled:value}});}
  function height(id,value,unit='px',metadata=signature){if(metadata.properties.maxHeight!=='number')fail('public-type-layout-binding');if(typeof value!=='number'||!Number.isFinite(value)||value<=0)fail('public-property-type');if(unit!==profile.layoutInput.unit)fail('geometry-unit');views[id].popup.style.setProperty(profile.layoutInput.cssVariable,value+unit);}
  function relation(id){const v=views[id],b=profile.instances[id];if(v.input.getAttribute('aria-controls')!==b.list||!v.popup.contains(document.getElementById(v.input.getAttribute('aria-controls'))))fail('accessible-instance-relation');if(v.input.getAttribute('aria-labelledby')!==b.label||v.label.textContent!==originalLabels[id.toLowerCase()])fail('accessible-name-source-conflict');if(v.input.getAttribute('role')!=='combobox'||v.list.getAttribute('role')!=='listbox')fail('accessible-role-source-conflict');return{inputRole:v.input.getAttribute('role'),name:v.label.textContent,listName:v.list.getAttribute('aria-label'),controls:v.input.getAttribute('aria-controls')};}
  function live(id){const s=views[id].status;if(s.getAttribute('role')!=='status'||s.getAttribute('aria-live')!=='polite'||s.getAttribute('aria-atomic')!=='true')fail('live-region-source-conflict');}
  function pattern(){for(const [key,expected]of Object.entries(profile.keys))if(keyMap[key]!==expected)fail('pattern-key-route');}
  function scroll(id){const v=views[id],controlled=document.getElementById(v.input.getAttribute('aria-controls'));if(controlled!==v.list||!v.popup.contains(controlled))fail('scroll-instance-target');const active=document.getElementById(v.input.getAttribute('aria-activedescendant'));if(!active||!controlled.contains(active))fail('scroll-instance-target');const a=active.getBoundingClientRect(),b=v.popup.getBoundingClientRect(),activeVisible=a.top>=b.top-0.1&&a.bottom<=b.bottom+0.1;return{scrollTop:v.popup.scrollTop,height:v.popup.clientHeight,scrollHeight:v.popup.scrollHeight,active:active.id,activeVisible,controls:controlled.id,overflow:getComputedStyle(v.popup).overflowY};}
  function waitParent(){return new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('original-parent-timeout')),3000);waiters.push(result=>{clearTimeout(timer);resolve(result)})})}
  async function commit(id,value){const wait=waitParent();send(id,{name:'COMMIT',data:{value:value??views[id].options[0].textContent}});return await wait;}
  const run={views,children,parents,raw,publicEvents,diagnostics,trace,keyMap,state,send,key,activate,property,height,relation,live,pattern,scroll,waitParent,commit,destroy(){for(const c of Object.values(children))c.cancel();for(const p of Object.values(parents))p.cancel();}};activeRun=run;return run;
 }
 const attempt=fn=>{try{return fn()}catch(e){return{error:e.message}}},display=r=>getComputedStyle(r.views.A.popup).display;
 window.complementResearch={sources,profile,signature,async runCase(id){const r=await create({foreignParent:id==='public-event-foreign-parent'}),A=r.views.A,B=r.views.B;let o={};const open=(query='Alpha')=>{A.input.value=query;r.send('A',{name:'OPEN',data:{query}})};
 switch(id){
  case'public-height-number':open();r.height('A',192);o={height:A.popup.clientHeight,scrollHeight:A.popup.scrollHeight,BHeight:Number.parseFloat(getComputedStyle(B.popup).maxHeight)};break;
  case'public-height-wrong-type':o=attempt(()=>r.height('A','192'));break;
  case'public-height-wrong-unit':o=attempt(()=>r.height('A',192,'rem'));break;
  case'public-property-metadata-conflict':{const sig=structuredClone(signature);sig.properties.maxHeight='string';o=attempt(()=>r.height('A',192,'px',sig));break;}
  case'public-event-and-css-state':open();await r.commit('A');o={publicEvents:r.publicEvents.filter(e=>e.instance==='A').length,...r.publicEvents[0]?.detail,AState:r.state('A'),ADisplay:display(r),BEvents:r.publicEvents.filter(e=>e.instance==='B').length};break;
  case'public-payload-type-conflict':open();r.send('A',{name:'QUERY',data:{query:42}});await r.commit('A');o={error:r.diagnostics[0],publicEvents:r.publicEvents.length,rawQueryType:typeof r.raw[0]?.data.query};break;
  case'public-event-foreign-parent':open();await r.commit('A');o={error:r.diagnostics[0],BEvents:r.publicEvents.filter(e=>e.instance==='B').length};break;
  case'states-to-css-display':{const sequence=[r.state('A')+':'+display(r)];open();sequence.push(r.state('A')+':'+display(r));r.send('A','CLOSE');sequence.push(r.state('A')+':'+display(r));o={sequence,BState:r.state('B')};break;}
  case'original-guard-false-then-true':r.property('A','enabled',false);open();o.blocked=r.state('A')+':'+display(r);r.property('A','enabled',true);open();o.allowed=r.state('A')+':'+display(r);break;
  case'original-event-context-data':open('Alpha A');r.property('A','query','Alpha A');await r.commit('A','Alpha A 2');o={...r.publicEvents[0]?.detail,publicEvents:r.publicEvents.length};break;
  case'input-query-wrong-type':o=attempt(()=>r.property('A','query',42));break;
  case'keyboard-actions-own-context':A.input.focus();r.key('A','ArrowDown');r.key('A','ArrowDown');o={AState:r.state('A'),BState:r.state('B'),focus:document.activeElement.id,active:A.input.getAttribute('aria-activedescendant')};break;
  case'keyboard-other-instance':B.input.focus();r.key('B','ArrowDown');o={AState:r.state('A'),BState:r.state('B'),focus:document.activeElement.id};break;
  case'accessible-role-name-relations':o=r.relation('A');break;
  case'accessible-name-conflict':A.label.textContent='Wrong name';o=attempt(()=>r.relation('A'));break;
  case'accessible-foreign-controls':A.input.setAttribute('aria-controls','list-b');o=attempt(()=>r.relation('A'));break;
  case'pattern-escape-focus':A.input.focus();r.key('A','ArrowDown');r.key('A','Escape');o={AState:r.state('A'),expanded:A.input.getAttribute('aria-expanded'),focus:document.activeElement.id,active:A.input.getAttribute('aria-activedescendant')};break;
  case'pattern-commit-selection':{A.input.focus();r.key('A','ArrowDown');r.key('A','ArrowDown');const wait=r.waitParent();r.key('A','Enter');await wait;o={value:A.input.value,focus:document.activeElement.id,expanded:A.input.getAttribute('aria-expanded')};break;}
  case'pattern-key-route-conflict':r.keyMap.Enter='CLOSE';o=attempt(()=>r.pattern());break;
  case'accessible-update-from-public-event':r.live('A');open();await r.commit('A');o={status:A.status.textContent,BStatus:B.status.textContent,role:A.status.getAttribute('role'),live:A.status.getAttribute('aria-live')};break;
  case'css-change-without-live-message':r.height('A',192);o={status:A.status.textContent,BStatus:B.status.textContent,publicEvents:r.publicEvents.length};break;
  case'live-region-semantic-conflict':A.status.setAttribute('aria-live','off');o=attempt(()=>r.live('A'));break;
  case'aria-controlled-scrollport':A.input.focus();for(let i=0;i<7;i++)r.key('A','ArrowDown');o=r.scroll('A');break;
  case'aria-scroll-foreign-list':open();r.activate('A',0);A.input.setAttribute('aria-controls','list-b');o=attempt(()=>r.scroll('A'));break;
  case'aria-scroll-clip-conflict':open();A.popup.style.overflow='clip';r.activate('A',6);o=r.scroll('A');if(!o.activeVisible)o.error='active-option-not-visible';break;
  default:throw Error('unknown-case '+id);
 }
 const expected=cases.find(c=>c.id===id);if(!expected)throw Error('missing-expected');return{...expected,observed:o,trace:r.trace,rawOriginalParentEvents:r.raw,publicEvents:r.publicEvents,diagnostics:r.diagnostics,expectationMet:Object.entries(expected.expected).every(([k,v])=>JSON.stringify(o[k])===JSON.stringify(v)),additionalHostCode:true,originalScxmlExecuted:true,syntheticKeyboardOnly:true};},async readLive(){const r=activeRun;return{A:r.state('A'),B:r.state('B'),names:[r.views.A.label.textContent,r.views.B.label.textContent],roles:[r.views.A.input.getAttribute('role'),r.views.B.input.getAttribute('role')]}}};
 document.body.dataset.ready='true';
})().catch(e=>{document.body.dataset.error=String(e);document.getElementById('research-root').textContent=String(e)});
