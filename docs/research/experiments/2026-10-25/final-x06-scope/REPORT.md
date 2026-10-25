# Die vier verbleibenden X06-Originalzugriffe

Stand: 25. Oktober 2026. Endlicher Abgleich der bereits benannten Originalstände; keine Suche über beliebige spätere Produkte. Zwei begrenzte Modellgrenzen eingeordnet, zwei Originalfragen bleiben ausdrücklich offen. Zusätzlich sechs neue Bedingungen am originalen Google-Konfigurationsschema ausgeführt, alle sechs Erwartungen erfüllt. Vorhandene Gegenfälle werden nicht erneut gezählt.

## Unverändertes Kriterium

X06 betrifft die unabhängige Prüfung eines separaten Domänenartefakts gegen dessen Originalschema, ohne stillschweigende Erweiterung des Originalformats. SDK-Programmtypen, Hostdokumente, Redaktionskonfiguration und Contractdaten haben unterschiedliche Subjekte. Ein begrenzter Originalschema-Beitrag braucht keine vollständige Produktionskonformität. Umgekehrt reicht ein echtes Schema für einen anderen Gegenstand nicht als Beleg dieses Beitrags.

## Zag: funktionales SDK-Maschinenmodell

Am Commit cafda74ba915d5abc5abb20abdde3a719d8e4e9c wurden Introduction, Building Machines, öffentliche Core-/Combobox-/ScrollArea-Exports, Core-Typen und Factory gezielt gelesen. Die Introduction ordnet Zag als Implementierungs-Toolkit ein und grenzt die eigene API ausdrücklich von SCXML ab. Die Autorenanleitung erstellt eine Maschine mit createMachine und konsumiert sie über Framework-Service und DOM-Connector.

Die Originaldefinition Machine verlangt initialState als Funktion. Context, Props, Refs, Guards, Actions und Effects sind ebenfalls an Funktions-/Service-/Hosttypen gebunden. MachineSchema bezeichnet die generischen Typdimensionen dieses SDK-Programms. createMachine nimmt dieses Machine-Objekt entgegen, baut den Stateindex und gibt die Konfiguration zurück. Die tatsächlichen öffentlichen Combobox-/ScrollArea-Einstiege exportieren Maschinen, Connectors, Anatomy, Props und zugehörige Service-/API-Typen. Damit ist der benannte Gegenstand positiv bestimmt: ein ausführbares SDK-Modell, kein davon unabhängiger neutraler Contractdatendateityp.

**Zag X06 U → N/C481 für genau diesen offiziellen Core-/Autoren-/Combobox-/ScrollArea-Beitrag.** Nicht als Abwesenheit sämtlicher Validatoren interpretieren: Original-Stateprüfungen und TypeScript-Prüfbarkeit bleiben belegt. Die bereits ausgeführten P39/P40-Modusgegenfälle bleiben unverändert erhalten. Auch ein in TypeScript gespeichertes Maschinenprogramm bleibt ein gültiger Zag-Gegenstand; es erfüllt nur nicht durch Umbenennung des generischen MachineSchema den verlangten unabhängigen Datenartefaktbeitrag. Ein neuer Datenimport/Exportvertrag oder SCXML-Übersetzer wäre eine zusätzliche Ergänzung. Die ältere Quellenkurzbeschreibung wird präzisiert: Die ausdrückliche SCXML-Abgrenzung steht in Introduction, die konstruktive Autorenanleitung in Building Machines.

## APG: Leitfaden und konkrete Beispieltests

Am Commit 0f765e4dc33e966026114ac12a8380db1de3b787 wurden package.json, README, Introduction, Combobox-Pattern, offizieller ariaTest-Einstieg und der Autocomplete-both-Test gelesen. Die Introduction beschreibt Optionen und illustrative Implementierungen. Sie grenzt einen eigenen Konformitätsanspruch ausdrücklich ab. Diese Aussage allein wäre noch kein Beweis gegen jedes mögliche Schema; entscheidend ist zusätzlich das tatsächlich gelesene Artefakt-/Prüfpaar.

Die benannten Artefakte sind Pattern-/Beispiel-HTML und ausführbare JavaScript-Tests. ariaTest erhält Beschreibung, Beispielseitenpfad, data-test-id und eine Testfunktion. Der originale Runner öffnet genau diese lokale HTML-Seite in Firefox/Selenium, kontrolliert die zugehörige Verhaltensbeschreibung und führt die Funktion aus. Der Combobox-Test bindet konkrete Selektoren und erwartete Attribute beziehungsweise Tastenfolgen an das offizielle Beispiel. README/package.json trennen HTML-/CSS-/JS-Codeprüfung von dieser Regression. Das ist ein positiver Nachweis des originalen Beispieltestgegenstands, kein neutrales Pattern-Contractschema.

