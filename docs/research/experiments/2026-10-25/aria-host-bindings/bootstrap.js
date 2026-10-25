const p=(await browser.pages.list()).find(p=>p.ownership==='mine'&&p.url==='about:blank');
return await browser.page(p.pageId).evaluate(async()=>{
  document.title='UI Contracts – isolierte Accessibility-Prüfung';
  const s=document.createElement('script');
  s.src='https://unpkg.com/axe-core@4.14.0/axe.min.js';
  s.integrity='sha384-lFUXB8tI4BaTE1bqxH9eeAXON2NH1qsdAhs7S5L++nUNP5QOy+hwr0C3TYEJUEl0';
  s.crossOrigin='anonymous';
  await new Promise((resolve,reject)=>{s.onload=resolve;s.onerror=()=>reject(new Error('Original library load failed'));document.head.append(s)});
  return {axeVersion:axe.version,userAgent:navigator.userAgent,rules:axe.getRules().filter(r=>/aria|duplicate-id|label|combobox/.test(r.ruleId)).map(r=>({id:r.ruleId,description:r.description,help:r.help}))};
});
