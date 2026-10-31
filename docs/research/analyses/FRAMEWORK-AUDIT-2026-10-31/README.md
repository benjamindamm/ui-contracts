# Framework-Audit · 31. Oktober 2026

**Urteil:** UI Contracts ist eine brauchbare, in Teilumfängen erprobte Grundlage für agentengestützte Komponentenarbeit. Für ein belastbares allgemeines UX-/Designhandbuch fehlen vor allem die durchgängige Verbindung der Bausteine und komponentenunabhängige Nachweise. Der größte aktuelle Fehlerpfad: Eine formal gültige UX-Fähigkeitsbehauptung kann zu einer fachlich falschen Auswahl führen, obwohl ihre verlinkten Originaldateien unverändert sind.

[13 priorisierte Befunde und Abnahmekriterien](findings.json) · [Ausgeführte Prüfungen](evidence/suite-counts.json) · [Inventar](evidence/inventory.json) · [Quell-/Belegbindung](receipt.json)

## Umfang und Aussagekraft

Ausgangsstand: Commit `fe44c53876f4f77c3e95222ee5b1ea118eb87d76`. Frameworkweit geprüft wurden Einstieg, Rollen/Übergaben, aktive Bibliothek, vier Domänen und eigene Bindungen, UX-Profile/Policy, Originalformat-/Zielprüfer, Ressourcen, OpenPencil-Präsentation, Chartgeometrie sowie Forschungsprovenienz und Übernahme neuer Ergebnisse.

Das Inventar umfasst **2.410 getrackte Dateien**. Das bedeutet nicht, dass jede Zeile aller historischen Experimente neu gelesen oder jeder Versuch wiederholt wurde. Führende aktuelle Dateien, zentrale Implementierungen und relevante historische Gegenbefunde wurden gezielt untersucht. **38 aktive Markdown-Dateien mit 261 lokalen Links:** keine fehlenden Linkziele. Anker innerhalb von Markdown und externe Links wurden nicht neu geprüft. Eingeschränktes Musterinventar statt pauschaler Behauptung vollständiger Dokumentkonformität.

Es gab keinen neuen unabhängigen Agenten-/Modellvergleich und keinen neuen Browser-/Screenreaderlauf. Vorhandene Browserstudien wurden anhand ihrer Berichte und Rohdaten eingeordnet. Die neuen Gegenfälle liefen ausschließlich in temporären Kopien. Historische Quellen und Ausgaben wurden nicht umgeschrieben; Produktcode wurde in diesem Audit nicht repariert.

## Was stabil funktioniert

- **Vier getrennte führende Domänen:** CEM, DTCG/CSS, SCXML und HTML/ARIA bleiben unterscheidbar. Zielimplementierung und Designexport werden nicht als zusätzliche führende Wahrheit behandelt.
- **Bibliotheksauswahl und Quellschutz:** separate Bibliotheken, explizite Auswahl, Hashbindungen, erhaltenes historisches Archiv und zahlreiche negative Pfad-/Versionsfälle.
- **Gezielter Agenteneinstieg:** kleine AGENTS-/Claude-/Gemini-Wegweiser, Rollenkarten und begrenzte Bootstrap-/Kontextpakete. Installierter und Repository-Skill stimmen im ausgeführten Dateivergleich überein; dies ist keine Messung des gesamten tatsächlichen Modellrequests.
- **Konkrete Werkzeugbelege:** Schriftdateien, Chartsektoren und native Präsentation haben tatsächliche Reader-/Writer-/Render- bzw. Metadatenprüfungen und Gegenfälle.
- **Ehrliche Nachweisgrenzen:** neue Komponenten erhalten keine pauschale Freigabe. Die neue Live-Library-Inspektion endet korrekt mit `BLOCKED / SEMANTIC_PROFILE_UNSUPPORTED`; die statische feste Referenz besteht begrenzt.

### Aktuell erneut ausgeführte Regressionen

