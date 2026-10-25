# IP-01: tatsächlich geprüftes statisches Vier-Domänen-Referenzpaket

Stand: 25. Oktober 2026. **27 vorregistrierte Bedingungen ausgeführt, alle Erwartungen erfüllt.** Ein gemeinsamer lokaler Quellenabschluss umfasst drei Definitionen, vier Domänen und zwei Instanzketten. Dies ist eine ausführbare statische Forschungsprüfung mit vorläufiger JSON-Bindung; kein beschlossenes Produktformat, keine produktive Komponentenbibliothek und kein gemeinsamer Browser-/SCXML-Hostlauf.

[Aufgelöste Referenzbindung](reference/bindings.json) · [Quellenabschluss](reference/resolved.json) · [Vorregistrierung](cases.json) · [vollständige Ergebnisse](results.json) · [Original-/Eigenartefakthashes](source-manifest.json)

## Tatsächlich vorhandene Dateien und Rollen

| Beitrag | Originalsyntax / tatsächliche Forschungsdateien | Was ausgeführt wurde |
| --- | --- | --- |
| Interface | CEM 2.1.0-Metadaten je [Autocomplete](reference/autocomplete/interface.json), [Overlay](reference/overlay/interface.json), [ScrollArea](reference/scroll-area/interface.json) | Unverändertes vorhandenes Original-CEM-Schema; danach eigener begrenzter TypeScript-AST-/Wertprüfer. Die CEM-Modulpfade sind Metadaten dieser Forschungsdefinitionen; zugehörige produktive JS-Klassen sind nicht implementiert. |
| Behavior | Je eigene SCXML-Datei: [Autocomplete](reference/autocomplete/behavior.scxml), [Overlay](reference/overlay/behavior.scxml), [ScrollArea](reference/scroll-area/behavior.scxml) | Original-SCXML-XSD sowie zusätzliche namespacebewusste XPath-Portbindung. Die Dateien leiten sich aus den Lifecycle-Fixtures ab; Originalruntime für diese neuen Pfade nicht ausgeführt. |
| Visual | [DTCG-Tokens](reference/visual/tokens.json), CSS je Definition einschließlich [Overlay](reference/overlay/layout.css) und [ScrollArea](reference/scroll-area/layout.css) | Eigene begrenzte dimension-/Curly-Aliasauflösung und konkrete Token→CSS-Variable-/Deklarationsbindung; css-tree 3.2.1 parst die CSS-Syntax. Keine vollständige DTCG-/CSS-Modulvalidierung oder tatsächliche Geometrieprüfung. |
| Accessibility | HTML-Templatebeiträge je Definition sowie [gemeinsamer statischer Host](reference/host.html) | HTML-Parsing und eigene Ziel-/Rollen-/Instanz-/aria-controls-Beziehungen. Kein erfundenes neutrales ARIA-Schema, kein Browser-AX-, APG-Gesamt- oder Assistenztechniklauf. |
| Verbindungen | [Vorläufiges bindings.json](reference/bindings.json) | Eigener enger Resolver für diese Quellen, Zielarten, Instanzpfade, Typen und Projektionen. Das ist kein Originalstandard und kein genereller Resolver. |

Vier logische Domänen bedeuten hier mehrere physische Dateien. `host.html` ist eine eigene statische Zielprojektion, keine fünfte Domäne. Er wurde für die Fixture ausdrücklich verfasst; automatische verlustfreie Ableitung aus allen Templates ist nicht nachgewiesen. `package/` enthält die erzeugbaren Vorlagen, `reference/` dagegen den tatsächlich gepinnten positiven Ausgangsabschluss.

Die Behaviordateien sind **Forschungsgerüste**: Sie enthalten den untersuchten Lifecyclekern und einen ausdrücklich `STATIC_PORT_ONLY` benannten Prüfport. Das eigene value-change-Sendziel ist dort ein lokaler SCXML-Port, kein bereits exportiertes DOM-CustomEvent. Die vollständige Autocomplete-Maschine mit Loading/Empty/Provider/Commit und Hostexport ist noch zu erstellen. Schemakonforme Dateien belegen diese Interaktion nicht.

