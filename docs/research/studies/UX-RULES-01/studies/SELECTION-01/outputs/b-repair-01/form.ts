(()=>{
type Country = {key:string; label:string; country:string; dialCode:string};
const options: Country[] = [{"key": "CH", "country": "Schweiz", "dialCode": "+41", "label": "Schweiz (+41)"}, {"key": "DE", "country": "Deutschland", "dialCode": "+49", "label": "Deutschland (+49)"}, {"key": "FR", "country": "Frankreich", "dialCode": "+33", "label": "Frankreich (+33)"}, {"key": "CA", "country": "Kanada", "dialCode": "+1", "label": "Kanada (+1)"}, {"key": "US", "country": "Vereinigte Staaten", "dialCode": "+1", "label": "Vereinigte Staaten (+1)"}, {"key": "GR", "country": "Griechenland", "dialCode": "+30", "label": "Griechenland (+30)"}, {"key": "NL", "country": "Niederlande", "dialCode": "+31", "label": "Niederlande (+31)"}, {"key": "BE", "country": "Belgien", "dialCode": "+32", "label": "Belgien (+32)"}, {"key": "ES", "country": "Spanien", "dialCode": "+34", "label": "Spanien (+34)"}, {"key": "HU", "country": "Ungarn", "dialCode": "+36", "label": "Ungarn (+36)"}, {"key": "IT", "country": "Italien", "dialCode": "+39", "label": "Italien (+39)"}, {"key": "AT", "country": "Österreich", "dialCode": "+43", "label": "Österreich (+43)"}, {"key": "GB", "country": "Vereinigtes Königreich", "dialCode": "+44", "label": "Vereinigtes Königreich (+44)"}, {"key": "DK", "country": "Dänemark", "dialCode": "+45", "label": "Dänemark (+45)"}, {"key": "SE", "country": "Schweden", "dialCode": "+46", "label": "Schweden (+46)"}, {"key": "NO", "country": "Norwegen", "dialCode": "+47", "label": "Norwegen (+47)"}, {"key": "PL", "country": "Polen", "dialCode": "+48", "label": "Polen (+48)"}, {"key": "AU", "country": "Australien", "dialCode": "+61", "label": "Australien (+61)"}, {"key": "NZ", "country": "Neuseeland", "dialCode": "+64", "label": "Neuseeland (+64)"}, {"key": "JP", "country": "Japan", "dialCode": "+81", "label": "Japan (+81)"}, {"key": "TR", "country": "Türkei", "dialCode": "+90", "label": "Türkei (+90)"}, {"key": "IN", "country": "Indien", "dialCode": "+91", "label": "Indien (+91)"}, {"key": "PT", "country": "Portugal", "dialCode": "+351", "label": "Portugal (+351)"}, {"key": "LU", "country": "Luxemburg", "dialCode": "+352", "label": "Luxemburg (+352)"}, {"key": "IE", "country": "Irland", "dialCode": "+353", "label": "Irland (+353)"}, {"key": "FI", "country": "Finnland", "dialCode": "+358", "label": "Finnland (+358)"}, {"key": "HR", "country": "Kroatien", "dialCode": "+385", "label": "Kroatien (+385)"}, {"key": "SI", "country": "Slowenien", "dialCode": "+386", "label": "Slowenien (+386)"}, {"key": "CZ", "country": "Tschechien", "dialCode": "+420", "label": "Tschechien (+420)"}, {"key": "SK", "country": "Slowakei", "dialCode": "+421", "label": "Slowakei (+421)"}];
const query = document.getElementById('country-query') as HTMLInputElement;
const value = document.getElementById('country-value') as HTMLInputElement;
const list = document.getElementById('country-list')!;
const popup = document.getElementById('country-popup')!;
const component = document.getElementById('country-component')!;
const status = document.getElementById('country-status')!;
const form = document.getElementById('personal-form') as HTMLFormElement;
const formStatus = document.getElementById('form-status')!;
function clearSuccess() { formStatus.textContent=''; }
for (const control of form.querySelectorAll<HTMLInputElement>('[data-component="Input"] input')) {
  let previousValue = control.value;
  control.addEventListener('input',()=>{
    if(control.disabled || control.readOnly || control.value===previousValue) return;
    previousValue=control.value;
    clearSuccess();
    control.dispatchEvent(new CustomEvent('value-change',{detail:{value:control.value},bubbles:true}));
  });
}
let previousQuery = query.value;
function recordQueryChange() {
  if(query.value!==previousQuery) { previousQuery=query.value; clearSuccess(); }
}
let committed: string | undefined;
let results: Country[] = [];
let activeKey: string | undefined;
let open = false;
let composing = false;
const fold = (s:string) => s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase('de');
function provider(text:string): Country[] { const term=fold(text.trim()); return options.filter(item => fold(item.label+' '+item.key).includes(term)); }
function close() { open=false; activeKey=undefined; popup.hidden=true; popup.parentElement!.style.paddingBottom='0'; component.dataset.state='closed'; query.setAttribute('aria-expanded','false'); query.removeAttribute('aria-activedescendant'); }
function render() {
  list.replaceChildren();
  for (const item of results) {
    const row=document.createElement('li'); row.id='country-option-'+item.key; row.dataset.part='option'; row.dataset.key=item.key;
    row.setAttribute('role','option'); row.setAttribute('aria-selected',String(item.key===activeKey)); row.textContent=item.label;
    row.addEventListener('pointerdown', e=>e.preventDefault());
    row.addEventListener('click',()=>commit(item.key)); list.append(row);
  }
  popup.hidden=false; popup.parentElement!.style.paddingBottom=`${Math.min(results.length*32,160)+8}px`; open=true; query.setAttribute('aria-expanded','true'); query.setAttribute('aria-busy','false');
  component.dataset.state=results.length?'ready':'empty';
  status.textContent=results.length?`${results.length} Länder verfügbar.`:'Keine Länder gefunden.';
  if(activeKey) { query.setAttribute('aria-activedescendant','country-option-'+activeKey); document.getElementById('country-option-'+activeKey)?.scrollIntoView({block:'nearest'}); }
  else query.removeAttribute('aria-activedescendant');
}
function search() { results=provider(query.value); activeKey=undefined; render(); }
function commit(key:string) {
  const item=results.find(x=>x.key===key); if(!item || composing || query.disabled || query.readOnly) return;
  if(committed!==key) clearSuccess();
  committed=key; value.value=key; query.value=item.label; recordQueryChange(); query.setCustomValidity(''); query.removeAttribute('aria-invalid'); close();
  status.textContent=`Ausgewählt: ${item.label}.`; query.dispatchEvent(new CustomEvent('value-change',{detail:{value:key},bubbles:true})); query.focus();
}
query.addEventListener('compositionstart',()=>{composing=true;});
query.addEventListener('compositionend',()=>{composing=false; if(query.disabled || query.readOnly) return; recordQueryChange(); search();});
query.addEventListener('input',()=>{ if(query.disabled || query.readOnly) return; recordQueryChange(); query.setCustomValidity(''); query.removeAttribute('aria-invalid'); if(!composing) search(); });
query.addEventListener('keydown',event=>{
  if(composing || event.isComposing || query.disabled || query.readOnly) return;
  if(event.key==='ArrowDown' || event.key==='ArrowUp') {
    if(!open && event.key==='ArrowUp') return;
    event.preventDefault(); const direction=event.key==='ArrowDown'?1:-1;
    if(!open) { results=provider(query.value); activeKey=results[0]?.key; }
    else {const index=results.findIndex(x=>x.key===activeKey); activeKey=results[index<0?(direction>0?0:results.length-1):Math.max(0,Math.min(results.length-1,index+direction))]?.key;}
    render();
  } else if(event.key==='Enter' && open) { event.preventDefault(); if(activeKey) commit(activeKey); }
  else if(event.key==='Escape') {event.preventDefault(); close();}
});
query.addEventListener('blur',()=>{close(); if(committed) {query.value=options.find(x=>x.key===committed)!.label;recordQueryChange();status.textContent=`Ausgewählt: ${query.value}.`;} });
query.addEventListener('invalid',()=>query.setAttribute('aria-invalid','true'));
form.addEventListener('submit',event=>{
 event.preventDefault();
 if(!committed || !options.some(x=>x.key===committed)) {query.setCustomValidity('Bitte ein Land aus der Liste auswählen.'); query.setAttribute('aria-invalid','true'); status.textContent='Bitte ein Land aus der Liste auswählen.';query.reportValidity();return;}
 document.getElementById('form-status')!.textContent='Angaben lokal geprüft. Es wurden keine Daten gesendet.';
});

})();
