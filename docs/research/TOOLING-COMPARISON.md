**Ausführungsfortschreibung, 24.10.2026:** Die nachfolgende Vergleichstabelle dokumentiert ihren damaligen Quellenstand. Inzwischen sind 217 Bedingungen in 22 Gruppen ausgeführt: unter anderem CEM-/UXSpec-JSON-Schemata, SCXML-XSD, Nu-Hostchecks, zwei CSS-Grammatiken und OpenPencil-Variablen-/CSSOM-Schemata. [Versuchsberichte](experiments/2026-10-24/REPORT.md), [neuer OpenPencil-Prüfumfang](experiments/2026-10-24/openpencil-validation/REPORT.md). Historische Aussagen „nicht ausgeführt“ gelten nicht als aktueller Ausführungsstand.

**Neuester Fachnachweis:** [OpenPencil-Overflowimport und native CSS-Folge](experiments/2026-10-25/openpencil-overflow-import/REPORT.md); zwölf Originalfragment- und drei Browserbedingungen erfüllt. hidden/clip gehen im benannten Feldpfad zusammen, vollständige Scrollsemantik bleibt U/C487. Weiter 41 U (26 Integration, 15 weitere), 383 Bedingungen/48 Gruppen; kein Gesamt-Roundtrip oder OpenPencil-Build behauptet.

**Neuester Nachweis:** [CSS-Anker an Originalteile und zwei Hostinstanzen gebunden](experiments/2026-10-25/css-semantic-anchors/REPORT.md); zusätzlicher statischer Resolver, 14 unterschiedliche Erwartungen erfüllt, CSS X03 A/C485. Kein nativer Layout-/AT-Nachweis. Aktuell 41 U (26 Integration, 15 weitere), 368 Bedingungen/46 Gruppen.

**Aktueller Nachweisblock:** [Vier letzte X06-Originalzugriffe](experiments/2026-10-25/final-x06-scope/REPORT.md); Zag/APG mit begründeter eigener Modellgrenze N, Google/OpenUI mit präziser externer Originalklärung weiterhin U. Sechs neue Konfigurationsschema-Gegenfälle erfüllt. Aktuell 41 U (26 Integration, 15 weitere), 354 Bedingungen/45 Gruppen. Kein Gesamtabschluss, Commit oder Push.

**CSS-Originalgrammatikbindung ausgeführt:** [Vier Properties, zwölf Bedingungen](experiments/2026-10-25/css-original-grammar/REPORT.md); Originalsyntax unverändert an zusätzlichen Lexer gebunden, native Wörterbuchlücken erhalten. X06 A/C479 im begrenzten Umfang. Aktuell 49 U, 348 Bedingungen/44 Gruppen.

**Panda-Originaldatenmodell und Adapterbedarf geklärt:** [Versionierter Export/Originaltyp/Reader](experiments/2026-10-25/panda-original-scope/REPORT.md); X06 A/C477 für zusätzliche tatsächlich geprüfte Originaltypanbindung, kein nativer Runtime-JSON-Schemavalidator. Vorhandene P42-Evidenz nicht doppelt gezählt. Aktuell 50 U, unverändert 336 Bedingungen/43 Gruppen.

**Ark-Originalschema identifiziert und ausgeführt:** [API-JSON → ursprüngliches Types-Collection-Schema](experiments/2026-10-25/ark-mcp-scope/REPORT.md), sechs Erwartungen erfüllt. X06 D/C474 für den eigenen Metadatenartefaktbeitrag, keine Runtime-Props-/Gesamtcontractprüfung. Aktuell 51 U, 336 Bedingungen/43 Gruppen.

**Endlicher Originalumfang für X06:** [Gepinnte offizielle Oberflächen und konkrete Restzugriffe](experiments/2026-10-25/x06-official-scope/REPORT.md); WAI-ARIA 1.2 eigenes Format-/Schemasubjekt anhand §8 geklärt, X06 N/C471. Originale Ark-Dokumentationsextraktion geklärt, X06 weiter U/C473. Aktuell 52 U; weiterhin 330 Bedingungen/42 Gruppen, keine neue Laufzeitbedingung.

