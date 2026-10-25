from pathlib import Path
import shutil,json
w=Path(__file__).parent;host=w/'host';src=host/'sources';base=w.parent/'ip01-static/reference'
for folder in ['autocomplete','overlay','scroll-area','visual']:
 shutil.copytree(base/folder,src/folder,dirs_exist_ok=True)
S='http://www.w3.org/2005/07/scxml'
# Own full reference behavior. Data/selection/request decisions are in SCXML;
# the host performs typed I/O, DOM projection and actual geometry measurement.
ac='''<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" datamodel="ecmascript" name="ResearchAutocomplete" initial="closed">
<datamodel><data id="owner" expr="'unset'"/><data id="epoch" expr="0"/><data id="query" expr="''"/><data id="value" expr="undefined"/><data id="results" expr="[]"/><data id="activeKey" expr="undefined"/><data id="reqSeq" expr="0"/><data id="revealSeq" expr="0"/><data id="overlayId"/><data id="intent" expr="0"/><data id="composing" expr="false"/><data id="stale" expr="0"/><data id="foreign" expr="0"/><data id="fault" expr="''"/><data id="visible" expr="false"/></datamodel>
<transition event="COMPOSITION_START"><assign location="composing" expr="true"/></transition>
<transition event="COMPOSITION_END"><assign location="composing" expr="false"/><raise event="INPUT_FINAL"/></transition>
<transition event="INPUT" cond="composing"><assign location="query" expr="_event.data.query"/></transition>
<transition event="SET_VALUE" cond="results.some(function(x){return x.key===_event.data.value;})"><assign location="value" expr="_event.data.value"/><assign location="query" expr="results.filter(function(x){return x.key===value;})[0].label"/></transition>
<state id="closed"><onentry><assign location="activeKey" expr="undefined"/><assign location="visible" expr="false"/></onentry>
 <transition event="NAV" cond="!composing &amp;&amp; _event.data.direction===1" target="active"><assign location="epoch" expr="epoch+1"/><assign location="intent" expr="1"/></transition>
 <transition event="INPUT INPUT_FINAL" cond="!composing" target="active"><assign location="query" expr="_event.data ? _event.data.query : query"/><assign location="epoch" expr="epoch+1"/><assign location="intent" expr="0"/></transition>
</state>
<state id="active" initial="opening">
 <invoke type="scxml" idlocation="overlayId" src="../overlay/behavior.scxml"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/></invoke>
 
 <transition event="CLOSE BLUR" target="closed"/>
 <transition event="init.failed" cond="_event.data.owner===owner &amp;&amp; _event.data.epoch===epoch" target="closed"><assign location="fault" expr="_event.data.fault"/></transition>
 <transition event="DATA FAILURE"><assign location="stale" expr="stale+1"/></transition>
 <transition event="overlay.revealed" cond="_event.data.owner===owner &amp;&amp; _event.data.epoch===epoch &amp;&amp; _event.data.requestId===revealSeq"><assign location="visible" expr="_event.data.visible"/></transition>
 <transition event="overlay.revealed"><assign location="foreign" expr="foreign+1"/></transition>
 <transition event="INPUT INPUT_FINAL" cond="!composing" type="internal" target="loading"><assign location="query" expr="_event.data ? _event.data.query : query"/><assign location="intent" expr="0"/><assign location="activeKey" expr="undefined"/></transition>
 <state id="opening"><transition event="INPUT" cond="!composing"><assign location="query" expr="_event.data.query"/></transition><transition event="overlay.ready" cond="_event.data.owner===owner &amp;&amp; _event.data.epoch===epoch" target="loading"/></state>
 <state id="loading"><onentry><assign location="activeKey" expr="undefined"/><assign location="reqSeq" expr="reqSeq+1"/><assign location="fault" expr="''"/><send event="provider.request" target="#_parent"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/><param name="seq" expr="reqSeq"/><param name="query" expr="query"/></send></onentry>
 <transition event="DATA" cond="_event.data.owner===owner &amp;&amp; _event.data.epoch===epoch &amp;&amp; _event.data.seq===reqSeq &amp;&amp; _event.data.results.length&gt;0" target="ready"><assign location="results" expr="_event.data.results"/><assign location="activeKey" expr="intent===1 ? (results.filter(function(x){return !x.disabled;})[0] || {}).key : undefined"/></transition>
 <transition event="DATA" cond="_event.data.owner===owner &amp;&amp; _event.data.epoch===epoch &amp;&amp; _event.data.seq===reqSeq" target="empty"><assign location="results" expr="[]"/></transition>
 <transition event="FAILURE" cond="_event.data.owner===owner &amp;&amp; _event.data.epoch===epoch &amp;&amp; _event.data.seq===reqSeq" target="error"><assign location="results" expr="[]"/><assign location="fault" expr="_event.data.message"/></transition>
 </state>
 <state id="ready"><onentry><raise event="REVEAL_ACTIVE"/></onentry>
 <transition event="NAV" cond="!composing"><script>var keys=results.filter(function(x){return !x.disabled;}).map(function(x){return x.key;}),idx=keys.indexOf(activeKey);activeKey=keys.length ? keys[idx&lt;0 ? (_event.data.direction&gt;0 ? 0 : keys.length-1) : Math.max(0,Math.min(keys.length-1,idx+_event.data.direction))] : undefined;</script><raise event="REVEAL_ACTIVE"/></transition>
 <transition event="REVEAL_ACTIVE" cond="activeKey!==undefined"><assign location="revealSeq" expr="revealSeq+1"/><send event="REVEAL" targetexpr="'#_'+overlayId"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/><param name="key" expr="activeKey"/><param name="requestId" expr="revealSeq"/></send></transition>
 <transition event="ENTER" cond="!composing &amp;&amp; activeKey!==undefined" target="closed"><assign location="value" expr="activeKey"/><assign location="query" expr="results.filter(function(x){return x.key===value;})[0].label"/><send event="value-change" target="#_parent"><param name="value" expr="value"/></send></transition>
 </state><state id="empty"/><state id="error"/>
</state>
<transition event="DATA FAILURE"><assign location="stale" expr="stale+1"/></transition>
</scxml>'''
ac=ac.replace('initial="closed"','initial="machine"',1).replace('</datamodel>','</datamodel><state id="machine" initial="closed">',1).replace('</scxml>','</state></scxml>')
(src/'autocomplete/behavior.scxml').write_text(ac+'\n')
overlay='''<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" datamodel="ecmascript" name="ResearchOverlay" initial="active"><datamodel><data id="owner" expr="'unset'"/><data id="epoch" expr="0"/><data id="scrollId"/></datamodel><state id="active"><invoke type="scxml" idlocation="scrollId" src="../scroll-area/behavior.scxml"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/></invoke>
<transition event="scroll.ready"><send event="overlay.ready" target="#_parent"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/></send></transition>
<transition event="REVEAL"><send event="REVEAL" targetexpr="'#_'+scrollId"><param name="owner" expr="_event.data.owner"/><param name="epoch" expr="_event.data.epoch"/><param name="key" expr="_event.data.key"/><param name="requestId" expr="_event.data.requestId"/></send></transition>
<transition event="scroll.revealed"><send event="overlay.revealed" target="#_parent"><param name="owner" expr="_event.data.owner"/><param name="epoch" expr="_event.data.epoch"/><param name="key" expr="_event.data.key"/><param name="requestId" expr="_event.data.requestId"/><param name="visible" expr="_event.data.visible"/><param name="offset" expr="_event.data.offset"/></send></transition>
<transition event="init.failed"><send event="init.failed" target="#_parent"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/><param name="fault" expr="_event.data.fault"/></send></transition>
</state></scxml>'''
(src/'overlay/behavior.scxml').write_text(overlay+'\n')
scroll='''<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" datamodel="ecmascript" name="ResearchScrollArea" initial="active"><datamodel><data id="owner" expr="'unset'"/><data id="epoch" expr="0"/></datamodel><state id="active"><onentry><send event="scroll.ready" target="#_parent"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/></send></onentry><transition event="REVEAL"/><transition event="MEASURED"><send event="scroll.revealed" target="#_parent"><param name="owner" expr="owner"/><param name="epoch" expr="epoch"/><param name="key" expr="_event.data.key"/><param name="requestId" expr="_event.data.requestId"/><param name="visible" expr="_event.data.visible"/><param name="offset" expr="_event.data.offset"/></send></transition></state></scxml>'''
(src/'scroll-area/behavior.scxml').write_text(scroll+'\n')
shutil.copyfile(w.parent/'ip01-followup/error-relay.scxml',src/'error-relay.scxml')
(src/'autocomplete/layout.css').write_text('[data-part="option"] { min-height:var(--row-height); height:var(--row-height); box-sizing:border-box; flex-shrink:0; padding:6px 10px; } [data-part="option"][aria-selected="true"] { background:#dceafe; } [data-part="option"][aria-disabled="true"] { color:#777; }\n')
(src/'overlay/layout.css').write_text('[data-part="surface"] { position:absolute; top:anchor(bottom); left:anchor(left); width:anchor-size(width); margin-top:var(--gap); background:white; border:0; box-shadow:0 2px 8px #0003; z-index:10; }\n')
(src/'scroll-area/layout.css').write_text('[data-part="viewport"] { max-height:var(--max-height); overflow-y:auto; } [data-part="list"] { display:flex; flex-direction:column; list-style:none; margin:0; padding:0; }\n')
