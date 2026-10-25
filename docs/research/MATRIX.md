# Anforderungsorientierte Abdeckungsmatrix

**Aktueller Stand,25. Oktober2026:** 16/16 Erstdurchgänge abgeschlossen;2 offene Nachweise (2 Integration,0 weitere),641 Bedingungen/102 Gruppen. Vollständige Integration bleibt unbelegt. [Aktueller Status](CURRENT-STATUS.md), [29er-Abgleich](REMAINING-29-REVIEW.md), [historische Notizen](MATRIX-PROGRESS-HISTORY.md).


Stand: 25. Oktober 2026. **Kandidaten-Durchgänge und gezielte Folgeprüfungen, weiterhin mit offenen Zellen.** Anforderungen stehen links, Kandidaten als Spalten. Zwei Spaltenblöcke je Abschnitt dienen nur der Lesbarkeit; dieselbe Anforderung gilt in beiden Blöcken. Die Kandidaten sind Beiträge unterschiedlicher Art, keine gleichartigen Komplettlösungen.

Der dokumentarische [Werkzeug-, Sprach- und Reifevergleich aller 16 Kandidaten](TOOLING-COMPARISON.md) führt Originalschema, tatsächliche Prüfpfade und verbleibende Grenzen zusammen. Seine ursprüngliche Vergleichstabelle ist dokumentarisch; die gekennzeichneten Folgeprüfungen ergänzen ausgeführte, begrenzte Nachweise.

Vor Verwendung lesen: [Kriterien und Herkunft](REQUIREMENTS.md), [Methode](METHODS.md), [Quellenstände](SOURCES.md), [Begründungen](CLAIMS.md).

**D** direkt · **R** über Referenz · **A** Adapter erforderlich · **N** im geprüften Umfang nicht abgedeckt · **U** ungeprüft. Ein Link wie D/C07 enthält Befund, Evidenzstufe und Grenze. Die meisten Befunde sind E1/E2; C418–C431 und C434–C435 belegen eng begrenzte E3-Prüfungen, keine vollständige Integration. U bedeutet weiterhin unzureichender Nachweis, auch nach einer dokumentarischen Prüfung; keine negative Eigenschaft. Es ist kein Kandidat bereits als Gesamtlösung ausgewählt.

Bei DTCG umfasst die Spalte Format **und** separat belegtes Resolver Module 2025.10. CSS Layout umfasst die getrennten Quellen zu Anchor Positioning und Overflow sowie seit der Gesamtprüfung ausdrücklich Media Queries 5 für V03. Die Verknüpfung beider ist nicht getestet. OpenPencil bezeichnet zunächst den Behaviour-Beitrag; für X05 wurde das originale Bibliotheks-/Revisionssubsystem und für V01/V03 ausdrücklich das Variablen-/Tokenexportmodell und für V04–V06 die Szenenlayout-/CSS-Projektion und für A02 ausdrücklich die Switch-Webpreview-/Reka-Bindung ergänzend geprüft. Bei D in einem spezialisierten Modell bleibt dessen technische Bindung bestehen; daraus folgt keine Abdeckung von G02 oder X03.

**Aktueller Reststand:** 2 U-Zellen: 2 Integration und 0 weitere. Seit der Gesamtprüfung sind CEM I02/C421 und SCXML I02/C425 als begrenzte Adapterbeiträge A nachgewiesen; [641 benannte ausgeführte Prüfbedingungen](experiments/INDEX.md) sind gespeichert. [Alle 72 Ausgangszellen](ALL-FIELDS-REVIEW.md) wurden dokumentarisch erneut ausgewertet, fünf begründet neu eingeordnet. Beide Detailvergleiche liegen vor: [UXSpec/SCXML](COMPARE-UXSPEC-SCXML.md), [DESIGN.md/Layout](COMPARE-DESIGN-LAYOUT.md). Statische HTML-Fixtures im Browser geprüft; keine bediente Produkt-UI oder AT-Versuche. [Aktuelles offenes Register](OPEN-FIELDS.md).

## CEM auf einen Blick – vertieft geprüft

**Erstrunde: 20 von 22 geklärt. Nach Folgeprüfungen: 22 von 22; keine U-Zelle im begrenzten CEM-Beitrag.** Mit den vier schon bewerteten Feldern sind 26 von 26 eingeordnet; viele davon sind N, keine Gesamteignung. Nur CEM wurde vertieft; andere Kandidatenbewertungen sind unverändert.

- **Kann:** Web-Komponenten-APIs mit Properties, Typangaben, Events, Slots und CSS-Parts dokumentieren. CSS-Designwerte lassen sich über `cssProperties.syntax/default` mit der Bedeutung der CSS-Wertsyntax beschreiben. Ein separates originales JSON Schema ist vorhanden.
- **Deckt im Standardkern nicht ab:** Layout/Scrollregeln, Stylezuordnung je Zustand, Themes, UX-Automaten, Accessibility-Regeln sowie UI-Instanzkomposition und paketweite Referenz-/Ownershipprüfung.
- **Noch offen:** dynamische und plattformübergreifende Gesamtbindung. X01 ist im begrenzten zusätzlichen Webprofil nun A/C447. I02 ist nun A/C421 für begrenzte TypeScript-/CustomEvent.detail-Auflösung. Das originale Gesamtschema lässt einen numerischen Eventnamen über einen allgemeinen Klassenzweig passieren (C419).

Geprüft wurden die vollständigen CEM-Typdefinitionen und das zugehörige JSON Schema am Commit `2570079a0525c26296f9ec39944f0c6e0f0461af`, ergänzt durch offizielle Format- und Analyzer-Dokumentation. **N gilt nur für die definierte Semantik dieses CEM-Kerns**, nicht für beliebige Erweiterungen, implementierte Komponenten oder Plugins. In dieser historischen CEM-Erstrunde wurden keine Tools installiert oder Laufzeittests ausgeführt. Die späteren Schema-/Payloadproben sind oben verlinkt.

## DTCG auf einen Blick – vertieft geprüft

**Alle 26 DTCG-Felder sind im jeweiligen begrenzten Umfang eingeordnet.** X01 ist nach dem zusätzlichen Webreferenzfall A/C454; dies ist kein universeller Integrationsnachweis. Die damalige DTCG-Erstvertiefung hatte X01 noch offen gelassen.

