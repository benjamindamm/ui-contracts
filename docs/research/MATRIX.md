# Anforderungsorientierte Abdeckungsmatrix

Stand: 23. Oktober 2026. **Erste Untersuchung mit bewusst offenen Zellen.** Anforderungen stehen links, Kandidaten als Spalten. Zwei Spaltenblöcke je Abschnitt dienen nur der Lesbarkeit; dieselbe Anforderung gilt in beiden Blöcken. Die Kandidaten sind Beiträge unterschiedlicher Art, keine gleichartigen Komplettlösungen.

Vor Verwendung lesen: [Kriterien und Herkunft](REQUIREMENTS.md), [Methode](METHODS.md), [Quellenstände](SOURCES.md), [Begründungen](CLAIMS.md).

**D** direkt · **R** über Referenz · **A** Adapter erforderlich · **N** im geprüften Umfang nicht abgedeckt · **U** ungeprüft. Ein Link wie D/C07 enthält Befund, Evidenzstufe und Grenze. Alle Bewertungen sind E1 oder E2, keine E3. U bedeutet fehlende Untersuchung, keine negative Eigenschaft. Es ist kein Kandidat bereits als Gesamtlösung ausgewählt.

Bei DTCG umfasst die Spalte Format **und** separat belegtes Resolver Module 2025.10. CSS Layout umfasst die getrennten Quellen zu Anchor Positioning und Overflow. Die Verknüpfung beider ist nicht getestet. OpenPencil bezeichnet nur den untersuchten Behaviour-Beitrag. Bei D in einem spezialisierten Modell bleibt dessen technische Bindung bestehen; daraus folgt keine Abdeckung von G02 oder X03.

## CEM auf einen Blick – vertieft geprüft

**20 der 22 zuvor offenen CEM-Felder sind jetzt geklärt; 2 bleiben mit konkreter Frage offen.** Zusammen mit den 4 schon bewerteten Feldern sind damit 24 von 26 eingeordnet. Nur CEM wurde vertieft; andere Kandidatenbewertungen sind unverändert.

- **Kann:** Web-Komponenten-APIs mit Properties, Typangaben, Events, Slots und CSS-Parts dokumentieren. CSS-Designwerte lassen sich über `cssProperties.syntax/default` mit der Bedeutung der CSS-Wertsyntax beschreiben. Ein separates originales JSON Schema ist vorhanden.
- **Deckt im Standardkern nicht ab:** Layout/Scrollregeln, Stylezuordnung je Zustand, Themes, UX-Automaten, Accessibility-Regeln sowie UI-Instanzkomposition und paketweite Referenz-/Ownershipprüfung.
- **Noch offen:** Eindeutige strukturierte Event-Payloadauflösung (I02/C37) und die vollständige Bindung vier unabhängig geführter Domänen (X01/C43).

Geprüft wurden die vollständigen CEM-Typdefinitionen und das zugehörige JSON Schema am Commit `2570079a0525c26296f9ec39944f0c6e0f0461af`, ergänzt durch offizielle Format- und Analyzer-Dokumentation. **N gilt nur für die definierte Semantik dieses CEM-Kerns**, nicht für beliebige Erweiterungen, implementierte Komponenten oder Plugins. Es wurden keine Tools installiert oder Laufzeittests ausgeführt.

## DTCG auf einen Blick – vertieft geprüft

**22 der 23 zuvor offenen DTCG-Felder sind geklärt; X01 bleibt mit konkreter Paketfrage offen.** Mit den 3 bereits belegten Feldern sind damit 25 von 26 eingeordnet. Nur die DTCG-Spalte wurde in diesem Schritt vertieft.

- **Kann:** Sprachneutrale, typisierte Designwerte austauschen (**Format Module**) und benannte Wertvarianten/Themes, Quellen und Auflösungsreihenfolge beschreiben (**Resolver Module**). Getrennte veröffentlichte Schemata sind verfügbar.
- **Deckt im definierten Kern nicht ab:** Komponenten-APIs, tatsächliches Layout/Scrollen, UX-Automaten, Accessibility-Regeln und UI-Komponenteninstanzen. Tokenverweise und Gruppenvererbung ersetzen diese Modelle nicht.
- **Offen:** Wie DTCG als eigenständige Wertequelle mit den anderen drei Domänen verbunden wird, ohne doppelte Definitionen (X01/C54). Externe URI-Unterstützung und tatsächliche semantische Konformität sind werkzeugabhängig und wurden nicht ausgeführt.

