// Explicit case-to-token mapping. Never infer a theme from names or component fills.
const hex=/^#[0-9a-f]{6}$/i;
function colorToken(tokens,path,seen=new Set()){
 if(typeof path!=='string'||!path||seen.has(path))throw Error('Missing/cyclic background token: '+path);
 seen.add(path);let token=tokens;
 for(const key of path.split('.')){
  if(!token||typeof token!=='object'||!Object.hasOwn(token,key))throw Error('Unknown background token: '+path);
  token=token[key];
 }
 if(token?.$type&&token.$type!=='color')throw Error('Background token is not a color: '+path);
 const value=token?.$value;
 if(typeof value==='string'&&/^\{[^{}]+\}$/.test(value))return colorToken(tokens,value.slice(1,-1),seen);
 if(typeof value==='string'&&hex.test(value))return value.toUpperCase();
 if(value?.colorSpace==='srgb'&&Array.isArray(value.components)&&value.components.length===3&&value.components.every(v=>Number.isFinite(v)&&v>=0&&v<=1)&&(value.alpha===undefined||value.alpha===1)){
  return '#'+value.components.map(v=>Math.round(v*255).toString(16).padStart(2,'0')).join('').toUpperCase();
 }
 throw Error('Background requires an opaque HEX/sRGB color token: '+path);
}
export function resolveCaseThemes(ids,mapping,tokens,style){
 if(!mapping||typeof mapping!=='object'||Array.isArray(mapping))throw Error('Case themes must be an object');
 for(const id of Object.keys(mapping))if(!ids.includes(id))throw Error('Unknown themed case: '+id);
 return ids.map(id=>{
  if(!Object.hasOwn(mapping,id))return {mode:'unspecified',background:style.colors.surface,caption:style.colors.muted,border:style.colors.border,backgroundToken:null};
  const entry=mapping[id];
  if(!entry||!['light','dark'].includes(entry.mode)||typeof entry.backgroundToken!=='string'||Object.keys(entry).some(k=>!['mode','backgroundToken'].includes(k)))throw Error('Explicit mode and backgroundToken required for case: '+id);
  return {mode:entry.mode,background:colorToken(tokens,entry.backgroundToken),caption:entry.mode==='dark'?style.darkCard.caption:style.colors.muted,border:entry.mode==='dark'?style.darkCard.border:style.colors.border,backgroundToken:entry.backgroundToken};
 });
}