**Panda-Artefakttyp/Reader getrennt geprüft:** [Neun gepaarte Eingaben](experiments/2026-10-25/panda-artifact-types/REPORT.md) belegen zusätzliche originale Shapeinformation und Grenzen beider Pfade. Die Literal-Typanbindung bleibt Zusatzcode, X06 U/C469. Weiterhin 53 U, jetzt 330 Bedingungen/42 Gruppen.

**Zag-/Ark-Originalprüfungen präzisiert:** [13 Bedingungen und getrennte Paketstände](experiments/2026-10-25/zag-ark-validation/REPORT.md); tatsächliche Core-Modusprüfungen und SDK-Typpfad belegt, neutrale X06-Artefaktschemafragen im breiteren Kandidatenumfang bleiben U/C466 und U/C467. Weiterhin 53 U, jetzt 321 Bedingungen/41 Gruppen.

**XState-Originalprüfgegenstand geklärt:** [Core 5.33.3, SDK-Typen und Snapshot getrennt](experiments/2026-10-25/xstate-validator/REPORT.md); sechs API- und drei SDK-Bedingungen erfüllt. X06 begrenzt N/C464 für den neutralen Originalartefaktschema-Pfad im veröffentlichten Core, keine pauschale Validatorabwesenheit. Aktuell 53 U, 308 Bedingungen/38 Gruppen.

**Neu: informationsbezogene Ownership geprüft.** [Originalpaket, Quelländerung und Konflikte](experiments/2026-10-25/ownership-conflicts/REPORT.md): zwei führende Informationen mit Ableitungen, 15 Änderungsfälle, eine erhaltene und korrigierte Revisionsverletzung sowie vier praktische Gegenbedingungen. CSS Layout X08 begrenzt A/C459; aktuell 41 U (26 Integration, 15 weitere), 283 Bedingungen in 35 Gruppen. Keine generische Ownership-/Transaktions-/Identitätsgarantie.

**Neue Laufzeitgrenze:** [Original-Defaultinvoke](experiments/2026-10-25/scxml-invoke/REPORT.md) koppelt bei gleichem Child-src die Daten zweier Instanzen trotz separater Elternvorbereitung: drei von sechs Erwartungen verletzt. Cancel/Neustart als Lebenszyklus sind begrenzt ausgeführt; ein Diagnosefall mit unterschiedlichen URIs besteht. Keine gewählte Lösung. Zum damaligen Teilabschluss 56 U-Zellen; in jenem Lauf keine Neubewertung. Sechs zusätzliche Fälle mit eigenem instanzgetrenntem Invokeradapter bestehen; die Originalverletzungen bleiben erhalten (C458).

**Ergänzung 25.10.2026 – SCXML-Laufzeit:** [Gespeicherter Prüfblock](experiments/2026-10-25/scxml-runtime/REPORT.md) mit 17 Bedingungen: 9/10 im Ausgangslauf, 2/2 Diagnosefälle und 5/5 Browserfälle. Getrennte Vorbereitung verhindert die beobachtete Datenkopplung. Native Parent-Sendung und ein zusätzlicher interaktiver Forschungs-Host sind ausgeführt; keine Produktionskomponente, physische Tastatur- oder AT-Prüfung. Ältere Aussagen zu ausschließlich statischer Prüfung gelten für die damaligen Teilversuche. Historischer Zwischenstand nach DTCG: 56 U-Zellen.

# Werkzeugvergleich: Originalschema, Code und Reifegrad