## Konkreter gemeinsamer Abschluss

Drei Definitionsnamen im Namespace `reference`, sechs Verwendungen A/B→Overlay→ScrollArea, konkrete CEM-Part-Pointer und jeweils eigene Hostziele. Logische Listbox, Overlayfläche und Scrollviewport bleiben getrennt. Der Input kontrolliert die eigene semantische Listbox. Zusätzliche `data-instance`-/`data-part`-Attribute sind ausgewiesene Forschungszuordnungen, keine neuen ARIA-Standardfelder.

Die Visualbeziehungen verweisen auf dieselben Originaldateien: DTCG `autocomplete.gap`→Overlay `margin-top:var(--gap)`, `maxHeight`→ScrollArea `max-height:var(--max-height)`, `rowHeight`→Autocomplete `min-height:var(--row-height)`. Tatsächliche Aliaswerte und Einheiten sowie die tatsächlich geparsten CSS-Deklarationen stehen als Auflösungszeugen im Ergebnis. Das prüft die statische Verbindung; CSS-Variablen werden noch nicht in einem Browser gesetzt oder gemessen.

Alle Originaldateien und Bindungen besitzen SHA-256 im Quellenabschluss. Die Bündelrevision wird aus der deterministisch sortierten Dateihashmap gebildet. Das ist eine eigene explizite Forschungsregel. Sie ist noch nicht die produktive, Policy separat behandelnde Revisionspolitik aus IP-01. Änderungen an bindings.json einschließlich seiner Policy ändern hier denselben Dateifingerprint. Die Pin-/Updatekonvention wird damit nicht als Standard ausgegeben.

Semantische Mutationen werden bewusst neu gepinnt. ST-12 allein enthält einen falschen Quellhash als Integritätsgegenfall. ST-25 verändert dagegen die referenzierte Zielrevision bei weiterhin korrekten Quellhashes und korrekter Bündelrevision; der Resolver erkennt deshalb einen **semantischen Revisionskonflikt**. Ergebnisse und aufgelöste Hashmaps sind in `runs/ST-xx/resolved.json` gespeichert. Statt alle identischen Dateien zu vervielfältigen, enthält `runs/ST-xx/patch.json` nur Änderungen gegenüber `reference/`. Der gesamte Fall lässt sich durch Baseline plus Patch rekonstruieren; diese Rekonstruktion wurde für alle Fälle geprüft.

`runtimeCandidate` bindet Paketversion und echten Hash des bereits geprüften idlocation-/Fehlerrelay-Adapters als Herkunft. **Der bisherige Adapter akzeptiert diese neuen Quelldateipfade nicht unverändert.** Seine lokale Whitelist und Hostbindung müssten für einen weiteren Runtimeversuch explizit angepasst werden. Der Provenienzeintrag wird deshalb nicht als ausgeführter Interpreterpfad ausgegeben.

## Typumfang und zusätzliche Regeln

Der originale CEM-Validator prüft die Metadatenstruktur, nicht die Bedeutung sämtlicher TypeScript-Typtexte oder konkrete Propertywerte. Der zusätzliche [AST-Leser](types.cjs) verwendet das tatsächlich vorhandene TypeScript 5.9.3 und interpretiert ausdrücklich begrenzte Knotenformen. T0 umfasst string/boolean/endliche number; `string | undefined` wird im unterstützten Umfang als optional behandelt. T1 ist die hier tatsächlich geprüfte homogene Ergebnisliste mit `{key:string,label:string,disabled?:boolean}`. Fehlend und null bleiben verschieden. Zusätzliche Recordfelder werden durch die ausdrücklich gewählte eigene Closed-Record-Policy abgewiesen; das ist keine allgemeine TypeScript-Regel.