Geprüft: Format und Resolver **2025.10**, jeweils getrennt, sowie ihre veröffentlichten JSON-Schemata. **N bezieht sich auf die definierte Semantik dieser Module**, nicht auf beliebige Herstellererweiterungen. Kein Compiler-, Validator- oder Laufzeitversuch wurde durchgeführt. Insbesondere ist nur Referenzauflösung im selben Resolverdokument verpflichtend; externe Dateien/Netzwerkquellen sind nicht pauschal garantiert (C56).

## SCXML auf einen Blick – vertieft geprüft

**18 der 21 zuvor offenen SCXML-Felder sind geklärt; 3 bleiben mit konkreter Frage offen.** Mit den 5 bereits belegten Feldern sind 23 von 26 eingeordnet. Nur SCXML wurde in diesem Schritt geprüft; ein abgeschlossener UXSpec-Durchgang wird nicht vorausgesetzt.

- **Kann:** Zustände, Ereignisübergänge, Guards, Aktionen und Datenverarbeitung definieren. `invoke` beschreibt eigene Verhaltensinstanzen mit Datenübergabe und Lebenszyklus. Eigenständige W3C-XSD-Schemata sind vorhanden.
- **Zusätzlich nötig:** Eine Hostbindung übersetzt UI-Tastatur-/Fokusereignisse und UI-Aktionen in beziehungsweise aus SCXML-Ereignissen (B04/C62). Kein universeller fertiger UI-Adapter ist nachgewiesen.
- **Nicht im Kern enthalten:** Design-/Layout-/Accessibility-Fachmodelle und eine vollständige domänenübergreifende UI-Instanz-/Ownershipprüfung.
- **Offen:** Getrennter öffentlicher Event-Payloadvertrag (I02/C60), vollständige Vier-Domänen-Bindung (X01/C64) und vollständige UI-Komponentenkomposition auf Basis der vorhandenen invoke-Semantik (X04/C66).

Grundlage ist **SCXML 1.0, W3C Recommendation vom 1. September 2015**, mit abgeglichenen Errata und publizierten XSD-Definitionen. Bewertet wird die Sprache, nicht ein konkreter Interpreter. Ausdrucks-/Datensemantik hängt vom gewählten Datenmodell ab. **Keine Praxis-, Validator- oder Laufzeittests** wurden durchgeführt. N ist auf die definierte Standardkernsemantik begrenzt; Erweiterungen und optionale Hostdienste werden nicht pauschal zugerechnet.

## XState auf einen Blick – vertieft geprüft

**21 der 24 zuvor offenen XState-Felder sind geklärt; 3 bleiben mit konkreter Frage offen.** Zusammen mit den 2 bisherigen Bewertungen sind 23 von 26 eingeordnet. Geprüft wurde ausschließlich XState.

- **Kann:** Zustände und Übergänge, typisierte Actor-Eingaben und öffentliche ausgegebene Events, Guards/Actions und Context-Verarbeitung beschreiben. Actor-Komposition bietet eigene Instanzen und Lebenszyklen.
- **Braucht Bindungen:** Konkrete UI-Tastatur-/Fokusereignisse und UI-Effekte benötigen Hostcode. Benutzerdefinierte Implementierungen bleiben JS/TS; serialisierte Namen oder persistierte Snapshots ersetzen diese Semantik nicht.
- **Nicht im Core:** Visuelle Regeln, Accessibility-Fachmodelle, UI-Anatomie sowie paketweite Domänenreferenzen, Ownership und Konfliktprüfung.
- **Offen:** vollständige Vier-Domänen-Bindung (X01/C79), vollständige UI-Komponentenkomposition (X04/C81) und eigenständige originale Artefakt-/Runtime-Schemavalidierung (X06/C83).

Stand: 24. Oktober 2026; offizielle v5-Dokumentation gelesen am 23. Oktober sowie Core **5.33.3** am Commit `8f25b68f3953a9dd3c146a76f1f4972aba092a3f`. E1/E2, **keine Ausführung, Installation oder Tests**. N gilt für den untersuchten Core, nicht für beliebige Hostintegrationen. Gesamtverteilung: D6, A2, N15, U3.

## Zag auf einen Blick – vertieft geprüft

**21 der 25 zuvor offenen Zag-Felder sind geklärt; 4 bleiben mit konkreter Frage offen.** Zusammen mit dem bisherigen G02/A sind 22 von 26 eingeordnet. Andere Kandidatenbewertungen bleiben unverändert.

