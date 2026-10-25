from pathlib import Path
import json
p=Path(__file__).parent;r=json.loads((p/'results.json').read_text());pre=json.loads((p/'schema-preflight.json').read_text());pre={f['input']:f for f in pre['files']}
criteria={
'ref-01-local-control':('Lokale Unterreferenz erhält LIBRARY',lambda o:o.get('childContent')=='LIBRARY'),
'ref-02-imported-shadowing':('Importierte Unterreferenz behält Bibliotheksziel trotz gleichnamigem Appziel',lambda o:o.get('childContent')=='LIBRARY'),
'ref-03-imported-no-local':('Importierte Unterreferenz wird in ihrer Bibliothek aufgelöst',lambda o:o.get('childContent')=='LIBRARY' and not o.get('issueCodes')),
'ref-04-missing-import-area':('Angeforderter, fehlender Bereich wird diagnostiziert',lambda o:bool(o.get('issueCodes'))),
'ref-05-missing-file-control':('Fehlende Datei erzeugt IMPORT_NOT_FOUND',lambda o:'IMPORT_NOT_FOUND' in o.get('issueCodes',[])),
'ref-06-original-cem-target':('Grenzfall: originales Fremdformat wird nicht ohne Adapter als UXSpec-Element aufgelöst',lambda o:'UNKNOWN_IMPORTED_ELEMENT_REFERENCE' in o.get('issueCodes',[])),
'ref-07-unit-value':('Bedeutungstragende Einheit bleibt bei der Tokenauflösung erhalten',lambda o:isinstance(o.get('resolvedPadding'),dict) and o['resolvedPadding'].get('unit')=='rem'),
'ref-08-separate-expansions':('Statische Expansionen A/B besitzen getrennte kopierte Werte',lambda o:o.get('before',[{},{}])[0].get('content')=='A' and o.get('before',[{},{}])[1].get('content')=='B' and o.get('after',[{},{}])[1].get('content')=='B'),
'bundle-01-unique-ids':('Drei unterschiedliche Module bleiben vollständig enthalten',lambda o:o.get('ok') and set(o.get('moduleIds',[]))=={'root','child-a','child-b'}),
'bundle-02-duplicate-child-id':('Doppelte Maschinen-IDs werden abgewiesen statt still überschrieben',lambda o:o.get('ok') is False and bool(o.get('issueCodes'))),
'bundle-03-entry-id-collision':('Eintrittsmodul kann nicht still durch gleichnamige Abhängigkeit ersetzt werden',lambda o:o.get('ok') is False and bool(o.get('issueCodes'))),
'bundle-04-transitive-child':('Tatsächlich referenzierte Großkindmaschine bleibt im Bundle auflösbar',lambda o:o.get('ok') and 'grand' in o.get('moduleIds',[])),
'ref-09-element-cycle':('Unauflösbare Elementrekursion ergibt strukturierte Diagnose statt Stackfehler',lambda o:not o.get('thrown') and bool(o.get('issueCodes'))),
'ref-10-file-self-cycle-control':('Direkter Datei-Selbstimport wird als IMPORT_CYCLE erkannt',lambda o:'IMPORT_CYCLE' in o.get('issueCodes',[])),
}
for c in r['cases']:
 desc,predicate=criteria[c['id']];c['criterion']=desc;c['criterion_met']=predicate(c['observation']);c['schema_preflight']=[{'input':f,'valid':pre[f]['valid']} for f in c['inputs'] if f in pre]
 # normalize observation path strings as already done for primary output
 c['observation']=json.loads(json.dumps(c['observation']).replace(str(p),'<probe-root>'))
r['assessment_note']='Explorative Ausführung; die Akzeptanzkriterien wurden anschließend explizit gegen die gespeicherten Outputs ausgewertet. Keine unabhängige Replikation und keine nachträglich behauptete Präregistrierung. Die vorangehenden E2-Befunde C390/C391/C395 enthalten bereits Hypothesen für Teilfälle.'
r['criteria_met']=sum(c['criterion_met'] for c in r['cases']);r['criteria_not_met']=sum(not c['criterion_met'] for c in r['cases']);(p/'results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('14 explorative cases:',r['criteria_met'],'criteria met,',r['criteria_not_met'],'not met')
for c in r['cases']:
 print(c['id'],'preflight',[(f['input'].split('/')[-1],f['valid']) for f in c['schema_preflight']],'criterion',c['criterion_met'])
