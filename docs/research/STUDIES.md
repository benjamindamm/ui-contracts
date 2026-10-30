# Studien

Nachfolgende Studien bauen auf der abgeschlossenen Kandidatenrecherche auf. Sie haben eigene Fragestellungen, Eingabeversionen und Auswertungen. Die früheren 702 Bedingungen in 106 Gruppen bleiben ein getrennter Forschungsstand und werden nicht als Stichproben dieser Studien ausgegeben.

| Studie | Frage | Modell / Reasoning | Ergebnis / Stand |
| --- | --- | --- | --- |
| [AC-R01 · Autocomplete-Reproduzierbarkeit](studies/AC-R01/README.md) | Erzeugen zwei Agenten mit leerem Kontext aus derselben Definition konforme und vergleichbare editierbare OpenPencil-Designs? | GPT-6.1 Sol / Medium¹ | Abgeschlossen: alle erfassten normalisierten Komponentenwerte stimmen überein; beide Designs **FAIL** wegen derselben falschen deaktivierten Platzhalterfarbe (#94A3B8 statt #64748B). |
| [AC-R02 · Lauf mit externer Analyse](analyses/AC-R02/README.md) | Wie belastbar sind die Ergebnisse und ihre Prüfung für künftige Modellvergleiche? | DeepSeek V4.1 Flash² | Zwei ähnliche editierbare Designs nach je zwei Limitunterbrechungen. Originalurteil: PASS_MIT_ABWEICHUNGEN; externe Analyse: gemeinsame explizite Farbabweichung und Prüflücken. Keine neue formale Studie. |
| [AC-R03 · Originaler Laufbericht](../../examples/autocomplete/reproducibility/run-03/README.md) | Erneute unabhängige statische Erzeugung und Prüfung derselben Definition | [qwen3.8-27B · FP8](studies/AC-R03/MODEL-PROVENANCE.json), nachträgliche Nutzerangabe vom 29.10.2026; nicht je Rolle technisch verifiziert. Ursprünglich als `local:default` dokumentiert | Lauf abgeschlossen. Internes Urteil: beide „Substanziell erfüllt“; B mit Platzhalterabweichung und Reportwiderspruch, gemeinsame A11Y-Befunde und vier HTTP-413-Abbrüche dokumentiert. Noch keine vollständige externe Bewertung. |
| [AC-R04 · Externe Prüfung](analyses/AC-R04/README.md) | Zwei Erzeugungen mit Rollenaufträgen und Bootstrap; nachträgliche PNG-Vorschauen | Konfiguriertes Default-Modell, Identität nicht ermittelt | Begrenzte Gegenprüfung erneut bestanden, 572/572 Paarwerte gleich; ursprüngliches Reviewer-Readback reproduziert. Fachliche Teilaufgabenzerlegung und kausaler Setupvergleich noch nicht belegt. |

¹ Nachträgliche Nutzerangabe vom 29. Oktober 2026 zur Konfiguration des Laufs; nicht gegen historische Laufzeitprotokolle verifiziert. Separate Modellangaben je Builder und Prüfer sowie exakte Modellrevision und Seeds fehlen.

² Nutzerangabe vom 29. Oktober 2026; Modellname, Reasoning und Konfiguration je Rolle fehlen im ursprünglichen [Laufprotokoll](../../examples/autocomplete/reproducibility/run-02/run.json). Die externe Analyse ergänzt die Einordnung, ohne run-02 zu verändern.

Das Register dient auch dem künftigen Vergleich über Modelle hinweg. AC-R01 und AC-R02 verwenden dieselbe Definition und Werkzeugbindung, aber unterschiedliche Prüfkriterien und Urteilslogiken; ihre Originalurteile erlauben keine Modellrangfolge. Ein vollständiger gemeinsamer Benchmark aller vier Designs steht aus. Weitere Läufe werden mit eigener Lauf-ID, Modell-/Reasoning-Angaben je Rolle, Definitionsrevision, Werkzeugbindung und unabhängig geprüftem Ergebnis ergänzt; Übereinstimmung und Definitionstreue bleiben getrennte Ergebnisse.

## Beschlossener nächster Forschungsschritt

[RD-001 · Gestufte Erzeugung mit prüfbaren Übergaben](decisions/RD-001-STAGED-GENERATION.md), beschlossen am 29. Oktober 2026: Komplexität über Teilverträge und explizite Komposition beherrschen; Erzeugung in persistierte Zwischenstände gliedern und unabhängige Prüfung mit begrenzten Reparaturrunden verbinden. Ziel ist zuverlässigere Arbeit auch mit weniger leistungsfähigen Modellen, keine bereits belegte Verbesserung.

Das [Pilotprotokoll](protocols/STAGED-GENERATION-PILOT.md) sieht zuerst dieselbe eingefrorene Autocomplete-Definition, zwei Erzeugungen je Kontroll-/Stufenarm und eine gemeinsame Prüfpolicy vor. Modellkonfiguration, Budgets, Helper und vollständige Messabdeckung müssen vor Ausführung festgelegt werden. Eine komplexere Komponente folgt erst danach. Der Pilot ist geplant, nicht gestartet; historische Läufe und Forschungszähler bleiben unverändert.

## UX-RULES-01 · Formales UX-Regelmodell

[Neuer Forschungsstrang ab 30. Oktober 2026](studies/UX-RULES-01/README.md): Regeln pro Komponente, eindeutige Bibliotheks-/Revisions-/Contractbindung und formale Semantik statt Prosa in YAML. Erstvergleich, zusätzlicher Survey und zwei praktische Teilblöcke dokumentiert; eigener Rego-Fehler erhalten und separat korrigiert. Zwölf gemeinsame Fälle noch nicht vollständig abgedeckt; keine Formatentscheidung. Aufgaben und Zähler bleiben getrennt von den historischen Studien.

UX-RULES-01-Folgeblock: [native DMN-/Regelzusammenspielproben](studies/UX-RULES-01/runs/03/README.md) und [bedingter Auswahlvorschlag](studies/UX-RULES-01/RECOMMENDATION.md) vorhanden; keine produktive Migration oder vollständige SBVR-Ausführung.

[AC-UX-01 · erster komponentengebundener UX-Pilot](studies/UX-RULES-01/pilots/AC-UX-01/README.md): drei Regeln, native DMN-Zeilennachverfolgung, 43/43 Checks; keine Agentenstudie und keine Veränderung der ursprünglichen Reproduktionsläufe.

## Auswahl von Komponenten

[SELECTION-01](studies/UX-RULES-01/studies/SELECTION-01/README.md) belegt die Anwendung einer gesetzten Auswahlpolicy in zwei Fällen; zwei Implementierungsfehler sind erhalten und separat repariert. [SELECTION-02](studies/UX-RULES-01/studies/SELECTION-02/README.md) ergänzt auf Nutzerhinweis Select mit Suche. Beide Studien bleiben getrennt; gute Policyanwendung ist kein Nachweis optimaler UX.
