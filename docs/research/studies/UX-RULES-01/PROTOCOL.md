# Untersuchungsprotokoll · UX-RULES-01

## Ziel und Schreibgrenzen

Bestehende Semantik zuerst prüfen; eigenes Format erst nach belegter Lücke erwägen. Quellenarbeit und Proben liegen in dieser Studie, spätere Ausführungen in neuen Unterordnern von `runs/`. Keine alten Runs, Definitionen, Originalschemas oder Erwartungswerte passend machen. Änderungen der Prüferwartungen erhalten eine neue Revision und Begründung. Vor Ausführung einen Hash der Fälle, Baseline und konkreten Kandidateneingaben festhalten. Ein Aufruf zum Vergleich autorisiert keinen zusätzlichen Agenten oder externen Dienst.

Arbeitspräferenz aus dem Gespräch: lokal, dateibasiert, versionierbar und ohne verpflichtenden externen Dienst. Dies ist zunächst ein Bewertungskriterium; nicht behaupten, dass ein Kandidat es bereits erfüllt.

## Kriterien

| ID | Erforderlicher Nachweis |
| --- | --- |
| UX01 | Bedingungen, Operatoren, Typen und referenzierte Begriffe haben festgelegte Bedeutung; Textfelder allein genügen nicht. |
| UX02 | Eignung, Ausschluss, Voraussetzung und Alternative können auseinandergehalten werden; ein Zwecktext ist keine ausführbare Entscheidung. |
| UX03 | Pflicht, Empfehlung und Ausnahme werden unterschieden; Severity, Priorität, fachliche Verbindlichkeit und Freigabestatus nicht gleichsetzen. |
| UX04 | Fehlender Wert, null, false, nicht anwendbar, Fehler und fachlich ungeklärt werden erfasst; kein stilles Ja/Nein bei fehlender Evidenz. |
| UX05 | Mehrere zutreffende Regeln, Widerspruch und übersteuernde Ausnahme haben dokumentierte Behandlung. |
| UX06 | Bibliotheks-ID, Komponenten-ID, Revision/Hash und Ziel innerhalb eines Originalartefakts sind eindeutig bindbar. Gleicher Komponentenname genügt nicht. |
| UX07 | Veraltete und fehlende Bindungen werden erkannt; keine unbemerkte Umleitung auf latest oder Beispielquellen. |
| UX08 | Bibliotheksweite Regeln sind wiederverwendbar, lokale Regeln erkennbar; keine unbewiesene automatische Vererbung. |
| UX09 | Begründung, Beleg, Autorentscheidung, Status und offene Fachfrage bleiben nachvollziehbar; Logikausgabe und fachliche Wahrheit sind getrennt. |
| UX10 | Originalformat, Schema/Parser, semantischer Evaluator und eigene Adapter sind getrennt dokumentiert. |
| UX11 | Lokaler Betrieb, Lizenz, Installation, Export, reproduzierbare Version und Wartbarkeit sind praktisch prüfbar. |
| UX12 | Agent kann relevante Regeln gezielt finden, ohne ganze Bibliothek oder Handbuch einzulesen. Bytes und benötigte Dateien messen; tatsächliche Modellausführung separat. |
| UX13 | Die vier bestehenden Domänen bleiben führend; UX-Verweise duplizieren deren Werte/Behavior nicht als eigene Wahrheit. |

UX01 und UX06 sind Kernanforderungen. Eine Lösung mit nur Dateistruktur/Schemaprüfung scheidet als alleinige Regelbasis aus. Eine Kombination muss ihre eigenen zusätzlichen Regeln und Kosten offenlegen.

## Nachweisstufen

- **Dokumentiert:** Aussage an konkrete offizielle Quelle gebunden; lokal nicht ausgeführt.
- **Erprobt:** Originalartefakt plus gepinnter Evaluator und gespeicherte Eingabe/Ausgabe, Exitcode, Version und Hashes.
- **Eigener Adapter:** zusätzlich implementierte Bindungs-/Regellogik; niemals als native Frameworkfähigkeit zählen.
- **Hypothese/offen:** Eignungseinordnung, ungetestete Fähigkeit oder fehlender Nachweis. Unbekannt bedeutet nicht unmöglich.

Keine addierte Gesamtpunktzahl vor gleichen Proben. Kriterien werden pro Kandidat und ggf. Kombination mit Befund, Quelle, Artefakt und Grenze geführt. Ein technisches PASS beweist weder gute UX noch allgemeine Agentenzuverlässigkeit.

## Gemeinsamer Versuchsablauf

1. Repräsentative Fälle aus cases.json verwenden; die Vorschläge sind Testannahmen, keine neuen Produktregeln. Begriffe, Typen, Zustände und erwartete Ergebnisse vorher festlegen.
2. Für jeden Kandidaten Originalformat verwenden. Beispieldaten gehören zur Studie, nicht automatisch nach libraries/. Ein reines Metadatenschema nicht als ausführbare Semantik bewerten.
3. Dokumentieren, was der Kandidat selbst ausdrückt und was Kontextvokabular, Wrapper oder Evaluatorpolicy ergänzt. Auch manuell zu beurteilende Regeln als solche erhalten.
4. Dieselben vollständigen, unvollständigen, widersprüchlichen, fremden und veralteten Eingaben prüfen. Ergebnis mit zutreffender Regel-ID und Quellbezug verlangen.
5. Alle vier Contractdomänen mit passenden Zielstellen referenzieren. Datei-URI genügt nicht als Nachweis für Existenz, Typ, Revision oder Geltung eines Zieles.
6. Aufwand, Lesbarkeit, Größe und offene Grenzen vergleichen; erst danach Auswahlvorschlag und nötige schmale Integrationskonvention erarbeiten. Keine Komponentenmigration in dieser Runde.

## Weitere Kandidaten finden

Die sechs Startkandidaten sind keine erschöpfende Marktübersicht. Vor endgültiger Auswahl gezielt UX-spezifische Guideline-/Design-Rationale-Modelle und weitere maschinenlesbare Regelsprachen sichten. Aufnahme braucht Primärquelle, definiertes Modell/Format und eine klare Lücke gegenüber vorhandenen Kandidaten; bloße Dokumentationswerkzeuge genügen nicht. Aussortierte Ansätze mit Grund erhalten. Autorennotation, Austauschformat und Ausführung getrennt betrachten.
