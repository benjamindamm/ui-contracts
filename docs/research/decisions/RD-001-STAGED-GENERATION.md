# RD-001 · Gestufte Erzeugung mit prüfbaren Übergaben

**Status: beschlossen · 29. Oktober 2026 · Nutzerentscheid.**

## Entscheid

UI Contracts entwickelt den Forschungsansatz von weitgehend zusammenhängenden Erzeugungsaufträgen zu einem **gestuften, quellengebundenen Arbeitsablauf** weiter. Komplexe Komponenten werden über Teilverträge und explizite Kompositionsregeln beschrieben. Die Erzeugung wird durch kleine, persistierte und prüfbare Übergaben strukturiert. Unabhängige Prüfungen und begrenzte Reparaturrunden gehören zum vorgesehenen Ablauf.

**Präzisierung des Entwicklungsziels:** Verbessert werden primär die wiederverwendbaren Skills und ihre Auftrags-/Wissensübergaben. Die Forschungsläufe sind die Evaluation dieser Verbesserung. Umgesetzt sind [fokussierte Rollen](../../../skills/ui-contracts/references/workflow.md), ein [gemeinsamer Übergabevertrag](../../../skills/ui-contracts/references/handoff-contract.md) und ein struktureller Kontext-/Integritätsprüfer. Dessen Funktionstests ersetzen keinen Modell-Verhaltenstest.

Ziel ist, auch mit weniger leistungsfähigen Modellen brauchbare und nachvollziehbar geprüfte Ergebnisse zu erhalten. Der Prozess darf Fehler auffangen; Erstleistung, Unterstützung und Endqualität werden deshalb getrennt gemessen. Die Wirksamkeit dieser Weiterentwicklung ist **noch zu untersuchen**, kein bereits erzieltes Forschungsresultat.

## Ausgangslage und Befundstatus

| Grundlage | Einordnung |
| --- | --- |
| [AC-R01](../studies/AC-R01/README.md) | Zwei ähnliche native Designs, gemeinsame explizite Platzhalterfarbabweichung. |
| [Externe Analyse AC-R02](../analyses/AC-R02/README.md) | Ähnliche Designs; falsche Quellauslegung und nachgewiesene Lücken des damaligen Prüfers. Aktuelle Gegenmaßnahmen und Regressionen liegen vor. |
| [run-03](../../../examples/autocomplete/reproducibility/run-03/README.md) | Laut laufinternem Review brauchbare statische Designs; A trifft die Platzhalterfarbe, B nicht und widerspricht dazu seinem Bericht. Vier HTTP-413-Abbrüche sind dokumentiert. Noch keine vollständige externe Gegenprüfung dieses Laufs. |
| Modell- und Prozessvergleiche | Unterschiedliche Kriterien, unvollständige Rollenmetadaten und Fortsetzungen verhindern eine belastbare Rangfolge aus den bisherigen Originalurteilen. |

Ein HTTP-413-Eintrag belegt hier keine genaue Kontext- oder Proxygrenze. Fehlerantworten und tatsächliche Anfragegrößen fehlen als Rohbelege. Kontextumfang, Modellfähigkeit, API-Anfragegröße und Harness-Schrittlimit sind verschiedene Größen; sie werden künftig getrennt erfasst. Die Behauptung, alle Abbrüche seien allein durch zu lange Kontexte verursacht, ist nicht belegt.

## Festgelegte Prinzipien

1. **Vier führende Domänen bleiben bestehen:** technisches Interface, Visual, Behavior, Accessibility. Keine neue universelle Zwischensprache ersetzt diese Originalquellen.
2. **Teilkomponenten plus Zusammenspiel:** Autocomplete bleibt Eigentümer von Query, aktivem Ergebnis und bestätigtem Wert gemäß Definition. Overlay verantwortet seine definierten Darstellungs-/Lebenszyklusaufgaben, ScrollArea ihren Viewport. Verbindungen werden an Instanz, Teil, Ereignis und Zustand gebunden; Namensgleichheit reicht nicht.
3. **Übergaben sind abgeleitete Arbeitsmittel:** Sie enthalten Quellenpfade, Hashes, Auszüge/Verweise, Entscheidungen und offene Fragen. Bei Widerspruch gilt die führende Quelle; eine Zusammenfassung wird nicht zur fünften Wahrheit.
4. **Technische Mechanik wiederverwenden:** Tokenauflösung, Export, Readback und Messungen möglichst über geprüfte Hilfsfunktionen statt ständig neu erfundener Skripte erledigen. Fachliche Regeln bleiben in der Definition und ihrer ausdrücklich begrenzten Prüfpolicy.
5. **Prüfen und Erzeugen trennen:** Gegen Originalartefakte messen, Berichte anschließend abgleichen. Gemeinsamer Prüfkern für Modellvergleiche; modellspezifisch abgeleitete Kriterien separat untersuchen.
6. **Reparaturen begrenzen und sichtbar halten:** Erstlieferung unverändert behalten; jede Korrektur als eigene Revision mit Fehlerdiagnose und Nachprüfung. Stärkere Modellhilfe wird ausdrücklich als zusätzliche Unterstützung ausgewiesen.
7. **Kontext aktiv begrenzen:** Rohdaten auf Datenträger, gezielte Ausschnitte in Anfragen, Wiederaufnahme über Checkpoints. Originalquellen bleiben zugänglich; Kompaktheit darf Regeln nicht unterschlagen.

## Abfolge und Nachweise