- **Kann im Web-Toolkit:** typisierte Properties und Callback-Payloads, Anatomie/Teil-IDs, Zustände/Guards/Aktionen, konkrete Tastatur-/Fokusbindungen, ARIA-Beziehungen und dynamische Ergebnisansagen beschreiben beziehungsweise ausführen. Das ist dokumentiert und im Quelltext gelesen, hier nicht ausgeführt.
- **Visuelle Teilbeiträge:** Popper definiert Anker, Platzierung, Abstände und verfügbare Maximalfläche; ScrollArea definiert Overflow-/Scrollregeln. Dimensionswerte sind typisiert. Zustandsvarianten lassen sich über dokumentierte Attribute an externe CSS-Regeln binden (R). Daraus folgt kein vollständiges Token-/Theme-System oder eine automatische Fünf-Zeilen-Grenze.
- **Grenzen:** JS/TS und DOM bleiben nötig. Core-Konfiguration, konkrete Maschinen, `connect` und Framework-Lifecycle haben verschiedene Aufgaben. Kein SCXML-Kompatibilitätsanspruch; kein eigener Theme-, externer Contract-Versionsresolver oder Vier-Domänen-Konflikt-/Ownershipvertrag im geprüften Umfang.
- **Offen:** vier unabhängig geführte Domänen (X01/C98), vollständige fachliche Referenzbindung (X03/C99), eigenständige Komponentenkomposition als Contract (X04/C100) und originale separate Artefaktvalidierung (X06/C102). Bestehende DOM-/CSS-/Maschinenmechanismen sind positive Teilbeiträge, kein Beweis vollständiger Integration.

Quellenstand: 24. Oktober 2026; **@zag-js/core und @zag-js/combobox 1.46.0** laut gepinnten Paketdateien am Commit `cafda74ba915d5abc5abb20abdde3a719d8e4e9c`. Geprüft wurden offizielle Dokumentation und ausgewählte Typ-/Quelltextdefinitionen (E1/E2), **keine Praxis-, Laufzeit- oder Validatortests**. Kein vollständiges Adapter-, Accessibility- oder Reifegradaudit. Verteilung: D16, R1, A1, N4, U4.

## Google DESIGN.md auf einen Blick – vertieft geprüft

**20 der 22 zuvor offenen Felder sind geklärt; X01 und X06 bleiben offen.** Insgesamt 24 von 26 eingeordnet: D4, N20, U2. Die vier bisherigen Klassifizierungen bleiben erhalten; die Quellenverweise sind jetzt auf den gepinnten Vollabgleich ausgerichtet.

- **Kann:** sprachneutrale visuelle Werte in Markdown/YAML und benannte Stylevarianten. Interne Tokenreferenzen und ein offizieller Parser-/Model-/Linterpfad sind vorhanden.
- **Nicht im definierten alpha-Kern:** öffentliche API-/Payload- oder Anatomieverträge, Themeauflösung, formale Anker-/Flächen-/Overflowmodelle, UX-Automaten, Accessibility-Interaktionsmodelle, UI-Instanzen und paketweite Ownership-/Konfliktprüfung. Lokale Tokenprüfungen und die Vorrangregel Tokens vor Prosa sind reale Teilbeiträge.
- **Offen:** vollständige Vier-Domänen-Bindung (X01/C122) und vollständiger eigenständiger Originalschema-Vertrag (X06/C127). Der offizielle Linter ist belegt; seine Existenz ersetzt kein vollständiges unabhängiges Schema und keine ausgeführte Konformitätsprüfung.

Stand: 24. Oktober 2026, Spezifikation **alpha**, CLI-/Librarypaket **0.4.0**, Commit `6e5da5382f41edbba9d73b2c62f33f32e9971f15`. Beschreibung: Markdown mit YAML; Werkzeuge: JS/TS auf Node >=18. Spec und CLI sind laut README in Entwicklung. Keine stabile Produktreife oder Migrationsgarantie nachgewiesen. Keine Ausführung.

## OpenUI auf einen Blick – vertieft geprüft

**21 der 23 zuvor offenen Felder sind geklärt; X01 und X06 bleiben offen.** Insgesamt 24 von 26 eingeordnet: D3, N21, U2. Gemeint ist openuispec.org / ctate/openui, nicht open-ui.org.

- **Kann:** einfache öffentliche Props mit Typmetadaten, Enum, Default und Required in YAML oder JSON beschreiben. Der fachliche Kern verlangt keine JS-/React-Funktionen.
- **Nicht im definierten draft-01-Kern:** strukturierte Event-Payloaddeklarationen, Teile-/Instanzmodell, visuelle/UX-/Accessibility-Fachmodelle sowie domänenübergreifende Referenz-, Versions- und Konflikt-/Ownershipsemantik. Event-/Accessibility-Empfehlungen sind keine ausgearbeitete formale Modellierung; State/Lifecycle ist ausdrücklich Zukunftsarbeit.
- **Offen:** Vier-Domänen-Integration (X01/C148) und kanonisches Originalschema samt nutzbarer Validierung (X06/C153). Entwurf, TS-Interface und Schema-Beschreibungsobjekt weichen voneinander ab. Letzteres darf nicht ungeprüft als ausführbares JSON Schema ausgegeben werden.

