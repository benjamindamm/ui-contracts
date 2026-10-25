async function runHostProbe({source,html,css,profile,interfaceProfile,expectations}) {
 if(location.href!=='about:blank')throw Error('Dedicated original-runtime research fixture page required');
 document.documentElement.lang='de';document.title='UI Contracts – originale SCXML-Laufzeitbindung';document.body.innerHTML=html;
 const style=document.createElement('style');style.textContent=css;document.head.append(style);
 const api=window.scion.scxml,core=window.scion.core;
 const compile=(text,id)=>new Promise((resolve,reject)=>{try{api.documentStringToModel('file:///ui-contracts/'+id+'.scxml',text,(err,m)=>err?reject(err):resolve(m));}catch(e){reject(e)}});
 const prepare=m=>new Promise((resolve,reject)=>m.prepare((err,f)=>err?reject(err):resolve(f)));
 const originalCompiled=await compile(source,'autocomplete');
 const parentSource='<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" initial="listening"><state id="listening"><transition event="value-change"/></state></scxml>';
 const parentsCompiled=await compile(parentSource,'host-parent');
 const children={},parents={},views={},publicEvents={A:[],B:[]},rawEvents={A:[],B:[]},errors=[],diagnostics=[],transitions=[];
 for(const id of ['A','B']) {
  const binding=profile.instances[id],input=document.getElementById(binding.parts.input),popup=document.getElementById(binding.parts.popup),root=input.parentElement;
  root.dataset.researchInstance=id;views[id]={input,popup,root};
  root.addEventListener(interfaceProfile.publicEvent,event=>publicEvents[id].push({name:event.type,detail:event.detail,targetInstance:event.target.dataset.researchInstance,bubbles:event.bubbles}));
  const parent=parents[id]=new core.Statechart(await prepare(parentsCompiled));
  parent.on('onBigStepBegin',event=>{
   if(!event)return;rawEvents[id].push({name:event.name,data:event.data,invokeid:event.invokeid});
   if(event.invokeid!==id){diagnostics.push({rule:'instance-route',id});return;}
   if(event.name!==interfaceProfile.publicEvent){diagnostics.push({rule:'event-not-declared',id});return;}
   for(const [key,p] of Object.entries(interfaceProfile.properties))if(p.type!=='StringKeyword'||typeof event.data?.[key]!=='string'){diagnostics.push({rule:'payload-type',id});return;}
   input.value=event.data.value;
   root.dispatchEvent(new CustomEvent(event.name,{detail:event.data,bubbles:true}));
  });parent.start();
  // Crucial: the original preparation API creates a fresh execution context for each actor.
  const child=children[id]=new core.Statechart(await prepare(originalCompiled),{parentSession:parent,invokeid:id});
  child.on('onError',e=>errors.push({id,error:String(e)}));
  child.on('onEntry',state=>{transitions.push({id,entered:state});const view=profile.stateView[state];if(!view)return;input.setAttribute('aria-expanded',String(view.expanded));popup.hidden=!view.popupVisible;if(view.popupVisible)input.setAttribute('aria-activedescendant',binding.parts.option);else input.removeAttribute('aria-activedescendant');});
  input.addEventListener('focus',()=>child.gen('OPEN'));
  input.addEventListener('keydown',event=>{if(event.key==='Escape')child.gen('CLOSE');if(event.key==='Enter')child.gen('COMMIT');});
  child.start();
 }
 const snapshot=()=>({A:children.A.getConfiguration()[0],B:children.B.getConfiguration()[0],expandedA:views.A.input.getAttribute('aria-expanded'),expandedB:views.B.input.getAttribute('aria-expanded'),hiddenA:views.A.popup.hidden,hiddenB:views.B.popup.hidden,focus:document.activeElement.id,publicAEvents:publicEvents.A.length,publicBEvents:publicEvents.B.length,value:publicEvents.A[0]?.detail.value});
 const results=[];function record(id){const e=expectations.cases.find(c=>c.id===id).expected;const observed=snapshot();results.push({id,expected:e,observed,expectationMet:Object.entries(e).every(([k,v])=>observed[k]===v)});}
 record('host-initial');views.A.input.focus();record('host-focus-a');views.A.input.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}));record('host-escape-a');
 views.A.input.blur();views.A.input.focus();
 const committed=new Promise((resolve,reject)=>{const timeout=setTimeout(()=>reject(Error('Native parent send / public DOM event timeout')),3000);views.A.root.addEventListener(interfaceProfile.publicEvent,()=>{clearTimeout(timeout);resolve();},{once:true});});
 views.A.input.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}));await committed;record('host-commit-a');views.B.input.focus();record('host-focus-b-after-a');
 const output={cases:results,publicEvents,rawEvents,errors,diagnostics,transitions,userAgent:navigator.userAgent,realOriginalScxmlExecution:true,originalSourceUnchanged:true,preparePerInstance:true,additionalHostCode:true,keyboardEventOrigin:'synthetic KeyboardEvent; no trusted physical key or screenreader test',eventTarget:'explicit research section container, not implemented CEM custom element'};
 for(const child of Object.values(children))child.cancel();for(const parent of Object.values(parents))parent.cancel();
 return output;
}
