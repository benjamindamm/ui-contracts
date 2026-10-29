# AC-R02 · Externe Bewertung der Ergebnisse und Prüfmethode

**29. Oktober 2026 · Analyse von außen · run-02 unverändert.**

**Fazit:** Die zwei Designs sind brauchbare, weitgehend übereinstimmende statische Umsetzungen. Die gelieferte Prüfkette ist ausführbar und ihre Ergebnisse sind reproduzierbar. Ihr Urteil „alle expliziten Kriterien erfüllt“ ist jedoch fachlich nicht haltbar: Beide Designs verletzen erneut die explizite Platzhalterfarbregel; der Prüfer erklärt sie fälschlich zur Wahlfreiheit. Darüber hinaus decken mehrere Checks weniger ab, als ihre Texte behaupten. Der wichtigste Verbesserungsbedarf liegt deshalb bei **Quellauslegung, Prüferqualität und kontrollierter Vergleichbarkeit**, nicht allein beim Builder-Modell.

## Gegenstand, Modell und Grenzen dieser Analyse

- Modell des Laufs laut Nutzer: **DeepSeek V4.1 Flash**. Diese Zuordnung stammt aus dem Auftrag vom 29. Oktober; `run-02/run.json` nennt kein Modell. Modellrevision, Reasoning-Stufe und Konfiguration je Builder/Prüfer sind nicht dokumentiert. Daraus wird keine gesondert verifizierte Prüfer-Modellzuordnung abgeleitet.
- Bewertet wurden [Laufrahmen](../../../../examples/autocomplete/reproducibility/run-02/run.json), [Laufübersicht](../../../../examples/autocomplete/reproducibility/run-02/README.md), beide Builderberichte, Generatoren, FIG-Dateien, Eingabehashes, versiegelte Kriterien, Reader/Renderer/Prüfcode, Messdaten und Ergebnisbericht.
- Maßstab für Verbesserungsvorschläge: [UI-Contracts-Skill](../../../../skills/ui-contracts/SKILL.md), [Autorenregeln](../../../../skills/ui-contracts/references/authoring.md), [Prüfanweisungen](../../../../skills/ui-contracts/references/validation.md). Ob diese Texte den Laufagenten tatsächlich vorlagen, ist nicht belegt. Die erlaubten Eingaben des Laufs nennen sie nicht; vollständige Aufträge und Fortsetzungsnachrichten fehlen. Ein Fehler ist deshalb nicht automatisch ein nachgewiesener Fehler des Skills.
- Kein Kontakt zu externen Diensten, keine Änderung der eingefrorenen Definition, Kriterien, Designs oder Ergebnisse. Die Analyse trennt die historische Bewertung von den anschließend beauftragten Setup-Reparaturen; es gibt keine rückwirkenden Reparaturen des Laufs.

## Tatsächlich ausgeführte Gegenprüfung

[audit.py](audit.py) legt eine temporäre Kopie an und führt dort Originalreader, Originalrenderer und beide Stufen von `verify.py` aus. Ergänzend liest ein eigener kurzer Reader die FIG-Dateien direkt. Gegenfälle verändern nur Messdaten im Arbeitsspeicher; sie sind **keine zusätzlich gefundenen Fehler der gelieferten Designs**.

Ergebnisse in [audit-results.json](audit-results.json):

| Prüfung | Ergebnis |
| --- | --- |
| Hashmanifest des Reviews, Kriterien-Siegel, Lieferungen und im Lauf referenzierte Artefakte | alle vorhandenen Einträge stimmen |
| Definition | 22/22 Hashes stimmen; Revisionshash unabhängig nachgerechnet |
| Vergleich mit run-01 | dieselben 22 Eingabedateien und derselbe Werkzeug-Lock |
| Erneutes Lesen der FIG-Dateien | native Knoten entsprechen den archivierten Readerauszügen |
| Erneutes Rendern | beide PNGs bytegleich mit den archivierten Review-Renders |
| Erneute Kriterienauswertung | gespeicherte Einzelbewertungen und Paarvergleich reproduziert |
| Direkter Readback | zehn Fallcontainer je Design; keine gesperrten Knoten gefunden |
| Unverändertheit run-02 | alle 32 Dateien vor/nach der Analyse hashgleich |

