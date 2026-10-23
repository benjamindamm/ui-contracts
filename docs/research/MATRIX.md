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

## Grundlagen

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G01 Maschinenlesbare Beschreibung | [D/C01](CLAIMS.md#c01) | [D/C04](CLAIMS.md#c04) | [D/C07](CLAIMS.md#c07) | [D/C11](CLAIMS.md#c11) | [D/C14](CLAIMS.md#c14) | [D/C16](CLAIMS.md#c16) | [D/C22](CLAIMS.md#c22) | [D/C70](CLAIMS.md#c70) |
| G02 Sprachneutrale fachliche Semantik | [A/C03](CLAIMS.md#c03) | U | U | U | [D/C48](CLAIMS.md#c48) | [D/C16](CLAIMS.md#c16) | [D/C22](CLAIMS.md#c22) | [A/C24](CLAIMS.md#c24) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G01 Maschinenlesbare Beschreibung | U | U | U | [D/C29](CLAIMS.md#c29) | U | U | U | U |
| G02 Sprachneutrale fachliche Semantik | [A/C25](CLAIMS.md#c25) | U | U | U | U | U | U | U |

## Interface

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I01 Öffentliche Eigenschaften mit Typangaben | [D/C01](CLAIMS.md#c01) | [D/C04](CLAIMS.md#c04) | U | U | [N/C49](CLAIMS.md#c49) | U | [N/C59](CLAIMS.md#c59) | [D/C71](CLAIMS.md#c71) |
| I02 Öffentliche Ereignisse mit Payload | [U/C37](CLAIMS.md#c37) | U | U | U | [N/C49](CLAIMS.md#c49) | U | [U/C60](CLAIMS.md#c60) | [D/C72](CLAIMS.md#c72) |
| I03 Benannte Komponentenbestandteile | [D/C02](CLAIMS.md#c02) | U | U | U | [N/C49](CLAIMS.md#c49) | U | [N/C59](CLAIMS.md#c59) | [N/C73](CLAIMS.md#c73) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I01 Öffentliche Eigenschaften mit Typangaben | U | U | U | U | U | U | U | U |
| I02 Öffentliche Ereignisse mit Payload | U | U | U | U | U | U | U | U |
| I03 Benannte Komponentenbestandteile | U | U | U | U | [D/C30](CLAIMS.md#c30) | U | U | U |

## Visual

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 Typisierte Designwerte | [R/C38](CLAIMS.md#c38) | U | [D/C07](CLAIMS.md#c07) | [D/C11](CLAIMS.md#c11) | [D/C14](CLAIMS.md#c14) | U | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V02 Visuelle Zustandsvarianten | [N/C39](CLAIMS.md#c39) | U | [D/C08](CLAIMS.md#c08) | [D/C12](CLAIMS.md#c12) | [D/C50](CLAIMS.md#c50) | [D/C18](CLAIMS.md#c18) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V03 Themes und Dark Mode | [N/C39](CLAIMS.md#c39) | U | U | [D/C12](CLAIMS.md#c12) | [D/C15](CLAIMS.md#c15) | U | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V04 Formale relative Geometrie | [N/C40](CLAIMS.md#c40) | U | [N/C09](CLAIMS.md#c09) | U | [N/C51](CLAIMS.md#c51) | U | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V05 Formale Flächenbegrenzung | [N/C40](CLAIMS.md#c40) | U | U | U | [N/C51](CLAIMS.md#c51) | U | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V06 Overflow und Scrollen | [N/C40](CLAIMS.md#c40) | U | U | U | [N/C51](CLAIMS.md#c51) | U | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 Typisierte Designwerte | U | U | U | U | U | U | U | U |
| V02 Visuelle Zustandsvarianten | U | U | [D/C28](CLAIMS.md#c28) | U | U | U | U | U |
| V03 Themes und Dark Mode | U | U | U | U | U | U | U | U |
| V04 Formale relative Geometrie | U | U | U | U | U | U | U | [D/C33](CLAIMS.md#c33) |
| V05 Formale Flächenbegrenzung | U | U | U | U | U | U | U | U |
| V06 Overflow und Scrollen | U | U | U | U | U | U | U | [D/C34](CLAIMS.md#c34) |

## Behavior

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B01 Zustände und Ereignisübergänge | [N/C41](CLAIMS.md#c41) | [N/C06](CLAIMS.md#c06) | U | U | [N/C52](CLAIMS.md#c52) | [D/C16](CLAIMS.md#c16) | [D/C22](CLAIMS.md#c22) | [D/C23](CLAIMS.md#c23) |
| B02 Guards und Aktionen | [N/C41](CLAIMS.md#c41) | U | U | U | [N/C52](CLAIMS.md#c52) | [D/C16](CLAIMS.md#c16) | [D/C22](CLAIMS.md#c22) | [D/C75](CLAIMS.md#c75) |
| B03 Ereignis- und Kontextdaten | [N/C41](CLAIMS.md#c41) | U | U | U | [N/C52](CLAIMS.md#c52) | [D/C16](CLAIMS.md#c16) | [D/C22](CLAIMS.md#c22) | [D/C76](CLAIMS.md#c76) |
| B04 Bindung von Eingaben an UX-Aktionen | [N/C41](CLAIMS.md#c41) | U | U | U | [N/C52](CLAIMS.md#c52) | [D/C18](CLAIMS.md#c18) | [A/C62](CLAIMS.md#c62) | [A/C77](CLAIMS.md#c77) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B01 Zustände und Ereignisübergänge | U | U | U | U | U | U | U | U |
| B02 Guards und Aktionen | U | U | U | U | U | U | U | U |
| B03 Ereignis- und Kontextdaten | U | U | U | U | U | U | U | U |
| B04 Bindung von Eingaben an UX-Aktionen | U | U | U | U | U | U | U | U |

## Accessibility

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 Rollen, Namen und Beziehungen | [N/C42](CLAIMS.md#c42) | U | U | U | [N/C53](CLAIMS.md#c53) | U | [N/C63](CLAIMS.md#c63) | [N/C78](CLAIMS.md#c78) |
| A02 Fokus- und Tastaturanforderungen | [N/C42](CLAIMS.md#c42) | U | U | U | [N/C53](CLAIMS.md#c53) | U | [N/C63](CLAIMS.md#c63) | [N/C78](CLAIMS.md#c78) |
| A03 Dynamische Rückmeldungen | [N/C42](CLAIMS.md#c42) | U | U | U | [N/C53](CLAIMS.md#c53) | U | [N/C63](CLAIMS.md#c63) | [N/C78](CLAIMS.md#c78) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 Rollen, Namen und Beziehungen | U | U | U | U | U | [D/C31](CLAIMS.md#c31) | U | U |
| A02 Fokus- und Tastaturanforderungen | U | U | U | U | U | U | [D/C32](CLAIMS.md#c32) | U |
| A03 Dynamische Rückmeldungen | U | U | U | U | U | [D/C31](CLAIMS.md#c31) | U | U |

## Integration

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X01 Vier unabhängig beschreibbare Domänen | [U/C43](CLAIMS.md#c43) | U | U | U | [U/C54](CLAIMS.md#c54) | U | [U/C64](CLAIMS.md#c64) | [U/C79](CLAIMS.md#c79) |
| X02 Stabile Elementidentität | [N/C44](CLAIMS.md#c44) | U | U | U | [N/C55](CLAIMS.md#c55) | [D/C19](CLAIMS.md#c19) | [N/C65](CLAIMS.md#c65) | [N/C80](CLAIMS.md#c80) |
| X03 Domänenübergreifende Referenzen | [N/C44](CLAIMS.md#c44) | U | U | U | [N/C55](CLAIMS.md#c55) | U | [N/C65](CLAIMS.md#c65) | [N/C80](CLAIMS.md#c80) |
| X04 Wiederverwendbare Komponenteninstanzen | [N/C44](CLAIMS.md#c44) | U | U | U | [N/C55](CLAIMS.md#c55) | [D/C20](CLAIMS.md#c20) | [U/C66](CLAIMS.md#c66) | [U/C81](CLAIMS.md#c81) |
| X05 Externe versionierte Abhängigkeiten | [N/C45](CLAIMS.md#c45) | U | U | U | [N/C56](CLAIMS.md#c56) | U | [N/C67](CLAIMS.md#c67) | [N/C82](CLAIMS.md#c82) |
| X06 Eigene Schemavalidatoren erhalten | [D/C46](CLAIMS.md#c46) | U | U | U | [D/C57](CLAIMS.md#c57) | U | [D/C68](CLAIMS.md#c68) | [U/C83](CLAIMS.md#c83) |
| X07 Referenz- und Konfliktprüfung des Pakets | [N/C47](CLAIMS.md#c47) | U | U | U | [N/C58](CLAIMS.md#c58) | U | [N/C69](CLAIMS.md#c69) | [N/C84](CLAIMS.md#c84) |
| X08 Eindeutige führende Quelle | [N/C47](CLAIMS.md#c47) | U | U | U | [N/C58](CLAIMS.md#c58) | U | [N/C69](CLAIMS.md#c69) | [N/C84](CLAIMS.md#c84) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X01 Vier unabhängig beschreibbare Domänen | U | U | U | U | U | U | U | U |
| X02 Stabile Elementidentität | U | [D/C27](CLAIMS.md#c27) | U | U | [D/C30](CLAIMS.md#c30) | U | U | U |
| X03 Domänenübergreifende Referenzen | U | U | U | U | U | U | U | U |
| X04 Wiederverwendbare Komponenteninstanzen | U | [D/C27](CLAIMS.md#c27) | U | U | U | U | U | U |
| X05 Externe versionierte Abhängigkeiten | U | U | U | U | U | U | U | U |
| X06 Eigene Schemavalidatoren erhalten | U | U | U | U | U | U | U | U |
| X07 Referenz- und Konfliktprüfung des Pakets | U | U | U | U | U | U | U | U |
| X08 Eindeutige führende Quelle | U | U | U | U | U | U | U | U |

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