- **Kann:** Sprachneutrale, typisierte Designwerte austauschen (**Format Module**) und benannte Wertvarianten/Themes, Quellen und Auflösungsreihenfolge beschreiben (**Resolver Module**). Getrennte veröffentlichte Schemata sind verfügbar.
- **Deckt im definierten Kern nicht ab:** Komponenten-APIs, tatsächliches Layout/Scrollen, UX-Automaten, Accessibility-Regeln und UI-Komponenteninstanzen. Tokenverweise und Gruppenvererbung ersetzen diese Modelle nicht.
- **Begrenzt nachgewiesen:** DTCG als eigenständige Visualquelle mit Zusatzadapter im Webreferenzfall (X01 A/C454). Universelle Integration bleibt offen. Externe URI-Unterstützung und tatsächliche semantische Konformität sind werkzeugabhängig und wurden nicht ausgeführt.

Geprüft: Format und Resolver **2025.10**, jeweils getrennt, sowie ihre veröffentlichten JSON-Schemata. **N bezieht sich auf die definierte Semantik dieser Module**, nicht auf beliebige Herstellererweiterungen. In der historischen Erstvertiefung wurde kein Compiler-, Validator- oder Laufzeitversuch durchgeführt. Die spätere zusätzliche dimension-/Alias-Übersetzung ist C454/C455; kein originaler vollständiger DTCG-Validator. Insbesondere ist nur Referenzauflösung im selben Resolverdokument verpflichtend; externe Dateien/Netzwerkquellen sind nicht pauschal garantiert (C56).

## SCXML auf einen Blick – vertieft geprüft

**Erstrunde: 18 von 21 geklärt. Nach Folgeprüfungen: 21 von 21; keine U-Zelle im begrenzten SCXML-Beitrag.** Mit den fünf bereits belegten Feldern sind 26 von 26 eingeordnet; keine Aussage über vollständige Eignung. Nur SCXML wurde in diesem Schritt geprüft; ein abgeschlossener UXSpec-Durchgang wird nicht vorausgesetzt.

- **Kann:** Zustände, Ereignisübergänge, Guards, Aktionen und Datenverarbeitung definieren. `invoke` beschreibt eigene Verhaltensinstanzen mit Datenübergabe und Lebenszyklus. Eigenständige W3C-XSD-Schemata sind vorhanden.
- **Zusätzlich nötig:** Eine Hostbindung übersetzt UI-Tastatur-/Fokusereignisse und UI-Aktionen in beziehungsweise aus SCXML-Ereignissen (B04/C62). Kein universeller fertiger UI-Adapter ist nachgewiesen.
- **Nicht im Kern enthalten:** Design-/Layout-/Accessibility-Fachmodelle und eine vollständige domänenübergreifende UI-Instanz-/Ownershipprüfung.
- **Offen:** dynamische Vier-Domänen-/Hostbindung; X01 ist im begrenzten statischen Webprofil A/C447. I02 ist A/C425 für das statische zusätzliche CEM-/SCXML-Referenzprofil; öffentliche Hostroute nicht implementiert. X04 ist jetzt A/C408: konkreter invoke-Beitrag mit zusätzlichem UI-Bindungsbedarf.

Grundlage ist **SCXML 1.0, W3C Recommendation vom 1. September 2015**, mit abgeglichenen Errata und publizierten XSD-Definitionen. Bewertet wird die Sprache, nicht ein konkreter Interpreter. Ausdrucks-/Datensemantik hängt vom gewählten Datenmodell ab. **Keine Praxis-, Validator- oder Laufzeittests** wurden durchgeführt. N ist auf die definierte Standardkernsemantik begrenzt; Erweiterungen und optionale Hostdienste werden nicht pauschal zugerechnet.

## XState auf einen Blick – vertieft geprüft

**Erstrunde: 21 von 24 geklärt. Nach Gesamtprüfung: 22 von 24; 2 U bleiben.** Zusammen mit den 2 bisherigen Bewertungen sind 24 von 26 eingeordnet. Geprüft wurde ausschließlich XState.

- **Kann:** Zustände und Übergänge, typisierte Actor-Eingaben und öffentliche ausgegebene Events, Guards/Actions und Context-Verarbeitung beschreiben. Actor-Komposition bietet eigene Instanzen und Lebenszyklen.
- **Braucht Bindungen:** Konkrete UI-Tastatur-/Fokusereignisse und UI-Effekte benötigen Hostcode. Benutzerdefinierte Implementierungen bleiben JS/TS; serialisierte Namen oder persistierte Snapshots ersetzen diese Semantik nicht.
- **Nicht im Core:** Visuelle Regeln, Accessibility-Fachmodelle, UI-Anatomie sowie paketweite Domänenreferenzen, Ownership und Konfliktprüfung.
- **Offen:** vollständige Vier-Domänen-Bindung (X01/C79) und eigenständige originale Artefakt-/Runtime-Schemavalidierung (X06/C405). X04 ist A/C409 für vorhandene Actor-Komposition mit zusätzlicher UI-Bindung.

Stand: 24. Oktober 2026; offizielle v5-Dokumentation gelesen am 23. Oktober sowie Core **5.33.3** am Commit `8f25b68f3953a9dd3c146a76f1f4972aba092a3f`. E1/E2, **keine Ausführung, Installation oder Tests**. N gilt für den untersuchten Core, nicht für beliebige Hostintegrationen. Aktuelle Gesamtverteilung: D6, A3, N15, U2.

## Zag auf einen Blick – vertieft geprüft

**Erstrunde: 21 von 25 geklärt. Nach Gesamtprüfung: 22 von 25; 3 U bleiben.** Zusammen mit dem bisherigen G02/A sind 23 von 26 eingeordnet. Andere Kandidatenbewertungen bleiben unverändert.