| Bereich | Erwartungen erfüllt |
| --- | ---: |
| Bibliotheken / Migration / Auswahl | 19/19 |
| Fontassets / Tokenbindung | 20/20 |
| Rollenaufträge / Kontext / Übergaben | 37/37 |
| Nativer Autocomplete-Gegenprüfer | 12/12 |
| Prozessmetadaten | 7/7 |
| Chartgeometrie und vorhandener FIG-Proof | 15/15 |
| Präsentationslayout / Themes | 25/25 |
| Statische Prüfkette: positive/negative Gegenfälle | 47/47 |
| **Summe** | **182/182** |

Das sind **135 Tests aus sieben Suiten plus 47 Gegenfälle**, keine 182 unabhängig repräsentativen Komponenten. Die neuen Audit-Gegenbeispiele zeigen ausdrücklich, welche Probleme diese bestehenden Suiten noch nicht abdecken. Erfolgreiche Regressionen sind kein Beweis allgemeiner Richtigkeit. Die abschließende Ausgabe des statischen Regressionstreibers wurde in den Auditordner umgeleitet; seine Prüfungen/Mutationen liefen unverändert in ihren temporären Kopien. Alte Belegdateien wurden dadurch nicht ersetzt.

## Fünf Punkte zuerst

### FW-001 · P1 · UX-Fähigkeiten können die Prüfung überlisten, ohne dass jemand betrügen muss

**Belegt durch einen ausgeführten Gegenfall.** In einer temporären Kopie erhielt das einfache Select in `ux.json` statt `searchMode: none` den schemaerlaubten Wert `query-provider`. Ein neues Manifest band diese neue Revision ehrlich. Interface, Verhalten und Accessibility-Dateien blieben bytegleich, ihre Quellenhashes stimmten weiterhin.

Der unveränderte Auswahlhelper empfahl anschließend für 30 Optionen **Select statt Autocomplete**. Er wusste nicht, dass das tatsächliche Select weiterhin kein Suchfeld und keinen Filtervertrag hat. Beide Auswertungen bleiben ausdrücklich `release:false`; es wurde keine vollständige Komponentenfreigabe umgangen. Trotzdem kann der Empfehlungswert einen Agenten fehlleiten.

**Ursache:** Schema und Hashes prüfen die Form bzw. die Identität der Behauptung und ihrer Referenzen, nicht die Bedeutung der behaupteten Fähigkeit. `sources` enthält noch keinen hinreichenden fachlichen Nachweis jeder Eigenschaft.

**Nächste Verbesserung:** Behauptete und tatsächlich für einen definierten Umfang geprüfte Fähigkeiten unterscheiden. Für entscheidungsrelevante Eigenschaften wie Suche, freie Werte oder Mehrfachauswahl kleine positive/negative Contractfälle und konkrete Quellanker verlangen. Es braucht dafür zunächst keinen universellen semantischen Beweiser.

[Konkrete ursprüngliche und veränderte DMN-Antwort](evidence/capability-counterexample.json) · Quelle: `SELECTION-01/evaluate.py`, insbesondere Zeilen 14–21.

### FW-002 · P1 · Neueste Forschung ist noch nicht das aktive Framework

Die neue UX-Leitlinie bevorzugt im festen Vorwahlfall Select mit separater Suche. `libraries/example/library.json` und die aktive `selection-policy.json` enthalten jedoch weiterhin nur die frühere Auswahl zwischen Select und Autocomplete. **SelectWithSearch und die neueren UX-Merkmale liegen ausschließlich in der SELECTION-02-Kandidatenbibliothek.**

Ein Konsument, der regulär die aktive Bibliothek verwendet, kann deshalb zur inzwischen fachlich weniger passenden alten Empfehlung kommen. Das ist keine Unredlichkeit der Studie – deren Grenzen sind dokumentiert –, aber eine reale Integrationslücke im Framework. Eine veraltete Existenznotiz in der Studienkopie wurde bereits als SEL2-D01 erkannt und ist bislang nur durch externe Errata eingeordnet.

**Nächste Verbesserung:** Forschungsergebnis ausdrücklich in eine neue aktive Revision übernehmen, widersprüchliche Notizen dort korrigieren und neue Quellenbindungen erstellen. Für jede Fähigkeit sollte auffindbar sein: vorgeschlagen, im Kandidaten geprüft, aktiv übernommen oder verworfen. Historische Definitionen und Erwartungen dürfen dabei nicht geändert werden.