Die Ausführung bestätigt Reproduzierbarkeit des **Prüfprogramms**, nicht automatisch Richtigkeit seiner Sollwerte. Das lokale Siegel belegt die heutigen Dateihashes, aber nicht unabhängig den historischen Zeitpunkt der Versiegelung. Die behauptete Reihenfolge „Kriterien vor Ausgaben“ bleibt dokumentierte Provenienz ohne externes Zeitprotokoll.

Nachvollziehen, ohne run-02 zu überschreiben:

```sh
python3 docs/research/analyses/AC-R02/audit.py
```

## Bewertung der Designs

Positiv: Beide Dateien sind mit dem gepinnten Originalreader lesbar, enthalten zehn Fälle und echte editierbare Text-/Frame-Strukturen. Die Zustandsdarstellungen, Ergebnisdaten, Geometrie und das statische Scroll-Ende sind im geprüften Umfang weitgehend konsistent. Die Originalrenders wurden zusätzlich visuell angesehen. Unterschiedliche Außenanordnung ist erlaubt; A hat einen transparenten Seitenhintergrund, B eine hinterlegte Übersichtsfläche. Diese Unterschiede rechtfertigen keinen pauschalen Qualitätsabzug.

### Gemeinsame explizite Abweichung: deaktivierter Platzhalter

Die führende Quelle [layout.css](../../../../components/autocomplete/layout.css) setzt:

```css
[data-part="input"]::placeholder { color: var(--ac-muted); }
[data-part="input"]:disabled { color: var(--ac-disabled); border-color: var(--ac-border); }
```

Das Pseudoelement hat eine eigene gesetzte Farbe. Die Farbe des deaktivierten Inputs überschreibt diese nicht. Soll für den sichtbaren Platzhalter ist **#64748B**; beide FIG-Dateien enthalten **#94A3B8**. Die aktuelle Definition stimmt laut Hashprüfung mit run-01 überein; dessen separate [Browserkontrolle](../../studies/AC-R01/native-css-control.json) bestätigt dieselbe Quellauslegung. Diese Analyse führt keinen neuen Browserlauf aus.

- A: Textknoten `0:129`, `Stadt suchen …`, #94A3B8.
- B: Textknoten `0:122`, `Stadt suchen …`, #94A3B8.
- Builder B benennt in seinem Bericht ausdrücklich, dass wörtlich die Platzhalterfarbe gewinnt, und wählt trotzdem zur besseren Unterscheidbarkeit die andere Farbe. Das ist eine bewusste gestalterische Abweichung, keine Definitionslücke.
- Der Prüfer lässt in AS15 beide Farben zu. COL03 gewährt die Ausnahme; ST10 und COL08 verlangen sogar die abweichende Farbe. Damit widersprechen sich Quellregel und Teile des Prüfmaßstabs.

**Externes Urteil:** Hohe Übereinstimmung in vielen gemessenen statischen Eigenschaften; **beide nicht vollständig definitionstreu**. Unter der in run-02 selbst festgelegten Regel „mindestens ein expliziter Verstoß → FAIL“ würde dieser Befund für beide zu FAIL führen. Das historische Urteil bleibt unverändert als Originalbefund erhalten. Die vier dort gezählten Accessibility-Abweichungen werden hier nicht einfach übernommen und auch keine neue Gesamtquote erfunden.

### Weitere Unterschiede und Grenzen

- B verwendet im normalen Inputrahmen **#CBD5E2 statt #CBD5E1**. Das ist innerhalb der vorab gewählten Farbtoleranz, aber keine exakte Tokenübernahme. Beim Übertragen eines expliziten Tokens ist eine Umrechnungstoleranz von einer legitimen Designfreiheit zu unterscheiden.
- B nutzt COMPONENT statt FRAME und liefert eine zusätzliche leere Seite. Das ist vom Lauf erlaubt. Weniger Knoten oder kleinere Dateigröße belegen keine höhere Qualität.
- A liest Tokens mit Aliasauflösung; B kodiert viele Tokenwerte, Ergebnisdaten und Meldungen im Generator fest. Für eine einmalige eingefrorene Projektion ist das nicht automatisch unzulässig. Es belegt aber keinen allgemeinen Adapter, der eine geänderte Definition korrekt verarbeitet; die kopierte Rahmenfarbe zeigt das Drift-Risiko.
- B meldet Font-Fallback, A eine mitgelieferte Inter-Schrift. Die Renders sind hier reproduziert, jedoch ohne neue Kontrolle der tatsächlich verwendeten Fontdatei/Glyphmetriken. Native `fontFamily: Inter` allein beweist keine identische Rasterdarstellung in anderen Umgebungen.
- Native Editierbarkeit ist strukturell gestützt; eine GUI-Änderung mit erneutem Speichern wurde in dieser Analyse nicht ausgeführt. Laufzeitverhalten, AX/Screenreader, echte Eingabe-/Fokus-/Scrollinteraktion und native Plattformen sind nicht geprüft.