Stand: 24. Oktober 2026, **draft-01**, Commit `09d39b211dcaa2e227ed38e312c8822e193cfea9`. Die Website verweist über die frühere specui/openui-Adresse auf ctate/openui. Websitepaket 0.1.0/private ist kein Validatorrelease. Kein Originalvalidator oder belastbare Kompatibilitätszusage nachgewiesen; kein Validatorversuch. Website-eigenes Dark Mode/Scrollen zählt nicht als Contractfähigkeit.

## AgentsORG auf einen Blick – vertieft geprüft

**20 der 22 zuvor offenen Felder geklärt; X01 und X08 bleiben offen.** Verteilung D7/N17/U2. Das Visualmodell bietet strukturierte Werte, Varianten, Theme-Overlays, benannte Anatomie und ein separates Originalschema. Ein realer Python-Linter verwendet das Schema und ergänzt lokale Prüfungen, deckt aber nicht jede Normforderung ab. Ein paketierter Standalone-Datei-CLI ist nicht belegt; der gelesene Einstieg scannt Repo-Beispiele.

Kein eigenes öffentliches API-/UX-/Accessibility-Modell, keine formale Anker-/Flächen-/Overflowsemantik und kein versioniertes UI-Instanz-/Vier-Domänen-Prüfmodell im definierten Kern. Visual-Ownership ist ein realer Teilbeitrag; ihre Übertragung auf vier unabhängige führende Quellen bleibt offen. Stand: design.v1 / Vertrag 1.3, Commit `014a1864c641f8e9792ed76de93c95493489dd8c`, 24. Oktober 2026, E1/E2, keine Ausführung oder Produktionsreifeentscheidung.

## UXSpec auf einen Blick – vertieft geprüft

**12 der tatsächlich 17 zuvor offenen Felder geklärt; V04/V05/V06/X01/X03 bleiben offen.** Neun D waren bereits vorhanden; die frühere Chatangabe „19/27“ wird nicht übernommen. Verteilung D14/R2/N5/U5.

UXSpec beschreibt JSON-Verhalten, typisierte Host-Eingaben und eingehende Ereignispayloads, strukturierte visuelle Werte/Varianten sowie parametrisierte Elemente. ARIA-Attribute und live:polite sind explizite Referenzbeiträge (R), kein eigenes vollständiges Accessibility-Patternmodell. `$visual` ist im Originalschema optional. Das beweist noch kein vollständiges getrenntes Vier-Domänen-Paket. Formale neutrale Overlay-/Flächen-/Overflowsemantik bleibt offen.

**Schema, CLI validate und Compiler sind unterschiedliche Prüfpfade:** Originales JSON Schema vorhanden; CLI validate lädt es nicht, sondern prüft ausgewählte Regeln. compile ruft validateSpec nicht auf. Compilererfolg oder erzeugte Assertions beweisen deshalb keine Schema-/Accessibility-Konformität. Lokale Imports sind belegt, reproduzierbare externe Versionsauflösung im geprüften Importkern nicht. Stand: Dokument v0.2, Paket 0.2.3, Commit `20dfae0e7224d952e198afdf4ffed26d6fd67180`, 24. Oktober 2026. Keine Ausführung oder native Kompatibilität nachgewiesen.

## Ark UI auf einen Blick – vertieft geprüft

**21 der 24 zuvor offenen Felder geklärt; X01/X03/X06 bleiben offen.** Zwei vorhandene D für Identität/Komposition bleiben in enger Web-Komponentenrolle erhalten. Verteilung D9/R9/A1/N4/U3.

Ark liefert typisierte Frameworkkomponenten, Props/Events, Teile, IDs, Providerkontexte und konkrete Web-Komposition. Verhaltens-, Daten-, Geometrie- und Scrollbeiträge sind über ausdrücklich belegte Zag-Maschinen-/Typ-/Connectorbindungen als R bewertet; CSS-Varianten ebenso über dokumentierte CSS-Bindung. Ark ist keine eigene neutrale Statechart-Sprache. Konkrete Eingabe-/ARIA-/APG-Bindungen sind dokumentiert, aber nicht praktisch auf Konformität getestet.

Vier unabhängige Domänenquellen, neutrale fachliche Referenzen und ein Originalschema/Artefaktvalidator bleiben ungeklärt. **API-Grenze:** Der geprüfte React-Root reicht loading nicht im Machine-Props-Split weiter, obwohl der referenzierte Zag-Typ es kennt; keine automatische Ladeansage über diesen Root behaupten. Stand: React-Paket 5.39.3, Ark-Commit `c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc`, dokumentierte Zag-Abhängigkeiten 1.46.0, 24. Oktober 2026. Quellpaketstand, kein Registry-/Runtime-/Gesamtadapteraudit.