[Aktives Komponenteninventar](evidence/inventory.json) · [Folgestudien-Errata](../../studies/UX-RULES-01/studies/SELECTION-02/ERRATA.md).

### FW-003 · P1 · Neue Komponenten werden noch nicht hinreichend zusammenhängend geprüft

`inspect` prüft unter anderem JSON, das vorhandene CEM-Schema und das lose SCXML-XSD. Es besitzt noch keinen allgemeinen Validator für den gesamten eigenen Komponenten-/Kompositionsvertrag. Ein ausgeführter Gegenfall mit lauter fehlenden Domänendateien erzeugt keinen präzisen Fehler für diese fehlenden Ziele; er bleibt unter der allgemeinen Semantikblockierung. Positiv: Er wird nicht als vollständig gültig freigegeben.

Die umfassendere Referenzkette prüft eine andere, festgelegte Paketstruktur. Selbst die Werkzeugbereitschaft der allgemeinen Inspektion wird derzeit durch einen Test des historischen IP-01-Referenzpakets festgestellt. Autorenwerkzeug und historische Forschungsreferenz sind dadurch unnötig eng gekoppelt.

**Nächste Verbesserung:** Den bereits verwendeten eigenen Mindestvertrag versionieren und einen bibliotheksbezogenen Referenz-/Identitäts-/Typprüfer hinzufügen. Quellenexistenz, Partziele, Zustands-/Eventbezüge und Quellführung müssen für neue Controls konkret überprüfbar werden. Originalschemas bleiben dabei unverändert; für noch nicht unterstützte Semantik bleibt Blockierung richtig.

[Gegenfall fehlender Referenzen](evidence/dangling-reference-inspect.json) · [Aktuelle Library-Inspektion](evidence/live-library-inspect.json).

### FW-004 · P1 · UX-Regelausführung ist noch nicht sauber aus einem Clone startbar

Die ausführbaren UX-Proben verweisen auf `/tmp/ui-contracts-ux-rules-runtime`, dort vorbereitete Java-Klassen/JARs und `/opt/homebrew/opt/openjdk/bin/java`. Auf diesem Rechner laufen sie, weil die vorbereitete Laufzeit vorhanden ist. Die Links und Quelltexte allein bieten jedoch noch keinen einheitlichen operativen Einstieg für einen neuen Konsumenten.

Dies ist durch Quellprüfung belegt; ein neuer leerer Rechner wurde **nicht** getestet. Auch die große Zahl vorgehaltener historischer Werkzeug-Locks ersetzt keinen gemeinsamen Setupweg.

**Nächste Verbesserung:** Einen konfigurierbaren, gepinnten UX-Runner mit dokumentierter Bereitstellung und strukturierten Fehlern bei fehlenden Voraussetzungen ergänzen. Nicht die alten Proben passend zum neuen Werkzeug umschreiben. Ein frischer Clone-Test gehört zur Abnahme dieses neuen operativen Wegs.

Quellen: `SELECTION-01/evaluate.py:22`, `SELECTION-02/preflight/check-policy.py:12–15`, `AC-UX-01/evaluate.py:64–65`.

### FW-007 · P1 · Richtige Komponentenwahl garantiert keine richtige Umsetzung

Die tatsächlichen Studien fanden fehlende Input-Ereignisse, alte Erfolgsmeldungen und Fokusverlust. Diese Fehler wurden separat repariert, obwohl die fachliche Komponentenwahl jeweils der gesetzten Policy entsprach. Die SCXML-Datei und eine daraus manuell übertragene TypeScript-Implementierung sind nicht automatisch identisch.

Die bestehenden starken Laufzeitnachweise betreffen die fest gebundene Webreferenz und konkrete zusätzliche Studienprüfungen. Ein neues Control erhält daraus noch keine wiederverwendbare allgemeine Adapterabnahme.