## Bewertung der Prüfkette

### 1. Gute Grundlage, aber keine belastbare Vollständigkeitsbehauptung

Positiv sind die getrennte Kriterienphase, Originaldatei-Readback, unabhängige Renders, Einzelmessungen und transparente Trennung von Selbstauskunft und Messung. Die Prüfkette lässt sich tatsächlich wiederholen. Die Definition wurde nicht passend gemacht und bekannte Unterschiede werden berichtet.

**Problem:** In `verify.py` sind A08 (Eingabeintegrität), A09 (Offenlegung), TY05 und mehrere A11Y-Bewertungen mit festen Wahrheitswerten implementiert. Solche Einträge können manuelle Bewertungen darstellen, werden durch das Skript aber nicht neu geprüft. Insbesondere liest `main_full()` für A08 weder aktuelle Komponentenhashes noch die Builder-Manifeste. Die externe Hashprüfung bestätigt den vorliegenden Stand trotzdem; sie ersetzt nicht die fehlende automatische Assertion im historischen Checker.

### 2. Ausgeführte Gegenfälle zeigen echte Prüflücken

| Gegenfall nur in Messdaten von A | Reaktion des vorhandenen Checkers | Bedeutung |
| --- | --- | --- |
| Platzhalter auf quellkonformes #64748B setzen | ST10 und COL08 wechseln von pass auf fail | Der Checker bestraft die korrekte Quellauslegung. |
| Input-Rahmenstärke ready von 1 auf 9 px setzen | GEO08 bleibt pass; keine Statusänderung; Paarwert weiter 1,0 | GEO08 prüft die Zahl der Konturen, nicht deren Stärke. |
| Schriftgröße der zweiten ready-Option von 14 auf 28 px setzen | TY02 bleibt pass; keine Statusänderung; Paarwert weiter 1,0 | Typografieprüfung liest nur einen ausgewählten Optionswert. |
| Inputwert in loading auf Fehlerrot setzen | COL02 und COL11 bleiben pass; keine Statusänderung | COL02 prüft Labels; COL11 prüft Tokenzugehörigkeit, nicht den richtigen Einsatz. |

Diese Gegenfälle testen den **Auswertungsteil** auf Messdatenebene; sie sind keine End-to-End-Mutationstests modifizierter FIG-Dateien. Trotzdem widerlegen sie die behauptete vollständige Abdeckung der jeweiligen Kriterien. Bei Farben erkennt der Paarvergleich teilweise einen Unterschied, obwohl die Konformitätsprüfung ihn akzeptiert; Übereinstimmung und Korrektheit sind verschiedene Prüffragen.

### 3. Paarwert 1,000 ist enger als die Beschreibung

Die 199 visuellen Merkmale sind ein ausgewählter Merkmalsvektor, nicht sämtliche Designwerte. Die Optionsschriftgrößen und Rahmenstärke aus den Gegenfällen fehlen darin; `None`-Werte werden übersprungen. In `A_struct` wird Gleichheit kompletter Optionslabel-Listen als ein Punkt addiert, statt den beschriebenen Jaccard-Vergleich der Optionsmengen vollständig umzusetzen. `A_state` zählt Einzelattribute, während das Protokoll von Fällen mit gemeinsam übereinstimmenden Attributen spricht. Bei den vorliegenden gleichen Werten ändern diese Unterschiede den Score nicht, bei künftigen Abweichungen können sie es tun.