**APG X06 U → N/C482 für den eigenen neutralen Contractschema-Beitrag dieses Guide-/Pattern-/Testpfads.** HTML-Konformität, ausführbare Originalregression und die fachlichen APG-Empfehlungen bleiben eigenständige Beiträge. Die Einordnung behauptet weder, informative Leitfäden könnten grundsätzlich keine Schemas enthalten, noch fehlende Zugänglichkeit oder fehlendes Tooling. Keine Firefox-/Selenium-/Tastatur-/Assistenzprüfung hier ausgeführt. Es wurden nur die Originalquellen des Prüfpfads gelesen; keine neuen APG-Laufzeitbedingungen gezählt.

## Google DESIGN.md: echtes Schema, anderes Subjekt

Gegenstand bleibt @google/design.md 0.4.0 mit RegistrygitHead 9bf8eae67128b6cc55ad9bf86665767deb4c11cd. Die mitgelieferten dist/spec.md, spec-config.yaml, öffentlichen Linter-/Outputdeklarationen und der gebündelte Config-Ladepfad wurden gelesen. Zusätzlich wurde die zugehörige originale spec-config.ts über BrowserOS geöffnet.

Die YAML-Konfiguration bezeichnet sich als maßgebliche Quelle für die Spezifikationsgenerierung. Tatsächlich gibt es PropertyDefSchema, TypeDefSchema und ConfigSchema in Zod. loadSpecConfig liest **diese Redaktionskonfiguration** und prüft sie mit ConfigSchema.parse. Die geprüften Eigenschaften heißen beispielsweise units, typography_properties, component_sub_tokens und examples. Das sind Definitionen und Beispiele der Spezifikation, nicht die Tokeninstanzen eines eingereichten DESIGN.md-Dokuments. Auch das vorhandene ParserInputSchema prüft einen anderen Gegenstand: den Text-Transportwrapper. ParsedDesignSystem ist ein internes, teilweise offenes und um sourceMap/Markdowninformationen erweitertes Outputmodell.

### Sechs vorab gespeicherte Originalschema-Gegenfälle (P45)

Die drei unveränderten Schema-Deklarationen wurden mit dem TypeScript-AST isoliert und ausschließlich transpiliert. Ausgeführt mit dem tatsächlich installierten Zod der gebundenen Distribution, ohne Schemaersatz. Modulinitialisierung, Dateilader und vollständiger Specgenerator wurden nicht ausgeführt. Das mitgelieferte spec-config.yaml dient als Originalkontrolle.

| Eingabe | Voraberwartung und Beobachtung |
| --- | --- |
| Mitgelieferte Originalkonfiguration | angenommen |
| units als Zahl | abgewiesen |
| typography_properties[0].type als Zahl | abgewiesen |
| Dort ein frei erfundener Typname als String | angenommen: Typetikett wird formal als String geprüft |
| Minimale DESIGN.md-Token-Daten statt Redaktionskonfiguration | abgewiesen: anderes Schemasubjekt |
| Numerischer Farbwert unter examples.colors | abgewiesen: Beispieltabelle erwartet Strings |

**Google X06 bleibt U/C483.** Die sechs erfolgreichen Gegenfälle belegen ein originales Konfigurationsschema, ohne es zu einem Dokumentinhaltsschema umzudeuten. Das ursprüngliche Prosa-Schema und selektive Linterregeln bleiben positive, begrenzte Beiträge. Ihre Existenz wird nicht bestritten und ein fehlender vollständiger semantischer Allzweckvalidator wird nicht als neues Kriterium verlangt. Nicht belegt ist weiterhin die eindeutige originale Bindung zwischen dem beschriebenen separaten Dokumentdatenmodell und einem Originalschemaprüfpfad. Die vorhandenen Parser-/Lint-Outputs liefern keinen ausgewiesenen Dokument-Schemaentscheid; errors=0 ist bereits durch gespeicherte Gegenfälle als solcher ungeeignet.