- **Kann im Web-Toolkit:** typisierte Properties und Callback-Payloads, Anatomie/Teil-IDs, Zustände/Guards/Aktionen, konkrete Tastatur-/Fokusbindungen, ARIA-Beziehungen und dynamische Ergebnisansagen beschreiben beziehungsweise ausführen. Das ist dokumentiert und im Quelltext gelesen, hier nicht ausgeführt.
- **Visuelle Teilbeiträge:** Popper definiert Anker, Platzierung, Abstände und verfügbare Maximalfläche; ScrollArea definiert Overflow-/Scrollregeln. Dimensionswerte sind typisiert. Zustandsvarianten lassen sich über dokumentierte Attribute an externe CSS-Regeln binden (R). Daraus folgt kein vollständiges Token-/Theme-System oder eine automatische Fünf-Zeilen-Grenze.
- **Grenzen:** JS/TS und DOM bleiben nötig. Core-Konfiguration, konkrete Maschinen, `connect` und Framework-Lifecycle haben verschiedene Aufgaben. Kein SCXML-Kompatibilitätsanspruch; kein eigener Theme-, externer Contract-Versionsresolver oder Vier-Domänen-Konflikt-/Ownershipvertrag im geprüften Umfang.
- **Offen:** vier unabhängig geführte Domänen (X01/C98), vollständige fachliche Referenzbindung (X03/C99) und originale separate Artefaktvalidierung (X06/C406). X04 ist A/C410: reale Maschinenkomposition, neutraler Contract zusätzlich. Bestehende DOM-/CSS-/Maschinenmechanismen sind positive Teilbeiträge, kein Beweis vollständiger Integration.

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

**Nach gezielter Folgeprüfung sind 13 der tatsächlich 17 zuvor offenen Felder eingeordnet; V04/V06/X01/X03 bleiben U.** Die erste Runde hatte 12 geklärt. V05 ist jetzt A: Der konkrete Webadapterpfad für size.maxHeight/maxWidth ist belegt, eine neutrale Bindung bleibt nötig (C398). Neun D waren bereits vorhanden; die frühere Chatangabe „19/27“ wird nicht übernommen. Aktuelle Verteilung D14/R2/A1/N5/U4.

UXSpec beschreibt JSON-Verhalten, typisierte Host-Eingaben und eingehende Ereignispayloads, strukturierte visuelle Werte/Varianten sowie parametrisierte Elemente. ARIA-Attribute und live:polite sind explizite Referenzbeiträge (R), kein eigenes vollständiges Accessibility-Patternmodell. `$visual` ist im Originalschema optional. Das beweist noch kein vollständiges getrenntes Vier-Domänen-Paket. Formale neutrale Overlay-/Flächen-/Overflowsemantik bleibt offen.

**Schema, CLI validate und Compiler sind unterschiedliche Prüfpfade:** Originales JSON Schema vorhanden; CLI validate lädt es nicht, sondern prüft ausgewählte Regeln. compile ruft validateSpec nicht auf. Compilererfolg oder erzeugte Assertions beweisen deshalb keine Schema-/Accessibility-Konformität. Lokale Imports sind belegt, reproduzierbare externe Versionsauflösung im geprüften Importkern nicht. Stand: Dokument v0.2, Paket 0.2.3, Commit `20dfae0e7224d952e198afdf4ffed26d6fd67180`, 24. Oktober 2026. Keine Ausführung oder native Kompatibilität nachgewiesen.

## Ark UI auf einen Blick – vertieft geprüft

**21 der 24 zuvor offenen Felder geklärt; X01/X03/X06 bleiben offen.** Zwei vorhandene D für Identität/Komposition bleiben in enger Web-Komponentenrolle erhalten. Verteilung D9/R9/A1/N4/U3.

Ark liefert typisierte Frameworkkomponenten, Props/Events, Teile, IDs, Providerkontexte und konkrete Web-Komposition. Verhaltens-, Daten-, Geometrie- und Scrollbeiträge sind über ausdrücklich belegte Zag-Maschinen-/Typ-/Connectorbindungen als R bewertet; CSS-Varianten ebenso über dokumentierte CSS-Bindung. Ark ist keine eigene neutrale Statechart-Sprache. Konkrete Eingabe-/ARIA-/APG-Bindungen sind dokumentiert, aber nicht praktisch auf Konformität getestet.

Vier unabhängige Domänenquellen, neutrale fachliche Referenzen und ein Originalschema/Artefaktvalidator bleiben ungeklärt. **API-Grenze:** Der geprüfte React-Root reicht loading nicht im Machine-Props-Split weiter, obwohl der referenzierte Zag-Typ es kennt; keine automatische Ladeansage über diesen Root behaupten. Stand: React-Paket 5.39.3, Ark-Commit `c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc`, dokumentierte Zag-Abhängigkeiten 1.46.0, 24. Oktober 2026. Quellpaketstand, kein Registry-/Runtime-/Gesamtadapteraudit.

## Panda CSS auf einen Blick – vertieft geprüft

**22 der 25 zuvor offenen Felder geklärt; X01/X06/X08 bleiben offen.** Verteilung D8/R1/A3/N11/U3. Vorhandenes V02/D bestätigt.

Starker Visualbeitrag: typisierte Tokens, Slot-Rezepte, Varianten, Themes, Größen- und Overflowregeln. CSS Anchor Positioning ist als Referenzbeitrag R dokumentiert; Panda verwaltet Ankernamen nicht selbst. Frameworkwrapper und Designsystem-Paketauflösung bieten konkrete Adapteransätze, keine neutrale Komponenten-/Abhängigkeitssemantik. Kein UX-Automat oder eigenes Accessibility-Fachmodell im begrenzten Kern.

**Neu belegter JSON-Spec-Export:** normalisierter Metadatenindex, kein verlustloses vollständiges Style-Original. Reader prüft flach und vertraut Zeilen; CLI-Flagschema ist kein fachliches Contractschema. Vollständiger unabhängiger Visualvalidator und vierdomänige Ownership bleiben ungeklärt. Quellenstand 24. Oktober 2026, Defaultbranch v2, Commit `86f78a228204d63baa0b8bca2676d9f26190e449`, @pandacss/dev 2.4.0 / Node >=22 laut Paketdatei. Keine Installation oder Ausführung.

## uSpec auf einen Blick – vertieft geprüft

**20 der 25 zuvor offenen Felder geklärt; V04/V06/X01/X03/X08 bleiben offen.** Verteilung D12/R2/N7/U5. Gemeint ist redongreen/uSpec, nicht UXSpec.

Kanonisches JSON und abgeleitetes Markdown dokumentieren Figma-basierte Propertytypen, Anatomie, visuelle Zustands-/Modewerte, begrenzte Abmessungen, Quellidentität und Komponenteninstanzen. Benannte Plattform-Accessibility-Eigenschaften liefern Referenzbeiträge; Fokusmuster sind dokumentiert. Das sind beschreibende Quell-/Dokumentationsrollen, keine bewiesene neutrale Laufzeit oder UX-Ausführungssprache.