| Stufe | Dauerhaftes Ergebnis | Gate vor dem nächsten abhängigen Schritt |
| --- | --- | --- |
| 0 · Versuchsrahmen | Eingabemanifest, Modell-/Rollenmetadaten, Aufträge, gemeinsame Prüfpolicy, Budgets | Hashes/Revision reproduzierbar; Umfang und Messlatte festgelegt. |
| 1 · Quellenzuordnung | Teile-/Zustands-/Quellenkarte, Konflikt- und Fragenliste | Alle geforderten Teile und Fälle zugeordnet; verbindliche Regeln nicht als Freiheit umgedeutet. |
| 2 · Minimale vollständige Lieferung | Native Datei mit allen geforderten statischen Fällen, Export-/Readback-Receipt | Lesbar, getrennt editierbare Strukturen, Fälle vollständig; vorhandene Fehler dürfen sichtbar bleiben. |
| 3 · Unabhängige Abnahme | Messwerte, Soll-/Ist-Diagnosen, Umfang/ungeprüfte Teile, Reportabgleich | Nur tatsächlich abgedeckte Aussagen bewerten; Erstleistung einfrieren. |
| 4 · Gezielte Reparatur | Neue Artefaktrevision und erneuter Prüfbericht | Vorherige Verletzungen plus betroffene Regressionen erneut prüfen. |
| 5 · Abschluss | Erst-/Endergebnis, Aufwand, Unterstützung und verbleibende Grenzen | Keine Vollfreigabe aus nur statischer Teilprüfung. |

Diese Stufen sind Arbeitsgrenzen, **keine automatische Aufforderung, zusätzliche Agenten zu starten**. Ein Agent kann mehrere Stufen bearbeiten; die unabhängige Prüfung braucht einen getrennten Bewertungskontext. Der nächste Versuch legt die konkrete Sessionaufteilung vorab fest.

## Skalierung auf komplexere Komponenten

Nicht jede mögliche Kombination von Teilzuständen wird als neues Design verlangt. Abgedeckt werden lokale Pflichtfälle sowie gezielte Kompositions-/Übergangsfälle: Ereignisübernahme, Ownership, Fokus, Auswahl/Commit, Overlay-Lifecycle, Scrollsichtbarkeit und Fehler-/Abbruchpfade. Für jede Verbindung ist ein zuständiger Vertrag und ein beobachtbarer Akzeptanzfall zu benennen. Zustandsnamen und Szenenbilder allein beweisen diese Verbindungen nicht.

Statisches OpenPencil bleibt zunächst das Erzeugungsziel. Dynamische Übergänge können darin nur als beschriftete Zustandsfolge/Annotation dokumentiert werden. Tatsächliche Events, Fokus und Scrollen müssen später im ausführbaren Ziel geprüft werden; der bestehende fest gebundene Webforschungs-Host ist kein allgemeiner Resolver. iOS/Android bleiben Zukunftsperspektive.

## Nächster beschlossener Entwicklungsschritt

Zuerst das [Versuchsvorgehen für Autocomplete](../protocols/STAGED-GENERATION-PILOT.md) vorbereiten und an der **unveränderten eingefrorenen Definition** untersuchen. Dabei erhält auch die Kontrollbedingung dieselben technischen Hilfsmittel und denselben Prüfkern. Erst anschließend die Übertragbarkeit an einer separat gewählten komplexeren Komponente untersuchen.

Beschlossen sind Richtung und Vorgehen; die ersten Skill-/Übergabeverbesserungen sind implementiert und funktional geprüft. **Noch nicht ausgeführt oder freigegeben:** neuer Generierungslauf, universeller Resolver, neue Definitionsrevision, neue native Plattformprüfung oder externe Veröffentlichung. Modellnamen und konkrete Laufbudgets werden vor dem Pilot separat als überprüfbare Konfiguration festgelegt. Für run-03 hat der Nutzer nachträglich **qwen3.8-27B in FP8** angegeben; die [separate Herkunftsergänzung](../studies/AC-R03/MODEL-PROVENANCE.json) bewahrt diese Angabe, ohne daraus eine technische Verifikation jeder Rolle abzuleiten.

## Erfolg, Grenzen und Konsequenzen

Erwartet werden weniger verlorene Arbeit, klarere Fehlerdiagnosen und bessere Endergebnisse bei kontrolliertem Unterstützungsaufwand. Mehr Dateien oder mehr Agenten sind kein Erfolgskriterium. Gemessen werden Regelverletzungen der Erstlieferung, verbleibende Fehler nach Reparatur, vollständige Lieferungen, Anfragegrößen, Abbrüche, Aufwand und Eskalationen.

Die zusätzlichen Übergaben können ihrerseits Regeln verlieren oder verfälschen. Sie brauchen deshalb Herkunft und Rückverweise. Ein Prüfer kann systematisch falsch urteilen; Gegenfälle und gemeinsame Policy bleiben notwendig. Ein repariertes Endergebnis ist keine ununterstützte Modellleistung. Ein kleiner Autocomplete-Pilot beweist keine allgemeine Skalierbarkeit.

Historische Eingaben, Kriterien und run-01/02/03 bleiben unverändert. Bekannte Fehler werden im [Fehlerregister](../../skills/ISSUES.md) weitergeführt. Der Entscheid eröffnet eine neue Forschungsphase und verändert keine Zähler der abgeschlossenen Kandidatenrecherche.

[Operatives Pilotprotokoll](../protocols/STAGED-GENERATION-PILOT.md) · [Laufmetadatenvertrag](../../skills/REPRODUCIBILITY.md) · [Aufgaben](../../../TASKS.md)