Darum lautet die belastbare Aussage: **Die aktuell ausgewählten und tolerierten Merkmale stimmen überein.** Der Wert belegt weder pixelgleiche Designs noch vollständige semantische Gleichheit oder ein besseres Modell.

### 4. Accessibility: Zielvertrag und Nachweisart müssen klarer werden

Die Definition verlangt für das Designziel benannte Teile, Label, Statustext sowie aktive/deaktivierte Styles und grenzt Screenreaderverhalten aus. Daraus leitet der Prüfer zusätzliche Annotationserwartungen ab, ohne ein verbindliches Ziel-Metadatenformat festzulegen. Fehlende echte ARIA-Ausführung auf einer Designfläche ist kein sinnvoller Laufzeittest.

Die vier als Ursache angegebenen A11Y-Fails werden in `verify.py` pauschal gesetzt; der Readerauszug erfasst insbesondere kein `pluginData`. Andere A11Y-Passes beruhen ebenfalls auf festen Einordnungen. Die Skripte allein beweisen somit weder das Fehlen aller Annotationen im nativen Format noch dessen generelle Unfähigkeit dazu. A11Y01 erlaubt laut Kriterium sogar einen Namen mit `combobox`; ein ausschließlich fehlendes Rollenfeld wäre dafür nicht ausreichend.

Für einen zukünftigen statischen Zielvertrag entweder konkrete, roundtrip-geprüfte Annotationen verpflichtend machen (Teil/Instanz/State/Source) oder die betreffenden Regeln als nicht abgebildet ausweisen. Echte Accessibility-Konformität benötigt separat ein ausführbares Ziel. Die vier historischen Abweichungen bleiben als Urteile dieses Prüfers erhalten; sie sind kein isolierter Beweis für eine Modellschwäche.

## Unterbrechungen und Prozessnachweise

`run.json` enthält **vier Unterbrechungseinträge: zwei für A, zwei für B**. Daraus ergeben sich je Builder drei Bearbeitungsabschnitte. Die Laufübersicht unterscheidet das korrekt; Review und `results.json` führen dagegen einen dritten „Stopp“ auf, dessen Inhalt bereits die erfolgreiche Abschlusslieferung beschreibt. Das sollte extern als Zählinkonsistenz gelesen werden, nicht als bewiesener weiterer Limitabbruch.

Gut dokumentiert sind Ursache laut Koordinator, Lieferstand, Fortsetzung derselben Session und fehlende Zwischenartefakte. Das macht den Versuch als fortgesetzten Lauf verwertbar. Es fehlen jedoch exakte Erstaufträge/Fortsetzungsnachrichten, Zeitpunkte, tatsächliche Schrittbudgets/-zahlen, Token-/Zeitaufwand und Zugriffsaudits. Die entfernten Proben sind nicht nachprüfbar. „Keine verbotenen Quellen gelesen“ bleibt eine Koordinator-/Agentenangabe, kein durch Dateihashes bewiesener Zugriffsnachweis; gleiche Kontexte allein begründen keine statistische Unabhängigkeit.

Fortsetzungen zerstören die Artefaktbewertung nicht. Wenn dabei neue fachliche Hinweise oder Prioritäten gegeben werden, kann das die Vergleichbarkeit der Erzeugung beeinflussen. Ob das hier geschah, ist ohne den Nachrichtenwortlaut nicht nachprüfbar. Ein Limitstopp belegt für sich weder Modellversagen noch schlechte Definitionen. „Der Prüfer war nicht betroffen“ ist ebenfalls enger zu dokumentieren: Das maschinenlesbare Feld versichert nur keine Unterbrechung während Phase 1.

## Vergleich mit GPT-6.1 Sol / Medium (run-01)

Die Eingabedateien und der Werkzeug-Lock sind identisch. Beide Läufe liefern je zwei native Designs mit hoher gemessener Übereinstimmung und **derselben Platzhalterfarbabweichung**. run-02 verwendet jedoch frisch abgeleitete Kriterien, andere Toleranzen und eine andere Urteilslogik. Deshalb ist **„DeepSeek besteht, GPT fällt durch“ keine durch diesen Versuch gestützte Aussage**. Der Unterschied liegt hier bereits im Prüfermaßstab.

