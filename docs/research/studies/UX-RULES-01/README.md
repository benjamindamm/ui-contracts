# UX-RULES-01 · Formale UX-Regeln pro Komponente

Begonnen am 30. Oktober 2026 auf Nutzerauftrag. **Stand: zusätzlicher Quellensurvey und vier abgegrenzte Messblöcke dokumentiert; bedingter Vorschlag für eine DMN-Integrationsprobe, noch keine Formatentscheidung und kein vollständiger Frameworkbenchmark.** Eigenständiger Forschungsstrang; die abgeschlossene 16-Kandidatenrecherche und Reproduktionsstudien bleiben unverändert.

## Fragestellung und Erwartung

Welches bestehende Regelmodell eignet sich, um präzise festzuhalten, was eine Komponente aus UX-Sicht ausmacht, und diese Regeln eindeutig mit UI Contracts zu verbinden? Reine Prosa in YAML genügt nicht. Ein Dokumentationsfrontend wie Storybook ist nicht gesucht. Zweck, Eignung, Ausschlüsse, Voraussetzungen, Alternativen und Inhalts-/Kombinationsregeln sollen nachvollziehbar beschrieben werden; Bedingungen und Fachbegriffe benötigen definierte Semantik.

Pflicht, Empfehlung, Ausnahme, Ungewissheit, Konflikt und Freigabestatus dürfen nicht zusammenfallen. Regeln sollen pro Bibliothek und Komponente auffindbar sein, bei Bedarf genauer an Variante, Zustand oder Teil gebunden. Bestehende CEM-, DTCG/CSS-, SCXML- und HTML/ARIA-Quellen bleiben führend. UX-Regeln referenzieren diese, statt eine fünfte konkurrierende Beschreibung des Verhaltens zu erzeugen.

Die spätere Auswahl und Zusammenstellung ganzer UIs aus Nutzerzielen bleibt Perspektive. Kein Abnahmekriterium dieser ersten Runde: vollständige UI-Generierung, native Plattformen, neue Präsentationsoberfläche oder Migration produktiver Bibliotheken.

## Lesereihenfolge

1. [Protokoll und Anforderungen](PROTOCOL.md): Vergleichsmaßstab, Grenzen und Nachweisstufen.
2. [Erster Vergleich](COMPARISON.md): belegte Fähigkeiten, eigene Einordnung und offene Prüfungen getrennt.
3. [Gemeinsame Prüffälle](cases.json): identische Aufgaben für spätere Kandidatenproben; keine normativen Regeln der example-Bibliothek.
4. [Bindungsprobe](BINDING.md): vorhandene Komponentenrevision und zu prüfende Referenzanforderungen; kein beschlossenes neues Komponentenformat.
5. [Quellen](sources.json) und [Arbeitsstatus](tasks.json).
6. [Praktische Befunde](FINDINGS.md) und die dort verlinkten unveränderten Messblöcke.

## Erhaltener erster Quellenvergleich

Sechs Ansätze sind anhand offizieller Quellen eingeordnet. DMN, SBVR, SHACL und OPA/Rego werden für vertiefte Proben priorisiert; ODRL bleibt gezielter Vergleich für Pflichten und Konflikte, MBUI/CTT eine Referenz für spätere Aufgabenmodelle. Das ist eine Arbeitsreihenfolge, kein Ausschluss und keine Rangfolge. Die Beiträge sind verschieden; eine kleine Kombination kann geeigneter sein als ein einzelner Gesamtsieger.

## Erhaltene erste Messblöcke

[Zusätzliche Ansätze](ADDITIONAL-APPROACHES.md) ergänzen die Suche um UGL/GDL, ACT, EARL und die getrennt zu betrachtende klinische GDL. [Befunde und Fehlerquellen](FINDINGS.md) führen die eigentliche Auswertung.

- [Lauf 01](runs/01/README.md): 39 Checks, 38 Erwartungen erfüllt; FEEL, Rego, SHACL, Originalschemas und eigener Komponentenbinder. Ein Fehler in der eigenen Rego-Proberegel bleibt erhalten.
- [Lauf 02](runs/02/README.md): separate Korrektur, 6/6 Erwartungen erfüllt. Keine unabhängige Reproduktion und keine nachträgliche Änderung des Erstlaufs.
- Die zwölf gemeinsamen Fälle sind nur teilweise abgedeckt. Pflicht-/Empfehlungslogik, vollständige Ausnahmebehandlung, gemeinsame/lokale Regeln und Agentennachladen bleiben offen. Kein vollständiger DMN- oder SBVR-Engine-Nachweis.

