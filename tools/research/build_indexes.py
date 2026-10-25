from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]/'docs/research';s=json.loads((r/'study.json').read_text());trials=s['runtime_trials']
lines=['# Index aller ausgeführten Nachweise','','Stand: 25. Oktober 2026. **702 Bedingungen in 106 Gruppen; Recherchephase abgeschlossen.** Vollständig aus study.json abgeleitet. Auch verletzte Erwartungen und korrigierte eigene Erstläufe bleiben erhalten; die Summe ist kein Erfolgs- oder Konformitätszähler.','','[Abschluss und Lesereihenfolge](../RESEARCH-CLOSEOUT.md) · [Aktueller Status](../CURRENT-STATUS.md) · [Dokumentenindex](../DOCUMENT-INDEX.md) · [Historischer Index](../archive/EXPERIMENT-INDEX-HISTORY.md)','','## Jüngste gemeinsame Integrationsnachweise','','- [P106: Browserlauf – 20 finale Erwartungen erfüllt](2026-10-25/ip01-browser/REPORT.md).','- [P105: Statisches Paket – 27 Erwartungen erfüllt](2026-10-25/ip01-static/REPORT.md).','- [P104: Lifecyclefolgevarianten – sechs neue Erwartungen erfüllt; acht Regressionen nicht erneut gezählt](2026-10-25/ip01-followup/REPORT.md).','- [P103: Erster Lifecycleversuch – sechs Erwartungen erfüllt, zwei verletzt; Gegenbefunde erhalten](2026-10-25/ip01-lifecycle/REPORT.md).','','## Vollständiges Register','','Jede Gruppe erscheint genau einmal. Ergebnisdateien enthalten tatsächliche Beobachtungen; Berichte erklären Originalpfad, zusätzliche Adapter, Erstfehler und Grenzen. Quellenkennungen verweisen auf das zentrale Quellenregister.','','| Gruppe | Bedingungen | Prüfgegenstand / Bericht | Ergebnisdateien | Quelle |','| --- | ---: | --- | --- | --- |']
for t in trials:
 report=t.get('report')or str(Path(t['record']).parent/'REPORT.md');assert(r/report).is_file(),t['id']
 title=next((x.lstrip('# ').strip()for x in(r/report).read_text().splitlines()if x.startswith('# ')),t['kind']).replace('|','/');record=f"[Ergebnis]({t['record'].removeprefix('experiments/')})"
 if t.get('additional_record'):record+=f" · [Zusatz]({t['additional_record'].removeprefix('experiments/')})"
 lines.append(f"| {t['id']} | {t['cases']} | [{title}]({report.removeprefix('experiments/')}) | {record} | [{t['source']}](../SOURCES.md) |")
lines+=['','**Zählregel:** Wiederholungen zählen nicht erneut. Eine erfüllte Erwartung ist kein Beleg vollständiger Plattform-/Produktkonformität. Originalbeitrag und eigener Forschungsadapter bleiben getrennt.',''];(r/'experiments/INDEX.md').write_text('\n'.join(lines))
idx=r/'DOCUMENT-INDEX.md';idx.touch(exist_ok=True)
primary=['RESEARCH-CLOSEOUT.md','INTEGRATION-PROFILE.md','INTEGRATION-BINDING-DRAFT.md','INTEGRATION-ACCEPTANCE.md','IMPLEMENTATION-HANDOFF.md','CURRENT-STATUS.md','ARCHITECTURE-DIRECTION.md','PROJECT-GAPS.md','DOCUMENT-INDEX.md','STUDIES.md','archive/README.md']
evidence=['MATRIX.md','CLAIMS.md','SOURCES.md','METHODS.md','REQUIREMENTS.md','CONTEXT.md','TOOLING-COMPARISON.md','COMPARE-UXSPEC-SCXML.md','COMPARE-DESIGN-LAYOUT.md']
limits=['OPEN-FIELDS.md','OPEN-QUESTIONS.md','REMAINDER-PLAN.md']
files=sorted(p.name for p in r.glob('*.md'));groups=[('Aktueller Einstieg und Übergabe',primary),('Methodik, Befunde und Vergleiche',evidence),('Dokumentierte externe Restklärungen',limits)];used=set(primary+evidence+limits);groups.append(('Vertiefungen und historische Arbeitsstände',[n for n in files if n not in used]))
lines=['# Dokumentenindex','','Stand: 25. Oktober 2026. Vollständiges Verzeichnis der '+str(len(files))+' Markdown-Dokumente im Forschungsstamm. Versuchsordner werden separat im [vollständigen Experimentindex](experiments/INDEX.md) erschlossen. [Abschluss und Lesereihenfolge](RESEARCH-CLOSEOUT.md).','','Aktuelle Einstiege stehen zuerst. Ältere Berichte behalten ihre damaligen Zahlen; maßgeblich für den Abschlussstand sind CURRENT-STATUS und study.json. iOS/Android sind Zukunftsperspektive, keine offene Testpflicht dieser Recherche.']
for heading,names in groups:
 lines+=['','## '+heading,'','| Dokument | Inhalt |','| --- | --- |']
 for n in names:
  p=r/n;assert p.is_file(),n
  title='Dokumentenindex'if n=='DOCUMENT-INDEX.md'else next((x.lstrip('# ').strip()for x in p.read_text().splitlines()if x.startswith('# ')),n).replace('|','/')
  lines.append(f'| [{n}]({n}) | {title} |')
nested=sorted(p for p in r.rglob('*.md')if p.parent!=r)
lines+=['','## Dokumente in Unterordnern','','Die einzelnen Berichte sind hier zusätzlich vollständig nach Pfad auffindbar; der Experimentindex ordnet ihnen die 106 Prüfgruppen zu.','','| Dokument | Inhalt |','| --- | --- |']
for p in nested:
 rel=str(p.relative_to(r));title=next((x.lstrip('# ').strip()for x in p.read_text().splitlines()if x.startswith('# ')),rel).replace('|','/')
 lines.append(f'| [{rel}]({rel}) | {title} |')
lines+=['','## Maschinenlesbare Daten und Prüfarbeitsstände','','| Datei | Bedeutung |','| --- | --- |']
for p in sorted(r.glob('*.json')):
 desc={'study.json':'Maßgebliche Bewertungen, Claims, Quellenzuordnungen und ausgeführte Prüfgruppen.','REMAINDER-PLAN.json':'Exakt verbleibende Matrix-U-Zellen; keine offene native Testpflicht.','INTEGRATION-PROFILE-EVIDENCE.json':'Belegpfade und Hashes des Integrationsvorschlags; kein ausführbares Produktmanifest.'}.get(p.name,'Maschinenlesbarer ergänzender Forschungsstand; Einordnung im zugehörigen Bericht.')
 lines.append(f'| [{p.name}]({p.name}) | {desc} |')
lines+=['','## Experimentordner','','[106 Gruppen mit direkten Links zu Berichten und Rohresultaten](experiments/INDEX.md). In den Ordnern stehen je nach Versuch Vorregistrierung, Original-/Eigenartefaktmanifest, ausführbarer Forschungszusatz und erhaltene Erst-/Korrekturläufe. Rohresultate und Code sind keine zusätzlich beschlossenen Produktformate.',''];idx.write_text('\n'.join(lines))
assert set(files).issubset({n for _,names in groups for n in names})
print(json.dumps({'root_markdown_documents':len(files),'all_markdown_documents':len(files)+len(nested),'indexed_groups':len(trials),'indexed_conditions':sum(t['cases']for t in trials)}))