**Nächste Verbesserung:** Für jeden unterstützten Komponententyp verpflichtende Contractfälle bereitstellen, die tatsächliche Events, Fokus, Scrollen und bestätigte Formularwerte prüfen. Wo möglich dieselben relevanten Eingabefolgen gegen SCXML und Zieladapter vergleichen. Ein Agent darf frei implementieren; er braucht danach eine gemeinsame belastbare Messlatte.

[SELECTION-01-Prüfbericht](../../studies/UX-RULES-01/studies/SELECTION-01/review/REVIEW.md) · [SELECTION-02-Prüfbericht](../../studies/UX-RULES-01/studies/SELECTION-02/review/REVIEW.md).

## Weitere Schwächen beim Skalieren

| ID | Priorität | Schwäche und praktische Folge | Sinnvoller nächster Schritt |
| --- | --- | --- | --- |
| FW-005 | P2 | Kein gemeinsamer Regressionseinstieg und kein getrackter CI-Workflow. Prüfungen können beim Weiterentwickeln leicht vergessen werden; einzelne Standardbefehle ersetzen aktuelle Belegdateien. | Ein gemeinsamer Testbefehl mit explizitem frischem Ausgabeziel; anschließend dieselbe Auswahl automatisieren. |
| FW-006 | P2 | Gesamtmanifeste sind sicher, aber grob: Auch Dokumentations-/Assetänderungen machen eine neue Bibliotheksrevision. Ein genereller Abhängigkeits-/Impactplan fehlt. | Komponentenabschluss, Bibliotheksrelease und betroffene Verbraucher/Nachweise getrennt darstellen. Pins nicht lockern. |
| FW-008 | P2 | Das UX-Auswahlmodell ist noch auf wenige konkrete Controls zugeschnitten. Noch kein allgemeines Vokabular für konkurrierende Regeln, unvollständige Fakten und komplexere fachliche Komposition. | Vorhandene Profile konsolidieren; einen zweiten fachlichen Fall außerhalb der Vorwahl prüfen. Nicht sofort eine universelle UX-Sprache erfinden. |
| FW-009 | P2 | Die neuen Auswahlstudien verwenden ein anderes Aufgabenformat als der vorhandene Übergabehelper. Der reale SELECTION-02-Auftrag wird dort mit `unsupported task format` abgewiesen. | Neue Studien an das Rollen-/Übergabeprofil anbinden oder einen expliziten kompatiblen Adapter bauen. Kein rückwirkender Fehler des damaligen Studienkriteriums. |
| FW-010 | P2 | Bessere Ergebnisse schwächerer Modelle sind plausibel und teilweise beobachtet, aber nicht als allgemeine Wirkung unseres Setups nachgewiesen. Gesamter Startkontext, Rollenmetadaten und wiederholte Bedingungen fehlen übergreifend. | Den beschlossenen Stufenvergleich mit gemeinsamem Prüfkern, Budget-/Quellenmessung und Wiederholungen durchführen. Keine Modellidentitätsrecherche durch Worker. |
| FW-011 | P2 | Die Designwerkzeuge sind enger als ein universeller Designbaukasten: eine Seite, Fallgruppen direkt am Seitenroot, keine Rotation/Spiegelung im Boundsadapter, lokale 400/700-Fonts, keine allgemeinen Stylespans, begrenzte Chart-/SVG-Familien. Theme-Karten erzeugen keinen Darkmode der Komponente. | Unterstützte Fähigkeiten vor Auftragsstart maschinenlesbar sichtbar machen; Erweiterungen einzeln mit echten Zielartefakten prüfen. Diese Grenzen sind überwiegend bereits ehrlich dokumentiert. |
| FW-012 | P2 | Accessibility ist in konkreten Fällen geprüft, aber kein vollständiges komponentenbezogenes AT-/IME-/Kontrast-/Theme-Abnahmeprogramm. Eine statische FIG-Annotation ist weiterhin kein Browsernachweis. | Zielbezogene Abnahmematrix und relevante reale Webfälle ergänzen. iOS/Android bleiben Zukunftsmusik und blockieren diesen Schritt nicht. |
| FW-013 | P2 | Ein harter Schemafehler kann im Gesamtstatus von einer späteren Blockierung überdeckt werden. | Fehlerpriorität korrigieren und den erhaltenen Gegenfall als Regression hinzufügen. |

