from pathlib import Path
import json,collections
p=Path(__file__).resolve().parents[1];s=json.loads((p/'study.json').read_text());d=json.loads((p/'REMAINDER-PLAN.json').read_text());active={(e['candidate'],e['requirement']):e for e in s['evaluations']if e['coverage']=='U'};assert set(active)=={(c['candidate'],c['requirement'])for c in d['cells']}
for c in d['cells']:assert c['current_claim']==active[(c['candidate'],c['requirement'])]['claim']
old=p/'REMAINDER-PLAN.md';history=p/'REMAINDER-PLAN-HISTORY.md'
if not history.exists():history.write_text('# Historischer Restplanverlauf\n\nDieser archivierte Text enthält ältere Tabellen und Zwischenzahlen. Er ist keine aktuelle Arbeitsqueue. Maßgeblich sind [aktueller Restplan](REMAINDER-PLAN.md), study.json und OPEN-FIELDS.md.\n\n'+old.read_text())
groups=collections.defaultdict(list)
for c in d['cells']:groups[c['group']].append(c)
names={'LAYOUT':'Ursprüngliche Layout-/Scrollmodelle','COMPLEMENT':'Fachfremde Teilbeiträge: eigenständigen Beitrag erst nachweisen','REFERENCES':'Externe Modellreferenzen','INDEPENDENCE':'Vier unabhängig beschreibbare Domänen','OWNERSHIP':'Führende Quellen und Änderungen','COMPOSITION':'APG-Komposition','ORIGINAL':'Konkrete externe Originalklärungen'}
lines=['# Aktuelle Restplanqueue', '',f"Stand:25. Oktober2026. **{len(active)} offene Zellen**, {len(s['claims'])} Claims, {sum(t['cases']for t in s['runtime_trials'])} Bedingungen/{len(s['runtime_trials'])} Gruppen. Diese Tabellen werden ausschließlich aus den aktuellen U-Schlüsseln in study.json und REMAINDER-PLAN.json abgeleitet.",'',f"{d['class_counts']['a']} unabhängig untersuchbare Fragen,{d['class_counts']['b']} konkrete Originalklärungen; keine Zusage, dass die Untersuchung positiv schließen wird. Die [46er Baseline](REMAINDER-BASELINE.md) und [historischen Zwischenstände](REMAINDER-PLAN-HISTORY.md) sind separat erhalten.",'','## Aktuelle Pakete','']
for group,cells in sorted(groups.items(),key=lambda x:min(c['priority']for c in x[1])):
 first=cells[0];lines += [f"### {names.get(group,group)} ({len(cells)} Zellen)",'',f"**Fehlende Aussage:** {first['question']}",'',f"**Endbedingung:** {first['stop_criterion']}",'',f"**Originalumfang:** {first['source_scope']}",'','| Kandidat | Feld | Aktueller Claim | Arbeitsklasse | Begrenzter Prüfpfad |','| --- | --- | --- | --- | --- |']
 for c in cells:
  review=next((c[k]for k in ['latest_overall_review','latest_review','latest_evidence_review','latest_builder_review','latest_bounded_review','latest_root_review']if c.get(k)),None)
  reviewed=f'[Bericht]({review})'if review else'Siehe Claim'
  lines.append(f"| {c['candidate']} | {c['requirement']} | [{c['current_claim']}](CLAIMS.md#{c['current_claim'].lower()}) | {c['plan_class']} | {reviewed} |")
 lines+=['']
lines+=['## Stopregeln und Herkunft','','Ein verlinkter Originalpfad kann vollständig untersucht sein, während seine konkrete fachliche Frage offen bleibt. U behauptet keine unbearbeitete Recherche; der aktuelle Claim und sein nächster notwendiger Beitrag sind maßgeblich.','','Nur neue entscheidende Originalpfade oder konkret begründete zusätzliche Bindungen eröffnen bereits begrenzt geprüfte Fragen erneut. Sachfremde Zellen bleiben U; keine automatische Zurechnung fremder Fähigkeiten. Eigene Policy, Adapter, Originalsemantik und tatsächlicher Ausführungsumfang bleiben getrennt. Vollständige Produkt-/Plattform-/AT-Abnahme ist ein stärkeres separates Ziel.','','Die zwei externen Originalklärungen werden ohne neue Originalinformation nicht erneut gleich geprüft. Keine Autorenanfrage wurde versandt. Untersuchung ist nicht gleich technische Schließung. Kein Commit/Push.','']
old.write_text('\n'.join(lines));baseline=d['baseline_cells'];assert len(baseline)==d['baseline_remaining_cells']==46
b=['# Erhaltene 46-Zellen-Baseline','','Dieser Ausgangsstand ist historisch. Die aktuelle Queue steht im [Restplan](REMAINDER-PLAN.md). Hier sind die unveränderten Baseline-Schlüssel und die danach geschlossen bewerteten Beiträge dokumentiert.','','| Kandidat | Feld | Baseline-Claim |','| --- | --- | --- |']
for c in baseline:b.append(f"| {c['candidate']} | {c['requirement']} | [{c['claim']}](CLAIMS.md#{c['claim'].lower()}) |")
b+=['','## Seit der Baseline begrenzt geschlossen','','| Kandidat | Feld | Abdeckung | Claim |','| --- | --- | --- | --- |']
for c in d['closed_since_baseline']:b.append(f"| {c['candidate']} | {c['requirement']} | {c['coverage']} | [{c['claim']}](CLAIMS.md#{c['claim'].lower()}) |")
(p/'REMAINDER-BASELINE.md').write_text('\n'.join(b)+'\n');assert len(d['closed_since_baseline'])+len(active)==46
print('Aktive Queue exakt',len(active),'Zellen;',len(d['closed_since_baseline']),'begrenzte Schließungen separat von46er Baseline. Gruppen:',{k:len(v)for k,v in groups.items()})