[Prüfumfang und Integrität](measurement-consistency.json). Der frühere consistency-check.json beschreibt ausschließlich den ersten dokumentarischen Stand vor diesen Proben; seine alten Dateihashes sind keine aktuellen Dokumenthashes.

## Praxisbezug

Der Nutzer berichtet, mehrere private Komponenten mit dem Framework erfolgreich erstellt zu haben. Diese Dateien sind hier nicht verfügbar. Das ist berichtete Praxiserfahrung, kein unabhängiger Nachweis und keine Stichprobe dieser Untersuchung. Es werden keine privaten Dateien benötigt oder als geprüft ausgegeben.

Die Forschungs-JSONs beschreiben nur Quellen, Fälle, Baseline und Aufgaben dieser Studie. Sie sind weder eine neue UX-Regelsprache noch bereits eingebundene Komponenten-Contracts. Bibliotheken und installierte Skills wurden für diese Studie nicht verändert. Kein Commit oder Push ohne separaten Auftrag.

## Folgeblock: konkrete Empfehlung

[Lauf 03](runs/03/README.md) ergänzt native DMN-XML-Ausführung, Pflicht-/Empfehlungs-/Ausnahmefälle und gemeinsame/lokale Regeln in DMN und Rego: 33/33 Erwartungen erfüllt. [Lauf 04](runs/04/README.md) grenzt ODRL anhand von Quellen und drei Kodierungsproben ab; keine ODRL-Policy wurde ausgewertet.

[Werkzeuge, gemessene Größen und Integrationsaufwand](TOOLING-AND-COST.md) · [Empfehlung für eine erste echte Komponentenprobe](RECOMMENDATION.md) · [Integritätsprüfung dieses Folgeblocks](followup-consistency.json).

Arbeitsvorschlag: DMN/FEEL zuerst mit einem schmalen eigenen Komponenten-/Evidenzprofil erproben; Rego als getestete Alternative behalten. Kein neuer Standard beschlossen und keine Änderung der Bibliotheken/Skills. Die weiterführende SBVR-Semantikprobe und ein umfassender Vergleich aller Fälle in allen Kandidaten bleiben offen. Technisch gezieltes Laden ist kein Agentenverständnisnachweis. Aufgabenstatus: sechs Arbeitspakete im dokumentierten Umfang erledigt, zwei noch begonnen/offen.

[Fallweise Abdeckung statt pauschalem PASS](coverage.json): Alle zwölf Fälle sind eingeordnet; mehrere nur teilweise oder durch eigene Adapter, kein vollständiger Benchmark aller Kandidaten.

## Erster komponentengebundener Pilot ausgeführt

[AC-UX-01](pilots/AC-UX-01/README.md) bindet drei konkrete Autocomplete-UX-Regeln an die unveränderte example-Revision. DMN führt die tatsächlichen Faktenbedingungen aus, der native Zeilentrace wird auf Regel-ID und Belege abgebildet. **43/43 Prüfungen erfüllt** bei elf Kontextauswertungen und 17 vorgelagerten Gegenfällen. Profile, Vokabular und Adapter bleiben separate Forschungskandidaten; kein universeller Standard und keine Änderung von libraries/ oder Skills. Keine Agenten-Leseprobe ausgeführt.

## Auswahlstudien und fachliche Verfeinerung

- [SELECTION-01](studies/SELECTION-01/README.md): zwei frische Builder, drei vs. 30 Vorwahlen; beide folgen der damaligen Policy. Zwei B-Erstfehler sind erhalten und separat repariert. Das unvollständige Kandidatenangebot begrenzt das Ergebnis.
- [UX-Eignung von Autocomplete](../../../ux/AUTOCOMPLETE.md): fachliche Nutzeranforderungen zu Schreibhilfe, freien Adressen und festen Werten. Keine allgemeine empirische UX-Regel.
- [SELECTION-02](studies/SELECTION-02/README.md): neue Kandidatenrevision mit Select mit Suche und getrennten Angaben für Wertevertrag/Suchoberfläche. Historische Eingaben bleiben erhalten.

Die frühere Aussage „Bibliothek unverändert“ beschreibt den damaligen AC-UX-01-Pilotzeitpunkt. SELECTION-01 erweitert die Live-Bibliothek; die ältere Revision wird in dessen prior-library unverändert bewahrt und reproduziert. SELECTION-02 führt nochmals eine separate Kandidatenkopie, ohne die erste Studienbindung zu ändern.