Modellzuordnungen beider Läufe sind nachträgliche Nutzerangaben, ohne vollständige Metadaten je Rolle. Für belastbare Modellvergleiche müssen dieselben Artefakte unter einem gemeinsamen externen Prüfkern bewertet und Kriterienentwurf, Builder-Output und Prüfer-Output getrennt betrachtet werden. Ein solcher vollständiger gemeinsamer Vier-Artefakt-Benchmark wurde hier nicht ausgeführt; diese Analyse belegt die gemeinsame konkrete Abweichung und die Unterschiede im Prüfmaßstab.

## Priorisierte Verbesserungen für den nächsten Lauf

| Priorität | Bereich | Konkrete Änderung | Nachweis, dass die Verbesserung greift |
| --- | --- | --- | --- |
| P0 | Builder-Instructions / Skill | Explizite Quellregeln haben Vorrang vor ästhetischer Plausibilität. Pseudoelement, eigener Wert und Vererbung unterscheiden; bewusste Abweichung als Verstoß melden. | Platzhalter-Gegenfall muss beanstandet werden; nur der Inputwert erbt disabled-Farbe. |
| P0 | Reviewer-Instructions | Kriterien vor dem Versiegeln auf Widersprüche zur Quelle und zueinander prüfen. Jede Annahme braucht Quelle und Begründung, warum wirklich keine verbindliche Regel existiert. | AS15 kann COL03 nicht still aufweichen; gültige Sollkorrektur löst keinen Fehler aus. |
| P0 | Prüfwerkzeuge | Kein automatisches pass ohne Assertion. Umfang aller Teile/Zustände prüfen; manuelle Urteile mit Evidenz und `manual` kennzeichnen. Positive und negative Gegenfälle für jeden Checktyp. | Die drei oben unentdeckten Fehler werden erkannt; fehlender Nachweis wird nicht pass. |
| P0 | Modellvergleich | Gemeinsamen externen Prüfkern und Toleranzen vor Modellläufen einfrieren; frei vom Builder abgeleitete Reviewer-Kriterien separat untersuchen. | Gleiche Artefakte erhalten bei gleicher Policy das gleiche Urteil, unabhängig vom Reviewer-Modell. |
| P1 | Zielprofil | Statisches OpenPencil-Profil mit verbindlicher Mappingtabelle für Instanz, Teil, Zustand und Herkunft; unterstützte Metadaten roundtrip-prüfen. | Anforderungen sind am ausgelieferten FIG oder explizit gebundenen Sidecar messbar. Kein Canvas-ARIA-Laufzeitversprechen. |
| P1 | Prozess-Instructions | Erst kurze Werkzeugprobe, dann minimale vollständige Lieferung, danach Ausbau; vor dem Budgetende Checkpoint mit Restaufgaben. Fortsetzungsauftrag neutral und unverändert speichern. | Jeder Abbruch hat eindeutige ID, Artefakthashes, Budget und Fortsetzungstext. Kein stilles Nachcoaching. |
| P1 | Dokumentation | Modell/Version/Reasoning je Rolle, Harness-Limits, Prompt-/Skillversion, Zeit/Token, Ergebnisstatus und Gründe erfassen. Stopps von erfolgreichen Abschlusssegmenten trennen. | Metadaten sind ohne Gesprächsverlauf rekonstruierbar; unbekannte Werte bleiben null. |
| P1 | Definition / Handoff | Hashalgorithmus in erlaubten technischen Metadaten erklären; „drei unsichtbare Zeilen“ separat für neue Definitionsrevision klären; `{count}` explizit definieren. | Unabhängiger Prüfer kann Revision nachrechnen und echte Textmehrdeutigkeiten vermeiden. Alte Definition bleibt eingefroren. |
| P2 | Rendering / Adapter | Fontdateien und Renderer binden; kopierte Tokens vermeiden oder gegen führende Tokens prüfen. Bytegleichheit, semantische Gleichheit und Bildähnlichkeit getrennt berichten. | #CBD5E2 wird als Tokenabweichung sichtbar; Font-/ZIP-Unterschiede verfälschen den Qualitätsvergleich nicht. |

Vorgeschlagene kurze Ergänzung für künftige Autorenaufträge:

