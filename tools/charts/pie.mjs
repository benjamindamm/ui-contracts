// Geometry from d3-shape; no axes, legend, DOM or chart styling imposed here.
import {pie,arc} from 'd3-shape';
export function pieGeometry(data,{radius=120,innerRadius=0}={}){
 if(!Array.isArray(data)||!data.length)throw Error('Nonempty chart data required');
 if(!Number.isFinite(radius)||radius<=0||!Number.isFinite(innerRadius)||innerRadius<0||innerRadius>=radius)throw Error('Invalid radii');
 const ids=new Set();let total=0;
 for(const d of data){if(!/^[a-z][a-z0-9-]*$/.test(d.id)||ids.has(d.id))throw Error('Unique XML-safe ids required');ids.add(d.id);
  if(typeof d.label!=='string'||!d.label||!/^#[0-9A-F]{6}$/.test(d.color)||typeof d.value!=='number'||!Number.isFinite(d.value)||d.value<0)throw Error('Invalid chart datum');total+=d.value;}
 if(!Number.isFinite(total)||total<=0)throw Error('Positive finite total required');
 const generator=arc().innerRadius(innerRadius).outerRadius(radius).digits(9);
 const segments=pie().sort(null).value(d=>d.value)(data).filter(d=>d.value>0).map(d=>({id:d.data.id,label:d.data.label,value:d.value,color:d.data.color,
  startAngle:d.startAngle,endAngle:d.endAngle,angle:d.endAngle-d.startAngle,proportion:d.value/total,path:generator(d)}));
 if(Math.abs(segments.reduce((s,d)=>s+d.angle,0)-2*Math.PI)>1e-10||segments.some((d,i)=>i&&Math.abs(d.startAngle-segments[i-1].endAngle)>1e-10))throw Error('Angular coverage failed');
 return {total,radius,innerRadius,segments};
}
export const xml=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
export function sectorsSvg(geometry,{cx=0,cy=0,stroke='#FFFFFF',strokeWidth=2}={}){
 return `<g id="pie-sectors" transform="translate(${cx},${cy})">${geometry.segments.map(s=>`<path id="slice-${s.id}" d="${s.path}" fill="${s.color}" stroke="${xml(stroke)}" stroke-width="${strokeWidth}"/>`).join('')}</g>`;
}
