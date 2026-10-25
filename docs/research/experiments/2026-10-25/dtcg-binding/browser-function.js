async ({html,layout,variants,expectations})=>{
 document.documentElement.lang='de';document.documentElement.style.fontSize='16px';document.title='UI Contracts – DTCG-Dimensionen';document.body.innerHTML=html;
 for(const s of document.head.querySelectorAll('style'))s.remove();
 const style=document.createElement('style');document.head.append(style);const results=[];
 for(const [variant,values] of Object.entries(variants)){
  style.textContent=':root{'+Object.entries(values).map(([key,v])=>`${key}:${v.value}${v.unit}`).join(';')+'}\n'+layout;
  await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
  for(const c of expectations.filter(c=>c.variant===variant)){
   const input=document.getElementById('input-'+c.instance),popup=document.getElementById('popup-'+c.instance),list=document.getElementById('list-'+c.instance);const ir=input.getBoundingClientRect(),pr=popup.getBoundingClientRect();const rows=[...list.children].map(x=>x.getBoundingClientRect().height);const computed=getComputedStyle(popup);const observed={gapPx:pr.top-ir.bottom,heightPx:pr.height,rowHeightPx:rows[0],scrollHeightPx:popup.scrollHeight,overflowY:computed.overflowY,maxHeight:computed.maxHeight,allRowHeights:rows};
   results.push({...c,observed,expectationMet:Object.entries(c.expected).every(([k,v])=>Math.abs(observed[k]-v)<=c.tolerancePx)&&rows.every(v=>Math.abs(v-c.expected.rowHeightPx)<=c.tolerancePx)&&computed.overflowY==='auto'});
  }
 }
 return {userAgent:navigator.userAgent,rootFontSize:getComputedStyle(document.documentElement).fontSize,originalDtcgValidator:false,additionalTranslator:true,staticHostOnly:true,cases:results};
}
