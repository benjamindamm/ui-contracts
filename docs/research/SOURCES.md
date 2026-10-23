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