**Schema und Veröffentlichung trennen:** inline Ajv-Originalschema samt verwendeter Validatorfunktion vorhanden; die deklarierte öffentliche Schemaadresse lieferte Not Found. Das Schema ist in vielen Fachfeldern permissiv. Basevalidator und Evidence-/Cacheprüfungen haben eigenen Umfang; fertiges Laden prüft nicht dieselbe Evidencekette wie Build. Kein vollständiger Vier-Bereiche-Konfliktvalidator. Quellenstand 24. Oktober 2026, Commit `1e25e9b8bc2e694689ba0489594f38807a341f14`, Canonicalschema 1.0 / CLI-Paket 0.3.3. Keine Ausführung.

## OpenPencil auf einen Blick – vertieft geprüft

**Erstrunde: 12 von 24 geklärt. Nach Folgeprüfungen: 17 von 24; 7 U bleiben.** Verteilung D7/R1/A6/N5/U7. Vorhandene D für Anatomie/Identität bleiben erhalten. Untersucht ist der Behaviour-Beitrag von open-pencil/open-pencil; für X05 ergänzend das originale Bibliotheks-/Revisionssubsystem. Kein Audit des gesamten Editormodells.

Benannte Controlwerte, Parts, IDs und das exportierte Original-Valibot-Schema sind konkret vorhanden. Der Dateidecoder verwendet das Schema tatsächlich; Specauflösung und Prüfung fehlender Bindungen sind separate Schritte. Variantenbindung, Eingabeverarbeitung und Instanzkomposition bieten Adapteransätze. Das begrenzte Modell enthält aber keinen allgemeinen Autorvertrag für Ereignispayloads, Automaten, Guards oder Contextausdrücke; Previewcode ersetzt ihn nicht.

**Offen:** übrige Layout-/Scrollbeiträge, vollständige Accessibility-Bindungen, Vier-Domänen-Trennung/Referenzen, neutrale externe Fachmodell-/Versionsbindung und paketweite Ownership. Diese U wurden nicht zur Verringerung der Zahl negativ bewertet. Quellenstand 24. Oktober 2026, Commit `ab2875cc761ee6cff17d389ff1c85fedae50aeab`, @open-pencil/scene-graph 0.16.0. Keine Vorschau-, Import-/Export- oder Laufzeitprobe.

**Folgeprüfung X05:** A/C411 statt U; explizite Bibliotheksrevision wird tatsächlich aufgelöst und materialisiert. latest ohne Revisionspin bleibt nicht reproduzierbar. Andere externe Fachmodelle und Roundtrip sind nicht bewiesen.

## WAI-ARIA auf einen Blick – vertieft geprüft

**19 der 24 zuvor offenen Felder geklärt; 5 bleiben U.** Verteilung D6/R2/A2/N11/U5. Eigener Beitrag: Rollen, typisierte Accessibility-Properties, Namen/Relationen, Fokuspflichten und dynamische Aktualisierungssemantik. Host-IDREF und CSS-Attributselektoren sind dokumentierte Referenzbeiträge, keine selbstständigen UI-Instanz-/Visualmodelle.

ARIA erzeugt nicht automatisch richtige Interaktion. §9 begrenzt Browserprüfung ausdrücklich; etwa zyklische Ownership oder tatsächliche Checkboxfunktion werden nicht umfassend verifiziert. Ein vollständiger separater neutraler Artefaktvalidator und Vier-Domänen-Ownership bleiben offen. Baseline WAI-ARIA **1.2 REC 06.06.2023**; 1.3 **WD 04.06.2026** getrennt. Core-AAM 1.2 **CRD 21.10.2026** und Accname 1.2 **WD 21.10.2026** haben eigene Reifegrade. Kein Browser-/Screenreader-/Native-Konformitätsnachweis.

## APG auf einen Blick – vertieft geprüft

**20 der 25 zuvor offenen Felder geklärt; X01/X03/X04/X06/X08 bleiben offen.** Verteilung D6/R2/A3/N10/U5. APG liefert konkrete referenzierbare Bedien-/Fokusmuster, Teile eines ausgewählten Beispiels, Rollenverweise und Alert-Guidance. JS-Beispielcode ist ein konkreter Adapteransatz für einen späteren Behaviorvertrag, kein generisches APG-Automatenformat.

**APG ist informativ und besitzt ausdrücklich kein eigenes Konformitätsmodell.** Die vorhandenen HTML-/CSS-/JS-Linter und Beispielregressionstests prüfen andere Artefakte als ein neutrales A11y-Contractschema. Illustrative CSS-Beispielwerte sind kein allgemeiner APG-Design-/Layoutstandard. Abruf 24. Oktober 2026, Referenzbeispiel-/Werkzeug-Snapshot `0f765e4dc33e966026114ac12a8380db1de3b787`; keine Praxis- oder AT-Prüfung. Produktionsnutzung verlangt zusätzliche konkrete Interoperabilitätsnachweise.

## CSS Layout auf einen Blick – vertieft geprüft

**Neue begrenzte Ergänzung:** Neun fachfremde Zellen sind A/C526–C534 ausschließlich durch [jeweils eigene tatsächliche Zusatzbindungen](experiments/2026-10-25/css-complement-runtime/REPORT.md). CSS selbst definiert weiterhin keine öffentlichen Komponentenpayloads, UX-Maschine oder zugängliche Semantik. Native Originalfähigkeit und zusätzliche gemeinsame Ausführung bleiben getrennt.


**Erstrunde: 9 von 24 geklärt. Nach Gesamtprüfung: 10 von 24; 14 konkrete Teilfragen bleiben U.** Aktuelle Verteilung D5/R2/A1/N4/U14. G02 wird gemäß festgelegtem Sprachkriterium als D eingeordnet: keine JS-Funktionen für deklarative CSS-Semantik erforderlich. Das ist kein Nachweis neutraler/native Rendererbindung; der Bericht hatte diese Grenze vorsichtiger als A formuliert.

Anchor Positioning definiert Anker-/Ziel-/Seiten-/Abstandsauflösung, Overflow definiert Scrollport und Overflowwerte. Dimensionen kommen über Values, maximale Höhe über ausdrücklich referenziertes Sizing (R). Mehrfachankernamen sind legal und benötigen für stabile Instanzen zusätzliches Mapping (A). Kein Komponenteninstanziierungs-, Versionsresolver- oder Vier-Domänen-Konfliktmodell im begrenzten Kern.

