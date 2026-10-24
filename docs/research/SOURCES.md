# Quellenregister

Abrufdatum aller Quellen: **23. Oktober 2026**, BrowserOS neo. Primärquellen liefern technische Informationen; der Originalchat liefert Anforderungen und historische Vorschläge. Diese Rollen dürfen nicht vertauscht werden.

Die Quellen wurden selektiv in den unten genannten Abschnitten geprüft, nicht als vollständiger Audit aller Projekte. Gepinnte Links beziehen sich auf sichtbare letzte Commits der jeweiligen Datei. Die Inhalte wurden über die zugehörige `main`-Ansicht gelesen; vor einem ausführbaren Versuch muss der gepinnte Abruf nochmals verglichen werden. Bei Websites ist der Abrufzeitpunkt der belegte Stand, kein erfundener Release.

| ID | Quelle | Konkreter Stand | Gelesener Umfang |
| --- | --- | --- | --- |
| S01 | [CEM](https://github.com/webcomponents/custom-elements-manifest/blob/2570079a0525c26296f9ec39944f0c6e0f0461af/schema.d.ts) | Dateicommit 2570079a0525c26296f9ec39944f0c6e0f0461af; kein behaupteter Paketrelease | Package, Reference, CustomElement, Event, Type, PropertyLike |
| S02 | [OpenUI Specification](https://openuispec.org/spec) | draft-01; Website ohne unveränderlichen Snapshot | §7 Format, §8 Discovery, §10 Best Practices, §11 Future Plans |
| S03 | [Google DESIGN.md](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/docs/spec.md) | alpha; Dateicommit 6e5da5382f41edbba9d73b2c62f33f32e9971f15 | Schema, Token References, Layout, Components/Variants |
| S04 | [AgentsORG DESIGN](https://github.com/AgentsORG/DESIGN/blob/014a1864c641f8e9792ed76de93c95493489dd8c/SPEC.md) | design.v1, dokumentierter Vertrag 1.3; Dateicommit 014a1864c641f8e9792ed76de93c95493489dd8c | §1–3, §7.3 Themes, §11.3 Referenzen, §13 Components, §19 Validation |
| S05 | [DTCG Format](https://www.designtokens.org/TR/2025.10/format/) | Format Module 2025.10; Final Community Group Report, 28.10.2025 | Token Properties, Types, Aliases/References |
| S06 | [DTCG Resolver](https://www.designtokens.org/TR/2025.10/resolver/) | Resolver Module 2025.10; Final Community Group Report, 28.10.2025 | Abstract, Syntax, Contexts/Modifiers und Auflösung |
| S07 | [UXSpec Spezifikation](https://github.com/johnlindquist/uxspec/blob/41c37aad700ae2a7756934f5131e0c23964b45da/spec/SPEC.md) | v0.2; Dateicommit 41c37aad700ae2a7756934f5131e0c23964b45da | Context, Events, Actions, Transitions, Visual, Layout, Element References |
| S08 | [UXSpec JSON Schema](https://github.com/johnlindquist/uxspec/blob/f788d5ebed734f3a24d7aae38e6d2f969dc6e80e/schema/uxspec.schema.json) | Dateicommit f788d5ebed734f3a24d7aae38e6d2f969dc6e80e | required, stateNode, machine, transition, elementBase, $imports |
| S09 | [SCXML](https://www.w3.org/TR/2015/REC-scxml-20150901/) | SCXML 1.0, W3C Recommendation 01.09.2015 | §3 Zustände/Transitions, §4 Executable Content, §6.4 invoke, Anhänge Datenmodelle |
| S10 | [XState](https://stately.ai/docs/machines) | Veränderliche Dokumentation, Abruf 23.10.2026; kein Paketrelease festgestellt | Creating a state machine, Providing implementations, Reusing machines |
| S11 | [Zag](https://zagjs.com/overview/introduction) | Veränderliche Dokumentation, Abruf 23.10.2026; kein Paketrelease festgestellt | Introduction, Why Zag |
| S12 | [Ark UI](https://ark-ui.com/docs/guides/composition) | Veränderliche Dokumentation, Abruf 23.10.2026; kein Paketrelease festgestellt | asChild, ID Composition, Limitations |
| S13 | [Panda CSS](https://panda-css.com/docs/recipes/overview) | Veränderliche Dokumentation, Abruf 23.10.2026; kein Paketrelease festgestellt | Recipes, base/variants/defaultVariants/compoundVariants |
| S14 | [uSpec](https://github.com/redongreen/uSpec/blob/bee78db1fed0d8c5d988fa1bff5651561b5c79ab/README.md) | README-Dateicommit bee78db1fed0d8c5d988fa1bff5651561b5c79ab; Übersichtsprüfung | Introduction, What you can generate |
| S15 | [OpenPencil Behaviours](https://openpencil.dev/development/behaviours-and-preview) | Veränderliche Dokumentation, Abruf 23.10.2026; kein Paketrelease festgestellt | The model, Authoring surfaces, Preview islands |
| S16 | [WAI-ARIA](https://www.w3.org/TR/2023/REC-wai-aria-1.2-20230606/) | WAI-ARIA 1.2, W3C Recommendation 06.06.2023 | Abstract, combobox, aria-controls, aria-activedescendant, aria-live |
| S17 | [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) | Veränderlicher Praxisleitfaden, Abruf 23.10.2026 | Varianten, Keyboard Interaction, Roles/States/Properties |
| S18 | [CSS Anchor Positioning](https://www.w3.org/TR/2026/WD-css-anchor-position-1-20260327/) | Level 1, Working Draft 27.03.2026 | Abstract, anchor-name, position-anchor, anchor(), anchor-size() |
| S19 | [CSS Overflow](https://www.w3.org/TR/2025/WD-css-overflow-3-20251007/) | Level 3, Working Draft 07.10.2025 | Abstract, overflow/overflow-x/overflow-y |

## Identitäten und Rollen

- OpenUI ist hier `openuispec.org`, nicht die Komponentenforschung unter `open-ui.org`. Die geprüfte Seite verweist im Kopf auf `specui/openui`, am Ende auf `ctate/openui`; Repository-Weiterleitung und maßgebliches Schema sind noch zu klären. Nicht ungeprüft einen anderen gleichnamigen Kandidaten einsetzen.
- Google DESIGN.md ist `google-labs-code/design.md`, nicht lediglich eine Datei im Stitch-Skills-Projekt.
- AgentsORG DESIGN ist ein eigener visueller Vertrag und kein Alias für Google DESIGN.md.
- UXSpec ist `johnlindquist/uxspec`; uSpec ist das andere Projekt `redongreen/uSpec`.
- OpenPencil Behaviours ist anhand seiner Entwicklungsdokumentation und des dort benannten `@open-pencil/scene-graph`-Modells identifiziert. Eine konkrete Paketversion ist noch nicht gepinnt.
- WAI-ARIA ist eine Semantikspezifikation; APG ein Praxisleitfaden mit Varianten und Bedienmustern. DTCG Format und Resolver sind Community Group Reports, keine W3C Recommendations.
- XState, Zag, Ark und Panda sind ausführbare Werkzeuge beziehungsweise Bibliotheken, keine schon dadurch sprachneutralen Austauschstandards.
- CSS Anchor Positioning und Overflow sind ergänzende Layoutmodelle für den bestätigten Detailvergleich; ihre Aufnahme entscheidet keine Web-Bindung des Contract-Pakets.

## Kontextquellen ohne technische Bewertung

[Originalgespräch](https://chatgpt.com/share/6adba3c9-accc-83ed-adbf-a78f5a880760): vollständig als Text gelesen, 71 Nachrichten; Download-Anhänge nicht geprüft. OpenSpec und Requirements as Code sind im Original als Kontext genannt, ohne eindeutig identifiziertes Projekt. Sie erhalten keine erfundene Kandidatenbewertung. Figma, HTML, PNG und OpenPencil waren mögliche Ausgaben; die spätere Präzisierung priorisiert zunächst das Contract-Paket.

Der Originalchat nennt auch einen [Salesforce-Beitrag](https://www.salesforce.com/blog/coding-agents-product-design/). Dessen Zahlen und Funktionsbehauptungen wurden hier nicht übernommen oder nachgeprüft. Tailwind ist ein vorhandener Stack-/Syntaxbezug; Flexbox und Grid sind weitere noch vertiefend zu prüfende Layoutbezüge.

## Grenzen und erfolglose Pfade

Eine zunächst versuchte Ark-Adresse `/docs/overview/composition` lieferte 404; die gültige, aus der Navigation gefundene Quelle ist S12. Panda `/docs/theming/semantic-tokens` lieferte 404; daher wurde Dark-Mode-Abdeckung für Panda noch nicht bewertet. Solche Zugriffsprobleme sind kein Nachweis fehlender Fähigkeiten.

## Integrität der lokal gelesenen Extraktionen

Die folgenden SHA-256-Werte beziehen sich auf lokal vom Browser extrahierte Lesefassungen einschließlich Browser-Markierungen, nicht auf die Originaldateibytes. Die vollständigen fremden Texte werden nicht in diesem Repository reproduziert. Die Hashes erleichtern den lokalen Audit der Recherche, ersetzen aber keine veröffentlichte Quellversion. Bei dynamischen Seiten können Navigationstexte und Markierungen variieren.

| Quelle | SHA-256 der gelesenen Lesefassung |
| --- | --- |
| S01 | `23b29a6b5ff2bf6776522426ff477c48711f3516cae3288658236a69d5d69e2b` |
| S02 | `e546058a2f213a68e78586f7b5bbe256d600a3d830fd8276411c7ebadbb6b74d` |
| S03 | `c01c8984a05f9a870483b369f64bd1775951b095564e67e7d120eb6b30786741` |
| S04 | `12cea47caa80a3de49e73cc313065c4ab85733f71cb99d77cb3bb1aef32ff94b` |
| S05 | `346c7affeba3ac1437c109efabf0f4423e4b1e2cdfbb3d08d05f829b0138a7a5` |
| S06 | `f5e6f4cdbdc6281f77350042675a3bd2cf723b5df2c1d0155dda4db572f41a77` |
| S07 | `6e6755037758fc94d52bbc88b318db4ed91d31eef5434560e534eaf2d3ee648b` |
| S08 | `5caff5fe878ff8fba062afb55047db7932dc76757052b76fc32cd1dffcf6d707` |
| S09 | `15152505493e1cbee60aad1ba93664bbf8490ef4f2436e8dcacf4854c8d7a09d` |
| S10 | `73e31ee7a8dc990ab2e2de6249830f1c5fa9c64410a4970cf7ac742844d82ffb` |
| S11 | `4f935700e84ffa75900f0fa2954236fc0853599dbbc463919f9d7e10a84df134` |
| S12 | `6e17dd83c76bc13bea0689bf1c65c0203fede00c026e62ba1145c67a9784a377` |
| S13 | `d69fc0a847cf8b4700097b77aca5cc7c64ca00f927a0917bd4214cf06930f47a` |
| S14 | `f29c51d64b33ec696004a7664a4bf9b371fb24b4790b8c08485bc4823b7d8d29` |
| S15 | `e15fc10108ed6d753efe5af28cdc72c540d7357830a8c75d0f7fa6cb6f205c1d` |
| S16 | `858caf38d7830986b1f02b5d95aae75d01b0b33464119419279ff8c50fb39fea` |
| S17 | `03a6acbcedd7a73dc0aca9c03eca3b802b089dd5bdbe8a3212fe18d65ab28772` |
| S18 | `fb0f98c1d92e195412849adc1856b26c1c7f5138b6f7ad93e35d8fefbcf3c21f` |
| S19 | `7cf449ca9de4341b3c303b08868917e1a1675f610119c5a6d4580b8548575ea5` |

## CEM-Vertiefung am 23. Oktober 2026

S01 wurde jetzt zusätzlich über den unveränderlichen Commit gelesen, vollständig einschließlich sämtlicher deklarierter Typen und Kommentare. Rohansicht: https://raw.githubusercontent.com/webcomponents/custom-elements-manifest/2570079a0525c26296f9ec39944f0c6e0f0461af/schema.d.ts . Der Befundumfang wird damit von ausgewählten Feldern auf den vollständigen dort definierten CEM-Kern erweitert. Die übrigen Kandidaten wurden in diesem Schritt nicht erneut untersucht.

| ID | Quelle | Konkreter Stand | Gelesener Umfang |
| --- | --- | --- | --- |
| S20 | [CEM JSON Schema](https://github.com/webcomponents/custom-elements-manifest/blob/2570079a0525c26296f9ec39944f0c6e0f0461af/schema.json) | Commit 2570079a0525c26296f9ec39944f0c6e0f0461af; JSON Schema Draft-07 | Vollständige Definitionen, Root, Pflichtfelder, Eigenschaftstypen und Schema-Referenzen |
| S21 | [CEM Format-README](https://github.com/webcomponents/custom-elements-manifest/blob/d2f79f0d22c4d48a68628cf867c2319576ffc5d2/README.md) | Commit d2f79f0d22c4d48a68628cf867c2319576ffc5d2; nennt Schema 2.1.0 und Tag v2.1.0 | Schemaimport, package.json.customElements, Schema Versioning; Use Cases nur als historische Ziele, insbesondere alte React-Aussagen nicht als heutige Fakten übernommen |
| S22 | [Open-WC Analyzer Configuration](https://custom-elements-manifest.open-wc.org/analyzer/config/) | Veränderliche offizielle Werkzeugdokumentation; Abruf 23.10.2026, keine Paketversion festgestellt | CLI/Config, dependencies und Analyzing dependencies; strikt vom CEM-Format getrennt |
| S23 | [CSS-Wertsyntax als CEM-Verweisziel](https://www.w3.org/TR/2024/WD-css-properties-values-api-1-20240326/) | CSS Properties and Values API Level 1, Working Draft 26.03.2024 | Typisierte registrierte Properties und Syntaxstrings; nur Einordnung der von CEM benannten Wertsemantik, keine neue Kandidatenbewertung |

Die Abgrenzung negativer Befunde lautet: Im vollständig gelesenen Standardkern sind die entsprechenden Zielarten, Relationen oder Ausführungsregeln nicht definiert. Beliebige zusätzliche JSON-Felder werden dadurch weder verboten noch standardisiert. Analyzer-Plugins können weitere Metadaten liefern; das ist ohne eigenes dokumentiertes Fachmodell kein Nachweis einer Standardfähigkeit. Referenzauflösung im installierten Projekt und Version-Locking über npm sind ebenfalls vom Manifestformat zu trennen.

Zusätzliche lokale Lesefassungs-Hashes nach derselben eingeschränkten Bedeutung wie oben:

| Quelle | SHA-256 |
| --- | --- |
| S01 (pinned) | `7955d6fedbc1cfbd53fd9e9948db5af23e777129f7ef195d98a94759ac9499e1` |
| S20 | `1edc11d8346595bc89f03fb85fe2369175be300affc1a6cc35d9662aa8899b1b` |
| S21 | `5a19788d9bfb4c08d72022cf4cb41f32293429dd3502853769f32db58b74e4a9` |
| S22 | `1cd2cf4540e536ccb045cc37adf4e78b28c8c483d54699605b916ed15981fe62` |
| S23 | `211854789978ce4350c774ae8bcae3ac607308d03769f287b0ccd7acf50da203` |

## DTCG-Vertiefung am 23. Oktober 2026

S05 (Format 2025.10) und S06 (Resolver 2025.10) wurden getrennt erneut konsultiert. Bei Format wurden Token-/Gruppenstruktur, Erweiterungen, Gruppenvererbung, Alias-/Pointerauflösung, Typen und zusammengesetzte Typen abgeglichen. Bei Resolver wurden Root, Sets, Modifier/Kontexte, Reference Objects, Extensions, Schemahinweis, Inputs, Resolution und Bundling abgeglichen. Gruppennamen besitzen keine implizite Komponentenbedeutung; transition-Tokens enthalten Animationsparameter. Die gesamte definierte Modellstruktur wurde außerdem mit den folgenden veröffentlichten Schemata abgeglichen. Das ist keine Aussage vollständiger Implementierungs- oder Schemakonformität.

| ID | Quelle | Konkreter Stand | Gelesener Umfang |
| --- | --- | --- | --- |
| S24 | [DTCG Format Schema](https://www.designtokens.org/schemas/2025.10/format.json) | Versionierter URL-Pfad 2025.10, Abruf 23.10.2026; deklariert JSON Schema Draft-07 | Root, Token-/Gruppen-/Referenzdefinitionen, TokenType und sämtliche Werttypen; manuelle E2-Prüfung |
| S25 | [DTCG Resolver Schema](https://www.designtokens.org/schemas/2025.10/resolver.json) | Versionierter URL-Pfad 2025.10, Abruf 23.10.2026; deklariert JSON Schema Draft-07 | Root, version/resolutionOrder, Sets, Modifier und Referenzobjekte einschließlich eingebetteter Formatdefinitionen; manuelle E2-Prüfung |

S24/S25 sind auf der offiziellen Domain veröffentlichte Schemahilfen. Der Formatbericht enthält weiterhin einen redaktionellen Hinweis zur Ergänzung eines JSON Schemas; das veröffentlichte Formatschema kennzeichnet sein $schema-Feld selbst als außerhalb der offiziellen Formatdefinition. Deshalb werden Bericht, Schemahilfe und tatsächlicher Resolver bewusst nicht gleichgesetzt. Externe Referenzen in einem JSON Schema laden Schemadefinitionen und sind nicht automatisch die Auflösung externer Tokenquellen.

Resolver §4.2 verlangt Referenzen im selben Dokument, erlaubt aber unterschiedliche Werkzeugunterstützung für lokale Dateien und Netzwerk-URIs. Resolver §4.1.2 version bezeichnet den Spezifikationsstand und bindet nicht die Inhaltsversion aller referenzierten Tokenquellen. Herstellerdaten in $extensions sind erlaubt beziehungsweise zu erhalten; daraus entsteht keine zusätzliche standardisierte UI-Semantik.

Lokale Lesefassungs-Hashes (gleiche eingeschränkte Bedeutung wie oben):

| Quelle | SHA-256 |
| --- | --- |
| S24 | `9b24c11b4b14492d11c8ceb11602a6fc2892916ee18b291dc1d668eea218e28f` |
| S25 | `d144355a851361adfee2ce5e86d21917627efcf55d930274259676cade95a203` |

## SCXML-Vertiefung am 23. Oktober 2026

S09 wurde erneut am datierten Recommendation-Dokument gelesen: §3 Core Constructs einschließlich Events, Transitions und IDs; §4 Executable Content/Erweiterungen; §5 Data/param/content und Systemereignisse; §6 send/invoke/finalize; Anhänge A/B/C/D/E sowie die dortige Abgrenzung der Schemaprüfung. Für die negativen Kernbefunde wurden die definierten Zielarten und Elementfamilien abgeglichen, nicht nur einzelne Schlagwörter gesucht. Zusätzliche Host-/Erweiterungssemantik wird nicht automatisch dem Standard zugeschrieben.

| ID | Quelle | Konkreter Stand | Gelesener Umfang |
| --- | --- | --- | --- |
| S26 | [W3C SCXML-XSD-Driver](https://www.w3.org/2011/04/SCXML/scxml.xsd), [Core](https://www.w3.org/2011/04/SCXML/scxml-module-core.xsd), [Data](https://www.w3.org/2011/04/SCXML/scxml-module-data.xsd), [External](https://www.w3.org/2011/04/SCXML/scxml-module-external.xsd), [Strict-Driver](https://www.w3.org/2011/04/SCXML/scxml-strict.xsd) | Offizielle /2011/04/SCXML-Pfade; Abruf 23.10.2026. Anhang E der Recommendation verweist auf diese Schemata; kein Interpreterrelease behauptet | Driver-Includes und deklarierte Core-/Data-/External-Elemente samt Attributen manuell gelesen. Strict-Driver gelesen, dessen komplette abhängige strenge Module nicht geprüft/ausgeführt. Kein XSD-Validierungslauf |
| S27 | [SCXML Recommendation Errata](https://www.w3.org/2015/08/scxml-errata.html) | Beim Abruf ausgewiesener letzter Stand 28.12.2016, Abruf 23.10.2026 | Bekannte redaktionelle Korrekturen E1–E7, insbesondere Datenmodellbeschreibung und Ereignisbeispiele; kein Laufzeitnachweis |

Anhang E ist informativ und unterscheidet das lockerere Schema-1.0-Set von Schema 1.1 mit Assertions. Im Recommendation-HTML zeigt der als scxml-strict.xsd beschriftete Link auf scxml.xsd; deshalb wurde zusätzlich der ausdrücklich beschriftete Strict-Pfad direkt geöffnet. Seine Existenz ist belegt, eine vollständige strengere Validierungskette nicht. Das lose Schema enthält zulässige Strukturen, die nicht jede Einschränkung der Recommendation ausdrücken; einzelne XSD-Defaults dürfen nicht ungeprüft die normative Semantik ersetzen.

E2 bedeutet Sichtprüfung der Schemadefinitionen. Es wurde kein Interpreter untersucht, kein Dokument praktisch validiert, kein externer Dienst ausgeführt und kein Runtime-/Kompositionsversuch vorgenommen. Anforderungen an Konformität eines Prozessors und Anforderungen an ein SCXML-Dokument sind getrennt zu lesen.

Lokale Lesefassungs-Hashes nach der oben erläuterten eingeschränkten Bedeutung:

| Quelle | SHA-256 |
| --- | --- |
| S09 (erneut) | `d2344ad79bbe3ec7460a1bbbf33697d785c27162e88a1fb072ff9ac2bcb41392` |
| S26 Core | `4d468337bc2809d54559a24efd8e0c92d385b906dadfa8ab5561f9e193cd727c` |
| S26 Data | `629138ef7b63f397c6e474c20cc2435bf082810b17ee1f27225c3c03715a8d15` |
| S26 External | `8f19202e729f54456c3f09802aa592ace22a64575818b370b822ce16856ea83f` |
| S27 | `449ec04a7e0412033045523b656932e3a2532f8ca06aff10ede0f284a464f824` |

## XState-Vertiefung – abgeschlossen am 24. Oktober 2026

Quellenabruf am 23. Oktober 2026. Die Dokumentation ist eine veränderliche v5-Dokumentation; der gelesene Core ist über den vollständigen Commit fixiert. Keine Runtime- oder SCXML-Kompatibilität aus Repository-Schlagwörtern beziehungsweise Testabhängigkeiten ableiten.

| ID | Primärquelle | Gelesener Umfang und Grenze |
| --- | --- | --- |
| S28 | [Core-Paketmetadaten](https://github.com/statelyai/xstate/blob/8f25b68f3953a9dd3c146a76f1f4972aba092a3f/packages/core/package.json), [types.ts](https://github.com/statelyai/xstate/blob/8f25b68f3953a9dd3c146a76f1f4972aba092a3f/packages/core/src/types.ts), [StateMachine.ts](https://github.com/statelyai/xstate/blob/8f25b68f3953a9dd3c146a76f1f4972aba092a3f/packages/core/src/StateMachine.ts) | Commit `8f25b68f3953a9dd3c146a76f1f4972aba092a3f`; package.json: 5.33.3. SetupTypes, StateNodeConfig, MachineConfig, Event-/Actor-Typen sowie Konfiguration/Implementierungen, schemas und Versionmetadaten manuell betrachtet. Keine vollständige Codeprüfung und keine Ausführung |
| S29 | [Setup](https://stately.ai/docs/setup), [Input](https://stately.ai/docs/input), [Context](https://stately.ai/docs/context) | Typdeklarationen, Actor-Input, initialer Context und Context-Updates. TypeScript-Prüfung ist keine Runtime-JSON-Schemaprüfung |
| S30 | [Guards](https://stately.ai/docs/guards), [Actions](https://stately.ai/docs/actions) | Funktionssemantik, Reihenfolge, benannte/parametrisierte Implementierungen, Effekte und eingebaute Aktionen. Namen serialisieren nicht die Implementierung |
| S31 | [Actors](https://stately.ai/docs/actors), [Invoke](https://stately.ai/docs/invoke) | Instanzen, Kommunikation, invoke/spawn, Eingaben und Lebenszyklen, Host-Ereignisquellen. Actor-Komposition beweist keine vollständige UI-Komposition |
| S32 | [Event emitter](https://stately.ai/docs/event-emitter) | emit, actor.on und separat typisierte emitted-Events; Feature laut Dokumentation seit 5.9 |
| S33 | [Persistence](https://stately.ai/docs/persistence) | Persistierter Snapshot, Wiederherstellung mit passender Actor-Logik, Serialisierungsgrenzen. Snapshot ist keine vollständige portable Maschinenbeschreibung |

Die negativen Core-Befunde beruhen auf dem definierten Konfigurations-/Typumfang und den beschriebenen Zielarten. Freies meta, Effektausführung oder registrierte Actor-Namen erhalten dadurch keine standardisierte UI-/Visual-/Accessibility-Semantik. `schemas: unknown` wird ausdrücklich nicht als vorhandene Validierungsfunktion gewertet. Alle verbleibenden U-Zellen besitzen konkrete Fragen in CLAIMS.md.

## Zag-Vertiefung am 24. Oktober 2026

Alle folgenden Quellen wurden am 24. Oktober 2026 über BrowserOS neo gelesen. Version 1.46.0 wurde in den gepinnten Core-/Combobox-Paketdateien festgestellt; die aktuelle Komponentendokumentation zeigte ebenfalls 1.46.0. Das ist keine pauschale Stabilitäts- oder Kompatibilitätszusage. Gepinnter Repositorystand: `cafda74ba915d5abc5abb20abdde3a719d8e4e9c`, als letzter Hauptzweig-Commit vom 23. Oktober sichtbar.

| ID | Primärquellen | Gelesener Umfang / Grenze |
| --- | --- | --- |
| S34 | [Introduction](https://zagjs.com/overview/introduction), [Building Machines](https://zagjs.com/guides/building-machines), [gepinnte Anleitung](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/website/data/guides/building-machines.mdx) | TS-Maschinen, Context, Props, Guard-/Action-/Effect-Beispiele; offizielle ausdrückliche SCXML-Abgrenzung. Keine Laufzeit |
| S35 | [Core-Typen](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/core/src/types.ts), [createMachine](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/core/src/create-machine.ts), [Zustandsindex/-auflösung](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/core/src/state.ts), [Core-Paket](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/core/package.json), [React-Maschinenausführung](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/frameworks/react/src/machine.ts), [Framework Adapters](https://zagjs.com/guides/framework-adapters), [gepinnte Adapteranleitung](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/website/data/guides/framework-adapters.mdx) | MachineSchema/Machine/Service/Scope/Transition, Initialisierung, interne Zustandsprüfungen; exemplarisch React-Auswahl, Action-/Guard-Ausführung, Effects/Cleanup und Lifecycle. Keine vollständige Prüfung anderer Frameworks, Typechecker oder Runtime |
| S36 | [Combobox-Typen](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.types.ts), [Anatomie](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.anatomy.ts), [DOM-IDs und Abfragen](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.dom.ts), [Combobox-Paket](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/package.json) | Öffentliche Props/Callback-Details, ElementIds/Teile, IDs aus Instanz und Teil, Paketversion 1.46.0. Keine Prüfung aller Komponenten-APIs |
| S37 | [Combobox](https://zagjs.com/components/react/combobox), [connect](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.connect.ts), [Maschine](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.machine.ts) | Props/Callback-Mapping, Tastatur-/Fokus-/IME-Bindung, ARIA/Label-Referenzen, APG-Verweis und Tastaturdokumentation, Positionierung und Ergebnisansagen. Relevante Quelltextabschnitte manuell gelesen; kein vollständiges Konformitätsaudit |
| S38 | [Styling](https://zagjs.com/guides/styling), [Composition](https://zagjs.com/guides/composition) | Zustands-/Teilattribute und externe CSS-Beispiele, Props-Merging, eindeutige id/ids, gemeinsame Trigger, Warnung vor konfigurierten aber nicht gerenderten ARIA-Zielen. Veränderliche Dokumentation, keine ausgeführte Komposition |
| S39 | [PositioningOptions](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/utilities/popper/src/types.ts), [Platzierungsberechnung](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/utilities/popper/src/get-placement.ts), [Floating-Styles](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/utilities/popper/src/get-styles.ts), [Middleware](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/utilities/popper/src/middleware.ts) | Anchor/Placement/Offset, Dimensionen, Boundary, fitViewport, maxWidth/maxHeight und verfügbare CSS-Pixelwerte. Gebündeltes Web-Hilfsmodell über Floating UI; keine neutralen Layoutartefakte und keine Geometrieversuche |
| S40 | [Scroll Area](https://zagjs.com/components/react/scroll-area), [ScrollArea-connect](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/scroll-area/src/scroll-area.connect.ts) | Scroll-/Overflow-API, Parts, overflow:auto, Achsen und Scrollbarzustände; kein Nachweis vollständiger Overlay-Einbettung oder Flächenbegrenzung nach Zeilenzahl |
| S41 | [LiveRegion-Implementierung](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/utilities/live-region/src/index.ts) | aria-live/atomic, role, Nachrichtenverzögerung/Ersetzung, cancel/destroy und DOM-Anbindung manuell gelesen. Keine tatsächlichen Screenreaderansagen getestet |

**Abgrenzung:** Die Zag-Spalte umfasst das benannte Toolkit mit seinen konkret genannten Hilfspaketen, nicht allein @zag-js/core. Ein D in einer konkreten Komponente oder einem Hilfspaket wird nicht als Eigenschaft jeder Maschine ausgegeben. Stylingbeispiele nutzen externes CSS; deshalb R für V02. Die restlichen vier Fachmodelle und deren Ownership werden nicht automatisch durch DOM-Bindungen ersetzt. Fehlende neutrale Artefaktvalidierung und ungeklärte Komposition bleiben U, nicht N.

Ein zunächst vermuteter alter Pfad packages/combobox wurde durch den auf der offiziellen Komponentenseite verlinkten packages/machines/combobox-Pfad korrigiert. Auch vermutete Dateien transition.ts, use-machine.ts und live-region.ts existierten an den versuchten Orten nicht; stattdessen wurden die tatsächlichen state.ts, React machine.ts und LiveRegion index.ts gelesen. Diese 404-Antworten begründen keine negative Bewertung. Einige Extraktionskopfzeilen zeigten nach Navigation noch die vorherige URL; Zuordnung erfolgte anhand angeforderter gepinnter Ziel-URL und tatsächlich extrahierten Dateiinhalts.

**Prüfgrenze:** Nur Dokumenten-/Quelltextarbeit. Kein Kandidat installiert, keine Compiler-/Schema-/Laufzeitversuche, kein Overlay/ScrollArea aufgebaut. Die vorgemerkte zusätzliche Untersuchung von Validierungs-Tooling, Beschreibungssprache und Reifegrad aller Kandidaten wird hier nicht als erledigt ausgegeben.

## Zentrale Quellenfortschreibung Google DESIGN.md und OpenUI – 24. Oktober 2026

Die beiden separat gelieferten Rechercheberichte wurden zentral fachlich abgeglichen. Die folgende Zuordnung ersetzt ihre lokalen Quellenkürzel durch globale IDs. Primärdefinitionen wurden selektiv erneut über BrowserOS neo gelesen; beide Formatspezifikationen vollständig, dazu Typ-/Schemaobjekte und zentrale Werkzeugpfade. Keine neuen Praxis-/Laufzeitversuche. Beide Projekte bleiben Kandidaten, keine Auswahl für produktiven Einsatz.

| ID | Primärquellen | Stand und Prüfumfang |
| --- | --- | --- |
| S42 | [SPEC: vollständige Spezifikation](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/docs/spec.md), [README: Status, Format und Tooling](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/README.md) | Google DESIGN.md, Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15. Alpha-Kern: Typen, alle Sections, Components/Variants, lokale Referenzen und unbekannte Inhalte. Tokens sind normativ, Prosa Kontext. README nennt alpha und Änderungsrisiko. |
| S43 | [PARSER](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/packages/cli/src/linter/parser/spec.ts), [MODEL](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/packages/cli/src/linter/model/spec.ts) | Derselbe Commit. ParsedDesignSystem, SCHEMA_KEYS, DesignSystemState/ComponentDef, ResolvedValue und Validierungshelfer manuell gelesen. ParserInputSchema prüft einen nichtleeren Contentstring; TS-Interfaces sind kein vollständiges Runtime-Schema. |
| S44 | [HANDLER](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/packages/cli/src/linter/model/handler.ts), [LINT](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/packages/cli/src/linter/lint.ts), [API](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/packages/cli/src/linter/index.ts), [PACKAGE](https://github.com/google-labs-code/design.md/blob/6e5da5382f41edbba9d73b2c62f33f32e9971f15/packages/cli/package.json) | Derselbe Commit, Werkzeug 0.4.0/Node >=18/ESM. Parser → Model → Linter und öffentliche API; Kollisions-/Tokenreferenz-/Wertprüfungen und Component-Propertyspeicherung selektiv gegengelesen. Unbekannte Component-Properties bleiben zulässig. Keine Installation/Ausführung und keine Garantie jeder Fehlerabweisung. |
| S45 | [P: Website-Entwurf](https://openuispec.org/spec), [S: vollständiger draft-01](https://github.com/ctate/openui/blob/09d39b211dcaa2e227ed38e312c8822e193cfea9/versions/draft-01.md) | OpenUI Snapshot 09d39b211dcaa2e227ed38e312c8822e193cfea9; Websiteentwurf draft-01. Vollständiger begrenzter Datenumfang §§7–9, Empfehlungen §10, Zukunft §11. Nicht Open UI. Laut separatem Bericht zeigt die Repositoryübersicht diesen Stand mit Commitdatum 11.12.2025; kein eigener Aktualitäts-/Wartungsnachweis daraus. |
| S46 | [T: Spec-Interface](https://github.com/ctate/openui/blob/09d39b211dcaa2e227ed38e312c8822e193cfea9/interfaces/Spec.ts), [F: Schema-Beschreibung](https://github.com/ctate/openui/blob/09d39b211dcaa2e227ed38e312c8822e193cfea9/lib/schema.ts) | Derselbe Snapshot; beide Dateien vollständig manuell gelesen. T verlangt etwa license/group und enthält enum/required nicht; F ist eine Feldbeschreibung mit unter anderem type:any und Platzhaltern. Nicht ungeprüft als kanonisches ausführbares JSON Schema interpretieren. |
| S47 | [Q: Websitepaket](https://github.com/ctate/openui/blob/09d39b211dcaa2e227ed38e312c8822e193cfea9/package.json), [D: Schematabellenrenderer](https://github.com/ctate/openui/blob/09d39b211dcaa2e227ed38e312c8822e193cfea9/components/schema-table.tsx), [W: Spec-Seite](https://github.com/ctate/openui/blob/09d39b211dcaa2e227ed38e312c8822e193cfea9/app/spec/page.tsx), [R: gepinnter rekursiver Pfadbaum](https://api.github.com/repos/ctate/openui/git/trees/09d39b211dcaa2e227ed38e312c8822e193cfea9?recursive=1) | Q/D/W zentral erneut gelesen: private Next-Webanwendung 0.1.0, YAML-Parser, Tabellenrendering und Darstellung von versions/draft-01.md. R wurde im separaten Bericht vollständig mit truncated:false gelesen, zentral nicht erneut vollständig erhoben. Kein nachgewiesener eigenständiger Contract-Validator; keine vollständige Inhaltsprüfung aller Dateien. |

**Zusatzkriterien als eng begrenzter Befund für diese zwei Kandidaten:** Google beschreibt Markdown/YAML, seine CLI/Library ist JS/TS. Vorhandenes angebotenes Lint-Tooling und ein vollständiges unabhängiges Originalschema sind getrennte Fragen; letzteres bleibt U. OpenUI beschreibt YAML/JSON; der Next/TS-Code seiner Website ist keine Pflichtsprache des Contracts und kein Validatornachweis. Alpha beziehungsweise draft-01 sind die belegten Spezifikationsstände; 0.4.0 beziehungsweise Website-0.1.0 sind andere Versionsgegenstände. Produktreife und belastbare Kompatibilitäts-/Migrationszusagen bleiben unbewiesen. Diese Auswertung erledigt nicht den vorgemerkten Zusatzvergleich für alle anderen Kandidaten.

**Provenienz:** Die Berichte lagen als /private/tmp/ui-contracts-designmd-review.md und /private/tmp/ui-contracts-openui-review.md vor. Entscheidend sind die obigen gepinnten Primärquellen und die dokumentierten Grenzen, nicht die Berichtsaussagen allein. Die früheren offenen Kurzbefunde C05 und C10 sind als historisch markiert und verweisen auf die aktuelle Einordnung. Keine neuen Dokumente oder Laufzeitprüfungen im Projekt erforderlich.

## Quellenrunde AgentsORG / UXSpec / Ark UI – 24. Oktober 2026

Drei ausdrücklich beauftragte Agenten erstellten getrennte Berichte außerhalb des Repos. Zentral erfolgte der Abgleich mit den operationalisierten Kriterien, bisherigen Zellen und Evidenzrollen. Die unten aufgeführten gepinnten Primärquellen tragen die Befunde; Berichte allein sind kein technischer Nachweis. Insbesondere wurde der AgentsORG-Schema-/Linterpfad zentral anhand der gesicherten Originalauszüge gegengelesen. UXSpec- und Ark-Quellprüfungen wurden durch die jeweiligen Recherche-Agenten dokumentiert; kein unabhängiger vollständiger Zweitaudit behauptet.

## S48

**AgentsORG: Primärquellen und lokale Fundstellenkürzel.**

Alle Fachquellen auf Commit **014a1864c641f8e9792ed76de93c95493489dd8c**. Die offizielle GitHub-API `/commits/main` wurde am 24. Oktober 2026 erneut gelesen und zeigte weiterhin genau diesen Hauptzweigstand; Commitdatum 5. September 2026. Repository nennt **design.v1, Vertrag 1.3 / v1.3.0**. Der vorherige vollständige Bericht wurde zuerst gelesen und als Recherchevorarbeit verwendet. Für die jetzige fachliche Gegenprüfung wurden SPEC, Originalschema, Linter und README am gepinnten Stand erneut über BrowserOS neo geöffnet. Die relevanten vollständigen Definitionen und Ausführungspfade wurden manuell gegengelesen; keine erneute Vollerhebung aller Projektdateien.

- **SPEC:** [SPEC.md](https://github.com/AgentsORG/DESIGN/blob/014a1864c641f8e9792ed76de93c95493489dd8c/SPEC.md), vollständig gelesen, besonders §§1–7.4, 11–15, 18–24.
- **SCHEMA:** [schema/design.v1.schema.json](https://github.com/AgentsORG/DESIGN/blob/014a1864c641f8e9792ed76de93c95493489dd8c/schema/design.v1.schema.json), vollständige Struktur gelesen: Draft 2020-12, required/properties/$defs, Komponenten, Tokens, Integrations- und Policyfelder.
- **LINT:** [scripts/lint_design.py](https://github.com/AgentsORG/DESIGN/blob/014a1864c641f8e9792ed76de93c95493489dd8c/scripts/lint_design.py), vollständig gelesen; `lint`, Referenzschleifen und `main`.
- **README:** [README.md](https://github.com/AgentsORG/DESIGN/blob/014a1864c641f8e9792ed76de93c95493489dd8c/README.md), Statusabschnitt aus Repositoryansicht: released/design.v1/current contract 1.3, Referenzskripte vorhanden, paketierte Standalone-CLI geplant. Die sichtbare HEAD-Identität wurde abgeglichen.
- **SCRIPTS:** [scripts-Verzeichnis](https://github.com/AgentsORG/DESIGN/tree/014a1864c641f8e9792ed76de93c95493489dd8c/scripts), Existenz von lint/export/diff/convert-Skripten bestätigt. Export- und Diffimplementierungen wurden nicht vollständig geprüft und erhalten keinen Laufzeitnachweis.


## Zusatzkriterien für produktive Nutzung

**Format versus Programmcode:** YAML 1.2 oder JSON desselben Objekts, bevorzugte Endung `.design`. Visuelle Daten unabhängig von JS/React. Prosa und freie Decisionbedingungen erfordern Interpretation durch Agenten; keine formal portable Verhaltenssprache. Optionale Brücken zu shadcn/Figma und weitere Exportziele sind eigene Integrationen. Referenztools sind Python; LINT importiert PyYAML und jsonschema. Keine Installation oder Versionskompatibilität dieser Abhängigkeiten getestet.

**Originalschema versus tatsächliches Tooling:** Originales JSON Schema Draft 2020-12 liegt separat vor und wird vom vorhandenen Linter über Draft202012Validator benutzt. Schema deckt Struktur/Typmetadaten ab, ist an zahlreichen Stellen offen: tokenNode akzeptiert beliebige Strings/Zahlen, policy.accessibility beliebige Eigenschaften. Es beweist keine gültige Farbe, semantisch konsistente Domänenbindung oder vollständige Fachkonformität. Der Linter ergänzt konkrete lokale Referenz-/Zyklus-/Alias-/Tiefenprüfungen und einige Kontrast-/Vollständigkeitswarnungen. Sein main-Einstieg scannt fest Repositorybeispiele und Templates statt beliebiger CLI-Dateiargumente; `lint(path, validator)` ist eine Pythonfunktion, eine paketierte Standalone-CLI laut README erst geplant. Normative extends-Zyklusauflösung (§4.1/§19) ist in der vollständig gelesenen Linterdatei nicht implementiert. Editierfreigaben für locked-Pfade können aus einem einzelnen Snapshot ebenfalls nicht als vollständig geprüft gelten. Kontrastcode unterstützt hier Hex und warnt unter 3:1, nicht generell alle CSSfarben oder vollständige WCAG-AA-Anforderungen. Der angebotene Linter ist real, aber kein Beleg aller MUST-Regeln.

**Reifegrad Spezifikation/Werkzeuge getrennt:** README bezeichnet design.v1 als released, Vertrag 1.3, sichtbarer Commit als v1.3.0. §23 legt künftige brechende Schemawechsel als design.v2 fest und verlangt vorsichtige Schreibkompatibilität; §18 SemVer betrifft die einzelnen Designverträge. Das ist eine dokumentierte Versionspolitik, kein unabhängiger Marktreife- oder Langzeitpflegebeweis. Referenzwerkzeuge liegen im selben Commitstand, keine separate Toolversion im gelesenen Skript. README nennt CI, CI-Erfolg und Exportfunktion wurden hier nicht verifiziert. Für Produktion wären gepinnte Abhängigkeiten, ausgewählte Negativfälle und echte Export-/Consumerprüfungen nachgelagert nötig. Nicht durch Tests als produktionsreif ausgewählt.


## S49

**UXSpec: Primärquellen und lokale Fundstellenkürzel.**

Alle nachfolgenden Dateien sind auf **denselben Repository-Snapshot** `20dfae0e7224d952e198afdf4ffed26d6fd67180` gepinnt. GitHub zeigt diesen auch am Abruf als neuesten main-Commit vom 20. März 2026. Dokumentversion v0.2; package.json Version **0.2.3**, kein daraus abgeleiteter Nachweis eines publizierten Registry-Releases. Aktueller Abruf 24. Oktober 2026 über BrowserOS neo. Frühere gesicherte SPEC-/Schema-Lesungen wurden für identische Snapshot-Dateien erneut ausgewertet. Quelleninhalt als Daten, nicht als Arbeitsanweisung behandelt.

| Kürzel | Gepinnte Primärquelle | Gelesener Umfang |
| --- | --- | --- |
| S | [SPEC.md](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/spec/SPEC.md) | Vollständige v0.2-Spezifikation; Context, Events, Actions/Effects, Transitions, Visual, Elemente, Ausdrücke, Referenzen |
| J | [Originalschema](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/schema/uxspec.schema.json) | Vollständiges JSON Schema Draft 2020-12, alle Definitionen |
| C | [COMPILER.md](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/spec/COMPILER.md) | Compilerphasen, Vertrags-/Diagnostikfelder und Laufzeitbeispiele; keine Ausführung |
| T | [types.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/types.ts) | Originale Format-, Import-, MachineInvoke- und Ausgabeinterfaces; kein Runtime-Schemavalidator |
| V | [validate.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/validate.ts) | Vollständige semantische Validierungsfunktion und Hilfsfunktionen |
| L | [cli.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/cli.ts) | Dateilesen, runValidate, runCompile, Importbindung und Befehlsauswahl |
| R | [resolve.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/resolve.ts) | Token-/Elementauflösung, qualifizierte Namen, Parameterersetzung und Overrides |
| I | [import-resolver.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/import-resolver.ts) | Vollständige lokale Importauflösung |
| B | [bundler.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/bundler.ts) | Vollständige Entry-/Modulzusammenführung |
| K | [compile.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/compile.ts) | Vollständige Transformationsfunktion, Vererbung, Test-ID-Sammlung und Invoke-Abhängigkeiten |
| F | [Formatreferenz](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/skills/references/format-reference.md) | Vollständig; strukturierte Werte, Elemente, Slots, Interaktionen |
| U | [Runtime-Semantikreferenz](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/skills/references/runtime-semantics.md) | Vollständig; Daten, Bindungen und ARIA-Metadaten |
| E | [Kompositionsbeispiel](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/examples/07-composable-app/app.uxspec.json) | Vollständige Import-/Element-/Invoke-Deklaration; Beispiel nicht ausgeführt |
| W | [Web-Styleadapter](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/app/src/lib/render/style-map.ts) | Vollständiger Adapter; eigene Web-Konventionen nicht als normative neutrale Layoutsprache gewertet |
| A | [Web-Interpreter](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/app/src/lib/engine/interpreter.ts) | Kontextinitialisierung, Ereignisablauf, Effects und Store; keine Laufzeitprobe und kein vollständiger Adapteraudit |
| P | [package.json](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/package.json) | Vollständig; Version, Scripts, Engines, Build- und Entwicklungspakete |
| M | [README](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/README.md) | Produktziel, Composability und Status; durch GitHub-Repoansicht gelesen und gegen Snapshot-HEAD abgeglichen |


## Getrennte Zusatzkriterien

### Originalschema gegenüber tatsächlich vorhandenem Tooling

**Offizielles Schema vorhanden:** J deklariert Draft 2020-12; Rootpflichten, Typmetadaten, event payload, Importfelder, Transitionformen, Machine/State-Struktur und Container-/Leafunterscheidung sind strukturiert. Es ist kein vollständiges Semantikschema: `$tokens`, `aria`, container und keyboard sind überwiegend object; expr erlaubt nichtleere Arrays ohne vollständige Operator-/Arityprüfung; context.default ist beliebig; Strings für Referenzen prüfen kein existierendes Ziel. Kontext-`type` prüft die Typmetadaten, nicht automatisch den Typ von default oder späteren Laufzeitwerten. Mehrere zusätzliche Eigenschaften sind erlaubt. Außerdem können permissive oneOf-Zweige etwa bei Elementen/Invoke Überlappungen erzeugen; **kein konkretes Validierungsergebnis behaupten**, da nicht ausgeführt.

**Werkzeug vorhanden:** P/L/V zeigen CLI `validate` plus validateSpec. Es liest JSON und führt manuelle Semantikprüfungen aus; es lädt **nicht das veröffentlichte JSON Schema**. V prüft unterstützte Operatornamen, deklarierte context.-Variablen, deklarierte Übergangs-/emit-Ereignisse, Kontextpräfix bei assign, Initial-/Übergangsziele und entry/exit-Aktionen. Nicht alle spezifizierten Regeln werden in dieser Funktion abgedeckt: z.B. keine vollständige Eventpayload-Pfad-/Wertetypprüfung, keine Arity-/Typprüfung der Operanden, kein gesamter Element-/ARIA-/Visual-/Defaultcheck. `options.imports` wird übergeben, ist aber in V nicht zur vollständigen domänenübergreifenden Validierung genutzt.

**Compiler ist weiterer Pfad:** K/R lösen Token-/Elementreferenzen und Zustände auf, expandieren Parameter, behandeln Invoke-Abhängigkeiten und sammeln Test-ID-Existenzassertions. `compile()` importiert/ruft **validateSpec nicht**; L runCompile ruft compile direkt. Deshalb darf man CLI validate, JSON-Schema-Konformität und Compilererfolg nicht gleichsetzen. `assertions` prüft hier erwartete Elementexistenz, keine automatische Accessibility-/Verhaltenskonformität. Existierender Code und Herstellerbeispiele beweisen kein erfolgreiches Ausführen. Kein Tool wurde installiert oder ausgeführt.

### Format/Sprache und zusätzlich nötiger Code

- Originalaustauschformat: UTF-8 JSON, `.uxspec.json`, JSON-Operatorarrays; YAML nicht als Originalformat nachgewiesen.
- Behaviorbeschreibung braucht für die dokumentierten eingebauten Kinds keine benutzerdefinierten JavaScript-Funktionen.
- Werkzeuge: Compiler/CLI TypeScript, Node-APIs; Paket engines Node >=18, Repo-Scripts über Bun. Paketversion 0.2.3.
- Ausführung erfordert einen Interpreter, Effects-/Hostbindung und Renderer. Der vorhandene Referenzadapter ist eine Next/React-Webapp; ein JSON-Dokument wird nicht allein durch Parsebarkeit zur ausführbaren SwiftUI-/Compose-/Slint-Implementierung. Native Ziele sind Anspruch/Mappingbeispiele, keine hier verifizierten Lieferungen.
- Behauptete SCJSON-Nähe und DTCG-Anlehnung sind kein verifizierter vollständiger Standardimport/-export. Ausnahmen/Übersetzung müssen separat geprüft werden.

### Reifegrad von Spezifikation und Werkzeugen

M nennt „Active specification“, bezeichnet die visuelle Schicht als „stable“ und v0.2 Runtime-Semantik als neu normativ mit Feedbackbedarf. Das sind **Selbsteinstufungen**, keine unabhängige Produktions-/Marktreifeprüfung. Dokument v0.2, Paketdatei 0.2.3, Snapshot oben. C enthält eine eng begrenzte additive Kompatibilitätsaussage zu optionalen Tracefeldern für ältere Consumer; daraus keine allgemeine SemVer-/Format-/Runtime-Kompatibilitätszusage ableiten. S dokumentiert SHOULD-Aliasse für Legacyfelder ohne hier ermittelte verbindliche Migrationsfrist. Werkzeuge/Referenzapp sind als Quelltext vorhanden; Installierbarkeit, veröffentlichte Artefakte, Maintenanceservice, cross-platform-Konformität und Stabilität nicht praktisch geprüft. Sichtbare GitHub-Releases waren leer; kein pauschales Urteil über eine Registry getroffen.


## S50

**Ark UI: Primärquellen und lokale Fundstellenkürzel.**

Alle Quellen am 24.10.2026 über BrowserOS neo gelesen. Dokumentation ist veränderlich; Code ist gepinnt.

- **AR01 – Rolle und Styling:** [About](https://ark-ui.com/docs/overview/about), [Styling](https://ark-ui.com/docs/guides/styling). Ark baut auf Zag auf; funktionale Positionierungsstyles im Toolkit, Präsentationsgestaltung extern; state-/part-Selektoren, CSS-Beispiele. React/Vue/Solid/Svelte sind JS-Frameworkbeiträge, kein Swift-/Angular-/Native-Nachweis.
- **AR02 – API und Muster:** [Combobox](https://ark-ui.com/docs/components/combobox). Anatomie, typed Props/Callbacks, id/ids, positioning, translations, RootProvider/useCombobox, APG-Verweis, Tastaturtabelle, Available-Size-CSS. Nicht die Marketingaussage zur Konformität als Testergebnis behandeln.
- **AR03 – Komposition:** [Composition](https://ark-ui.com/docs/guides/composition), [Scroll Area](https://ark-ui.com/docs/components/scroll-area). asChild mit einem Kind, Props-/Verhaltensmerging, ID-Sharing Avatar/Tooltip; Warnung vor falschem Basiselement. ScrollArea-Teile, Achsen, verschachtelte Instanzen, benötigtes CSS.
- **AR04 – Ark-Stand:** [Commit](https://github.com/chakra-ui/ark/commit/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc), [React package.json](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/package.json), [React CHANGELOG](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/CHANGELOG.md). GitHub main beim Abruf: Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc vom 20.10.2026; React-Paketversion 5.39.3, Changelog nennt 05.10.2026. Paket referenziert Zag-Pakete ausdrücklich mit 1.46.0. Nur gelesener Repo-Paketstand, kein Registry-/Installationsnachweis. Scripts enthalten tsc/typecheck und Testwerkzeuge; deren Ausführung wurde nicht geprüft.
- **AR05 – Ark-Adapter:** [useCombobox](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/combobox/use-combobox.ts), [Root](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/combobox/combobox-root.tsx), [RootProvider](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/combobox/combobox-root-provider.tsx), [Input](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/combobox/combobox-input.tsx), [Anatomie](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/combobox/combobox.anatomy.ts). Manuell vollständig gelesen. useId, optionale explizite ids, Field-/Locale-/Environmentanbindung, `useMachine(combobox.machine, machineProps)`, connect/normalizeProps, individuelle Providerwerte; Root trennt explizite Machine-Props von DOM-Props.
- **AR06 – Typmetadaten und Vue-Events:** [generiertes React-API-JSON](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/website/src/content/types/react/combobox.types.json), [Vue-Typen](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/vue/src/components/combobox/combobox.types.ts), [Vue Root](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/vue/src/components/combobox/combobox-root.vue). API-JSON enthält Teile/props/type/isRequired/defaultValue/description; Typen sind zum Teil Typausdrücke als Strings. RootEmits ordnet Eventnamen wie valueChange/inputValueChange/openChange strukturierten Zag-Detailtypen zu; defineEmits bindet sie. Das API-JSON ist kein nachgewiesenes JSON Schema für UI Contracts.
- **AR07 – unabhängige ScrollArea:** [useScrollArea](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/scroll-area/use-scroll-area.ts), [Viewport](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/scroll-area/scroll-area-viewport.tsx). Eigene useId-/Props-/useMachine-Instanz, eigener Kontext, getViewportProps und DOM-Prop-Merging. Keine ausgeführte Overlay-/ScrollArea-Komposition.
- **AR08 – tatsächlich referenziertes Zag-Modell:** [Combobox-Typen](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.types.ts), [Maschine](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.machine.ts), [Connector](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/combobox/src/combobox.connect.ts), [Popper-Typen](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/utilities/popper/src/types.ts), [ScrollArea-Connector](https://github.com/chakra-ui/zag/blob/cafda74ba915d5abc5abb20abdde3a719d8e4e9c/packages/machines/scroll-area/src/scroll-area.connect.ts). Bestehender Zag-Prüfstand erneut selektiv gelesen; im Projekt S36/S37/S39/S40. Props/Callbackdetails und Translations, Initialzustand/Transitions/Guard- und Actionimplementierungen, Ereignis-/Contextdaten, ARIA-/Key-Mapping, Ergebnisansagen, getAnchorElement/placement/gutter/offset/fitViewport und overflow:auto. Dies ist ein referenzierter Zag-Repo-Stand der Version 1.46.0, kein ausgepackter npm-Tarball und kein zusätzlicher Kompatibilitätstest.
- **AR09 – begrenzte Schemarecherche:** [gepinnter rekursiver Ark-Pfadbaum](https://api.github.com/repos/chakra-ui/ark/git/trees/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc?recursive=1). Antwort `truncated:false`; Pfade nach schema sowie relevanten Komponenten-/Typdateien gesichtet. Keine Datei mit schema im Pfad gefunden. Kein Beweis, dass es außerhalb dieser Suche keinerlei Validator gibt. Zusammen mit AR04/AR06 bleiben Originalschema und neutraler Artefaktvalidator ungeklärt.


## Vorgemerkte Zusatzkriterien: Teilbefunde, kein neuer Gesamtvergleich

### Schema und Tooling getrennt

Es gibt ein konkretes generiertes JSON für Props-/API-Dokumentation und TS-Schnittstellen. Das JSON enthält stringförmige Typausdrücke und beschreibt API-Dokumentation, nicht automatisch ein ausführbares JSON Schema. `typecheck: tsc` ist ein vorhandener Entwicklerwerkzeugaufruf, kein dokumentierter neutraler Vier-Domänen-Artefaktvalidator. Validierbarkeit von generischen Item-Payloads, callback-/DOM-Referenzen, instanzübergreifenden IDs und externen Fachmodellversionen wurde nicht nachgewiesen. X06 bleibt deshalb U. Auch ein JSON Schema würde Cross-Domain-Semantik nicht allein garantieren.

### Format und zusätzlich nötiger Code

Gelesene Ark-Implementierung: TS/TSX sowie Vue-SFC mit TS; Distribution laut Paket ESM/JS und Typen. API-Metadaten: JSON, aber Typausdrücke als Text. Verwendung benötigt Framework-/Zag-Laufzeit, Komponentenaufbau, Funktionen für Filter/Callbacks/Übersetzungen je nach Bedarf und externes CSS. YAML-/JSON-only-Ausführung und sprachneutrale komplette Verhaltenssemantik sind nicht nachgewiesen. Das vorhandene API-JSON ist eine mögliche Quelle für spätere Extraktion, keine bereits ausgewählte Contractserialisierung.

### Reife und Kompatibilität

Ark React trägt im gepinnten Stand die reguläre Version 5.39.3 ohne alpha/beta-Suffix; Changelog dokumentiert fortlaufende Reparaturen, unter anderem Accessibility- und Frameworkunterschiede. Das ist stärkerer Wartungsnachweis als eine reine Projektankündigung, aber keine eigenständige formale Contractstandard-Stabilitätszusage. Einzelne Komponenten sind auf der Website als Preview markiert; daraus nicht das ganze Paket pauschal als experimentell oder jeden Teil als stabil einstufen. Keine langfristige Schema-/Austauschformat-Kompatibilitätsgarantie gefunden; keine solche Garantie behaupten. Die genaue zugesicherte Breaking-Change-/Supportpolitik und die Gleichheit aller vier Frameworkadapter bleiben eine begrenzte Folgefrage. Keine Produktionsreifeentscheidung oder Technologieauswahl aus dieser Quellenprüfung ableiten.


Diese Ergänzungen sichern kandidatenbezogene Zusatzbefunde. Der vorgemerkte Gesamtvergleich zu Schema/Tooling, Sprache/Code und Reifegrad ist damit weiterhin nicht vollständig erledigt. Für alle drei: E1/E2, keine Installation oder ausgeführte Kandidaten-/Validator-/Laufzeitprüfung. Lokale Vorarbeiten lagen unter /private/tmp/ui-contracts-{agentsorg,uxspec,arkui}-review-current.md; die dauerhaften Nachweise sind nun die obigen Primärquellen und die verlinkten Claims.

## Quellenrunde Panda CSS / uSpec / OpenPencil – 24. Oktober 2026

Drei getrennte Recherche-Agenten prüften die folgenden offiziellen Quellen und Originaldefinitionen. Zentral wurden Berichte, Kriterien, Quellenrollen und bisherige Bewertungen abgeglichen; kein vollständiger unabhängiger zweiter Quellaudit behauptet. Die globalen Sammel-IDs lösen die lokalen Kürzel der Einzelbefunde vollständig auf. Alle Nachweise E1/E2; keine ausgeführten Kandidaten-/Validator-/Compiler-/Laufzeitversuche.

## S51

**Panda CSS: Primärquellen und lokale Fundstellenkürzel.**

Alle Webquellen über BrowserOS neo gelesen. Aktueller Defaultbranch ist **v2**, nicht main. GitHub-API lieferte für main 422, also keinen fehlenden Projektstand daraus abgeleitet. **Pin P = 86f78a228204d63baa0b8bca2676d9f26190e449**, Commit 23.10.2026 20:21:05 UTC. [Commit](https://github.com/chakra-ui/panda/commit/86f78a228204d63baa0b8bca2676d9f26190e449). Dokumentationsseiten sind veränderlich; mehrere zeigen Aktualisierung 21.10.2026. Aktueller Repo-Paketstand @pandacss/dev **2.4.0**, Node >=22. Kein Registry-Tarball oder Installationsnachweis.

- **P01** [Tokens](https://panda-css.com/docs/theming/tokens), [Token-TS-Typen am Pin](https://github.com/chakra-ui/panda/blob/86f78a228204d63baa0b8bca2676d9f26190e449/packages/types/src/tokens.ts). value/description, TokenDataTypes, Border/Shadow/Gradient, SemanticTokens. Farben bleiben Strings; keine behauptete vollständige Einheiten-/Farbvalidierung. DTCG-Anlehnung der Dokumentation ist keine verifizierte vollständige DTCG-Konformität.
- **P02** [Slot Recipes](https://panda-css.com/docs/recipes/slot-recipes), [Rezepttypen am Pin](https://github.com/chakra-ui/panda/blob/86f78a228204d63baa0b8bca2676d9f26190e449/packages/types/src/recipe.ts). slots, per-slot base/variants/compoundVariants, RecipeSelection/RecipeVariantProps, Klassenmap. Vollständige Typdatei gelesen, keine Instanz-IDs daraus abgeleitet.
- **P03** [Multiple Themes](https://panda-css.com/docs/theming/multiple-themes), [Conditional Styles](https://panda-css.com/docs/styling/conditional-styles). base/_dark, dark-Klasse im base preset, data-panda-theme, staticCss.themes für Ausgabe. SemanticTokens unterstützen at-rule-/parent-selector-Bedingungen, nicht beliebige Kind-/Pseudozustände. Alte /docs/theming/semantic-tokens liefert weiterhin 404; der Inhalt steht unter Tokens.
- **P04** [Position Try](https://panda-css.com/docs/styling/position-try), [Layout](https://panda-css.com/docs/reference/layout), [Sizing](https://panda-css.com/docs/reference/sizing), [Patterns](https://panda-css.com/docs/theming/patterns), [Layout Patterns](https://panda-css.com/docs/styling/patterns). CSS anchor()/positionAnchor/positionTryFallbacks, inset/spacing, maxHeight/maxWidth, overflowX/Y auto/hidden im ScrollArea-Muster. Das Pattern benötigt eine JS-transform-Funktion. Float hat placement/offset relativ zum positionierten Elternteil. Native CSS-Bedeutung, keine neutrale Geometriesprache.
- **P05** [JSON Spec](https://panda-css.com/docs/theming/json-spec), [Exporttypen am Pin](https://github.com/chakra-ui/panda/blob/86f78a228204d63baa0b8bca2676d9f26190e449/packages/compiler-shared/src/design-system-spec/types.ts), [Reader am Pin](https://github.com/chakra-ui/panda/blob/86f78a228204d63baa0b8bca2676d9f26190e449/packages/compiler-shared/src/design-system-spec/read.ts). DesignSystemSpec mit schemaVersion, tokens/values/conditions/themes sowie optionalen Rezept-/Pattern-/Quellentabellen; parseDesignSystem ausdrücklich flache Strukturprüfung, Zeilen werden vertraut.
- **P06** [Presets](https://panda-css.com/docs/theming/presets), [Design Systems](https://panda-css.com/docs/design-systems/overview), [Headless Wrapping](https://panda-css.com/docs/design-systems/wrap-headless-libraries). Presetimporte, Merge-Reihenfolge; Komponenten plus Konfiguration über panda lib; Frameworkkomposition mit createSlotRecipeContext/withProvider/withContext und Ark-Komponenten. Frameworkkomponenten bleiben zusätzlicher Code.
- **P07** [Diagnostics](https://panda-css.com/docs/reference/diagnostics), [Config](https://panda-css.com/docs/reference/config), [CLI-Flagschema am Pin](https://github.com/chakra-ui/panda/blob/86f78a228204d63baa0b8bca2676d9f26190e449/packages/cli/src/schema.ts). validation none/warn/error; Token- und Designsystemfehler, Warnungen normalerweise kein Fehlerexit. Flagschema ist für CLI-Argumente, kein Contract-JSON-Schema.
- **P08** [dev package am Pin](https://github.com/chakra-ui/panda/blob/86f78a228204d63baa0b8bca2676d9f26190e449/packages/dev/package.json), [vollständiger Pfadbaum am Pin](https://api.github.com/repos/chakra-ui/panda/git/trees/86f78a228204d63baa0b8bca2676d9f26190e449?recursive=1). Tree truncated:false, Schema-/Designsystem-/Token-/Paketpfade gesichtet. Dies ist eine begrenzte Suchstrategie, kein Nachweis, dass nirgendwo ein JSON Schema existiert.


## Schema, Tooling und Ausführung getrennt

**Eingabe:** Panda-Konfiguration in TypeScript/JavaScript mit defineConfig; statische Objekte für Tokens/Rezepte, zusätzlich Funktionen etwa für Patterns und Wrapper. TS-Typen sind keine unabhängige JSON-Schema-Validierung. **Export:** codegen/build/lib --spec erzeugt DesignSystemSpec schemaVersion 1. Es ist ein normalisierter Dokumentations-/Toolingindex, kein verlustloses Originalformat: Recipe-Einträge enthalten Variantenmetadaten, nicht sämtliche base-/variant-CSS-Körper; Pattern-default-Funktionen und Regexmatcher besitzen keine vollständige Serialform, composition-Einträge nur Beschreibungsmetadaten. Eine Übernahme des Exports als vollständiges Visualcontract wäre deshalb verfrüht.

**Reader E2:** parseDesignSystem prüft JSON-Parse, Rootobjekt, Vorhandensein categories/paths/tokens/values, Arrays für paths/values, numerisches schemaVersion und lehnt Versionen größer 1 ab. Er prüft weder jede Zeile noch Referenzintegrität, Geometrie, Payloadtypen oder Cross-Domain-Konflikte. Er akzeptiert auf Quelltextebene jede numerische Version <=1; daraus keine komplette historische Kompatibilitätsgarantie ableiten. Typen und Reader manuell gelesen, nicht ausgeführt.

**Compiler-/Configdiagnosen E1:** validation default warn, none/warn/error konfigurierbar; fehlende Tokenwerte, fehlende/zyklische/self-Referenzen und Artefaktnamenkonflikte sind dokumentiert. Warnungen ändern regulär den Exitcode nicht, max-warnings kann CI-Grenze setzen. Dokumentation unterscheidet PostCSS von Vite (Vite meldet als Warnung und schlägt nicht fehl). Es gibt konkrete Werkzeuge, aber deren Existenz ist kein erfolgreicher Validatorversuch. CLI schema.ts beschreibt Flags, nicht das fachliche JSON-Artefakt.

**Code/Ausgabe:** CSS-Ziel benötigt CSS-Engine/DOM, Buildtoolchain für Extraktion und Codegen. Statische CSS-Ausgabe benötigt nach Dokumentation nicht die JSON-Spec-Datei. Komponentenverhalten und Accessibility kommen im Wrapperbeispiel aus Ark, nicht aus Token-/Recipe-Dateien. Beschreibungsformat, Buildprogramm, Frameworkcode und Browsersemantik getrennt halten.

## Reife und Kompatibilität

Paketversion 2.4.0 ohne prerelease-Suffix ist konkreter Repo-Stand, keine unabhängige Produktionsreifezertifizierung. Neuer v2-Stand und Node >=22 bedeuten, dass ältere Panda-Aussagen/Beispiele nicht ungeprüft fortgeschrieben werden dürfen. Diagnostics nennt root hooks als in v2 entfernt sowie Designsystem-version_mismatch, peer_range_unsatisfied, buildinfo_stale und option_mismatch. Konkrete Kompatibilitätsmechanismen existieren, aber keine langfristige neutrale Contractformat-Stabilitätszusage nachgewiesen. Export schemaVersion 1 und Parsergrenze sind engere Zusagen als allgemeine SemVer-/Cross-Renderer-Kompatibilität. Zwei versuchte Migration-URLs waren 404; das ist nur Zugriffsgrenze, kein Nachweis fehlender Migrationsdokumentation.


## S52

**uSpec: Primärquellen und lokale Fundstellenkürzel.**

Repository main beim Abruf: **1e25e9b8bc2e694689ba0489594f38807a341f14**, sichtbar 03.09.2026. S14s bee78db… ist der letzte README-Dateicommit, keine aktuelle Gesamtversion. Alle unten genannten Repositoryquellen auf denselben Snapshot gepinnt. Lokale Kürzel ausschließlich für diese Übergabe; keine globalen IDs vergeben.

- **TREE** [vollständiger Pfadbaum](https://api.github.com/repos/redongreen/uSpec/git/trees/1e25e9b8bc2e694689ba0489594f38807a341f14?recursive=1), Antwort main mit identischer SHA, truncated:false; gezielt Schema-/Validator-/Contractdateien lokalisiert. Kein Beweis beliebiger externer Abwesenheit.
- **DOC** [Component.MD](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/docs/specs/component-md.mdx), vollständig. JSON canonical, Markdown abgeleitet; Evidence → Interpretation → Reconciliation → Contract → Render; keine ausgeführte Zuverlässigkeitsprüfung.
- **CON** [component-contract.ts](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/packages/cli/src/component-md/component-contract.ts), vollständig; tatsächlich implementiertes inline contractSchema, Ajv, load/build/validateCanonicalContract.
- **TYP** [types.ts](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/packages/cli/src/component-md/types.ts), vollständig; BaseJson, TreeNode, EvidenceEnvelope, CanonicalComponentContract.
- **CAC** [cache-validation.ts](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/packages/cli/src/component-md/cache-validation.ts), vollständig; manuelle Domänenchecks und Evidence-JSON-Pointer, keine Ausführung.
- **BASE** [base-json-schema.md](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/figma-plugin/docs/base-json-schema.md), vollständig; dokumentierte JSONC-Form, Figma-Quellmodell, IDs, Variablen, Komposition, Ownership, Traversal-/Samplinggrenzen.
- **BVAL** [validate-base.mjs](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/figma-plugin/scripts/validate-base.mjs), vollständig; weiteres inline Ajv-Schema, ausdrücklich pragmatischer Strukturcheck statt literal conversion der JSONC-Dokumentation; eigene CLI vorhanden, nicht ausgeführt.
- **SAFE** [safe.ts](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/figma-plugin/src/safe.ts), vollständig; typed snapshotComponentProperties und Placement-Deduplikation.
- **API** [API-Referenz](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/references/api/agent-api-instruction.md), gezielt Outputform, ApiDictionary, Subcomponent-/Slot-/Stateformen und Beispiele geprüft, kein Vollständigkeitsaudit aller Agentenanweisungen.
- **STR** [Structure-Referenz](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/references/structure/agent-structure-instruction.md), gezielt Figma Properties Reference, Output Data Structure, target anchors, min/max, clipsContent und Tabellenregeln geprüft.
- **COL** [Color-Referenz](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/references/color/agent-color-instruction.md), gezielt Data Structure, state tables, Variable Mode Colors und Token resolution per mode geprüft.
- **VOI** [Screenreader-Referenz](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/references/screen-reader/agent-screenreader-instruction.md), gezielt Merge Analysis, FocusOrderData/StateData/TableData/PropertyItem, platform properties und Tab-/Errorbeispiele geprüft.
- **PKG** [CLI package.json](https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/packages/cli/package.json), vollständig; uspec-skills 0.3.3, Node >=18, Ajv ^8.17.1, TypeScript, bin dist/index.js.
- **URL** [deklarierte Schema-URL](https://uspec.design/schemas/component-contract-1.0.json) am Abruf als Browserseite mit Text **Not Found**. Kein extern abrufbares Schema von dieser URL bestätigt. Das widerlegt nicht das in CON tatsächlich vorhandene Schema.


## Originalschema und tatsächlich vorhandenes Tooling getrennt

1. **Originales Schema existiert im Quelltext:** CON definiert contractSchema mit $id und $schema-Konstante component-contract-1.0.json und schemaVersion 1.0. Ajv compile wird tatsächlich aufgerufen. validateCanonicalContract wird von load und build verwendet. Kein bloßes README-Versprechen.
2. **Externe Schemaadresse nicht verfügbar bestätigt:** URL lieferte Not Found; TREE enthält keine separate canonical .schema.json. Das ist eine begrenzte Veröffentlichungs-/Interoperabilitätslücke, keine Behauptung „kein Schema“ und kein Beweis nicht überprüfbarer extern angebotener Alternativen. contractSchema ist nicht exportiert; Validatorfunktion ist exportiert. Für einen unabhängigen Fremdvalidator wäre Extraktion/Veröffentlichung dieses Objekts nötig.
3. **Schemaumfang eng:** Root additionalProperties:false und einige strengere Metadaten; variants.axes ohne items, default/anatomy Werte `{}`, api.mainTable.properties array ohne Elementdefinition, color nur componentName, accessibility.states array ohne items, sourceModel weite Objekte. In TYP Fachdomänen Record<string,any>. Somit keine vollständige Typ-, Referenz-, Accessibility-, Behavior- oder Layoutsemantikprüfung.
4. **Separate Baseprüfung:** BVAL nutzt zweites inline Ajv-Schema mit eigenen Pflichtfeldern; JSONC-Datei BASE ist Dokumentation und nicht identisch damit. Viele Objekt-/Arrayinhalte bleiben offen. BVAL prüft zusätzlich rohe U+2028/U+2029-Transportzeichen. Keine Prüfung aller gemessenen Fachwerte daraus folgern.
5. **Echte lokale Zusatzprüfungen:** CAC prüft JSON-Struktur, Zeitstempel, configurationExamples, Zeilenbreiten, not-measured-Werte, Farbstrategien/Arraylängen, drei Plattformsektionen, focusOrderIndex/layerName, Ledgerbekanntheit/-eindeutigkeit, unresolved/omitted must-emit, existierende JSON-Pointer, targetKind/field/equals/pattern und Evidenceabdeckung jeder semantischen Zeile. Bei vorhandenen Evidence-Dateien; fehlt diese ENOENT, kehrt validateEvidenceObligations ohne Fehler zurück. Domänenübergreifend: Achsennamen + fileKey/nodeId/componentSlug für structure/color/voice und componentName API/Dictionary. Das ist substanziell, aber keine vollständige fachliche Widerspruchsprüfung.
6. **Build vs laden trennen:** build ruft validateCaches auf, checkt manifest/plan slug und baseSourceHash sowie renderer evidence hash; load eines fertigen Contracts macht nur validateCanonicalContract und liefert cacheValidations:[]. Ein korrekt geladenes JSON beweist daher keine nachträglich geprüfte Evidencekette.

## Format/Sprache und zusätzlich nötiger Code

JSON ist Originalaustausch; Markdown menschliche abgeleitete Sicht, JSONC in BASE beschreibende Dokumentation; kein YAML-Originalformat nachgewiesen. Fachliche Snapshots sind ohne JS-Funktionen lesbar. Herstellung erfordert Figma-Extraktion, LLM-Interpretation und TS/Node-CLI; PKG Node >=18, Ajv ^8.17.1. JSX Motion-Skripte gehören nicht automatisch zum Canonical-Behavior. DOC empfiehlt nachgelagerte LLM-Implementierung in React/SwiftUI/Compose; das sind Arbeitsmöglichkeiten, keine verifizierten vorhandenen Renderer oder portablen Laufzeitadapter. Für formale Behaviorlogik wäre ein weiteres Fachmodell/Adapter nötig; freier Text runtimeCondition reicht nicht.

## Reifegrad und Kompatibilität

Schema 1.0, Base schema 1, CLI-Paket 0.3.3 sind getrennte Versionsachsen; Repo-/Dokumentmarketing V2.7 nicht als Canonicalschemaversion verwenden. PKG belegt vorhandene Build-/typecheck-/Testskripte, kein bestandenes Test-/Publish-/Installationsresultat. BASE dokumentiert additive Vorbereitung älterer schema-v1 Exporte und legacy booleanOverrides; dedup fingerprint v1 ignoriert Text-/Instance-Swapunterschiede bewusst. DOC Troubleshooting verlangt abgestimmte Plugin-/Skillversion und warnt vor Drift; keine allgemeine langfristige Format-/Renderer-Kompatibilitätszusage daraus ableiten. Keine Produktionsreifeentscheidung, Marktanteilswertung oder Registryrelease behauptet.


## S53

**OpenPencil: Primärquellen und lokale Fundstellenkürzel.**

Alle externen Quellen über BrowserOS neo gelesen. Code-Links sind gepinnt.

- OPD: [aktuelle offizielle Entwicklungsdokumentation](https://openpencil.dev/development/behaviours-and-preview), vollständig gelesen, sichtbarer Seitenstand 14.10.2026. Kinds/Contracts, Storage, Values/States, Authoring, Preview und Export. Veränderliche Seite.
- OPH: [Commit](https://github.com/open-pencil/open-pencil/commit/ab2875cc761ee6cff17d389ff1c85fedae50aeab).
- OPS: [Originalschema schema.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/behaviours/schema.ts), vollständig. Valibot `behaviourSchema` und `behaviourSpecSchema`, keine bloße Toolbeschreibung.
- OPK: [kinds.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/behaviours/kinds.ts), vollständig. 15 eingebaute Kinds; Typen boolean/text/number/choice; required values/parts; items/children; fünf Interaktionszustände.
- OPM: [model.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/behaviours/model.ts), vollständig. behaviourOwner, behaviourProperties, missingBindings, ID-Umbenennung.
- OPR: [spec.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/behaviours/spec.ts), vollständig. Namen/IDs, property type lookup, on/off guessing, numbers, part checks und Konvertierung zurück. Browser-Extraktion zeigte bei einer parallelen Navigation einen veralteten URL-Header schema.ts; der gelesene Inhalt ist anhand Funktionen/imports eindeutig spec.ts. Maßgeblich ist dieser gepinnte Originalpfad.
- OPF: [plugin-data/field.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/plugin-data/field.ts), vollständig, plus [fields.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/plugin-data/fields.ts), vollständig. `behaviour` ist jsonPluginDataField mit Rolle content und Originalschema; decoder parseJson/safeParse, encoder JSON.stringify.
- OPT: [Agenttools](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/core/src/tools/create/behaviours.ts), vollständig. set_behaviour/get_behaviour/create_slot, Valibot Toolinput; Agenttool-ID ist Zielkomponente, kein öffentliches UI-Ereignis.
- OPV: [Preview controls/index.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/vue/src/canvas/islands/controls/index.ts), [shared.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/vue/src/canvas/islands/controls/shared.ts), [state.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/vue/src/canvas/islands/state.ts), vollständig. Vue/Reka-Primitives, modelValue/open callbacks, DOM pointer/focus handlers, Auswahl und instanzeigener State anhand Layerpfad.
- OPP: [scene-graph package.json](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/package.json), Version/Exports gelesen; [behaviours/index.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/behaviours/index.ts) exportiert das Originalschema separat mit.
- OPB: [gepinnter Pfadbaum](https://api.github.com/repos/open-pencil/open-pencil/git/trees/ab2875cc761ee6cff17d389ff1c85fedae50aeab?recursive=1), für relevante Behaviour-/Preview-/Schemaquellen gesichtet; keine pauschale Vollprüfung des Repositorycodes.


## Originalschema und tatsächliches Tooling

Originalschema ist **TypeScript/Valibot**, nicht ein hier gefundenes JSON Schema. OPS speichert kind, booleans/texts/numbers/parts/states; Spec schreibt Eigenschaften/Slots nach Namen. Schemas prüfen Shapes, bekannte Kinds und beim gespeicherten number range finite Zahlen sowie max>min/step>0. Aus dem Code folgt keine Prüfung default innerhalb min/max oder Stepausrichtung. Records lassen beliebige Schlüssel syntaktisch zu; zulässige Value-/Part-IDs werden erst teilweise in OPR anhand OPK geprüft. OPS kann allein die Existenz der String-IDs nicht beweisen.

OPF verwendet parseJson plus safeParse tatsächlich im Dateidecoder. Ungültiger JSON-/Shapeinhalt wird als fehlend gelesen, nicht als paketweiter Fehler ausgegeben. encode verwendet JSON.stringify. OPR ist zusätzliche semantische Auflösung: vorhandener Propertyname/Typ, unterstützte Value-/Part-ID, explizite on/off-Optionen, Zahlenbereich, kein doppelter Slot für zwei Parts. `resolveStates` kombiniert geratenes Mapping mit expliziten Strings; hier kein vollständiger expliziter State-Optionscheck erkennbar. `missingBindings` prüft required Text/Boolean/Parts und eine verloren gegangene states-Property, keine beliebigen Cross-Domain-Referenzen. `behaviourToSpec` lässt unaufgelöste Bindungen aus. Diese Pfade nicht als garantiert verlustfreien Roundtrip ausgeben.

OPT verwendet das Original-Specschema für Toolinput, delegiert an OpenPencilAPI und meldet fehlende Bindungen. Toolinput, Dateidecode, Specauflösung und vollständige Paketvalidierung sind unterschiedliche Prüfaufgaben. Es wurde keiner dieser Pfade ausgeführt.

## Format, zusätzliche Sprache und Code

Der Dateninhalt benötigt keine frei eingebetteten JS-Funktionen, wird als JSON im Pluginfeld serialisiert und kann von Skripting/Agenttools/Design-JSX erstellt werden. YAML ist nicht als Originalformat belegt. Das Schematooling ist TS/JS mit Valibot. Preview benötigt Scenegraph, Extraktion/private graph projection, dom-css, Vue und Reka UI. OPV zeigt feste Callback-/DOM-Handler; der Behaviourdatensatz ist weder eine allgemeine ausführbare Verhaltenssprache noch allein eine plattformneutrale UX-Maschine. Die eigene Implementierung neuer Kinds verlangt laut OPD Änderungen an Contracts, Preview, JSX/Export und UI-Labels. Ein neuer Kindname im JSON genügt nicht.

## Reifegrad und Kompatibilität

OPP zeigt Version 0.16.0 und einen öffentlichen behaviours-Export. OPD beschreibt konkretes vorhandenes Authoring/Preview/Codeexport und weist Testquellen aus; deren Vorhandensein wurde im Pfadbaum gesehen, nicht ihre erfolgreiche Ausführung verifiziert. Keine belastbare eigenständige Behaviour-Spezifikationsversion oder langfristige Format-/Migrations-/Crossplatform-Kompatibilitätszusage festgestellt. Keine Produktionsreifeentscheidung. `.fig`-Propertyumbenennung ist explizit unterstützt (OPM), aber Roundtripstabilität, Namenskollisionen bei Layerpfaden, Umbenennungen und externe Assetupdates bleiben ungeprüft.


Diese Zusatzbefunde sind kandidatenbezogen. Der vorgemerkte Gesamtvergleich aller Kandidaten zu Schema/Tooling, Beschreibungssprache/Code und Reifegrad ist weiterhin nicht als erledigt markiert. Die Berichtsvorlagen lagen unter /private/tmp/ui-contracts-{panda,uspec,openpencil}-review-current.md; die obigen öffentlichen gepinnten Primärlinks und aktuellen Claims sichern den dauerhaften Projektstand.

## Letzte Kandidatenrunde – 24. Oktober 2026

Alle öffentlichen Quellen über BrowserOS neo konsultiert. WAI-ARIA/APG wurden nach Agenten-Kapazitätsfehlern zentral geprüft; der CSS-Agent lieferte einen getrennten Bericht mit datierten Quellen. Gegenprüfung und Rollenabgleich sind keine ausgeführten Konformitätsversuche. Keine zweite vollständige Auditprüfung sämtlicher Dokumente behauptet.

## S54

**WAI-ARIA: Primärquellen und Fundstellenkürzel.**



- AR12: [WAI-ARIA 1.2 REC 06.06.2023](https://www.w3.org/TR/2023/REC-wai-aria-1.2-20230606/), aktueller TR-Endpunkt identischer Titel/Status. Gelesen: Scope/Hostrollen, §4.3 Fokus, Rollencharakteristika und combobox/listbox/option/spinbutton, §6 Typen/IDL/Attribute einschließlich live/controls/labelledby/activedescendant, §8 Hostintegration/CSS-Selektoren, §9 Fehlerbehandlung, Anhang A Typabbildungen. Keine Vollerhebung aller 744k Zeichen.
- AR13: [WAI-ARIA 1.3 WD 04.06.2026](https://www.w3.org/TR/2026/WD-wai-aria-1.3-20260604/), Status/Änderungen gelesen; kein Ersatz der 1.2-REC-Baseline. ariaNotify nicht als 1.2-Fähigkeit ausgegeben.
- AAM: [Core-AAM 1.2 CRD 21.10.2026](https://www.w3.org/TR/2026/CRD-core-aam-1.2-20261021/), aktueller TR-Status/Mappingrolle gelesen; kein unabhängiger Vollaudit sämtlicher Plattformmappings oder Implementierungsbericht.
- NAME: [Accname 1.2 WD 21.10.2026](https://www.w3.org/TR/2026/WD-accname-1.2-20261021/), Status/Nameberechnungsrolle gelesen, kein REC-Status für diesen WD behauptet.


## Zusatzkriterien und Grenzen

Semantik wird über Hostmarkup/-attribute ausgedrückt; die Attributwerte besitzen dokumentierte generische Typen und Hostabbildungen. Keine JS-Funktionen sind nötig, um die Semantik zu deklarieren. Das bedeutet keine automatische tatsächliche Bedienlogik; Autoren müssen Interaktion und sichtbare Darstellung umsetzen.

Anhang A ist eine Typabbildung zu HTML/XML Schema, kein Nachweis eines separat veröffentlichten vollständigen Schemaartefakts für das gewünschte Accessibility-Contractformat. §6.3 sagt, dass IDL-Getter nicht validieren; §9 begrenzt Browserlogik ausdrücklich. Ein ungültiger Wert kann als String zurückgegeben werden. Originalchecker/Toolversion und dessen vollständiger semantischer Prüfbereich bleiben X06-U; keine Browser-/Validatorausführung.

1.2 ist eine W3C Recommendation; 1.3 bleibt WD, Core-AAM und Accname haben eigene oben genannte Stände. Das ist Normreife, keine bestätigte Unterstützung jedes Browsers/Screenreaders oder native Produktkonformität. Die frühe Agentenvorarbeit wurde zentral genutzt; nach Kapazitätsfehlern erfolgte die konkrete Quellenprüfung zentral erneut. Kein fehlgeschlagener Agentenstart wird als fertiger Nachweis gezählt.


## S55

**APG: Primärquellen und Fundstellenkürzel.**



- AP0: [About/Introduction](https://www.w3.org/WAI/ARIA/apg/about/introduction/) und [Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/), Zweck, nichtnormativer Status, fehlendes Konformitätsmodell, illustrative Beispiele und reale AT-Prüfgrenze gelesen.
- AP1: [Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/), Varianten, Keyboard Interaction, Rollen/States/Properties vollständig fachlich gelesen.
- AP2: [Developing a Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/), Fokus/Selektion, tab/arrow-Konventionen, Fokusverwaltung und Auswirkungen visueller Reihenfolge gezielt gelesen.
- AP3: [Alert Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alert/), dynamische Meldungen/Fokus/Timing und Rollen gelesen.
- AP4: [Editable Combobox with List Autocomplete Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-list/), Warnungen, Semantik, Fokus, Scrollen und Quellverweise gelesen.
- AP5: [gepinnte Combobox-JS-Implementierung](https://github.com/w3c/aria-practices/blob/0f765e4dc33e966026114ac12a8380db1de3b787/content/patterns/combobox/examples/js/combobox-autocomplete.js), Constructor, interne Zustandsvariablen, open/close/filter, Keyhandler und scrollIntoView manuell gelesen.
- AP6: [gepinnte Beispiel-CSS](https://github.com/w3c/aria-practices/blob/0f765e4dc33e966026114ac12a8380db1de3b787/content/patterns/combobox/examples/css/combobox-autocomplete.css), vollständig gelesen. Reale Styles enthalten feste Größen und Overflow; keine allgemeinen APG-Vertragspflichten daraus abgeleitet.
- AP7: [Repository](https://github.com/w3c/aria-practices) und [Paket-/Toolskripte am Snapshot](https://github.com/w3c/aria-practices/blob/0f765e4dc33e966026114ac12a8380db1de3b787/package.json), Snapshot 0f765e4dc33e966026114ac12a8380db1de3b787 vom 30.09.2026 laut sichtbarem main-Stand. Lint: HTMLHint/vnu, CSS/JS-Lint, AVA/Selenium-Regressionspfad dokumentiert; kein Tool ausgeführt. Paket private/0.0.0 ist kein APG-Spezifikationsrelease.


## Zusatzkriterien und Grenzen

APG ist eine veränderliche informative Website mit HTML/CSS/JS-Beispielen, kein JSON-/YAML-Patternaustauschschema und keine W3C Recommendation mit eigenem Konformitätsmodell. Die Regeln sind unabhängig von einer bestimmten JS-Frameworksprache lesbar, die ausgewählten Referenzimplementierungen benötigen aber Web-/DOM-Code.

Es existieren reale HTML-/JS-/CSS-Prüfwerkzeuge und Beispielregressionstests. Ihr Vorhandensein wird nicht als fehlend bewertet; sie prüfen ein anderes Artefakt als das gewünschte neutrale A11y-Contract. Ein vollständiges Originalschema und dessen Validator bleiben X06-U. Keine tatsächlich bestandenen Beispiel-, Browser- oder AT-Tests behauptet. APG fordert entsprechende Interoperabilitätsprüfung vor produktiver Nutzung ausdrücklich.

Pattern und Beispiele besitzen verschiedene Rollen. Beispielspezifische CSS-Werte sind nicht allgemeine APG-Visualnormen; eine vollständige Nutzung der Beispielgestaltung würde einen separat gewählten CSS-Beitrag erfordern. Für Behavior dienen die tatsächlich vorhandenen JS-Handler als belegter Adapteransatz (A), nicht als neue APG-Maschinensprache. Die zentral übernommene Accessibility-Anforderungsquelle kann weiterhin getrennt geführt werden, ihre Vier-Domänen-Bindung ist aber noch offen.

Der APG-Agent scheiterte vor Quellenarbeit am Kapazitätslimit; dieser Bericht stammt aus der zentralen Quellenprüfung. Er ist kein fingiertes Agentenergebnis.


## S56

**CSS Layout: Primärquellen und Fundstellenkürzel.**

Lokale Kürzel dieses Berichts sind keine globalen Quellen-/Claim-IDs.

- **ANCHOR**: [CSS Anchor Positioning 1, WD 27.03.2026](https://www.w3.org/TR/2026/WD-css-anchor-position-1-20260327/), insbesondere §§1.1, 2.1–2.4, 3.1–3.2, 5, 6, 9 sowie Property/IDL Index und Conformance. Der aktuelle TR-Endpunkt lieferte diesen Stand. Entspricht vorhandener S18/C33, nicht S17.
- **OVERFLOW**: [CSS Overflow 3, WD 07.10.2025](https://www.w3.org/TR/2025/WD-css-overflow-3-20251007/), insbesondere §§1.1–1.2, 2, 3, 4 und Conformance. Aktueller TR-Endpunkt lieferte diesen Stand. Entspricht vorhandener S19/C34. S17 im Repository ist APG und ist keine CSS-Quelle.
- **SYNTAX**: [CSS Syntax 3, Candidate Recommendation Draft 01.10.2026](https://www.w3.org/TR/2026/CRD-css-syntax-3-20261001/), §§3, 4–5, insbesondere parse-stylesheet und consume-declaration. Dokumentierte Tokenisierung, Grammatik und Parseralgorithmen, kein JSON Schema.
- **VALUES**: [CSS Values and Units 3, Candidate Recommendation Draft 22.03.2024](https://www.w3.org/TR/2024/CRD-css-values-3-20240322/), §§2, 5 und 8.1. ANCHOR/OVERFLOW §1.1 verweisen ausdrücklich normativ auf CSS-VALUES-3 für Wertsyntax und nicht lokal definierte Typen. Länge, Einheit, Prozent und calc() sind daher kein frei erfundenes Contractmodell. Values 4 [WD 12.03.2024](https://www.w3.org/TR/2024/WD-css-values-4-20240312/) zusätzlich zur Abgrenzung gelesen; keine pauschale Erweiterung auf dessen sämtliche Features.
- **SIZING**: [CSS Box Sizing 3, WD 04.09.2026](https://www.w3.org/TR/2026/WD-css-sizing-3-20260904/), §§3.1.3 (max-width/max-height), 3.2 (Sizing Values), 3.3 (box-sizing). OVERFLOW verlinkt max-height ausdrücklich auf dieses Zielmodell und zeigt das Beispiel `overflow: auto; max-height: 5em`. ANCHOR referenziert Größenwerte/-eigenschaften; V05 wird hier als Referenzbeitrag ausgewiesen, nicht als in Overflow neu definierte Eigenschaft.

**Editors gegenüber Publikation:** [Anchor-Editors-Endpunkt](https://drafts.csswg.org/css-anchor-position-1/) zeigte 06.09.2026 und bezeichnete sich im Kopf als WD; seine angebliche datierte „This version“-Adresse `https://www.w3.org/TR/2026/WD-css-anchor-position-1-20260906/` lieferte bei direkter Prüfung 404. Daher kein nachgewiesener publizierter WD dieses Datums und keine Übernahme als neuer normativer Basissnapshot. [Overflow-Editors-Endpunkt](https://drafts.csswg.org/css-overflow-3/) zeigte Editor’s Draft 13.08.2026, veränderlich und nicht W3C-endorsed. Diese Editors-Texte wurden zur aktuellen Gegenprüfung gelesen, ihre Header und begrenzte Änderungen sind keine Browserunterstützungsnachweise. Keine Recommendation für die zwei Kernmodule behauptet. CRD der Syntax/Values macht Anchor/Overflow nicht zu CR oder Recommendation. Die verlinkten Test-/Implementierungsberichte wurden nicht ausgeführt und hier nicht als belegte Kompatibilität gewertet.


## Syntax, Schema und reales Tooling getrennt

Die Grammatik ist maschinenlesbare CSS-Syntax und enthält eigene Propertyproduktionen. SYNTAX spezifiziert Tokenizer/Parser und Conformance-Checker-Pflichten. Das ist weder ein JSON-Schema noch ein bereits nachgewiesenes, versionskompatibles Validierungswerkzeug. Ein Parser kann Syntax akzeptieren und dennoch keine richtige geometrische oder paketweite Bedeutung durchsetzen. Fehlende Anker können Fallback/ungültige Berechnung ergeben; mehrfach benannte Anker sind legal. Eine spätere Paketprüfung muss fehlende Zielbindungen, Instanzkollisionen und Domänenwidersprüche zusätzlich behandeln.

## Beschreibung und zusätzlicher Code getrennt

Das geometrische Modell ist deklarativ; CSS plus eine strukturierte Element-/Boxhierarchie reichen als Spezifikationsbeschreibung für die gelesenen Layoutbeziehungen. Beispielschema im Text, nicht getestet: `anchor-name: --input`, am positionierten Ziel `position-anchor: --input; top: calc(anchor(bottom) + 8px);`, kombiniert mit `max-height` und `overflow-y: auto`. Die Zahl 8 ist ein Testwert. Reale Zielrenderer benötigen Stylesheetanbindung, richtige Elementstruktur, Positionskontext und unterstützte Modulsemantik. Für native Swift-Ziele ist keine standardisierte Übersetzung nachgewiesen. UX-Logik, Eventpayloads, Komponenteninstanziierung und zugängliche Semantik entstehen nicht automatisch durch diese Deklarationen. Kein Polyfill oder Adapter wurde implementiert.


**Zentrale G02/CSS-Korrektur:** Die Berichtstabelle schlug A vor, nennt selbst D als mögliche enge Lesart. Die gespeicherte Matrix verwendet D konsistent zum operationalisierten Kriterium ohne notwendige JS-/Reactfunktionen. CSS-Box-/Hostbindung bleibt eine eigene Grenze; daraus folgt kein neutraler oder nativer Renderer. Rohbericht und aktuelle Bewertung werden nicht still gleichgesetzt.

Die drei Berichte lagen unter /private/tmp/ui-contracts-{aria,apg,css-layout}-review-current.md. CSS-Lesekopien/Hashmanifest unter /private/tmp/ui-contracts-css-layout-evidence/ beziehen sich auf extrahierte Lesefassungen, nicht originale HTML-Bytes. Dauerhafte Projektbelege sind die datierten/gepinnten Primärlinks und aktuellen Claims.


## S57

**Integrationsfolgeprüfung – 24. Oktober 2026.** Sechs bestehende Primärdateien erneut manuell über BrowserOS neo gelesen, unveränderte Snapshotbindung. Keine Ausführung, kein neuer Release-/Produktionsreifecheck. C390–C393 ergänzen die vorhandenen Befunde; keine Matrixbewertung geändert. Rohansichten wurden vollständig gelesen, längere Browserausgaben aus den lokal gespeicherten Vollauszügen. Die temporären Auszüge sind kein dauerhafter Quellenersatz.

| Kürzel | Gepinnte Primärquelle | Umfang |
| --- | --- | --- |
| IR | [UXSpec import-resolver.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/import-resolver.ts) | Vollständig: lokale Pfade, Bereiche, Diagnosen, ancestorPaths |
| BU | [UXSpec bundler.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/bundler.ts) | Vollständig: direkte Abhängigkeiten, erneute Importauflösung und Modulschlüssel |
| RE | [UXSpec resolve.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/resolve.ts) | Vollständig: Tokenqualifizierung, Elementverzeichnis, Expansion und Parameter |
| AC | [Ark use-combobox.ts](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/combobox/use-combobox.ts) | Vollständig: useId, Field-IDs, Props-Reihenfolge und Maschinenkontext |
| AS | [Ark use-scroll-area.ts](https://github.com/chakra-ui/ark/blob/c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc/packages/react/src/components/scroll-area/use-scroll-area.ts) | Vollständig: eigene ID und eigener Maschinenkontext |
| OP | [OpenPencil behaviours/spec.ts](https://github.com/open-pencil/open-pencil/blob/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/scene-graph/src/behaviours/spec.ts) | Vollständig: Value-/Partauflösung, Stateheuristik und Rückkonvertierung |

Die hier gelesenen Funktionen zeigen begrenzte lokale Prüflogik. Andere Aufrufpfade werden nicht pauschal ausgeschlossen. Insbesondere sind Aussagen über nicht nachgewiesene Graph-/Zustandsprüfung keine behaupteten erfolgreichen Fehlerreproduktionen.


## S58

**Konkrete Feldbindungen – 24. Oktober 2026.** Gezielte erneute Primärquellenprüfung über BrowserOS neo. Bestehende Quellenstände bleiben gepinnt beziehungsweise ausdrücklich datiert. Die ausgewählten Abschnitte tragen C394–C396; kein vollständiger neuer Projektaudit, keine ausgeführten Validatoren und keine Laufzeitprüfung.

| Quelle | Stand und gelesener Umfang |
| --- | --- |
| [CEM schema.d.ts](https://github.com/webcomponents/custom-elements-manifest/blob/2570079a0525c26296f9ec39944f0c6e0f0461af/schema.d.ts) | Gepinnter Originalstand; gezielt Reference, CustomElement, Event, Type, CssPart, Slot und Klassentypen im gespeicherten Vollauszug gelesen |
| [UXSpec Originalschema](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/schema/uxspec.schema.json) | Vollständig erneut gelesen; contextField, eventSpec, actionSpec, machine/stateNode, invoke und elementBase |
| [UXSpec resolve.ts](https://github.com/johnlindquist/uxspec/blob/20dfae0e7224d952e198afdf4ffed26d6fd67180/src/compiler/resolve.ts) | Bereits in S57 vollständig gelesener Originalpfad erneut ausgewertet: resolveTokenValue und Behandlung von value/unit; in dieser Runde nicht neu abgerufen |
| [DTCG Format 2025.10](https://www.designtokens.org/TR/2025.10/format/) | Gezielte erneute Lesung §6.6 und §8.2 einschließlich Dimensionvalidierung und Plattformhinweisen; kein neuer Resolveraudit |
| [WAI-ARIA 1.2](https://www.w3.org/TR/2023/REC-wai-aria-1.2-20230606/#aria-activedescendant) | Fester Recommendationstand; aria-activedescendant samt Bedingungen und ID-Referenzdefinition gezielt gelesen |
| [APG Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) | Veränderliche Guide-Seite, Abruf 24. Oktober 2026; Listbox-Fokusnotiz sowie Roles/States/Properties einschließlich Auswahlfolge erneut gelesen. Verlinkte Editor-ARIA-Ziele nicht als neue normative Quelle übernommen |

Neu abgerufen wurden fünf Dokumente; eine vorhandene Resolverlesung wurde erneut ausgewertet. Temporäre Browserauszüge sind kein Ersatz für die hier verlinkten Primärstände. Die neue Instanz-/Ownership-Regel und das präzisierte Prüfungstor bleiben Vorschläge des Projekts, keine Aussagen dieser Standards.