Defaults sind deklarierte CEM-Metadatenstrings. Nur als JSON-Literal interpretierbare Defaults werden hier gegen denselben abgeleiteten Typ geprüft. Beliebige JS-Ausdrücke und vollständige CEM-/TypeScript-Typsprache bleiben unsupported. Ein ausdrücklich begrenzter Guard `typeof value === 'string'` verengt den optionalen Wert am statischen Prüfport; dies ist eine eigene enge Guardkonvention, keine vollständige JavaScript-Kontrollflussanalyse.

ST-08 übergibt positive Unendlichkeit direkt an den zusätzlichen Wertprüfer. Es wird bewusst **kein Infinity als gültiger JSON-Transport** in die Originalquelle geschrieben. Die abweichende In-Memory-Eingabe ist im Fall protokolliert. Diese Prüfung ist keine tatsächliche Interpreter-/DOM-Payloadzustellung.

## Vorregistrierte Ergebnisse

| Fälle | Erwartung und tatsächliches Ergebnis |
| --- | --- |
| ST-01–ST-03 | Positiver Abschluss, anderer gültiger Unicode-/Boolean-/Zahlen-/Recorddatensatz sowie fehlende optionale Felder werden akzeptiert. |
| ST-04–ST-08 | Fehlendes label, falsche query, null statt optionalem string, doppelte Keys und nichtendliche Zahl werden mit den vorgesehenen Typ-/Datenfehlern erkannt. |
| ST-09–ST-13 | Fehlendes Pointerziel, fremde Instanz, anderer Namespace, falscher Quellhash und nicht unterstützte Formatversion werden getrennt erkannt. |
| ST-14–ST-17 | Eventtypwiderspruch, rekursive Komponentenexpansion, nicht unterstützter Uniontyp und falsche Hostzielart werden erkannt. Zustandsmaschinen-Schleifen werden nicht pauschal verboten. |
| ST-18–ST-19 | Beschädigtes CEM und falsche SCXML-Version scheitern bereits an den jeweiligen Originalschemas. |
| ST-20–ST-24 | Nicht unterstützte Dimensionseinheit, falscher Defaulttyp, Tokenaliaszyklus, fehlende Pflichtbeziehung und zusätzliches Recordfeld werden durch ausgewiesene eigene Prüfungen erkannt. |
| ST-25 | Falsche Zielrevision scheitert trotz korrekt aktualisiertem Quellenabschluss an REVISION_MISMATCH. |
| ST-26–ST-27 | Fehlendes Tokenziel und Widerspruch zwischen deklarierter Tokenbindung und echter CSS-Variablenreferenz werden erkannt. |

Die ursprünglichen 24 Erwartungen wurden vor dem ersten Lauf gespeichert. ST-25 sowie ST-26/ST-27 wurden jeweils vor ihrer ersten Ausführung zusätzlich registriert; die Ergänzungen sind im Plan ausgewiesen. Die letzten beiden Fälle entstanden mit der ausdrücklich ergänzten Token-/CSS-Beziehung. Alle 27 finalen Erwartungen sind erfüllt. Die positiven Daten von ST-01 und ST-02 sind tatsächlich verschieden.

Der erste Runner verwendete für ST-02 versehentlich dieselben Werte wie im Baselinefall. Diese eigene Prüflücke ist in [erstem Runner](run-initial.py) und [ersten Resultaten](results-initial.json) erhalten. Sie wurde durch einen tatsächlich anderen gültigen Datensatz korrigiert. Außerdem wurden Originalschema-Ergebnisse bei frühem Abbruch explizit im Protokoll erhalten, CSS-Syntaxzeugen ergänzt und die Ausgabe auf Baseline plus Patches verkleinert. Der [rekonstruierbare ursprüngliche Eingabepatch](initial-input-patch.json) ergänzt die damaligen Vorlagen; die so rekonstruierte erste Baselinerevision stimmt mit dem archivierten Ergebnis überein. Frühere Ausgaben sind keine zusätzlich gezählten Bedingungen; ursprüngliche Erwartungen wurden nicht zu Erfolgen umformuliert.

