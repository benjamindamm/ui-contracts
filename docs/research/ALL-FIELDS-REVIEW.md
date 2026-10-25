# Gesamtprüfung der 72 zuvor offenen Felder

**Aktuelle Fortschreibung nach diesem dokumentarischen Stand:** [49 E3-Proben](experiments/2026-10-24/REPORT.md) sind inzwischen ausgeführt. CEM I02 ist nun A/C421; aktuell 65 U (41 Integration, 24 weitere). Frühere Aussagen „keine Ausführung“ und damalige Zählungen unten dokumentieren den Entstehungsstand. Keine vollständige UI-/AT-/Integrationsprüfung.


Stand: 24. Oktober 2026. **72/72 Zellen dokumentarisch erneut ausgewertet; fünf begründet neu eingeordnet; 67 U-Nachweise bleiben technisch offen.** Dazu sind beide bestätigten Detailvergleiche ausgearbeitet. Das ist keine Meldung „alle Nachweise gelöst“. Keine Implementierung, keine ausgeführten Originalvalidatoren, keine Browser-/AT-Versuche, kein Commit oder Push.

## Was tatsächlich geprüft wurde

Für jede Ausgangszelle wurden Kriterium, bestehender Claim, Quellenrolle und die zum Schließen erforderliche Evidenz abgeglichen. Neue Primärlesungen sind in [S63](SOURCES.md#s63), [S64](SOURCES.md#s64) und [S65](SOURCES.md#s65) abgegrenzt. Die übrigen Einträge werten die bereits gespeicherten Originalbefunde erneut aus; sie behaupten keinen frischen Vollabruf aller Projekte. Das maschinenlesbare Protokoll steht unter followup_reviews in [study.json](study.json).

U bleibt gemäß Methode auch bei sachfremden Zellen bestehen. Nach gründlicherer Lektüre kann ein externer Beleg weiterhin fehlen. Ein geklärter Adapterbedarf ist A; eine bloß vorstellbare Adapteridee genügt nicht. X01/X03/X08 werden nicht durch eine selbst erfundene Paketstruktur als original unterstützt ausgegeben.

## Fünf Neubewertungen

| Kandidat / Feld | Ergebnis | Begründung und Grenze |
| --- | --- | --- |
| SCXML X04 | U→A | Normierte eigene Dienstinstanz und Parameter; UI-Bindung zusätzlich. [C408](CLAIMS.md#c408) |
| XState X04 | U→A | Eigene Actorinstanz, Input und Lifecycle; UI-Bindung zusätzlich. [C409](CLAIMS.md#c409) |
| Zag X04 | U→A | Referenzierte Maschinen und konkrete Instanzkomposition; neutraler Childvertrag zusätzlich. [C410](CLAIMS.md#c410) |
| OpenPencil X05 | U→A | Neu geprüfter Libraryresolver mit expliziter Revision und Behaviourinhalt; externe neutrale Fachmodellbindung zusätzlich. [C411](CLAIMS.md#c411) |
| CSS Layout V03 | U→D | Explizite Scopeergänzung um Media Queries 5; bedingte Light/Dark-Auswahl. [C412](CLAIMS.md#c412) |

Die drei X04-Neubewertungen korrigieren eine zu strenge Anforderung an den begrenzten Beitrag: Die vollständige Vier-Domänen-Komposition bleibt ein Paketnachweis, während Definition/Verwendung und eigene Instanz bereits als Mechanismus belegt sind. Dies ist keine nachträgliche Runtimebestätigung.

## Gemeinsame Abhängigkeiten statt 67 unabhängiger Implementierungsaufgaben

| Kürzel | Noch benötigter Nachweis / Entscheidung |
| --- | --- |
| P | Paket-/Domänenprofil: vier Originalartefakte, adressierbare Zielarten, Instanz und semantische Bindungen |
| O | Führende Quelle je Information, Vorrang bei Widerspruch und nachvollziehbare Änderung |
| T | Identifiziertes Originalartefakt plus tatsächliches Werkzeug/Regelabdeckung; Typchecker und Beispieltests getrennt |
| Q | Öffentliche Eventsignatur und explizite Payloadprojektion |
| L | Formale relative Geometrie und Scrollsemantik statt Mess-/Clippingdaten |
| M | Separater fachlich zuständiger Beitrag, weil untersuchter Kandidatenkern diese Rolle nicht nachweislich erfüllt |
| A | Konkretes Host-/Patternprofil mit Rollen/Namen, Fokus/Tasten und Meldungen |
| K | Childdefinition, Instanzkontext, Parameter, Ereignisse und UI-Anatomie |
| V | Reproduzierbare Revision und Integrität bis Verwendung/Export |

Diese Gruppen sind eine Arbeitsordnung, keine neuen Standards oder automatischen Abdeckungswerte. Die genaue Zellenzahl je Gruppe lässt sich aus study.json ableiten; manche fachlichen Probleme überlappen.

## Jede Ausgangszelle mit Ergebnis

„Alt“ bezeichnet den Claim vor diesem Paket. Die Spalte Ergebnis ist der aktuelle Matrixwert. Jede Zeile ist eine abgeschlossene dokumentarische Auswertung; U markiert den weiterhin fehlenden technischen Nachweis.

### CEM

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| I02 | [C37](CLAIMS.md#c37) → [C413](CLAIMS.md#c413) | U | Type.references adressiert Typdeklarationen; der fehlende Schritt ist die öffentliche Eventobjekt→Payload-Projektion. Das offizielle Event-Beispiel schließt diese Lücke nicht. | Q |
| X01 | [C43](CLAIMS.md#c43) | U | Eigenständiges Manifest verlangt keine Visual-/Behavior-/A11y-Daten; gemeinsame fachliche Ziele sind nicht Bestandteil dieses Nachweises. | P |

### OpenUI

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C148](CLAIMS.md#c148) | U | Der Interfaceentwurf lässt sich separat führen; seine abweichenden Originaldefinitionen lösen die Paketbindung nicht. | P |
| X06 | [C402](CLAIMS.md#c402) | U | TS-Interface und Feldkatalog weichen ab; der Tabellenrenderer prüft keine Contractdatei. Ein selbst korrigiertes Schema wäre eine neue Ergänzung. | T |

### Google DESIGN.md

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C122](CLAIMS.md#c122) | U | Eigenständige Visualdatei ist möglich; Prosa oder offene Maps machen andere Originaldomänen nicht unabhängig prüfbar. | P |
| X06 | [C403](CLAIMS.md#c403) | U | Der Textwrapper prüft content; lint führt Parser, Modell und Regeln aus. Warnungen/Recovery und gültige Fachmodellstruktur sind verschiedene Ergebnisse. | T |

### AgentsORG

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C174](CLAIMS.md#c174) | U | Der kanonische Visualvertrag ist getrennt möglich; seine Sync-/Exportregeln legen keine vier unabhängigen Master fest. | P |
| X08 | [C181](CLAIMS.md#c181) | U | .design-Kanonizität, Tokenvorrang und Sync-Richtung klären lokale Ownership. Über unabhängige API/Behavior/A11y-Quellen entscheiden sie noch nicht. | O |

### DTCG

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C54](CLAIMS.md#c54) | U | Resolvervarianten und Tokenquellen bleiben Visualwerte. Ein fremdes Interface-/Behavior-/A11y-Artefakt wird nicht durch dessen Tokenreferenz zum DTCG-Dokument. | P |

### UXSpec

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| V04 | [C397](CLAIMS.md#c397) | U | layer=relative plus absolut gestreckte Kindwrapper liefert lokale Überlagerung, keine typisierte Input-Zielrelation mit Richtung/Abstand. Eine neue freie Property wäre keine Originalsemantik. | L |
| V06 | [C399](CLAIMS.md#c399) | U | maxHeight begrenzt Geometrie; der geprüfte Mapper/Container reicht keine formale overflow-Achse durch. Zusätzliches Host-CSS ist als Ergänzung zu kennzeichnen. | L |
| X01 | [C200](CLAIMS.md#c200) | U | Behavior ohne $visual ist schemafähig; eine reine unabhängige Visualdatei ohne Pflicht-$machine ist kein eigenes UXSpec-Root. | P |
| X03 | [C202](CLAIMS.md#c202) | U | Aliasimporte lösen eigene Elemente/Tokens/Maschinen auf. Ein Original-DTCG- oder CEM-Knoten ist ohne Übersetzungsregel kein solcher UXSpec-Knoten. | P |

### SCXML

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| I02 | [C60](CLAIMS.md#c60) → [C414](CLAIMS.md#c414) | U | Benannte param-Werte und _event.data sind Kommunikation. Ein öffentlicher Signaturkatalog unabhängig von allen Sendepunkten wird daraus nicht vollständig gewonnen. | Q |
| X01 | [C64](CLAIMS.md#c64) | U | Das Behavior-Dokument benötigt keine UI-Visualdefinition. Die Brücke zu drei unabhängigen Originalformaten bleibt zusätzlich. | P |
| X04 | [C66](CLAIMS.md#c66) → [C408](CLAIMS.md#c408) | A | Eigene Dienstinstanz, Daten und Parameter sind normiert. UI-Teile und Hostbinding fehlen weiterhin; das begründet A statt einer Forderung nach vollständiger Paketkomposition. | K |

### XState

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C79](CLAIMS.md#c79) | U | Eigenständige Actorlogik benötigt keine Visual-/A11y-Dateien. Diese Freiheit belegt noch keine gemeinsame Format-/Validatorgrenze. | P |
| X04 | [C81](CLAIMS.md#c81) → [C409](CLAIMS.md#c409) | A | Actorlogik und Verwendung mit eigenem Input/Lebenszyklus sind getrennt. Die zusätzliche Zuordnung Actor→UI-Unterkomponente ist ein Adapterbedarf. | K |
| X06 | [C405](CLAIMS.md#c405) | U | schemas:unknown und toJSON/restore sind kein Originalartefaktvalidator. Wiederherstellung setzt vorhandene Logik voraus; Snapshot und Quellmodell getrennt behandeln. | T |

### Zag

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C98](CLAIMS.md#c98) | U | Styles können extern sein; die gelieferten Maschinen/connect-Pfade koppeln Fokus, DOM, ARIA und Verhalten. | P |
| X03 | [C99](CLAIMS.md#c99) | U | Part-IDs, data-state und CSS-Selektoren adressieren DOM-/Styleziele. Art und Version externer Fachmodellknoten werden dadurch nicht geprüft. | P |
| X04 | [C100](CLAIMS.md#c100) → [C410](CLAIMS.md#c410) | A | Mehrere konkrete Maschineninstanzen mit eigenen Props und bewussten gemeinsamen IDs sind belegt; deklarativer Childvertrag und Fokus-/Scrollzuständigkeit fehlen. | K |
| X06 | [C406](CLAIMS.md#c406) | U | Interne Prüfungen existieren, manche invariant-Fehler sind modusabhängig. Ein unabhängiges neutrales Originalartefakt und sein Validator bleiben unbelegt. | T |

### Ark UI

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C226](CLAIMS.md#c226) | U | Frameworkkomposition trennt Styling; funktionale Geometrie, Fokus, ARIA und Zag-Verhalten bleiben in der ausführbaren Integration gekoppelt. | P |
| X03 | [C228](CLAIMS.md#c228) | U | IDs und Parts binden DOM/ARIA/CSS; sie liefern keinen Resolver für originale neutrale Interface-/Behavior-/A11y-Artefakte. | P |
| X06 | [C407](CLAIMS.md#c407) | U | API-JSON beschreibt Typen/Defaults als Metadaten. Ohne zusätzliche Typ-/Referenzsemantik entsteht daraus kein originaler neutraler Runtimevalidator. | T |

### Panda CSS

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C252](CLAIMS.md#c252) | U | Visualkonfiguration ist getrennt führbar; Export und CSS-Ausgabe beweisen keine vier unveränderten Fachartefakte. | P |
| X06 | [C404](CLAIMS.md#c404) | U | Der Exportreader prüft bewusst flach; Kategorien/Token/Zeilen werden dort nicht vollständig validiert. Build-/Flagprüfungen sind andere Gegenstände. | T |
| X08 | [C259](CLAIMS.md#c259) | U | Configreihenfolge und optionale sources zeigen lokale Priorität/Provenienz. Ein fremder Behavior-/A11y-Konflikt wird dadurch nicht aufgelöst. | O |

### uSpec

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| V04 | [C400](CLAIMS.md#c400) | U | _anchor benennt den Figma-Quellknoten; bbox ist variantenrelative Messgeometrie. Beide bestimmen keinen beweglichen Laufzeitanker für ein Popup. | L |
| V06 | [C401](CLAIMS.md#c401) | U | clipsContent im Basis-/Strukturpfad beschreibt Abschneiden. Daraus folgen weder Scrollachse noch auto/scroll-Entscheidung oder Scrollport. | L |
| X01 | [C278](CLAIMS.md#c278) | U | api/structure/color/voice-Caches sind reale Teilungen, aber andere als Interface/Visual/Behavior/A11y; der Canonicalcontainer ist nicht deren Ersatz. | P |
| X03 | [C280](CLAIMS.md#c280) | U | Evidence-JSON-Pointer und Figma-IDs weisen Provenienz nach. Sie definieren keine fachliche Ereignis-/A11y-Zuordnung zu externen Originalen. | P |
| X08 | [C285](CLAIMS.md#c285) | U | Base sole-writer, read-only Interpretation und JSON→Markdown sind interne Pipelineverantwortung; externe Originalquellen brauchen eigene Änderungsregeln. | O |

### OpenPencil

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| V01 | [C291](CLAIMS.md#c291) | U | Behaviour numbers besitzen Controlbereiche und Defaults. Farben/Dimensionen erfordern ein separat geprüften Visualbeitrag; dessen Editorfähigkeit wird nicht dem Behaviour-Schema zugerechnet. | M |
| V03 | [C293](CLAIMS.md#c293) | U | Behaviour states ordnen Interaction-Properties zu; ein aufgelöster Light/Dark-Modus ist dadurch nicht definiert. Dokumentvariablen und Themes sind ein anderer Untersuchungsgegenstand. | M |
| V04 | [C294](CLAIMS.md#c294) | U | Der Sliderpreview setzt Geometrie bestimmter Teile über Reka; das ist keine allgemeine Popup→Input-Ziel-/Abstandsdefinition im Behaviourmodell. | M |
| V05 | [C295](CLAIMS.md#c295) | U | Slider-/Numberfield-min/max begrenzen Controlwerte. Ohne Visual-/Zeilenmessmodell folgt daraus keine maximale Fläche oder Fünf-Zeilen-Höhe. | M |
| V06 | [C296](CLAIMS.md#c296) | U | Canvas-Wheelweitergabe und Controlpreview sind Hostmechanismen. Ein formaler eigener Scrollcontainer mit Achse und Overflowpolitik ist in diesem Behaviour-Beitrag nicht belegt. | M |
| A01 | [C301](CLAIMS.md#c301) | U | Der gelesene Radiobutton besitzt role=radio und aria-checked; Reka-Wrapper liefern weitere konkrete Webbindungen. Ein vollständiger neutraler Rollen-/Namen-/Beziehungskatalog samt externen Zielen bleibt unbelegt. | A |
| A02 | [C302](CLAIMS.md#c302) | U | Reka/asChild und native Controls sind reale Delegationen. Ein Control-kind ist noch kein versioniertes, separat prüfbares Pattern mit allen Fokus-/Tastenregeln. | A |
| A03 | [C303](CLAIMS.md#c303) | U | Behaviourwerte und onUpdate-Callbacks transportieren Änderungen. Die zusätzliche Zuordnung zu Ergebnis-/Statusmeldung, Live-Region und Zeitpunkt ist nicht im geprüften Behaviour-Schema belegt. | A |
| X01 | [C304](CLAIMS.md#c304) | U | Behaviour ist ein Subartefakt und bindet Scenegraph-Properties/Slots; das ist keine unabhängige Vier-Domänen-Originalformatkette. | P |
| X03 | [C306](CLAIMS.md#c306) | U | Behaviour-Slots und Property-IDs verbinden denselben Scenegraph. Die neue Libraryrevision löst nicht automatisch externe Domänenadressen auf. | P |
| X05 | [C308](CLAIMS.md#c308) → [C411](CLAIMS.md#c411) | A | Neue Bibliothekspfade lösen explizite Revisionen und Assets auf; Behaviourinhalt wird in Snapshot und Hash einbezogen. Neutrale externe Fachmodelle brauchen weiterhin Bindung. | V |
| X08 | [C311](CLAIMS.md#c311) | U | behaviourOwner und Library-readOnly sind lokale Regeln. Versionierung entscheidet nicht, welche fremde Domäne eine überlappende Information führt. | O |

### WAI-ARIA

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| I03 | [C316](CLAIMS.md#c316) | U | Required Context/Owned Elements bestimmen semantische Rollenbeziehungen. Ein strukturierter UI-Anatomiekatalog mit Namen input/overlay/viewport ist eine zusätzliche Produkt-/Interfacebeschreibung. | M |
| V06 | [C322](CLAIMS.md#c322) | U | Orientierung und Fokusregeln benötigen einen tatsächlichen Scrollhost. Sie definieren keinen eigenständigen Clip-/Overflow-/Maximalhöhenvertrag. | M |
| X01 | [C330](CLAIMS.md#c330) | U | Websemantik kann unabhängig als Anforderung dienen; ein neutrales A11y-Dateiartefakt mit Originalschema folgt daraus nicht. | P |
| X03 | [C332](CLAIMS.md#c332) | U | IDREF adressiert reale Hostelemente. Existenz eines DOM-Ziels ist nicht gleich der richtigen fachlichen Instanz oder einem externen Modellknoten. | P |
| X06 | [C335](CLAIMS.md#c335) | U | Normregeln und Hostabbildungen sind vorhanden. Ein neutrales separates A11y-Originalschema/Checkerpaar samt genauem Host-/Versionsprofil ist nicht identifiziert. | T |
| X08 | [C337](CLAIMS.md#c337) | U | Host-/ARIA-Vorrang normiert Semantik im Webhost. Das ist kein Änderungs-/Provenienzmodell zwischen vier Originaldateien. | O |

### APG

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| X01 | [C356](CLAIMS.md#c356) | U | Ein Patternlink ist eine unabhängige Anforderungsquelle, kein schon vorhandenes separates maschinenlesbares Pattern-Contractartefakt. | P |
| X03 | [C358](CLAIMS.md#c358) | U | Pattern-URLs und Beispiel-DOM-IDs liefern Quellen/Hostbezüge. Eine versionsgebundene semantische Zuordnung fremder Originalartefakte fehlt weiterhin. | P |
| X04 | [C359](CLAIMS.md#c359) | U | Combobox-Popupvarianten und Beispielklassen zeigen Zusammenbau; ein neutraler Childvertrag mit eigener Definition, Kontext, Parametern und Versionsresolver ist damit nicht belegt. | K |
| X06 | [C361](CLAIMS.md#c361) | U | HTML/CSS/JS-Linter und Beispielregression sind echte Werkzeuge. Sie prüfen nicht automatisch eine unabhängige originale Pattern-Contractdatei. | T |
| X08 | [C363](CLAIMS.md#c363) | U | Nichtnormativer Guide gegenüber normativem ARIA klärt Quellenrang; Produktprofil und Originaldateien benötigen weitere per-information Regeln. | O |

### CSS Layout

| Feld | Alt → aktuell | Ergebnis | Prüfung / Grenze | Abhängigkeit |
| --- | --- | --- | --- | --- |
| I01 | [C366](CLAIMS.md#c366) | U | CSS-Wertgrammatiken typisieren Styles, keine öffentlichen Komponenten-Inputs. Ein separat führender Interfacevertrag und eine Propertybindung bleiben nötig. | M |
| I02 | [C367](CLAIMS.md#c367) | U | Layoutgrammatiken definieren keine öffentliche Payloadsignatur. Scroll-/Geometrieänderung und Produkt-Auswahlereignis sind getrennte Bedeutungen. | M |
| I03 | [C368](CLAIMS.md#c368) | U | anchor-name benennt eine Boxrolle für Layoutsuche. Es liefert keinen vollständigen fachlichen Teilekatalog oder Slotvertrag. | M |
| V03 | [C371](CLAIMS.md#c371) → [C412](CLAIMS.md#c412) | D | Der Umfang wird explizit um Media Queries 5 erweitert. prefers-color-scheme besitzt bedingte Wertauswahl mit Light/Dark-Semantik; Produktoverride bleibt offen. | M |
| B01 | [C375](CLAIMS.md#c375) | U | Positionierungsfallbacks sind Layoutentscheidungen. Fachliche Zustände, Initialzustand und Eventziele benötigen den getrennten Behaviorvertrag. | M |
| B02 | [C376](CLAIMS.md#c376) | U | Geometrische Bedingungen sind keine UX-Guards oder Produktaktionen. Gleichnamige CSS-Zustände ersetzen keine Aktionssemantik. | M |
| B03 | [C377](CLAIMS.md#c377) | U | Layoutwerte und berechnete Boxen sind kein Kontext-/Ereignisdatenmodell für Suchergebnisse und bestätigte Auswahl. | M |
| B04 | [C378](CLAIMS.md#c378) | U | Ein Scrollport beschreibt keine vollständige Tastatur-/Fokus→Aktionsabbildung. Der Host muss das gewählte Behavior-/Patternprofil binden. | M |
| A01 | [C379](CLAIMS.md#c379) | U | Anchor §9 trennt visuelle Lage ausdrücklich von sinnvoller zugänglicher Beziehung. Die Input→Listbox-/Optionbeziehungen müssen in ARIA/Hostsemantik separat entstehen. | A |
| A02 | [C380](CLAIMS.md#c380) | U | Visuelle Nähe und Scrollbarkeit bestimmen kein zugängliches Comboboxmuster. Popupvariante, Fokus und Tasten brauchen ein eigenes Patternprofil. | A |
| A03 | [C381](CLAIMS.md#c381) | U | Ein Layoutwechsel ist keine definierte zugängliche Statusmeldung. Inhalt, Auslöser und Zeitpunkt bleiben in Behavior/A11y zu binden. | A |
| X01 | [C382](CLAIMS.md#c382) | U | Stylesheet trennt Visualregeln; gemeinsames Elementziel und fachliche Domänenbindung sind zusätzliche Paketinformation. | P |
| X03 | [C384](CLAIMS.md#c384) | U | Anchorlookup adressiert Boxen im CSS-Baum. Korrekte fachliche Instanz und externe Domänenart müssen separat gebunden werden. | P |
| X06 | [C387](CLAIMS.md#c387) | U | Grammatiken und Conformance-Regeln sind belegt. Unterstützung genau der gespeicherten Draftkombination durch einen konkreten Checker wurde nicht nachgewiesen. | T |
| X08 | [C389](CLAIMS.md#c389) | U | Kaskade, Scope und Fallback entscheiden berechnete Styles. Sie ersetzen keine fachliche Ownership oder protokollierte Rückschreibung in Originalmodelle. | O |

## Dokumentarische Detailvergleiche

- [UXSpec gegen SCXML](COMPARE-UXSPEC-SCXML.md): Originalformat, Schema, CLI und App getrennt; enger Vergleichsfall mit Guard/Kontext, Papierablauf und negativen Fällen. Neu: App-Mockereignisse und invoke-/oneOf-Grenzen.
- [DESIGN.md gegen deklarative Layoutmodelle](COMPARE-DESIGN-LAYOUT.md): gleicher Zwei-Instanzen-Fall, Werte gegenüber Ankergeometrie, Höhe, Overflow und Modus; illustrativer CSS-Entwurf und Grenzen bei Portal/variablen Zeilen/native Ziele.

## Was sich jetzt noch nicht als erledigt melden lässt

Die Matrix hat **67 U-Zellen: 41 Integration und 26 weitere**. Insbesondere fehlt weiterhin ein belastbarer technischer Nachweis einer vollständigen Vier-Domänen-Kette zwischen unveränderten Originalartefakten. Keine hier untersuchte Quelle belegt diese konkrete Kombination bereits. Das ist ein Befund über den untersuchten Stand, kein Beweis, dass sie unmöglich wäre.

Der nächste Coding-Auftrag braucht ein explizites begrenztes Profil und praktische Nachweise. Die vorhandenen Entwürfe erlauben, Typen, Ziele, Instanzen, Einheiten, Childkontext und Konflikte einzeln zu prüfen. Der gewählte Arbeitsumfang bleibt Informationssammlung; zusätzliche Integration wird weder als gebaut noch als erfolgreich getestet ausgegeben.