Basis: Anchor **WD 27.03.2026**, Overflow **WD 07.10.2025**, Syntax **CRD 01.10.2026**, Values 3 **CRD 22.03.2024**, Sizing **WD 04.09.2026**. Neuere veränderliche Editors-Texte separat; eine angebliche datierte Anchor-WD-Adresse vom 06.09.2026 lieferte 404 und wird nicht als veröffentlichte Basis ausgegeben. Keine Browserlayout-/Validatorprobe oder Unterstützungsgarantie.

**Folgeprüfung V03:** D/C412 für zusätzlich geprüftes Media Queries 5. Nach V03 zunächst 14 U; nach dem begrenzten X01-Webprofil aktuell 13 U statt 15 aus der Erstrunde. Der Umfang wird ausdrücklich erweitert; keine getestete Browser-/native Themeunterstützung.

## Grundlagen

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G01 Maschinenlesbare Beschreibung | [D/C01](CLAIMS.md#c01) | [D/C130](CLAIMS.md#c130) | [D/C104](CLAIMS.md#c104) | [D/C156](CLAIMS.md#c156) | [D/C14](CLAIMS.md#c14) | [D/C182](CLAIMS.md#c182) | [D/C22](CLAIMS.md#c22) | [D/C70](CLAIMS.md#c70) |
| G02 Sprachneutrale fachliche Semantik | [A/C03](CLAIMS.md#c03) | [D/C131](CLAIMS.md#c131) | [D/C105](CLAIMS.md#c105) | [D/C157](CLAIMS.md#c157) | [D/C48](CLAIMS.md#c48) | [D/C183](CLAIMS.md#c183) | [D/C22](CLAIMS.md#c22) | [A/C24](CLAIMS.md#c24) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G01 Maschinenlesbare Beschreibung | [D/C85](CLAIMS.md#c85) | [D/C208](CLAIMS.md#c208) | [D/C234](CLAIMS.md#c234) | [D/C260](CLAIMS.md#c260) | [D/C286](CLAIMS.md#c286) | [D/C312](CLAIMS.md#c312) | [N/C338](CLAIMS.md#c338) | [D/C364](CLAIMS.md#c364) |
| G02 Sprachneutrale fachliche Semantik | [A/C25](CLAIMS.md#c25) | [A/C209](CLAIMS.md#c209) | [A/C235](CLAIMS.md#c235) | [D/C261](CLAIMS.md#c261) | [A/C287](CLAIMS.md#c287) | [D/C313](CLAIMS.md#c313) | [D/C339](CLAIMS.md#c339) | [D/C365](CLAIMS.md#c365) |

## Interface

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I01 Öffentliche Eigenschaften mit Typangaben | [D/C01](CLAIMS.md#c01) | [D/C132](CLAIMS.md#c132) | [N/C106](CLAIMS.md#c106) | [N/C158](CLAIMS.md#c158) | [N/C49](CLAIMS.md#c49) | [D/C184](CLAIMS.md#c184) | [N/C59](CLAIMS.md#c59) | [D/C71](CLAIMS.md#c71) |
| I02 Öffentliche Ereignisse mit Payload | [A/C421](CLAIMS.md#c421) | [N/C133](CLAIMS.md#c133) | [N/C107](CLAIMS.md#c107) | [N/C159](CLAIMS.md#c159) | [N/C49](CLAIMS.md#c49) | [D/C185](CLAIMS.md#c185) | [A/C425](CLAIMS.md#c425) | [D/C72](CLAIMS.md#c72) |
| I03 Benannte Komponentenbestandteile | [D/C02](CLAIMS.md#c02) | [N/C134](CLAIMS.md#c134) | [N/C108](CLAIMS.md#c108) | [D/C160](CLAIMS.md#c160) | [N/C49](CLAIMS.md#c49) | [D/C186](CLAIMS.md#c186) | [N/C59](CLAIMS.md#c59) | [N/C73](CLAIMS.md#c73) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I01 Öffentliche Eigenschaften mit Typangaben | [D/C86](CLAIMS.md#c86) | [D/C210](CLAIMS.md#c210) | [D/C236](CLAIMS.md#c236) | [D/C262](CLAIMS.md#c262) | [D/C288](CLAIMS.md#c288) | [D/C314](CLAIMS.md#c314) | [R/C340](CLAIMS.md#c340) | [A/C526](CLAIMS.md#c526) |
| I02 Öffentliche Ereignisse mit Payload | [D/C86](CLAIMS.md#c86) | [D/C211](CLAIMS.md#c211) | [N/C237](CLAIMS.md#c237) | [N/C263](CLAIMS.md#c263) | [N/C289](CLAIMS.md#c289) | [N/C315](CLAIMS.md#c315) | [N/C341](CLAIMS.md#c341) | [A/C527](CLAIMS.md#c527) |
| I03 Benannte Komponentenbestandteile | [D/C87](CLAIMS.md#c87) | [D/C212](CLAIMS.md#c212) | [D/C238](CLAIMS.md#c238) | [D/C264](CLAIMS.md#c264) | [D/C290](CLAIMS.md#c290) | [A/C493](CLAIMS.md#c493) | [D/C342](CLAIMS.md#c342) | [A/C492](CLAIMS.md#c492) |

## Visual

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 Typisierte Designwerte | [R/C38](CLAIMS.md#c38) | [N/C135](CLAIMS.md#c135) | [D/C109](CLAIMS.md#c109) | [D/C161](CLAIMS.md#c161) | [D/C14](CLAIMS.md#c14) | [D/C187](CLAIMS.md#c187) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V02 Visuelle Zustandsvarianten | [N/C39](CLAIMS.md#c39) | [N/C136](CLAIMS.md#c136) | [D/C110](CLAIMS.md#c110) | [D/C162](CLAIMS.md#c162) | [D/C50](CLAIMS.md#c50) | [D/C188](CLAIMS.md#c188) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V03 Themes und Dark Mode | [N/C39](CLAIMS.md#c39) | [N/C137](CLAIMS.md#c137) | [N/C111](CLAIMS.md#c111) | [D/C163](CLAIMS.md#c163) | [D/C15](CLAIMS.md#c15) | [N/C189](CLAIMS.md#c189) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V04 Formale relative Geometrie | [N/C40](CLAIMS.md#c40) | [N/C138](CLAIMS.md#c138) | [N/C112](CLAIMS.md#c112) | [N/C164](CLAIMS.md#c164) | [N/C51](CLAIMS.md#c51) | [A/C540](CLAIMS.md#c540) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V05 Formale Flächenbegrenzung | [N/C40](CLAIMS.md#c40) | [N/C139](CLAIMS.md#c139) | [N/C113](CLAIMS.md#c113) | [N/C165](CLAIMS.md#c165) | [N/C51](CLAIMS.md#c51) | [A/C398](CLAIMS.md#c398) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |
| V06 Overflow und Scrollen | [N/C40](CLAIMS.md#c40) | [N/C140](CLAIMS.md#c140) | [N/C114](CLAIMS.md#c114) | [N/C166](CLAIMS.md#c166) | [N/C51](CLAIMS.md#c51) | [A/C541](CLAIMS.md#c541) | [N/C61](CLAIMS.md#c61) | [N/C74](CLAIMS.md#c74) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 Typisierte Designwerte | [D/C88](CLAIMS.md#c88) | [R/C213](CLAIMS.md#c213) | [D/C239](CLAIMS.md#c239) | [D/C265](CLAIMS.md#c265) | [D/C432](CLAIMS.md#c432) | [N/C317](CLAIMS.md#c317) | [N/C343](CLAIMS.md#c343) | [R/C369](CLAIMS.md#c369) |
| V02 Visuelle Zustandsvarianten | [R/C89](CLAIMS.md#c89) | [R/C214](CLAIMS.md#c214) | [D/C240](CLAIMS.md#c240) | [D/C266](CLAIMS.md#c266) | [A/C292](CLAIMS.md#c292) | [R/C318](CLAIMS.md#c318) | [N/C344](CLAIMS.md#c344) | [N/C370](CLAIMS.md#c370) |
| V03 Themes und Dark Mode | [N/C90](CLAIMS.md#c90) | [N/C215](CLAIMS.md#c215) | [D/C241](CLAIMS.md#c241) | [D/C267](CLAIMS.md#c267) | [D/C433](CLAIMS.md#c433) | [N/C319](CLAIMS.md#c319) | [N/C345](CLAIMS.md#c345) | [D/C412](CLAIMS.md#c412) |
| V04 Formale relative Geometrie | [D/C91](CLAIMS.md#c91) | [R/C216](CLAIMS.md#c216) | [R/C242](CLAIMS.md#c242) | [A/C542](CLAIMS.md#c542) | [R/C525](CLAIMS.md#c525) | [N/C320](CLAIMS.md#c320) | [N/C346](CLAIMS.md#c346) | [D/C372](CLAIMS.md#c372) |
| V05 Formale Flächenbegrenzung | [D/C92](CLAIMS.md#c92) | [R/C217](CLAIMS.md#c217) | [D/C243](CLAIMS.md#c243) | [D/C269](CLAIMS.md#c269) | [A/C436](CLAIMS.md#c436) | [N/C321](CLAIMS.md#c321) | [N/C347](CLAIMS.md#c347) | [R/C373](CLAIMS.md#c373) |
| V06 Overflow und Scrollen | [D/C93](CLAIMS.md#c93) | [R/C218](CLAIMS.md#c218) | [D/C244](CLAIMS.md#c244) | [A/C543](CLAIMS.md#c543) | [A/C498](CLAIMS.md#c498) | [A/C535](CLAIMS.md#c535) | [N/C348](CLAIMS.md#c348) | [D/C374](CLAIMS.md#c374) |

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
| B01 Zustände und Ereignisübergänge | [D/C94](CLAIMS.md#c94) | [R/C219](CLAIMS.md#c219) | [N/C245](CLAIMS.md#c245) | [N/C271](CLAIMS.md#c271) | [N/C297](CLAIMS.md#c297) | [N/C323](CLAIMS.md#c323) | [A/C349](CLAIMS.md#c349) | [A/C528](CLAIMS.md#c528) |
| B02 Guards und Aktionen | [D/C94](CLAIMS.md#c94) | [R/C220](CLAIMS.md#c220) | [N/C246](CLAIMS.md#c246) | [N/C272](CLAIMS.md#c272) | [N/C298](CLAIMS.md#c298) | [N/C324](CLAIMS.md#c324) | [A/C350](CLAIMS.md#c350) | [A/C529](CLAIMS.md#c529) |
| B03 Ereignis- und Kontextdaten | [D/C94](CLAIMS.md#c94) | [R/C221](CLAIMS.md#c221) | [N/C247](CLAIMS.md#c247) | [N/C273](CLAIMS.md#c273) | [N/C299](CLAIMS.md#c299) | [N/C325](CLAIMS.md#c325) | [A/C351](CLAIMS.md#c351) | [A/C530](CLAIMS.md#c530) |
| B04 Bindung von Eingaben an UX-Aktionen | [D/C95](CLAIMS.md#c95) | [D/C222](CLAIMS.md#c222) | [N/C248](CLAIMS.md#c248) | [N/C274](CLAIMS.md#c274) | [A/C300](CLAIMS.md#c300) | [A/C326](CLAIMS.md#c326) | [D/C352](CLAIMS.md#c352) | [A/C531](CLAIMS.md#c531) |

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
| A01 Rollen, Namen und Beziehungen | [D/C96](CLAIMS.md#c96) | [D/C223](CLAIMS.md#c223) | [N/C249](CLAIMS.md#c249) | [R/C275](CLAIMS.md#c275) | [R/C494](CLAIMS.md#c494) | [D/C327](CLAIMS.md#c327) | [R/C353](CLAIMS.md#c353) | [A/C532](CLAIMS.md#c532) |
| A02 Fokus- und Tastaturanforderungen | [D/C96](CLAIMS.md#c96) | [D/C224](CLAIMS.md#c224) | [N/C250](CLAIMS.md#c250) | [D/C276](CLAIMS.md#c276) | [R/C439](CLAIMS.md#c439) | [D/C328](CLAIMS.md#c328) | [D/C354](CLAIMS.md#c354) | [A/C533](CLAIMS.md#c533) |
| A03 Dynamische Rückmeldungen | [D/C97](CLAIMS.md#c97) | [R/C225](CLAIMS.md#c225) | [N/C251](CLAIMS.md#c251) | [R/C277](CLAIMS.md#c277) | [R/C495](CLAIMS.md#c495) | [D/C329](CLAIMS.md#c329) | [D/C355](CLAIMS.md#c355) | [A/C534](CLAIMS.md#c534) |

## Integration

### Kandidatenblock 1

| Anforderung | CEM | OpenUI | Google DESIGN.md | AgentsORG | DTCG | UXSpec | SCXML | XState |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X01 Vier unabhängig beschreibbare Domänen | [A/C447](CLAIMS.md#c447) | [A/C524](CLAIMS.md#c524) | [A/C523](CLAIMS.md#c523) | [A/C508](CLAIMS.md#c508) | [A/C454](CLAIMS.md#c454) | [A/C520](CLAIMS.md#c520) | [A/C447](CLAIMS.md#c447) | [A/C501](CLAIMS.md#c501) |
| X02 Stabile Elementidentität | [N/C44](CLAIMS.md#c44) | [N/C149](CLAIMS.md#c149) | [N/C123](CLAIMS.md#c123) | [N/C175](CLAIMS.md#c175) | [N/C55](CLAIMS.md#c55) | [D/C201](CLAIMS.md#c201) | [N/C65](CLAIMS.md#c65) | [N/C80](CLAIMS.md#c80) |
| X03 Domänenübergreifende Referenzen | [N/C44](CLAIMS.md#c44) | [N/C150](CLAIMS.md#c150) | [N/C124](CLAIMS.md#c124) | [N/C176](CLAIMS.md#c176) | [N/C55](CLAIMS.md#c55) | [A/C509](CLAIMS.md#c509) | [N/C65](CLAIMS.md#c65) | [N/C80](CLAIMS.md#c80) |
| X04 Wiederverwendbare Komponenteninstanzen | [N/C44](CLAIMS.md#c44) | [N/C151](CLAIMS.md#c151) | [N/C125](CLAIMS.md#c125) | [N/C177](CLAIMS.md#c177) | [N/C55](CLAIMS.md#c55) | [D/C430](CLAIMS.md#c430) | [A/C408](CLAIMS.md#c408) | [A/C409](CLAIMS.md#c409) |
| X05 Externe versionierte Abhängigkeiten | [N/C45](CLAIMS.md#c45) | [N/C152](CLAIMS.md#c152) | [N/C126](CLAIMS.md#c126) | [N/C178](CLAIMS.md#c178) | [N/C56](CLAIMS.md#c56) | [N/C204](CLAIMS.md#c204) | [N/C67](CLAIMS.md#c67) | [N/C82](CLAIMS.md#c82) |
| X06 Eigene Schemavalidatoren erhalten | [D/C419](CLAIMS.md#c419) | [U/C484](CLAIMS.md#c484) | [U/C483](CLAIMS.md#c483) | [D/C179](CLAIMS.md#c179) | [D/C57](CLAIMS.md#c57) | [D/C429](CLAIMS.md#c429) | [D/C424](CLAIMS.md#c424) | [N/C464](CLAIMS.md#c464) |
| X07 Referenz- und Konfliktprüfung des Pakets | [N/C47](CLAIMS.md#c47) | [N/C154](CLAIMS.md#c154) | [N/C128](CLAIMS.md#c128) | [N/C180](CLAIMS.md#c180) | [N/C58](CLAIMS.md#c58) | [N/C206](CLAIMS.md#c206) | [N/C69](CLAIMS.md#c69) | [N/C84](CLAIMS.md#c84) |
| X08 Eindeutige führende Quelle | [N/C47](CLAIMS.md#c47) | [N/C155](CLAIMS.md#c155) | [N/C129](CLAIMS.md#c129) | [A/C507](CLAIMS.md#c507) | [N/C58](CLAIMS.md#c58) | [N/C207](CLAIMS.md#c207) | [N/C69](CLAIMS.md#c69) | [N/C84](CLAIMS.md#c84) |

### Kandidatenblock 2

| Anforderung | Zag | Ark UI | Panda CSS | uSpec | OpenPencil | WAI-ARIA | APG | CSS Layout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X01 Vier unabhängig beschreibbare Domänen | [A/C518](CLAIMS.md#c518) | [A/C519](CLAIMS.md#c519) | [A/C521](CLAIMS.md#c521) | [A/C538](CLAIMS.md#c538) | [A/C539](CLAIMS.md#c539) | [A/C447](CLAIMS.md#c447) | [A/C522](CLAIMS.md#c522) | [A/C447](CLAIMS.md#c447) |
| X02 Stabile Elementidentität | [D/C87](CLAIMS.md#c87) | [D/C227](CLAIMS.md#c227) | [N/C253](CLAIMS.md#c253) | [D/C279](CLAIMS.md#c279) | [D/C305](CLAIMS.md#c305) | [R/C331](CLAIMS.md#c331) | [D/C357](CLAIMS.md#c357) | [A/C383](CLAIMS.md#c383) |
| X03 Domänenübergreifende Referenzen | [A/C510](CLAIMS.md#c510) | [A/C511](CLAIMS.md#c511) | [N/C254](CLAIMS.md#c254) | [A/C536](CLAIMS.md#c536) | [A/C505](CLAIMS.md#c505) | [A/C462](CLAIMS.md#c462) | [A/C513](CLAIMS.md#c513) | [A/C485](CLAIMS.md#c485) |
| X04 Wiederverwendbare Komponenteninstanzen | [A/C410](CLAIMS.md#c410) | [D/C229](CLAIMS.md#c229) | [A/C255](CLAIMS.md#c255) | [D/C281](CLAIMS.md#c281) | [A/C307](CLAIMS.md#c307) | [N/C333](CLAIMS.md#c333) | [A/C514](CLAIMS.md#c514) | [N/C385](CLAIMS.md#c385) |
| X05 Externe versionierte Abhängigkeiten | [N/C101](CLAIMS.md#c101) | [N/C230](CLAIMS.md#c230) | [A/C256](CLAIMS.md#c256) | [N/C282](CLAIMS.md#c282) | [A/C411](CLAIMS.md#c411) | [N/C334](CLAIMS.md#c334) | [N/C360](CLAIMS.md#c360) | [N/C386](CLAIMS.md#c386) |
| X06 Eigene Schemavalidatoren erhalten | [N/C481](CLAIMS.md#c481) | [D/C474](CLAIMS.md#c474) | [A/C477](CLAIMS.md#c477) | [D/C283](CLAIMS.md#c283) | [D/C309](CLAIMS.md#c309) | [N/C471](CLAIMS.md#c471) | [N/C482](CLAIMS.md#c482) | [A/C479](CLAIMS.md#c479) |
| X07 Referenz- und Konfliktprüfung des Pakets | [N/C103](CLAIMS.md#c103) | [N/C232](CLAIMS.md#c232) | [N/C258](CLAIMS.md#c258) | [N/C284](CLAIMS.md#c284) | [N/C310](CLAIMS.md#c310) | [N/C336](CLAIMS.md#c336) | [N/C362](CLAIMS.md#c362) | [N/C388](CLAIMS.md#c388) |
| X08 Eindeutige führende Quelle | [N/C103](CLAIMS.md#c103) | [N/C233](CLAIMS.md#c233) | [A/C506](CLAIMS.md#c506) | [A/C537](CLAIMS.md#c537) | [A/C515](CLAIMS.md#c515) | [A/C504](CLAIMS.md#c504) | [A/C517](CLAIMS.md#c517) | [A/C459](CLAIMS.md#c459) |

## Einordnung der ersten Befunde

R ist keine pauschale Komplettbewertung: Ein dokumentierter Tokenalias erfüllt nur einen Wertbezug. Er deckt die gesamte Anforderung einer domänenübergreifenden Referenz oder einer Komponenteninstanz nicht ab. C36 beschreibt diesen Teilbeitrag. Bei CEM V01 bezeichnet R dagegen ausdrücklich die im Format benannte CSS-Wertsyntax (C38), keine Komponentenreferenz. Referenzmechanismen werden daher nicht überbewertet.

- **OpenUI:** Einfache Props sind konkret beschrieben. Die alte Chatbehauptung einer umfassenden Event-/Payloadbeschreibung ist damit nicht bestätigt (C05). State/Lifecycle ist in draft-01 zukünftige Arbeit (C06).
- **Google DESIGN.md:** Strukturierte Werte und benannte Stylevarianten sind vorhanden. Das ist noch keine standardisierte Geometriesprache für Beziehungen zwischen Elementen (C07–C10).
- **UXSpec:** Verhalten ohne `$visual` ist auf der gelesenen Schemaebene nicht ausgeschlossen; die frühere Vermutung einer zwingenden Visualpflicht ist zu korrigieren (C17). Compilerverhalten und Domänenbindung sind weiterhin offen. Schemafelder wie `container: object` beweisen keine vollständig typisierte Layoutsemantik.
- **Komposition:** UXSpec-Elementreferenzen, Ark-Komposition und OpenPencil-ID-Bindungen sind reale unterschiedliche Mechanismen (C20/C27/C30). Keiner dieser Befunde beweist allein ein gemeinsames versioniertes Komponentenpaket über alle vier Domänen.
- **Accessibility:** ARIA liefert Semantik und APG Interaktionswissen. Die konkreten Produktregeln und eine ausführbare Paketprüfung müssen gesondert abgebildet werden (C31/C32).

## Warum viele Zellen offen bleiben

Diese Lieferung priorisiert belastbare Teilbefunde gegenüber flächendeckenden Vermutungen. Besonders X03/X05/X06/X07/X08 verlangen Prüfung der Verbindungen und konkreter Werkzeuge. Eine Übersichtsseite, ein Feld namens version oder ein vorhandenes JSON Schema beweisen diese Anforderungen nicht. Die inzwischen vertieften Kandidaten besitzen oben konkrete Quellenstände und verbleibende Folgefragen; weitere Prüfungen richten sich nach TASKS.md. Bei keinem Kandidaten wurde das gesamte Contract-Paket praktisch validiert.

Die vorgeschlagene Eigenleistung ist daher **noch keine implementierte Architektur**: Möglicherweise werden Identitätsabbildung, externe Versionsauflösung, Domänenbindungen und Konfliktprüfung benötigt. Ob vorhandene Mechanismen ausreichen, bleibt anhand der folgenden Versuche zu klären: [RESEARCH-PLAN.md](RESEARCH-PLAN.md).

## Aktuelle E3-Fortschreibung

Die obigen Kandidatenporträts enthalten historische Erstrundenbeschreibungen ohne Versuche. Maßgeblich sind jetzt zusätzlich [49 gespeicherte Proben](experiments/2026-10-24/REPORT.md): drei Originalschema-Pfade, Gegenprüfungen, Original-Webmapper, TypeScript-Payloadauflösung, statische CEM-/SCXML-Bindung sowie Nu-Hostchecker. CEM und SCXML I02 sind A; andere betroffene Abdeckungswerte bleiben erhalten. Keine UI-/AT- oder vollständige Vier-Domänen-Prüfung.

**Ausgeführte Visualvalidatoren:** [31 weitere Fälle](experiments/2026-10-24/openpencil-validation/REPORT.md) trennen Datenhülle, Referenzintegrität und sichere CSS-Ausgabeform. Keine zusätzliche U-Neubewertung.

**Weitere Layoutfolgeprüfung:** OpenPencil V05 A/C436; V04/V06 bleiben mit konkreteren Originalpfaden U/C437/C438. [Bericht](experiments/2026-10-24/openpencil-layout/REPORT.md). Aktuell 62 U.

**25.10.2026 – Accessibility-Folgeprüfung:** OpenPencil A02 R/C439 für den konkreten Switch→Reka→APG-Webpfad. A01/A03 bleiben U mit genaueren Grenzen; keine pauschale Bibliothekskonformität. [Bericht](experiments/2026-10-25/openpencil-a11y/REPORT.md). Aktuell 61 U.

**Vier-Domänen-Webreferenzfall:** X01 bei CEM, SCXML, CSS Layout und WAI-ARIA ist nun A/C447 für getrennte Originalsprachen mit expliziter zusätzlicher statischer Bindung. Vier Originalkontrollen, 13 Bindungsbedingungen und vier Layoutmessfälle ausgeführt. Keine vollständige interaktive oder native Integration. [Abnahmebericht](experiments/2026-10-25/four-domain/REPORT.md).

[Verbindlicher aktueller Nachweisstand und Abnahme dieses Pakets](CURRENT-STATUS.md).