**Konkrete externe Klärung:** Welcher vom Herausgeber benannte Schema-/Prüfeinstieg und welches Ergebnis gelten für die Inhaltsform eines separaten DESIGN.md-Dokuments, insbesondere Roottypen, optionale Abschnitte und bewusst ausgelassene Token? Falls die Prosa maßgeblich und das Regelwerk bewusst nur teilweise ist, bleibt eine eigene ausführbare Prosaabbildung ein Zusatzprofil. Eine solche eigene Grammatik wird hier weder erfunden noch als Originalnachweis ausgegeben. Diese Frage ist von der Produktentscheidung über eine strengere Abnahmepolitik getrennt. Keine Anfrage an Herausgeber versandt.

## OpenUI: Originalwiderspruch braucht Vorrangklärung

Gegenstand ist weiterhin ctate/openui beziehungsweise openuispec.org, Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9, draft-01. README/Entwurf, lib/schema.ts, interfaces/Spec.ts und der Tabellenrenderer wurden erneut gezielt gelesen. Ein erster Zugriff auf lib/Spec.ts lieferte 404 und bleibt im Zugriffsprotokoll; der bereits bekannte tatsächliche Pfad interfaces/Spec.ts wurde anschließend erfolgreich gelesen. Aus dem fehlgeschlagenen Zugriff folgt keine fachliche Abwesenheit.

| Frage | Entwurf/Feldkatalog | interfaces/Spec.ts |
| --- | --- | --- |
| license am Root / group je Komponente | nicht als entsprechende Pflichtfelder geführt | beide verpflichtend |
| Einzelne Prop als Typstring | ausdrücklich erlaubt | nur Objektform |
| enum und required innerhalb Propdefinition | ausdrücklich beschrieben | keine entsprechenden Properties |
| default-Wert | beliebiger Wert im Katalog | boolean, number oder string; Feld im Typ verpflichtend |

Der Renderer verarbeitet den Feldkatalog zu Tabellen, kein importiertes openui.yaml. Das Katalogobjekt benutzt unter anderem type:any und Platzhalter als Beschreibungsmodell; es wird hier nicht ohne Übersetzung als standardkonformes ausführbares JSON Schema ausgegeben. Draft und README benennen zwar die Datei und Formatregeln, die gelesenen Originale liefern aber keine Vorrang-/Synchronisationsregel für diese widersprüchlichen Definitionen.

**OpenUI X06 bleibt U/C484, externe Autorenklärung im exakt gebundenen Stand.** Erforderlich ist die offizielle Festlegung, welche Definition für die genannten Formen maßgeblich ist und welches Originalprüfpaar daran gebunden wird. Ein eigener TypeScript-Check gegen einen der widersprüchlichen Typstände würde diese Originalfrage nicht entscheiden. Keine Abstimmung des Nutzers über technische Wahrheit, keine selbst reparierte Schemasprache und keine Nachricht an Autoren.

## Ergebnis und verbleibende Arbeit

Aktuell **47 U: 27 Integration und 20 weitere**. X06: **8 D, 2 A, 4 begrenzte N, 2 U**. Insgesamt **354 Bedingungen in 45 Gruppen**. Die Zahl sinkt durch zwei begründete Modellgrenzen, nicht durch zwei neue positive Integrationsbelege. Weder Zag noch APG werden dadurch zu vollständigen Vier-Domänen-Lösungen.

Die endlichen Zugriffe auf alle vier Kandidaten sind durchgeführt. Google und OpenUI bleiben mit den oben benannten Originalinformationen offen. Das blockiert nicht sämtliche andere Forschung: Im Register stehen weiterhin unabhängige Layout-/Scroll-, Referenz-, Ownership- und Praxisfragen. Die 47 Zellen sind keine pauschal extern blockierte Abschlussliste. Keine vollständige Integration behauptet. Kein Commit, Push, neue Komponente oder neue Agenten.

## Reproduktion

source-access.json enthält URLs, Lesehashes und den erhaltenen 404. source-manifest.json bindet zusätzlich die tatsächlich verwendeten originalen Paket-/Tooldateien und eigenen Ergebnisartefakte. Die vollständigen gelesenen Originaltexte bleiben im lokalen Recherchebereich; im Repository werden eigene Befunde, Zugriffshashes, Extraktionsmetadaten und Ergebnisse gesichert. run-config.cjs benötigt am dokumentierten Ort die gepinnte Originalquelle und dieselben bestehenden Werkzeuge; prepare.py extrahiert sie aus den lokalen Browsercaptures. cases.json wurde vor Ausführung gespeichert. results.json und extraction.json bewahren Schema-Identität, Werkzeugstände und alle sechs Ergebnisse. Kein Parser-/Schemafehler wurde nachträglich zum erwarteten Erfolg umgeschrieben.