## Grundlagen

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G01 Maschinenlesbare Beschreibung | [D/C01](CLAIMS.md#c01) | [D/C130](CLAIMS.md#c130) | [D/C104](CLAIMS.md#c104) | [D/C156](CLAIMS.md#c156) | [D/C14](CLAIMS.md#c14) | [D/C182](CLAIMS.md#c182) | [D/C22](CLAIMS.md#c22) | [D/C70](CLAIMS.md#c70) |
| G02 Sprachneutrale fachliche Semantik | [A/C03](CLAIMS.md#c03) | [D/C131](CLAIMS.md#c131) | [D/C105](CLAIMS.md#c105) | [D/C157](CLAIMS.md#c157) | [D/C48](CLAIMS.md#c48) | [D/C183](CLAIMS.md#c183) | [D/C22](CLAIMS.md#c22) | [A/C24](CLAIMS.md#c24) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G01 Maschinenlesbare Beschreibung | [D/C85](CLAIMS.md#c85) | [D/C208](CLAIMS.md#c208) | U | [D/C29](CLAIMS.md#c29) | U | U | U | U |
| G02 Sprachneutrale fachliche Semantik | [A/C25](CLAIMS.md#c25) | [A/C209](CLAIMS.md#c209) | U | U | U | U | U | U |

## Interface

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I01 Öffentliche Eigenschaften mit Typangaben | [D/C01](CLAIMS.md#c01) | [D/C132](CLAIMS.md#c132) | [N/C106](CLAIMS.md#c106) | [N/C158](CLAIMS.md#c158) | [N/C49](CLAIMS.md#c49) | [D/C184](CLAIMS.md#c184) | [N/C59](CLAIMS.md#c59) | [D/C71](CLAIMS.md#c71) |
| I02 Öffentliche Ereignisse mit Payload | [U/C37](CLAIMS.md#c37) | [N/C133](CLAIMS.md#c133) | [N/C107](CLAIMS.md#c107) | [N/C159](CLAIMS.md#c159) | [N/C49](CLAIMS.md#c49) | [D/C185](CLAIMS.md#c185) | [U/C60](CLAIMS.md#c60) | [D/C72](CLAIMS.md#c72) |
| I03 Benannte Komponentenbestandteile | [D/C02](CLAIMS.md#c02) | [N/C134](CLAIMS.md#c134) | [N/C108](CLAIMS.md#c108) | [D/C160](CLAIMS.md#c160) | [N/C49](CLAIMS.md#c49) | [D/C186](CLAIMS.md#c186) | [N/C59](CLAIMS.md#c59) | [N/C73](CLAIMS.md#c73) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I01 Öffentliche Eigenschaften mit Typangaben | [D/C86](CLAIMS.md#c86) | [D/C210](CLAIMS.md#c210) | U | U | U | U | U | U |
| I02 Öffentliche Ereignisse mit Payload | [D/C86](CLAIMS.md#c86) | [D/C211](CLAIMS.md#c211) | U | U | U | U | U | U |
| I03 Benannte Komponentenbestandteile | [D/C87](CLAIMS.md#c87) | [D/C212](CLAIMS.md#c212) | U | U | [D/C30](CLAIMS.md#c30) | U | U | U |

## Visual

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 Typisierte Designwerte | [R/C38](CLAIMS.md#c38) | [N/C135](CLAIMS.md#c135) | [D/C109](CLAIMS.md#c109) | [D/C161](CLAIMS.md#c161) | [D/C14](CLAIMS.md#c14) | [D/C187](CLAIMS.md#c187) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V02 Visuelle Zustandsvarianten | [N/C39](CLAIMS.md#c39) | [N/C136](CLAIMS.md#c136) | [D/C110](CLAIMS.md#c110) | [D/C162](CLAIMS.md#c162) | [D/C50](CLAIMS.md#c50) | [D/C188](CLAIMS.md#c188) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V03 Themes und Dark Mode | [N/C39](CLAIMS.md#c39) | [N/C137](CLAIMS.md#c137) | [N/C111](CLAIMS.md#c111) | [D/C163](CLAIMS.md#c163) | [D/C15](CLAIMS.md#c15) | [N/C189](CLAIMS.md#c189) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V04 Formale relative Geometrie | [N/C40](CLAIMS.md#c40) | [N/C138](CLAIMS.md#c138) | [N/C112](CLAIMS.md#c112) | [N/C164](CLAIMS.md#c164) | [N/C51](CLAIMS.md#c51) | [U/C190](CLAIMS.md#c190) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V05 Formale Flächenbegrenzung | [N/C40](CLAIMS.md#c40) | [N/C139](CLAIMS.md#c139) | [N/C113](CLAIMS.md#c113) | [N/C165](CLAIMS.md#c165) | [N/C51](CLAIMS.md#c51) | [U/C191](CLAIMS.md#c191) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V06 Overflow und Scrollen | [N/C40](CLAIMS.md#c40) | [N/C140](CLAIMS.md#c140) | [N/C114](CLAIMS.md#c114) | [N/C166](CLAIMS.md#c166) | [N/C51](CLAIMS.md#c51) | [U/C192](CLAIMS.md#c192) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 Typisierte Designwerte | [D/C88](CLAIMS.md#c88) | [R/C213](CLAIMS.md#c213) | U | U | U | U | U | U |
| V02 Visuelle Zustandsvarianten | [R/C89](CLAIMS.md#c89) | [R/C214](CLAIMS.md#c214) | [D/C28](CLAIMS.md#c28) | U | U | U | U | U |
| V03 Themes und Dark Mode | [N/C90](CLAIMS.md#c90) | [N/C215](CLAIMS.md#c215) | U | U | U | U | U | U |
| V04 Formale relative Geometrie | [D/C91](CLAIMS.md#c91) | [R/C216](CLAIMS.md#c216) | U | U | U | U | U | [D/C33](CLAIMS.md#c33) |
| V05 Formale Flächenbegrenzung | [D/C92](CLAIMS.md#c92) | [R/C217](CLAIMS.md#c217) | U | U | U | U | U | U |
| V06 Overflow und Scrollen | [D/C93](CLAIMS.md#c93) | [R/C218](CLAIMS.md#c218) | U | U | U | U | U | [D/C34](CLAIMS.md#c34) |

## Behavior

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B01 Zustände und Ereignisübergänge | [N/C41](CLAIMS.md#c41) | [N/C141](CLAIMS.md#c141) | [N/C115](CLAIMS.md#c115) | [N/C167](CLAIMS.md#c167) | [N/C52](CLAIMS.md#c52) | [D/C193](CLAIMS.md#c193) | [D/C22](CLAIMS.md#c22) | [D/C23](CLAIMS.md#c23) |
| B02 Guards und Aktionen | [N/C41](CLAIMS.md#c41) | [N/C142](CLAIMS.md#c142) | [N/C116](CLAIMS.md#c116) | [N/C168](CLAIMS.md#c168) | [N/C52](CLAIMS.md#c52) | [D/C194](CLAIMS.md#c194) | [D/C22](CLAIMS.md#c22) | [D/C75](CLAIMS.md#c75) |
| B03 Ereignis- und Kontextdaten | [N/C41](CLAIMS.md#c41) | [N/C143](CLAIMS.md#c143) | [N/C117](CLAIMS.md#c117) | [N/C169](CLAIMS.md#c169) | [N/C52](CLAIMS.md#c52) | [D/C195](CLAIMS.md#c195) | [D/C22](CLAIMS.md#c22) | [D/C76](CLAIMS.md#c76) |
| B04 Bindung von Eingaben an UX-Aktionen | [N/C41](CLAIMS.md#c41) | [N/C144](CLAIMS.md#c144) | [N/C118](CLAIMS.md#c118) | [N/C170](CLAIMS.md#c170) | [N/C52](CLAIMS.md#c52) | [D/C196](CLAIMS.md#c196) | [A/C62](CLAIMS.md#c62) | [A/C77](CLAIMS.md#c77) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B01 Zustände und Ereignisübergänge | [D/C94](CLAIMS.md#c94) | [R/C219](CLAIMS.md#c219) | U | U | U | U | U | U |
| B02 Guards und Aktionen | [D/C94](CLAIMS.md#c94) | [R/C220](CLAIMS.md#c220) | U | U | U | U | U | U |
| B03 Ereignis- und Kontextdaten | [D/C94](CLAIMS.md#c94) | [R/C221](CLAIMS.md#c221) | U | U | U | U | U | U |
| B04 Bindung von Eingaben an UX-Aktionen | [D/C95](CLAIMS.md#c95) | [D/C222](CLAIMS.md#c222) | U | U | U | U | U | U |

## Accessibility

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 Rollen, Namen und Beziehungen | [N/C42](CLAIMS.md#c42) | [N/C145](CLAIMS.md#c145) | [N/C119](CLAIMS.md#c119) | [N/C171](CLAIMS.md#c171) | [N/C53](CLAIMS.md#c53) | [R/C197](CLAIMS.md#c197) | [N/C63](CLAIMS.md#c63) | [N/C78](CLAIMS.md#c78) |
| A02 Fokus- und Tastaturanforderungen | [N/C42](CLAIMS.md#c42) | [N/C146](CLAIMS.md#c146) | [N/C120](CLAIMS.md#c120) | [N/C172](CLAIMS.md#c172) | [N/C53](CLAIMS.md#c53) | [N/C198](CLAIMS.md#c198) | [N/C63](CLAIMS.md#c63) | [N/C78](CLAIMS.md#c78) |
| A03 Dynamische Rückmeldungen | [N/C42](CLAIMS.md#c42) | [N/C147](CLAIMS.md#c147) | [N/C121](CLAIMS.md#c121) | [N/C173](CLAIMS.md#c173) | [N/C53](CLAIMS.md#c53) | [R/C199](CLAIMS.md#c199) | [N/C63](CLAIMS.md#c63) | [N/C78](CLAIMS.md#c78) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 Rollen, Namen und Beziehungen | [D/C96](CLAIMS.md#c96) | [D/C223](CLAIMS.md#c223) | U | U | U | [D/C31](CLAIMS.md#c31) | U | U |
| A02 Fokus- und Tastaturanforderungen | [D/C96](CLAIMS.md#c96) | [D/C224](CLAIMS.md#c224) | U | U | U | U | [D/C32](CLAIMS.md#c32) | U |
| A03 Dynamische Rückmeldungen | [D/C97](CLAIMS.md#c97) | [R/C225](CLAIMS.md#c225) | U | U | U | [D/C31](CLAIMS.md#c31) | U | U |

## Integration

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X01 Vier unabhängig beschreibbare Domänen | [U/C43](CLAIMS.md#c43) | [U/C148](CLAIMS.md#c148) | [U/C122](CLAIMS.md#c122) | [U/C174](CLAIMS.md#c174) | [U/C54](CLAIMS.md#c54) | [U/C200](CLAIMS.md#c200) | [U/C64](CLAIMS.md#c64) | [U/C79](CLAIMS.md#c79) |
| X02 Stabile Elementidentität | [N/C44](CLAIMS.md#c44) | [N/C149](CLAIMS.md#c149) | [N/C123](CLAIMS.md#c123) | [N/C175](CLAIMS.md#c175) | [N/C55](CLAIMS.md#c55) | [D/C201](CLAIMS.md#c201) | [N/C65](CLAIMS.md#c65) | [N/C80](CLAIMS.md#c80) |
| X03 Domänenübergreifende Referenzen | [N/C44](CLAIMS.md#c44) | [N/C150](CLAIMS.md#c150) | [N/C124](CLAIMS.md#c124) | [N/C176](CLAIMS.md#c176) | [N/C55](CLAIMS.md#c55) | [U/C202](CLAIMS.md#c202) | [N/C65](CLAIMS.md#c65) | [N/C80](CLAIMS.md#c80) |
| X04 Wiederverwendbare Komponenteninstanzen | [N/C44](CLAIMS.md#c44) | [N/C151](CLAIMS.md#c151) | [N/C125](CLAIMS.md#c125) | [N/C177](CLAIMS.md#c177) | [N/C55](CLAIMS.md#c55) | [D/C203](CLAIMS.md#c203) | [U/C66](CLAIMS.md#c66) | [U/C81](CLAIMS.md#c81) |
| X05 Externe versionierte Abhängigkeiten | [N/C45](CLAIMS.md#c45) | [N/C152](CLAIMS.md#c152) | [N/C126](CLAIMS.md#c126) | [N/C178](CLAIMS.md#c178) | [N/C56](CLAIMS.md#c56) | [N/C204](CLAIMS.md#c204) | [N/C67](CLAIMS.md#c67) | [N/C82](CLAIMS.md#c82) |
| X06 Eigene Schemavalidatoren erhalten | [D/C46](CLAIMS.md#c46) | [U/C153](CLAIMS.md#c153) | [U/C127](CLAIMS.md#c127) | [D/C179](CLAIMS.md#c179) | [D/C57](CLAIMS.md#c57) | [D/C205](CLAIMS.md#c205) | [D/C68](CLAIMS.md#c68) | [U/C83](CLAIMS.md#c83) |
| X07 Referenz- und Konfliktprüfung des Pakets | [N/C47](CLAIMS.md#c47) | [N/C154](CLAIMS.md#c154) | [N/C128](CLAIMS.md#c128) | [N/C180](CLAIMS.md#c180) | [N/C58](CLAIMS.md#c58) | [N/C206](CLAIMS.md#c206) | [N/C69](CLAIMS.md#c69) | [N/C84](CLAIMS.md#c84) |
| X08 Eindeutige führende Quelle | [N/C47](CLAIMS.md#c47) | [N/C155](CLAIMS.md#c155) | [N/C129](CLAIMS.md#c129) | [U/C181](CLAIMS.md#c181) | [N/C58](CLAIMS.md#c58) | [N/C207](CLAIMS.md#c207) | [N/C69](CLAIMS.md#c69) | [N/C84](CLAIMS.md#c84) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X01 Vier unabhängig beschreibbare Domänen | [U/C98](CLAIMS.md#c98) | [U/C226](CLAIMS.md#c226) | U | U | U | U | U | U |
| X02 Stabile Elementidentität | [D/C87](CLAIMS.md#c87) | [D/C227](CLAIMS.md#c227) | U | U | [D/C30](CLAIMS.md#c30) | U | U | U |
| X03 Domänenübergreifende Referenzen | [U/C99](CLAIMS.md#c99) | [U/C228](CLAIMS.md#c228) | U | U | U | U | U | U |
| X04 Wiederverwendbare Komponenteninstanzen | [U/C100](CLAIMS.md#c100) | [D/C229](CLAIMS.md#c229) | U | U | U | U | U | U |
| X05 Externe versionierte Abhängigkeiten | [N/C101](CLAIMS.md#c101) | [N/C230](CLAIMS.md#c230) | U | U | U | U | U | U |
| X06 Eigene Schemavalidatoren erhalten | [U/C102](CLAIMS.md#c102) | [U/C231](CLAIMS.md#c231) | U | U | U | U | U | U |
| X07 Referenz- und Konfliktprüfung des Pakets | [N/C103](CLAIMS.md#c103) | [N/C232](CLAIMS.md#c232) | U | U | U | U | U | U |
| X08 Eindeutige führende Quelle | [N/C103](CLAIMS.md#c103) | [N/C233](CLAIMS.md#c233) | U | U | U | U | U | U |

## Einordnung der ersten Befunde

R ist keine pauschale Komplettbewertung: Ein dokumentierter Tokenalias erfüllt nur einen Wertbezug. Er deckt die gesamte Anforderung einer domänenübergreifenden Referenz oder einer Komponenteninstanz nicht ab. C36 beschreibt diesen Teilbeitrag. Bei CEM V01 bezeichnet R dagegen ausdrücklich die im Format benannte CSS-Wertsyntax (C38), keine Komponentenreferenz. Referenzmechanismen werden daher nicht überbewertet.

- **OpenUI:** Einfache Props sind konkret beschrieben. Die alte Chatbehauptung einer umfassenden Event-/Payloadbeschreibung ist damit nicht bestätigt (C05). State/Lifecycle ist in draft-01 zukünftige Arbeit (C06).
- **Google DESIGN.md:** Strukturierte Werte und benannte Stylevarianten sind vorhanden. Das ist noch keine standardisierte Geometriesprache für Beziehungen zwischen Elementen (C07–C10).
- **UXSpec:** Verhalten ohne `$visual` ist auf der gelesenen Schemaebene nicht ausgeschlossen; die frühere Vermutung einer zwingenden Visualpflicht ist zu korrigieren (C17). Compilerverhalten und Domänenbindung sind weiterhin offen. Schemafelder wie `container: object` beweisen keine vollständig typisierte Layoutsemantik.
- **Komposition:** UXSpec-Elementreferenzen, Ark-Komposition und OpenPencil-ID-Bindungen sind reale unterschiedliche Mechanismen (C20/C27/C30). Keiner dieser Befunde beweist allein ein gemeinsames versioniertes Komponentenpaket über alle vier Domänen.
- **Accessibility:** ARIA liefert Semantik und APG Interaktionswissen. Die konkreten Produktregeln und eine ausführbare Paketprüfung müssen gesondert abgebildet werden (C31/C32).

## Warum viele Zellen offen bleiben

Diese Lieferung priorisiert belastbare Teilbefunde gegenüber flächendeckenden Vermutungen. Besonders X03/X05/X06/X07/X08 verlangen Prüfung der Verbindungen und konkreter Werkzeuge. Eine Übersichtsseite, ein Feld namens version oder ein vorhandenes JSON Schema beweisen diese Anforderungen nicht. uSpec, Panda, XState und OpenPencil benötigen vertiefte Schema-/Quelltextprüfung. Bei keinem Kandidaten wurde das gesamte Contract-Paket praktisch validiert.

Die vorgeschlagene Eigenleistung ist daher **noch keine implementierte Architektur**: Möglicherweise werden Identitätsabbildung, externe Versionsauflösung, Domänenbindungen und Konfliktprüfung benötigt. Ob vorhandene Mechanismen ausreichen, bleibt anhand der folgenden Versuche zu klären: [RESEARCH-PLAN.md](RESEARCH-PLAN.md).
