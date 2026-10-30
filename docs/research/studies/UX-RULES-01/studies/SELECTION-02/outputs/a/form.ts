/** Native adapters derived from the Input and Select SCXML contracts. */
type Choice = {key:string;label:string;disabled?:boolean};
class InputAdapter {
  value: string;
  constructor(readonly control:HTMLInputElement) {
    this.value=control.value;
    control.addEventListener('input',()=>{
      if(control.disabled || control.readOnly){control.value=this.value;return;}
      if(this.value===control.value)return;
      this.value=control.value;
      control.dispatchEvent(new CustomEvent('value-change',{bubbles:true,detail:{value:this.value}}));
    });
  }
  setValue(value:unknown){if(typeof value==='string')this.control.value=this.value=value;}
  setEnabled(enabled:unknown){if(typeof enabled==='boolean')this.control.disabled=!enabled;}
  setReadOnly(readOnly:unknown){if(typeof readOnly==='boolean')this.control.readOnly=readOnly;}
}
class SelectAdapter {
  value:string|undefined;
  options:Choice[]=[];
  constructor(readonly control:HTMLSelectElement){
    this.setOptions(Array.from(control.options).filter(o=>o.value!=='').map(o=>({key:o.value,label:o.text,disabled:o.disabled})));
    control.addEventListener('change',()=>{
      const key=control.value;
      if(control.disabled || (!this.options.some(o=>o.key===key&&!o.disabled) && (key!==''||control.required))){control.value=this.value??'';return;}
      const value=key||undefined;
      if(value===this.value)return;
      this.value=value;this.emit('user');
    });
  }
  private emit(reason:'user'|'options-change'){this.control.dispatchEvent(new CustomEvent('value-change',{bubbles:true,detail:{value:this.value,reason}}));}
  setOptions(options:unknown){
    if(!Array.isArray(options)||!options.every((o,i,a)=>o&&typeof o.key==='string'&&o.key.trim().length>0&&typeof o.label==='string'&&o.label.trim().length>0&&(o.disabled===undefined||typeof o.disabled==='boolean')&&a.every((p,j)=>i===j||p.key!==o.key)))return;
    this.options=options.map(o=>({...o}));
    this.control.replaceChildren(new Option('Bitte wählen',''),...this.options.map(o=>{const e=new Option(o.label,o.key);e.disabled=!!o.disabled;return e;}));
    if(this.value!==undefined&&!this.options.some(o=>o.key===this.value&&!o.disabled)){this.value=undefined;this.emit('options-change');}
    this.control.value=this.value??'';
  }
  setValue(value:unknown){if(value===undefined||this.options.some(o=>o.key===value&&!o.disabled)){this.value=value as string|undefined;this.control.value=this.value??'';}}
  setRequired(required:unknown){if(typeof required==='boolean')this.control.required=required;}
  setEnabled(enabled:unknown){if(typeof enabled==='boolean')this.control.disabled=!enabled;}
}
const form=document.querySelector<HTMLFormElement>('#personal-form')!;
const statusNode=document.querySelector<HTMLElement>('#submission-status')!;
const inputs=Array.from(form.querySelectorAll<HTMLInputElement>('input')).map(e=>new InputAdapter(e));
const country=new SelectAdapter(document.querySelector<HTMLSelectElement>('#country-control')!);
const controls=[...inputs.map(i=>i.control),country.control];
function error(control:HTMLInputElement|HTMLSelectElement,message:string){
  const root=control.parentElement!;const node=root.querySelector<HTMLElement>('[data-part="error"]')!;
  node.textContent=message;node.hidden=!message;
  if(message)control.setAttribute('aria-invalid','true');else control.removeAttribute('aria-invalid');
  const ids=[...root.querySelectorAll<HTMLElement>('[data-part="hint"],[data-part="error"]')].filter(n=>!n.hidden&&n.textContent?.trim()).map(n=>n.id);
  if(ids.length)control.setAttribute('aria-describedby',ids.join(' '));else control.removeAttribute('aria-describedby');
}
form.addEventListener('value-change',event=>{
  statusNode.textContent='';
  const target=event.target;
  if(target instanceof HTMLInputElement||target instanceof HTMLSelectElement)error(target,'');
});
form.addEventListener('submit',event=>{
  event.preventDefault();statusNode.textContent='';let first:HTMLInputElement|HTMLSelectElement|undefined;
  for(const control of controls){
    let message='';
    if(!control.value.trim())message=control===country.control?'Bitte ein Land auswählen.':'Bitte dieses Feld ausfüllen.';
    else if(control instanceof HTMLInputElement&&control.validity.typeMismatch)message='Bitte eine gültige E-Mail-Adresse eingeben.';
    else if(control===country.control&&!country.options.some(o=>o.key===control.value&&!o.disabled))message='Bitte ein vorgegebenes Land auswählen.';
    error(control,message);if(message&&!first)first=control;
  }
  if(first){first.focus();return;}
  // No persistence or external request. Phone is retained as a string, including leading zeros.
  const localData={givenName:inputs[0].value,familyName:inputs[1].value,email:inputs[2].value,nationalNumber:inputs[3].value,countryKey:country.value};
  statusNode.textContent=typeof localData.nationalNumber==='string'?'Alle Pflichtangaben sind lokal geprüft. Es wurden keine Daten versendet.':'';
});
