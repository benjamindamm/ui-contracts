async ({artifacts,expectations})=>{
 document.documentElement.lang='de';document.title='UI Contracts – nachvollziehbare Visualänderung';document.body.innerHTML=artifacts['accessibility.html'];
 for(const s of document.head.querySelectorAll('style'))s.remove();const style=document.createElement('style');style.textContent=artifacts['generated-vars.css']+'\n'+artifacts['layout.css'];document.head.append(style);
 await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
 return {userAgent:navigator.userAgent,cases:expectations.map(c=>{const input=document.getElementById('input-'+c.instance),popup=document.getElementById('popup-'+c.instance);const i=input.getBoundingClientRect(),p=popup.getBoundingClientRect();const observed={heightPx:p.height,gapPx:p.top-i.bottom,scrollHeightPx:popup.scrollHeight};return {...c,observed,expectationMet:Math.abs(observed.heightPx-c.heightPx)<=c.tolerancePx&&Math.abs(observed.gapPx-c.gapPx)<=c.tolerancePx&&Math.abs(observed.scrollHeightPx-c.scrollHeightPx)<=c.tolerancePx}})};
}