**Aktuelle Fortschreibung nach diesem dokumentarischen Stand:** [49 E3-Proben](experiments/2026-10-24/REPORT.md) sind inzwischen ausgeführt. CEM I02 ist nun A/C421; aktuell 65 U (41 Integration, 24 weitere). Frühere Aussagen „keine Ausführung“ und damalige Zählungen unten dokumentieren den Entstehungsstand. Keine vollständige UI-/AT-/Integrationsprüfung.


Stand: 24. Oktober 2026. **Dokumentarischer Vergleich aller 16 Kandidaten am jeweils gespeicherten Quellenstand.** Zusammengeführt werden die bereits belegten Einzelbefunde; neu sind gezielte X06-Folgeprüfungen zu XState, Zag und Ark UI. Keine neue Vollrecherche sämtlicher Releases, keine Installation und keine ausgeführten Compiler-, Validator-, Browser- oder Assistenztechniktests.

## 1. Was dieser Vergleich abschließt

Die drei vorgemerkten Vergleichsdimensionen sind für alle Kandidaten in einer gemeinsamen Sicht erfasst: Originalschema gegenüber tatsächlichem Werkzeug, Beschreibungsformat gegenüber zusätzlich nötigem Code sowie Versions-/Reifegegenstand gegenüber Kompatibilitätsnachweis. Unbekannte Antworten bleiben benannt. Das schließt die dokumentarische Zusammenführung ab, nicht alle technischen Nachweislücken oder eine Produktionsfreigabe.