> Übertrage explizite Regeln unverändert. Eine optisch plausiblere Entscheidung ersetzt keine Quellregel. Unterscheide Element, Pseudoelement und Vererbung. Erzeuge zuerst ein lesbares Zielartefakt mit allen geforderten Fällen; dokumentiere Annahmen, echte Abweichungen und noch ungeprüfte Eigenschaften getrennt. Sichere vor einem Limitstopp einen Checkpoint. Lies keine fremden Läufe oder Prüfergebnisse.

Vorgeschlagene kurze Ergänzung für künftige Prüferaufträge:

> Prüfe zuerst den Zielumfang und die Widerspruchsfreiheit deiner Sollwerte. Belege jede Interpretation mit der führenden Quelle. Teste deine Assertions mit mindestens einem gültigen und einem fehlerhaften Gegenfall je Prüfart. Trenne automatisierte Messung, manuelle Bewertung und fehlenden Nachweis. Bezeichne nur den tatsächlich verglichenen Merkmalsumfang als übereinstimmend. Originale, Kriterien und historische Ergebnisse bleiben unverändert.

Die Formulierungen waren zunächst Vorschläge. Nach dem ergänzenden Nutzerauftrag wurden die daraus abgeleiteten Regeln im Repository-Skill und seiner lokalen Installation sowie im [Laufprotokollvertrag](../../../skills/REPRODUCIBILITY.md) umgesetzt. Der Umfang der Reparaturen und noch offene Fähigkeiten bleiben im [Fehlerregister](../../../skills/ISSUES.md) einzeln sichtbar. Die Autorenskill-Validierung für CEM/SCXML/HTML ist weiterhin kein Ersatz für eine nachweislich abdeckende native Designprüfung.

## Anschließend umgesetzte Setup-Reparaturen

Der [neue Zusatzchecker](../../../../tools/design-review/README.md) liest FIG-Dateien erneut und prüft die belegten Lücken mit einem gemeinsamen, quellgebundenen Maßstab. Er akzeptiert den richtigen Platzhalter, erkennt falsche Konturstärke, prüft jede Optionsschriftgröße und vergleicht Farben nach ihrem Einsatz. Locks, Sichtbarkeit, Duplikate, Tokenabweichungen und Profilgrenzen sind ebenfalls abgedeckt. Er meldet ausschließlich seinen expliziten statischen Teilumfang und gibt keine Produktionsfreigabe.

Die [aktuelle Gegenprüfung run-01](static-countercheck-run01.json) und [run-02](static-countercheck-run02.json) findet in allen vier Originaldesigns dieselbe Platzhalterabweichung. B von run-02 hat zusätzlich drei Warnungen wegen der kopierten Konturfarbe. Das ist eine gemeinsame **begrenzte** Gegenprüfung, kein vollständiger Vier-Artefakt-Benchmark oder Ersatz der früheren Reviews.

Ein separater Prozessprüfer verlangt für künftige Vergleiche Rollen-/Prompt-/Skillangaben sowie klar getrennte Stop-/Resume-/Abschlussereignisse. Er kann fehlende historische Protokolle nicht wiederherstellen. Statischer Semantikadapter, Font-/Glyphnachweis und eine neue korrigierte Definitionsrevision sind weiterhin offen; sie werden nicht als repariert ausgegeben.

Aktuelle Regressionen und Integritätsnachweise: [setup-verification.json](setup-verification.json). Die ursprünglichen 32 Dateien von run-02 bleiben hashgleich.

## Abschließende Einordnung

**DeepSeek V4.1 Flash hat in diesem fortgesetzten Versuch zwei nutzbare, sehr ähnliche statische Designs geliefert.** Das ist ein positives Ergebnis für die grundsätzliche Tragfähigkeit der Definitionsbibliothek. Vollständige Definitionstreue ist wegen der gemeinsamen Farbabweichung nicht erreicht. Die vorhandene Bewertung überschätzt ihre Abdeckung; eine modellübergreifende Rangfolge ist daraus nicht ableitbar. Ein quellengebundener, mit Gegenfällen geprüfter begrenzter Prüfkern und ein standardisiertes Laufprotokoll sind anschließend ergänzt worden. Ihre Grenzen und die noch fehlenden Nachweise bleiben ausdrücklich offen.
