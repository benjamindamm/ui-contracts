# Ark: Originalschema für API-JSON identifiziert und ausgeführt

Stand: 25. Oktober 2026. **Die endliche offizielle X06-Frage ist für den nun identifizierten API-Metadatengegenstand geklärt. Sechs vorab festgelegte Originalschema-Bedingungen ausgeführt, sämtliche Erwartungen erfüllt.** Ark X06 U → D/C474 im ausdrücklich begrenzten Originalmodell.

## Konkreter Originalpfad

Unveränderter Repo-Pin **c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc**. An den bereits gelesenen Generatorpfad wurde der konkret benannte MCP-Einstieg angeschlossen:

1. packages/mcp/package.json identifiziert den offiziellen MCP-Beitrag und seine Quell-/Transportentrypoints.
2. src/http.ts führt zu server.ts und tools/index.ts; dort sind genau sieben Tools registriert. Alle sieben Handler und die gemeinsamen lib/types.ts-/lib/fetch.ts-Pfade sind gelesen.
3. get_component_props liefert die API-Dokumentationsdaten aus /api/types/<framework>/<component>. Seine Zod-inputSchema prüft framework und component, keinen übergebenen Komponentencontract.
4. Der am selben Commit vollständig gelistete Originalbaum führt zum tatsächlichen Website-Routehandler und zu **website/velite.config.ts**. Der Handler liefert parts aus der originalen Types-Collection.
5. **Diese Collection besitzt ein reales Originalschema für types/**/*.json.** Der zuvor gelesene Generator erzeugt genau solche frameworkbezogenen API-JSON-Dateien. Damit ist ein konkretes Originalartefakt-/Schema-/Prüferpaar vorhanden.

Der Befund ist nicht aus dem bloßen Auftreten einer Zod-/Velite-Abhängigkeit abgeleitet. Die Dateiquelle, der verwendete Collection-Schemakörper, die Originalbibliothek und ihr tatsächlicher Prüferaufruf sind konkret gebunden. Die übrigen SDK-Props, Dokumentationsextraktion und MCP-Anfragevalidierung bleiben getrennte Gegenstände.

## Welches Originalschema hier geprüft wird

website/velite.config.ts definiert das absichtlich unverändert geschriebene Originalsymbol **PropDefintion**:

- type muss ein String sein.
- isRequired muss Boolean sein.
- defaultValue und description sind optionale Strings.

Die Types-Collection ist ein Record aus Teilen. Jeder Teil hat einen props-Record aus diesen Metadaten; element/tag sind optionale Strings, emits ist optional und verwendet denselben Metadatengegenstand. Eine originale Transformationsstufe ergänzt parts, component und framework aus Dateimetadaten.

**Das sind Metadaten einer Komponenten-API, keine tatsächlichen Laufzeitwerte von open, value oder collection.** Das Schema prüft beispielsweise, dass ein Typtext ein String ist. Es löst nicht automatisch ListCollection<T>, Callbacktypen, Fremdreferenzen oder eine öffentliche Eventpayloadsemantik auf. Diese begrenzte Regelabdeckung verhindert den D-Befund nicht: Ebenso wird ein ursprüngliches Typtextfeld bei anderen Originalschemas nicht erst durch eine universelle Typauflösung zum Schema.

## Tatsächlicher Prüfaufruf ohne Schemareimplementierung

Die offizielle Website-Paketdefinition bindet **velite 0.4.0**. Genau diese Originaldistribution wurde ohne Installationsskripte isoliert installiert, mit Lock/Registryintegrity und Dateihashes gebunden. TypeScript 5.9.3 isoliert per AST die drei unveränderten Originaldeklarationen normalizePath, PropDefintion und types aus der vollständigen gelesenen Quelle. Ihre Quellenpositionen und Hashes sind in extraction.json gespeichert.

Die Originaldeklarationen werden mit den echten velite.s-/defineCollection-Exporten ausgewertet; keine ersetzten Schemas/Validatorfunktionen, keine zusätzlichen Fachregeln. Aufgerufen wird das vollständige originale **types.schema.safeParse**, einschließlich seiner originalen Metadatentransformation. Dateimetadaten path/basename werden kontrolliert für die gepinnte React-Combobox-Datei bereitgestellt. Das ist Prüfharness-Kontext, kein nachgebauter Validator. Die originale Velite-Parserimplementierung unterstützt diesen meta-Kontext ausdrücklich.

Kein kompletter Next-/Website-/Velite-Dateiladebuild, keine MCP-Serverinitialisierung und kein Abruf der Live-Dokumentations-API ausgeführt. Die NPM-Transitivauflösung ist im eigenen Lock reproduzierbar gebunden, aber nicht pauschal mit dem ursprünglichen Bun-Website-Lock gleichgesetzt. Node v24.22.1.

