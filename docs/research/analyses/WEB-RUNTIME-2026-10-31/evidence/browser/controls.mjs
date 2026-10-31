// Deliberately bounded adapters. Native SCXML is authoritative; markup comes from the selected library.
export async function installControls({texts,roles,factory,core}) {
 const machines={},events={},nodes={},errors=[];const data=s=>s.getSnapshot()[3],phase=s=>s.getConfiguration()[0];
 const rows=Array.from({length:30},(_,i)=>({key:'K'+(i+1),label:'Land '+String(i+1).padStart(2,'0'),...(i===1?{disabled:true}:{})}));
 for(const kind of ['Input','Select','SelectWithSearch']){
  const box=document.createElement('section');box.dataset.kind=kind;box.innerHTML='<h2>'+kind+'</h2>';const holder=document.createElement('div');holder.innerHTML=texts['sources/'+roles[kind]+'/accessibility.html'];
  const template=holder.querySelector('template');box.append(template?template.content.cloneNode(true):holder.querySelector('[data-component]'));document.querySelector('#controls-host').append(box);
  for(const n of box.querySelectorAll('[id]')){const old=n.id;n.id=kind+'-'+old;for(const node of box.querySelectorAll('*'))for(const attr of ['for','aria-controls','aria-labelledby'])if(node.hasAttribute(attr))node.setAttribute(attr,node.getAttribute(attr).split(' ').map(v=>v===old?n.id:v).join(' '));}
  const control=box.querySelector('[data-part=control]'),trigger=box.querySelector('[data-part=trigger]'),search=box.querySelector('[data-part=search]'),list=box.querySelector('[data-part=listbox]'),dialog=box.querySelector('[data-part=dialog]'),hidden=box.querySelector('input[type=hidden]');
  if(trigger)trigger.id=kind+'-trigger';
  let rendering=false;
  events[kind]=[];box.addEventListener('value-change',e=>events[kind].push({detail:e.detail,focus:document.activeElement.id}));
  const machine=machines[kind]=new core.Statechart(await factory('sources/'+roles[kind]+'/behavior.scxml'),{parentSession:{gen:e=>{if(e.name==='value-change')box.dispatchEvent(new CustomEvent(e.name,{detail:e.data,bubbles:true}));}}});machine.on('onError',e=>errors.push(String(e)));
  const send=(name,args)=>machine.gen({name,data:args});
  function render(){rendering=true;try{const d=data(machine),open=phase(machine)==='opened';
   if(kind==='Input'){control.value=d.value;control.disabled=!d.enabled;control.readOnly=d.readOnly;return;}
   if(kind==='Select'){const opts=[new Option('Bitte wählen','')].concat(d.options.map(o=>{const n=new Option(o.label,o.key);n.disabled=!!o.disabled;return n;}));control.replaceChildren(...opts);control.value=d.value??'';control.disabled=!d.enabled;control.required=d.required;return;}
   trigger.disabled=!d.enabled;trigger.setAttribute('aria-expanded',String(open));dialog.hidden=!open;trigger.querySelector('span').textContent=d.options.find(o=>o.key===d.value)?.label||'Bitte wählen';hidden.value=d.value??'';search.value=d.query;
   const focusKey=list.contains(document.activeElement)?document.activeElement.dataset.key:null;
   list.replaceChildren(...d.options.filter(o=>d.matches(o,d.query)).map(o=>{const n=document.createElement('li');n.id=kind+'-option-'+o.key;n.dataset.key=o.key;n.role='option';n.tabIndex=-1;n.textContent=o.label;n.setAttribute('aria-selected',String(o.key===d.value));n.setAttribute('aria-disabled',String(!!o.disabled));n.addEventListener('click',()=>{if(!o.disabled){send('USER_SELECT',{value:o.key});trigger.focus();}});return n;}));
   if(focusKey&&open){const n=[...list.children].find(n=>n.dataset.key===focusKey);if(n)n.focus();}
  }finally{rendering=false;}}
  machine.on('onBigStepEnd',render);machine.start();nodes[kind]={box,control,trigger,search,list};
  if(kind==='Input'){control.addEventListener('input',()=>send('USER_INPUT',{value:control.value}));}
  else if(kind==='Select'){control.addEventListener('change',()=>send(control.value?'USER_SELECT':'USER_CLEAR',{value:control.value}));send('SET_OPTIONS',{options:rows.slice(0,3)});}
  else {send('SET_OPTIONS',{options:rows});trigger.addEventListener('click',()=>{send('OPEN');search.focus();});search.addEventListener('input',()=>send('SEARCH',{query:search.value}));
   box.addEventListener('keydown',e=>{if(phase(machine)!=='opened')return;if(e.key==='Escape'){e.preventDefault();send('ESCAPE');trigger.focus();return;}
    if(['ArrowDown','ArrowUp'].includes(e.key)){e.preventDefault();const d=data(machine),visible=d.options.filter(o=>!o.disabled&&d.matches(o,d.query)),idx=visible.findIndex(o=>o.key===d.activeKey),next=visible[Math.max(0,Math.min(visible.length-1,idx+(e.key==='ArrowDown'?1:-1)))];if(next){send('ACTIVE_KEY',{key:next.key});const n=[...list.children].find(n=>n.dataset.key===next.key);n.focus();n.scrollIntoView({block:'nearest'});}}
    if(e.key==='Enter'&&data(machine).activeKey){e.preventDefault();send('USER_SELECT',{value:data(machine).activeKey});trigger.focus();}
   });box.addEventListener('focusout',e=>{if(!rendering&&phase(machine)==='opened'&&!box.contains(e.relatedTarget))send('CLOSE');});
  }
 }
 return {send:(kind,name,args)=>machines[kind].gen({name,data:args}),snapshot:()=>({events:JSON.parse(JSON.stringify(events)),errors,states:Object.fromEntries(Object.entries(machines).map(([k,m])=>{const n=nodes[k],d=data(m);return[k,{phase:phase(m),data:JSON.parse(JSON.stringify(d)),focus:document.activeElement.id,value:n.control?.value??n.box.querySelector('input[type=hidden]')?.value,readOnly:n.control?.readOnly,disabled:(n.control||n.trigger).disabled,expanded:n.trigger?.getAttribute('aria-expanded'),scrollTop:n.list?.scrollTop,options:n.list?[...n.list.children].map(n=>({key:n.dataset.key,selected:n.getAttribute('aria-selected'),disabled:n.getAttribute('aria-disabled')})):[]}];}))})};
}