## Einordnung in die IP-Abnahme

- **A01:** Original-CEM-/SCXML-Prüfungen konkret; HTML/CSS/DTCG bleiben mit ihren bezeichneten zusätzlichen Teilprüfungen sichtbar. Kein vollständiger Originalvalidator für alle vier Domänen.
- **A02:** Ein statischer Abschluss mit konkreten Parts, Zielarten, Definitionen, Instanzen und XPath-Portbindung einschließlich Gegenfällen ist vorhanden. Livezustandsbindung fehlt.
- **A03:** Quelle-/Zielrevisionen und rekonstruierbare Hashabschlüsse sind konkret geprüft. Allgemeine Migration/Kompatibilität und produktive Paketpolitik fehlen.
- **A04:** Die ausgewählten T0-/T1-Werte, Optionalität, Defaults und Typbindungen sind statisch geprüft. Gemeinsame Runtimeverarbeitung und öffentliche Hosteventfolge fehlen.
- **A15:** Ausgewählte Versions-/Typ-/Rekursions-/Aliasgrenzen konkret erkannt; keine allgemeine Transport-, Netzwerk-, Ressourcen- oder Sicherheitsprüfung.

Keiner der vollständigen IP-Gesamtfälle wird dadurch pauschal abgehakt. Keine Matrixklassifikation geändert. Aktueller Forschungsstand nach dieser Ergänzung: 682 Bedingungen in 105 Gruppen, zwei offene Originalklärungen. Die 27 neuen Fälle zählen einmal; AST-/Schema-Vorläufe, Wiederholungen und einzelne Prüfaussagen eines Falls werden nicht zusätzlich gezählt.

## Was für die Fortsetzung entschieden werden muss

Für den nächsten engen Forschungs-Hostlauf genügt die jetzt konkrete Fixture mit ihrem ausgewiesenen Adapterkandidaten; eine neue produktive Formatsprache ist dafür nicht nötig. Noch zu reviewen sind die fachlichen Varianten von IP-01, bevor daraus ein Produktvertrag entsteht: manuelle Listenauswahl gegenüber Freitextbestätigung, Query-/Werttrennung und tatsächlicher Plattformumfang. JSON-Serialisierung, Forschungsnamen und Closed-Record-Policy dieses Pakets bleiben vorläufig. Diese Entscheidungen sind am nun vorhandenen Paket reviewbar und werden nicht aus einem erfolgreichen statischen Test als beschlossen abgeleitet.

Nächster technischer Umfang: dieselben gepinnten Quellen in einem tatsächlich ausgeführten Host verbinden, die vollständige Behaviorlogik ergänzen, den Kandidaten auf den deklarierten lokalen Quellenbestand binden und dann echte Event-/Fokus-/Scroll-/A11y-Zustandsfolgen abnehmen. Kein Theme-/Crossplattform-/AT-Erfolg aus dieser statischen Prüfung ableiten.

## Reproduktion

Die Pythonumgebung benötigt jsonschema und lxml; der zusätzliche AST-/CSS-Pfad die vorhandenen gepinnten TypeScript-/css-tree-Verzeichnisse. `create_fixture.py` erzeugt Vorlagen, `run.py` führt den Plan aus und schreibt den positiven Abschluss, Patches und Ergebnisse. Im Forschungsworkspace wurde die gebündelte Pythonumgebung mit den vorhandenen Abhängigkeiten verwendet; deren Provenienz steht im Manifest. Die Skripte erwarten wie die früheren Forschungsproben die Verzeichnisstruktur `work/...` für Originalwerkzeuge und das aktuelle Projektverzeichnis als Ausgangspunkt. Kein stilles Installieren neuer Versionen. Schema-/Werkzeug-/Eigenartefakthashes vor Reproduktion prüfen. Kein Commit oder Push.