## Sechs Bedingungen

Die Kontrolle verwendet das tatsächlich gepinnte combobox.types.json mit 16 Teilen. Negative Varianten sind definierte Einzelmutationen dieses Originalinputs. Originaldatei/Varianten werden über Quellhash, Eingabehash und gespeicherte Mutationsregel reproduziert.

| Eingabe | Beobachtung |
| --- | --- |
| Originales API-JSON | Akzeptiert; ursprüngliche Transformation liefert component=combobox, framework=react, 16 Teile |
| isRequired als String | invalid_type, erwarteter Boolean |
| type als Zahl | invalid_type, erwarteter String |
| Root.props fehlt | Required-Fehler am props-Ort |
| defaultValue als Boolean | invalid_type, erwarteter String |
| Frei erfundener Typtext als String | Akzeptiert; keine fachliche Typausdrucksvalidierung behauptet |

Alle sechs Erwartungen erfüllt. results.json erhält die tatsächlichen Fehlerpfade und die Akzeptanz der bewusst opaken Typzeichenfolge. Keine Erwartung nachträglich geändert. Keine fremde Domäne in das Originalformat eingebaut.

## MCP-Schemas haben einen anderen Gegenstand

| Originaltool | Tatsächliche Eingabeart |
| --- | --- |
| list_components | Frameworkauswahl |
| list_examples | Framework und Komponentenname |
| get_example | Framework, Komponentenname, Beispiel-ID |
| get_component_props | Framework und Komponentenname |
| styling_guide | Komponentenname |
| search_docs | Suchtext |
| get_docs | Dokumentations-Slug |

Die Handler liefern Dokumentation, Beispiele oder JSON als Text. Die gemeinsame Fetchfunktion liest JSON und verwendet eine TypeScript-Zusage; dies ist keine Runtimeprüfung der Rückgabedaten gegen das Types-Collection-Schema. Der laufende Dienst wird im Quellcode über eine veränderliche API-Adresse angesprochen; **unsere** Quellen und Prüfeingaben sind dagegen auf den Repo-Pin gebunden. Keine Behauptung über den gerade live ausgelieferten Inhalt oder die Vollständigkeit seiner serverseitigen Builds.

## X06-Bewertung und nicht behauptete Unterstützung

**Ark UI X06: D/C474** für den originalen separaten API-JSON-Metadatenbeitrag mit seinem Original-Collection-Schema. Ein unveränderter Originalprüfpfad ist nun identifiziert und an gültigem/fehlerhaftem Originaldatenformat ausgeführt. Der gemeinsame Collection-Code beschreibt die vier Frameworkmetadaten; **die ausgeführte Kontrollinstanz hier ist React-Combobox**, keine Prüfung aller Komponenten oder Frameworkdateien.

D ist keine Zusage neutraler Runtime-Props-/Behavior-/Accessibility-Gesamtcontracts, vollständiger Referenzsemantik, Migration, eines stabilen SchemaVersion-Feldes oder Produktions-/AT-Konformität. Arks Repository-5.39.3/Zag1.46.0-Quellen und die früher isoliert untersuchte NPM-5.39.3/Zag1.45.0-Distribution bleiben weiterhin verschiedene Originalstände. Kein Beleg wird zwischen ihnen verschoben.

Die bisher offene Frage nach einem ursprünglichen Schema des API-JSON ist damit **durch einen konkreten Fund und Aufruf** geklärt, nicht durch eine weichere Auslegung von SDK-Typchecks. Die früheren U-Claims behalten ihren historischen fehlenden Beleg; die nun vollständiger erschlossene offizielle Datenpipeline liefert genau diesen zusätzlichen Originalnachweis.

Aktuell **51 U: 31 Integration und 20 weitere**. X06 jetzt **8 D, 2 begrenzte N, 6 U**. Gesamt **336 Bedingungen/43 Gruppen**. Keine neue Produktentscheidung, Produktionskomponente, Commits oder Pushes.

## Reproduktion und Quellen

Manifest bindet Repo-Dateien/URLs, vollständige gelesene Originalfassungen, Extraktionspositionen, Velite-Distribution/Lock und Inputs. Originalcode/Original-API-JSON anhand dieser Pins in sources/velite.config.ts und sources/combobox.types.json bereitstellen. run-schema.cjs isoliert den Schemaquellkörper selbst; cases.json enthält die sechs vorab gesetzten Eingriffe/Erwartungen. Der bereits verwendete TypeScript-5.9.3-Ordner wird benötigt. tool/package-lock.json mit npm ci --ignore-scripts reproduzieren. Originalquellen werden nicht als eigene Projektimplementierung ausgegeben oder vollständig mitverteilt.