Quellenbasis: [Register](SOURCES.md), [Claims](CLAIMS.md), [Methoden](METHODS.md). Bereits geprüfte Quellen werden hier erneut ausgewertet; sie gelten nicht als in dieser Runde frisch abgerufen. Neu gelesene Primärpfade sind unter [S62](SOURCES.md#s62) abgegrenzt. Aktuelle X06-Bewertungen: **8 D, 2 A, 4 begrenzte N, 2 U**. D belegt den begrenzten Originalschema-Beitrag, keine vollständig ausgeführte Validierungskette.

## 2. Originalschema und tatsächliches Werkzeug

| Kandidat | Originalartefakt / Schema | Tatsächlich belegte Prüfung | Wichtige Grenze / Befund |
| --- | --- | --- | --- |
| CEM | JSON-Manifest; originales JSON Schema Draft-07 | Schema veröffentlicht und importierbar; kein Validator ausgeführt | Typtext und Semantik externer Typen brauchen weitere Auflösung. X06 D, [C46](CLAIMS.md#c46) |
| OpenUI | YAML/JSON; TS-Interface und Feldkatalog weichen ab | Website rendert Schemaübersicht; kanonischer Contractvalidator nicht belegt | Originalwiderspruch braucht offizielle Vorrangklärung; keine eigene Reparatur. X06 U, [C484](CLAIMS.md#c484) |
| Google DESIGN.md | Markdown mit YAML; Textwrapperschema, TS-Modell | Original-Library lint mit Parser/Modell/Regeln | Originales ConfigSchema ausgeführt, Subjekt ist Spezifikationskonfiguration. Dokument-Schemabindung weiter U, [C483](CLAIMS.md#c483) |
| AgentsORG | Eigenes .design-Artefakt, originales JSON Schema Draft 2020-12 | Python-Referenzlinter verwendet Schema und eigene Fachprüfungen | Reale Prüflogik vorhanden, keine vollständige Vier-Domänen-Prüfung. X06 D, [C179](CLAIMS.md#c179) |
| DTCG | Format und Resolver 2025.10; getrennte JSON-Schemata | Syntax-/Editorprüfung durch veröffentlichte Schemata möglich | Auflösung, Zyklen und konkrete Werkzeuge separat prüfen. X06 D, [C57](CLAIMS.md#c57) |
| UXSpec | Originalschema Draft 2020-12; Behavior ohne $visual auf Schemaebene möglich | CLI validate besitzt eigene ausgewählte Regeln; Compiler ist weiterer Pfad | CLI lädt Originalschema nicht; Compiler ruft validateSpec nicht auf. X06 D für Schema, [C205](CLAIMS.md#c205) |
| SCXML | XML; Original-XSD-Module und getrennte striktere Variante | Schemaquellen veröffentlicht; kein XSD-Validator/Interpreter ausgeführt | Datenmodell und Hostcode sind zusätzlich; Schema allein beweist keine Ablaufsemantik. X06 D, [C68](CLAIMS.md#c68) |
| XState | JS-/TS-Maschinenkonfiguration, Snapshot/Definition als andere Gegenstände | TS-Typen und Maschinenimplementierung; schemas wird im gelesenen Pfad nur übernommen | schemas:unknown und toJSON sind kein unabhängiger Artefaktvalidator. X06 N im veröffentlichten Core 5.33.3, [C464](CLAIMS.md#c464) |
| Zag | TS-Maschinen und Komponenten-Props | Typprüfung sowie interne Zustandsauflösung/-diagnosen | Endlicher öffentlicher Modellumfang geklärt: funktionales SDK-Maschinenprogramm, eigener neutraler Contractdatenbeitrag N; echte interne Prüfungen erhalten. [C481](CLAIMS.md#c481) |
| Ark UI | Frameworkkomponenten; generiertes API-JSON | TS-Typen/Typecheckpfad, konkrete Zag-Bindung | Ursprüngliches Types-Collection-Schema jetzt identifiziert und tatsächlich ausgeführt. X06 D für API-Metadatenartefakt, [C474](CLAIMS.md#c474) |
| Panda CSS | JS-/TS-Konfiguration; normalisierter JSON-Export | Build-/Configdiagnosen; flacher Exportreader | Originales JSON-Datenmodell mit zusätzlich tatsächlich geprüfter Originaltypbindung; kein nativer Runtime-JSON-Schemavalidator. X06 A, [C477](CLAIMS.md#c477) |
| uSpec | Canonical-/Base-JSON, originale Inline-Schemata | Tatsächliche Ajv-Verwendung plus manuelle Cache-/Evidenceprüfungen | Weite Fachteile, publizierte Schemaadresse am Prüftag nicht erreichbar; load und build prüfen unterschiedlich. X06 D, [C283](CLAIMS.md#c283) |
| OpenPencil | Behaviour-Subartefakt, originales Valibot-Schema | JSON-Decoder verwendet safeParse; zusätzliche Bindungsauflösung | Shapeprüfung ist keine vollständige State-/Referenzprüfung; Export kann Bindungen auslassen. X06 D, [C309](CLAIMS.md#c309), [C393](CLAIMS.md#c393) |
| WAI-ARIA | Normative Web-Semantik, Hostattribute und Beziehungen | Regeln und Host-Wertabbildungen; neutrales Original-A11y-Dateischema nicht belegt | Eigenständige Originalformat-/Schemagrenze der REC1.2 nun N; Hostprüfung separat. [C471](CLAIMS.md#c471) |
| APG | Informativer Guide und HTML/CSS/JS-Beispiele | Reale Linter und Beispielregressionspfade vorhanden | Guide-/Beispieltest-Subjekt mit tatsächlichem Runner abgegrenzt. Eigener neutraler Pattern-Contractschema-Beitrag N, [C482](CLAIMS.md#c482) |
| CSS Layout | CSS-Grammatiken für ausgewählte Module | Sprachliche Parser-/Conformance-Anforderungen belegt | Vier exakte Originalpropertygrammatiken an vorhandenen Lexer zusätzlich gebunden, zwölf Bedingungen ausgeführt. X06 A im engen Profil, [C479](CLAIMS.md#c479) |

## 3. Beschreibung gegenüber zusätzlich nötigem Code

| Kandidat | Beschreibungsform | Zusätzlich nötig / nicht darin bewiesen |
| --- | --- | --- |
| CEM | JSON mit sprachabhängigen Typtexten | Auflösung des gewählten Typsystems und Plattformabbildung; Manifest ist kein Renderer |
| OpenUI | YAML/JSON | Generator-/Runtimebindung und ungeklärter Originalvalidator; Website-TS ist nicht Pflichtsprache des Contracts |
| Google DESIGN.md | Markdown/YAML | JS-/TS-Werkzeugkette, ausgewähltes Ausgabe-/Layoutziel; Prosa besitzt nicht automatisch Token-Verbindlichkeit |
| AgentsORG | Eigener strukturierter Designvertrag | Referenztooling, Ausgabe-/Hostbindung; nicht daraus abgeleitete Behavior-/A11y-Laufzeit |
| DTCG | JSON-Designwerte und Resolverbeschreibung | Konkrete Auflösung/Transformation und UI-Verwendung; kein Komponentenverhalten |
| UXSpec | JSON mit Ausdrucks-/Aktionsmodell | Interpreter, Effects und Renderer; JSON-Parsebarkeit beweist keine identische native Ausführung |
| SCXML | XML | Gewähltes Datenmodell, Interpreter und Host-/Eventbindung; Ausdrücke können zusätzliche Sprache benötigen |
| XState | JS/TS, teils serialisierbare Konfiguration/Definition | Guard-/Action-/Actorimplementierungen und Hostcode; Snapshot speichert nicht automatisch gesamte Logik |
| Zag | TypeScript-/JavaScript-Toolkit | Laufzeit, Frameworkadapter, DOM und zusätzliches Styling; Maschinenname ist kein portabler Vertrag |
| Ark UI | React/Vue/Solid/Svelte-Komponenten und Metadaten | Framework-/Zag-Runtime und Styling; kein neutraler Vier-Domänen-Dateistapel allein daraus |
| Panda CSS | JS/TS-Konfiguration mit Objekten und teilweise Funktionen | Build/Extraktion, CSS-Engine und gegebenenfalls Frameworkwrapper; Export ist nicht verlustfreier Quellvertrag |
| uSpec | JSON-Snapshots/Canonical; Markdown abgeleitet | Figmaextraktion, Interpretation und CLI zur Herstellung; vorgeschlagene Zielplattformen sind keine getesteten Renderer |
| OpenPencil | Gespeicherte Behaviourdaten; TS/Valibot-Definition | Scenegraph-/Preview-/Exportbindung; Web-Interaktion/A11y nicht allein aus Shape ableitbar |
| WAI-ARIA | Normbegriffe und Hostattribute | DOM/Host, korrekt implementiertes Verhalten und Assistenztechnikprüfung |
| APG | Leitfaden plus Web-Beispielcode | Produktvariante und tatsächliche Implementierung; Beispiele sind keine neutrale ausführbare Patternsprache |
| CSS Layout | Deklarative Stylesheets | CSS-/Layoutengine und Element-/Hostbindung; Geometrie benötigt kein zwingendes JS, bleibt aber zielgebunden |

Die Tabelle beschreibt Rollen. Sie ist keine Rangfolge nach Codefreiheit: Ein Interpreter kann für ein Datenformat nötig sein, ohne dass dessen Dokument selbst Funktionen enthält. Ebenso kann ein serialisierbarer Snapshot die notwendige Implementierung nicht vollständig enthalten.

## 4. Reife- und Versionsgegenstand getrennt erfassen

| Kandidat | Gesicherter Gegenstand des gespeicherten Stands | Offene produktive Zusage |
| --- | --- | --- |
| CEM | Gepinntes Schema; Format-README nennt 2.1.0 | Kompatibilität mit konkretem Analyzer, Typsystem und Integrationsprofil praktisch offen |
| OpenUI | draft-01; Websitepaket private 0.1.0 ist andere Versionsachse | Maßgebliche Schemafassung, Toolverfügbarkeit und Migration nicht ausreichend belegt |
| Google DESIGN.md | Alpha-Format; Repo-Werkzeug 0.4.0 | Änderungen ausdrücklich möglich; langfristiger neutraler Vertrag nicht zugesagt |
| AgentsORG | design.v1 / dokumentierter Vertrag 1.3 | Verlustfreier Import und produktive Änderungs-/Integrationsgarantien unabhängig ungeprüft |
| DTCG | Format/Resolver 2025.10, Final Community Group Reports; keine W3C Recommendations | Vollständige konkrete Toolkonformität und plattformgerechte Übersetzung ungetestet |
| UXSpec | Dokument v0.2, Paketdatei 0.2.3 | Compiler-/Schema-/Runtimegleichheit und native Kompatibilität nicht bewiesen |
| SCXML | W3C Recommendation 1.0 von 2015 | Gewählter Interpreter, Datenmodell und UI-Host noch zu bestimmen |
| XState | Core-Paketstand 5.33.3 plus datierte v5-Dokumentation | Neutrales Artefaktformat und dessen langfristige Validierungszusage nicht belegt |
| Zag | Untersuchte Pakete 1.46.0 | Zielprofil-/Frameworkgleichheit und neutrale Austauschkompatibilität nicht bewiesen |
| Ark UI | React-Paketstand 5.39.3, referenzierte Zag-Abhängigkeiten; einzelne Previewkomponenten | Keine pauschale Reifezusage aller Teile/Frameworks; neutrale Schemaversion ungeklärt |
| Panda CSS | Dev-Paketstand 2.4.0, JSON-ExportschemaVersion 1 | Quell-/Exportgleichheit und langfristige neutrale Formatzusage ungeklärt |
| uSpec | Canonical schemaVersion 1.0, Base schemaVersion 1, CLI 0.3.3 | Getrennte Versionsachsen und begrenzte Legacyanpassung; keine generelle Renderer-/Formatgarantie |
| OpenPencil | Scenegraph-Paketstand 0.16.0 | Eigene Behaviour-Formatversion/Migrationsgarantie und vollständiger Roundtrip nicht nachgewiesen |
| WAI-ARIA | 1.2 Recommendation; untersuchte 1.3 Working Draft separat | Normstatus beweist keine Unterstützung jedes Browsers/Screenreaders; native Abbildung offen |
| APG | Informativer Guide; gepinnte Beispielquellen | Keine eigene normative Contract-Konformität; Beispielpaket 0.0.0 ist keine Spezifikationsversion |
| CSS Layout | Anchor Positioning 1 und Overflow 3, ergänzend Media Queries 5 für V03, jeweils getrennte Working-Draft-Stände | Modul-/Checker-/Browserunterstützung genau dieser Kombination ungeprüft |

Es gibt noch keinen vereinbarten produktiven Mindest-Reifegrad. Versionsnummer, Herstellergröße und vorhandene Tests sind keine Produktionsfreigabe. Die Tabelle ist eine datierte Bestandsaufnahme; sie behauptet keinen frisch recherchierten Marktanteil oder umfassenden Supportvertrag.

## 5. Neue präzise Prüflücken

### XState

Der gelesene Konstruktor übernimmt config.schemas in ein unknown-Feld. toJSON liefert eine Maschinendefinition, während Restore auf die vorhandene Maschine und referenzierte Actorlogik zugreift. Daraus folgt weder ein neutraler Originalvalidator noch die Abwesenheit aller externen Validatoren. Historisch X06 U/C405; nach E3-Folgeprüfung N im ausdrücklich abgegrenzten Core, [C464](CLAIMS.md#c464)

### Zag

Die Zustandsindizierung enthält Aufrufe für doppelte Zustands-IDs und ungültige Initialknoten. Die tatsächlich exportierte invariant-Funktion wirft jedoch nur bei NODE_ENV ungleich production; ensure wirft bei null/undefined ohne diese Modusbedingung. **Die pauschale Aussage, sämtliche solchen Fehler würden in jeder Umgebung abgewiesen, wäre falsch.** Dies war der historische Quellbefund. Beide Modi sind nun im veröffentlichten Core 1.46.0 tatsächlich geprüft (C466); nicht mit Arks ausgeliefertem Core 1.45.0 gleichsetzen. X06 bleibt U im breiteren Toolkit.

### Ark UI

Das API-JSON enthält Typausdrücke wie ListCollection<T>, Callbacktexte und Stringdarstellungen von Defaults. isRequired ist Metadatum. Eine Umwandlung in einen neutralen Prüfer müsste Typen, Defaults und Referenzziele erst semantisch festlegen; sie wäre eine neue Ableitung. SDK-Typgegenkontrollen bleiben getrennt; die ursprüngliche Types-Collection liefert nun den konkret ausgeführten API-JSON-Schemanachweis, X06 D/C474.

## 6. Konsequenzen und nächste Nachweise

**Belegte Gesamtfolgerung:** Die Kandidaten besitzen acht direkte Originalschema-Beiträge, zwei konkrete zusätzliche Prüfbindungen A, vier begrenzte N (XState-Core, Zag-SDK-Modell, WAI-ARIA 1.2 und APG-Guide-/Beispieltestpfad) und zwei offene Originalklärungen für X06. Das bedeutet nicht „sieben vollständige Validatoren, neun Projekte ohne Werkzeuge“. Für keine Kombination ist hier eine ausgeführte Vier-Domänen-Validierung belegt.

**Arbeitsvorschlag für die Fortsetzung:** Für einen begrenzten Contractfall zuerst das konkrete Originalartefakt und seinen Prüfungseinstieg bestimmen, dann Struktur, Fachsemantik, Referenzauflösung und tatsächliche Zielausführung einzeln erfassen. Bei Bibliotheken ohne belegtes neutrales Artefakt diese Rolle ausdrücklich offen lassen. Bei ARIA/APG/CSS zunächst Zielprofil und mögliche eigene Ergänzung klären, statt ein nicht belegtes Original-JSON-Schema vorauszusetzen.

Die dokumentarische Vergleichssicht ist vollständig besetzt; externe Schemaidentitäten, tatsächliche Werkzeugversuche und produktiver Mindest-Reifegrad bleiben offen. Die beiden bestätigten Detailvergleiche sind inzwischen dokumentarisch ausgearbeitet: [UXSpec/SCXML](COMPARE-UXSPEC-SCXML.md), [DESIGN.md/Layout](COMPARE-DESIGN-LAYOUT.md). Nach der [Gesamtprüfung aller 72 Ausgangszellen](ALL-FIELDS-REVIEW.md) verbleiben 67 U-Zellen; die neun X06-U bleiben unverändert. Kein Commit in diesem Paket.

**Ergänzende Grenzen der Gesamtprüfung:** OpenPencil besitzt einen neu geprüften konkreten Library-/Revisionsresolver (C411), ohne bewiesenen neutralen Fremdmodellroundtrip. UXSpecs Originalschema enthält im invoke-Pfad überlappende oneOf-Zweige (C416, manuell abgeleitet); der Apppfad kann Mockevents senden und belegt keine allgemeine Invoke-Laufzeit (C415). Das ändert die Existenz eines Originalschemas nicht in einen ausgeführten Konsistenznachweis.

**25.10.2026 – Panda ausgeführt:** 18 Fälle gegen Originalreader/-Index bestätigen Rootteilprüfungen und ungesicherte Zeilen/Referenzen. X06 bleibt U/C442. [Bericht](experiments/2026-10-25/panda-reader/REPORT.md).

**Google nun ausgeführt:** [Originalpaket 0.4.0](experiments/2026-10-25/google-linter/REPORT.md), 20 Fälle. Ein Warnungsreport mit leerem Modell ist kein erfolgreicher Originalcontractnachweis. Selektive Referenzregeln und Datenschema getrennt; X06 bleibt U.