Die vollständigen Herkunftsangaben, Auswirkungen und jeweils konkreten Abnahmekriterien stehen in [findings.json](findings.json). Eine dokumentierte und bewusst begrenzte Fähigkeit ist nicht automatisch ein Implementierungsfehler. Die P2-Befunde benennen vor allem Grenzen für die nächste Ausbaustufe.

### FW-013 im Detail: Diagnosepriorität

Ein temporärer Kandidat enthielt `library.json`, `fonts.json` und ein absichtlich ungültiges CEM-Dokument. Die Originalschemaprüfung fand den Fehler und setzte dessen Artefaktstatus auf `FAIL`. Danach setzte die Prüfung des nicht unterstützten Font-Libraryroots das **Gesamtergebnis auf `BLOCKED`**. Der erkannte Schemafehler blieb nur in den Einzelresultaten sichtbar.

`release:false` bleibt erhalten. Es ist deshalb kein Freigabe-Durchbruch, aber ein konkreter Fehler der Gesamtdiagnose: Der Konsument kann zuerst eine Runtime-/Rootfrage bearbeiten und dabei den bereits feststehenden Quellfehler übersehen. Erwartung für eine Reparatur: Gesamt-`FAIL` mit zusätzlicher Blockierungsdiagnose, ohne den negativen Originalfall zu verändern.

[Erhaltener Gegenfall](evidence/error-precedence.json) · Quelle: `skills/ui-contracts/scripts/contracts.py`, Font-Prüfung nach der Fehleraggregation.

## Empfohlene Arbeitsfolge

1. **Aktive UX-Revision konsolidieren (FW-002, FW-008).** Select mit Suche und die vereinbarten Bedeutungen aus dem Kandidaten bewusst übernehmen. Varianten und fehlende Fähigkeiten eindeutig auffindbar machen. Die freie Adress-Schreibhilfe bleibt ein eigener noch zu definierender Vertrag.
2. **Entscheidungsgrundlagen absichern (FW-001, FW-003, FW-013).** Quellenabschluss und Nachweisstatus entscheidender UX-Fähigkeiten prüfen; Diagnosepriorität korrigieren. Die im Audit gefundenen negativen Fälle zuerst als zukünftige Regressionen übernehmen.
3. **Wiederholbar ausführen und gegen das Ziel prüfen (FW-004, FW-005, FW-007).** Gepinnte Laufzeit, gemeinsamer Testeinstieg und wiederverwendbare tatsächliche Adaptertests. Zunächst die vorhandenen drei bis vier Controlfamilien stabilisieren.
4. **Erst danach breiter skalieren (FW-006, FW-009–FW-012).** Aufgabenformat vereinheitlichen, Änderungsfolgen sichtbar machen und den gestuften Modellvergleich ausführen; neue Charts/Themes/AT-Fälle gezielt ergänzen.

Mein nächster Schwerpunkt wäre damit **kein weiterer großer Standardsurvey**, sondern ein kleiner durchgängiger Weg: aktive Definition → begründete UX-Eignung → erzeugtes Webziel → gemeinsamer tatsächlicher Nachweis. Dafür sind die vorhandenen Teile weit genug; ihre Übergänge benötigen jetzt die meiste Arbeit. Diese Reihenfolge ist eine Empfehlung dieses Audits, noch kein beauftragtes Reparaturpaket.

## Nachvollziehbarkeit

- [Quellen- und Belegreceipt](receipt.json) bindet den gelesenen Ausgangsstand und die abgelegten Ergebnisse.
- [Maschinenlesbare Befunde](findings.json) führen ID, Priorität, Status `open`, Maßnahme und Abnahmekriterium.
- Unter `execution/` liegen die tatsächlich ausgeführten einmaligen Auditwrapper mit ihren damaligen lokalen Pfaden. Sie sind keine neue portable Produkt-CLI. Belegdateien enthalten synthetische Testdaten und lokale Werkzeugpfade.
- Es wurden keine laufenden OpenPencil-/S3-Installationen verändert, keine neuen Browser-/Modellversuche behauptet und kein Commit/Push durch den Auditauftrag ausgelöst.
