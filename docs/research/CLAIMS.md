# Claim- und Befundregister

Abdeckung und Evidenzstufe folgen [METHODS.md](METHODS.md). Alle Quellenstände stehen in [SOURCES.md](SOURCES.md). Die Matrix verweist auf diese IDs; Interpretation und nächster Versuch sind Teil jedes Befunds. **C01–C417 dokumentieren den historischen E1/E2-Stand. C418–C431 enthalten nun begrenzte ausgeführte E3-Prüfungen; keine vollständige UI-/AT-/Integrationsprüfung.**

## C01

- **Quelle:** [S01](SOURCES.md), E2; betrifft G01, I01.
- **Befund:** Package/CustomElement/ClassField und Type.text bilden Properties mit Typmetadaten ab.
- **Bedeutung/Grenze:** Direkt für beschreibende Web-API-Metadaten. Type.text ist ein Typausdruck als String, kein neutraler Payload-Validator.
- **Nächste Prüfung:** Komplexe Typen und deren Übersetzung separat validieren.

## C02

- **Quelle:** [S01](SOURCES.md), E2; betrifft I03.
- **Befund:** CustomElement besitzt benannte slots und cssParts.
- **Bedeutung/Grenze:** Benannte Anatomie ist direkt beschrieben; das ist keine Instanz-ID oder beliebiger Komponentenbaum.
- **Nächste Prüfung:** Mehrfachinstanzen und Rollen von Slot versus internem Teil prüfen.

## C03

- **Quelle:** [S01](SOURCES.md), E2; betrifft G02.
- **Befund:** Das Modell dokumentiert JavaScript-Module, Klassen, Attribute und Custom-Element-Events; Type.text darf sprachspezifische Syntax tragen.
- **Bedeutung/Grenze:** Für einen sprachneutralen gemeinsamen Kern ist eine Abbildung erforderlich; CEM bleibt als Web-Beitrag brauchbar.
- **Nächste Prüfung:** Bubbling/Cancelation und Typverlust bei nativer Abbildung untersuchen.

## C04

- **Quelle:** [S02](SOURCES.md), E1; betrifft G01, I01.
- **Befund:** §7 definiert YAML/JSON, components und props mit type/default/enum/required.
- **Bedeutung/Grenze:** Direkt für einfache Property-Metadaten; keine durchgeführte Schemaprüfung.
- **Nächste Prüfung:** Maßgebliches Schema und Typregeln lokalisieren.

## C05

**Fortschreibung vom 24. Oktober 2026:** Die damalige offene Frage ist durch [C133](#c133) im begrenzten Kern eingeordnet. Der folgende Text dokumentiert den früheren Prüfstand.

- **Quelle:** [S02](SOURCES.md), E1; betrifft I02.
- **Befund:** §10 empfiehlt Eventdokumentation, §7 definiert kein eigenes Event-/Payloadmodell.
- **Bedeutung/Grenze:** U statt D: Empfehlung ist kein belastbarer Nachweis strukturierter öffentlicher Payloads.
- **Nächste Prüfung:** Repository/Schema nach Eventmodell prüfen.

## C06

- **Quelle:** [S02](SOURCES.md), E1; betrifft B01.
- **Befund:** §11 führt State/Lifecycle und komplexes State-Management als zukünftige Erweiterung.
- **Bedeutung/Grenze:** N ausschließlich für ein spezifiziertes Zustandsübergangsmodell in draft-01; keine allgemeine Aussage über spätere Versionen.
- **Nächste Prüfung:** Neueren Entwurf und Repositorystand vergleichen.

## C07

- **Quelle:** [S03](SOURCES.md), E1; betrifft G01, V01.
- **Befund:** DESIGN.md kombiniert Markdown mit maschinenlesbaren YAML-Tokens; Typen für Farben, Dimensionen und Typografie sind beschrieben.
- **Bedeutung/Grenze:** Direkte strukturierte visuelle Werte; das gesamte Dokument ist keine vollständig formale UI-Beschreibung.
- **Nächste Prüfung:** Konkrete Positiv-/Negativfälle gegen Originalvalidator ausführen.

## C08

- **Quelle:** [S03](SOURCES.md), E1; betrifft V02.
- **Befund:** Components erlaubt verwandte Schlüssel wie button-primary und button-primary-hover mit Property-Tokens.
- **Bedeutung/Grenze:** Direkte benannte Stylevarianten; Zuordnung durch Namenskonvention/Agenten ist keine geprüfte externe Zustandsreferenz.
- **Nächste Prüfung:** Falschen Variantennamen und fehlende Zuordnung prüfen.

## C09

- **Quelle:** [S03](SOURCES.md), E1; betrifft V04.
- **Befund:** Layout beschreibt Strategie in Prosa und Spacing-Tokens; Components ist eine flexible Tokenmap.
- **Bedeutung/Grenze:** N für standardisierte relative Anker-/Abstandssemantik im geprüften Kern. Ein beliebiger Tokenname offset schafft diese Semantik nicht.
- **Nächste Prüfung:** Zusätzliche Layoutsprache prüfen; keine eigene Syntax als bestehend ausgeben.

## C10

**Fortschreibung vom 24. Oktober 2026:** Die damalige offene Frage ist durch [C124](#c124) im begrenzten Kern eingeordnet. Der folgende Text dokumentiert den früheren Prüfstand.

- **Quelle:** [S03](SOURCES.md), E1; betrifft X03.
- **Befund:** Token References adressieren Werte im eigenen YAML-Baum.
- **Bedeutung/Grenze:** U für vierformatige Domänenreferenzen: vorhandene interne Tokenverweise belegen dies nicht.
- **Nächste Prüfung:** Externe Referenzen und deren Prüfung separat untersuchen.

## C11

- **Quelle:** [S04](SOURCES.md), E1; betrifft G01, V01.
- **Befund:** §1 definiert YAML/JSON; §11 typisierte Tokenwerte und Referenzen.
- **Bedeutung/Grenze:** Direkte visuelle Daten; keine ausgeführte Validierung.
- **Nächste Prüfung:** Originalschema und Linter auf falsche Dimensionen prüfen.

## C12

- **Quelle:** [S04](SOURCES.md), E1; betrifft V02, V03.
- **Befund:** §13 hat variants/states und Tokenbags; §7.3 definiert Themes als pfadweise Overlays mit Defaultmodus.
- **Bedeutung/Grenze:** Direkt für beschriebene Varianten und Modeauflösung; keine unabhängige Bestätigung der Exporte.
- **Nächste Prüfung:** Themewechsel und Vorrang mit einem minimalen Artefakt prüfen.

## C13

**Fortschreibung vom 24. Oktober 2026:** [C180](#c180) ordnet die frühere offene Frage im begrenzten Kern ein; der folgende Wortlaut ist historischer Prüfstand.

- **Quelle:** [S04](SOURCES.md), E1; betrifft X07.
- **Befund:** §11.3/§19 fordern Fehler bei gebrochenen oder zyklischen Tokenreferenzen und Alias-Kollisionen.
- **Bedeutung/Grenze:** U für Paketkonflikte: interne Regeln sind vorhanden, prüfen aber nicht automatisch Interface/Behavior/APG-Verknüpfungen.
- **Nächste Prüfung:** Interne Negativtests und anschließend domänenübergreifenden Konfliktfall prüfen.

## C14

- **Quelle:** [S05](SOURCES.md), E1; betrifft G01, V01.
- **Befund:** Format Module definiert Tokenobjekte mit Typ und Wert sowie Dimensionstypen.
- **Bedeutung/Grenze:** Direkt für Tokenwerte, keine vollständige Komponentengeometrie.
- **Nächste Prüfung:** Falsche Einheiten und ungültige Typ/Wert-Kombination prüfen.

## C15

- **Quelle:** [S06](SOURCES.md), E1; betrifft V03.
- **Befund:** Resolver Module beschreibt Auflösung in mehreren Kontexten, ausdrücklich auch Light/Dark Mode.
- **Bedeutung/Grenze:** Direkt innerhalb des Resolvermodells; Format Module allein wird nicht damit gleichgesetzt.
- **Nächste Prüfung:** Kontexte und deterministische Modusauswahl am konkreten Resolver testen.

## C16

- **Quelle:** [S07](SOURCES.md), E1; betrifft G01, G02, B01, B02, B03.
- **Befund:** UXSpec v0.2 beschreibt JSON, Context, Events, Transitions, Guard-Ausdrücke und definierte Action-Kinds.
- **Bedeutung/Grenze:** Direkt dokumentiertes sprachneutrales Datenmodell. Behauptete SCJSON-Kompatibilität ist nicht durch Gleichheit mit SCXML oder Compilerlauf belegt.
- **Nächste Prüfung:** Ereignisfolge mit Guard/assign unabhängig vom visuellen Modell prüfen.

## C17

- **Quelle:** [S08](SOURCES.md), E2; betrifft X01.
- **Befund:** stateNode hat keine required-Liste für $visual; machine verlangt id/initial/states, nicht $visual; oberste Pflichtfelder sind $schema/$description/$machine.
- **Bedeutung/Grenze:** Positiver Teilbefund für die eng begrenzte Frage eines Verhaltensdokuments ohne Visual auf Schemaebene. X01 bleibt insgesamt U, weil alle vier getrennten Teilmodelle verlangt sind. Vierformatige Integration, Compiler und Runtime bleiben ungeprüft.
- **Nächste Prüfung:** Visualfreies Minimaldokument gegen Schema und anschließend Compiler testen.

## C18

- **Quelle:** [S07](SOURCES.md), E1; betrifft V02, B04.
- **Befund:** interactions definiert visuelle Style-Overrides; $visual.keyboard bildet Tasten auf Ereignisse ab.
- **Bedeutung/Grenze:** Direkt beschrieben; Keyboard-Bindung liegt im visuellen Block und muss bei strikter Domänentrennung bewusst behandelt werden.
- **Nächste Prüfung:** Binding extrahieren/referenzieren, ohne unabhängige zweite Tastaturregeln einzuführen.

## C19

- **Quelle:** [S07](SOURCES.md), E1; betrifft X02.
- **Befund:** testId ist als stabiler Testbezeichner dokumentiert; name und focus.target ermöglichen Elementbezug.
- **Bedeutung/Grenze:** Direkt für explizite Elementkennzeichnung; globale/instanzübergreifende Eindeutigkeit nicht nachgewiesen.
- **Nächste Prüfung:** Zwei gleiche Komponenteninstanzen auf ID-Kollision prüfen.

## C20

- **Quelle:** [S07](SOURCES.md), E1; betrifft X04.
- **Befund:** Element References verwendet $elements/$ref mit Instanz-Overrides und Inline-Expansion.
- **Bedeutung/Grenze:** Direkte Wiederverwendung von Elementdefinitionen; autonomes ScrollArea-Verhalten und Instanzlebenszyklus noch nicht bewiesen.
- **Nächste Prüfung:** Wiederverwendbare Unterkomponente mit Parametern und Verhalten prüfen.

## C21

**Fortschreibung vom 24. Oktober 2026:** [C204](#c204) ordnet die frühere offene Frage im begrenzten Kern ein; der folgende Wortlaut ist historischer Prüfstand.

- **Quelle:** [S08](SOURCES.md), E2; betrifft X05.
- **Befund:** Das Schema erlaubt $imports.from und boolesche Teilimporte; machineInvoke verlangt kind/src/id.
- **Bedeutung/Grenze:** U für versionierte externe Abhängigkeiten: Stringpfad und Import beweisen keine Versionbindung und keinen Lockmechanismus.
- **Nächste Prüfung:** Compilerauflösung, Namespaces, Zyklen und Versionsbindung untersuchen.

## C22

- **Quelle:** [S09](SOURCES.md), E1; betrifft G01, G02, B01, B02, B03.
- **Befund:** SCXML definiert XML-Zustandsmodell, event/cond/target, ausführbare Inhalte und Datenmodelle.
- **Bedeutung/Grenze:** Direkt für Verhalten in gewähltem Datenmodell. Hostbindungen und native UI-Integration werden dadurch nicht geliefert.
- **Nächste Prüfung:** Konkretes Datenmodell und Interpreter festlegen, Trace gegen Erwartung prüfen.

## C23

- **Quelle:** [S10](SOURCES.md), E1; betrifft B01.
- **Befund:** createMachine beschreibt initial/states/on/target und unabhängige Actorinstanzen.
- **Bedeutung/Grenze:** Direkt dokumentierte Zustandsübergänge; kein Schema-/Runtimeversuch in dieser Studie.
- **Nächste Prüfung:** Konkreten Paketstand pinnen und Trace testen.

## C24

- **Quelle:** [S10](SOURCES.md), E1; betrifft G02.
- **Befund:** Providing implementations beschreibt sprachspezifische Implementierungen für Actions, Actors und Guards.
- **Bedeutung/Grenze:** A für den hier geforderten sprachneutralen, datenbasierten Kern: konkrete Implementierungen benötigen zusätzliche neutrale Semantik oder Bindungen.
- **Nächste Prüfung:** Serialisierbare Teilmenge und externe Implementierungsabhängigkeiten isolieren.

## C25

- **Quelle:** [S11](SOURCES.md), E1; betrifft G02.
- **Befund:** Zag beschreibt JS-Frameworkadapter, Statecharts und eigene API; es erklärt ausdrücklich, SCXML nicht zu folgen.
- **Bedeutung/Grenze:** A für neutralen Verhaltenstransfer; kein vorhandener SCXML-Export nachgewiesen.
- **Nächste Prüfung:** Quellmodell und Exportmöglichkeiten gezielt prüfen.

## C26

- **Quelle:** [S11](SOURCES.md), E1; betrifft A02.
- **Befund:** Zag dokumentiert Umgang mit Tastatur, Fokus und ARIA als Teil der Bibliothek.
- **Bedeutung/Grenze:** U für ein separates referenzierbares Anforderungsmodell: Bibliotheksfunktion ist kein Nachweis eines exportierten Contracts.
- **Nächste Prüfung:** Konkrete Komponentenmaschine und APG-Bindung untersuchen.

## C27

- **Quelle:** [S12](SOURCES.md), E1; betrifft X02, X04.
- **Befund:** Ark dokumentiert ids sowie asChild-Komposition eigener Komponenten, einschließlich gemeinsamen IDs für Interaktion.
- **Bedeutung/Grenze:** Direkt in der Ark-Laufzeitrolle; kein sprachneutraler Paketverweis und keine Versionsauflösung.
- **Nächste Prüfung:** Overlay/ScrollArea-Komposition mit zwei Instanzen und Fokus prüfen.

## C28

- **Quelle:** [S13](SOURCES.md), E1; betrifft V02.
- **Befund:** Recipes definiert base, variants, defaultVariants und compoundVariants als strukturierte Maps.
- **Bedeutung/Grenze:** Direkt für visuelle Varianten innerhalb Panda; Extraktion in ein neutrales Schema ist noch offen.
- **Nächste Prüfung:** Rezept und zustandsbezogene Tokenreferenzen am gepinnten Stand prüfen.

## C29

- **Quelle:** [S14](SOURCES.md), E1; betrifft G01.
- **Befund:** uSpec dokumentiert kanonische .json-Komponentencontracts und daraus erzeugtes Markdown.
- **Bedeutung/Grenze:** Direkter dokumentierter maschinenlesbarer Beitrag. Einzelne API-/Accessibility-Felder bleiben U bis zur Schemaprüfung.
- **Nächste Prüfung:** Kanonisches Schema und Beispielartefakt lokalisieren und prüfen.

## C30

- **Quelle:** [S15](SOURCES.md), E1; betrifft I03, X02.
- **Befund:** OpenPencil bindet Werte/Slots per ID; Behaviour-Contracts benennen Parts und Zustandsvarianten.
- **Bedeutung/Grenze:** Direkt für Anatomy und IDs im OpenPencil-Modell; beim .fig-Export werden IDs umbenannt. Universelle stabile Identität bleibt offen.
- **Nächste Prüfung:** Export/Import mit Identitätsabbildung und Mehrfachinstanzen prüfen.

## C31

- **Quelle:** [S16](SOURCES.md), E1; betrifft A01, A03.
- **Befund:** ARIA definiert Rollen, Zustände, Eigenschaften, ID-Beziehungen und Live-Region-Semantik.
- **Bedeutung/Grenze:** Direkt als Web-Semantikreferenz, nicht als ausführbarer neutraler Paketvalidator. Konkrete Ergebnisansage ist Produktregel.
- **Nächste Prüfung:** Auslöser/Inhalt und reale Assistive-Technology-Wahrnehmung separat testen.

## C32

- **Quelle:** [S17](SOURCES.md), E1; betrifft A02.
- **Befund:** APG Combobox beschreibt Varianten, Tastatur und Fokus, einschließlich aria-activedescendant im Listbox-Fall.
- **Bedeutung/Grenze:** Direkt als Interaktionsleitfaden; nicht als universell verpflichtende konkrete Produktvariante und nicht als maschinenlesbarer Automat.
- **Nächste Prüfung:** Gewählte Variante in Assertions übersetzen und manuell prüfen.

## C33

- **Quelle:** [S18](SOURCES.md), E1; betrifft V04.
- **Befund:** CSS Anchor Positioning beschreibt Beziehung zu Ankerelementen und relative Größen/Positionen.
- **Bedeutung/Grenze:** Direkt im CSS-Webmodell; kein neutraler Cross-Platform-Standard und kein Nachweis von Browserunterstützung.
- **Nächste Prüfung:** Abstand, Ankerbreite, Fallback und Namensräume in konkreten Umgebungen testen.

## C34

- **Quelle:** [S19](SOURCES.md), E1; betrifft V06.
- **Befund:** CSS Overflow definiert Scroll-Overflow und overflow-Achsen.
- **Bedeutung/Grenze:** Direkt für Overflow im CSS-Modell; exakte sichtbare Zeilenzahl verlangt zusätzlich Höhenmodell und darf nicht aus overflow allein gefolgert werden.
- **Nächste Prüfung:** Höhenbegrenzung mit variabler Typografie und Wiederverwendung einer ScrollArea prüfen.

## C35

- **Quelle:** [S01](SOURCES.md), E2; betrifft X05.
- **Befund:** Reference enthält name/package/module, aber keine Versionbindung an dieser Stelle.
- **Bedeutung/Grenze:** Erster Teilbefund war U. Die vollständige CEM-Kernprüfung präzisiert X05 jetzt zu N im Formatkern; siehe C45. Externe Symbolnamen bleiben unterstützt, eine standardisierte Versionsbindung wird im CEM-Kern nicht definiert.
- **Nächste Prüfung:** Paketmanifest/Lockdatei und Referenzsemantik gemeinsam prüfen.

## C36

- **Quelle:** [S05](SOURCES.md), E1; betrifft V01.
- **Befund:** Tokenalias verweist auf einen anderen Tokenwert; Typ-/Wertregeln bleiben im Tokenmodell.
- **Bedeutung/Grenze:** R für das Teilkriterium eines abgeleiteten Werts innerhalb V01; kein Beleg für Komponentenkomposition.
- **Nächste Prüfung:** Fehlendes/zyklisches Ziel als Negativfall prüfen.


# Vertiefung ausschließlich CEM

Alle 22 zuvor offenen CEM-Zellen wurden am 23. Oktober 2026 geprüft. 20 wurden eingeordnet; I02 und X01 bleiben mit benannter Frage U. Die ursprünglichen vier CEM-Bewertungen bleiben unverändert. N-Befunde beruhen auf dem vollständig geprüften, unten bezeichneten Standardkern und seinen Zielarten, nicht allein auf einer erfolglosen Stichwortsuche. Erweiterte Fremdfelder und Plugins sind davon ausdrücklich getrennt. Alle neuen Schema-Befunde sind E2; ergänzende Werkzeug-/CSS-Dokumentation E1. Kein E3-Versuch wurde ausgeführt.

## C37

**Fortschreibung der Gesamtprüfung:** Aktueller Befund [C413](#c413); der folgende Text dokumentiert den früheren Stand.

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft I02; Bewertung **U**.
- **Befund:** Event hat name/type; Type enthält text und optionale TypeReference. Referenzen können auf Deklarationen mit members zeigen. Ein eigener payload-Feldkatalog oder eine vorgeschriebene Zuordnung von CustomEvent<T> zu dessen detail-Feldern ist nicht definiert.
- **Bedeutung/Grenze:** Ereignisname und Typ sind abgedeckt. Die gesamte Anforderung strukturierter Payload-Felder bleibt U: Ein Typstring ist nicht derselbe Nachweis wie ein aufgelöstes, eindeutig zugeordnetes Payloadmodell. Die allgemeinen Klassen-/Typreferenzen könnten dazu beitragen; sie werden weder als unmöglich noch als fertige Lösung bewertet.
- **Offene Frage / weiterer Bedarf:** Offene Frage: Kann eine dokumentierte Ereignistyp-/Payloaddeklaration allein mit Standardreferenzen eindeutig bis zu detail-Feldern verfolgt werden, auch für CustomEvent<T>, ohne frei gewählte Bindungskonvention? Zunächst offizielle Beispiele und Typreferenzkonventionen prüfen; nur bei verbleibender Unklarheit einen kleinen Typauflösungsversuch durchführen.

## C38

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md), [S23](SOURCES.md); CEM-Schema-/Typprüfung E2; ergänzende Dokumentation E1. Betrifft V01; Bewertung **R**.
- **Befund:** CssCustomProperty enthält name, syntax und default. Der Kommentar verlangt für syntax die CSS-Syntaxstrings der Properties and Values API, etwa <color> oder <length> | <percentage>. Die externe CSS-Spezifikation definiert deren Bedeutung.
- **Bedeutung/Grenze:** R für typisierte CSS-Designwerte: Name/Syntax/Standardwert sind strukturiert, die Wertsemantik wird aus dem benannten CSS-Modell übernommen. Das ist kein DTCG-Tokenmodell, keine Typografie-Komposition und keine automatische Durchsetzung: Im CEM-JSON-Schema bleiben syntax/default Strings; die CSS-Grammatik wird dort nicht als Validator implementiert. CEM registriert die CSS-Property auch nicht automatisch im Browser.
- **Offene Frage / weiterer Bedarf:** Für eine spätere Validierungsbehauptung muss geprüft werden, welches konsumierende Werkzeug CSS-Syntax und Standardwert tatsächlich zusammen prüft. Für die dokumentierte Beschreibungsmöglichkeit ist kein Laufzeitversuch erforderlich.

## C39

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft V02, V03; Bewertung **N**.
- **Befund:** CssCustomState beschreibt name/summary/description/deprecated. CssCustomProperty beschreibt jeweils syntax/default. Das vollständig geprüfte Kernschema enthält weder Zustand-zu-Style-/Token-Zuordnungen noch Modusauswahl oder Theme-Overlay-Regeln.
- **Bedeutung/Grenze:** N im CEM-Kern für strukturierte visuelle Zustandsvarianten und Themeauflösung. Benannte CSS-Zustände dokumentieren die Styling-Schnittstelle, nicht die Styles je Zustand. Ein Propertyname wie theme oder dark und eine Erklärung im description-Feld führen keine normierte Auflösungsregel ein.
- **Offene Frage / weiterer Bedarf:** Kein Versuch nötig, um diesen begrenzten Modellumfang festzustellen. Falls später externe Styles referenziert werden sollen, muss deren eigenes Modell separat geprüft werden; keine Auswahl erfolgt hier.

## C40

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft V04, V05, V06; Bewertung **N**.
- **Befund:** Die vollständig gelesenen Definitionen von CustomElementDeclaration, CssPart, Slot und CssCustomProperty enthalten keine Layoutknoten, Ankerbeziehungen, Flächenbegrenzungen oder Overflow-Anweisungen mit Ausführungssemantik.
- **Bedeutung/Grenze:** N im CEM-Kern für relative Geometrie, Flächenbegrenzung und Scrollregeln. Eine CSS-Custom-Property könnte einen Abstandswert oder ein Limit dokumentieren; CEM ordnet diesen Wert aber nicht formal einem bestimmten Elementlayout zu. CSS-Parts sind benannte Stylingziele, keine gespeicherten Stylesheets.
- **Offene Frage / weiterer Bedarf:** Kein praktischer Versuch nötig: Gegenstand ist die deklarierte Formatsemantik, nicht die Fähigkeit einer bereits implementierten Web-Komponente zu layouten oder zu scrollen.

## C41

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft B01, B02, B03, B04; Bewertung **N**.
- **Befund:** Das Kernmodell beschreibt Events, Methoden, Parameter, Felder und CSS-State-Namen. Es definiert keine Initialzustände, Transitionen, Guards, Aktionsauswertung, Ereignisverarbeitung oder Tastatur-/Fokus-zu-Aktionsbindung.
- **Bedeutung/Grenze:** N für die vier Behavior-Anforderungen im CEM-Kern. Öffentliches API-Inventar und Zustandsnamen sind keine Verhaltensmaschine. FunctionLike dokumentiert eine Methodensignatur; deren Aufrufbedingungen und Wirkung verbleiben im Implementierungscode beziehungsweise in Prosa.
- **Offene Frage / weiterer Bedarf:** Keine Komponentenimplementierung erforderlich. Ein Analyzer kann Signaturen extrahieren; das erzeugt ohne zusätzliche Fachsemantik keinen UX-Automaten.

## C42

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft A01, A02, A03; Bewertung **N**.
- **Befund:** Keine Kerndefinition enthält Accessibility-Rollen-/Namensregeln, semantische IDREF-Beziehungen, Patternanforderungen, Tastatur-/Fokusregeln oder eine Ankündigungssemantik. Attribute und Properties sind allgemein beschreibbar, einschließlich möglicher ARIA-bezogener Namen.
- **Bedeutung/Grenze:** N im CEM-Kern für die drei Accessibility-Anforderungen. Ein Attribut namens aria-label oder ein Textverweis auf ein Pattern ist noch kein Accessibility-Fachmodell. Dies sagt nichts über die tatsächliche Barrierefreiheit einer mit CEM dokumentierten Komponente aus.
- **Offene Frage / weiterer Bedarf:** Für diesen Formatbefund ist kein Screenreadertest nötig. Zusätzliche Accessibility-Metadaten eines Plugins wären als eigenes Modell zu prüfen und nicht ungeprüft dem Standard zuzuschreiben.

## C43

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft X01; Bewertung **U**.
- **Befund:** Ein CEM-Dokument verlangt auf oberster Ebene nur schemaVersion und modules. Es verlangt keine visuellen Regeln und kein UX- oder Accessibility-Modell. Damit lässt sich der Interface-Beitrag eigenständig führen.
- **Bedeutung/Grenze:** Positiver Teilbefund, aber U für die vollständige Vier-Domänen-Anforderung: CEM allein definiert weder die anderen drei Originalformate noch deren gemeinsame Paketbindung. Ohne diese Bindung ist vollständige Unabhängigkeit samt korrekten Beziehungen nicht entschieden. Eine fremde Zusatzstruktur innerhalb CEM wäre keine automatisch standardisierte Domäne.
- **Offene Frage / weiterer Bedarf:** Offene Frage: Lassen sich die separat gewählten Domänenartefakte mit unverändertem CEM verbinden, ohne dort fachfremde Pflichtfelder oder doppelte Definitionen einzuführen? Diese Paketfrage erst nach Untersuchung der übrigen Kandidaten klären.

## C44

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft X02, X03, X04; Bewertung **N**.
- **Befund:** Reference benennt exportierte Symbole über name/package/module. SourceReference.href zeigt auf Quellcode. Slot/CssPart benennen APIs einer Deklaration. Der Kern enthält keine UI-Instanzknoten, instanzbezogenen Teile-IDs, Domänen-Zielarten oder Komponentenbaum-/Instanzbindungen.
- **Bedeutung/Grenze:** N im CEM-Kern für elementbezogene Instanzidentität, vierformatige Domänenreferenzen und wiederverwendbare Komponenteninstanzen. Deklarationsreferenzen sind vorhanden, verweisen jedoch auf andere Zielarten. Slotannahme, Vererbung und Mixins sind kein Contract für ein Overlay, das eine ScrollArea mit eigenem Instanzkontext verwendet. Auch eine Quellcode-URL ist keine solche Bindung.
- **Offene Frage / weiterer Bedarf:** Eine spätere Abbildung müsste Deklaration, UI-Instanz und Teilidentität ausdrücklich unterscheiden. Ein solcher Mechanismus wird in diesem Schritt weder entworfen noch als vorhandener Adapter behauptet.

## C45

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md), [S21](SOURCES.md), [S22](SOURCES.md); CEM-Schema-/Typprüfung E2; ergänzende Dokumentation E1. Betrifft X05; Bewertung **N**.
- **Befund:** Reference hat name/package/module, aber keine Version-/Integritätsbindung. schemaVersion bezeichnet die Version des CEM-Schemas. Die README beschreibt Manifest-Discovery über package.json.customElements. Der Analyzer kann mit --dependencies Metadaten vorhandener Abhängigkeiten einbeziehen; das ist eine Werkzeugfunktion.
- **Bedeutung/Grenze:** N für eigenständige reproduzierbare Versionsbindung externer Referenzen im CEM-Kern. Ein vorhandenes npm-Lockfile könnte den umgebenden Installationsstand fixieren, ist aber kein normierter Versionsresolver des CEM-Dokuments. Externe Symbole sind beschreibbar; ein standardisierter referenzlokaler Versions-/Integritätsvertrag ist damit nicht gegeben. C35 wird dadurch auf Grundlage der vertieften Prüfung präzisiert.
- **Offene Frage / weiterer Bedarf:** Keine Paketinstallation nötig, um die Felder und ihre dokumentierte Bedeutung festzustellen. Ob ein zukünftiges Contract-Paket externes Locking übernimmt, bleibt außerhalb dieses Schritts offen.

## C46

**E3-Fortschreibung:** aktueller Befund [C419](#c419); folgender Text dokumentiert den früheren Stand.

- **Quelle:** [S20](SOURCES.md), [S21](SOURCES.md); CEM-Schema-/Typprüfung E2; ergänzende Dokumentation E1. Betrifft X06; Bewertung **D**.
- **Befund:** Das Formatprojekt veröffentlicht ein eigenständiges JSON Schema nach Draft-07. Root verlangt schemaVersion/modules; lokale Schema-$ref verweisen auf die mitgelieferten Definitionen. Die README zeigt den direkten Import dieses Schemas.
- **Bedeutung/Grenze:** D für das Beibehalten der originalen CEM-Schemaprüfung eines separaten Interface-Artefakts. Hier wurde das Schema gelesen, kein Validator ausgeführt. Geprüft werden Datenform und Pflichtfelder, nicht automatisch Typstring-/CSS-Grammatik, UI-Referenzen oder das gesamte Vier-Domänen-Paket.
- **Offene Frage / weiterer Bedarf:** Ein späterer Versuch kann einen Draft-07-Validator auf ein gültiges und ein strukturell falsches Manifest anwenden. Das ist für die dokumentierte Verfügbarkeit des unveränderten Schemas noch nicht nötig.

## C47

- **Quelle:** [S01](SOURCES.md), [S20](SOURCES.md); CEM-Schema-/Typprüfung E2. Betrifft X07, X08; Bewertung **N**.
- **Befund:** Das JSON Schema prüft strukturelle Datentypen und Pflichtfelder. Die TypeScript-Kommentare nennen einzelne Konsistenzregeln, etwa korrespondierende Attribute oder gemeinsam vorkommende Referenz-Indizes. Es gibt aber keine paketweite Domänen-Ownership-/Vorrangregel und keine beschriebenen Cross-Domain-Konflikt-, Instanz- oder Zielauflösungsprüfungen.
- **Bedeutung/Grenze:** N im CEM-Kern für die gesamte Paketkonfliktprüfung und eindeutige domänenübergreifende führende Quelle. Die Empfehlung eines kanonischen Exports betrifft Symbolidentität, nicht Ownership über alle Fachmodelle. Fehlendes additionalProperties:false in den geprüften Objekten bedeutet, dass zusätzliche Daten nicht allein deshalb scheitern; es verleiht ihnen keine definierte Semantik oder Prüfung.
- **Offene Frage / weiterer Bedarf:** Plugins oder Verbraucher könnten zusätzliche Prüfungen implementieren. Solche Fähigkeiten dürfen erst nach eigener Prüfung bewertet werden; sie sind nicht automatisch Eigenschaften des CEM-Formats.


# Vertiefung ausschließlich DTCG

Alle 23 zuvor offenen DTCG-Zellen wurden am 23. Oktober 2026 gegen die getrennten Module Format und Resolver 2025.10 geprüft. 22 wurden eingeordnet, X01 bleibt mit einer konkreten Frage U. Die 3 ursprünglichen DTCG-Bewertungen bleiben erhalten. Kein anderer Kandidat wurde dabei neu bewertet. Quellenprüfung E1 und manuelle Prüfung der veröffentlichten Schemadefinitionen E2 sind keine ausgeführten E3-Versuche. Format-Token, Resolver-Kontext und UI-Komponente sind verschiedene Gegenstände.

## C48

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md); E1. Betrifft G02; Bewertung **D**.
- **Befund:** Format §4 legt JSON als Austauschformat fest; §8/9 definieren Werte und Typen. Resolver §3/5/6 legt JSON, JSON-serialisierbare Kontexteingaben und Auflösungsschritte fest, ohne JavaScript-/React-Funktionen im Dokument vorauszusetzen.
- **Bedeutung/Grenze:** Direkt für den sprachneutralen Token-/Resolverkern. Plattformkonvertierung kann dennoch verlustbehaftet sein, etwa rem ohne entsprechendes Zielkonzept (Format §8.2). Kein Nachweis identischer Renderer oder universeller UI-Semantik.
- **Offene Frage / weiterer Bedarf:** Für diese Modellfrage ist kein Laufzeitversuch nötig; spätere Zielformatkonvertierung gesondert prüfen.

## C49

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft I01, I02, I03; Bewertung **N**.
- **Befund:** Format modelliert Tokenwerte und beliebig benannte Gruppen. Resolver modelliert Token-Sets, Kontexte und Auflösungsreihenfolge. Weder öffentliches Komponenten-API-Modell mit Inputs/Outputs noch Event-Payloadmodell oder Komponenten-Anatomie ist darin definiert.
- **Bedeutung/Grenze:** N im geprüften Format-/Resolverkern. Ein Token namens value oder eine Gruppe input ist kein öffentlicher Input beziehungsweise kein identifizierter UI-Teil. Format §3.7 verbietet gerade die Ableitung von Typ oder Zweck allein aus Gruppennamen. JSON-Typen für Designwerte erfüllen I01 nicht.
- **Offene Frage / weiterer Bedarf:** Kein Implementierungsversuch nötig, um diese Fachmodellgrenze festzustellen. Erweiterungsdaten wären separat spezifizierte Semantik, keine bereits definierte Standardfähigkeit.

## C50

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft V02; Bewertung **D**.
- **Befund:** Format §6.4 definiert Gruppenvererbung mit lokalen Overrides. Resolver §4.1.5/§5/§6 definiert benannte Kontexte eines Modifiers mit Tokenquellen, Auswahl durch Input und eindeutiger Auflösungsreihenfolge.
- **Bedeutung/Grenze:** Direkt für benannte visuelle Varianten auf Tokenebene: Unterschiedliche benannte Kontexte liefern unterschiedliche strukturierte Designwerte/Referenzen. Ein Zustandsname kann als Kontextwert verwendet werden; DTCG entscheidet jedoch nicht, wann dieser UX-Zustand eintritt oder welche Komponente den Wert anwendet. Die externe Bindung bleibt X03.
- **Offene Frage / weiterer Bedarf:** Kein neuer Variantentyp wird erfunden. Später Kontextauswahl, Default und Überschreibungen gegen ein konkretes Resolverwerkzeug prüfen; hier kein Laufzeitnachweis.

## C51

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft V04, V05, V06; Bewertung **N**.
- **Befund:** Format §8.2 definiert Dimensionen als Wert/Einheit, §9 zusammengesetzte Stylewerte. Resolver verarbeitet diese Tokenstrukturen. Kein Kernmodell definiert UI-Anker-/Zielbeziehungen, die Anwendung einer Maximalhöhe auf eine Fläche oder Overflow-/Scrollverhalten.
- **Bedeutung/Grenze:** N im Kern für Geometrie, Flächenbegrenzung und Overflow. Ein Abstand oder eine Maximalhöhe kann als Dimensionstoken gespeichert werden; der Tokenname allein bindet ihn nicht mit normierter Geometriesemantik an ein Element. Shadow.offsetX/offsetY beschreibt einen Schatten, keine allgemeine Overlayposition.
- **Offene Frage / weiterer Bedarf:** Für die festgestellte Semantikgrenze ist kein praktischer Versuch nötig. Die spätere Anwendung der Werte gehört zu einem weiteren bereits separat zu prüfenden Modell.

## C52

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft B01, B02, B03, B04; Bewertung **N**.
- **Befund:** Format §9.5 transition enthält duration, delay und timingFunction. Resolver-Inputs wählen Kontexte; sie beschreiben keine Benutzerereignisfolge, Initialzustände, Guards/Aktionsmaschine oder Fokus-/Tastaturbindungen.
- **Bedeutung/Grenze:** N für die vier UX-Verhaltensanforderungen im DTCG-Kern. Ein transition-Token ist ein Satz Animationsparameter, kein Zustandsübergang. Bedingte Tokenauswahl durch Modifier ist ebenfalls kein UX-Automat und verarbeitet keine UI-Event-/Kontextdaten nach einer solchen Maschine.
- **Offene Frage / weiterer Bedarf:** Keine Komponentenimplementierung erforderlich. Für ein späteres Behavior-Modell bleibt nur zu klären, wie dessen Zustandsausgabe die dokumentierte Resolvereingabe liefert.

## C53

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft A01, A02, A03; Bewertung **N**.
- **Befund:** Die definierten Token-/Resolvermodelle enthalten keine Rollen-/Namensbeziehungen, Fokus-/Tastaturpatterns oder Live-Region-/Ankündigungssemantik. Farben und High-Contrast-Kontexte können zugängliche Gestaltung unterstützen.
- **Bedeutung/Grenze:** N im Kern für die drei Accessibility-Anforderungen. Wahrnehmbare Designwerte oder ein Kontext namens highContrast sind kein vollständiges Accessibility-Fachmodell und kein Nachweis einer Screenreaderrückmeldung.
- **Offene Frage / weiterer Bedarf:** Kein Screenreadertest nötig, um diese Formatgrenze einzuordnen. Tatsächliche Wahrnehmung und Accessibility-Bindungen sind hier nicht untersucht.

## C54

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft X01; Bewertung **U**.
- **Befund:** Token- und Resolverdokumente verlangen kein Komponenteninterface, kein UX-Verhaltensmodell und keine Accessibility-Definition. Sie können als eigenständiger Designwerte-Beitrag geführt werden.
- **Bedeutung/Grenze:** Positiver Teilbefund; die vollständige Vier-Domänen-Anforderung bleibt U. Aus DTCG allein folgt nicht, dass die noch separat zu wählenden anderen Originalformate unverändert und widerspruchsfrei gemeinsam gebunden werden können.
- **Offene Frage / weiterer Bedarf:** Konkrete offene Frage: Wie referenzieren die anderen Domänen die aufgelösten Tokens/gewählte Permutation, ohne Werte oder Zuständigkeiten doppelt zu definieren? Diese Paketbindung nach den weiteren Einzelprüfungen klären.

## C55

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft X02, X03, X04; Bewertung **N**.
- **Befund:** Format §6/7 definiert Token-/Gruppenpfade, Aliase, $extends und JSON-Pointer-Wertzugriff. Resolver §4.2 erlaubt Verweise auf Tokenquellen und Resolverstrukturen. Weder UI-Element-/Instanzidentität noch Zustands-/Event-/Accessibility-Zielarten oder wiederverwendbare Komponenteninstanzen sind standardisiert.
- **Bedeutung/Grenze:** N im Kern für die drei UI-Integrationsanforderungen. Tokenidentität und Wiederverwendung von Gruppen sind echte Beiträge, aber keine Identität einer Inputinstanz oder Komposition einer ScrollArea. Die JSON-Pointer-Syntax macht das adressierte Objekt nicht automatisch zu einem UI-Element. $extensions kann fremde Metadaten tragen, deren Bedeutung bleibt außerhalb des Kerns.
- **Offene Frage / weiterer Bedarf:** Für diesen begrenzten Befund keine neue Referenzsyntax und keinen Adapter entwerfen. Eine spätere domänenübergreifende Abbildung muss den Unterschied zwischen Wert, Definition und UI-Instanz ausdrücklich behandeln.

## C56

- **Quellen:** [S06](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft X05; Bewertung **N**.
- **Befund:** Resolver §4.2 beschreibt lokale und externe URI-/Pointerreferenzen. Unterstützung von Referenzen im selben Dokument ist verpflichtend; Dateisystem- und Netzwerk-URIarten können Werkzeuge unterschiedlich unterstützen. version=2025.10 bezeichnet die Resolver-Spezifikation.
- **Bedeutung/Grenze:** N im Kern für reproduzierbar versionierte externe Komponenten-/Teilmodellabhängigkeiten: Eine externe Tokenquelle ist beschreibbar, aber ein Versions-/Integritäts- oder Lockvertrag für deren Inhalt ist nicht definiert. Eine unveränderliche URL kann außerhalb des Formats gewählt werden; daraus folgt weder verpflichtende Remoteauflösung noch eigenes Versionsmanagement des Resolvers.
- **Offene Frage / weiterer Bedarf:** Die konkrete externe URI-Unterstützung eines später ausgewählten Werkzeugs wäre bei Bedarf zu prüfen. Hier wird nicht behauptet, dass externe Referenzen generell unmöglich sind.

## C57

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft X06; Bewertung **D**.
- **Befund:** Auf der offiziellen DTCG-Domain sind getrennte JSON-Schemata für Format und Resolver 2025.10 verfügbar, beide mit Draft-07-Schemadialekt. Resolver §4.4 nennt ausdrücklich sein Schema zur Editor-/Syntaxprüfung. Die Formatfassung enthält noch einen redaktionellen Hinweis zur Schemaarbeit.
- **Bedeutung/Grenze:** D für die Beibehaltung veröffentlichter DTCG-Schemata eines separaten Domänenartefakts. Die Schemahilfen sind von der normativen Fachsemantik zu unterscheiden: Ein Schemaerfolg beweist keine korrekte Alias-/Vererbungs-/Resolverausführung. Kein Validator wurde ausgeführt, und vollständige Übereinstimmung von Schemata und Bericht wurde nicht bewiesen.
- **Offene Frage / weiterer Bedarf:** Später bei tatsächlichem Werkzeugbedarf Schemaabhängigkeiten laden und Positiv-/Negativfälle prüfen. Semantische Prüfungen wie Zyklen und Kontextauflösung separat behandeln.

## C58

- **Quellen:** [S05](SOURCES.md), [S06](SOURCES.md), [S24](SOURCES.md), [S25](SOURCES.md); E2 und E1. Betrifft X07, X08; Bewertung **N**.
- **Befund:** Format §6.4/§6.7/§7 fordert Prüfung von Verweisen, Zyklen und Typen sowie definierte lokale Overrides. Resolver §4.2/§6 regelt ungültige Pointer, Eingaben und Reihenfolge; bei Tokenkonflikten gewinnt der spätere Eintrag.
- **Bedeutung/Grenze:** N für die vollständige Paketkonfliktprüfung und domänenübergreifende Ownership. DTCG enthält bereits präzise interne Prioritäts- und Fehlerregeln; diese prüfen aber weder widersprüchliche UX-/Accessibility-Regeln noch UI-Instanzkollisionen oder führende Quellen fremder Fachmodelle. Nicht alle Konflikte werden abgewiesen: gewollte Tokenüberschreibungen sind definiertes Verhalten.
- **Offene Frage / weiterer Bedarf:** Keine eigenen Konfliktregeln in diesem Schritt erfinden. Eine spätere Paketprüfung muss DTCGs interne Regeln erhalten und zusätzlich die noch zu definierenden Domänenbindungen prüfen.


# Vertiefung ausschließlich SCXML

Alle 21 zuvor offenen SCXML-Zellen wurden am 23. Oktober 2026 gegen die W3C Recommendation vom 1. September 2015 geprüft. 18 wurden eingeordnet; I02, X01 und X04 bleiben mit konkreter Frage U. Die 5 vorhandenen SCXML-Bewertungen bleiben erhalten. Sie betreffen jeweils die definierte Sprache mit bewusst zu wählendem Datenmodell, nicht automatisch einen vorhandenen Interpreter. Die Errata erläutern insbesondere die zu definierenden Ausdruckssprachen und korrigieren Beispiele; ein unbesehenes Kopieren der Beispiele ist kein Nachweis. Keine praktische Ausführung fand statt, und kein UXSpec-Durchgang wird als erledigt angenommen.

## C59

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft I01, I03; Bewertung **N**.
- **Befund:** SCXML §3 definiert Zustände/Transitionen; §5 Daten und Parameter; §6 externe Kommunikation und Dienste. Die Standardsprache definiert kein öffentliches UI-Property-Typsystem und keine Komponenten-Anatomie mit Input/Popup/Slots. <data id> ist eine Datenmodellvariable; <param> übergibt Werte, nicht eine typisierte öffentliche Komponentenbeschreibung.
- **Bedeutung/Grenze:** N im SCXML-1.0-Kern für I01 und I03. Zustand-ID, Dienstname oder frei benannte Datenvariable sind keine standardisierte UI-Property beziehungsweise kein UI-Teil. Die Wahl eines Datenmodells ist nicht mit einem öffentlichen Interfacevertrag gleichzusetzen.
- **Offene Frage / weiterer Bedarf:** Die Fachmodellgrenze ist durch die Spezifikation bestimmbar; keine Komponentenimplementierung erforderlich. Ein späterer Interfacevertrag könnte Daten und Dienstparameter binden, wird hier aber nicht entworfen.

## C60

**Fortschreibung der Gesamtprüfung:** Aktueller Befund [C414](#c414); der folgende Text dokumentiert den früheren Stand.

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft I02; Bewertung **U**.
- **Befund:** §5.7 und §6.2 definieren <send event> mit benannten <param>-Werten, namelist oder <content>. §5.10.1 definiert _event.data; §6.2.5 und Anhang C unterscheiden I/O-Prozessoren. Damit können Ereignisse einschließlich strukturierter Daten gesendet werden.
- **Bedeutung/Grenze:** Positiver Teilbefund, aber U für einen vom Auslösezeitpunkt getrennten öffentlichen Event-/Payloadvertrag. <send> beschreibt ausführbare Kommunikation und kann Eventnamen/Werte dynamisch berechnen. Die genannte öffentliche Signatur als separat überprüfbare Beschreibung folgt daraus noch nicht. Das Versenden strukturierter Daten wird ausdrücklich nicht als fehlend bewertet.
- **Offene Frage / weiterer Bedarf:** Offene Frage: Reicht eine klar abgegrenzte, dokumentierte SCXML-Teilmenge mit statischen Events und benannten Parametern aus, um die öffentlichen Payloadfelder eindeutig und unabhängig vom Sendepunkt zu bestimmen, oder ist eine separate Eventdeklaration nötig? In diesem Durchgang keine Praxisversuche.

## C61

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft V01, V02, V03, V04, V05, V06; Bewertung **N**.
- **Befund:** Die SCXML-Kernelemente beschreiben Zustandslogik, Daten und Kommunikation. Kein definierter Element-/Attributsatz beschreibt Design-Tokentypen, visuelle Styles/Varianten, Themeauflösung, Layoutanker, Flächenbegrenzung oder Overflow. <content>/<data> dürfen fremde Inhalte enthalten; §4.10 erlaubt Erweiterungen ausführbarer Inhalte.
- **Bedeutung/Grenze:** N für die sechs visuellen Anforderungen im SCXML-1.0-Kern. Werte oder XHTML/CSS lassen sich transportieren, erhalten dadurch aber keine SCXML-eigene Visual-/Layoutsemantik. Ein benannter Zustand wie dark oder highlighted definiert weder dessen Farben noch die Themeauflösung. Standarderweiterbarkeit ist kein Nachweis eines bestimmten vorhandenen visuellen Zusatzmodells.
- **Offene Frage / weiterer Bedarf:** Keine visuelle Laufzeitprüfung nötig, um den Kernumfang abzugrenzen. Eine eventuelle externe Darstellungsspezifikation bleibt ein gesonderter Beitrag; keine zusätzliche Kandidatenbewertung erfolgt hier.

## C62

- **Quellen:** [S09](SOURCES.md); E1. Betrifft B04; Bewertung **A**.
- **Befund:** §3.12/§3.13 verarbeiten anwendungsspezifische externe Ereignisse; §6 und Anhang C definieren Kommunikation über I/O-Prozessoren. Der SCXML-Kern definiert jedoch weder DOM-Key-/Fokusereignisse als Eingabequelle noch eine generische UI-focus-Aktion.
- **Bedeutung/Grenze:** A mit konkret benanntem Abbildungsbedarf: Die Hostintegration muss etwa ein bestimmtes Tastatur-/Fokusereignis in ein SCXML-Ereignis mit passenden Daten übersetzen und eine ausgehende Fokusanforderung an die UI weitergeben. Die danach ausgeführte Ereignis-/Transitionslogik ist standardisiert. Es wird kein vorhandener universeller UI-Adapter behauptet.
- **Offene Frage / weiterer Bedarf:** Welche Ereignisnamen, Elementidentitäten und Hostaktionen verwendet werden, ist später ausdrücklich zu binden. Kein Interpreter oder Adapter wurde installiert beziehungsweise getestet.

## C63

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft A01, A02, A03; Bewertung **N**.
- **Befund:** SCXML definiert weder Accessibility-Rollen-/Namensbeziehungen noch verpflichtende UI-Bedienmuster oder Live-Region-/Screenreader-Semantik. <log> erzeugt Debugausgabe; <send>/<invoke> kommuniziert mit Diensten. Optionale VoiceXML-Diensttypen sind keine allgemeine Accessibility-Spezifikation.
- **Bedeutung/Grenze:** N für die drei Accessibility-Anforderungen im SCXML-1.0-Kern. Eine Maschine kann Aktionen zur Bedienbarkeit koordinieren, aber die Bedeutung und Anforderungen dieser Aktionen müssen aus einer anderen Quelle kommen. Sprach-/Audioausgabe eines Dienstes darf nicht pauschal mit Barrierefreiheit gleichgesetzt werden.
- **Offene Frage / weiterer Bedarf:** Für die Formatabgrenzung ist kein Screenreadertest nötig. Spätere Bindungen an vereinbarte Accessibility-Regeln bleiben separat nachzuweisen.

## C64

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft X01; Bewertung **U**.
- **Befund:** Ein SCXML-Dokument kann gemäß §3/A.1 ohne visuelle Beschreibung, öffentliches UI-Interface oder Accessibility-Definition geführt werden. Ein eigenständiges Behavior-Artefakt ist damit möglich.
- **Bedeutung/Grenze:** Positiver Teilbefund; U für das vollständige Vier-Domänen-Paket. Die Spezifikation allein bestimmt nicht, wie die separat gewählten Originalformate und dieselben UI-Elemente ohne widersprüchliche Definitionen verbunden werden. Erweiterungsnamespaces lösen diese Ownershipfrage nicht von selbst.
- **Offene Frage / weiterer Bedarf:** Offene Frage: Welche Referenz-/Ereignisbindungen verbinden ein unverändertes SCXML-Verhaltensdokument mit den drei anderen Domänen, und bleiben dabei deren eigenen Validatoren und führenden Quellen erhalten? Keine Architekturentscheidung in diesem Schritt.

## C65

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft X02, X03; Bewertung **N**.
- **Befund:** §3.14 definiert innerhalb einer Session eindeutige IDs für SCXML-Elemente; für send/invoke können pro Ausführung neue IDs entstehen. §6 kennt URI-Dienstziele und invoke-IDs. Diese Kennungen adressieren Zustände, Sendevorgänge oder Dienste, nicht standardisierte UI-Elementinstanzen oder fremde Domänenknoten.
- **Bedeutung/Grenze:** N im SCXML-Kern für die hier verlangte UI-Elementidentität und domänenübergreifende semantische Referenz. Vorhandene IDs sind ein echter Teilbeitrag, aber eine state-ID ist nicht automatisch die Identität eines Inputs. URI-Syntax und fremder Inlineinhalt definieren keine gemeinsame UI-/Design-/Accessibility-Zielart.
- **Offene Frage / weiterer Bedarf:** Eine spätere Zuordnung müsste UI-Instanz, Teil-ID und Maschinen-/invoke-Identität ausdrücklich unterscheiden. Weder URN-Technik noch ein bestimmter Referenzresolver wird hier festgelegt.

## C66

**Fortschreibung der Gesamtprüfung:** Aktueller Befund [C408](#c408); der folgende Text dokumentiert den früheren Stand.

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft X04; Bewertung **U**.
- **Befund:** §6.4 definiert invoke mit src/content, eigener Dienstinstanz, id/idlocation, Parameterübergabe, Abbruch und Abschlussereignis. §6.4.3 legt für aufgerufene SCXML-Sessions die Initialisierung passender Datenvariablen und Kommunikation fest. §6.4.4 beschreibt logische Datentrennung.
- **Bedeutung/Grenze:** Starker positiver Teilbefund: wiederverwendbare Verhaltensmaschinen mit eigenem Instanzkontext und Lebenszyklus sind definiert. U bleibt für vollständige UI-Komponentenkomposition wie Overlay verwendet ScrollArea, weil Sichtstruktur, öffentliche UI-Schnittstelle, Elementidentität und deren Bindungen nicht durch invoke bestimmt werden. Weder vollständige UI-Komposition noch generelle Nichtunterstützung wird daraus abgeleitet.
- **Offene Frage / weiterer Bedarf:** Offene Frage: Reicht invoke als Behavior-Beitrag für die Komposition autonomer UI-Unterkomponenten, wenn Identitäts-, Interface- und Darstellungsbindungen separat vorliegen? Konkrete Interpreter-/Hostfähigkeiten und Mehrfachinstanzen werden ausdrücklich nicht getestet.

## C67

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft X05; Bewertung **N**.
- **Befund:** §6.4 erlaubt externe src-URIs für aufgerufene Dienste; §5.3 erlaubt externe Datenquellen. version=1.0 bezeichnet die SCXML-Sprache. Der Kern definiert keine bibliotheksbezogenen Versionsconstraints, Inhaltsintegrität oder Lockdatei-/Abhängigkeitsauflösung.
- **Bedeutung/Grenze:** N für eine eigenständige reproduzierbare Versionsbindung externer Teilmodelle im SCXML-Kern. Ein Host kann eine unveränderliche Quell-URI oder ein externes Locking wählen; das ist kein standardisierter SCXML-Versionsresolver. Dienstaufruf und Versionsmanagement bleiben unterscheidbar.
- **Offene Frage / weiterer Bedarf:** Keine externe Quelle wird zur Ausführung geladen. Später muss die konkrete Host-/Paketbindung für reproduzierbare Quellen ausdrücklich untersucht werden.

## C68

**E3-Fortschreibung:** [aktueller Befund C424](#c424); folgender Text ist der frühere Stand.

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft X06; Bewertung **D**.
- **Befund:** Anhang E verweist auf eigenständige W3C-XSD-Schemata. Der gelesene scxml.xsd-Driver bindet Core-, Data- und External-Module ein; scxml-strict.xsd bindet separate strengere Module ein. Anhang E unterscheidet ein lockeres Schema-1.0- und ein strengeres Schema-1.1-Set.
- **Bedeutung/Grenze:** D für das Beibehalten einer separaten originalen SCXML-Schemaprüfung. Anhang E ist informativ; das lockere Schema erzwingt ausdrücklich nicht sämtliche Spezifikationsbedingungen. A.1 verlangt zusätzliche syntaktische und datenmodellspezifische Regeln, A.2 fordert nicht bei jedem konformen Prozessor einen validierenden XML-Parser. Schemaerfolg und Interpreterkonformität sind daher verschieden.
- **Offene Frage / weiterer Bedarf:** Es wurde kein XSD-Validator oder Interpreter ausgeführt. Die vollständigen Schemaabhängigkeiten, insbesondere die strengeren Module, wurden nicht als ausführbare Validierungskette getestet.

## C69

- **Quellen:** [S09](SOURCES.md), [S26](SOURCES.md); E1 mit ergänzender XSD-Sichtprüfung E2. Betrifft X07, X08; Bewertung **N**.
- **Befund:** §3.11/§3.14/A definieren gültige Zustandskonfigurationen, IDs und Dokumentkonformität; §3.13/D definieren Transitionsauswahl und Ausführung. Die Regeln betreffen SCXML-Zustände und Ereignisse, nicht Ownership oder semantische Konflikte zwischen Interface-, Design-, Behavior- und Accessibility-Artefakten.
- **Bedeutung/Grenze:** N für die vollständige Paketkonfliktprüfung und domänenübergreifende führende Quelle im SCXML-Kern. Eigene Gültigkeits-/Prioritätsregeln bleiben vorhanden und müssen erhalten werden. Ein ungültiges Transitionziel oder ein Ausführungsfehler ist eine andere Prüfkategorie als widersprüchliche Tastatur- oder Darstellungsanforderungen fremder Domänen.
- **Offene Frage / weiterer Bedarf:** Keine neue Konfliktarchitektur entwerfen. Später zusätzliche Paketregeln getrennt von SCXML-Konformität und konkreten Interpreterdiagnosen prüfen.


# Vertiefung ausschließlich XState

Abgeschlossen am 24. Oktober 2026; Quellen am 23. Oktober gelesen. Alle 24 zuvor offenen Zellen betrachtet: 21 eingeordnet, X01/X04/X06 bleiben U. Zwei vorherige Bewertungen bleiben bestehen. Keine Installation, Ausführung oder Tests. D bezeichnet jeweils den begrenzten Actor-/Behavior-Beitrag, keine universelle UI-Vertragslösung.

## C70

- **Quellen:** [S28](SOURCES.md), [S29](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft G01; **D**.
- **Befund:** MachineConfig und StateNodeConfig definieren strukturierte Zustände, Übergänge und benannte Implementierungen.
- **Bedeutung/Grenze:** D für das dokumentierte Konfigurationsmodell, nicht für eine vollständig JSON-serialisierbare Maschine. Inlinefunktionen und externe Implementierungen bleiben ausführbarer JS/TS-Code.
- **Offene Frage / weiterer Bedarf:** Keine vollständige sprachneutrale Serialisierung behaupten; G02 bleibt A.

## C71

- **Quellen:** [S28](SOURCES.md), [S29](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft I01; **D**.
- **Befund:** setup.types.input deklariert typisierte Actor-Eingaben; createActor übergibt input, aus dem initialer context gebildet werden kann.
- **Bedeutung/Grenze:** D im begrenzten Actor-Interface: typisierte öffentliche Eingabefelder. Kein allgemeiner Vertrag für beliebige veränderliche UI-Properties und keine Runtime-Schemavalidierung.
- **Offene Frage / weiterer Bedarf:** Live-UI-Propertybindung separat untersuchen, wenn gefordert.

## C72

- **Quellen:** [S28](SOURCES.md), [S32](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft I02; **D**.
- **Befund:** setup.types.emitted deklariert eine öffentliche Eventunion einschließlich Payloadfeldern. emit erzeugt diese Ereignisse; actor.on hört darauf.
- **Bedeutung/Grenze:** D für getrennt typisierte ausgegebene Actor-Events. Interne events und öffentliche emitted sind unterscheidbar; Auslösepunkt und Typdeklaration sind getrennt. TypeScript-Typen sind keine Runtime-Payloadprüfung.
- **Offene Frage / weiterer Bedarf:** Eventreihenfolge und fachlicher Auslösezeitpunkt weiterhin ausdrücklich festlegen.

## C73

- **Quellen:** [S28](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft I03; **N**.
- **Befund:** StateNodeConfig definiert Zustandsknoten, invoke, transitions, tags und frei verwendbares meta; keine standardisierte UI-Anatomie mit Input, Popup oder Slots.
- **Bedeutung/Grenze:** N im untersuchten XState-Core. Zustandsnamen und meta geben UI-Teilen keine standardisierte Bedeutung.
- **Offene Frage / weiterer Bedarf:** Ein externer Anatomievertrag wäre ein gesonderter Beitrag.

## C74

- **Quellen:** [S28](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft V01, V02, V03, V04, V05, V06; **N**.
- **Befund:** Der gelesene Core-Konfigurationsumfang definiert kein Token-Typsystem, keine visuellen Stylevarianten oder Themeauflösung, Ankergeometrie, Flächenbegrenzung oder Overflow-Semantik.
- **Bedeutung/Grenze:** N für diese visuellen Anforderungen im Core. Ein Zustand dark oder Farbwerte im context beschreiben noch keine formale Gestaltung. Beliebiges meta ist kein vorhandener Visualstandard.
- **Offene Frage / weiterer Bedarf:** Externe Darstellung nicht pauschal dem Core zurechnen.

## C75

- **Quellen:** [S28](SOURCES.md), [S30](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft B02; **D**.
- **Befund:** Guards sind synchrone reine Funktionen mit booleschem Ergebnis; die erste erfüllte bewachte Transition kann gewählt werden. Actions sind Effekte bei Übergängen oder Eintritt/Austritt; benannte parametrisierte Implementierungen und eingebaute Aktionen sind dokumentiert.
- **Bedeutung/Grenze:** D für dokumentierte Ausführung samt konkreter JS/TS-Implementierung. Serialisierte Namen allein enthalten die Funktionssemantik nicht; Actions werden nicht als automatisch abgewartete asynchrone Aufgaben verstanden.
- **Offene Frage / weiterer Bedarf:** Sprachneutralität bleibt eingeschränkt; keine Übersetzung zu SCXML behaupten.

## C76

- **Quellen:** [S28](SOURCES.md), [S29](SOURCES.md), [S30](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft B03; **D**.
- **Befund:** context und Ereignispayloads werden von Guards/Actions verarbeitet; assign beschreibt Context-Updates. Initialer context kann pro Actor aus input erzeugt werden.
- **Bedeutung/Grenze:** D für Datenverarbeitung im XState-Ausführungsmodell. Die Semantik benutzerdefinierter Ausdrücke hängt von JS/TS ab.
- **Offene Frage / weiterer Bedarf:** Keine Laufzeitversuche durchgeführt.

## C77

- **Quellen:** [S30](SOURCES.md), [S31](SOURCES.md); E1. Betrifft B04; **A**.
- **Befund:** actor.send nimmt Ereignisse entgegen; invoke dokumentiert unter anderem eine DOM-Ereignisquelle über Host-/Bibliothekscode. Actions können Hosteffekte auslösen.
- **Bedeutung/Grenze:** A: Ein UI-Binding muss konkrete Tastatur-/Fokusereignisse auf Actor-Events und Fokusaktionen auf reale UI-Elemente abbilden. Keine universelle plattformneutrale Tastatur-/Fokusbindung im Core belegt.
- **Offene Frage / weiterer Bedarf:** Elementidentitäten, Eingabeabbildungen und Hostaktionen ausdrücklich definieren.

## C78

- **Quellen:** [S28](SOURCES.md), [S30](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft A01, A02, A03; **N**.
- **Befund:** Die gelesenen Core-Typen und Aktionsmodelle definieren keine Accessibility-Rollen-/Namensbeziehungen, verpflichtende Bedienmuster oder zugängliche dynamische Ansagen.
- **Bedeutung/Grenze:** N im Core; Effekte können eine Accessibility-Integration ausführen, liefern deren fachliche Regeln aber nicht selbst.
- **Offene Frage / weiterer Bedarf:** Externe Patternanforderungen und Plattformsemantik getrennt nachweisen.

## C79

- **Quellen:** [S28](SOURCES.md), [S29](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft X01; **U**.
- **Befund:** Eine XState-Verhaltensmaschine benötigt keine visuelle oder Accessibility-Datei. Eigenständiges Behavior ist möglich.
- **Bedeutung/Grenze:** Positiver Teilbefund; die vollständige Verbindung vier separat geführter Originalmodelle ist damit nicht nachgewiesen.
- **Offene Frage / weiterer Bedarf:** Offen: Welche Referenzbindungen erhalten unabhängige Validatoren und eindeutige führende Quellen aller vier Domänen?

## C80

- **Quellen:** [S28](SOURCES.md), [S31](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft X02, X03; **N**.
- **Befund:** Zustands-IDs adressieren Maschinenknoten; Actor-IDs/-Referenzen dienen Actor-Kommunikation und Lebenszyklen.
- **Bedeutung/Grenze:** N für standardisierte UI-Elementidentität und fachliche Verweise zwischen den vier Modellen. Eine Zustands-ID ist nicht automatisch eine Input-Instanz; meta liefert keine definierte Zielsemantik.
- **Offene Frage / weiterer Bedarf:** Eine spätere Abbildung muss UI-Teil, Komponenteninstanz, Actor und Zustand unterscheiden.

## C81

**Fortschreibung der Gesamtprüfung:** Aktueller Befund [C409](#c409); der folgende Text dokumentiert den früheren Stand.

- **Quellen:** [S28](SOURCES.md), [S31](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft X04; **U**.
- **Befund:** createActor erzeugt unabhängige Instanzen; invoke und spawn verwenden wiederverwendbare Actor-Logik mit eigenem Context und definierten Lebenszyklen. invoke folgt der Lebensdauer des aufrufenden Zustands.
- **Bedeutung/Grenze:** Starker Teilbeitrag für wiederverwendbare Verhaltensinstanzen. Vollständige UI-Komposition wie Overlay verwendet ScrollArea einschließlich Interface, Darstellung und Elementidentität ist noch nicht belegt.
- **Offene Frage / weiterer Bedarf:** Offen: Reicht Actor-Komposition als Behavior-Beitrag, wenn die übrigen Komponentenbindungen unabhängig beschrieben werden?

## C82

- **Quellen:** [S28](SOURCES.md), [S31](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft X05; **N**.
- **Befund:** invoke.src referenziert registrierte Actor-Logik oder ein Logic-Objekt. Die Maschinenversion ist Metadatum; der untersuchte Core definiert keine externe Bibliotheksauflösung mit Versionsconstraints und Inhaltsintegrität.
- **Bedeutung/Grenze:** N für einen Core-eigenen reproduzierbaren Resolver externer Fachmodelle. Ein Paketmanager kann JS-Abhängigkeiten pinnen; das ist ein gesonderter Mechanismus.
- **Offene Frage / weiterer Bedarf:** Keinen Paket-Lockmechanismus aus einem version-Feld ableiten.

## C83

**Historischer Befund; aktuelle Werkzeugfolgeprüfung: [C405](#c405).**

- **Quellen:** [S28](SOURCES.md), [S33](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft X06; **U**.
- **Befund:** TypeScript-Konfigurationstypen erlauben statische Prüfungen. StateMachine führt schemas als unknown. Persistierte Snapshots sind Zustandsdaten; sie ersetzen die separat benötigte Actor-Logik nicht.
- **Bedeutung/Grenze:** Typebene ist positiv belegt, ein unterstütztes originales Runtime-Schema für ein eigenständiges neutrales Contract-Artefakt dagegen nicht. schemas: unknown ist kein Nachweis eines Validators und auch kein Beweis seiner Nichtexistenz.
- **Offene Frage / weiterer Bedarf:** Offen: Welche offiziell unterstützte Artefakt-/Schemaform lässt sich unabhängig von ausführbaren Implementierungen validieren, und welche Semantik deckt sie ab?

## C84

- **Quellen:** [S28](SOURCES.md); E1 und ergänzende manuelle Typ-/Quelltextsichtprüfung E2. Betrifft X07, X08; **N**.
- **Befund:** Core-Typen und Ausführungsregeln betreffen Zustände, Events und Actors; sie definieren keine führende Quelle oder Konfliktprüfung fremder Interface-, Visual- und Accessibility-Artefakte.
- **Bedeutung/Grenze:** N für paketweite fachliche Referenz-/Konfliktprüfung und Ownership. Eigene Typ-/Zustandsregeln sind davon verschieden.
- **Offene Frage / weiterer Bedarf:** Zusätzliche Paketregeln erst aus nachgewiesenen Integrationsanforderungen ableiten.


# Vertiefung ausschließlich Zag

Am 24. Oktober 2026 wurden alle 25 zuvor offenen Zag-Zellen gegen offizielle Dokumentation und ausgewählte gepinnte Definitionen geprüft. 21 wurden eingeordnet; X01, X03, X04 und X06 bleiben U mit konkreter Frage. Die bisherige G02-Bewertung A bleibt unverändert. Untersuchungseinheit ist das Zag-Toolkit: generischer Core, konkrete Combobox und mitgelieferte Popper-/ScrollArea-/LiveRegion-Beiträge werden ausdrücklich unterschieden. Framework-Ausführung wurde exemplarisch im React-Quelltext gelesen; keine Vollprüfung aller Adapter. Kein Praxis-/Laufzeit-/Validatorversuch, keine Implementierung.

## C85

- **Quellen:** [S34](SOURCES.md), [S35](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft G01; **D**.
- **Befund:** Machine<T> und MachineSchema definieren initialState, states, on, Transitionen und Implementierungen als dokumentierte TypeScript-Konfiguration. createMachine nimmt diese Konfiguration entgegen.
- **Bedeutung/Grenze:** D für eine maschinenverarbeitbare Beschreibung des Behavior-Beitrags. MachineSchema ist eine TypeScript-Schnittstelle, kein nachgewiesenes JSON Schema. Funktionen in props, initialState, Context und Implementierungen bleiben Code.
- **Offene Frage / weiterer Bedarf:** Die bestehende G02-Bewertung A bleibt erhalten: frameworkunabhängig bedeutet hier keine sprachneutrale ausführbare Semantik.

## C86

- **Quellen:** [S36](SOURCES.md), [S37](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft I01, I02; **D**.
- **Befund:** ComboboxProps benennt unter anderem inputValue:string, value:string[], open:boolean und öffentliche Callbacks. onValueChange verweist auf ValueChangeDetails mit value und items, onInputValueChange auf inputValue und reason; weitere Details-Typen beschreiben Auswahl, Hervorhebung und Öffnung.
- **Bedeutung/Grenze:** D in der Rolle einer typisierten TS-Toolkit-API. Callbackname und strukturierte Payload sind unabhängig vom konkreten Aufrufpunkt deklariert; interne Maschinenereignisse werden nicht mit öffentlichen Callbacks gleichgesetzt. Keine Runtime-Payloadvalidierung und kein plattformneutraler Eventbus folgen daraus.
- **Offene Frage / weiterer Bedarf:** Komplexe generische Typen und spätere neutrale Abbildung weiterhin getrennt prüfen; keinerlei Callbacks ausgeführt.

## C87

- **Quellen:** [S36](SOURCES.md), [S38](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft I03, X02; **D**.
- **Befund:** combobox.anatomy.ts benennt input, control, content, positioner, item, label und weitere Teile. ElementIds und combobox.dom.ts bilden id/ids auf explizite Teil-IDs ab. Die Kompositionsdokumentation verlangt eindeutige Maschinen-IDs und beschreibt gemeinsam verwendete Teil-IDs.
- **Bedeutung/Grenze:** D für benannte UI-Teile und explizite Elementidentität im Webmodell. Mehrfachinstanz-Stabilität ist nur unter korrekter Vergabe eindeutiger IDs beabsichtigt und hier nicht praktisch belegt. IDs sind keine automatisch versionsstabilen domänenübergreifenden URNs.
- **Offene Frage / weiterer Bedarf:** Custom IDs über ids setzen; manuelles Überschreiben eines DOM-id kann Beziehungen brechen. Rendern fehlender Ziele bleibt gesondert zu prüfen.

## C88

- **Quellen:** [S39](SOURCES.md), [S40](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft V01; **D**.
- **Befund:** PositioningOptions typisiert gutter, shift und Achsenoffsets als Zahlen mit dokumentierter Abstandssemantik. Die Positionierung schreibt berechnete Dimensionen als CSS-Pixelwerte; ScrollArea liefert benannte Breiten-/Höhengrößen für Corner und Thumb.
- **Bedeutung/Grenze:** D als eng begrenzter Dimensionsbeitrag des mitgelieferten Web-Positionierungs-/Scrollmodells. Kein allgemeines Design-Tokenformat, kein Typografie-/Farbsystem und keine DTCG-Konformität werden behauptet. Die vorhandene Farb-CSS-Variable allein wäre kein umfassender Typnachweis.
- **Offene Frage / weiterer Bedarf:** Die Übertragung von Designsystem-Tokens in solche Dimensionsparameter ist nicht geprüft; Layoutsemantik bleibt webgebunden.

## C89

- **Quellen:** [S38](SOURCES.md), [S37](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft V02; **R**.
- **Befund:** Zag erzeugt dokumentierte data-part/data-scope- und Zustandsattribute wie data-highlighted, data-state und data-disabled. Die Styling-Anleitung zeigt deren Verwendung in separaten CSS-Selektoren mit konkreten Deklarationen.
- **Bedeutung/Grenze:** R über die dokumentierte Bindung benannter Teile/Zustände an ein externes CSS-Stylemodell. Zag liefert die Zustands-/Teilreferenz, CSS die strukturierten visuellen Werte. Keine eigenen fertigen Stylevarianten oder Tokenrezepte im Maschinenkern behaupten.
- **Offene Frage / weiterer Bedarf:** Eine neutrale Variantenbibliothek oder die Verbindung mit separat gewähltem DESIGN.md ist damit nicht nachgewiesen; diese offene Paketbindung ist X03.

## C90

- **Quellen:** [S35](SOURCES.md), [S38](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft V03; **N**.
- **Befund:** Die untersuchten Maschinen-/Konfigurationsmodelle definieren kein Themeverzeichnis mit Auswahl- oder Wertauflösungsregeln. Styling wird ausdrücklich dem Verbraucher überlassen.
- **Bedeutung/Grenze:** N für eine eigene Theme-/Dark-Mode-Semantik im untersuchten Toolkitkern. Dass die Anwendung externes CSS oder ein Designsystem mit Themes verwenden kann, wird nicht bestritten und nicht als Zag-eigenes Themeformat gezählt.
- **Offene Frage / weiterer Bedarf:** Andere Stylingwerkzeuge nicht ohne konkreten dokumentierten Beitrag in diese Spalte übernehmen.

## C91

- **Quellen:** [S37](SOURCES.md), [S39](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft V04; **D**.
- **Befund:** ComboboxProps.positioning referenziert PositioningOptions. placement, gutter/offset und getAnchorElement bestimmen Platzierung, Abstand und Anker. Die Combobox bindet Control beziehungsweise Trigger als Anker und Positioner als Floating-Ziel an getPlacement.
- **Bedeutung/Grenze:** D für definierte relative Web-Geometrie im gebündelten @zag-js/popper-Beitrag, der Floating UI nutzt. Die Bindung ist konkreter JS/DOM-Code, kein neutraler deklarativer Layoutstandard.
- **Offene Frage / weiterer Bedarf:** Kollisionen, Umplatzierung, variable Größen und Zielplattformübertragung bleiben praktisch ungeprüft; acht Pixel sind weiterhin nur Beispielwert.

## C92

- **Quellen:** [S39](SOURCES.md), [S37](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft V05; **D**.
- **Befund:** fitViewport und sizeMiddleware berechnen verfügbare Abmessungen anhand der definierten Boundary und overflowPadding. getPlacementStyles setzt bei fitViewport maxWidth auf --available-width und maxHeight auf --available-height; die Combobox verwendet die Floating-Styles am Positioner.
- **Bedeutung/Grenze:** D für eine formal bestimmte maximale verfügbare Fläche des Popups im Positionierungsmodell. Keine automatische Begrenzung auf fünf sichtbare Zeilen und kein vollständiges frei parametrierbares Größenregelwerk nachgewiesen.
- **Offene Frage / weiterer Bedarf:** Eine zusätzliche produktspezifische Zeilen-/Höhenbegrenzung und deren Zusammenspiel mit Content und Overflow müssten separat festgelegt werden.

## C93

- **Quellen:** [S40](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft V06; **D**.
- **Befund:** ScrollArea ist ein separates Maschinenpaket für einen Overflow-Viewport. getViewportProps setzt overflow:auto; API und Dokumentation definieren horizontale/vertikale Overflowzustände, Scrollposition, scrollTo und scrollToEdge.
- **Bedeutung/Grenze:** D im Web-ScrollArea-Beitrag; dieser gehört zum Toolkit, nicht zum generischen Zustandskern. Er liefert Scroll-/Overflowsemantik, jedoch weder die maximale Anzahl sichtbarer Zeilen noch eine nachgewiesene automatische Einbettung in ein fremdes Overlay.
- **Offene Frage / weiterer Bedarf:** Die Einbettung und Verantwortlichkeit zweier Komponenten ist X04; keine ScrollArea-Instanz oder Gerätetests ausgeführt.

## C94

- **Quellen:** [S34](SOURCES.md), [S35](SOURCES.md), [S37](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft B01, B02, B03; **D**.
- **Befund:** Machine/Transition definieren Zustände, Initialisierung, Ereignisziele, Guards, Actions und Effects; BindableContext sowie Params stellen Ereignis-/Kontextdaten bereit. Die gelesene React-Ausführung wählt die erste erfüllte Transition, führt benannte Implementierungen aus und behandelt Cleanup beim Verlassen. Konkrete Combobox-Guards und Aktionen sind vorhanden.
- **Bedeutung/Grenze:** D im ausführbaren JS/TS-Maschinenmodell einschließlich seiner Framework-Laufzeitbindung. Semantik ist durch Code definiert, nicht durch freie Namen allein. Die im React-Adapter gelesene Scheduling-/Effektreihenfolge wird nicht ohne Prüfung auf jeden Adapter verallgemeinert.
- **Offene Frage / weiterer Bedarf:** Kein SCXML-Anspruch: Die Einleitung grenzt sich ausdrücklich von SCXML ab. Die Erwähnung von XState in Paketmetadaten ist kein Kompatibilitätsnachweis. Keine Maschine ausgeführt.

## C95

- **Quellen:** [S37](SOURCES.md), [S35](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft B04; **D**.
- **Befund:** combobox.connect.ts bindet onFocus/onBlur/onChange und Tastaturereignisse ausdrücklich an Maschinenereignisse wie INPUT.FOCUS und INPUT.ARROW_DOWN. Fokusaktionen adressieren DOM-Elemente über Scope und Teil-IDs; IME-Komposition wird in der Tastaturbehandlung berücksichtigt.
- **Bedeutung/Grenze:** D für vorhandene Web-Eingabebindungen. connect liefert Props/Handler; normalizeProps und der Framework-Adapter übernehmen deren Form und Lifecycle, der Verbraucher muss die Props korrekt an gerenderte Elemente binden. Der generische Core allein liefert keine fertige UI.
- **Offene Frage / weiterer Bedarf:** Andere Frameworks und native Plattformen sind nicht praktisch geprüft. Die vorhandene Bindung ist kein sprachneutraler Eingabevertrag.

## C96

- **Quellen:** [S37](SOURCES.md), [S38](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft A01, A02; **D**.
- **Befund:** Die Combobox-Dokumentation referenziert das WAI-ARIA-APG-Comboboxmuster und beschreibt Tastaturinteraktionen. connect setzt konkrete Rollen und Beziehungen, darunter combobox/listbox/option, aria-expanded, aria-controls, aria-activedescendant und Label-IDs; DOM-Fokus bleibt entsprechend der gewählten Variante geführt.
- **Bedeutung/Grenze:** D als referenzierter Web-Pattern- und Implementierungsbeitrag. Die Behauptung vollständiger APG-Konformität des Projekts wurde nicht unabhängig praktisch bestätigt. Inhalt, Label und gerenderte Teile bleiben Verantwortung der Integration; benutzerdefinierte ids können fehlende DOM-Ziele referenzieren.
- **Offene Frage / weiterer Bedarf:** Keine allgemeine Accessibility-Konformität oder native Übertragbarkeit ableiten. Reale Tastatur-/Screenreader-Unterstützung und Produktprofil bleiben separat nachzuweisen.

## C97

- **Quellen:** [S37](SOURCES.md), [S41](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft A03; **D**.
- **Befund:** Combobox beschreibt Ergebnis-, Leer- und Ladeansagen. translations definiert die Texte/Funktion, loading beeinflusst Nachricht und aria-busy. Die Maschine ruft eine polite Ergebnisregion nach einem definierten Ruheintervall auf; @zag-js/live-region erzeugt aria-live/aria-atomic und role=status oder alert und ersetzt ausstehende Nachrichten.
- **Bedeutung/Grenze:** D für vorhandene, konkrete Web-Rückmeldungssemantik. Der gelesene Stand verwendet unter anderem 1000 ms für Ergebnisansagen; dies ist Implementierungsstand, keine universelle Produktpflicht. Echte Wahrnehmbarkeit mit assistiver Technik wurde nicht getestet.
- **Offene Frage / weiterer Bedarf:** Auslöser, Texte und Warteverhalten mit dem Produktprofil abstimmen; native Ansage-APIs und vollständige Screenreader-Konformität bleiben unbewiesen.

## C98

- **Quellen:** [S34](SOURCES.md), [S35](SOURCES.md), [S37](SOURCES.md), [S38](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft X01; **U**.
- **Befund:** Visuelle Styles können getrennt gepflegt werden, Maschinen und connect sind verschiedene Funktionen. Die mitgelieferten Maschinen-/connect-Dateien verbinden aber Behavior, DOM-Anatomie, Fokus, ARIA und teilweise Geometrie in ausführbarem Code.
- **Bedeutung/Grenze:** Teilweise Trennung ist positiv belegt; vier unabhängig beschreibbare Originaldomänen ohne erzwungene fremde Fachdefinitionen sind nicht nachgewiesen. Funktions-/Dateigrenzen sind keine vollständigen Domänengrenzen.
- **Offene Frage / weiterer Bedarf:** Offen: Kann Zag mit vier extern geführten Verträgen konsistent gebunden werden, ohne dass sein gebündeltes Fokus-/ARIA-/Geometrieverhalten zur zweiten führenden Quelle wird?

## C99

- **Quellen:** [S36](SOURCES.md), [S37](SOURCES.md), [S38](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft X03; **U**.
- **Befund:** Teil-IDs, Scope und Zustandsattribute binden UI-Teile, DOM-ARIA-Ziele und separate CSS-Regeln. Diese Mechanismen sind reale Teilbeiträge und werden nicht als fehlend bewertet.
- **Bedeutung/Grenze:** Ein gemeinsamer Referenzvertrag zu separat gewählten Interface-, Visual-, Behavior- und Accessibility-Originalartefakten ist damit nicht belegt. Ein CSS-Selektor oder DOM-id allein adressiert noch keinen typisierten Fachmodellknoten.
- **Offene Frage / weiterer Bedarf:** Offen: Welche explizite Zuordnung erhält Zielart, Versionsstand und Bedeutung zwischen vier externen Verträgen und den vorhandenen Teil-/Zustands-/Callbackbindungen?

## C100

**Fortschreibung der Gesamtprüfung:** Aktueller Befund [C410](#c410); der folgende Text dokumentiert den früheren Stand.

- **Quellen:** [S36](SOURCES.md), [S38](SOURCES.md), [S40](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft X04; **U**.
- **Befund:** Importierte Maschinen werden mit eigenen props/id über useMachine instanziiert. Die Kompositionsanleitung beschreibt zwei Maschinen mit gemeinsamem Trigger über ids und das Zusammenführen von Props. ScrollArea existiert als eigenständiges Toolkitpaket.
- **Bedeutung/Grenze:** Starker positiver Befund für echte wiederverwendbare UI-Maschinen und gemeinsame DOM-Teile. Ein deklarativ referenziertes Overlay mit unabhängiger ScrollArea samt Parametern, Ereignissen, eigenem Kontext und geklärten Fokus-/Scrollzuständigkeiten ist noch nicht nachgewiesen.
- **Offene Frage / weiterer Bedarf:** Offen: Lassen sich genau diese unabhängigen Komponentenbindungen mit Originalmodellen ausdrücken und prüfen, oder bleibt ihre Komposition nur imperativer Anwendungscode? Kein Kompositionsversuch ausgeführt.

## C101

- **Quellen:** [S35](SOURCES.md), [S36](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft X05; **N**.
- **Befund:** Die untersuchten Machine-/Service-Schnittstellen enthalten keine bibliotheksübergreifende versionierte Contract-Referenz oder deren Resolver. Maschinen werden aus JS-Paketen importiert; Paketmetadaten nennen Versionen und workspace-Abhängigkeiten.
- **Bedeutung/Grenze:** N für einen eigenen Resolver reproduzierbar versionierter externer Teilmodelle im untersuchten Toolkitvertrag. Paketmanager und Lockdateien können Softwareversionen sichern, ersetzen aber keinen Zag-eigenen Fachmodellresolver.
- **Offene Frage / weiterer Bedarf:** Keine allgemeine Nichtreproduzierbarkeit des Projekts behaupten; externe Paketverwaltung und Contract-Auflösung ausdrücklich unterscheiden.

## C102

**Historischer Befund; aktuelle Werkzeugfolgeprüfung: [C406](#c406).**

- **Quellen:** [S35](SOURCES.md), [S36](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft X06; **U**.
- **Befund:** MachineSchema und ComboboxProps sind echte TypeScript-Typen; Paketmetadaten nennen tsc --noEmit. createMachine baut einen Zustandsindex, der unter anderem doppelte Zustands-IDs und ungültige Initialknoten behandelt.
- **Bedeutung/Grenze:** Positiver Nachweis statischer Typen und einzelner interner Strukturprüfungen, jedoch kein ausreichender Nachweis eines originalen separaten Schemas/Validators für ein eigenständig gespeichertes Domänenartefakt. Die Bezeichnung Schema allein ist kein JSON-Schema-/Runtime-Validierungsnachweis.
- **Offene Frage / weiterer Bedarf:** Offen: Welches offiziell unterstützte Artefakt mit welchem Originalvalidator lässt sich unabhängig von Implementierungen prüfen, und welche Typ-/Referenz-/Semantikprüfungen umfasst das? Kein Typechecker oder Validator ausgeführt.

## C103

- **Quellen:** [S35](SOURCES.md), [S38](SOURCES.md); E1/E2 (Dokumentation und manuelle Definitionenprüfung, keine Ausführung). Betrifft X07, X08; **N**.
- **Befund:** Die definierten Core-Prüfungen betreffen Maschinenzustände; die Kompositionsdokumentation warnt ausdrücklich, dass konfigurierte ids auf nicht gerenderte DOM-Elemente zeigen können. Machine/Service und connect definieren keine führende Quelle oder Priorität zwischen vier externen Fachartefakten.
- **Bedeutung/Grenze:** N für vollständige paketweite Referenz-/Konfliktprüfung und domänenübergreifende Ownership im untersuchten Umfang. Interne Zustandsprüfungen bleiben vorhanden; Props-Merging und gemeinsame IDs beweisen keine Abweisung widersprüchlicher Accessibility-/Behavior-/Designregeln.
- **Offene Frage / weiterer Bedarf:** Zusätzliche Paketprüfung und Ownershipregeln wären eigenständige Integrationsarbeit; nicht aus DOM-Zielnamen oder einer erfolgreichen Typprüfung ableiten.


# Zentrale Integration: Google DESIGN.md und OpenUI

Stand 24. Oktober 2026. Grundlage sind zwei separate Rechercheberichte; ihre Einzelbewertungen wurden zentral gegen REQUIREMENTS/METHODS geprüft und wichtige Primärdefinitionen erneut gelesen. Beide vollständigen Formatspezifikationen, OpenUI-Interface/Schema-Beschreibung sowie Google Parser-/Modellgrenzen und der Linterpfad wurden abgeglichen. Berichtsinhalte sind keine eigenständigen technischen Primärnachweise. Keine Installation, Schemaausführung, Praxis- oder Laufzeitversuche. N gilt ausschließlich für die definierte Fachsemantik des geprüften Kerns, nicht für beliebige Erweiterungen oder natürlichsprachliche Anweisungen.

## C104

- **Kandidat / Anforderung:** Google DESIGN.md; G01; **D**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Design Tokens / Schema; PARSER, ParsedDesignSystem.
- **Befund:** Normative visuelle Werte besitzen YAML-Syntax in Frontmatter oder interleavten Codeblöcken; Blöcke werden zu einem Tokenbaum vereinigt.
- **Bedeutung/Grenze:** D im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Prosa bleibt informell.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C105

- **Kandidat / Anforderung:** Google DESIGN.md; G02; **D**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Token References; MODEL, ResolvedValue.
- **Befund:** Der visuelle Kern verwendet Werte, Einheiten und Pfadreferenzen ohne JS-/React-Funktionen. JS/TS implementiert nur die untersuchten Werkzeuge.
- **Bedeutung/Grenze:** D im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; CSS-Farb-/Längensemantik bleibt fachliche Bindung, kein Nachweis aller nativen Zieladapter.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C106

- **Kandidat / Anforderung:** Google DESIGN.md; I01; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Components / Component Property Tokens; MODEL, ComponentDef; PARSER, SCHEMA_KEYS.
- **Befund:** Components beschreibt Style-Property-Tokens, nicht öffentliche Komponentenparameter mit explizitem API-Typvertrag.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; typisierte visuelle Werte erfüllen I01 nicht. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C107

- **Kandidat / Anforderung:** Google DESIGN.md; I02; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Components; PARSER, ParsedDesignSystem; MODEL, ComponentDef.
- **Befund:** Kein öffentliches Event-/Payload-Modell im definierten Token-/Komponentenmodell.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; frei hinzugefügte Schlüssel erhalten keine Eventsemantik. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C108

- **Kandidat / Anforderung:** Google DESIGN.md; I03; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Components / Component Property Tokens; MODEL, ComponentDef.
- **Befund:** Komponentenbezeichner adressieren Stylegruppen; keine strukturierte Anatomie-/Partsdeklaration innerhalb einer Komponente.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; ein zusätzlicher Stylegruppenname ist noch keine Teilebeziehung. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C109

- **Kandidat / Anforderung:** Google DESIGN.md; V01; **D**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Token References / Typography / Layout / Shapes; MODEL, ResolvedValue.
- **Befund:** Farben, Typography, Spacing und Rounded besitzen definierte Werttypen/Einheiten; Referenzen auf zusammengesetzte Typographywerte sind in Components erlaubt.
- **Bedeutung/Grenze:** D im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; manuelle Quellprüfung, keine vollständige Konformitätsprüfung.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C110

- **Kandidat / Anforderung:** Google DESIGN.md; V02; **D**.
- **Quellen:** [S42](SOURCES.md), [S44](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Components / Variants; HANDLER, Phase 3 Build components.
- **Befund:** Benannte Stylegruppen wie button-primary-hover sind ausdrücklich als Varianten mit strukturierten Tokenwerten vorgesehen.
- **Bedeutung/Grenze:** D im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Auswahl erfolgt laut Spec durch Agenten, keine externe Maschinenzustandsbindung.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C111

- **Kandidat / Anforderung:** Google DESIGN.md; V03; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, vollständiges Schema / Colors / Components; PARSER, SCHEMA_KEYS; MODEL, DesignSystemState.
- **Befund:** Der definierte Kern hat Paletten und Varianten, aber kein Modus-/Theme-Auswahl- oder Overlayauflösungsmodell.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Farbname dark oder handgeführte zweite Datei erzeugt diese Semantik nicht. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C112

- **Kandidat / Anforderung:** Google DESIGN.md; V04; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Layout / Components / Component Property Tokens; MODEL, ComponentDef.
- **Befund:** Layoutstrategie wird als Prosa formuliert; Spacing ist ein Wertvorrat ohne Anker/Ziel/Richtung.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Tooltips-Prosa mit positioning definiert kein geometrisches Modell. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C113

- **Kandidat / Anforderung:** Google DESIGN.md; V05; **N**.
- **Quellen:** [S42](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Layout / Component Property Tokens / Consumer Behavior for Unknown Content.
- **Befund:** height/width sind Dimensionstokens, aber maxHeight, Flächenbegrenzung oder zeilenbasierte Höhenableitung besitzen im Kern keine definierte Geometriesemantik.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; unbekannter Propertyname wird höchstens akzeptiert, nicht semantisch spezifiziert. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C114

- **Kandidat / Anforderung:** Google DESIGN.md; V06; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Component Property Tokens; MODEL, DesignSystemState / ComponentDef.
- **Befund:** Kein formal definiertes Overflow-/Scrollmodell unter den Token- oder Component-Property-Typen.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Stylingwerte oder Scroll-Prosa sind kein Verhaltensmodell. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C115

- **Kandidat / Anforderung:** Google DESIGN.md; B01; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Components / Variants; MODEL, ComponentDef.
- **Befund:** Stylevarianten enthalten keine Initialzustände oder ereignisbestimmten Transition-Ziele.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; state in der Stylebeschreibung ist kein Automat. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C116

- **Kandidat / Anforderung:** Google DESIGN.md; B02; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Components; PARSER, ParsedDesignSystem; MODEL, DesignSystemState.
- **Befund:** Keine Guard-Auswertung oder Aktionsausführungssemantik im definierten Modell.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; natürlichsprachliche Do/Don't-Regeln sind keine Guards. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C117

- **Kandidat / Anforderung:** Google DESIGN.md; B03; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema; MODEL, ResolvedValue / DesignSystemState.
- **Befund:** Keine UX-Kontext-/Ereignisdatenverarbeitung; ResolvedValue beschreibt Designwerte.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; boolesche/numerische Komponentenwerte im Handler schaffen keine Datenlogik. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C118

- **Kandidat / Anforderung:** Google DESIGN.md; B04; **N**.
- **Quellen:** [S42](SOURCES.md), [S44](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Components / Component Property Tokens; HANDLER, Phase 3.
- **Befund:** Keine Tastatur-/Fokus-/Eingabezuordnung zu UX-Aktionen; der bekannte Components-Kern verarbeitet Stylewerte.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Agenteninterpretation ersetzt keine Bindungssemantik. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C119

- **Kandidat / Anforderung:** Google DESIGN.md; A01; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Components / Do's and Don'ts; MODEL, ComponentDef.
- **Befund:** Kein Modell zugänglicher Rollen, Namen oder Zielbeziehungen.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Kontrastempfehlung und -prüfung tragen nicht Rollen-/Beziehungssemantik bei. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C120

- **Kandidat / Anforderung:** Google DESIGN.md; A02; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, sämtliche Sections insbesondere Components / Do's and Don'ts; PARSER, SCHEMA_KEYS.
- **Befund:** Keine referenzierbaren Fokus-/Tastaturinteraktionsmuster im Kern.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; zusätzliche freie Guidelines wären informell. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C121

- **Kandidat / Anforderung:** Google DESIGN.md; A03; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Components; MODEL, DesignSystemState.
- **Befund:** Keine Live-Region-/Announcement- oder andere zugängliche Aktualisierungssemantik.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; WCAG-Kontrastprüfung ist anderer Teilbereich. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C122

- **Kandidat / Anforderung:** Google DESIGN.md; X01; **U**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Sections / Omitted / Consumer Behavior for Unknown Content; PARSER, ParsedDesignSystem.
- **Befund:** Visual kann separat geführt werden; zulässige ausgelassene Sections erzwingen keine UX-/API-Daten. Vollständige Bindung vier unabhängig geführter Originalmodelle ist hiermit noch nicht bewiesen.
- **Bedeutung/Grenze:** U im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; offen: externes Bindungsmodell ohne fachliche Umdefinition und ohne stillen Schemaumbau festlegen.
- **Offene Frage / weiterer Bedarf:** Welche externe Bindung verbindet vier unveränderte Originalmodelle ohne fachliche Umdefinition und doppelte führende Quellen?

## C123

- **Kandidat / Anforderung:** Google DESIGN.md; X02; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Token References / Components; MODEL, symbolTable / ComponentDef.
- **Befund:** Tokenpfade und Stylegruppenschlüssel identifizieren Werte/Definitionen, keine UI-Elemente oder Bindungs-IDs.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; keine Instanzidentität im begrenzten Modell. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C124

- **Kandidat / Anforderung:** Google DESIGN.md; X03; **N**.
- **Quellen:** [S42](SOURCES.md), [S44](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Token References; HANDLER, symbolTable / Phase 3.
- **Befund:** Der dokumentierte Referenzmechanismus zielt ausdrücklich auf einen Wert im selben YAML-Baum. Keine Adressierung separat geführter API-/Behavior-/A11y-Modelle.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; keine Aussage über eigene Integrationsschicht oder proprietäre Erweiterungen. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C125

- **Kandidat / Anforderung:** Google DESIGN.md; X04; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md), [S44](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Components; MODEL, ComponentDef; HANDLER, Phase 3.
- **Befund:** Components sind Property-Maps, ohne Definition/Use, Instanzkontext, Parameter oder Lebenszyklus für Unterkomponenten.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Tokenwiederverwendung ist keine Komponenteninstanziierung. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C126

- **Kandidat / Anforderung:** Google DESIGN.md; X05; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md), [S44](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema / Token References; PARSER, version / SCHEMA_KEYS; HANDLER, symbolTable.
- **Befund:** Lokale YAML-Pfade definieren keine externe Quelle oder reproduzierbare Versionsauflösung; version bezeichnet Dokumentformat.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; Repository-Pinning durch uns ist keine im Format vorhandene Abhängigkeitssemantik. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C127

**Historischer Befund; aktuelle Werkzeugfolgeprüfung: [C403](#c403).**

- **Kandidat / Anforderung:** Google DESIGN.md; X06; **U**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md), [S44](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Schema; PARSER, ParserInputSchema / ParsedDesignSystem; MODEL, VALIDATION HELPERS; LINT, lint; API, lint export.
- **Befund:** Offizieller Original-Linter kann das eigenständige DESIGN.md-Artefakt verarbeiten. Ein unabhängig veröffentlichtes vollständiges Originalschema ist durch gelesene Pseudostruktur, TS-Interfaces und Zod-Eingabeschema jedoch nicht nachgewiesen.
- **Bedeutung/Grenze:** U im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; offen: vollständiger Originalschema-Vertrag/Export und Umfang der Schema- gegenüber programmatischer Validierung. Kein N aus bloß fehlendem Schemafund.
- **Offene Frage / weiterer Bedarf:** Welcher vollständige eigenständige Originalschema-Vertrag/Export besteht, und welche Regeln prüfen Schema und programmatischer Linter jeweils?

## C128

- **Kandidat / Anforderung:** Google DESIGN.md; X07; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md), [S44](SOURCES.md); E2. Fundstelle im Primärquellenregister: README, Linting Rules; HANDLER, buildCollisionGuard / resolveReference; MODEL, DesignSystemState; LINT, lint.
- **Befund:** Original-Linter prüft interne Tokenziele, Typwerte und einige Kollisionen, führt aber weder fremde Domänenmodelle noch UI-Instanzkonflikte zusammen.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; interne gebrochene Tokenreferenzen sind positiver Teilbeitrag, keine Paketprüfung. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C129

- **Kandidat / Anforderung:** Google DESIGN.md; X08; **N**.
- **Quellen:** [S42](SOURCES.md), [S43](SOURCES.md); E2. Fundstelle im Primärquellenregister: SPEC, Einleitung Tokens normative / prose context; PARSER, SCHEMA_KEYS; MODEL, DesignSystemState.
- **Befund:** Lokal gilt ausdrücklich Tokenwert vor Prosa; darüber hinaus existiert im definierten Modell keine Ownership-/Änderungsnachverfolgung zwischen vier Originalformaten und Integration.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (Google DESIGN.md alpha am Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15). E1/E2; lokale Präzedenz erfüllt die gesamte paketweite Anforderung nicht. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Konkrete Formatgrenze festgehalten; keine Ausführung. Offene weiterführende Integrations-/Werkzeugfragen bleiben gesondert.

## C130

- **Kandidat / Anforderung:** OpenUI; G01; **D**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7, §8; F gesamtes Exportobjekt.
- **Befund:** Komponenten und Props besitzen dokumentierte YAML-/JSON-Datensyntax.
- **Bedeutung/Grenze:** D im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Maschinenlesbarkeit ist kein Beleg eines ausführbaren Validators. Bisherige D-Bewertung bleibt.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C131

- **Kandidat / Anforderung:** OpenUI; G02; **D**.
- **Quellen:** [S45](SOURCES.md); E1. Fundstelle im Primärquellenregister: S §6 Framework Agnosticism, §7–9.
- **Befund:** Der begrenzte Props-Kern enthält Typmetadaten, Default, Enum und Required, ohne ausführbare React-/JS-Funktionen zu verlangen; YAML und JSON sind explizit erlaubt.
- **Bedeutung/Grenze:** D im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Gilt für diesen fachlichen Kern, nicht universelle komplexe Typsemantik oder Codebeispiele; Zielcodeadapter unbewiesen.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C132

- **Kandidat / Anforderung:** OpenUI; I01; **D**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7 Prop-Tabelle; T `components.*.props`.
- **Befund:** Benannte öffentliche Props mit `type`, `description`, `default`, `enum`, `required` sind ausdrücklich beschrieben.
- **Bedeutung/Grenze:** D im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). T weicht ab: verlangt u.a. `group` und `license`, kennt kein enum/required und beschränkt default. Komplexe Typdurchsetzung nicht nachgewiesen. Bisherige D-Bewertung bleibt.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C133

- **Kandidat / Anforderung:** OpenUI; I02; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7, §10 Punkt Document Events; T und F vollständige Komponentenfelder.
- **Befund:** Im vollständig definierten Komponenten-/Propmodell fehlt eine eigene Zuordnung öffentlicher Eventnamen zu strukturierten Payloadfeldern. §10 empfiehlt lediglich Eventdokumentation.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). N nur für diese definierte Kernsemantik; freie Callback-Typstrings oder Prosa ersetzen keinen Payloadvertrag. Frühere U-Frage nach einem Modell im Repo jetzt gegen T/F abgeglichen. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C134

- **Kandidat / Anforderung:** OpenUI; I03; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7 Komponentenfelder; T/F `components` und `props`.
- **Befund:** Der Kern benennt Komponenten- und Propnamen, aber keine Anatomie-/Part-/Slotstruktur innerhalb einer Komponente.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Mehrere separat benannte Komponenten sind noch keine benannten Bestandteile oder anatomischen Beziehungen. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C135

- **Kandidat / Anforderung:** OpenUI; V01; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7 Prop-Tabelle; F vollständige Prop-Felder.
- **Befund:** Primitive Prop-Typen definieren keine typisierte Farb-, Dimensions-, Einheiten- oder Typografiesemantik.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Ein Prop namens color mit type string wäre zulässige Beschreibung, aber kein im Standard festgelegter Designwerttyp. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C136

- **Kandidat / Anforderung:** OpenUI; V02; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §9 variant/size; §7 vollständige Felder; F.
- **Befund:** Das Variant-Enum im Beispiel benennt Ausprägungen, verknüpft sie jedoch weder mit strukturierten Styles noch Tokenreferenzen.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Bietet API-Auswahlmetadaten, keine eigene Stylezuordnung pro Zustand. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C137

- **Kandidat / Anforderung:** OpenUI; V03; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7–9; F vollständiges Modell.
- **Befund:** Weder Theme-/Modeauswahl noch Werteauflösungsregeln sind im Kern definiert.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Website-eigene dark-CSS-Klassen und mögliche library Props sind keine Semantik dieses Austauschformats. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C138

- **Kandidat / Anforderung:** OpenUI; V04; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7; F vollständige Komponenten-/Propfelder.
- **Befund:** Kein Anker, Bezugsziel, Positionsmodell oder geometrisch definierter Abstand ist vorgesehen.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Freie Props dürfen Beziehungen beschreiben, deren Bedeutung muss jedoch zusätzlich festgelegt werden. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C139

- **Kandidat / Anforderung:** OpenUI; V05; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7; F vollständiges Modell.
- **Befund:** Kein formales Flächen-/Maximalhöhenmodell mit geometrischer Semantik ist definiert.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). maxHeight als beliebiger Propname wäre nicht standardisierte Layoutbedeutung. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C140

- **Kandidat / Anforderung:** OpenUI; V06; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7; F vollständiges Modell.
- **Befund:** Kein Overflow-/Scrollmodell ist im Contractkern definiert.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Die ScrollArea-Dependency der Website und deren Preview-CSS sind hiervon getrennt. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C141

- **Kandidat / Anforderung:** OpenUI; B01; **N**.
- **Quellen:** [S45](SOURCES.md); E1. Fundstelle im Primärquellenregister: S §11 Punkt Describing Component State and Lifecycle; §7.
- **Befund:** Zustände, Lifecycle und komplexes State-Management sind explizit zukünftige Erweiterungen; kein Zustands-/Transitionsmodell im aktuellen Kern.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Bestehende N-Bewertung bestätigt; keine Aussage zu späteren Entwürfen. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C142

- **Kandidat / Anforderung:** OpenUI; B02; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7, §11; F.
- **Befund:** Keine Guard-Auswertung oder Aktionsausführung im Kern; State-/Lifecycle-Unterstützung ist zukünftige Arbeit.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Prop-/Callback-Typstrings legen keine Auswertungssemantik fest. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C143

- **Kandidat / Anforderung:** OpenUI; B03; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7, §11; T/F.
- **Befund:** Kein Maschinenkontext, kein formal verarbeiteter Eventdatenraum und keine Datenverarbeitungssemantik definiert.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Defaultwerte sind öffentliche Prop-Metadaten, kein veränderbarer Verhaltenskontext. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C144

- **Kandidat / Anforderung:** OpenUI; B04; **N**.
- **Quellen:** [S45](SOURCES.md); E1. Fundstelle im Primärquellenregister: S §7, §10 Document Events, §11.
- **Befund:** Keine formale Zuordnung von Taste, Fokus oder Eingabe zu UX-Aktion/Maschinenereignis definiert.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Eventdokumentation ist Empfehlung; ein konkreter vorhandener Bindingmechanismus für A ist nicht belegt. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C145

- **Kandidat / Anforderung:** OpenUI; A01; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §10 Punkt Emphasize Accessibility; §7; F.
- **Befund:** Accessibility wird empfohlen, aber Rollen, Namen und zielgerichtete ARIA-/Native-Beziehungen erhalten im Kern kein eigenes Begriffs- oder Relationsmodell.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Accessibility-Properties können als gewöhnliche Props dokumentiert werden; ihre fremde Semantik ist kein dokumentierter normativer Referenzmechanismus (daher kein R). Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C146

- **Kandidat / Anforderung:** OpenUI; A02; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §10 Emphasize Accessibility; §7; F.
- **Befund:** Kein referenzierbares Fokus-/Tastaturmuster im spezifizierten Datenmodell.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Prosa-Guidelines bleiben möglich, aber kein formal adressierbares Bedienmuster gemäß Kriterium. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C147

- **Kandidat / Anforderung:** OpenUI; A03; **N**.
- **Quellen:** [S45](SOURCES.md); E1. Fundstelle im Primärquellenregister: S §7, §10 Emphasize Accessibility, §11 Complex UI Patterns.
- **Befund:** Kein definiertes Modell für zugängliche dynamische Rückmeldungen oder deren Auslöser/Inhalte.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). aria-live als beliebiger Propname reicht nicht als eigene Standardspezifikation dynamischer Rückmeldung. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C148

- **Kandidat / Anforderung:** OpenUI; X01; **U**.
- **Quellen:** [S45](SOURCES.md); E1. Fundstelle im Primärquellenregister: S §5 selbstenthaltende Datei, §7–8.
- **Befund:** Der Entwurf kann den einfachen Interfacebeitrag separat liefern; er beschreibt jedoch keine Integration vier unabhängig geführter Fachartefakte.
- **Bedeutung/Grenze:** U im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Offen: Kann ein Interfaceartefakt unverändert mit drei anderen Originalartefakten und einer expliziten Integrationsschicht verbunden werden, ohne Informationen doppelt zu führen? Kein Paketversuch durchgeführt.
- **Offene Frage / weiterer Bedarf:** Kann das Interfaceartefakt unverändert mit drei Originaldomänen und einer expliziten Integrationsschicht verbunden werden, ohne Doppelpflege?

## C149

- **Kandidat / Anforderung:** OpenUI; X02; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7; T/F `components` und `props`.
- **Befund:** Komponenten-/Propnamen sind Definitionsschlüssel; keine Elementinstanz-ID oder domänenübergreifend bindbare Instanzidentität.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Ein Komponentenname ist keine stabile Identität von Input und Overlay in mehreren Autocomplete-Instanzen. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C150

- **Kandidat / Anforderung:** OpenUI; X03; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7; F vollständige Felder.
- **Befund:** Kein referenztypisiertes Feld oder Auflösungsmodell für separat beschriebene Domänen definiert.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). package nennt optional ein Modul, aber kein Visual-/Behavior-/Accessibility-Ziel mit semantischer Zuordnung. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C151

- **Kandidat / Anforderung:** OpenUI; X04; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7 Komponentenmodell, §9 Beispiel; T/F.
- **Befund:** Collection unabhängiger Komponentendefinitionen, jedoch keine Instanziierungsrelation, eigene Parameterbindung oder Instanzkontexte.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). JSX im example ist ein undurchsichtiger String; Definitionen wie Button oder ScrollArea beweisen keine Contract-Komposition. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C152

- **Kandidat / Anforderung:** OpenUI; X05; **N**.
- **Quellen:** [S45](SOURCES.md); E1. Fundstelle im Primärquellenregister: S §7 Top-Level und package; §8 Discovery.
- **Befund:** `version` bezeichnet die Bibliothek/den Komponentensatz; `package` bezeichnet ein optionales Modul. Keine externe versionierte Teilmodellreferenz mit definierter Auflösung.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Bibliotheksversion allein ist keine Bindung aller referenzierten Inhalte. Website-package-lock nicht dem Contract zurechnen. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C153

**Historischer Befund; aktuelle Werkzeugfolgeprüfung: [C402](#c402).**

- **Kandidat / Anforderung:** OpenUI; X06; **U**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md), [S47](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §12 Validate; T vollständiges Interface; F vollständiges Schemaobjekt; Q Scripts/Dependencies; R.
- **Befund:** Eigene Interfacebeschreibung wäre separat führbar, doch kein kanonisches ausführbares Originalschema/Validator nachgewiesen. T und F sind unterschiedliche Definitionen.
- **Bedeutung/Grenze:** U im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Offen: Welches unveränderte offizielle Schema und welches Werkzeug validieren draft-01-Dokumente vollständig? Erst dessen Identität/Stand klären, dann gültige/ungültige Eingaben testen.
- **Offene Frage / weiterer Bedarf:** Welches kanonische Originalschema und welches verfügbare Werkzeug validieren draft-01 vollständig trotz der dokumentierten Definitionsabweichungen?

## C154

- **Kandidat / Anforderung:** OpenUI; X07; **N**.
- **Quellen:** [S45](SOURCES.md), [S46](SOURCES.md); E2. Fundstelle im Primärquellenregister: S §7–8, §10–12; F vollständiges Modell.
- **Befund:** Keine Paket-/Referenz-/Instanz- oder Konfliktprüfregeln zwischen vier Domänen definiert.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Die allgemeine Aufforderung zur Schema-Konformität ist keine domänenübergreifende Prüfung. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.

## C155

- **Kandidat / Anforderung:** OpenUI; X08; **N**.
- **Quellen:** [S45](SOURCES.md); E1. Fundstelle im Primärquellenregister: S §3 Ziel Efficiency, §5 selbstenthaltende Datei, §10 Keep Updated; §7.
- **Befund:** Zentrale Referenz ist ein Ziel; §10 verlangt Aktualität. Der Kern definiert jedoch weder Feld-Ownership noch Vorrang-/Synchronisationsregeln zwischen Originalformaten und Integration.
- **Bedeutung/Grenze:** N im ausdrücklich begrenzten Modell (OpenUI draft-01 am Commit 09d39b211dcaa2e227ed38e312c8822e193cfea9). Single-source-Ziel allein erfüllt keine dokumentierte Zuständigkeits-/Änderungssemantik für vier Fachquellen. Unbekannte Felder oder frei ergänzte Prosa erhalten dadurch keine definierte Fachsemantik. Fehlende Recherche allein wäre kein N.
- **Offene Frage / weiterer Bedarf:** Im definierten draft-01-Kern abgegrenzt; keine Aussage über künftige Versionen oder eigene Erweiterungen.


# Drei-Agenten-Runde: AgentsORG, UXSpec und Ark UI

Stand 24. Oktober 2026. Die drei getrennten Berichte wurden gegen den aktuellen 26-Zeilen-Katalog, vorhandene Bewertungen und die Quellenrollen abgeglichen. Schema, Werkzeug und Laufzeitnachweis bleiben getrennt. AgentsORG-Vorarbeit wurde gezielt gegengeprüft; UXSpec-Vorarbeit gesichert und vervollständigt; für Ark UI war kein früherer Webbericht belegt. E1/E2, keine E3. Keine Installation, Praxis-/Laufzeitversuche oder Implementierung. N bezieht sich ausschließlich auf den jeweils definierten untersuchten Kern, nie auf einen bloßen fehlenden Fund.

## C156

- **Kandidat / Anforderung:** AgentsORG; G01; **D**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§1–3,7; SCHEMA root. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** `.design` ist ein einzelnes Datenobjekt, bevorzugt YAML 1.2, JSON gleichwertig; konkrete Struktur und Schema existieren.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Prosa bleibt Kontext.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C157

- **Kandidat / Anforderung:** AgentsORG; G02; **D**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§1,7.3,11,13. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Normativer Visual-Kern benötigt keine JS-/React-Funktionen; Werte, Themes und Tokenpfade sind Daten.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; optionale shadcn-Integration und Pythonwerkzeuge getrennt; natürlichsprachliche Regeln sind keine formale Programmiersprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C158

- **Kandidat / Anforderung:** AgentsORG; I01; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§13.2–13.3; SCHEMA $defs.component / componentPropertyBag. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Components definiert Stylebags und Nutzungsmetadaten, keinen öffentlichen Parametervertrag mit API-Typmetadaten.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; visuelle Propertytypen erfüllen I01 nicht. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C159

- **Kandidat / Anforderung:** AgentsORG; I02; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§7,13; SCHEMA $defs.component. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Kein öffentlicher Eventname mit zugeordnetem strukturiertem Payloadvertrag im definierten Komponentenmodell.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Soundrollen und frei ergänzte Felder sind kein Event-API-Modell. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C160

- **Kandidat / Anforderung:** AgentsORG; I03; **D**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §13.1–13.2; SCHEMA $defs.component.properties.anatomy. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** `anatomy` ist eine strukturierte Liste benannter Slots innerhalb eines Komponentenfamilieneintrags.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; keine Aussage über instanzstabile Elementidentität.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C161

- **Kandidat / Anforderung:** AgentsORG; V01; **D**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §11.1–11.3; SCHEMA properties.tokens / $defs.tokenNode. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Definierte Color-, Dimension-, Typography-, Time-/Levelwerte und Tokenpfade; nackte Dimensionszahlen werden in bestimmten Gruppen als px interpretiert.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Schema ist teilweise permissiv und erzwingt nicht sämtliche Fachsemantik.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C162

- **Kandidat / Anforderung:** AgentsORG; V02; **D**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§13.1–13.3,13.5; SCHEMA $defs.component. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Varianten/Zustände werden deklariert und besitzen strukturierte Tokenbags; flache Geschwistereinträge ebenfalls zulässig.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; keine externe UX-Maschinenbindung.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C163

- **Kandidat / Anforderung:** AgentsORG; V03; **D**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §7.3; SCHEMA properties.themes. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Base-Tokens, benannte Mode-Overlays, pfadweises Überschreiben und aktive Auswahl via Präferenz/default sind definiert.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; CSS-Ausgabe und OS-/Toggleverhalten wurden nicht ausgeführt.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C164

- **Kandidat / Anforderung:** AgentsORG; V04; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§11,13.3,13A,21; SCHEMA rationale.layout / componentPropertyBag. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Layout liegt in rationale.layout-Prosa; Gap/Spacingwerte besitzen keine Anker-, Ziel- und Positionsbeziehung.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; unbekannte Eigenschaftsnamen sind keine Geometriesprache. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C165

- **Kandidat / Anforderung:** AgentsORG; V05; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §13.3,13A,21; SCHEMA componentPropertyBag. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Height/Width sind Werte, kein definiertes Maximalflächen-/Maximalhöhenmodell oder Ableitung aus sichtbaren Zeilen.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; content-max-Tokenname definiert keine geometrische Anwendung. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C166

- **Kandidat / Anforderung:** AgentsORG; V06; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§11,13–14,21; SCHEMA components/patterns. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Kein formal definiertes Overflow-/Scrollmodell unter den Kernfeldern und Propertytokens.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Scrollverbote für Sounds beschreiben keinen Scrollcontainer. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C167

- **Kandidat / Anforderung:** AgentsORG; B01; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §13.2; SCHEMA $defs.component. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** states listet Stylezustände, aber weder Initialzustand noch Ereignisübergangsziel sind spezifiziert.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Dokumentlebenszyklus bootstrap/refine/lock/evolve betrifft Vertragsbearbeitung, nicht UI-Zustandsautomaten. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C168

- **Kandidat / Anforderung:** AgentsORG; B02; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §15.2; SCHEMA properties.decisions. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** decisions hat first-match-Ordnung, die Bedingungen sind aber freie Strings/Objekte ohne definierte Ausdrucks- oder Aktionsausführungssemantik.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Designentscheidungen durch Agenten erfüllen das operationalisierte Guard-/Actionkriterium nicht. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C169

- **Kandidat / Anforderung:** AgentsORG; B03; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§13,15.2; SCHEMA properties.decisions. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Kein modellierter UX-Kontext oder Ereignisdatenzugriff; decisions beschreibt Designzuweisung, nicht Datenverarbeitung im Automaten.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Datencontainer oder Strings allein genügen nicht. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C170

- **Kandidat / Anforderung:** AgentsORG; B04; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§13,15; SCHEMA component/decisions/policy. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Keine strukturierte Bindung von Tastatur/Fokus/Eingaben an Maschinenereignisse oder UX-Aktionen im Kern.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Agentenanweisungen zu Eingaben sind keine explizite UI-Bindung. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C171

- **Kandidat / Anforderung:** AgentsORG; A01; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §15.1; SCHEMA properties.policy.properties.accessibility. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** policy.accessibility enthält Richtlinien, kein definiertes Rollen-/Namens-/Zielbeziehungsmodell.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; offener Objectcontainer und Kontrastwerte belegen das Kriterium nicht. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C172

- **Kandidat / Anforderung:** AgentsORG; A02; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §15.1–15.1.1; SCHEMA policy.accessibility. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** focus_visible und reduced_motion sind Richtlinien; kein referenzierbares komponentenspezifisches Fokus-/Tastaturinteraktionsmuster.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; optionale Craftverfahren ersetzen kein Muster im geprüften Formatkern. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C173

- **Kandidat / Anforderung:** AgentsORG; A03; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§11.6,15.1; SCHEMA policy/voice. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Kein definiertes Announcement-/Live-Region-Modell für zugängliche Aktualisierungen.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Sound-plus-visuelle-Rückmeldung und Fehlertextstil sind andere Teilbeiträge. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C174

- **Kandidat / Anforderung:** AgentsORG; X01; **U**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§7,21; SCHEMA required. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Eigenständiger Visualvertrag ohne erforderliche UI-Verhaltens-/API-Daten ist möglich; vollständige Bindung vier unverändert separat geführter Bereiche bleibt unbelegt.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; offen: Bindung zu externen Interface-/Behavior-/Accessibility-Artefakten konkret festlegen.
- **Offene Frage / weiterer Bedarf:** E1/E2; offen: Bindung zu externen Interface-/Behavior-/Accessibility-Artefakten konkret festlegen.

## C175

- **Kandidat / Anforderung:** AgentsORG; X02; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§13.1–13.2; SCHEMA $defs.component. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Anatomy benennt Slots, Komponentenkeys benennen Katalogdefinitionen; keine explizite UI-Instanz-/Element-Bindungs-ID.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Figma-Dateiidentität ist keine Elementidentität. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C176

- **Kandidat / Anforderung:** AgentsORG; X03; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§7.1–7.2,11.3; SCHEMA figmaIntegration/shadcnIntegration. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Definierte Tokenpfade adressieren Visualwerte im selben Dokument; Figma/shadcn-Brücken bilden Token-/Dateiwerte ab, keine separaten drei Domänenmodelle.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; lokale Komponentenreferenzwarnungen des Linters sind keine vierformatige semantische Zuordnung. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C177

- **Kandidat / Anforderung:** AgentsORG; X04; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§13.2,14,21; SCHEMA component/patterns. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Katalogimport und Pattern-Rezepte fördern Wiederverwendung, definieren aber kein Use/Instanzmodell mit eigenen Parametern und Kontext.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; import-Modulpfad ist keine Contract-Instanziierung. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C178

- **Kandidat / Anforderung:** AgentsORG; X05; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§4.1,7,18,23; SCHEMA properties.extends. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** extends definiert lokale Pfad-/Namensauflösung und Overlayreihenfolge, aber keine gebundene Abhängigkeitsversion; Remote/Registry optional.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; version bezeichnet aktuellen Vertrag; keine reproduzierbare Version des Referenzziels. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C179

- **Kandidat / Anforderung:** AgentsORG; X06; **D**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§3,19,24; SCHEMA root; LINT lint/main. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Eigenständiges `.design` kann unverändert gegen originales Draft-2020-12-Schema geprüft werden; Referenzlinter tut genau dies zusätzlich zu Fachprüfungen.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; Existenz und Codepfad belegt, kein Validatorversuch und keine Vollkonformitätsgarantie.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C180

- **Kandidat / Anforderung:** AgentsORG; X07; **N**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §19; LINT lint/resolve_path; SCHEMA root. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Interne Token-/Alias-/Tiefenprüfungen vorhanden, aber keine gemeinsame Prüfung fremder Domänenmodelle, UI-Instanzkollisionen oder domänenübergreifender Widersprüche.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1/E2; interne Prüfungen ausdrücklich positiver Teilbeitrag; extends-Zyklusprüfung wird normativ verlangt, im gelesenen Linter nicht implementiert. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C181

- **Kandidat / Anforderung:** AgentsORG; X08; **U**.
- **Quellen:** [S48](SOURCES.md#s48); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Fundstelle: SPEC §§1,5,7.1–7.4,17–18. Lokale Quellenkürzel des Befunds sind unter S48 aufgelöst.
- **Befund:** Starke vorhandene Regeln: `.design` repo-kanonisch, Tokens vor exportierten CSSwerten, Figma-Syncrichtung und Git-Audit. Übertragung auf unabhängige API-/Behavior-/A11y-Originale ist ungeklärt.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (AgentsORG am gepinnten Commit 014a1864c641f8e9792ed76de93c95493489dd8c). E1; offen: Ownership/Vorrang je Information über vier Bereiche ohne zweiten konkurrierenden Master definieren. Lokale Regeln werden nicht als vollständiger Paketnachweis ausgegeben.
- **Offene Frage / weiterer Bedarf:** Wie bleibt jede der vier Originalquellen führend, während .design Visualwerte, Exporte und Synchronisationsrichtungen bestimmt?

## C182

- **Kandidat / Anforderung:** UXSpec; G01; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** JSON-Autorformat mit maschinenlesbaren Feldern und Originalschema. S File Format/Top-Level; J vollständig; T UXSpecDocument.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Strukturierter Teilbeitrag, keine Gleichsetzung von akzeptierten freien Feldern und definierter Semantik. Bestehendes D erhalten.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C183

- **Kandidat / Anforderung:** UXSpec; G02; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Guards/Aktionen sind JSON-Kinds und S-Expressions mit dokumentierten Operatoren statt erforderlichen JS-Funktionen. S Actions, Effects, Dynamic Expressions; U.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Compiler TS/Node und Webrenderer React sind Werkzeug-/Adaptersprachen. Sprachneutrales Modell beweist keine identischen Ergebnisse in allen Zielsprachen; SCJSON-/SCXML-Kompatibilität bleibt Herstellerbehauptung ohne Konformitätsbeleg. Bestehendes D erhalten.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C184

- **Kandidat / Anforderung:** UXSpec; I01; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** `$context` benennt Felder mit sechs Typkategorien; `required:true` verlangt Versorgung durch den Host vor Start. S Context; J contextField; T ContextField.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Direkt für öffentliche Host-Eingaben/Initialdaten der Maschine, kein vollständiger Katalog beliebiger laufend setzbarer UI-Props. object/array sind keine tiefen Schemas. Werteprüfung separat.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C185

- **Kandidat / Anforderung:** UXSpec; I02; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** `$events` ist ein ausdrücklich deklarierter Katalog aller an die Maschine sendbaren Ereignisse, mit benannten typisierten Payload-Feldern und source; getrennt von transitions/onPress. S Events; J eventSpec; T EventSpec.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Öffentliche **eingehende** Maschinenereignisse; keine Behauptung eines eigenen ausgehenden Komponenten-Eventprotokolls. `emit` sendet laut S an dieselbe Maschine. Runtime-Payloadvalidierung nicht belegt.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C186

- **Kandidat / Anforderung:** UXSpec; I03; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Benannte `$elements`, `slots` und Element-`name` beschreiben strukturierte Teile/Anatomie. S Elements/Visual/Element References; J elementBase/visual; F.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Der Teil ist im UXSpec-eigenen visuellen Modell beschrieben; keine importierte CEM-Anatomie oder instanzglobale Identität daraus ableiten.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C187

- **Kandidat / Anforderung:** UXSpec; V01; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** `$tokens` beschreibt `$type`/`$value`, Dimensionen mit value/unit, Farben und Fonts; strukturierte Stylewerte. S Tokens/Token References; F Tokens; R Auflösung.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Eigene dokumentierte Werte genügen dem Teilkriterium; vollumfängliche DTCG-2025.10-Konformität nicht belegt. Schema `$tokens` nur object; Hex-Farbbeispiele nicht als Beleg aller normativen DTCG-Typen ausgeben.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C188

- **Kandidat / Anforderung:** UXSpec; V02; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** `interactions` definiert hover/focus/press/disabled als rein visuelle Style-Overrides; zustandsbezogene `$visual`-Blöcke besitzen Vererbung/Slotsersetzung. S Interaction States/Slot Inheritance; F; K mergeVisual.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). D erhalten. Keine eigenständige externe UX-Zuordnung daraus ableiten; X03 bleibt offen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C189

- **Kandidat / Anforderung:** UXSpec; V03; **N**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Der begrenzte v0.2-Kern definiert Tokens, Visuals, Zustandsvererbung und Interaktionsstile, aber keine Theme-/Modusauswahl oder kontextabhängige Tokenauflösung. S vollständige Struktur; J vollständige properties/defs; T.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Gilt für die definierten Mechanismen, nicht für die Unmöglichkeit einer Erweiterung. Unterschiedlich benannte dark-Tokens oder frei erlaubte Felder erfüllen keine Theme-Semantik. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C190

**Historischer Befund; aktuelle Folgeprüfung: [C397](#c397).**

- **Kandidat / Anforderung:** UXSpec; V04; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Layoutprimitiven stack/grid/layer und offene container-/Elementobjekte sind belegt; ein normatives Anker-Ziel-Richtung-Abstand-Modell wurde nicht gefunden. S Layout/Visual; J visual.container/elementBase; W.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Konkrete Frage: Welche originale dokumentierte Eigenschaft bindet ein Overlay geometrisch an ein benanntes anderes Element, mit Einheiten/Auflösung? Freie Felder und CSS des Webadapters reichen nicht für D; fehlender Fund allein führt nicht N.
- **Offene Frage / weiterer Bedarf:** Konkrete Frage: Welche originale dokumentierte Eigenschaft bindet ein Overlay geometrisch an ein benanntes anderes Element, mit Einheiten/Auflösung? Freie Felder und CSS des Webadapters reichen nicht für D; fehlender Fund allein führt nicht N.

## C191

**Historischer Befund; aktuelle Folgeprüfung: [C398](#c398).**

- **Kandidat / Anforderung:** UXSpec; V05; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Dimensionen und Elementgrößen sind strukturiert möglich; kein ausreichender Originalnachweis für formale maximale Höhe/Fläche. S/F; J offene Visualfelder; W mapSize.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Welche originale Regel definiert maxHeight/max-area einschließlich Einheit/Bezug? Beliebiges zulässiges JSON-Feld ist keine bestätigte Semantik; fünf Zeilen/variable Zeilenhöhe nicht bewiesen.
- **Offene Frage / weiterer Bedarf:** Welche originale Regel definiert maxHeight/max-area einschließlich Einheit/Bezug? Beliebiges zulässiges JSON-Feld ist keine bestätigte Semantik; fünf Zeilen/variable Zeilenhöhe nicht bewiesen.

## C192

**Historischer Befund; aktuelle Folgeprüfung: [C399](#c399).**

- **Kandidat / Anforderung:** UXSpec; V06; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Containerlayout und freie Zusatzfelder sind vorhanden; neutrale Overflow-/Scrollsemantik ist in den geprüften normativen Definitionen nicht hinreichend belegt. S Layout/Element Types; J; W.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Welche originale Definition spezifiziert clip/scroll/auto und Scrollcontainer? Weboverflow oder erfundene Zusatzfelder nicht ohne dokumentierte Formatsemantik zurechnen.
- **Offene Frage / weiterer Bedarf:** Welche originale Definition spezifiziert clip/scroll/auto und Scrollcontainer? Weboverflow oder erfundene Zusatzfelder nicht ohne dokumentierte Formatsemantik zurechnen.

## C193

- **Kandidat / Anforderung:** UXSpec; B01; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Machine id/initial/states, verschachtelte Zustände und event→target-Übergänge sind definiert. S Machine/Transitions; J; K.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Bestehendes D erhalten; kein SCXML-Kompatibilitätsnachweis.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C194

- **Kandidat / Anforderung:** UXSpec; B02; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Definierte Guard-Ausdrücke, Operatoren, assign/emit/log und Entry/Exit-Ausführungsreihenfolge; benannte Effects mit Lebenszyklusanforderungen. S Actions/Effects/Transitions/Entry/Exit/Invoke; U; V.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Bestehendes D für dokumentierte Semantik erhalten. Nicht behaupten, alle Compiler-/Runtimepfade erzwingen jede normative Regel; insbesondere compile ruft validateSpec nicht auf.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C195

- **Kandidat / Anforderung:** UXSpec; B03; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** context.*, event.* und binding mit Ausdrücken sowie assign sind beschrieben. S Context/Events/Binding/Dynamic Expressions; U.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Bestehendes D erhalten. Event- und Context-Typdeklaration ist keine bewiesene Runtime-Typprüfung.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C196

- **Kandidat / Anforderung:** UXSpec; B04; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** `$visual.keyboard` ordnet Tasten Ereignissen zu; onEnter.focus, focus-effect, onPress/onChange bilden Eingaben auf Aktionen/Ereignisse ab. S Visual/Effects/Runtime Properties; F/U.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Bestehendes D erhalten. Keyboard/Fokus befinden sich teils im Visualblock; ihre getrennte führende Fachquelle und externe Bindung sind nicht dadurch gelöst.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C197

- **Kandidat / Anforderung:** UXSpec; A01; **R**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** `aria` hat ausdrücklich auf ARIA-Attribute abgebildete Schlüssel, z.B. label. S Element Runtime Properties; U; J elementBase.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Referenz auf **externe ARIA-Websemantik**, kein eigenes Rollen-/Relationsschema und kein Nachweis gültiger Kombinationen oder Native-A11y-Abbildung. Für konkrete Rollen/Relationen muss die WAI-ARIA-Quelle separat maßgeblich bleiben; generisches object allein wäre ungenügend, hier ist die Attributzuordnung ausdrücklich dokumentiert.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C198

- **Kandidat / Anforderung:** UXSpec; A02; **N**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Tastenzuordnung/Fokusaktionen sind im Kern Mechanismen für Verhalten; das definierte Modell enthält keinen referenzierbaren APG-/A11y-Patternvertrag mit Anforderungen an Bedienung und Fokus. S vollständige Runtime-/Visualbegriffe; J/T.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). N für Pattern-Anforderungsmodell, nicht für die Möglichkeit zugänglicher Implementierungen. B04 nicht doppelt als Erfüllung von A02 zählen. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C199

- **Kandidat / Anforderung:** UXSpec; A03; **R**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Dokumentiertes aria-Beispiel `live:polite` verweist auf zugängliche ARIA-Aktualisierungssemantik. S Element Runtime Properties; U.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Referenzbeitrag für Web, kein vollständiger Live-Region-Workflow: Auslöser, Inhalt, Regionidentität, Zeitpunkt und Screenreaderverhalten gesondert bestimmen. Kein Renderer-/AT-Test.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C200

- **Kandidat / Anforderung:** UXSpec; X01; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Originalschema verlangt top-level `$schema`/`$description`/`$machine`; `$visual` ist auf machine und stateNode optional. Behavior ohne Visual ist daher **auf Schemaebene** möglich. J machine/stateNode; K mergeVisual mit undefined.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Vier unabhängige Fachartefakte samt neutraler Interface-/A11y-Bindung bleiben ungeklärt. Keine falsche Aussage „UXSpec erzwingt Visual im Behavior“; auch reine Token-/Visualdateien ohne `$machine` wären nicht selbst schema-konforme UXSpec-Rootdokumente.
- **Offene Frage / weiterer Bedarf:** Vier unabhängige Fachartefakte samt neutraler Interface-/A11y-Bindung bleiben ungeklärt. Keine falsche Aussage „UXSpec erzwingt Visual im Behavior“; auch reine Token-/Visualdateien ohne `$machine` wären nicht selbst schema-konforme UXSpec-Rootdokumente.

## C201

- **Kandidat / Anforderung:** UXSpec; X02; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** testId ist ausdrücklich als stabiler Testidentifier definiert, auf Web data-testid oder Plattformäquivalent abzubilden; name/focus.target ermöglichen Elementbezug. S Runtime Properties; J; K collectTestIds.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). D erhalten für explizite Kennzeichnung. Compiler dedupliziert identische testIds für Assertions; das ist keine Abweisung instanzübergreifender Kollisionen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C202

**Weitere E3-Fortschreibung:** [C426](#c426) ergänzt die tatsächliche Folgeprüfung; der folgende Text ist ein früherer Stand.

- **Kandidat / Anforderung:** UXSpec; X03; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Aliasqualifizierte Imports erschließen getrennte Token-/Element-/Maschinenquellen; konkrete Namensauflösung in I/R. S/F Referenzen, M Composability, J imports.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Starker Teilbefund, aber bisher UXSpec-eigene Teile: kein ausreichender Nachweis, dass Ziele in **separaten originalen Interface-/Visual-/Behavior-/A11y-Domänen** semantisch adressiert werden. Welche Originalartefakte/Bindungen bleiben unverändert? Tokenreferenz allein erfüllt X03 nicht.
- **Offene Frage / weiterer Bedarf:** Starker Teilbefund, aber bisher UXSpec-eigene Teile: kein ausreichender Nachweis, dass Ziele in **separaten originalen Interface-/Visual-/Behavior-/A11y-Domänen** semantisch adressiert werden. Welche Originalartefakte/Bindungen bleiben unverändert? Tokenreferenz allein erfüllt X03 nicht.

## C203

**Weitere E3-Fortschreibung:** [C430](#c430) ergänzt die tatsächliche Folgeprüfung; der folgende Text ist ein früherer Stand.

- **Kandidat / Anforderung:** UXSpec; X04; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** `$elements` plus `$ref` trennen Definition/Verwendung, params/$bind und Instanz-Overrides sind konkret; R substituteParams/expandRefs. Zusätzlich machineInvoke mit src/id/input/onDone in J/T und I/K/B, Beispiel E.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Bestehendes D für parametrisierte Komponenten-/Elementinstanzen erhalten; keine Behauptung autonom funktionierender ScrollArea-Runtime. Separater Instanzkontext/Lebenszyklus und UI-Anatomie sind bei einer komplexen Unterkomponente weiter zu prüfen. Ein vollständiger Child-Machine-Renderer ist damit nicht nachgewiesen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C204

- **Kandidat / Anforderung:** UXSpec; X05; **N**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Definierte Importfelder sind from + boolesche Teilimporte; I löst from über lokalen node:path relativ zur Dokumentdatei auf und liest JSON. Kein Versions-/Hash-/Lockfeld und keine solche Auflösung im geprüften Importkern J/T/I.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). N eng auf reproduzierbare externe Abhängigkeitsbindung im Originalkern. Ein Git-gepinntes Gesamtverzeichnis kann außerhalb des Formats Reproduzierbarkeit liefern, wäre eine zusätzliche Paketkonvention. `$version:0.2` der Ausgabe ist Formatversion. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C205

**E3-Fortschreibung:** aktueller Befund [C418](#c418); folgender Text dokumentiert den früheren Stand.

- **Kandidat / Anforderung:** UXSpec; X06; **D**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Eigenes unverändertes JSON Schema Draft 2020-12 existiert. Ein separat geführtes Behaviorartefakt ohne Visual kann an dessen Root-/Machine-Schema geprüft werden. J; S.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Direkter Schema-Beitrag, **nicht** Vollabdeckung aller vier Originalvalidatoren. Original-CLI ist ein anderer semantischer Prüfer und lädt J nicht. Tatsächlicher allgemeiner JSON-Schema-Validator wurde nicht ausgeführt; kein E3.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C206

- **Kandidat / Anforderung:** UXSpec; X07; **N**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Originalwerkzeuge prüfen ausgewählte interne Ziele/Operatoren/Referenzen. J/T/V/R/I/K/B definieren kein Vier-Domänen-Konfliktmodell mit Typkompatibilität, ID-Kollisionen und widersprüchlichen Fachanforderungen.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). N nur für die Paketanforderung. Nicht behaupten „keine Referenzprüfung“: Token-/Element-/Zustands-/Importprüfungen sind vorhanden. Deduplizieren von Assertions und Überschreiben von Modulen ist keine Kollisionsabweisung. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C207

- **Kandidat / Anforderung:** UXSpec; X08; **N**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** README nennt ein einziges UXSpec-Dokument als führende Quelle. Originalmodell und Import-Overrides definieren keine Feld-Ownership/Vorrang-/Änderungssynchronisation zwischen vier externen Fachquellen. S/J/T/M, K/R.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). N für vierfaches Ownershipmodell. Lokale Child-/Instanz-Override-Regeln sind belegt, genügen aber nicht der Paket-Governance. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C208

- **Kandidat / Anforderung:** Ark UI; G01; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR05/AR06, E2: strukturierte TS-Props/Emits sowie generiertes JSON mit Teilen, Typen, Defaults und Pflichtangaben. Maschinenlesbarer Interface-Teilbeitrag, kein vollständiges neutrales JSON-Laufzeitmodell.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C209

- **Kandidat / Anforderung:** Ark UI; G02; **A**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR04/AR05/AR06, E1/E2: JS-Frameworkhooks, Funktionen, DOM-/Collectionobjekte und Zag-Ausführung. Die vorhandenen Props-/Event-Metadaten wären ein konkreter Extraktions-/Bindungsansatz; zusätzliche neutrale Beschreibung und Zieladapter nötig. Keine automatische Portierung nach Swift oder Angular nachgewiesen.
- **Bedeutung/Grenze:** A im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C210

- **Kandidat / Anforderung:** Ark UI; I01; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR05/AR06, E1/E2: benannte Props etwa open:boolean, value:string[], collection:ListCollection<T>, Pflichtmetadaten. TS-Compiletime und Typstrings nicht mit Laufzeitvalidierung verwechseln; generische Items verlangen konkrete Typisierung.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C211

- **Kandidat / Anforderung:** Ark UI; I02; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR06/AR08, E2: Vue RootEmits: valueChange mit ValueChangeDetails<T>, inputValueChange mit InputValueChangeDetails, openChange mit OpenChangeDetails; zugehörige Felder value/items, inputValue/reason, open/reason/value im Zag-Typ. React bietet entsprechende typisierte on...-Callbacks. Deklaration getrennt von Aufrufstellen. Frameworkabhängige Namen, kein gemeinsamer neutraler Eventkatalog.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C212

- **Kandidat / Anforderung:** Ark UI; I03; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR05/AR06, E1/E2: benannte Root, Label, Control, Input, Positioner, Content, Item usw.; API-JSON pro Teil; comboboxAnatomy erweitert Zag-Anatomie um empty. Keine Gleichsetzung von Partname und Instanz-ID.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C213

- **Kandidat / Anforderung:** Ark UI; V01; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR08, E1/E2: vorhandenes PositioningOptions-Modell und dimensionierte CSS-Variablen als konkreter geometrischer Wertebeitrag. Stylingwerte für Farben/Typografie kommen aus externem CSS; kein eigener allgemeiner Design-Token-Typenkatalog. D wäre nur für die angebotenen Geometrieparameter begründbar, nicht für komplette Designwerte.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C214

- **Kandidat / Anforderung:** Ark UI; V02; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR01/AR02, E1: benannte Teile/Zustände über data-scope/data-part/data-state an separate CSS-Selektoren mit strukturierten Deklarationen gebunden. CSS liefert Styles, Ark liefert benannte Zustands-/Teilbindung. Keine eigene Recipe-/Variantensprache und kein externer UX-Contract-Mappingbeweis.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C215

- **Kandidat / Anforderung:** Ark UI; V03; **N**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR01/AR04/AR05/AR06, E1/E2: definierter headless Kern liefert Funktionsstyles und Stylinghooks, überlässt Präsentation externer Lösung. Keine eigene Theme-/Dark-Mode-Auswahl-/Auflösung im geprüften API-/Adaptermodell. Externe CSS-/Designsystemthemes bleiben möglich.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C216

- **Kandidat / Anforderung:** Ark UI; V04; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR05/AR08, E1/E2: positioning-Prop geht an Zag; getAnchorElement/AnchorRect, placement, gutter/offset, Positioner und Control/Trigger als Standardanker. Vorhandenes Web-Popper-Zielmodell statt eigener sprachneutraler Geometriesprache. Keine praktische Positionsmessung.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C217

- **Kandidat / Anforderung:** Ark UI; V05; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR08, E1/E2: dokumentierte --available-height/--available-width und max-height:calc(...) in separatem CSS, außerdem referenziertes fitViewport. Formale Web-Flächenbegrenzung per CSS/Popper; exakt fünf variable Zeilen dadurch nicht automatisch definiert.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C218

- **Kandidat / Anforderung:** Ark UI; V06; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR03/AR07/AR08, E1/E2: eigenständige ScrollArea-Wrappingkette bis getViewportProps, `overflow:auto`, Achsen, Overflow-/Scrollbarzustände. Kein Neutralformat; die notwendige geometrische Begrenzung und dokumentierte Zusatzstyles müssen im Produkt ergänzt werden.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C219

- **Kandidat / Anforderung:** Ark UI; B01; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR01/AR05/AR08, E1/E2: konkrete Referenz auf combobox.machine mit initialState sowie closed/open-Subzuständen und ereignisbestimmten targets. Ark selbst ist kein Maschineneditor oder allgemeiner Statechart-Contract.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C220

- **Kandidat / Anforderung:** Ark UI; B02; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR05/AR08, E2: referenzierte Maschine enthält tatsächliche Guards/Actions, etwa openOnChange, restoreFocus, setInputValue und invokeOnOpen; nicht nur freie Namen. Ausführungssemantik kommt aus Zag/JS. Keine SCXML-Kompatibilität daraus ableiten.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C221

- **Kandidat / Anforderung:** Ark UI; B03; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR05/AR08, E2: useMachine erzeugt Service mit Props; referenzierte Maschine bindet value/inputValue/highlightedValue, verarbeitet Eventdaten und ruft typisierte öffentliche Callbackdetails auf. Gemeinsame portable Event-/Contextsprache nicht belegt.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C222

- **Kandidat / Anforderung:** Ark UI; B04; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR05/AR08, E1/E2: Ark Input integriert getInputProps samt onFocus/onBlur/onChange/onKeyDown; ArrowDown/Enter/Escape werden konkret in Maschinenereignisse übersetzt. Ark stellt diese Web-/Frameworkbindung bereit; keine Nachweise zu nativen Eingabesystemen.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C223

- **Kandidat / Anforderung:** Ark UI; A01; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR03/AR05/AR08, E1/E2: getInputProps/Label/Content-Verkettung liefert role=combobox, aria-controls/expanded/activedescendant/labelledby; Field ergänzt aria-describedby. ids-Sharing dokumentiert. Korrekte Elemente und Inhalte bleiben verantwortlich zu wählen, asChild kann Semantik beschädigen. Keine getestete Konformität.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C224

- **Kandidat / Anforderung:** Ark UI; A02; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR05/AR08, E1/E2: expliziter referenzierbarer APG-Combobox-Verweis und eigene Keyboard-Tabelle; Bindung im gerenderten Input belegt. Das erfüllt das Musterteilkriterium, nicht vollständige normative oder plattformübergreifende Konformität.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C225

- **Kandidat / Anforderung:** Ark UI; A03; **R**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR05/AR08, E1/E2: translations wird an die referenzierte Maschine gegeben; resultsCount/noResults und polite Ergebnisregion mit verzögerter Ansage sind dort definiert, Highlightansage separat assertive/Apple-bedingt. Produkttexte, Trigger und Sprachen explizit festlegen. **Wichtige Grenze:** der gelesene Ark React Root-Split enthält loading nicht, obwohl der aktuelle Zag-Typ loading kennt. Deshalb keine ungeprüfte Garantie einer durch <Combobox.Root loading=...> gesteuerten Ladeansage. Der direkte Hook nimmt Zag-Props an; seine tatsächliche Laufzeit wurde nicht getestet.
- **Bedeutung/Grenze:** R im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C226

- **Kandidat / Anforderung:** Ark UI; X01; **U**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR01/AR05/AR08, E1/E2: externe Präsentation kann getrennt bleiben; Fokus, ARIA, UX und funktionale Geometrie sind in der ausführbaren Integration gekoppelt. Offen: Wie werden vier unabhängig führende externe Domänen ohne widersprechende zweite Definition gebunden?
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** AR01/AR05/AR08, E1/E2: externe Präsentation kann getrennt bleiben; Fokus, ARIA, UX und funktionale Geometrie sind in der ausführbaren Integration gekoppelt. Offen: Wie werden vier unabhängig führende externe Domänen ohne widersprechende zweite Definition gebunden?

## C227

- **Kandidat / Anforderung:** Ark UI; X02; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR02/AR03/AR05/AR07, E1/E2: explizite id/ids für Elemente, React useId als Default, dokumentiertes Sharing zwischen Tooltip-Trigger und Avatar-Root. Keine Garantie dauerhafter Identität über Neustarts, Umordnung, SSR oder mehrere unabhängige Roots; stabile Contract-IDs müssten explizit vergeben werden.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C228

- **Kandidat / Anforderung:** Ark UI; X03; **U**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR01/AR03/AR05/AR06, E1/E2: IDs verbinden Komponenten und ARIA-Ziele; Part-/Stateattribute verbinden CSS. Offen: Wie adressiert Ark ein Ziel in einem separat definierten neutralen Interface-/UX-/A11y-Vertrag mit überprüfbarer semantischer Zuordnung? DOM-IDs und Importe reichen als Nachweis dafür nicht.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** AR01/AR03/AR05/AR06, E1/E2: IDs verbinden Komponenten und ARIA-Ziele; Part-/Stateattribute verbinden CSS. Offen: Wie adressiert Ark ein Ziel in einem separat definierten neutralen Interface-/UX-/A11y-Vertrag mit überprüfbarer semantischer Zuordnung? DOM-IDs und Importe reichen als Nachweis dafür nicht.

## C229

- **Kandidat / Anforderung:** Ark UI; X04; **D**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR03/AR05/AR07, E1/E2: getrennte Komponentendefinition und Verwendung mit Props, per useCombobox/useScrollArea eigener Machine-/ID-Kontext, Root/RootProvider und Providerwerte; asChild und dokumentiertes Avatar/Tooltip-Beispiel zeigen konkrete Web-Komposition. D in der ausführbaren Frameworkrolle. Keine behauptete neutrale Overlay->ScrollArea-Vertragssyntax, Konfliktfreiheit oder Laufzeitprüfung; komplexe Focus-/Scroll-Ownership bleibt X01/X07.
- **Bedeutung/Grenze:** D im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C230

- **Kandidat / Anforderung:** Ark UI; X05; **N**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR04/AR05/AR06, E2: geprüfte Props/Emits-/Root-/API-Metadaten kennen keinen eigenen versionierten externen Fachmodellresolver. Versionierte npm-Abhängigkeiten sind Softwaredistribution und sichern nicht automatisch referenzierte Contractartefakte. N nur für diesen definierten Ark-Vertragskern, nicht für die Existenz externer Paketmanager.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C231

**Historischer Befund; aktuelle Werkzeugfolgeprüfung: [C407](#c407).**

- **Kandidat / Anforderung:** Ark UI; X06; **U**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR04/AR06/AR09, E2: TS-Typen und API-JSON belegt, typecheck-Script vorhanden. Kein nachgewiesenes kanonisches Schema und ausführbares Validierungstooling für separate neutrale Domänenartefakte. Offen: Gibt es ein offizielles Originalschema und einen Validator, der Properties, Details und externe Referenzen solcher Artefakte prüft? JSON-Metadaten und tsc allein beweisen das nicht.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache.
- **Offene Frage / weiterer Bedarf:** AR04/AR06/AR09, E2: TS-Typen und API-JSON belegt, typecheck-Script vorhanden. Kein nachgewiesenes kanonisches Schema und ausführbares Validierungstooling für separate neutrale Domänenartefakte. Offen: Gibt es ein offizielles Originalschema und einen Validator, der Properties, Details und externe Referenzen solcher Artefakte prüft? JSON-Metadaten und tsc allein beweisen das nicht.

## C232

- **Kandidat / Anforderung:** Ark UI; X07; **N**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR03/AR05/AR06, E1/E2: Props-/ID-Komposition und DOM-Bindung im geprüften Kern, keine gemeinsame vierdomänige Referenz-/Kollisions-/Widerspruchsprüfung. Nutzer muss korrekte IDs/Semantik wählen; keine Behauptung, alle internen Runtimeprüfungen fehlten.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.

## C233

- **Kandidat / Anforderung:** Ark UI; X08; **N**.
- **Quellen:** [S50](SOURCES.md#s50); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S50 aufgelöst.
- **Befund:** AR01/AR03/AR05/AR06, E1/E2: Anleitung trennt funktionale und externe Präsentationsstyles und beschreibt Merging, aber kein führendes Quellen-/Vorrangmodell je Information zwischen vier Originalformaten und Integrationsschicht. N nur für diese geforderte paketweite Governance im geprüften Modell.
- **Bedeutung/Grenze:** N im begrenzten untersuchten Modell (Ark UI am gepinnten Commit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc). Rollenbegrenzung und offene Punkte sind im Befund ausdrücklich angegeben. Referenzbeiträge R beruhen auf konkret belegten Zag-Imports/-Delegationen oder dokumentierter CSS-Bindung; keine eigene neutrale Ark-Maschinensprache. Freie zusätzliche Felder oder Prosa sind kein Nachweis standardisierter Fachsemantik; fremde Erweiterungen werden nicht pauschal ausgeschlossen.
- **Offene Frage / weiterer Bedarf:** Keine praktische Ausführung. Vor späteren Versuchen konkrete Produkt-/Plattformbindung, Werkzeugstand und positive/negative Prüffälle getrennt festlegen.


# Nächste Drei-Agenten-Runde: Panda CSS, uSpec und OpenPencil

Stand 24. Oktober 2026. Drei getrennte, ausdrücklich beauftragte Rechercheberichte wurden zentral gegen den aktuellen Anforderungskatalog, vorhandene Klassifizierungen und Evidenzrollen abgeglichen. Die Primärquellenprüfung ist im jeweiligen Bericht dokumentiert; kein unabhängiger zweiter Vollaudit behauptet. 54 zuvor offene Felder wurden eingeordnet, 20 bleiben mit konkretem Nachweisbedarf U. E1/E2, keine Installation, Kandidaten-, Compiler-, Validator- oder Laufzeitversuche. Editor-, Framework- und Werkzeugfähigkeiten werden nur im ausdrücklich bezeichneten Beitrag zugerechnet.

## C234

- **Kandidat / Anforderung:** Panda CSS; G01; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P01/P02/P05 E1/E2: strukturierte Konfigurationsobjekte, TS-Typen und generiertes Designsystem-JSON sind maschinenlesbar. JSON-Export ist kein vollständiger Contract-Input.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C235

- **Kandidat / Anforderung:** Panda CSS; G02; **A**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P01/P04/P05/P06 E1/E2: statische Token-/Stylewerte sind extrahierbar; CSS-Selektoren/-Werte und JS-transform/Frameworkwrapper benötigen Übersetzung für sprachneutrale Semantik. Kein Swift-/Angular-/Native-Nachweis.
- **Bedeutung/Grenze:** A ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C236

- **Kandidat / Anforderung:** Panda CSS; I01; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E2: benannte Recipe-Variantprops mit Auswahltypen; Patternproperties besitzen enum/token/property/primitive-Typmetadaten. Direkt im Visual-API-Umfang, keine generische Interfacebeschreibung aller fachlichen Props.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C237

- **Kandidat / Anforderung:** Panda CSS; I02; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E2: untersuchte Recipe-/Exporttypen modellieren keine öffentlichen UI-Ereignisse samt strukturierten Payloads. Callback-Props externer Headless-Komponenten sind nicht Panda-Contractfelder.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C238

- **Kandidat / Anforderung:** Panda CSS; I03; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E1/E2: slots:string[] und per-slot Styles benennen Teile. Weder anatomische DOM-Pflicht noch instanzstabile Identität folgt daraus.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C239

- **Kandidat / Anforderung:** Panda CSS; V01; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P01 E2: TokenDataTypes ordnet Kategorien Wertformen zu; Border/Shadow/Gradient strukturiert. Kategorie- und TS-Typen sind enger Nachweis; Stringfarbe keine vollständige formale Farbvalidierung.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C240

- **Kandidat / Anforderung:** Panda CSS; V02; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P03 E1/E2: base, variants, defaultVariants, compoundVariants und Bedingungen. Visuelle Auswahl ist kein Zustandsautomat. Vorhandenes C28 bestätigt.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C241

- **Kandidat / Anforderung:** Panda CSS; V03; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E1. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P01/P03 E1: semanticTokens value base/_dark; Modus per dark-Klasse, Themes per data-panda-theme, explizite CSS-Ausgabeauswahl. Ohne base preset gibt es keine automatische dark-Bedingung.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C242

- **Kandidat / Anforderung:** Panda CSS; V04; **R**.
- **Quellen:** [S51](SOURCES.md#s51); E1. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P04 E1: dokumentierte Weitergabe an CSS Anchor Positioning über positionAnchor/anchor() und benannte positionTry-Fallbacks; CSS-Namensraum --trigger, Richtung/Insets/Spacing. Panda verwaltet anchor-name/position-anchor je Element ausdrücklich nicht selbst. Native CSS-Zielsemantik; keine rendererneutrale Ankerreferenz.
- **Bedeutung/Grenze:** R ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C243

- **Kandidat / Anforderung:** Panda CSS; V05; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E1. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P04 E1: maxHeight/maxH und maxWidth/maxW haben dokumentierte CSS-Geometriebedeutung. Token '5' ist eine Größenreferenz, nicht fünf Zeilen. Variable Zeilenhöhen benötigen zusätzliche Berechnung/Regel.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C244

- **Kandidat / Anforderung:** Panda CSS; V06; **D**.
- **Quellen:** [S51](SOURCES.md#s51); E1. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P04 E1: Styleobjekte und ScrollArea-Pattern setzen overflowX/overflowY auf auto/hidden. Browser-CSS-Scrollsemantik; keine daraus abgeleitete Zahl sichtbarer Einträge oder Fokusnavigation.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C245

- **Kandidat / Anforderung:** Panda CSS; B01; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E2: begrenzter Style-/Rezeptkern besitzt keinen Initialzustand und keine Ereignis-Übergangsziele. data-state-Selektor beobachtet Zustand, definiert ihn nicht.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C246

- **Kandidat / Anforderung:** Panda CSS; B02; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E2: compoundVariants und CSS-Bedingungen wählen Styles; keine UX-Guard-/Action-Ausführungssemantik im untersuchten Kern. Pattern-transform ist Code für Styles.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C247

- **Kandidat / Anforderung:** Panda CSS; B03; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E2: kein UX-Kontext und keine Ereignispayload-Verarbeitung im begrenzten Datenmodell. Variantparameter sind kein Ersatz.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C248

- **Kandidat / Anforderung:** Panda CSS; B04; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P03/P05 E1/E2: focus/hover/active selektieren Styles, binden jedoch keine Taste/Eingabe auf UX-Aktion. P06 delegiert Verhalten an Headless-Code.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C249

- **Kandidat / Anforderung:** Panda CSS; A01; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05/P06 E1/E2: kein Rollen-/Accessible-name-/Beziehungsmodell im gelesenen visuellen Kern. Styling vorhandener ARIA-Attribute verleiht ihnen keine eigene Panda-Semantik.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C250

- **Kandidat / Anforderung:** Panda CSS; A02; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P03/P05/P06 E1/E2: Fokusstyles sind keine Fokusführung/Tastaturpattern. Headless-Wrapper demonstriert externe Zuständigkeit, keine hier verifizierte ARIA/APG-Referenzkonformität.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C251

- **Kandidat / Anforderung:** Panda CSS; A03; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E2: kein Live-Region-/Announcement-Modell im begrenzten Kern. Animation/Transition ist keine zugängliche Rückmeldung.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C252

- **Kandidat / Anforderung:** Panda CSS; X01; **U**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P05/P06: Visual-Konfiguration lässt sich ablegen; vier unabhängige Originaldomänen samt gemeinsamen Bindungen nicht belegt. Frage: welche dokumentierte Paketgrenze erlaubt alle vier unveränderten Domänen mit separaten Validatoren?
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X01: P05/P06: Visual-Konfiguration lässt sich ablegen; vier unabhängige Originaldomänen samt gemeinsamen Bindungen nicht belegt. Frage: welche dokumentierte Paketgrenze erlaubt alle vier unveränderten Domänen mit separaten Validatoren?

## C253

- **Kandidat / Anforderung:** Panda CSS; X02; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P02/P05 E2: Slot-/Recipe-/Token-/Theme-Namen und Klassen sind Definitionen/Werte; kein Elementinstanz-ID-Modell im begrenzten Kern. CSS-anchor-name bleibt Autorverantwortung.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C254

- **Kandidat / Anforderung:** Panda CSS; X03; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P01/P02/P05 E2: Tokenpfade und Quellenindex sind interne Visualreferenzen; keine fremden Interface-/Behavior-/A11y-Artefaktziele mit semantischer Zuordnung im gelesenen Kern. data-state-Bindung per Code müsste zusätzlich beschrieben werden.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C255

- **Kandidat / Anforderung:** Panda CSS; X04; **A**.
- **Quellen:** [S51](SOURCES.md#s51); E1. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P06 E1: wiederverwendbare Frameworkkomponenten und Headless-Teile mit eigenem Providerkontext/Props sind konkret; neutrale Definition/Instanzreferenz mit eigenem ID-/Eventkontext benötigt Adapter. Recipewiederverwendung allein wäre kein ausreichender Nachweis.
- **Bedeutung/Grenze:** A ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C256

- **Kandidat / Anforderung:** Panda CSS; X05; **A**.
- **Quellen:** [S51](SOURCES.md#s51); E1. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P06/P07 E1: externes Designsystempaket wird installiert und über designSystem aufgelöst, Kompatibilitätsdiagnosen existieren. Reproduzierbare exakte Bindung benötigt Paketmanagerstand/Lock und Übersetzung in neutrale Paketabhängigkeit; ^1.0.0-Beispiel ist kein Pin. Kein D für versionierte Contractreferenzen.
- **Bedeutung/Grenze:** A ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C257

**Historischer Befund; aktuelle Werkzeugfolgeprüfung: [C404](#c404).**

- **Kandidat / Anforderung:** Panda CSS; X06; **U**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P05/P07 E1/E2: TS-Eingabetypen, CLI-Flagschema, Configdiagnosen und flacher Exportreader vorhanden; vollständiges Originalschema/Originalvalidator für separates deklaratives Visualartefakt nicht nachgewiesen. Frage: welches vollständige offizielle Schema prüft das unveränderte Visualartefakt unabhängig vom Compiler?
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X06: P05/P07 E1/E2: TS-Eingabetypen, CLI-Flagschema, Configdiagnosen und flacher Exportreader vorhanden; vollständiges Originalschema/Originalvalidator für separates deklaratives Visualartefakt nicht nachgewiesen. Frage: welches vollständige offizielle Schema prüft das unveränderte Visualartefakt unabhängig vom Compiler?

## C258

- **Kandidat / Anforderung:** Panda CSS; X07; **N**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P05/P07 E1/E2: gelesener Exportreader/CLI-Diagnoseumfang prüft keine vierdomänigen Instanzkollisionen oder fachlichen Widersprüche. Tokenzyklen/fehlende Referenzen und Paketdiagnosen sind enger.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C259

- **Kandidat / Anforderung:** Panda CSS; X08; **U**.
- **Quellen:** [S51](SOURCES.md#s51); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** P05/P06/P07: Panda-intern config-last-Vorrang und optionale sources-Provenienz belegt; Gesamtpaket-Ownership über vier Originalformate offen. Frage: welche führende Domäne entscheidet bei Konflikten zwischen Visual, Behavior und A11y, und wie bleiben Änderungen nachvollziehbar?
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Visual-Token-/Recipe-/DesignSystemSpec-Kern samt ausdrücklich dokumentierter CSS- und Paketbindung, Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X08: P05/P06/P07: Panda-intern config-last-Vorrang und optionale sources-Provenienz belegt; Gesamtpaket-Ownership über vier Originalformate offen. Frage: welche führende Domäne entscheidet bei Konflikten zwischen Visual, Behavior und A11y, und wie bleiben Änderungen nachvollziehbar?

## C260

- **Kandidat / Anforderung:** uSpec; G01; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CON/TYP/DOC: kanonisches JSON-Komponentenartefakt; Markdown daraus abgeleitet. E2.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C261

- **Kandidat / Anforderung:** uSpec; G02; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CON/TYP/BASE: fachliche Daten benötigen keine eingebetteten JS-/Reactfunktionen. Strings und Figma-Konzepte sind beschreibend; keine portable ausführbare Verhaltenssprache. Generierung ist separat JS/TS-/Figma-/LLM-gebunden.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C262

- **Kandidat / Anforderung:** uSpec; I01; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** BASE rawDefs.type und instance componentProperties type/value; SAFE bewahrt BOOLEAN/INSTANCE_SWAP/TEXT/VARIANT/SLOT explizit. API dokumentiert property/values/required/default sowie Dictionary. Typnachweis im extrahierten Quellmodell, keine vollständige Prüfung komplexer Laufzeittypen.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C263

- **Kandidat / Anforderung:** uSpec; I02; **N**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CON/TYP/API-Output/Dictionary: Property-/State-/Slotdaten, keine definierte öffentliche Eventdeklaration mit strukturiertem Payloadschema im geprüften Kern. Freitextnotizen sind kein Eventmodell.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C264

- **Kandidat / Anforderung:** uSpec; I03; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** anatomy.defaultTree/composition/subcomponents, TreeNode.name/id, childComposition und benannte API-Subcomponenttabellen. CON/TYP/BASE.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C265

- **Kandidat / Anforderung:** uSpec; V01; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** BASE/TYP/STR: strukturierte Dimensionswerte {value,token,display}, Farbhex/-property, resolvedType und kind-bezogene Variablenwerte, Typografie; fachliche Werte sind vorhanden. Schemafelder sind teils offen und garantieren keine gültigen Einheiten/Farben.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C266

- **Kandidat / Anforderung:** uSpec; V02; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** COL: Varianten/State-Spalten mit tokensByState; BASE variantProperties/colorWalk/stateComparison. Strukturierte visuelle Zustandswerte, keine UX-Transitionsbindung.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C267

- **Kandidat / Anforderung:** uSpec; V03; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** COL Variable Mode Colors: modeId, Type×Mode-Abschnitte, modeTokenMap-Auflösung generischer zu semantischen Tokens, explizite Figma-Modeauswahl. BASE valuesByMode/collection modes. Direkt in Figma-/Dokumentationsrolle; keine bewiesene neutrale Theme-Laufzeit.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C268

**Historischer Befund; aktuelle Folgeprüfung: [C400](#c400).**

- **Kandidat / Anforderung:** uSpec; V04; **U**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** STR besitzt section._anchor mit layerId/variantId sowie Abstand/Layoutfelder. Das ist ein Mess-/Renderziel, kein ausreichender Beleg Overlay→Input mit definierter Richtung/Abstand und unabhängiger Layoutsemantik. Frage: Welche originale Felddefinition bindet Referenzziel + placement/side + offset als relative Geometrie?
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für V04: STR besitzt section._anchor mit layerId/variantId sowie Abstand/Layoutfelder. Das ist ein Mess-/Renderziel, kein ausreichender Beleg Overlay→Input mit definierter Richtung/Abstand und unabhängiger Layoutsemantik. Frage: Welche originale Felddefinition bindet Referenzziel + placement/side + offset als relative Geometrie?

## C269

- **Kandidat / Anforderung:** uSpec; V05; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** STR dokumentiert minHeight/maxHeight/minWidth/maxWidth mit Figma Frame Min/Max und begrenzt feste Messwerte auf FIXED-Container; BASE dimensions erhält Messdaten. Direkt als Figma-basierte maximale Abmessung, keine Ableitung fünf variabler Zeilen und kein neutraler Constraintsolver.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C270

**Historischer Befund; aktuelle Folgeprüfung: [C401](#c401).**

- **Kandidat / Anforderung:** uSpec; V06; **U**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** STR dokumentiert clipsContent true/false ausdrücklich als Clip content (overflow); BASE erwähnt Scrollwrapper. Clipping beweist kein formal beschriebenes Scrollverhalten/Achse. Frage: Wird overflowDirection/scrolling im Originalartefakt mit Semantik gespeichert oder braucht es neue Modellierung?
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für V06: STR dokumentiert clipsContent true/false ausdrücklich als Clip content (overflow); BASE erwähnt Scrollwrapper. Clipping beweist kein formal beschriebenes Scrollverhalten/Achse. Frage: Wird overflowDirection/scrolling im Originalartefakt mit Semantik gespeichert oder braucht es neue Modellierung?

## C271

- **Kandidat / Anforderung:** uSpec; B01; **N**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CON/TYP/API-Dictionary states speichern Zuordnung zu API-Werten/runtimeCondition als Prosa. Kein initial + event→target-Transitionsmodell im definierten Kern.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C272

- **Kandidat / Anforderung:** uSpec; B02; **N**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** API kennt priorityOrder und textuelle Resolver-/runtimeCondition-Notizen; keine definierte Guardauswertung oder Actionausführung im Kern. CON/TYP/API.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C273

- **Kandidat / Anforderung:** uSpec; B03; **N**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CON/TYP/BASE/API: Daten-Snapshots und Propertywerte, kein Kontext-/Ereignisdatenmodell für eine ausführbar definierte Behaviorlogik.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C274

- **Kandidat / Anforderung:** uSpec; B04; **N**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** VOI beschreibt Tastatur/Fokus, aber keine strukturierte Input→UX-Aktion/Maschinenereignis-Bindung im geprüften Contractkern.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C275

- **Kandidat / Anforderung:** uSpec; A01; **R**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** VOI benennt Plattformen und konkrete ARIA/VoiceOver/TalkBack-Eigenschaften, label-for/ID-/describedby-Zuordnung; PropertyItem.property/value/notes verweisen auf Plattformsemantik. Keine Konformitätsprüfung der Stringwerte oder Zielbeziehungen durch CON/CAC.
- **Bedeutung/Grenze:** R ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C276

- **Kandidat / Anforderung:** uSpec; A02; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** VOI: Mergeanalyse, referenzierbare Fokusreihenfolge, conditional focus stops und konkretes Tabpattern mit roving tabindex/Arrow keys. Direkt als dokumentiertes Interaktionsmuster, kein ausführbarer Keyboardprüfer.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C277

- **Kandidat / Anforderung:** uSpec; A03; **R**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** VOI: live region von Fokusstopps getrennt, Fehlerbeispiele mit liveRegion:polite und iOS Notification; Semantik stammt aus den benannten Plattformen. Produkttrigger/Inhalt werden interpretiert; kein automatischer Nachweis tatsächlicher AT-Ansage.
- **Bedeutung/Grenze:** R ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C278

- **Kandidat / Anforderung:** uSpec; X01; **U**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Separate api/structure/color/voice Evidence-/Cachedateien tatsächlich vorhanden; CON erzwingt alle Bereiche plus SourceModel und kein separates Behavior. Frage: Können vier gewählte Fachartefakte unabhängig mit Originalschämata geführt werden, ohne uSpecs Pflichtcontainer neu zu modellieren? Vier Spezialisten sind nicht die gewünschten vier Domänen.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X01: Separate api/structure/color/voice Evidence-/Cachedateien tatsächlich vorhanden; CON erzwingt alle Bereiche plus SourceModel und kein separates Behavior. Frage: Können vier gewählte Fachartefakte unabhängig mit Originalschämata geführt werden, ohne uSpecs Pflichtcontainer neu zu modellieren? Vier Spezialisten sind nicht die gewünschten vier Domänen.

## C279

- **Kandidat / Anforderung:** uSpec; X02; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** BASE/TYP: Figma node IDs, fileKey, topLevelInstanceId, placementsByVariant.nodeIds und section anchor IDs. Direkt für Quell-/Placementidentität. Deduplizierung nach set/name und bool-Fingerprint limitiert Unterscheidung; Stabilität nach Designänderung/Export oder universelle URNs nicht bewiesen.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C280

- **Kandidat / Anforderung:** uSpec; X03; **U**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CAC besitzt interne Evidence→Output-JSON-Pointer und gemeinsame Dictionaryvokabeln; STR `_anchor`/source IDs adressieren Figmaquellen. Nicht ausreichend für externe Interface/Behavior/Visual/A11y-Ziele. Frage: Welcher Resolver adressiert ein Originalartefakt anderer Domäne und definiert die semantische Bindung?
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X03: CAC besitzt interne Evidence→Output-JSON-Pointer und gemeinsame Dictionaryvokabeln; STR `_anchor`/source IDs adressieren Figmaquellen. Nicht ausreichend für externe Interface/Behavior/Visual/A11y-Ziele. Frage: Welcher Resolver adressiert ein Originalartefakt anderer Domäne und definiert die semantische Bindung?

## C281

- **Kandidat / Anforderung:** uSpec; X04; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** BASE: instanceConfig mit mainComponentId und variantProperties/booleanOverrides/instanceSwapOverrides/textOverrides; defaultChildren.contextualOverrides, Slots preferredInstances, genaue Placements. Direkt für dokumentierte Figma-Komponenteninstanzen/Parameter, keine runtimefähige Contractkomposition behauptet.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C282

- **Kandidat / Anforderung:** uSpec; X05; **N**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CON/TYP/BASE: Figma IDs, componentKey, remote collections, hashes und schemaVersion, aber keine reproduzierbare externe Komponenten-/Teilmodellversion mit definierter Versionsauflösung im geprüften Kern. Hash der Extraktion ist keine Dependencyversion.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C283

- **Kandidat / Anforderung:** uSpec; X06; **D**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CON validateCanonicalContract/Ajv prüft eigenes Canonicalartefakt unverändert; BVAL eigenes Baseartefakt separat. CAC prüft Spezialistencaches manuell, nicht gegen publizierte Fach-JSON-Schemas. D nur für eigene Originalformate; Erhalt vier fremder Validatoren nicht belegt.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C284

- **Kandidat / Anforderung:** uSpec; X07; **N**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** CAC vollständige Funktion: Evidence-Ziele, Ledger, Achsen und Sourceidentität werden geprüft. Keine allgemeine Paketprüfung für fremde Domänen, Instanzkollisionen und widersprechende fachliche Anforderungen; CON nur Struktur/Hash/Slug. Kein pauschales „uSpec prüft keine Referenzen“.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C285

- **Kandidat / Anforderung:** uSpec; X08; **U**.
- **Quellen:** [S52](SOURCES.md#s52); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** BASE Plugin sole writer of base, Interpretation read-only; DOC canonical JSON→Markdown und domain retries; reale interne Ownershipregeln. Frage: Gibt es eine normative per-information Vorrang-/Rückschreibregel zwischen unabhängigen Originalformaten und Integrationsschicht des gewünschten Pakets? Interne Pipelineownership allein klärt das nicht.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Canonicalcontract, dokumentiertes Figma-Quellmodell und gelesene Spezialisten-/Cachedefinitionen, Commit 1e25e9b8bc2e694689ba0489594f38807a341f14. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X08: BASE Plugin sole writer of base, Interpretation read-only; DOC canonical JSON→Markdown und domain retries; reale interne Ownershipregeln. Frage: Gibt es eine normative per-information Vorrang-/Rückschreibregel zwischen unabhängigen Originalformaten und Integrationsschicht des gewünschten Pakets? Interne Pipelineownership allein klärt das nicht.

## C286

- **Kandidat / Anforderung:** OpenPencil; G01; **D**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS/OPF: strukturierte JSON-Objekte im Pluginfeld; benannte Spec mit dokumentiertem Schema. Kein bloßer Freitext.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C287

- **Kandidat / Anforderung:** OpenPencil; G02; **A**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS enthält datenförmige Bindungen ohne nutzereigene Funktionen; Kindsemantik und Interaktion werden aber durch Reka/Vue/DOM realisiert (OPD/OPV). Für neutralen fachlichen Kern müssen deren fest eingebaute Regeln explizit übertragen werden; kein Swift-/Angular-Nachweis.
- **Bedeutung/Grenze:** A ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C288

- **Kandidat / Anforderung:** OpenPencil; I01; **D**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPK typisiert benannte Controlwerte value/disabled/open/text als boolean/text/number/choice; OPS/OPR binden die vorhandenen Komponentenproperties nach Typ. Enger fester Controlvertrag, kein allgemeines öffentliches Prop-Typsystem.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C289

- **Kandidat / Anforderung:** OpenPencil; I02; **N**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Vollständiger OPS/OPK-Kern enthält keine Deklaration öffentlicher Eventnamen mit Payloadfeldern. OPV modelValue/open-Callbacks sind Adapterimplementierung; OPT sind Agenttools, keine UI-Events.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C290

- **Kandidat / Anforderung:** OpenPencil; I03; **D**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPK parts mit IDs, required/items/children, OPS parts zu Slotproperty-ID; reale strukturierte Anatomie.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C291

- **Kandidat / Anforderung:** OpenPencil; V01; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Eigene numbers sind Controlwerte/-ranges, keine typisierten Designfarben/Dimensionen. Gesamter Editor-/Tokenkern nicht diesem Behaviour-Beitrag zugerechnet; gesondertes Visualmodell prüfen.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für V01: Eigene numbers sind Controlwerte/-ranges, keine typisierten Designfarben/Dimensionen. Gesamter Editor-/Tokenkern nicht diesem Behaviour-Beitrag zugerechnet; gesondertes Visualmodell prüfen.

## C292

- **Kandidat / Anforderung:** OpenPencil; V02; **A**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS states ordnet rest/hover/pressed/focus/disabled einer VARIANT-Property zu; OPD beschreibt Styles aus graphischen Varianten. Das Behaviour enthält keine Styles/Tokenreferenzen selbst. Scenegraph-/Variantbindung ist belegter Mechanismus, benötigt für externes Visualartefakt Übersetzung.
- **Bedeutung/Grenze:** A ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C293

- **Kandidat / Anforderung:** OpenPencil; V03; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Keine belastbare Themeauflösung für diesen Beitrag untersucht. Dokumentvariablen im Preview sind kein eigener Themevertrag. Separates Visualmodell prüfen.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für V03: Keine belastbare Themeauflösung für diesen Beitrag untersucht. Dokumentvariablen im Preview sind kein eigener Themevertrag. Separates Visualmodell prüfen.

## C294

- **Kandidat / Anforderung:** OpenPencil; V04; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Keine neutrale Anker-/Abstandssemantik des Behaviourbeitrags belegt; Slider-Thumb-Laufzeitposition ist kein allgemeiner Overlayvertrag. Renderer-/Layoutmodell separat prüfen.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für V04: Keine neutrale Anker-/Abstandssemantik des Behaviourbeitrags belegt; Slider-Thumb-Laufzeitposition ist kein allgemeiner Overlayvertrag. Renderer-/Layoutmodell separat prüfen.

## C295

- **Kandidat / Anforderung:** OpenPencil; V05; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Control min/max sind Wertebereiche, keine Flächenbegrenzung. Eigenes Layoutmodell und dynamische Zeilenhöhen separat prüfen.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für V05: Control min/max sind Wertebereiche, keine Flächenbegrenzung. Eigenes Layoutmodell und dynamische Zeilenhöhen separat prüfen.

## C296

- **Kandidat / Anforderung:** OpenPencil; V06; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Preview-Wheelweitergabe zum Canvas (OPD) ist kein formales Overflow-/ScrollArea-Modell des Contracts. Separates Modell prüfen.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für V06: Preview-Wheelweitergabe zum Canvas (OPD) ist kein formales Overflow-/ScrollArea-Modell des Contracts. Separates Modell prüfen.

## C297

- **Kandidat / Anforderung:** OpenPencil; B01; **N**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS/OPK nennen Interaktionszustandszeichnungen, aber keine deklarierte Initialzustands-/Event-/Transitiontarget-Tabelle. OPV enthält festen Code für Priorität disabled→pressed→hover→focus→rest; das ist kein vom Autor beschreibbares Maschinenmodell.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C298

- **Kandidat / Anforderung:** OpenPencil; B02; **N**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS/OPK-Kern besitzt keine Guard-/Action-Ausdruckssyntax oder Ausführungsreihenfolge für fachliche Aktionen. Feste OPV-Funktionen sind Implementierung, kein Contractfeld.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C299

- **Kandidat / Anforderung:** OpenPencil; B03; **N**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS/OPK enthalten Wertebindungen, aber keine Ereignispayload-/Contextreferenzen oder datenverarbeitende Logiksprache. OPV hält konkrete Werte und verarbeitet Callbacks in TS; das erweitert nicht die Originalsyntax.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C300

- **Kandidat / Anforderung:** OpenPencil; B04; **A**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPV interaction bindet Pointer-/FocusEvents, Reka-Komponenten übernehmen Tastatur und Eingaben (OPD). Ein neutraler expliziter Input→UX-Action-Vertrag benötigt Extraktion/Hostbindung dieser vorhandenen Mechanismen.
- **Bedeutung/Grenze:** A ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C301

- **Kandidat / Anforderung:** OpenPencil; A01; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPV zeigt role=radio/aria-checked und Reka-Wrapper. Vollständige Rollen-/Namen-/Beziehungssemantik je Kind und benennbare externe Ziele nicht geprüft; keine automatische R-Zurechnung aller Reka-Fähigkeiten.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für A01: OPV zeigt role=radio/aria-checked und Reka-Wrapper. Vollständige Rollen-/Namen-/Beziehungssemantik je Kind und benennbare externe Ziele nicht geprüft; keine automatische R-Zurechnung aller Reka-Fähigkeiten.

## C302

- **Kandidat / Anforderung:** OpenPencil; A02; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPD delegiert Tastatur/Fokus an Browser/Reka; referenzierte einzelne Reka-Muster und ihr vollständiges Mapping wurden nicht auditiert. Kindname allein ist noch kein nachgewiesener neutraler Patternvertrag.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für A02: OPD delegiert Tastatur/Fokus an Browser/Reka; referenzierte einzelne Reka-Muster und ihr vollständiges Mapping wurden nicht auditiert. Kindname allein ist noch kein nachgewiesener neutraler Patternvertrag.

## C303

- **Kandidat / Anforderung:** OpenPencil; A03; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Kein Nachweis einer dynamischen zugänglichen Ergebnis-/Statusmeldung im Behaviourvertrag. Vollständige Reka-/Exportpfade wären gezielt zu untersuchen.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für A03: Kein Nachweis einer dynamischen zugänglichen Ergebnis-/Statusmeldung im Behaviourvertrag. Vollständige Reka-/Exportpfade wären gezielt zu untersuchen.

## C304

- **Kandidat / Anforderung:** OpenPencil; X01; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS ist als Submodell exportiert, wird aber auf Scenegraph-Properties/Slots aufgelöst. Vier unabhängig beschriebene Domänen mit getrennten Originalformaten nicht nachgewiesen. Paketkompositionsnachweis fehlt.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X01: OPS ist als Submodell exportiert, wird aber auf Scenegraph-Properties/Slots aufgelöst. Vier unabhängig beschriebene Domänen mit getrennten Originalformaten nicht nachgewiesen. Paketkompositionsnachweis fehlt.

## C305

- **Kandidat / Anforderung:** OpenPencil; X02; **D**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS propertyId/part bindings, OPM ownerbezogene Auflösung und renameBehaviourProperties sind explizit. Begrenzte D wie C30: kein Nachweis universeller Identität über Änderungen/Mehrfachinstanzen. OPD/OPV nutzen für Preview Layerpfade, weil Varianten neue Node-IDs erzeugen.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C306

- **Kandidat / Anforderung:** OpenPencil; X03; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPR verbindet Behavior mit Properties/Slots desselben Scenegraphs. Das ist reale interne Bindung, jedoch kein Nachweis auf ein separat beschriebenes externes Interface-/Visual-/A11y-Artefakt mit Namensraum und semantischer Zuordnung. Genau diesen externen Bezug als Folgeprüfung spezifizieren.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X03: OPR verbindet Behavior mit Properties/Slots desselben Scenegraphs. Das ist reale interne Bindung, jedoch kein Nachweis auf ein separat beschriebenes externes Interface-/Visual-/A11y-Artefakt mit Namensraum und semantischer Zuordnung. Genau diesen externen Bezug als Folgeprüfung spezifizieren.

## C307

- **Kandidat / Anforderung:** OpenPencil; X04; **A**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPK items erlaubt Instanzen mit eigenem Verhalten; OPT create_slot erklärt instanzeigenen Slotinhalt, OPV State pro control.path/chooseItem. Konkrete Komposition ist belegt, Übersetzung in neutrales Komponentenpaket mit Parametern/Ereignisbindungen/Ownership fehlt. Kein pauschales D aus Editorinstanzen.
- **Bedeutung/Grenze:** A ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C308

**Fortschreibung der Gesamtprüfung:** Aktueller Befund [C411](#c411); der folgende Text dokumentiert den früheren Stand.

- **Kandidat / Anforderung:** OpenPencil; X05; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS hat kein externes Dependency-/Versionsfeld. OPF zeigt separate libraryId/assetKey/revisionId-Buchhaltung; OPD sagt Behaviour reist mit Assets. Resolver, reproducible binding und Import-/Updatepfade für externes Fachmodell nicht geprüft; Versionsstrings allein reichen nicht für D/R/N.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X05: OPS hat kein externes Dependency-/Versionsfeld. OPF zeigt separate libraryId/assetKey/revisionId-Buchhaltung; OPD sagt Behaviour reist mit Assets. Resolver, reproducible binding und Import-/Updatepfade für externes Fachmodell nicht geprüft; Versionsstrings allein reichen nicht für D/R/N.

## C309

- **Kandidat / Anforderung:** OpenPencil; X06; **D**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPS ist originales separat exportiertes Valibot-Schema (OPP); OPF zeigt seine tatsächliche Verwendung bei JSON-decode. Dieses Subartefakt kann gegen Originalschema geprüft werden. Keine Behauptung eines Vier-Domänen-Paketvalidators oder erfolgreicher Probe.
- **Bedeutung/Grenze:** D ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C310

- **Kandidat / Anforderung:** OpenPencil; X07; **N**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** Im begrenzten Behaviourkern OPS/OPM/OPR werden Propertytypen, bestimmte fehlende Bindungen und ein doppelt für Parts belegter Slot geprüft; keine Referenz-/Instanz-/Widerspruchsprüfung zwischen vier separaten Domänen. Dies ist die Grenze dieser konkreten Prüffunktionen, kein Audit sämtlicher Editortools.
- **Bedeutung/Grenze:** N ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund. Frei ergänzbare Felder oder fremde Bibliotheken liefern keine eigene definierte Kernsemantik; fehlende Recherche allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Plattformbindung und gezielte positive/negative Prüffälle getrennt festlegen; keine praktische Funktionsfähigkeit oder vollständige Integration aus Dokumentation ableiten.

## C311

- **Kandidat / Anforderung:** OpenPencil; X08; **U**.
- **Quellen:** [S53](SOURCES.md#s53); E2. Lokale Quellenkürzel im Befund sind dort auf gepinnte Primärquellen aufgelöst.
- **Befund:** OPM definiert lokalen behaviourOwner; OPF unterscheidet content/format/bookkeeping und OPD nennt ein Modell für alle Authoringsurfaces. Vorrang/Änderungsnachvollziehbarkeit zwischen vier Originalformaten und Integrationsschicht bleibt unbelegt.
- **Bedeutung/Grenze:** U ausschließlich für den bezeichneten Beitrag: Behaviour-/Spec-Modell von @open-pencil/scene-graph; nicht der gesamte Editor oder sämtliche Reka-Funktionen, Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab. Die konkrete Rollenbegrenzung steht im Befund.
- **Offene Frage / weiterer Bedarf:** Konkrete Nachweislücke für X08: OPM definiert lokalen behaviourOwner; OPF unterscheidet content/format/bookkeeping und OPD nennt ein Modell für alle Authoringsurfaces. Vorrang/Änderungsnachvollziehbarkeit zwischen vier Originalformaten und Integrationsschicht bleibt unbelegt.


# Letzte Kandidatenrunde: WAI-ARIA, APG und CSS Layout

Stand 24. Oktober 2026. Alle 26 Kriterien je Kandidat betrachtet. CSS-Bericht stammt vom getrennten Recherche-Agenten; WAI-ARIA/APG wurden nach Kapazitätsfehlern zentral anhand offizieller Quellen geprüft. Kein fehlgeschlagener Start wird als Nachweis ausgegeben. 47 der 73 zuvor offenen Felder geklärt; 26 U-Fragen verbleiben. Kein Kandidat installiert, keine Praxis-/Laufzeit-/Browser-/AT-/Validatorversuche. ARIA-Norm, informativer APG-Guide und CSS-Layoutmodule bleiben getrennte Rollen.

**Methodische Zentralentscheidung G02/CSS:** D statt des konservativen A-Vorschlags im Bericht, weil das festgelegte Kriterium keine erforderlichen JS-/Reactfunktionen verlangt. CSS erfüllt dies im Fachmodell. Fehlende native/rendererneutrale Abbildung wird dadurch nicht behauptet oder gelöst. Keine heimliche Verschärfung des Kriteriums auf vollständige Plattformneutralität.

## C312

- **Kandidat / Anforderung:** WAI-ARIA; G01; **D**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §§5–6/8 definiert Rollen sowie maschinenlesbare Zustands-/Propertyattribute in Host-Markup, einschließlich Werttypen und Verarbeitung. Das ist A11y-Datensyntax, kein vollständiges JSON-Komponentenformat.
- **Bedeutung/Grenze:** D im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C313

- **Kandidat / Anforderung:** WAI-ARIA; G02; **D**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §6.2.4/Anhang A trennt generische Werttypen von ihrer Hostrepräsentation; Semantik verlangt keine JS-/React-Funktionen. Web-/Hostbindung und native Umsetzung bleiben gesonderte Fragen.
- **Bedeutung/Grenze:** D im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C314

- **Kandidat / Anforderung:** WAI-ARIA; I01; **D**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §6 definiert benannte öffentlich exponierte Accessibility-Properties mit ausdrücklichen Typen, etwa aria-expanded und IDREF-Werte. D nur für diese A11y-Schnittstelle, kein allgemeiner Komponenten-Propkatalog oder Runtime-Wertetest.
- **Bedeutung/Grenze:** D im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C315

- **Kandidat / Anforderung:** WAI-ARIA; I02; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Im begrenzten Rollen-/Propertykern AR12 ist kein öffentlicher Komponenten-Eventkatalog mit strukturierten Payloaddeklarationen definiert. AAM-Ereignisse sind Plattformmeldungen, kein daraus abgeleiteter UI-API-Vertrag.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C316

- **Kandidat / Anforderung:** WAI-ARIA; I03; **U**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 Required Context/Owned Elements beschreibt Rollenbeziehungen, aber keinen ausreichend nachgewiesenen benannten UI-Partkatalog. Frage: Wie wird konkrete Komponenten-Anatomie von Input/Popup/Slots mit diesen Rollen verbunden?
- **Bedeutung/Grenze:** U im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** AR12 Required Context/Owned Elements beschreibt Rollenbeziehungen, aber keinen ausreichend nachgewiesenen benannten UI-Partkatalog. Frage: Wie wird konkrete Komponenten-Anatomie von Input/Popup/Slots mit diesen Rollen verbunden?

## C317

- **Kandidat / Anforderung:** WAI-ARIA; V01; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 definiert semantische Werte, keine Designfarben, Typografie oder typisierten Geometriedimensionen. aria-valuenow bezeichnet Controlwerte, keine visuelle Größensprache.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C318

- **Kandidat / Anforderung:** WAI-ARIA; V02; **R**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §8.7 verlangt Unterstützung von CSS-Attributselektoren und aktualisierte Präsentation bei ARIA-Änderungen. R für die ausdrücklich dokumentierte Bindung an externe CSS-Styledeklarationen, keine eigenen fertigen Styles/Designvarianten.
- **Bedeutung/Grenze:** R im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C319

- **Kandidat / Anforderung:** WAI-ARIA; V03; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Im AR12-Rollen-/Propertykern kein Theme-/Dark-Mode-Wertauflösungsmodell. Host-CSS und Betriebssystempräferenzen sind getrennte Beiträge.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C320

- **Kandidat / Anforderung:** WAI-ARIA; V04; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12-Semantik definiert keinen geometrischen Anker, Position/Seite oder Pixelabstand. aria-controls/owns bezeichnet semantische Beziehungen, nicht Layoutanker.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C321

- **Kandidat / Anforderung:** WAI-ARIA; V05; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ARIA-Range-Minimum/Maximum beschreibt zulässige Controlwerte. Der definierte Kern enthält keine maximale Fläche/Höhe oder Zeilenableitung.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C322

- **Kandidat / Anforderung:** WAI-ARIA; V06; **U**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Orientierung, Fokus-/Sichtbarkeitshinweise und Scrollbarkeit im Host sind kein geprüfter formaler Overflowvertrag. Frage: Welches getrennte Layout-/Scrollmodell bestimmt Clip, Scrollport und Begrenzung?
- **Bedeutung/Grenze:** U im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Orientierung, Fokus-/Sichtbarkeitshinweise und Scrollbarkeit im Host sind kein geprüfter formaler Overflowvertrag. Frage: Welches getrennte Layout-/Scrollmodell bestimmt Clip, Scrollport und Begrenzung?

## C323

- **Kandidat / Anforderung:** WAI-ARIA; B01; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Benannte ARIA-Zustandswerte sind keine Autorenmaschine mit Initialzustand und eventbestimmten Transitionzielen. AR12 §§1.2/4 weist tatsächliche Interaktion dem Autor/Host zu.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C324

- **Kandidat / Anforderung:** WAI-ARIA; B02; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 beschreibt Pflichten/Attributbedeutungen, keine frei beschreibbare Guard-/Action-Ausführungssprache. Normative MUST-Regeln sind keine ausführbaren Guards.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C325

- **Kandidat / Anforderung:** WAI-ARIA; B03; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Im begrenzten AR12-Kern kein Context-/Eventausdrucksmodell für Produktlogik; semantische Attribute ersetzen keine Datenverarbeitung.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C326

- **Kandidat / Anforderung:** WAI-ARIA; B04; **A**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §4.3 beschreibt Fokusführung über Host-tabindex/DOM-Fokus und aria-activedescendant; Hostevents werden am fokussierten Element verarbeitet. Konkrete Tastenevents und Produktaktionen müssen durch Hostcode gebunden werden, keine universelle fertige UX-Bindung.
- **Bedeutung/Grenze:** A im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C327

- **Kandidat / Anforderung:** WAI-ARIA; A01; **D**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 Rollen, Accessible-Name-Anforderungen, aria-label/labelledby/describedby/controls/owns und IDREF-Typen sind ausdrücklich definiert. Accname/AAM sind getrennte ergänzende Quellen; keine echte Browser-/AT-Konformität daraus ableiten.
- **Bedeutung/Grenze:** D im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C328

- **Kandidat / Anforderung:** WAI-ARIA; A02; **D**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §4.3 und Rollendefinitionen beschreiben referenzierbare Fokus-/Keyboardpflichten für Composite-Widgets; etwa Container-Tabstopp und Focusmanagement. D für diesen Normteil; konkrete vollständige Tastaturkonventionen werden durch APG ergänzt.
- **Bedeutung/Grenze:** D im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C329

- **Kandidat / Anforderung:** WAI-ARIA; A03; **D**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 aria-live/atomic/relevant/busy und Rollen alert/status definieren zugängliche dynamische Aktualisierungssemantik. Produktauslöser, Inhalte und tatsächliche Ansage bleiben ausdrücklich gesondert.
- **Bedeutung/Grenze:** D im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C330

- **Kandidat / Anforderung:** WAI-ARIA; X01; **U**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ARIA-Markup kann als Accessibility-Beitrag referenziert werden. Frage: Wie bindet ein eigenständiges A11y-Artefakt vier unveränderte Originaldomänen mit getrennten führenden Quellen? Hostintegration allein beweist dies nicht.
- **Bedeutung/Grenze:** U im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** ARIA-Markup kann als Accessibility-Beitrag referenziert werden. Frage: Wie bindet ein eigenständiges A11y-Artefakt vier unveränderte Originaldomänen mit getrennten führenden Quellen? Hostintegration allein beweist dies nicht.

## C331

- **Kandidat / Anforderung:** WAI-ARIA; X02; **R**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §6.2.4/Anhang A nutzt ausdrücklich IDs anderer Elemente desselben Dokuments; HTML-id/XML-IDREF sind benannte Host-Zielmodelle. R für konkrete Elementreferenz, keine dauerhafte komponentenübergreifende Instanz-/URN-Garantie.
- **Bedeutung/Grenze:** R im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C332

- **Kandidat / Anforderung:** WAI-ARIA; X03; **U**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** IDREF verbindet reale Hostelemente semantisch, keine nachgewiesenen externen Fachmodellknoten. Frage: Welcher Resolver bindet separate Interface-/Visual-/Behavior-Originalartefakte an diese Elementziele?
- **Bedeutung/Grenze:** U im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** IDREF verbindet reale Hostelemente semantisch, keine nachgewiesenen externen Fachmodellknoten. Frage: Welcher Resolver bindet separate Interface-/Visual-/Behavior-Originalartefakte an diese Elementziele?

## C333

- **Kandidat / Anforderung:** WAI-ARIA; X04; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12-Rollenhierarchie und owned elements sind semantische Struktur, keine Trennung von Komponentendefinition und parametrisierter Verwendung mit eigenem Instanzkontext.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C334

- **Kandidat / Anforderung:** WAI-ARIA; X05; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Im definierten AR12-Attributkern kein versionierter externer Komponenten-/Teilmodellresolver. Datierte Norm-URLs versionieren die Quelle, nicht eine abhängige Komponenteninstanz.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C335

**E3-Fortschreibung:** aktueller Befund [C422](#c422); folgender Text dokumentiert den früheren Stand.

- **Kandidat / Anforderung:** WAI-ARIA; X06; **U**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §8/Anhang A nennt Host-Wertabbildungen; kein vollständiges separates Originalschema samt konkret geprüftem neutralen A11y-Artefaktvalidator nachgewiesen. Frage: Welcher Originalchecker prüft welche Host-/ARIA-Version und welche semantischen Beziehungen?
- **Bedeutung/Grenze:** U im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** AR12 §8/Anhang A nennt Host-Wertabbildungen; kein vollständiges separates Originalschema samt konkret geprüftem neutralen A11y-Artefaktvalidator nachgewiesen. Frage: Welcher Originalchecker prüft welche Host-/ARIA-Version und welche semantischen Beziehungen?

## C336

- **Kandidat / Anforderung:** WAI-ARIA; X07; **N**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §9 begrenzt UA-Validierung ausdrücklich: unter anderem zirkuläre ownership, echte Checkboxfunktion und korrektes active-descendant-Ziel werden nicht logisch vollständig verifiziert. Keine Vier-Domänen-Paketkonfliktprüfung im definierten Kern.
- **Bedeutung/Grenze:** N im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C337

- **Kandidat / Anforderung:** WAI-ARIA; X08; **U**.
- **Quellen:** [S54](SOURCES.md#s54); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AR12 §8 behandelt Vorrang nativer/Host-Semantik und ARIA-Konflikte. Das ist positiv, aber kein Quellen-/Änderungsmodell über vier Originalformate. Frage: Welche Paketregel legt die führende Quelle pro überlappender Information fest?
- **Bedeutung/Grenze:** U im begrenzten Beitrag WAI-ARIA 1.2 REC plus ausdrücklich getrennte Host-/AAM-/Accnamebezüge. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** AR12 §8 behandelt Vorrang nativer/Host-Semantik und ARIA-Konflikte. Das ist positiv, aber kein Quellen-/Änderungsmodell über vier Originalformate. Frage: Welche Paketregel legt die führende Quelle pro überlappender Information fest?

## C338

- **Kandidat / Anforderung:** APG; G01; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP0 definiert APG ausdrücklich als informativen Guide ohne Konformitätsmodell; im untersuchten Patternkern kein separates maschinenlesbares Komponenten-/Domänenaustauschschema. HTML/JS-Referenzbeispiele sind Implementierungen, kein dadurch vorhandenes APG-Contractformat.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C339

- **Kandidat / Anforderung:** APG; G02; **D**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP0/AP1 beschreiben Tastatur-, Fokus- und Rollenregeln ohne erforderliche JS-/React-Funktionssprache. D in der Pattern-/Guidance-Rolle, keine neutral ausführbare Maschine oder native Konformität; Referenzimplementierung separat JS/DOM.
- **Bedeutung/Grenze:** D im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C340

- **Kandidat / Anforderung:** APG; I01; **R**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP1 Roles/States/Properties ordnet konkret aria-expanded/controls/autocomplete und erlaubte Werte zu und verweist auf ARIA. R für externe semantische Propertytypen, kein allgemeiner öffentlicher API-Propkatalog.
- **Bedeutung/Grenze:** R im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C341

- **Kandidat / Anforderung:** APG; I02; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Der begrenzte APG-Patternumfang AP0/AP1 definiert keinen öffentlichen Eventnamen-/Payloadkatalog. Keydown im Beispiel ist Hostevent, keine allgemeine Komponenten-Eventdeklaration.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C342

- **Kandidat / Anforderung:** APG; I03; **D**.
- **Quellen:** [S55](SOURCES.md#s55); E2. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP1 und AP4 benennen Input, Popup/Listbox, Button und Optionen; AP5-Constructor bindet comboboxNode/buttonNode/listboxNode und Optionselemente. D für strukturiert benannte Beispiel-/Patternteile, kein universelles serialisiertes Anatomieschema.
- **Bedeutung/Grenze:** D im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C343

- **Kandidat / Anforderung:** APG; V01; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** APG-Patternregeln definieren keinen eigenen Designwert-/Token-Typenkatalog. AP6 enthält echte CSS-Beispielwerte, die hier nicht als allgemeines APG-Designmodell zugerechnet werden.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C344

- **Kandidat / Anforderung:** APG; V02; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Fokus-/Hoverdarstellung in AP6 ist illustrative CSS-Präsentation eines Beispiels. Der definierte Guide besitzt keine eigene Variantensprache mit verbindlichen Style-/Tokenmaps für Komponenten.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C345

- **Kandidat / Anforderung:** APG; V03; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Im untersuchten APG-Patternkern kein eigener Theme-/Mode-Resolver. Hinweise zu High Contrast sind Accessibility-Anforderungen, kein vollständiges Token-Themeformat.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C346

- **Kandidat / Anforderung:** APG; V04; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** APG definiert keine allgemeine formale Anker-/Abstandsnotation. AP6 verwendet konkrete CSS-Positionen; das ist kein vom Pattern vorgeschriebener geometrischer Contract.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C347

- **Kandidat / Anforderung:** APG; V05; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP6 verwendet max-height:250px als illustrative Beispielentscheidung. AP0/AP1 definieren kein allgemeines maximales Flächen-/Zeilenmodell; keine Fünf-Zeilen-Regel ableiten.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C348

- **Kandidat / Anforderung:** APG; V06; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP5/AP6 zeigen scrollIntoView und CSS-overflow im Beispiel. Keine eigene abstrakte Overflow-/Scrollsprache im definierten Guide; realer Beispielbeitrag wird ausdrücklich nicht mit einem APG-Layoutstandard gleichgesetzt.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C349

- **Kandidat / Anforderung:** APG; B01; **A**.
- **Quellen:** [S55](SOURCES.md#s55); E2. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP1 beschreibt Aktionen bei offenem/geschlossenem Popup; AP5 enthält open/close und konkrete Ereignishandler. Übertragung dieser vorhandenen Weblogik in eine formale neutrale Zustands-/Transitiondatei benötigt ein explizites Adaptermodell.
- **Bedeutung/Grenze:** A im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C350

- **Kandidat / Anforderung:** APG; B02; **A**.
- **Quellen:** [S55](SOURCES.md#s55); E2. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP5 enthält tatsächliche Bedingungen etwa verfügbare Optionen/Fokus und Aktionen zur Auswahl/Öffnung, AP1 erläutert optionale Interaktionen. Konkrete JS-Implementierung vorhanden, kein generisches APG-Guard-/Actionformat; formale Übertragung nötig.
- **Bedeutung/Grenze:** A im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C351

- **Kandidat / Anforderung:** APG; B03; **A**.
- **Quellen:** [S55](SOURCES.md#s55); E2. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP5 verarbeitet event.key, Filtertext, gefilterte Optionen und aktuellen Wert in JS. Dokumentierter Datenverarbeitungsmechanismus, aber kein sprachneutrales Context-/Eventdatenschema; für getrennten Behaviorvertrag zu übersetzen.
- **Bedeutung/Grenze:** A im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C352

- **Kandidat / Anforderung:** APG; B04; **D**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP1/AP2 verknüpfen Pfeile, Enter, Escape und Fokus ausdrücklich mit UI-Aktionen. D als dokumentierte Patternbindung; optionale Varianten vorher wählen und Beispielcode nicht pauschal als Produktprofil übernehmen.
- **Bedeutung/Grenze:** D im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C353

- **Kandidat / Anforderung:** APG; A01; **R**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP1 Rollen-/State-/Propertyabschnitt übernimmt Bedeutung aus den verlinkten WAI-ARIA-Definitionen und konkretisiert Beziehungen im Pattern. R zeigt externe normative Semantik; Guide ist selbst kein normativer Rollenstandard.
- **Bedeutung/Grenze:** R im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C354

- **Kandidat / Anforderung:** APG; A02; **D**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP1/AP2 liefern referenzierbare Combobox- und Tastatur-/Fokusmuster. Bestehendes D bleibt; keine tatsächliche Konformitäts-/AT-Prüfung durch bloßen Verweis.
- **Bedeutung/Grenze:** D im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C355

- **Kandidat / Anforderung:** APG; A03; **D**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP3 Alert Pattern beschreibt dynamische Meldung ohne Fokusübernahme sowie Grenzen bei initial vorhandenen Alerts und Unterbrechungshäufigkeit. Direkter Patternbeitrag, kein universeller Ergebnisansagen-Automat; echte Screenreaderunterstützung ungeprüft.
- **Bedeutung/Grenze:** D im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C356

- **Kandidat / Anforderung:** APG; X01; **U**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** APG lässt sich als unabhängige Accessibility-Anforderungsquelle referenzieren. Frage: Wie werden vier getrennte Originalartefakte ohne doppelte Führung und stilles Umdefinieren der Patternvarianten verbunden?
- **Bedeutung/Grenze:** U im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** APG lässt sich als unabhängige Accessibility-Anforderungsquelle referenzieren. Frage: Wie werden vier getrennte Originalartefakte ohne doppelte Führung und stilles Umdefinieren der Patternvarianten verbunden?

## C357

- **Kandidat / Anforderung:** APG; X02; **D**.
- **Quellen:** [S55](SOURCES.md#s55); E2. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP4/AP5 benutzen konkrete Element-/Option-IDs für aria-activedescendant und Beziehungselemente. D im ausgewählten Web-Referenzbeispiel, kein stabiler Mehrfachinstanz-/Export-/URN-Standard des gesamten Guides.
- **Bedeutung/Grenze:** D im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C358

- **Kandidat / Anforderung:** APG; X03; **U**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Patternlinks und DOM-ID-Verweise sind konkrete Teilbindungen. Frage: Welches Paketprofil adressiert Ziele in separat beschriebenen Interface-/Visual-/Behavior-Artefakten semantisch und überprüfbar?
- **Bedeutung/Grenze:** U im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Patternlinks und DOM-ID-Verweise sind konkrete Teilbindungen. Frage: Welches Paketprofil adressiert Ziele in separat beschriebenen Interface-/Visual-/Behavior-Artefakten semantisch und überprüfbar?

## C359

- **Kandidat / Anforderung:** APG; X04; **U**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP1 verbindet Popupmuster mit Combobox und AP5 instanziiert eine JS-Beispielklasse. Frage: Wie werden autonome Unterkomponenten mit eigenen Parametern/Kontexten und versionierten Definitionen als Contract komponiert? Kein neutraler Overlay/ScrollArea-Nachweis.
- **Bedeutung/Grenze:** U im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** AP1 verbindet Popupmuster mit Combobox und AP5 instanziiert eine JS-Beispielklasse. Frage: Wie werden autonome Unterkomponenten mit eigenen Parametern/Kontexten und versionierten Definitionen als Contract komponiert? Kein neutraler Overlay/ScrollArea-Nachweis.

## C360

- **Kandidat / Anforderung:** APG; X05; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Im definierten Pattern-/Beispielmodell kein externer versionierter Komponenten-/Teilmodellresolver. Gepinnter Git-Stand sichert die Quelle, keine APG-eigene Contract-Abhängigkeitsauflösung.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C361

- **Kandidat / Anforderung:** APG; X06; **U**.
- **Quellen:** [S55](SOURCES.md#s55); E2. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP7/Repository dokumentiert reale HTML-/CSS-/JS-Linter und Beispielregressionstests. Frage: Welches originale separate A11y-/Patternartefaktschema und Werkzeug prüft unveränderte Contractdateien? Beispielcodevalidierung ist keine Antwort auf diese Frage.
- **Bedeutung/Grenze:** U im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** AP7/Repository dokumentiert reale HTML-/CSS-/JS-Linter und Beispielregressionstests. Frage: Welches originale separate A11y-/Patternartefaktschema und Werkzeug prüft unveränderte Contractdateien? Beispielcodevalidierung ist keine Antwort auf diese Frage.

## C362

- **Kandidat / Anforderung:** APG; X07; **N**.
- **Quellen:** [S55](SOURCES.md#s55); E2. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP7 testet konkrete Beispiele und Quelltextqualität, keine gemeinsame Referenz-/Instanz-/fachliche Konfliktprüfung von vier externen Domänen. Nicht behaupten, dass APG keine Tests hat.
- **Bedeutung/Grenze:** N im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C363

- **Kandidat / Anforderung:** APG; X08; **U**.
- **Quellen:** [S55](SOURCES.md#s55); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** AP0 erklärt nichtnormativen Status und Beziehung zu ARIA/WCAG; dies klärt Quellenrollen teilweise. Frage: Welche per-information Ownership-/Änderungsregel verbindet Guide, Produktprofil und drei weitere Originalformate?
- **Bedeutung/Grenze:** U im begrenzten Beitrag informativer Patternguide und ausdrücklich bezeichnete Web-Referenzbeispiele, kein normativer Gesamtcontract. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** AP0 erklärt nichtnormativen Status und Beziehung zu ARIA/WCAG; dies klärt Quellenrollen teilweise. Frage: Welche per-information Ownership-/Änderungsregel verbindet Guide, Produktprofil und drei weitere Originalformate?

## C364

- **Kandidat / Anforderung:** CSS Layout; G01; **D**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** SYNTAX §§3–5 definiert maschinenlesbare Stylesheets, Regeln und Deklarationen; ANCHOR/OVERFLOW besitzen formale Propertygrammatiken und Semantik. CSS als textuelle Sprache erfüllt die Datensyntax für den Fachbeitrag; JSON/YAML ist nicht erforderlich.
- **Bedeutung/Grenze:** D im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C365

- **Kandidat / Anforderung:** CSS Layout; G02; **D**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Zentrale Einordnung nach G02: CSS-Wert-/Layoutsemantik verlangt keine React-/JavaScript-Funktionen. D gilt im deklarativen CSS-Fachbeitrag; fehlende rendererneutrale oder native Bindung bleibt ausdrücklich unbewiesen. Bericht schlug konservativ A vor; die reine Plattformfrage ist jedoch nicht mit dem definierten Sprachkriterium gleichzusetzen.
- **Bedeutung/Grenze:** D im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C366

- **Kandidat / Anforderung:** CSS Layout; I01; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** CSS-Propertywerttypen sind keine nachgewiesenen öffentlichen Komponenten-API-Typmetadaten. Frage: Welches separat referenzierte Komponentenmodell definiert öffentliche Inputs und bindet sie an diese Deklarationen?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** CSS-Propertywerttypen sind keine nachgewiesenen öffentlichen Komponenten-API-Typmetadaten. Frage: Welches separat referenzierte Komponentenmodell definiert öffentliche Inputs und bindet sie an diese Deklarationen?

## C367

- **Kandidat / Anforderung:** CSS Layout; I02; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Kein ausreichender Nachweis öffentlicher Komponentenereignisse mit Payload in den gelesenen Layoutquellen. Frage: Welches Ereignisschema bindet den Layoutbeitrag an öffentliche Events?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Kein ausreichender Nachweis öffentlicher Komponentenereignisse mit Payload in den gelesenen Layoutquellen. Frage: Welches Ereignisschema bindet den Layoutbeitrag an öffentliche Events?

## C368

- **Kandidat / Anforderung:** CSS Layout; I03; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** anchor-name benennt Anker, keine geprüfte Komponenten-Anatomie. Frage: Wie werden Input/Overlay/ScrollArea als Komponentenbestandteile definiert und an CSS-Elemente gebunden?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** anchor-name benennt Anker, keine geprüfte Komponenten-Anatomie. Frage: Wie werden Input/Overlay/ScrollArea als Komponentenbestandteile definiert und an CSS-Elemente gebunden?

## C369

- **Kandidat / Anforderung:** CSS Layout; V01; **R**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ANCHOR/OVERFLOW §1.1 referenzieren VALUES; VALUES §5 definiert dimensionierte Längen, relative/absolute Einheiten und Auflösung. Unterstützt typisierte Dimensionen, nicht automatisch ein vollständiges Design-Token-, Farb- oder Typografiemodell.
- **Bedeutung/Grenze:** R im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C370

- **Kandidat / Anforderung:** CSS Layout; V02; **N**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Im begrenzten ANCHOR/OVERFLOW-Kern keine benannten visuellen UX-Zustandsvarianten. ANCHOR §6 position-try/@position-try definiert geometrische Ausweichoptionen bei Überlauf, keine Zustandsvarianten einer UX-Maschine. Selektoren, Cascade- oder Animationsmodule wurden nicht zu diesem Kandidaten erweitert.
- **Bedeutung/Grenze:** N im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C371

**Fortschreibung der Gesamtprüfung:** Aktueller Befund [C412](#c412); der folgende Text dokumentiert den früheren Stand.

- **Kandidat / Anforderung:** CSS Layout; V03; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Theme-/Dark-Mode-Auswahl liegt außerhalb der geprüften Kernmodule. Frage: Soll ein separat zu prüfendes CSS-Modul für Modusauswahl eingebunden werden, und wie wäre dessen Bindung an Contract-Modi?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Theme-/Dark-Mode-Auswahl liegt außerhalb der geprüften Kernmodule. Frage: Soll ein separat zu prüfendes CSS-Modul für Modusauswahl eingebunden werden, und wie wäre dessen Bindung an Contract-Modi?

## C372

- **Kandidat / Anforderung:** CSS Layout; V04; **D**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ANCHOR §§2.1–2.4: anchor-name, anchor-scope, position-anchor und Zielauflösung; §3.1 position-area; §3.2 anchor() mit Seite/Richtung und Länge; VALUES calc() erlaubt zusätzlichen Abstand. §5 anchor-size() liefert relative Größe. D innerhalb CSS-Boxmodell.
- **Bedeutung/Grenze:** D im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C373

- **Kandidat / Anforderung:** CSS Layout; V05; **R**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** OVERFLOW referenziert max-height nach SIZING §3.1.3; SIZING §§3.2–3.3 definiert nichtnegative Größen und Content-/Border-Boxbezug. Maximalhöhe ist formal; fünf sichtbare Einträge bei variablen Zeilenhöhen folgen daraus nicht. Minimum/Maximum, Padding, Border, Schreibmodus und Prozentbasis gehören zur konkreten Bindung.
- **Bedeutung/Grenze:** R im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C374

- **Kandidat / Anforderung:** CSS Layout; V06; **D**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** OVERFLOW §§2–3 definiert scrollable overflow area/scrollport und overflow-x/-y: visible, hidden, clip, scroll, auto. hidden bleibt programmatisch scrollbar, clip verbietet Scrollen, auto hängt von tatsächlichem Overflow ab. Daraus folgt keine sichtbare Elementzahl.
- **Bedeutung/Grenze:** D im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C375

- **Kandidat / Anforderung:** CSS Layout; B01; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Positionierungsfallback ist keine geprüfte Ereigniszustandsmaschine. Frage: Welches Behavior-Modell liefert Initialzustand, Ereignisse und Übergangsziele und bindet Styles daran?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Positionierungsfallback ist keine geprüfte Ereigniszustandsmaschine. Frage: Welches Behavior-Modell liefert Initialzustand, Ereignisse und Übergangsziele und bindet Styles daran?

## C376

- **Kandidat / Anforderung:** CSS Layout; B02; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Geometrische Bedingungen/Ausweichregeln sind kein Nachweis von UX-Guards und Aktionen. Frage: Wo sind Auswertung und Ausführung der Contract-Aktionen definiert?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Geometrische Bedingungen/Ausweichregeln sind kein Nachweis von UX-Guards und Aktionen. Frage: Wo sind Auswertung und Ausführung der Contract-Aktionen definiert?

## C377

- **Kandidat / Anforderung:** CSS Layout; B03; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Keine ausreichende Zustands-/Ereignisdatenmodellierung für Produktlogik geprüft. Frage: Welche separat typisierten Kontext-/Eventdaten steuern die Bindung?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Keine ausreichende Zustands-/Ereignisdatenmodellierung für Produktlogik geprüft. Frage: Welche separat typisierten Kontext-/Eventdaten steuern die Bindung?

## C378

- **Kandidat / Anforderung:** CSS Layout; B04; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Scrollmechanismus ist keine ausdrückliche Abbildung von Tastatur/Fokus auf UX-Aktionen. Frage: Welches Input-/Behavior-Binding übernimmt diese Zuordnung?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Scrollmechanismus ist keine ausdrückliche Abbildung von Tastatur/Fokus auf UX-Aktionen. Frage: Welches Input-/Behavior-Binding übernimmt diese Zuordnung?

## C379

- **Kandidat / Anforderung:** CSS Layout; A01; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ANCHOR §9 weist ausdrücklich darauf hin, dass visuelle Beziehung keine sinnvolle DOM-/zugängliche Beziehung erzeugt; verweist auf HTML/ARIA. Frage: Welches konkrete semantische Zielmodell und Mapping wird für das Paket gewählt? Fremdmodellreferenz allein wird nicht als vollständige Abdeckung gezählt.
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** ANCHOR §9 weist ausdrücklich darauf hin, dass visuelle Beziehung keine sinnvolle DOM-/zugängliche Beziehung erzeugt; verweist auf HTML/ARIA. Frage: Welches konkrete semantische Zielmodell und Mapping wird für das Paket gewählt? Fremdmodellreferenz allein wird nicht als vollständige Abdeckung gezählt.

## C380

- **Kandidat / Anforderung:** CSS Layout; A02; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ANCHOR §9 erläutert Risiken nichtgrafischer Navigation, liefert kein vollständig geprüftes referenzierbares Interaktionsmuster. Frage: Welches APG-/plattformbezogene Muster bestimmt Fokus und Tasten?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** ANCHOR §9 erläutert Risiken nichtgrafischer Navigation, liefert kein vollständig geprüftes referenzierbares Interaktionsmuster. Frage: Welches APG-/plattformbezogene Muster bestimmt Fokus und Tasten?

## C381

- **Kandidat / Anforderung:** CSS Layout; A03; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Keine nachgewiesene Accessible-Update-Semantik im Layoutkern. Frage: Welche ARIA-/Plattformregel bindet Ereignis, Meldung und Zeitpunkt an zugängliche Rückmeldung?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Keine nachgewiesene Accessible-Update-Semantik im Layoutkern. Frage: Welche ARIA-/Plattformregel bindet Ereignis, Meldung und Zeitpunkt an zugängliche Rückmeldung?

## C382

- **Kandidat / Anforderung:** CSS Layout; X01; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** CSS kann den Visualteil als Stylesheet führen; damit sind noch keine vier unabhängigen Contractartefakte samt gemeinsamen Bindungen nachgewiesen. Frage: Welches Paketprofil erhält vier Domänen ohne versteckte fachfremde Pflichtdefinitionen?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** CSS kann den Visualteil als Stylesheet führen; damit sind noch keine vier unabhängigen Contractartefakte samt gemeinsamen Bindungen nachgewiesen. Frage: Welches Paketprofil erhält vier Domänen ohne versteckte fachfremde Pflichtdefinitionen?

## C383

- **Kandidat / Anforderung:** CSS Layout; X02; **A**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ANCHOR §2.1 explizite anchor-name-Bindungsnamen und §2.2 anchor-scope liefern konkreten Referenzmechanismus. Namen müssen nicht eindeutig sein; §2.3 wählt über Scope, Akzeptabilität und Baumreihenfolge. Für instanzstabile gemeinsame Identität ist zusätzliches ID-/Scope-Mapping nötig. Kein direkter UI-Instanz-ID-Standard.
- **Bedeutung/Grenze:** A im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C384

- **Kandidat / Anforderung:** CSS Layout; X03; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Ankerreferenzen zielen auf Elemente im CSS-Baum, nicht auf separat beschriebene Behavior-/Interface-/A11y-Domänen. Frage: Welche dokumentierte externe Domänenbindung adressiert diese Ziele eindeutig?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** Ankerreferenzen zielen auf Elemente im CSS-Baum, nicht auf separat beschriebene Behavior-/Interface-/A11y-Domänen. Frage: Welche dokumentierte externe Domänenbindung adressiert diese Ziele eindeutig?

## C385

- **Kandidat / Anforderung:** CSS Layout; X04; **N**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** Vollständiger Property-/Regelkern von ANCHOR/OVERFLOW definiert geometrische Beziehungen und Ausweichdeklarationen, keine Trennung von Komponentendefinition und parametrisierter Instanziierung. Wiederbenutzte Ankernamen/-Scopes oder Styles erzeugen keine Komponente mit Instanzkontext. Nur Aussage über diesen Kern.
- **Bedeutung/Grenze:** N im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C386

- **Kandidat / Anforderung:** CSS Layout; X05; **N**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** In ANCHOR/OVERFLOW kein Mechanismus für externe Komponenten-/Teilmodellreferenz mit gebundener Version und Auflösung. Spezifikations-URLs versionieren die Normlektüre, keine Abhängigkeit einer UI-Instanz. Stylesheetimport-/Paketverwaltung wurde nicht als zusätzliche Kandidatenfähigkeit unterstellt.
- **Bedeutung/Grenze:** N im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C387

**E3-Fortschreibung:** [C423](#c423) enthält die tatsächliche Checkerprobe; folgender Text ist der frühere Stand.

- **Kandidat / Anforderung:** CSS Layout; X06; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** SYNTAX §3 enthält Anforderungen an Parser und Conformance Checker, aber CSS hat hier kein JSON/XSD-Originalschema; reine Parserregeln belegen kein aktuelles Tool mit Unterstützung exakt dieser Anchor-/Overflow-Stände. Frage: Welcher konkrete Originalchecker kann getrennte Artefakte gegen welche Modulversionen prüfen? Kein Prüftool ausgeführt.
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** SYNTAX §3 enthält Anforderungen an Parser und Conformance Checker, aber CSS hat hier kein JSON/XSD-Originalschema; reine Parserregeln belegen kein aktuelles Tool mit Unterstützung exakt dieser Anchor-/Overflow-Stände. Frage: Welcher konkrete Originalchecker kann getrennte Artefakte gegen welche Modulversionen prüfen? Kein Prüftool ausgeführt.

## C388

- **Kandidat / Anforderung:** CSS Layout; X07; **N**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** ANCHOR §2.3/§3.2 regelt lokale Zielauflösung/ungelöste Funktionen und Fallback; SYNTAX behandelt Parsefehler. Mehrfachnamen sind erlaubt und werden aufgelöst statt als Instanzkollision abgewiesen. Keine Prüfung domänenübergreifender Vertragskonflikte im begrenzten Kern.
- **Bedeutung/Grenze:** N im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund. Keine pauschale Aussage über andere Host-/Frameworkmodelle oder eine neue Integrationsschicht; fehlender Fund allein wäre U.
- **Offene Frage / weiterer Bedarf:** Spätere Produkt-/Host-/Plattformbindung und Originalprüfwerkzeuge gezielt bestimmen; Spezifikations- oder Beispielcodebefund ist kein ausgeführter Konformitätsnachweis.

## C389

- **Kandidat / Anforderung:** CSS Layout; X08; **U**.
- **Quellen:** [S56](SOURCES.md#s56); E1. Lokale Kürzel im Befund sind dort vollständig aufgelöst.
- **Befund:** CSS-Reihenfolge/Scope oder Fallback sind keine nachgewiesene Ownership und Änderungsverfolgung zwischen Originalformaten. Frage: Welche Paketregel weist jeder Information eine führende Quelle und nachvollziehbare Änderungen zu?
- **Bedeutung/Grenze:** U im begrenzten Beitrag CSS Anchor Positioning 1 und Overflow 3 mit normativ referenzierten Syntax-/Values-/Sizing-Beiträgen. Die genaue Rollen-/Nachweisgrenze steht im Befund.
- **Offene Frage / weiterer Bedarf:** CSS-Reihenfolge/Scope oder Fallback sind keine nachgewiesene Ownership und Änderungsverfolgung zwischen Originalformaten. Frage: Welche Paketregel weist jeder Information eine führende Quelle und nachvollziehbare Änderungen zu?


## C390

- **Gegenstand:** UXSpec: Import- und Modulgrenzen; Anforderungen X03, X05, X07. Integrationsfolgeprüfung, keine neue Kandidatenbewertung.
- **Quelle:** [S57](SOURCES.md#s57), gepinnte Primärdateien, manuell über BrowserOS neo gelesen.
- **Befund:** Der gepinnte import-resolver.ts liest lokale JSON-Dateien und übernimmt angeforderte $tokens/$elements/$animations/$machine. Fehlt ein angeforderter Bereich, erzeugt diese Funktion dafür keine eigene Diagnose; eine spätere Verwendung kann scheitern. bundler.ts kompiliert direkte Maschinenabhängigkeiten und löst deren Imports auf, trägt Module aber ohne ausdrückliche Kollisionsabweisung nach Maschinen-ID ein. Die Aufrufe teilen keine durchgehende ancestorPaths-Menge; ein vollständiger transitiver Modulabschluss beziehungsweise allgemeine Zyklusprüfung ist dadurch nicht nachgewiesen.
- **Bedeutung/Grenze:** E2 für diese Quellpfade; kein CLI-/Laufzeitversuch. Bestehendes X05=N und X07=N im begrenzten Originalkern werden präzisiert; X03 bleibt U. Eine vorhandene IMPORT_CYCLE-Diagnose darf nicht als vollständiger Graphnachweis gelten.
- **Nächste Prüfung:** Doppelte Maschinen-IDs, A→B→A und A→B→C sowie angeforderte fehlende Bereiche bei gesondertem praktischem Auftrag prüfen.

## C391

- **Gegenstand:** UXSpec: Geltungsbereich verschachtelter Elementreferenzen; Anforderungen X03, X04, X07. Integrationsfolgeprüfung, keine neue Kandidatenbewertung.
- **Quelle:** [S57](SOURCES.md#s57), gepinnte Primärdateien, manuell über BrowserOS neo gelesen.
- **Befund:** resolve.ts qualifiziert in importierten Elementen unqualifizierte Tokenreferenzen mit dem Importalias. expandRefs übergibt nach importierter Elementexpansion jedoch weiterhin das lokale elements-Verzeichnis. Verschachtelte unqualifizierte Element-$ref werden dort lokal gesucht. Instanzargumente werden flach über die Basis gelegt; Parameterersetzung ist kein Nachweis eines eigenständigen Child-Machine-Lebenszyklus.
- **Bedeutung/Grenze:** E2 Quellbefund. Ableitung: Ein importierter Unterverweis kann einen lokalen Namensvetter meinen; diese Folge wurde nicht ausgeführt. Bestehendes X04=D für parametrisierte Elemente bleibt bestehen, keine Aufwertung von X03.
- **Nächste Prüfung:** Gleichnamige lokale/importierte Unterelemente und explizite Aliasbindung gegenüberstellen; resultierende Identität und Informationsverlust prüfen.

## C392

- **Gegenstand:** Ark UI: Kontext- und ID-Grenzen; Anforderungen X02, X04, X08. Integrationsfolgeprüfung, keine neue Kandidatenbewertung.
- **Quelle:** [S57](SOURCES.md#s57), gepinnte Primärdateien, manuell über BrowserOS neo gelesen.
- **Befund:** use-combobox.ts und use-scroll-area.ts erzeugen jeweils useId und einen eigenen useMachine-Kontext. Abschließendes ...props überschreibt vorherige Vorgaben. In use-combobox.ts ersetzt ein übergebenes ids-Objekt die vorher gesetzten Field-label/input-IDs ohne tiefe Zusammenführung in dieser Funktion.
- **Bedeutung/Grenze:** E2 im React-Adapter am gepinnten Stand. Getrennte Kontexte und explizite IDs sind vorhanden; keine Garantie stabiler neutraler Contract-Identität oder konfliktfreier Overlay-/ScrollArea-Komposition. Bestehende Matrixbewertungen bleiben unverändert.
- **Nächste Prüfung:** Explizite IDs für zwei Instanzen, Field-Verknüpfung, Umordnung und Overlay-/Viewport-Bindung bei gesondertem praktischem Auftrag prüfen.

## C393

- **Gegenstand:** OpenPencil: partielle Bindungsprüfung und Exportverlust; Anforderungen X03, X06, X07, X08. Integrationsfolgeprüfung, keine neue Kandidatenbewertung.
- **Quelle:** [S57](SOURCES.md#s57), gepinnte Primärdateien, manuell über BrowserOS neo gelesen.
- **Befund:** spec.ts prüft bestimmte Propertynamen/-typen, Value-/Part-IDs und doppelte Slotbelegung. Boolean-Varianten werden gegen Optionen geprüft; resolveStates kombiniert heuristische Zustände und explizite Werte ohne dort entsprechenden vollständigen Optionsabgleich. behaviourToSpec lässt unauflösbare Namen/Bindungen aus.
- **Bedeutung/Grenze:** E2 im gepinnten Scenegraph-Pfad. Keine vollständige Zustands-/Vier-Domänen-Prüfung und kein verlustfreier Roundtrip daraus ableiten. X06=D für den bestehenden Originalschema-Beitrag bleibt bestehen; keine automatische Änderung anderer Matrixzellen.
- **Nächste Prüfung:** Ungültige Statewerte, entfernte Properties und doppelte Namen als getrennte negative Fälle ausarbeiten und später prüfen.

## C394

- **Gegenstand:** CEM und UXSpec: unterschiedliche Typziele; Anforderungen I01, I02, X03. Integrationsfolgeprüfung.
- **Quelle:** [S58](SOURCES.md#s58); E2, begrenzte Primärquellenprüfung über BrowserOS neo.
- **Befund:** CEM Event.type beschreibt das ganze Eventobjekt über Type.text und optionale Referenzen. UXSpec eventSpec.payload führt Felder über contextField; dessen Typenum enthält object/array, aber keinen rekursiven Properties-/Itemsvertrag in dieser Definition. Eine Emit-Aktion und gleichnamige Ereignisse definieren keine gemeinsame öffentliche Payloadprojektion.
- **Bedeutung/Grenze:** Manuelle Prüfung gepinnter Originaldefinitionen. Einfache typgebundene Zuordnungen sind als Arbeitsfall möglich; allgemeine strukturelle Typkompatibilität und CustomEvent.detail-Abbildung sind nicht nachgewiesen. Keine neue Matrixbewertung.
- **Nächste Prüfung:** Für ein einfaches öffentliches Auswahlereignis Quellwert, Zielpayload, Ereignisobjekt und Adapterkonvention ausdrücklich binden; komplexe Typen separat prüfen.

## C395

- **Gegenstand:** DTCG-Dimension und UXSpec-Auflösung: Einheit erhalten; Anforderungen V01, X03. Integrationsfolgeprüfung.
- **Quelle:** [S58](SOURCES.md#s58); E2, begrenzte Primärquellenprüfung über BrowserOS neo.
- **Befund:** DTCG Format 2025.10 §8.2 verlangt dimension mit numerischem value und unit px/rem. UXSpec resolveTokenValue reduziert im gelesenen Pfad ein Objekt mit genau numerischem value und String-unit auf die Zahl. Eine entsprechende Integration kann damit Einheiteninformation verlieren; ein eigenständiges DTCG-Rootdokument ist nicht allein aufgrund ähnlicher Tokenfelder ein UXSpec-Import.
- **Bedeutung/Grenze:** E1 für DTCG-Regel, E2 für Resolver. Informationsverlust ist eine Ableitung aus dem Quellpfad, kein ausgeführter Import-/Runtimeversuch und kein pauschales Urteil über sämtliche Adapter. Keine neue Matrixbewertung.
- **Nächste Prüfung:** Bei konkreter Importkette px/rem getrennt prüfen, Originaleinheit und Adapterumrechnung nachvollziehbar erhalten; Geometrieziel separat binden.

## C396

- **Gegenstand:** ARIA-/APG-Bindung: Zielrelation und Auswahlbegriffe; Anforderungen A01, A02, X03, X08. Integrationsfolgeprüfung.
- **Quelle:** [S58](SOURCES.md#s58); E1, begrenzte Primärquellenprüfung über BrowserOS neo.
- **Befund:** WAI-ARIA 1.2 aria-activedescendant verlangt zulässige Eigentums- beziehungsweise Kontrollbeziehungen und referenziert ein aktives Element; ein existierendes ID-Ziel allein genügt nicht. Das gelesene APG-Combobox-Muster führt DOM-Fokus, Popupbezug und aria-selected auf und beschreibt Auswahlfolge im Popup.
- **Bedeutung/Grenze:** Semantik und Patternempfehlung getrennt. Für den vorgeschlagenen Webfall sind aktive Option, zugänglich gemeldete Popupauswahl und bestätigter Produktwert ausdrücklich zuzuordnen; keine automatische Aussage, Navigation habe keine Auswahlsemantik. Kein Browser-/Assistenztechniktest und keine neue Matrixbewertung.
- **Nächste Prüfung:** Fachliche Teile auf echte Input-/Listbox-/Option-Elemente derselben Instanz abbilden; ARIA-Relationen, Produktbestätigung und Scrollzuständigkeit getrennt prüfen.

## C397

**E3-Fortschreibung:** aktueller Befund [C420](#c420); folgender Text dokumentiert den früheren Stand.

- **Kandidat / Anforderung:** UXSpec; V04; **U**. Ankergeometrie bleibt ungeklärt.
- **Quelle:** [S59](SOURCES.md#s59); E1/E2, begrenzte manuelle Original-/Rendererprüfung.
- **Befund:** SPEC und Formatreferenz definieren die Layoutprimitiven stack-h/stack-v/grid/layer. Der erneut vollständig gelesene Stylemapper bindet layer an relative Positionierung; LayerContainer setzt Kindwrapper absolut mit top/left/right/bottom 0. Das ist eine konkrete lokale Überlagerung, kein belegter Bezug auf ein separat benanntes Inputziel mit Richtung und Abstand.
- **Bedeutung/Grenze:** Die zusätzlichen Rendererpfade präzisieren den Teilbeitrag. Kein N aus fehlendem Treffer, keine freie Ankereigenschaft als Standard ausgegeben und kein Praxisversuch.
- **Nächste Prüfung:** Welche originale normative Eigenschaft oder dokumentierte Bindung ergänzt Zielidentität, Richtung und Abstand über die lokalen Layerwrapper hinaus? Andere Renderer/Erweiterungen gezielt und getrennt prüfen.

## C398

- **Kandidat / Anforderung:** UXSpec; V05; **A**. Maximale Größe über vorhandenen Webadapter.
- **Quelle:** [S59](SOURCES.md#s59); E1/E2, begrenzte manuelle Original-/Rendererprüfung.
- **Befund:** style-map.ts mapSize liest size.maxWidth und size.maxHeight und übersetzt sie über normalizeDimension in CSS maxWidth/maxHeight. mapContainerStyle und mapElementStyle verwenden mapSize; containers.tsx ruft beide auf und setzt das Ergebnis als style am gerenderten div. normalizeDimension verarbeitet Zahlen, Strings und value/unit-Objekte; Zahlen werden in diesem Pfad als px behandelt.
- **Bedeutung/Grenze:** Gezielt erweiterter E2-Nachweis des Aufrufpfads, keine Ausführung. U wird zu A gemäß Methodenregel: vorhandener konkreter Mechanismus, zusätzliche Bindung für den neutralen Visualvertrag nötig. Kein D für eine vollständig typisierte normative Layoutsprache; beliebige Strings/any bleiben unzureichend validiert. Fünf variable Zeilen und native Geometrie sind nicht bewiesen.
- **Nächste Prüfung:** Bei späterem praktischem Auftrag eine gültige/falsche Dimension und variable Zeilenhöhen prüfen; neutrales Visualfeld, Einheit, Containerziel und Adapter ausdrücklich binden.

## C399

**E3-Fortschreibung:** aktueller Befund [C420](#c420); folgender Text dokumentiert den früheren Stand.

- **Kandidat / Anforderung:** UXSpec; V06; **U**. Overflow und Scrollen bleiben ungeklärt.
- **Quelle:** [S59](SOURCES.md#s59); E1/E2, begrenzte manuelle Original-/Rendererprüfung.
- **Befund:** Die erneut gelesenen SPEC-/Formatreferenzdefinitionen liefern keinen hinreichenden formalen Overflowvertrag. Der vollständige Stylemapper setzt keine overflow-/overflowX-/overflowY-Eigenschaft. Die gelesenen Containerfunktionen geben keine solche Contracteigenschaft weiter. Maximale Höhe erzeugt allein keine definierte Scrollsemantik.
- **Bedeutung/Grenze:** Auf diese Definitionen und Rendererpfade begrenzter E1/E2-Befund; keine Behauptung, im gesamten Repository gebe es nirgendwo scrollendes CSS oder andere Renderer. U bleibt bestehen.
- **Nächste Prüfung:** Welche originale Definition benennt Scrollcontainer, Achse und clip/auto/scroll samt Semantik? Vorschau-/Host-CSS und eine mögliche zusätzliche Layoutbindung ausdrücklich getrennt prüfen.

## C400

- **Kandidat / Anforderung:** uSpec; V04; **U**. uSpec-Anker ist ein Mess-/Dokumentationsziel.
- **Quelle:** [S60](SOURCES.md#s60); manuelle begrenzte E1/E2-Prüfung.
- **Befund:** STR beschreibt section._anchor durch layerName/layerId/variantId/variantName/variantProperties und ordnet es je Abschnitt einem Figma-Quellknoten zu. phaseE.ts extrahiert Layout-/Maßdaten; treeFlat bildet absolute Koordinaten relativ zur Variantenwurzel als bbox ab. Das ist keine belegte dynamische Overlay→Input-Bindung mit Richtung und Abstand.
- **Bedeutung/Grenze:** Gezielte E1/E2-Folgeprüfung. U bleibt bestehen: Quellknotenidentität, statische Messkoordinaten und relative Laufzeitgeometrie sind unterschiedliche Bedeutungen. Keine Ausführung oder pauschale Aussage über alle anderen uSpec-Pfade.
- **Nächste Prüfung:** Welcher weitere originale Ausgabe-/Auswertungspfad bindet ein benanntes anderes UI-Ziel mit Richtung/Abstand? Vorhandene _anchor-Felder nicht dafür umdeuten; nötiges zusätzliches Layoutmodell explizit ausweisen.

## C401

- **Kandidat / Anforderung:** uSpec; V06; **U**. uSpec-Basisextraktion erhält Clipping, aber keine belegte Scrollachse.
- **Quelle:** [S60](SOURCES.md#s60); manuelle begrenzte E1/E2-Prüfung.
- **Befund:** phaseE.ts extractDims liest clipsContent und schreibt value/token/display; die gezielt vollständig gelesene Funktion extrahiert keine Scrollrichtung oder auto/scroll-Auswahl. BASE beschreibt erhaltene Wrapper mit Dimensionen/Clipping. STRs Overflowdefinition führt clipsContent true/false. Die konkrete Basisextraktion belegt damit Clipping, nicht eine vollständige Scrollcontainersemantik.
- **Bedeutung/Grenze:** E1/E2 im beschriebenen Basis-/Strukturpfad. U bleibt für das gesamte V06-Kriterium bestehen; keine Behauptung, uSpec oder Figma könnten grundsätzlich nicht scrollen. Ein Variantenname overflow=scroll ersetzt keine fachliche Achsen-/Ausführungsdefinition.
- **Nächste Prüfung:** Andere originale Speicher-/Rendererpfade gezielt auf Scrollrichtung und Scrollcontainer prüfen; falls ein Zusatzmodell nötig ist, Clippingbeitrag und neue Scrollsemantik getrennt dokumentieren.

## C402

- **Kandidat / Anforderung:** OpenUI; X06; **U**. lib/schema.ts ist ein Feldkatalog, Spec.ts ein abweichender TS-Typ.
- **Quelle:** [S61](SOURCES.md#s61); E2, manuelle gezielte Prüfung ohne Ausführung.
- **Befund:** lib/schema.ts definiert eine Map von Feldbeschreibungen. schema-table.tsx erwartet Record<string,SchemaProperty> und rendert diese rekursiv als HTML-Tabelle; es validiert dort kein Contractdokument. Spec.ts verlangt license und component.group, die im Katalog nicht entsprechend geführt werden; enum/required aus dem Katalog fehlen im Typ. Das Paket stellt Next-dev/build/start/lint bereit, keinen in dieser Paketdatei ausgewiesenen Contract-Validator.
- **Bedeutung/Grenze:** Gezielte E2-Prüfung der Originaldateien, kein globaler Beweis fehlender externer Werkzeuge. Ein Feldkatalog ist nicht automatisch ein kanonisches ausführbares JSON Schema. Die frühere Fundstellenangabe §12 Validate wird nicht weitergeführt: Im erneut gelesenen draft-01 heißt §12 Contributing. X06 bleibt U.
- **Nächste Prüfung:** Zuerst die maßgebliche übereinstimmende Originaldefinition und einen offiziellen Validator identifizieren. Ein selbst repariertes Schema wäre eine neue Ergänzung mit offengelegter Abweichung, kein unverändertes Originalschema.

## C403

- **Kandidat / Anforderung:** Google DESIGN.md; X06; **U**. Original-Linter ist verfügbar; Eingabeschema prüft nur den Textwrapper.
- **Quelle:** [S61](SOURCES.md#s61); E2, manuelle gezielte Prüfung ohne Ausführung.
- **Befund:** parser/spec.ts ParserInputSchema prüft content als nichtleeren String. ParsedDesignSystem ist ein TypeScript-Interface mit offenen Fachobjekten. lint.ts ruft Parser, Modellauflösung, runLinter und Ausgabehandler auf; bei recoverable Parsefehler liefert die Library einen Bericht mit Warnung und leerem Modell. index.ts exportiert lint und Regeln.
- **Bedeutung/Grenze:** E2 für diesen Librarypfad. Eine regulär zurückkehrende API oder summary.errors=0 ist nicht gleich vollständige Originalschemakonformität. Daraus folgt kein nachgewiesener CLI-Exitcode. Ein vollständiges unabhängiges Originalartefaktschema bleibt unbestätigt; X06 bleibt U.
- **Nächste Prüfung:** Vollständige fachliche Originalschemaidentität getrennt vom Textwrapper klären und konkrete Pflichtfelder/Regelabdeckung dokumentieren; später Warnungs-/Fehlerpolitik und gültige/ungültige Artefakte praktisch prüfen.

## C404

- **Kandidat / Anforderung:** Panda CSS; X06; **U**. Exportreader prüft ausgewählte Rootformen und vertraut Tabellenzeilen.
- **Quelle:** [S61](SOURCES.md#s61); E2, manuelle gezielte Prüfung ohne Ausführung.
- **Befund:** parseDesignSystem prüft Rootobjekt, nicht-null categories/paths/tokens/values, Arrays für paths/values und numerische schemaVersion mit Obergrenze 1. categories/tokens werden hier nicht vollständig typgeprüft, Zeilen und Referenzintegrität nicht validiert. Der Code nennt die Prüfung ausdrücklich flach.
- **Bedeutung/Grenze:** E2, kein ausgeführter Parser. Aus dem gelesenen Kontrollfluss folgt für einen gezielt beschädigten Root mit categories=7, tokens=false, paths=[], values=[], schemaVersion=1 die Erwartung ok:true; dies ist eine manuelle Ableitung und kein E3-Test. Das belegt die Grenze dieses Readers, nicht die Abwesenheit anderer Validatoren. X06 bleibt U.
- **Nächste Prüfung:** Ein vollständiges offizielles Schema/Prüfwerkzeug für das separate deklarative Visualartefakt identifizieren; Quellkonfiguration und normalisierten Export unterscheiden. Später ungültige Tabellen und Versionen als getrennte Negativfälle ausführen.

## C405

- **Kandidat / Anforderung:** XState; X06; **U**. Schemas, Definition und Snapshot sind getrennte Gegenstände.
- **Quelle:** [S62](SOURCES.md#s62); manuelle E2-Prüfung am gepinnten Originalstand.
- **Befund:** Der gelesene StateMachine-Konstruktor nimmt schemas?:unknown entgegen und weist config.schemas unverändert this.schemas zu. toJSON liefert this.definition. restoreSnapshot greift für Child-Actors auf vorhandene oder referenzierte Actorlogik der Maschine zu.
- **Bedeutung/Grenze:** E2 gezielt im gepinnten Konstruktor-/Serialisierungs-/Restorepfad. Das Schemafeld belegt keine eigene Runtime-Validierung und ein exportierter Gegenstand keine vollständige unabhängige neutrale Logik. Andere Validatoren außerhalb dieser Pfade nicht ausgeschlossen; X06 bleibt U.
- **Nächste Prüfung:** Offiziellen separaten Artefakt-/Schemaeinstieg mit tatsächlicher Prüfsemantik identifizieren; Snapshot, Definition, Implementierungen und Maschineninput für spätere Versuche getrennt festhalten.

## C406

- **Kandidat / Anforderung:** Zag; X06; **U**. Interne Zustandsprüfungen sind teilweise vom Produktionsmodus abhängig.
- **Quelle:** [S62](SOURCES.md#s62); manuelle E2-Prüfung am gepinnten Originalstand.
- **Befund:** state.ts ruft invariant bei doppelten Zustands-IDs und ungültiger initial-Kindzuordnung auf. Die über @zag-js/utils exportierte Funktion aus utilities/core/src/warning.ts wirft nur bei process.env.NODE_ENV !== production; ensure wirft bei null/undefined ohne diese Modusbedingung. Package-/Indexdatei bestätigen Name und Export.
- **Bedeutung/Grenze:** Neuer E2-Befund zur bisher nicht explizit geprüften Hilfsfunktion; kein ausgeführter Entwicklungs-/Produktionsversuch. Interne Prüflogik ist real, aber keine universelle Abweisungsgarantie. Kein neutraler Originalartefaktvalidator daraus; X06 bleibt U.
- **Nächste Prüfung:** Bei späterem praktischem Auftrag doppelten State-ID-/Initialziel-Fall unter explizitem Entwicklungs-/Produktionsbuild vergleichen. Unabhängiges Originalartefakt und Validator weiterhin gesondert identifizieren.

## C407

- **Kandidat / Anforderung:** Ark UI; X06; **U**. API-JSON sind Typmetadaten, kein nachgewiesenes neutrales Prüfschema.
- **Quelle:** [S62](SOURCES.md#s62); manuelle E2-Prüfung am gepinnten Originalstand.
- **Befund:** Das gepinnte generierte Combobox-API-JSON enthält Props mit type/isRequired/defaultValue/description, unter anderem ListCollection<T> und Callback-Typausdrücke als Strings. Boolean-Defaults sind teilweise als Stringtexte gespeichert.
- **Bedeutung/Grenze:** E2 an den relevanten API-JSON-Einträgen. Diese Metadaten lassen sich lesen, führen aber keine fachliche Typprüfung aus. Ein daraus erzeugter neutraler Validator müsste zusätzliche Typ-/Default-/Referenzsemantik definieren. Keine pauschale Abwesenheitsbehauptung und keine Änderung von X06=U.
- **Nächste Prüfung:** Vorhandenen offiziellen Runtime-/Contractschemaeinstieg nachweisen oder eine neue Metadatenübersetzung samt Informationsverlust ausdrücklich als Ergänzung abgrenzen.

## C408

- **Quelle:** [S63](SOURCES.md#s63), E1; betrifft X04.
- **Befund:** SCXML §6.4 definiert neue logische Dienstinstanzen, invoke-ID, Parameterinitialisierung eigener Daten und zustandsgebundenen Abbruch. Die erneute Prüfung bestätigt Definition/Verwendung und eigenen Lebenszyklus.
- **Bedeutung/Grenze:** X04 U→A: vorhandene Verhaltenskomposition ist ein konkreter Beitrag; UI-Anatomie, Host und ScrollArea-Bindung benötigen Übersetzung. Die frühere U-Einordnung verlangte hier bereits die vollständige Vier-Domänen-Kette; diese bleibt X01/X03/X07. Keine UI-Komposition ausgeführt.
- **Nächste Prüfung:** Eigenen Child-Kontext samt UI-Anatomie und getrennten Instanzen in einem späteren Hostversuch binden.

## C409

- **Quelle:** [S63](SOURCES.md#s63), E1; betrifft X04.
- **Befund:** Offizielle XState-invoke-Dokumentation beschreibt referenzierte Actorlogik, eigenen Input, innerhalb des Elternteils eindeutige IDs sowie Start/Stop beim Zustandswechsel.
- **Bedeutung/Grenze:** X04 U→A für diesen Behavior-Beitrag. Definition/Verwendung und eigener Kontext sind belegt; UI-Unterkomponentenstruktur und Domänenbindung bleiben zusätzlich. Datierte Dokumentation ist keine gepinnte Runtimeausführung.
- **Nächste Prüfung:** Actor-/UI-Instanz und Ereignisweitergabe explizit zuordnen; zwei Instanzen und Abbruch praktisch prüfen.

## C410

- **Quelle:** [S63](SOURCES.md#s63), E1; betrifft X04.
- **Befund:** Die erneut gelesene Zag-Kompositionsanleitung zeigt getrennte useMachine-Aufrufe referenzierter Maschinen, eigene Props/IDs und das bewusste Teilen eines Triggerziels mittels ids und mergeProps.
- **Bedeutung/Grenze:** X04 U→A: reale Instanzkomposition vorhanden, neutrale deklarative Unterkomponentenbindung zusätzlich nötig. Keine pauschale formale ScrollArea-Komposition oder konfliktfreie Mehrfachinstanz belegt. Die bisherige U-Begründung forderte mehr als diesen begrenzten vorhandenen Beitrag.
- **Nächste Prüfung:** Eigene Child-ID/Props, gemeinsame Teile, Fokus-/Scrollzuständigkeit und Eventmerging ausdrücklich in einer zusätzlichen Bindung festhalten.

## C411

- **Quelle:** [S64](SOURCES.md#s64), E2; betrifft X05.
- **Befund:** OpenPencil LibraryCatalog löst libraryId plus explizite revisionId auf. Revisionen besitzen contentbasierte IDs; Snapshot/Hashpfad erhält Behaviour-Plugininhalt, Serialisierung klont ihn, Materialisierung verwendet assetKey und revisionId und schreibt librarySource-Identität.
- **Bedeutung/Grenze:** X05 U→A für den Behaviour-Beitrag über das zusätzlich geprüfte Bibliothekssubsystem. Konkreter Resolver und Version sind nun mehr als Strings; latest ohne revisionId ist nicht reproduzierbar gebunden. Keine externe neutrale Fachmodellauflösung oder verlustfreier Roundtrip nachgewiesen.
- **Nächste Prüfung:** Explizite Revision festschreiben, Datenintegrität prüfen, zwei Versionen/Assets und Exporterhalt praktisch vergleichen. Keine Migration aus contentHash ableiten.

## C412

- **Quelle:** [S65](SOURCES.md#s65), E1; betrifft V03.
- **Befund:** Media Queries Level 5 WD 19.02.2026 §12.5 definiert prefers-color-scheme mit light/dark, einschließlich light bei fehlender aktiver Präferenz, und bedingter Styleauswahl.
- **Bedeutung/Grenze:** V03 U→D ausschließlich nach ausdrücklich dokumentierter Ergänzung des CSS-Untersuchungsumfangs um dieses Modul. Anchor/Overflow allein liefern diesen Nachweis nicht. Keine Aussage über manuellen Produktoverride, native Themes oder getesteten Browsersupport.
- **Nächste Prüfung:** Modul-/Browserstand und eigenes Overrideprofil vor praktischer Nutzung festhalten; Light/Dark ohne aktive Präferenz gesondert prüfen.

## C413

**E3-Fortschreibung:** aktueller Befund [C421](#c421); folgender Text dokumentiert den früheren Stand.

- **Quelle:** [S63](SOURCES.md#s63), E2; betrifft I02.
- **Befund:** CEM Event.name/type und Type.text/references wurden erneut gelesen; das offizielle simple-element-Beispiel beschreibt disabled-changed als Event. Typreferenzen können externe Deklarationen adressieren, definieren aber keine allgemeine CustomEvent<T>→detail-Projektion.
- **Bedeutung/Grenze:** CEM I02 bleibt U. Generische Typtexte könnten durch einen gewählten Typsystemresolver erschlossen werden; dieser ist hier nicht bewiesen. Weder ein unmöglicher Payloadvertrag noch eine freie Auflösungskonvention wird behauptet.
- **Nächste Prüfung:** Typsystem und Eventobjekt/Payloadprojektion explizit auswählen; dasselbe externe Eventpayload mit positivem und falschem Typziel nachvollziehen.

## C414

**E3-Fortschreibung:** [aktueller Befund C425](#c425); folgender Text ist der frühere Stand.

- **Quelle:** [S63](SOURCES.md#s63), E1; betrifft I02.
- **Befund:** SCXML send/param/content und _event.data sind normiert. Erneute Prüfung trennt send-Ausführung und öffentlich deklarierten Signaturkatalog; Eventnamen und Daten können dynamisch erzeugt werden.
- **Bedeutung/Grenze:** SCXML I02 bleibt U für das vollständige Kriterium. Statische send-Aufrufe bilden keine automatisch vollständige, vom Sendepunkt unabhängige öffentliche API. Ein eigenes Signaturprofil wäre zusätzliche Arbeit.
- **Nächste Prüfung:** Öffentlichen Interfacevertrag getrennt festlegen und send/event/data daran binden, statt eine originale Eventregistry zu erfinden.

## C415

- **Quelle:** [S63](SOURCES.md#s63), E2; betrifft B01, B02, B03, X04.
- **Befund:** UXSpecs gelesener App-Interpreter verarbeitet send mit exit/actions/entry/always/notify und danach rekursivem Send emittierter Namen; die always-Schleife ist begrenzt. enterState/exitState richten keine allgemeinen state.invoke-Dienste ein/ab. Initialisierung kann bei fehlendem Visualinhalt automatisch Mockevents planen.
- **Bedeutung/Grenze:** Gezielter Quellbefund zum Apppfad, keine Ausführung und keine globale Abwesenheitsbehauptung über alle Engines. Formatnorm, CLI und Vorschauimplementierung dürfen nicht gleichgesetzt werden. Bestehende sprachbezogene Bewertungen ändern sich dadurch nicht automatisch.
- **Nächste Prüfung:** Für einen neutralen Äquivalenzversuch Engine und Simulationsmodus kontrollieren; Invoke-Abbruch und Ereignisordnung eigens protokollieren.

## C416

- **Quelle:** [S63](SOURCES.md#s63), E2; betrifft X06, X04.
- **Befund:** Im originalen UXSpec-Schema erlaubt stateNode.invoke.items.oneOf sowohl machineInvoke als auch das allgemeine Schema type:object. Ein Objekt, das machineInvoke erfüllt, erfüllt auch den zweiten Zweig.
- **Bedeutung/Grenze:** Manuell folgt ein oneOf-Mehrfachtreffer für solche Objekte; keine ausgeführte Validierung oder Fehlermeldung. Die Existenz des Originalschemas bleibt X06=D; seine vollständige Konsistenz ist damit nicht belegt. Keine stille Schemareparatur.
- **Nächste Prüfung:** Minimalen machineInvoke mit Schema-Draft und Originalvalidator prüfen; erwartete Mehrfachtreffer und reale Ausgabe getrennt speichern.

## C417

- **Quelle:** [S63](SOURCES.md#s63), E1; betrifft V04, V05, V06, X03.
- **Befund:** Die erneut gelesene DESIGN.md-Spezifikation beschreibt spacing und bekannte Komponentenstylefelder; die geprüften CSS-Anchor-Abschnitte definieren benannte Boxziele und anchor-scope im Elementteilbaum. Gleiche Namen sind zulässig.
- **Bedeutung/Grenze:** Dokumentarischer Layoutvergleich: Werte, relative Geometrie und Overflow haben verschiedene Semantik. Ein optionales Textfeld ist keine ursprüngliche Ankersprache; ein gültiger CSS-Ankername beweist keine richtige Instanz-/Domänenbindung. Keine Grafik oder Browserprüfung.
- **Nächste Prüfung:** Vergleichsfall mit zwei Instanzen, Portal, variablen Zeilenhöhen und fehlendem Anker anhand expliziter Erwartungen ausführen.

## C418

**Weitere E3-Fortschreibung:** [C429](#c429) ergänzt die tatsächliche Folgeprüfung; der folgende Text ist ein früherer Stand.

- **Quelle:** [S66](SOURCES.md#s66), E3; betrifft X06, X04.
- **Befund:** Neun UXSpec-Fälle wurden gegen das unveränderte Originalschema mit python-jsonschema 4.25.1 Draft202012Validator ausgeführt. Vollständiges machineInvoke trifft beide oneOf-Zweige und wird abgewiesen; der Eintrag ohne id passiert den allgemeinen Objektzweig. Fehlender Übergangszielzustand, unbekannter Operator und falsch typisierter Default werden strukturell akzeptiert.
- **Bedeutung/Grenze:** Tatsächliche Schemaausgaben, keine Runtime-/CLI-Gleichsetzung und keine Reparatur. X06 bleibt D für das Originalschema, mit belegter Fachgrenze. Die frühere manuelle invoke-Ableitung ist bestätigt.
- **Nächste Prüfung:** CLI, Compiler und kontrollierte Engine auf dieselben Eingaben vergleichen; Format-/Schemadifferenz und genaue Version beibehalten.

## C419

- **Quelle:** [S66](SOURCES.md#s66), E3; betrifft I02, X06.
- **Befund:** CEM-Gesamtschema akzeptiert die synthetische CustomElement-Klassendeklaration mit numerischem Eventnamen. Gegenprüfungen der unveränderten Definitionen weisen den Wert unter Event und CustomElementDeclaration ab, akzeptieren die Deklaration aber unter ClassDeclaration. Das Modul-anyOf kann damit über den allgemeinen Klassenzweig passieren.
- **Bedeutung/Grenze:** Die zunächst erwartete Abweisung blieb als Erwartungsabweichung gespeichert. Zusätzliche Diagnosewrapper sind keine Änderung des Originalschemas. X06 bleibt D für einen realen Originalschema-Beitrag, ohne vollständige Eventfachprüfung zu versprechen.
- **Nächste Prüfung:** Gewählte Deklarationsart separat prüfen; bei späterer Nutzung keine vollständige Eventvalidierung aus Root-Schemaerfolg ableiten.

## C420

- **Quelle:** [S66](SOURCES.md#s66), E3; betrifft V04, V05, V06.
- **Befund:** Sechs Aufrufe der unveränderten UXSpec-Webmapperfunktionen wurden mit Node 24.22.1 ausgeführt: maxHeight=160 erzeugt 160px, value/unit erzeugt 5rem; zusätzliche anchorTarget/placement/offset sowie overflow-/Styleangaben erzeugen in diesen Pfaden keine entsprechenden CSS-Eigenschaften.
- **Bedeutung/Grenze:** Konkreter Funktionsnachweis, kein Rendering. Die erste Harness-Erwartung hatte Standardlayoutwerte übersehen; Original und korrigierte Erwartungen sind erhalten. V04/V06 bleiben U für das vollständige Kriterium, V05 bleibt A; andere Renderer/Hostregeln nicht ausgeschlossen.
- **Nächste Prüfung:** Einen vorhandenen formalen Anker-/Scrollbeitrag und dessen tatsächliche Hostbindung identifizieren; Schemaakzeptanz freier Felder nicht als Umsetzung ausgeben.

## C421

- **Quelle:** [S67](SOURCES.md#s67), E3; betrifft I02.
- **Befund:** TypeScript 5.9.3 löst den tatsächlichen CEM-Eventtyptext CustomEvent<{value:string}> auf und erschließt detail als Payload mit value:string. Ein zweiter Fall erhält optionale verschachtelte Typmetadaten. Ungültiger Typtext, fehlende Typdefinition, Event ohne detail sowie falscher Eventname werden im begrenzten Versuch jeweils unterschieden.
- **Bedeutung/Grenze:** CEM I02 U→A ausschließlich für ausdrücklich als TypeScript interpretierte Web-Typtexte plus explizite CustomEvent.detail-Projektion. Compiler und Projektion sind zusätzliche Bindung, keine automatische CEM-Originalvalidierung und keine generelle Auflösung aller Typnotationen/externer Pakete. Kein öffentlicher Auslösezeitpunkt muss in diesem Typmodell enthalten sein.
- **Nächste Prüfung:** Weitere konkrete Typnotationen und Paket-/Modulauflösung separat prüfen; Adapterregel für Eventobjekt/Payload und Eingangsprüfung sichtbar halten.

## C422

- **Quelle:** [S68](SOURCES.md#s68), E3; betrifft X06, X07, A01.
- **Befund:** Fünf synthetische HTML-Fälle wurden im W3C Nu Html Checker geprüft, Ergebnisansicht vnu 26.10.18. Ungültiges aria-expanded und doppelte ID erzeugen Fehler. Fehlendes aria-controls-Ziel und falsche aktive Option aus zweiter Listbox erzeugen gegenüber der bestehenden descendant/aria-owns-Warnung des Kontrollfalls keine weitere Diagnose.
- **Bedeutung/Grenze:** Reales Webtool mit begrenzter nachgewiesener Reichweite. Kein vollständiger neutraler ARIA-Artefaktvalidator, kein lokaler Versionspin und keine assistive Prüfung. WAI-ARIA X06 bleibt U; bloßes Bestehen einer Hostprüfung belegt keine Instanz-/Referenzkonsistenz.
- **Nächste Prüfung:** Norm-/Hostprofil und vollständige konkrete Referenzprüfung bestimmen; Kontrollwarnung fachlich gegen ARIA/APG prüfen, nicht durch Zusatzattribute nur unterdrücken.

## C423

**Weitere E3-Fortschreibung:** [C431](#c431) ergänzt die lokal gebundenen CSS-Prüferstände; der folgende Nu-Befund bleibt gültig.

- **Quelle:** [S69](SOURCES.md#s69), E3; betrifft X06.
- **Befund:** Vier CSS-Proben im Nu-Dienst vnu 26.10.18: Basis-CSS mit Größenbegrenzung, overflow-y und prefers-color-scheme passiert; ungültiger Overflowwert und unbekannte Längeneinheit werden beanstandet. Anchor-scope/name, position-anchor und Anchorfunktionen werden hingegen als unbekannt oder unzulässig abgewiesen.
- **Bedeutung/Grenze:** CSS X06 bleibt U für einen geeigneten Checker der gespeicherten Modulstände. Der konkrete Dienst unterstützt diese Kombination nicht ausreichend; das ist kein Beweis fehlender CSS- oder Browserfähigkeit. Keine Layoutausführung.
- **Nächste Prüfung:** Checker mit nachgewiesener Grammatikunterstützung der relevanten Anchor-/Overflow-/Media-Queries-Stände identifizieren; nicht den erfolgreichen Basis-CSS-Fall verallgemeinern.

## C424

- **Quelle:** [S70](SOURCES.md#s70), E3; betrifft X06.
- **Befund:** Offizielle SCXML-XSD-1.0-Kette aus acht Originaldateien lokal kompiliert und sechs Fälle mit lxml 6.1.1/libxml2 2.14.6 geprüft. Zweizustands- und send/param-Fall akzeptiert; fehlende Version und doppelte Zustands-ID abgewiesen. Fehlender Zielzustand und ungültiger ECMAScript-Ausdruck werden von dieser Kombination akzeptiert.
- **Bedeutung/Grenze:** SCXML X06 bleibt D, nun mit tatsächlicher begrenzter Originalschema-Prüfung. Kein Interpreter oder striktes XSD-1.1-Set geprüft. Die unerwartete Zielakzeptanz bleibt mit Erwartung und Exitstatus 1 erhalten; kein allgemeiner Befund über alle XSD-/SCXML-Implementierungen.
- **Nächste Prüfung:** Genau diese Fälle gegen kontrollierten Interpreter beziehungsweise strengeren Originalschema-Pfad prüfen; Host-/Ausdruckssemantik nicht aus XSD-Erfolg ableiten.

## C425

- **Quelle:** [S71](SOURCES.md#s71), E3; betrifft I02.
- **Befund:** Vier getrennte CEM-/SCXML-Bindungsfälle geprüft: alle SCXML-Eingaben bestehen Original-XSD, während eine zusätzliche statische Regel falschen Ausgabenamen, falschen Parameternamen und numerischen Wert gegen die öffentliche CEM-TypeScript-Signatur erkennt. Der korrekte statische value-change/value-Stringfall ist kompatibel.
- **Bedeutung/Grenze:** SCXML I02 U→A für statisches send/param plus separat geführte öffentliche CEM-Signatur und explizite zusätzliche Web-/Typbindung. Die Bindung ist ein Forschungsprofil, keine native SCXML-Signaturregistry oder implementierte öffentliche Hostroute. Keine Interpreterausführung, dynamische Ausdrücke und andere I/O-Prozessoren nicht abgedeckt.
- **Nächste Prüfung:** Hosttransport, tatsächlichen Dispatch und Instanzen separat prüfen; für weitere Typ-/Ausdrucksformen den nachgewiesenen Profilumfang explizit erweitern.

## C426

- **Quelle:** [S72](SOURCES.md#s72), E3; betrifft X03.
- **Befund:** Originale UXSpec-Import-/Resolvefunktionen explorativ ausgeführt: importierter Unterverweis löst bei gleichnamigem Appziel APP statt LIBRARY auf, ohne lokales Ziel UNKNOWN_ELEMENT_REFERENCE. Angeforderter fehlender Tokenbereich erzeugt keine Importdiagnose; fehlende Datei und direkter Datei-Selbstimport werden erkannt. Fremdes CEM liefert keinen UXSpec-Elementbereich.
- **Bedeutung/Grenze:** X03 bleibt U für unabhängige Originaldomänen. Referenzfälle sind Compilerpfad-Erkundungen; ihre normalen $ref-Objekte scheitern separat am Originalschema. Fehlender-Bereich-/Datei-/Selbstimportkontrollen sind schema-konform. Kein garantierter gültiger UI-Gegenfall und kein zugesagter CEM-Import behauptet.
- **Nächste Prüfung:** Original-Schemareferenzform, Namespaceherkunft und externe Zielarten gemeinsam klären; Alias oder erfolgreiche Dateilesung nicht als semantische Bindung ausgeben.

## C427

- **Quelle:** [S72](SOURCES.md#s72), E3; betrifft X02, X04, X07.
- **Befund:** Originaler Bundler gibt bei zwei schema-konformen Kinddateien mit gleicher Maschinen-ID ok=true zurück und enthält nur die zuletzt zugewiesene Definition. Eine Kind-ID gleich der Eintritts-ID ersetzt ebenso das Eintrittsmodul ohne Diagnose. Der positive Drei-ID-Fall enthält alle drei Module.
- **Bedeutung/Grenze:** Konkreter E3-Befund zu globalen Maschinen-IDs und Modulzuweisung, keine ausgeführte Actor-/UI-Instanz. Vorhandene X02-/X04-Beiträge beweisen weiterhin keine konfliktfreie Paketidentität; X07 bleibt N im bisherigen Vier-Domänen-Umfang.
- **Nächste Prüfung:** Vor Bundleverwendung Kollisionen und Definition/Instanz trennen; ein zusätzlicher Konfliktcheck wäre neue Projektlogik, kein vorhandener Originalnachweis.

## C428

- **Quelle:** [S72](SOURCES.md#s72), E3; betrifft V01, V05, X03.
- **Befund:** Ein schema-konformer UXSpec-Token mit $value={value:1,unit:rem} wird durch resolveDocument an einer Paddingreferenz auf die Zahl 1 reduziert, ohne Diagnose.
- **Bedeutung/Grenze:** Bestätigt den zuvor gelesenen Einheitenverlustpfad. Es wurde ein originales UXSpec-Tokenobjekt geprüft, kein automatischer Import einer unveränderten DTCG-Datei. Neue Format-/Zieladapter müssen Einheit und Bedeutung erhalten.
- **Nächste Prüfung:** Werte-/Einheitenbindung ausdrücklich prüfen, bevor neutrale Tokenquellen und Zielrenderer als gleichwertig gelten.

## C429

- **Quelle:** [S72](SOURCES.md#s72), E3; betrifft X06, X04.
- **Befund:** Die getrennte Originalschema-Vorprüfung der 24 beteiligten UXSpec-Dateien akzeptiert 15 und weist neun ab. Normale $ref-Objekte treffen mehrere element-oneOf-Zweige gleichzeitig; die tatsächliche Diagnose nennt Container/Leaf/Ref. Compilerfunktionen verarbeiten solche Eingaben dennoch.
- **Bedeutung/Grenze:** X06 bleibt D für ein tatsächlich vorhandenes/geprüftes Originalschema, mit zusätzlicher belegter Referenzgrenze. Compilerpfad-Ergebnisse sind nicht pauschal Ergebnisse gültiger Originalschemadokumente. Keine Schemareparatur und keine komplette Originalformat-Gleichheit behauptet.
- **Nächste Prüfung:** Dokumentierte Referenzsyntax, Originalschema und tatsächlichen Compilepfad gemeinsam prüfen; eine eigene korrigierte Schemafassung ausdrücklich als Änderung kennzeichnen.

## C430

- **Quelle:** [S72](SOURCES.md#s72), E3; betrifft X04.
- **Befund:** Zwei statische Elementexpansionen werden mit getrennten Parameterwerten kopiert; Änderung der ersten Kopie lässt die zweite unverändert. In einem explorativen Kind/Großkindfall enthält das Bundle dagegen nur Eltern- und Kindmodul, obwohl die Kindabhängigkeit auf die Großkinddatei zeigt. Elementrekursion führt zu RangeError statt strukturierter Resolverdiagnose.
- **Bedeutung/Grenze:** Positiver statischer Kopiernachweis ist keine Actor-/UI-Kontextisolierung. Referenz- und Invoke-Dateien dieser explorativen Fälle bestehen das Originalschema nicht; Transitivitäts-/Rekursionsbefunde werden daher nicht als garantierte schema-konforme UI-Gegenfälle verallgemeinert. X04 bleibt D im beschriebenen Teilbeitrag, keine vollständige Kompositionsfreigabe.
- **Nächste Prüfung:** Gültige Originalartefaktkette, vollständigen Modulabschluss und tatsächliche getrennte Laufzeitkontexte gemeinsam nachweisen.

## C431

- **Quelle:** [S73](SOURCES.md#s73), E3; betrifft X06.
- **Befund:** Je 17 Deklarationsfälle gegen css-tree 3.1.0/mdn-data 2.12.2 und 3.2.1/mdn-data 2.27.1 ausgeführt. 3.2.1 unterstützt direktes anchor() und anchor-size() besser. Beide akzeptieren jedoch ein ungültiges Anchorargument innerhalb calc, kennen die originalen position-anchor-Werte normal/match-parent nicht und unterstützen var()-Matching ausdrücklich nicht.
- **Bedeutung/Grenze:** CSS X06 bleibt U für die vollständige gespeicherte Draftkombination. Reales lokales Tooling und positive/negative Teilprüfungen sind belegt; Match ist keine Garantie aller verschachtelten Regeln, DOM-Ziele oder Variablenauflösung. Kein eigenes Grammatikpaket oder CSS-Format ergänzt.
- **Nächste Prüfung:** Erforderliches Prüfprofil und exakte Modulgrammatiken samt verschachtelten Funktionen, Variablen und Hostreferenzen binden; neue Konfiguration ausdrücklich als Ergänzung kennzeichnen.

## C432

- **Quelle:** [S74](SOURCES.md#s74), E2.
- **Befund:** Zusätzlich zum Behaviour-Beitrag sind originale Scenegraph-Variablen mit COLOR/FLOAT/STRING/BOOLEAN, Einheiten, Aliaswerten und CSS-Ausgabe belegt. Keine vollständige Composite-Typografie oder DTCG-Konformität.
- **Grenze:** D ausschließlich für den ausdrücklich erweiterten Visualbeitrag. Keine vollständige Behaviour-/Visual-/Interface-/A11y-Bindung oder ausgeführte Export-/Browserintegration. Loose-Originalschema und Einzel-Featureparser ersetzen keine vollständige semantische Validierung.
- **Nächste Prüfung:** Konkrete getrennte Originalartefakte und ihre Instanz-/Versionsbindung prüfen; Visualsyntax und gerenderte Wirkung getrennt validieren.

## C433

- **Quelle:** [S74](SOURCES.md#s74), E2.
- **Befund:** Zusätzlich untersuchte Variablenauflösung besitzt aktive/Standard- und geerbte Knotenmodi; der originale Tokenexport schreibt Standardwerte und Modusbedingungen per Selektor oder CSS-Bedingung.
- **Grenze:** D ausschließlich für den ausdrücklich erweiterten Visualbeitrag. Keine vollständige Behaviour-/Visual-/Interface-/A11y-Bindung oder ausgeführte Export-/Browserintegration. Loose-Originalschema und Einzel-Featureparser ersetzen keine vollständige semantische Validierung.
- **Nächste Prüfung:** Konkrete getrennte Originalartefakte und ihre Instanz-/Versionsbindung prüfen; Visualsyntax und gerenderte Wirkung getrennt validieren.

## C434

- **Quelle:** [S75](SOURCES.md#s75), E3.
- **Befund:** 15 Fälle gegen originale OpenPencil-Valibot-Schemata ausgeführt. Pflicht-ID und Name werden geprüft, fachliche Typ-/Werte-/Einheiten-/Alias-/Moduskonsistenz nicht umfassend. valuesByMode als Array wird unerwartet angenommen und als Objekt mit Indexschlüssel ausgegeben; die unveränderte Voraberwartung schlägt fehl. COMPOSE_COLOR prüft eigene Struktur, aber keine Opacityobergrenze oder Graphauflösung.
- **Bedeutung/Grenze:** Reales Originalschema-Tooling, keine vollständige semantische Visualvalidierung. Ergebnisse gelten für die aufgerufenen Exporte, nicht automatisch den kompletten Import-/Editorpfad. V01 bleibt D als Modellbeitrag; keine weitere U-Zelle geschlossen.
- **Nächste Prüfung:** Getrennte Typ-/Wertebereich-/Modus-/Referenzprüfungen des vollständigen Import- und Exportpfads nachweisen.

## C435

- **Quelle:** [S75](SOURCES.md#s75), E3.
- **Befund:** 16 Fälle gegen originalen CSSOM-Tokenvalidator ausgeführt: Werte einschließlich var() und komplexere Bedingungen werden angenommen, zusätzliche Deklarationen/Regeln und unzulässige Namen/At-Rules abgewiesen. Custom-Property-Texte banana/16bananas und unbekannter Mediafeaturewert werden ebenfalls angenommen.
- **Bedeutung/Grenze:** Sichere CSS-Ausgabeform ist ein anderer Prüfumfang als fachliche Typ-/Eigenschafts-/Featurekonformität. Keine belegte generelle Unfähigkeit, Werte oder Variablen zu übernehmen; keine behauptete neu gefundene vollständige Alternative. V03 bleibt D für Modusmodell und Exportabbildung.
- **Nächste Prüfung:** Anwendungsziel und aufgelöste Werte getrennt validieren, bevor ein Tokenstrom als gültiger Farb-/Dimensionswert gilt.

## C436

- **Quelle:** [S76](SOURCES.md#s76), E2.
- **Befund:** SceneNode und Layoutfelder führen min/maxWidth/Height; originale dom-css-Projektion schreibt nicht-null Grenzen über Pixel-/Tokenabbildung nach CSS und wird vom Design-/HTML-Ausgabepfad verwendet.
- **Bedeutung/Grenze:** Konkreter bestehender Webadapter, wie bei UXSpec V05 als A eingeordnet. Keine gemessene Geometrie, keine variable Zeilenhöhenbindung oder native Abbildung.
- **Nächste Prüfung:** Originalfeld, ausgewählten Zielrenderer und Instanzbindung gemeinsam prüfen; Geometrie-/Scrollwirkung und variable Zeilenhöhen später praktisch nachweisen.

## C437

- **Quelle:** [S76](SOURCES.md#s76), E2.
- **Befund:** Originale Projektion schreibt absolute x/y-Koordinaten im Elternkontext oder richtet einen relativen Elterncontainer ein.
- **Bedeutung/Grenze:** Belegte Positionierung ist kein vollständiger dynamischer Input-Overlay-Anker mit Richtung und Abstand. V04 bleibt U; andere Pfade nicht ausgeschlossen.
- **Nächste Prüfung:** Originalfeld, ausgewählten Zielrenderer und Instanzbindung gemeinsam prüfen; Geometrie-/Scrollwirkung und variable Zeilenhöhen später praktisch nachweisen.

## C438

- **Quelle:** [S76](SOURCES.md#s76), E2.
- **Befund:** Originale Projektion übersetzt clipsContent nach overflow:hidden. Der vollständig gelesene Feldpfad bietet keine auto/scroll- oder achsenspezifische Scrollauswahl.
- **Bedeutung/Grenze:** Clippingbeitrag ist real, aber keine vollständige Scrollcontainersemantik für überlaufende Optionen. V06 bleibt U.
- **Nächste Prüfung:** Originalfeld, ausgewählten Zielrenderer und Instanzbindung gemeinsam prüfen; Geometrie-/Scrollwirkung und variable Zeilenhöhen später praktisch nachweisen.

## C439

- **Quelle:** [S77](SOURCES.md#s77), E2 mit E1-Musterabgleich.
- **Befund:** OpenPencil switch-Kind wird im gepinnten Vue-Preview konkret auf Reka SwitchRoot mit Buttonbasis, Booleanmodell und disabled abgebildet. Die innerhalb des deklarierten Bereichs liegende Reka-2.10.5-Quelle und deren Dokumentation definieren Switch-Rolle, Zustand, Space-/Enterbedienung und APG-Musterbezug.
- **Bedeutung/Grenze:** R nur für diesen vorhandenen referenzierten Switch-Webbeitrag. Keine neue Bedeutung erfunden, aber weder vollständige Prüfung aller Kinds noch Autocomplete-, native oder Browser-/AT-Konformität. Versionsbereich nicht als nachgewiesenen tatsächlichen Lockstand ausgeben.
- **Nächste Prüfung:** Gewählten Controlpfad, tatsächlichen Abhängigkeitsstand und alle Namen-/Relations-/Meldebindungen nachvollziehbar verbinden; später gerenderte Tastatur-/Fokus-/AT-Fälle gesondert ausführen.

## C440

- **Quelle:** [S77](SOURCES.md#s77), E2 mit E1-Musterabgleich.
- **Befund:** Reka SwitchRoot besitzt konkrete Rollen-/Zustands- und Labelmechanismen; OpenPencil verwendet diesen Wrapper und übernimmt Hostattribute. Vollständig gelesene Fieldpfade können Text auf input/textarea/Placeholder abbilden.
- **Bedeutung/Grenze:** Positive Mechanismen sind belegt, aber eine vollständige Behaviour-zu-Name-/Beziehungsbindung, stabile Labels und getrennte externe Ziele aller nötigen Teile bleiben unbewiesen. Placeholder oder importierter Komponentenname genügen hierfür nicht.
- **Nächste Prüfung:** Gewählten Controlpfad, tatsächlichen Abhängigkeitsstand und alle Namen-/Relations-/Meldebindungen nachvollziehbar verbinden; später gerenderte Tastatur-/Fokus-/AT-Fälle gesondert ausführen.

## C441

- **Quelle:** [S77](SOURCES.md#s77), E2 mit E1-Musterabgleich.
- **Befund:** Switchzustand und Progresswert werden im vorhandenen Preview weitergegeben. Die gelesenen Control-/Field-/Renderpfade belegen keinen vollständigen allgemeinen Ergebnis-/Fehler-/Lademeldevertrag mit Auslöser, Inhalt, Ziel und Zeitpunkt.
- **Bedeutung/Grenze:** A03 bleibt U. Aktualisierte Zustandsattribute sind nicht automatisch eine definierte Produktansage. Keine pauschale Negativaussage über Reka oder andere noch ungeprüfte Exportpfade.
- **Nächste Prüfung:** Gewählten Controlpfad, tatsächlichen Abhängigkeitsstand und alle Namen-/Relations-/Meldebindungen nachvollziehbar verbinden; später gerenderte Tastatur-/Fokus-/AT-Fälle gesondert ausführen.

## C442

- **Quelle:** [S78](SOURCES.md#s78), E3.
- **Befund:** 14 Eingabe- und vier Indexabfragefälle am originalen Panda-read.ts ausgeführt. Root-/Array-/Versionsobergrenzen prüfen ausgewählte Formen. Falsche categories/tokens, null-Zeile, negative/gebrochene Version und fehlende conditions/themes werden angenommen. Doppelte Basiswerte liefern den ersten Treffer, fehlende Referenzziele werden indiziert, null-Zeile scheitert erst beim Indexaufbau.
- **Bedeutung/Grenze:** 18/18 vorher gespeicherte Erwartungen bestätigt; kein vollständiger fachlicher Originalvalidator daraus ableitbar. Reader vertraut laut Originalkommentar erzeugten Zeilen. X06 bleibt U, ohne andere Panda-Prüfungen oder Generatorgarantien auszuschließen.
- **Nächste Prüfung:** Gewählten Originalgegenstand und Validatorumfang vollständig binden; externen Export vor Abfragen unabhängig auf Tabellen-, Zeilen-, Versions- und Referenzkonsistenz prüfen, eigene Ergänzungen offen kennzeichnen.

## C443

- **Quelle:** [S79](SOURCES.md#s79), E3.
- **Befund:** Veröffentlichten Google DESIGN.md Linter 0.4.0 mit 16 gespeicherten Hauptfällen ausgeführt. Farben und Rundungsdimensionen werden konkret geprüft; leeres/fehlendes/kaputtes/dupliziertes YAML erzeugt Warnungsreports mit leerem Modell. Falsches spacing, numerische colors und YAML-Rootliste können ohne fachlichen Fehler bleiben. Vier Voraberwartungen widerlegt, unverändert gespeichert.
- **Bedeutung/Grenze:** Reales ausführbares Originaltool belegt, vollständiges separates Original-Dokumentschema weiterhin nicht. X06 bleibt U. PaketgitHead 9bf8eae... ist vom früheren Quellencommit 6e5da538... getrennt; zwei verglichene Quelldateien identisch, keine pauschale Repoidentität.
- **Nächste Prüfung:** Unverarbeitetes YAML, erwartete Modellinhalte, fachliche Dimensionen und Referenzintegrität zusätzlich prüfen; eigenes Abnahmeprofil offen kennzeichnen.

## C444

- **Quelle:** [S79](SOURCES.md#s79), E3.
- **Befund:** Vier zusätzliche Diagnosefälle desselben Original-Linters: unbenutzte fehlende/zyklische Farbtoken bleiben ohne Diagnose im Hauptlauf; Komponentenverbrauch erzeugt unresolvedRef-Fehler. Gültiger Alias funktioniert, fehlerhaftes spacing bleibt auch als Component-Padding ohne Dimensionsfehler.
- **Bedeutung/Grenze:** Selektive Komponentenreferenzprüfung ist kein Nachweis vollständiger Token-/Domänengraphvalidierung. Keine Veränderung der übrigen Abdeckungswerte; Befund ist eine Präzisierung des gebundenen Originalwerkzeugs.
- **Nächste Prüfung:** Alle relevanten Graphkanten und erwarteten fachlichen Zieltypen einzeln mit positiven/negativen Fällen prüfen, bevor Fehlerfreiheit oder Verlustfreiheit behauptet wird.

## C445

- **Quelle:** [S80](SOURCES.md#s80), E3.
- **Befund:** Zehn statische Zwei-Instanz-HTML-Fixtures im Browser gegen neun explizite Originalregeln von axe-core 4.14.0 ausgeführt. Fehlende aktive/offene Popupziele, ungültiges aria-expanded und fehlender Name werden diagnostiziert. Doppelte referenzierte ID liefert incomplete statt sicherer violation. Vorhandene instanzfremde Ziele bleiben unter diesen Regeln ohne Diagnose.
- **Bedeutung/Grenze:** Original-Hosttooling ist praktisch belegt; die Kontrolle besteht im begrenzten Regelsatz. Keine vollständige ARIA-/WCAG-/AT-Konformität oder neutrales Original-A11y-Artefaktschema. X06 bleibt U. Frühere Nu-Befunde bleiben gültig und werden um andere konkrete Abdeckung ergänzt.
- **Nächste Prüfung:** Originalchecker mit erwarteter fachlicher Ziel-/Instanzzuordnung und gerenderten Bedien-/Meldeabläufen verbinden; incomplete manuell prüfen.

## C446

- **Quelle:** [S80](SOURCES.md#s80), E3.
- **Befund:** Zusätzliches ausdrücklich eigenes Instanzprofil A/B auf dieselben zehn statischen Fixtures angewendet. Feste erwartete Input-/Listen-/Optionsziele erkennen alle instanzfremden Bezüge sowie fehlende/mehrdeutige Ziele. Namen und Booleanwerte werden von diesem Zusatzschritt nicht geprüft.
- **Bedeutung/Grenze:** Positiver begrenzter Zusatznachweis für explizite semantische Zielbindung, keine ursprüngliche ARIA- oder axe-Fähigkeit. Mapping stammt aus Testtabelle, nicht aus vollständig verbundenen vier Originalartefakten; WAI-ARIA X03 bleibt U. Keine Formatwahl oder Produktkomponente.
- **Nächste Prüfung:** Mapping aus führenden Originaldomänen mit Version und Instanzidentität nachvollziehbar herleiten; danach denselben Gegenfallkatalog gegen die vollständige Kette prüfen.

## C447

- **Quelle:** [S81](SOURCES.md#s81), E3.
- **Befund:** Vier eigene Prüfarbeitsdateien in unveränderten Originalsprachen CEM/SCXML/CSS/HTML getrennt erstellt und geprüft; zusätzliche externe Forschungstabelle verbindet dieselben Teile zweier Instanzen. Originaldateien erzwingen keine fremden API-/UX-/Visual-/A11y-Fachdefinitionen. CEM/SCXML-Schemata, CSS-Eigenschaftsgrammatiken und ausgewählte HTML-Hostregeln sind ausgeführt.
- **Bedeutung/Grenze:** X01 bei CEM, SCXML, CSS Layout und WAI-ARIA nun A, ausschließlich für diesen begrenzten Webreferenzfall mit expliziter zusätzlicher Bindung. Keine Produktformatwahl, neutrale A11y-Sprache, Actor-/Hostlaufzeit, native oder vollständige interaktive Gesamtintegration daraus ableiten.
- **Nächste Prüfung:** Verhalten tatsächlich mit Hostupdates verbinden, Unterkomponenten-/Instanzlebenszyklus und vollständige Typ-/Melde-/Plattformabbildung separat nachweisen.

## C448

- **Quelle:** [S81](SOURCES.md#s81), E3.
- **Befund:** 13 eigene statische Bindungsbedingungen inklusive Kontrollfall und zwölf Gegenfällen ausgeführt: Hash, deklarierte Teile, Verhaltensdefinition, Zustand, Instanzziele, Anker, Einheit, Ereignisname, Payloadtyp, führende Quelle und doppelte Teile werden unterschieden. Alle Voraberwartungen erfüllt; der Typfall nutzt tatsächlichen TypeScript-Check gegen CEM-CustomEvent.detail.
- **Bedeutung/Grenze:** Zusätzliches Forschungsprofil ist praktisch prüfbar, aber keine ursprüngliche Referenz-/Konfliktfähigkeit aller Kandidaten. Ownership ist weiterhin ein vorgeschlagenes Profil. Keine allgemeine Umwertung von X03/X08 oder vollwertige öffentliche Eventroute.
- **Nächste Prüfung:** Mapping und Provenienz für reale Produktartefakte verbindlich herleiten; Änderungen, Rundlauf und ausführbare Semantik prüfen.

## C449

- **Quelle:** [S81](SOURCES.md#s81), E3.
- **Befund:** Zwei getrennte HTML-/CSS-Instanzen im Chrome-155-Browser gemessen: je 8px Abstand zum eigenen Input, links an dessen Kante, Popup-/Clienthöhe 160px, Scrollinhalt 224px, sieben Zeilen je 32px und overflow-y:auto. Beide vorab definierten Geometriefälle erfüllt.
- **Bedeutung/Grenze:** Konkreter statischer Web-Layoutnachweis mit unterstützten Ankern; kein Crossbrowser-/Native-/Bedien- oder vollständiger ScrollArea-Kompositionsnachweis. Bestehende CSS-Abdeckungswerte bleiben erhalten.
- **Nächste Prüfung:** Resize, Scroll-/Portal-/Fallbacksituationen und aktive Option bei wirklicher Navigation getrennt prüfen.

## C450

- **Quelle:** [S81](SOURCES.md#s81), E3.
- **Befund:** Separate CSS-Variante mit Zeilenhöhen 24/48/36/24/60/28/40px an beiden Instanzen ausgeführt. Scrollinhalt 260px, Popup weiterhin 160px und 8px Abstand, aber nur vier vollständige Zeilen sichtbar. Beide vorher festgelegten Erwartungen erfüllt.
- **Bedeutung/Grenze:** Geometrische Maximalhöhe garantiert bei variablen Zeilenhöhen nicht fünf vollständig sichtbare Einträge. Keine Produktregel dafür erfunden; Visualvariante als eigene Datei und eigener Fall protokolliert.
- **Nächste Prüfung:** Explizite Produktanforderung für sichtbare Zeilen, partielle Zeilen und variable Inhalte festlegen und dynamisch prüfen.

## C451

- **Quelle:** [S82](SOURCES.md), E3; betrifft B01, B02, I02.
- **Befund:** Originaler SCION-SCXML-Interpreter 4.3.28 führt unveränderte Kontrollquelle aus: OPEN/COMMIT, ereignisloser Rücksprung und natives #_parent-send mit value-change/{value:alpha}. Zehn Voraberwartungen ausgeführt, neun erfüllt. Negativfälle für fehlendes Ziel, falschen Eventnamen, numerischen Payload, falschen Parent und fehlenden Parent protokolliert.
- **Bedeutung/Grenze:** Die zusätzliche Host-Allowlist prüft nur die aus CEM abgeleitete einfache Stringsignatur und Instanzroute. Keine vollständige Typprüfung oder universelle SCXML-Konformitätsprüfung.
- **Nächste Prüfung:** Invoke-Lebenszyklus und stärkere Payload-/Ereignisverträge getrennt prüfen.

## C452

- **Quelle:** [S82](SOURCES.md), E3; betrifft X04, X05.
- **Befund:** Bei gemeinsam vorbereiteter Factory senden beide Instanzen beta-B trotz Parametern alpha-A/beta-B: ursprüngliche Isolationserwartung verletzt. Zwei getrennt vorregistrierte Diagnosefälle bestehen: einmal kompilieren und je Instanz prepare sowie separat kompilieren und vorbereiten.
- **Bedeutung/Grenze:** Getrennte Zustandskonfigurationen allein belegen keine getrennten Datenkontexte. Die geprüfte SCION-prepare-Grenze erzeugt die notwendigen separaten Ausführungskontexte. Kein genereller Fehlerbefund zu SCXML als Standard.
- **Nächste Prüfung:** Echte invoke-Unterkomposition mit unabhängigen Kontexten prüfen.

## C453

- **Quelle:** [S82](SOURCES.md), E3; betrifft B04, I02, A02.
- **Befund:** Fünf Browser-Hostfälle erfüllen die gespeicherten Erwartungen: zwei anfangs geschlossene Instanzen, programmgesteuerter Fokus öffnet nur A, synthetisches Escape schließt A, Enter führt native SCXML-Sendung und echtes bubbling DOM-CustomEvent am Forschungscontainer aus, anschließend öffnet Fokus nur B. Originalquelle unverändert, prepare pro Instanz.
- **Bedeutung/Grenze:** Interaktive Forschungs-Hostfixture mit explizitem Zusatzcode, keine CEM-Produktionskomponente. Programmatischer DOM-Fokus und synthetische KeyboardEvents sind keine physische Tastatur-/AT-Prüfung. Vollständige Navigation, Async-Daten und dynamische Ansagen fehlen.
- **Nächste Prüfung:** Navigation, Scroll-to-active, Ansagen und native Zielprofile separat nachweisen.

## C454

- **Quelle:** [S83](SOURCES.md), E3; betrifft X01.
- **Befund:** Eigenständige DTCG-dimension-/Alias-Tokendatei und separate CSS-Layoutdatei mit bytegleichen CEM-, SCXML- und HTML/ARIA-Artefakten verbunden. Zusätzliches Profil benennt Quelle, Hash, Instanzen A/B, Tokenpfad, Selektor, Eigenschaft und Visualzuständigkeit. Zwölf vorher definierte Übersetzungs-/Bindungsbedingungen erfüllen ihre Erwartungen.
- **Bedeutung/Grenze:** X01 nun A im begrenzten Webreferenzfall: zusätzlicher Adapter erforderlich. Eigener Übersetzer prüft nur explizit typisierte dimension-/Curly-Alias-Teilmenge, kein Original- oder vollständiger DTCG-Validator. Keine fremde Domäne in Tokens definiert.
- **Nächste Prüfung:** Weitere Tokenarten, Resolverkontexte, Schriftgrößenänderungen und Versions-/Ownershipkonflikte separat prüfen.

## C455

- **Quelle:** [S83](SOURCES.md), E3; betrifft V01, V05, V06.
- **Befund:** Vier Browserbedingungen: Instanzen A/B jeweils mit px- und rem-Tokens bei 16px Rootschriftgröße. Alle ergeben 8px Abstand, 160px Popuphöhe, sieben 32px-Zeilen, 224px Scrollinhalt und Overflow auto.
- **Bedeutung/Grenze:** Zusätzliche Übersetzung in CSS-Variablen und tatsächliches Browserlayout nachgewiesen. Keine generelle Gleichheit von rem und px, keine DTCG-Scrollsemantik, keine Navigation oder Assistenzprüfung.
- **Nächste Prüfung:** Rootschriftänderung und zusätzliche Token-/Layoutvarianten mit expliziten Erwartungen prüfen.

## C456

- **Quelle:** [S84](SOURCES.md), E3; betrifft X04, X05.
- **Befund:** Echter Default-src-invoke desselben Childartefakts an zwei separat vorbereiteten Eltern erzeugt unterschiedliche Kindobjekte, aber gekoppelte Datensnapshots: owner A wird nach Start B zu B; SCROLL A setzt auch Bs offset auf 40; Wiederöffnung A überschreibt Bs owner. Drei der sechs ursprünglichen Erwartungen verletzt.
- **Bedeutung/Grenze:** Originalinvoker cached vorbereitete Modellfunktionen nach Quelladresse. Getrennte Elternvorbereitung allein garantiert deshalb keine unabhängigen Childdaten in dieser Runtimeversion. Zustands-/Objekttrennung und richtige Parentroute sind keine Datenisolation. Kein allgemeiner Fehlerbefund gegen SCXML als Standard.
- **Nächste Prüfung:** Geeignete instanzgetrennte Invokerbindung beziehungsweise Runtimealternative separat prüfen, ohne ursprüngliche Fehler zu überschreiben.

## C457

- **Quelle:** [S84](SOURCES.md), E3; betrifft X04.
- **Befund:** Von sechs Defaultinvoke-Bedingungen bestehen Initialstart A, CLOSE-A-Kindcancel bei weiter aktivem B und Parentcancel B mit finalem Kind. Ein separat vorregistrierter Diagnosefall mit bytegleichen Kinddateien unter unterschiedlichen URIs zeigt owner A/B und offset 40/0 korrekt.
- **Bedeutung/Grenze:** Begrenzter tatsächlicher Lebenszyklus belegt. URI-Kontrolle stützt Cachegrenze, ist keine gewählte Bereitstellungsstrategie. Eigenes ResearchScrollArea-Modell enthält nur owner/offset/Ereignisse, keinen vollständigen visuellen oder zugänglichen Scrollvertrag.
- **Nächste Prüfung:** Datenisolation mit gleicher fachlicher Definition und belastbarem Instanzkontext sowie vollständige UI-Scrollbindung nachweisen.

## C458

- **Quelle:** [S84](SOURCES.md), E3; betrifft X04.
- **Befund:** Zusätzlicher eigener Invokeradapter führt dieselbe kontrollierte Childdatei je Instanz über originale documentStringToModel/prepare/Statechart-APIs mit frischem Ausführungskontext aus. Alle sechs separat gespeicherten Adaptererwartungen erfüllt: owner/offset und Parentereignisse getrennt, Close/Reopen/Cancel wie erwartet.
- **Bedeutung/Grenze:** Begrenzter tatsächlicher Adapterpfad für unabhängige Kindkontexte. Kein Original-Defaultinvoker-Erfolg, keine gewählte Produktlösung oder generische Runtimeabsicherung. Unterstützt ausschließlich die kontrollierte lokale Datei; Initialisierungsrennen, Fehlerpropagation, weitere Invokertypen und tiefere Hierarchien ungeprüft. Die drei Originalverletzungen bleiben erhalten.
- **Nächste Prüfung:** Cancel-während-Initialisierung, Fehlerpfade und vollständigen UI-Scrollvertrag gesondert prüfen.

## C459

- **Quelle:** [S85](SOURCES.md), E3; betrifft X08, X07.
- **Befund:** Zusätzliches Forschungsprofil benennt zwei führende Originalinformationen und ihre Ableitungen: DTCG-Maximalhöhe → CSS-Variable, CEM-Eventname → SCXML-send/Integrationsprofil. 15 vorab gespeicherte Änderungs-/Konfliktfälle bestehen; Journal bindet Herkunft, Informationspfad, Vorher-/Nachherhashes und Policyrevision. Konflikte/veraltete Quellen/unerlaubte Seiteneffekte werden verworfen.
- **Bedeutung/Grenze:** CSS Layout X08 nun A für die konkrete zusätzliche Visualwert-/Ableitungskette; keine native CSS-Ownershipfunktion oder Abdeckung aller Informationen. In-Memory-Staging und deklarierte Agentenrollen sind kein Nachweis persistenter Transaktionsatomarität oder authentifizierter Identität.
- **Nächste Prüfung:** Andere Informationsarten und A11y-Ownership, Schema-/Versionsmigration sowie persistente Konfliktbehandlung separat prüfen.

## C460

- **Quelle:** [S85](SOURCES.md), E3; betrifft X05, X08.
- **Befund:** Separat vorregistrierte Revisionskonsistenz-Erwartung verletzt im eigenen Ausgangsprüfer: neue Revision verwendet anderen Algorithmus und lässt Policyhash weg. Originalfehlbefund samt Skript/Outputs erhalten. Korrigierte Fassung verwendet dieselbe kanonische Dateihash-/Policyhashableitung wie Baseline; Kontrollfall und beide angenommene Änderungen stimmen nun überein.
- **Bedeutung/Grenze:** Fehler und Korrektur im zusätzlichen Forschungsprüfer, kein Originalstandardfehler. Regression der ursprünglichen 15 Fälle besteht und zählt nicht als zusätzliche 15 Bedingungen. Hashbindung ist keine Signatur oder manipulationssichere Speicherung.
- **Nächste Prüfung:** Mehrstufige Revisionen, Policyänderungen und konkurrierende persistente Aktualisierungen getrennt prüfen.

## C461

- **Quelle:** [S85](SOURCES.md), E3; betrifft X08, X06, I02, V05.
- **Befund:** Tatsächlich angenommene Änderungen gegengeprüft: beide Browserinstanzen zeigen 192px Höhe/8px Abstand/224px Inhalt; Original-SCXML-Interpreter sendet nach gemeinsamer Namensänderung selection-change mit value=alpha und invokeid=A; geändertes CEM/SCXML werden von ihren unveränderten Originalschemata akzeptiert. Vier praktische Gegenbedingungen erfüllt.
- **Bedeutung/Grenze:** Konkrete Quelldelta-/Ableitungskette desselben Pakets, keine generische Vier-Domänen-/Typ-/AT-Konformität. Originalschemaakzeptanz ist getrennt von zusätzlicher Ownershipprüfung und Runtimeverhalten.
- **Nächste Prüfung:** Weitere überlappende Felder, Migrationen und Zielplattformen eigenständig prüfen.

## C462

- **Quelle:** [S86](SOURCES.md), E3; betrifft X03.
- **Befund:** Eigener zusätzlicher Resolver verbindet ARIA-Hostinstanzen A/B mit separat beschriebenen CEM-Klassenteilen und SCXML-Zuständen über Quellhash, konkrete JSON-Pointer/namespace-gebundene XPaths und geprüfte Zielarten/Definitionszugehörigkeit. 16 vorab definierte Fälle erfüllen ihre Erwartungen; eine zweite gleichnamige Klasse wird über explizite Adresse unterschieden.
- **Bedeutung/Grenze:** WAI-ARIA X03 A für die begrenzte zusätzliche statische Host-/Originalmodellbindung. Native IDREF bleibt DOM-Referenz; keine neutrale Original-ARIA-Modellsprache oder generische Livebindung behauptet. Partnamen und Komponenten-/Maschinennamenpaar sind explizite Zusatzbedingungen dieses Beispiels.
- **Nächste Prüfung:** Weitere Referenzformen, Liveinstanzzustände, A11y-Originalschema sowie Schema-/Versionsmigration getrennt prüfen.

## C463

- **Quelle:** [S86](SOURCES.md), E3; betrifft X03, X06, X07.
- **Befund:** Alle 16 erzeugten CEM-/SCXML-Varianten werden von den gepinnten Originalschemata akzeptiert, während der Zusatzresolver falsche Zielart, fremde Klassenteile, fehlende/mehrdeutige Ziele, veraltete Quellen und falsche Hostinstanzbeziehungen abweist. Pro Fall Schemaergebnis, Quellhash und Auflösungszeugen gespeichert.
- **Bedeutung/Grenze:** Formale Originalschemaakzeptanz und domänenübergreifende Zielbedeutung sind getrennte Nachweise. Keine Aussage, dass alle mutierten HTML-Fälle native ARIA-Regeln bestehen; kein zusätzlicher Browser-/axe-/Interpreter-/AT-Lauf in diesem Paket.
- **Nächste Prüfung:** Auflösungszeugen mit weiteren tatsächlich gewählten Zielprofilen verknüpfen, ohne andere Kandidaten pauschal aufzuwerten.

## C464

- **Quelle:** [S87](SOURCES.md), E3; betrifft X06.
- **Befund:** Veröffentlichter xstate-Core 5.33.3 mit 132/132 inventarisierten Dateien, öffentlichen Exporten und relevantem Originaldatenfluss abgegrenzt. schemas wird als unknown-Metadatum durchgereicht/gespeichert; false und ein parse-Hook werden nicht als Originalartefaktprüfung ausgeführt. Kontextzahl 42 trotz beigefügter String-Schemavorgabe akzeptiert; ungültiges Transitionsziel durch echten Graphaufbau abgewiesen.
- **Bedeutung/Grenze:** X06 N im ausdrücklich geprüften Coreumfang für den getrennten neutralen Maschinenartefakt-/Originalschema-Pfad. Keine Aussage, dass XState generell ohne Typ-/Runtimeprüfung oder alle Stately-/externen Werkzeuge ohne Validator seien. Abgrenzung beruht auf Originaldistributions-/APIrolle und Gegenkontrollen, nicht fehlendem Fund allein.
- **Nächste Prüfung:** Gesamtpaketvalidierung durch eigenständig identifizierte andere Originalartefakte oder explizite Zusatzbindung untersuchen; SDK/Schema/Snapshot getrennt halten.

## C465

- **Quelle:** [S87](SOURCES.md), E3; betrifft X06, I01, I02.
- **Befund:** Originale XState-SDK-Deklarationen mit TypeScript 5.9.3: gültige Stringkonfiguration ohne Diagnose, falscher Kontext- und Eventpayloadtyp jeweils TS2322. Separater Original-Snapshotrestore über vorhandene Maschine akzeptiert geänderten numerischen Kontext. Sechs API- und drei SDK-Bedingungen erfüllen ihre Voraberwartungen.
- **Bedeutung/Grenze:** Vorhandener SDK-Typprüfpfad, Graphkonsistenz und Snapshotwiederherstellung sind echte, aber unterschiedliche Nachweise. Keiner wird zum unabhängigen neutralen JSON-Artefaktschema umgedeutet. Keine ungeprüfte Gleichsetzung der NPM-Bytes mit dem früheren gleichversionierten Repositorysnapshot.
- **Nächste Prüfung:** Andere Validatorrollen und neutrale Originalartefaktidentitäten bei den noch offenen X06-Kandidaten prüfen.

## C466

- **Quelle:** [S88](SOURCES.md), E3; betrifft X06.
- **Befund:** Original @zag-js/core 1.46.0 mit tatsächlichen utils/dom-query 1.46.0 in getrennten development-/production-Prozessen geprüft. Doppelte Zustands-IDs und ungültige Compound-initial-Kinder werden nur in development abgewiesen; fehlendes Compound-initial in beiden Modi. createMachine akzeptiert auch ein Objekt ohne obligatorische Root-initialState-Funktion und gibt das Objekt zurück. Zehn Voraberwartungen erfüllt.
- **Bedeutung/Grenze:** Begrenzte interne Aufbauprüfung, kein vollständiger Shape-/neutraler Originalartefaktvalidator. X06 bleibt U für die ausdrücklich breitere Zag-Toolkit-Spalte; Corebefund nicht ohne Nachweis auf alle Komponenten/Hilfsartefakte oder Arks andere ausgelieferte Coreversion übertragen. Kein Service/UI-Lauf.
- **Nächste Prüfung:** Konkretes neutrales Originalartefakt-/Schema-/Validatorpaar im definierten Toolkitumfang oder eine abschließend belegte Modellgrenze dieses gesamten Gegenstands identifizieren.

## C467

- **Quelle:** [S88](SOURCES.md), E3; betrifft X06.
- **Befund:** Separater originaler Ark-API-Metadatensatz liefert Typausdrücke, required-Metadaten, Callbacktexte und Stringdefaults. Tatsächlich veröffentlichtes React-SDK 5.39.3 mit TypeScript 5.9.3: open=true akzeptiert, open als String TS2322, einfache Array-collection TS2740. Drei Voraberwartungen erfüllt.
- **Bedeutung/Grenze:** Vorhandener ausgewählter SDK-Typpfad; Metadaten sind nicht von selbst ein ausführbares neutrales Originalschema. X06 bleibt U für den breiteren Ark-Kandidatenumfang. Kein Frameworkrender oder Runtime-Propsvalidator ausgeführt; kein Ersatzschema aus Typstrings gebaut.
- **Nächste Prüfung:** Eigenständigen Original-Contractgegenstand mit eigener Schemaidentität und tatsächlichem Aufruf/Regelumfang identifizieren; SDK-/Generator-/Metadatenrollen getrennt halten.

## C468

- **Quelle:** [S88](SOURCES.md), E2; betrifft X05, X06.
- **Befund:** Exakte Registry-/Lock-/Installationsauflösung unterscheidet Ark-Stände: veröffentlichtes @ark-ui/react 5.39.3 führt Zag-Core/Combobox/Reactbindung 1.45.0 und RegistrygitHead 90eb2125a9ac6a8225b2e4053484da08cbb68a54. Früherer Repositorysnapshot c7af88a… nennt ebenfalls Ark 5.39.3, aber Zag-Paketangaben 1.46.0. Paketdateizahlen 35/3874 und Dateihashes inventarisiert.
- **Bedeutung/Grenze:** Versionszeichenfolge allein beweist keine Byte-/Abhängigkeitsidentität. Direkte Core-1.46.0-Proben gelten nicht automatisch für Arks ausgelieferten 1.45.0-Pfad; historische Repositorybefunde bleiben als eigener Originalstand erhalten. Inventar ist kein Vollcodeaudit.
- **Nächste Prüfung:** Jede weitere Ark-/Zag-Prüfung an der tatsächlich relevanten Originalrevision und aufgelösten Abhängigkeit binden.

## C469

- **Quelle:** [S89](SOURCES.md), E3; betrifft X06.
- **Befund:** Original-Panda-Exporttyp DesignSystemSpec und unveränderter JSON-Reader am Commit 86f78a… mit neun identischen kontrollierten Eingaben gegengeprüft. Zusätzliche Literal-/Originaltypzuweisung erkennt categories-Zahl, tokens-Boolean, null-Wertzeile, fehlende conditions/themes und numerisches value; derselbe Originalreader akzeptiert diese Fälle. Alle Voraberwartungen erfüllt.
- **Bedeutung/Grenze:** Reale Originalartefakt-Shapeinformation ist vorhanden; Leser prüft sie nicht vollständig. Zusätzliche statische Typanbindung ist kein originales neutrales Runtime-JSON-Schema/Validatorpaar. X06 bleibt U im definierten Panda-Umfang; keine negative Aussage über alle Pakete/Plugins aus diesem begrenzten Befund.
- **Nächste Prüfung:** Konkrete Originalschema-/Validatoridentität mit tatsächlichem Aufruf und Regelumfang oder abschließend belegte Modellgrenze des gesamten Kandidatengegenstands identifizieren.

## C470

- **Quelle:** [S89](SOURCES.md), E3; betrifft X06, X07.
- **Befund:** Originalreader und zusätzliche Originaltypzuweisung akzeptieren beide eine refs-Kante auf fehlenden Token, einen Kategorienbereich über paths hinaus und schemaVersion=-1. Originaltyp beschreibt diese als Stringliste, Zahlentupel beziehungsweise number; keine Originaldefinition verschärft.
- **Bedeutung/Grenze:** Shape-/Typakzeptanz allein belegt keine referentielle Bereichs-/Ziel-/Versionskonsistenz. Kein Befund, dass der reguläre Generator solche Daten erzeugt; Generator und Compilerbuild wurden nicht ausgeführt. Fehlende semantische Regelabdeckung allein widerlegt nicht die Existenz anderer Originalschemas.
- **Nächste Prüfung:** Originale referentielle Prüfpfade beziehungsweise erforderliche explizite Zusatzregeln getrennt identifizieren.

## C471

- **Quelle:** [S90](SOURCES.md), E1; betrifft X06.
- **Befund:** WAI-ARIA 1.2 Recommendation §8 grenzt Rollen/Zustände/Eigenschaften ausdrücklich von einem vollständigen Format ab und verlangt Hostsprachenintegration als Attribute. §3.4 beschreibt Dokumentkonformitätsprüfer; Anhang A ist eine nichtnormative Datentypabbildung, kein eigenständiges Komponenten-A11y-Contractschema. Erneute gezielte Auswertung des bekannten Standards, keine neue Version oder Laufzeitprüfung.
- **Bedeutung/Grenze:** X06 N für die Recommendation 1.2 als eigenen neutralen Artefaktschema-Beitrag. Positive Modell-/Hostsprachenabgrenzung statt Negativschluss aus Nichtfinden. Keine Aussage gegen ARIA-Konformitätsregeln, Hostschemas oder Accessibilitywerkzeuge; eigene neutrale Contract-/Schemaschicht wäre zusätzliche Beschreibung.
- **Nächste Prüfung:** Konkrete zusätzliche A11y-Contract-/Hostprüfprofile separat identifizieren; deren ursprüngliche Identität nicht WAI-ARIA allein zuschreiben.

## C472

- **Quelle:** [S90](SOURCES.md), E1; betrifft X06.
- **Befund:** Die acht bisherigen X06-U-Fragen sind in einem endlichen offiziellen Umfangsregister nach Originalpin, öffentlicher Werkzeugoberfläche, bereits geprüftem Beitrag und konkretem nächsten Originalzugriff abgegrenzt. Zukünftige Releases oder beliebige externe Plugins sind keine Abschlussvoraussetzung. Nach WAI-ARIA-Modellgrenze sieben X06-U-Fragen.
- **Bedeutung/Grenze:** Kein Kriteriumswechsel und keine Suche über einen unendlichen hypothetischen Markt. Für einen begrenzten Originalschema-Beitrag wird kein vollständiger semantischer Allvalidator verlangt; SDK-/Transport-/Dokumentationsschemas bleiben eigene Gegenstände. Keine neue Produktentscheidung des Nutzers nötig, um die dokumentierten Originalzugriffe auszuführen.
- **Nächste Prüfung:** Die benannten offiziellen Restzugriffe gezielt abschließen, ohne erneute illustrative Tests desselben bereits geklärten Teilpfads.

## C473

- **Quelle:** [S91](SOURCES.md), E2; betrifft X06.
- **Befund:** Ark-Root-/Scripts-Manifeste am Commit c7af88a… führen document:types auf scripts/src/generate-type-docs.ts zurück. Vollständig gelesener Generator extrahiert mit TypeScript-Typechecker SDK-Propertytypen/JSDoc/Pflicht-/Defaultmetadaten und schreibt frameworkbezogene *.types.json in website/src/content/types. Pipeline ist Dokumentationsextraktion, kein neutraler Original-Contractvalidierungsaufruf.
- **Bedeutung/Grenze:** Konkreter ursprünglicher API-Metadaten-Producer geklärt, kein Generator ausgeführt oder neue Runtimebedingung gezählt. Ark X06 bleibt U für den verbleibenden endlichen offiziellen Artefaktanspruch; tatsächliche NPM-SDK-Typprüfung C467 und Repo-/Releaseunterschied bleiben getrennt erhalten.
- **Nächste Prüfung:** packages/mcp/package.json und dessen deklarierte öffentliche Tool-/Schemaentrypoints am selben Pin gezielt abgleichen: Dokumenttransport oder eigener Original-Contractgegenstand?

## C474

- **Quelle:** [S92](SOURCES.md), E3; betrifft X06.
- **Befund:** Originale website/velite.config.ts am Ark-Pin c7af88a… definiert ein konkretes Collection-Schema für erzeugte types/**/*.json. Unveränderte Originaldeklarationen per AST isoliert, mit tatsächlichem velite 0.4.0 über types.schema.safeParse samt Originalmetadatentransformation ausgeführt. Sechs Voraberwartungen erfüllt: Original-API-JSON akzeptiert; fehlerhafte type/isRequired/defaultValue-Felder und fehlendes props abgewiesen.
- **Bedeutung/Grenze:** X06 D für den separaten originalen API-Metadaten-JSON-Beitrag und sein Originalschema. Kein neuer SDK-Typcheck als Schema ausgegeben, keine reimplementierten Regeln. Ausgeführter Kontrollgegenstand React-Combobox; kein Vollwebsitebuild, keine Prüfung aller Frameworkdateien oder vollständigen UI-/Behavior-/A11y-Contractsemantik.
- **Nächste Prüfung:** Weiterhin offene Ark-Integrationszellen separat nachweisen; Schemaexistenz/-Shape von Typausdrucksauflösung und konkreter Runtime-/Plattformsemantik trennen.

## C475

- **Quelle:** [S92](SOURCES.md), E2; betrifft X06.
- **Befund:** Offizieller MCP-Registryeintrag am selben Repo-Pin enthält sieben gelesene Dokumentations-/Beispiel-/Propsabfragetools. inputSchema prüft Framework/Komponentenname/Beispiel-ID/Suchtext/Slug. Get-component-props liest Website-API parts; Fetch nutzt JSON und TypeScript-Zusage, nicht die Collection-Schema-Runtimeprüfung. Tatsächlicher serverseitiger Metadatentyp stammt aus der separaten Types-Collection.
- **Bedeutung/Grenze:** MCP-Anfragevalidierung, ursprüngliche Metadaten-Artifactprüfung, SDK-Deklarationen und Live-APIantworten sind getrennte Gegenstände. Kein MCP-Server oder Live-APIaufruf ausgeführt; kein Validierungsbeweis allein aus Toolnamen/Zod-Abhängigkeit.
- **Nächste Prüfung:** Jeden späteren Tool-/Schemaeinsatz an seinen tatsächlichen Eingabe- und Ausgabegegenstand und Originalpin binden.

## C476

- **Quelle:** [S92](SOURCES.md), E3; betrifft X06, I01.
- **Befund:** Absichtlich erfundener Typausdruck TotallyInvalid<unknown> bleibt als String im ursprünglichen API-Metadatenschema akzeptiert; Originalkontrolle liefert component combobox, framework react und 16 Teile. Originalschema prüft Struktur/Metadaten, keine fachliche TypeScript-Typausdruckssemantik oder wirklichen open-/collection-Werte.
- **Bedeutung/Grenze:** Begrenzte Originalschema-Regelabdeckung ist explizit; keine Forderung universeller Semantik als Voraussetzung des D-Beitrags. Repo-/NPM-Arkstände und SDK-1.45/1.46-Abhängigkeiten bleiben getrennt; Velite-Transitivauflösung nicht mit ursprünglichem Bunbuild gleichgesetzt.
- **Nächste Prüfung:** Typtexte und externe SDK-/Eventreferenzen in konkreten Integrationsprofilen separat auswerten.

## C477

- **Quelle:** [S93](SOURCES.md), E3; betrifft X06.
- **Befund:** Original-Rustexporter und offizielle JSON-Spec-Beschreibung bestätigen den eigenständigen versionierten JSON-Datenartefaktgegenstand zur vorhandenen DesignSystemSpec. Die bereits ausgeführte P42-Bindung an diesen unveränderten Originaltyp prüft dessen Shapeconstraints über zusätzliche Literal-/Compileranbindung; neun gespeicherte Ergebnisse wiederverwendet, keine neue Ausführung gezählt.
- **Bedeutung/Grenze:** X06 A für das konkret definierte Original-JSON-Spec-Shapemodell: tatsächlicher zusätzlicher Prüfbindungsbedarf, kein nativer Original-Runtime-JSON-Validator und keine eigene Ersatzschemasemantik. Datenartefakttyp von beliebigen funktionalen SDK-Konfigurationen unterscheiden. Reader-/Typ-/Referenzgrenzen bleiben unverändert sichtbar.
- **Nächste Prüfung:** Verbleibende Panda-Integrationsfragen getrennt nachweisen; eventuelle produktive Import-/Compilerbrücke und referentielle Regeln ausdrücklich als weitere Anbindung behandeln.

## C478

- **Quelle:** [S93](SOURCES.md), E2; betrifft X06, X07.
- **Befund:** Gezielt gelesener Rustproducer erzeugt Kategorienbereiche aus dem paths-Vektor, schreibt Versionskonstante 1 und filtert token_refs über bekannten Pfadbestand. Referenzierte Design-Notiz beschreibt Löschung des alten Studio-Zod-Schemas zugunsten des gemeinsamen Readers; teils zukünftige Rezept-/Patternaussagen werden durch aktuellen Code bereits überholt.
- **Bedeutung/Grenze:** Begrenzte Originalproducer-/Migrationsrollen, kein Rustbuild oder Generatortest. Plausible Producerkonstruktion ersetzt keine Prüfung externer importierter Daten; Reader-/Typ-Gegenfälle werden dadurch nicht widerlegt. Alte Notiz nicht als vollständige aktuelle normative Schemapublikation ausgeben.
- **Nächste Prüfung:** Bei weiterer Untersuchung Producer-, Importprüfer- und Referenzsemantik jeweils am konkreten Originalstand getrennt halten.

## C479

- **Quelle:** [S94](SOURCES.md), E3; betrifft X06.
- **Befund:** Vier exakte Originalgrammatiken aus Anchor-WD27.03.2026 und Overflow-WD07.10.2025 sowie originaler anchor-name-Typalias an den vorhandenen css-tree3.2.1-createLexer-Einstieg gebunden. Zwölf vorab gespeicherte Stylesheetbedingungen erfüllen Erwartungen. Normale native Ablehnung von normal/match-parent bleibt gespeichert, zusätzliche Originalgrammatikbindung akzeptiert beide.
- **Bedeutung/Grenze:** X06 A für diesen konkreten vier-Property-Originalgrammatik-/Checkeradapter. Keine Modifikation des ursprünglichen Paketwörterbuchs, keine neu erfundene Standardsyntax, kein vollständiger Gesamt-Draftvalidator. Unbekannte Properties und nicht unterstützte Werte nicht als gültige vollständige Datei ausgeben.
- **Nächste Prüfung:** Weitere Originalregeln nur unter eigenem genauem Profil-/Versionsnachweis ergänzen; verbleibende CSS-DOM-/Instanzsemantik separat prüfen.

## C480

- **Quelle:** [S94](SOURCES.md), E3; betrifft X06, X03.
- **Befund:** Zusätzlicher Checker weist falschen Ankernamen, Overflowwert und angehängten Wert ab; gemischte unbekannte Property, top und max-height bleiben unsupported_scope, var-Matching unsupported_value. Syntaktischer Verweis auf --missing bleibt akzeptiert, da kein DOM-/Instanzkontext ausgeführt wird.
- **Bedeutung/Grenze:** Syntaxbeitrag getrennt von Substitution, Referenzbedeutung und Layout. Zuvor beobachtete calc-/var-/Versionslücken nicht überschrieben und nicht als gelöst ausgegeben. Kein Browser-/Geometrie-/AT-Lauf in diesem Paket.
- **Nächste Prüfung:** CSS X03 und weitere offene Domänenfragen mit tatsächlichem Modell-/Hostkontext nachweisen.

## C481

- **Kandidat / Anforderung:** Zag; X06; **N**.
- **Quelle:** [S95](SOURCES.md#s95), E2.
- **Befund:** Originalanleitung, Introduction, öffentliche Core-/Combobox-/ScrollArea-Exports, Machine-/MachineSchema-Typen und Factory am cafda74-Pin abschließend gelesen. Originalmodell verlangt initialState-Funktion und weitere Service-/Hostfunktionen; Autorenpfad erzeugt und konsumiert ein SDK-Maschinenprogramm. Introduction grenzt SCXML ausdrücklich ab.
- **Bedeutung/Grenze:** N im endlichen benannten offiziellen Modellumfang für den eigenen unabhängigen neutralen Contractdatenschema-Beitrag. SDK-Typen, echte interne Prüfungen und gespeicherte Development-/Production-Gegenfälle bleiben positive Beiträge. Kein globaler Ausschluss späterer anderer Werkzeuge.
- **Nächste Prüfung:** Neue Original-Datendateisprache nur als neuen Gegenstand prüfen; vorhandene SDK-/Host-/Referenzfragen unabhängig bearbeiten.

## C482

- **Kandidat / Anforderung:** APG; X06; **N**.
- **Quelle:** [S95](SOURCES.md#s95), E2.
- **Befund:** Original-Introduction/Combobox-Pattern, README/package.json, ariaTest-Runner und Combobox-Autocomplete-both-Test am 0f765e-Pin gelesen. Guide grenzt eigenen Konformitätsanspruch ab; tatsächlicher Runner erhält HTML-Beispielpfad, data-test-id und ausführbare Testfunktion, öffnet die Seite und prüft konkrete Demonstration.
- **Bedeutung/Grenze:** N für den eigenen neutralen Pattern-Contractschema-Beitrag dieses Guide-/Beispieltestpfads. Positive Bestimmung des echten Prüfgegenstands zusätzlich zur Guideabgrenzung; nicht aus informativer Natur allein gefolgert. HTML-/Codeprüfung, Beispielregression und fachliche Empfehlungen bleiben erhalten. Kein Lauf/AT-Test behauptet.
- **Nächste Prüfung:** Fachliche Patternauswahl und Host-/Praxisprüfung separat nachweisen; eigene Contractableitung wäre Zusatzprofil.

## C483

- **Kandidat / Anforderung:** Google DESIGN.md; X06; **U**.
- **Quelle:** [S95](SOURCES.md#s95), E3.
- **Befund:** Mitgelieferte Spec/Config und öffentliche Linter-/Outputdefinitionen von @google/design.md0.4.0 abschließend abgeglichen. Originales ConfigSchema mit sechs vorab gesetzten Gegenfällen ausgeführt: Originalconfig angenommen, drei Shapeverletzungen und Dokumentdaten abgewiesen, erfundener Typname als String angenommen.
- **Bedeutung/Grenze:** Echtes Zod-Schema für Redaktions-/Spezifikationskonfiguration belegt, kein Inhaltsschema für eingereichte DESIGN.md-Dateien. Keine Forderung eines vollständigen semantischen Allzweckvalidators. X06 U bleibt wegen fehlender eindeutiger Originalbindung zwischen Dokumentdatenmodell und Schemaentscheidung; vorhandene Prosa und selektive Lintregeln bleiben positive Beiträge.
- **Nächste Prüfung:** Externe Originalklärung des benannten Dokument-Schemaeinstiegs und seiner Ergebnisbedeutung, Roottypen und Optionalität. Eigene ausführbare Prosaabbildung nur als zusätzliches Profil; keine Autorenanfrage versandt.

## C484

- **Kandidat / Anforderung:** OpenUI; X06; **U**.
- **Quelle:** [S95](SOURCES.md#s95), E2.
- **Befund:** README/draft-01, lib/schema.ts, tatsächliches interfaces/Spec.ts und Tabellenrenderer am 09d39b-Pin abgeglichen. Rootlicense/Komponentengroup, String-Propform, enum/required und Defaulttypen weichen konkret ab; gelesene Publikationen liefern keine Vorrangregel. Fehlzugriff lib/Spec.ts mit 404 erhalten, danach tatsächlicher Pfad erfolgreich.
- **Bedeutung/Grenze:** X06 U mit präziser externer Autorenklärung der kanonischen Originaldefinition; keine eigene Reparatur oder Wahl des Nutzers über technische Wahrheit. Renderer beschreibt Felder statt Contractdateiprüfung. Kein globaler Negativbeweis für alle Werkzeuge.
- **Nächste Prüfung:** Offizielle Vorrang-/Synchronisationsregel und gebundenen Originalvalidator für die konkret widersprüchlichen Formen benötigen; keine Nachricht an Autoren versandt.

## C485

- **Quelle:** [S96](SOURCES.md#s96), E3; betrifft X03.
- **Befund:** Zusätzlichen statischen CSS-Ankerresolver am bytegleichen CEM/SCXML/CSS/HTML-Basispaket ausgeführt. Reale CSS-AST und Originalwertgrammatik, CEM-Komponenten-/Partpointer, Sourcehash und A/B-Hostzugehörigkeit verbunden. 14 unterschiedliche Bedingungen, alle Erwartungen erfüllt; passende Umbenennung bleibt gültig, instanzfremde/falsche/fehlende deklarierte Ziele werden abgewiesen.
- **Bedeutung/Grenze:** CSS Layout X03 A für diese zusätzliche deklarierte Originalmodell-/Hostbindung. bound ist kein nativer Anchorlookup-/Kaskaden-/Layout-/Accessibility-Nachweis. Originalformate unverändert; zusätzliche Zielarten-/Instanzregeln offen ausgewiesen.
- **Nächste Prüfung:** Nicht unterstützte Scopes, Ankerfunktionen, Variablen und native Box-/Kaskadensemantik separat prüfen; CSS-fremde Domänenfelder nicht automatisch umbewerten.

## C486

- **Quelle:** [S96](SOURCES.md#s96), E2/E3; betrifft X03, A01.
- **Befund:** Original-WD §§2.1–2.4 erlaubt gleichnamige Anker und bestimmt native Auswahl über Scope/Zulässigkeit/Baumreihenfolge; §7 trennt Accessibilitybeziehungen. Zusätzliches enges Profil meldet Mehrdeutigkeit als eigene Bindungsverletzung und Scope/Nesting/Variablen/implizite Anker/spätere position-Resets/explizite andere anchor()-Namen als unsupported.
- **Bedeutung/Grenze:** Gültige CSS-Sprache ist nicht automatisch durch diesen Zusatzresolver unterstützt. Eindeutigkeitsforderung ist zusätzliche Profilregel, keine erfundene CSS-Normpflicht; sichtbare oder zugängliche Beziehung wird daraus nicht abgeleitet. Erstlauf13 und Folgelauf14 erhalten, nur14 unterschiedliche Bedingungen gezählt.
- **Nächste Prüfung:** Für echte native/AT-Abnahme reale Zielumgebungen und Zustands-/Boxzulässigkeit nachweisen; bestehende Begrenzungen nicht als Sprachfehler oder erfüllte Konformität ausgeben.

## C487

- **Quelle:** [S97](SOURCES.md#s97), E3; betrifft V06.
- **Befund:** Zwölf vorab gespeicherte Gegenfälle an unveränderten isolierten Originalanweisungen des OpenPencil-Dom-CSS-Overflowfeldpfads ausgeführt. hidden und clip werden zu clipsContent:true und danach hidden; auto/scroll und reine Achsenwerte erhalten in diesem Fragment keine Scrollangabe. Alle Erwartungen erfüllt.
- **Bedeutung/Grenze:** OpenPencil V06 bleibt U: konkreter Verlust der ursprünglichen Scrollpolitik im benannten Originalfeldpfad, kein positiver vollständiger Scrollvertrag. Originalfragmente, eigene Aufrufrahmen und nicht ausgeführter Gesamtimport/-export ausdrücklich getrennt. Kein globaler Negativbefund für alle OpenPencil-Beiträge.
- **Nächste Prüfung:** Konkret benannte Originalrepräsentation oder ausdrücklich zusätzliche Bindung für Achse/Scrollpolitik/Clipping mit tatsächlichem vollständigem Import-/Host-/Exportpfad nachweisen.

## C488

- **Quelle:** [S97](SOURCES.md#s97), E2/E3; betrifft V06.
- **Befund:** Original-mergedStyle mit computedStyle nach inlineStyle tatsächlich ausgeführt: computed hidden beziehungsweise auto entscheidet die beiden Kontrollfälle. Ein isolierter Setteraufruf bei zuvor true und visible löscht das Feld nicht; gelesener normaler createElementNode-Pfad initialisiert es hingegen mit false.
- **Bedeutung/Grenze:** Kein behaupteter fehlerhafter In-place-Updatepfad und keine Ausführung kompletter Style-/Layoutnormalisierung. Eigenen AST-Harnischfehler vor jeder Fallausführung dokumentiert und korrigiert; keine Originalquelle oder Erwartung geändert.
- **Nächste Prüfung:** Vollständige Originalnormalisierung und tatsächlich verwendete Styleeingaben getrennt prüfen, bevor Rohobjektfälle auf jeden Browserimport übertragen werden.

## C489

- **Quelle:** [S97](SOURCES.md#s97), E2/E3; betrifft V06.
- **Befund:** Originale CSS-Overflow-Wertdefinitionen unterscheiden hidden mit programmgesteuertem Scrollen von clip ohne Scrollen. Drei eigene native CSS-Browserfixtures bestätigen bei 60px Fenster/300px Inhalt: scrollTop80 bleibt bei clip0, bei hidden80; der aus der Originalfeldprobe projizierte clip-Wert hidden liefert ebenfalls80.
- **Bedeutung/Grenze:** Konkrete native semantische Folge der Feldzusammenführung belegt, kein gerenderter OpenPencil-Build oder vollständiger Roundtrip. Keine physische Eingabe, Assistenztechnik, allgemeine Achsen-/Scrollbar-/Formatting-Context-Konformität daraus ableiten.
- **Nächste Prüfung:** Tatsächliche Gesamtpipeline und weitere Original-Scrollrepräsentationen prüfen; separate native/AT-Zielnachweise weiterhin offen halten.

## C490

- **Quelle:** [S98](SOURCES.md#s98), E3; betrifft A01.
- **Befund:** Zwölf vorab gespeicherte Bedingungen am isolierten originalen Radio-/Render-/Statepfad mit Vue3.5.41 und tatsächlicher SSR-Ausgabe ausgeführt. Explizite Namens-/Labelreferenzattribute bleiben erhalten; ursprüngliche role/checked-Overrides gewinnen, öffentliche IDs und getrennte Islandkontexte bleiben korrekt. Unbenanntes Control und nicht aufgelöstes labelledby-Ziel werden ebenfalls ausgegeben.
- **Bedeutung/Grenze:** OpenPencil A01 bleibt U: konkreter Attribut-/Instanztransport ausgeführt, nicht der vollständige Ursprung der semantischen Modellbindungen oder berechnete zugängliche Name. Roleclassifier, Scenegraphprojektion, Editor und Reka nicht ausgeführt; keine Fälle künstlich auf volle Konformität erweitert.
- **Nächste Prüfung:** Originalprojektion/Roleklassifizierung bis zu Namen und externen Beziehungszielen verfolgen und tatsächliche Host-/Zielauflösung prüfen; identische reine Renderattribute nicht erneut zählen.

## C491

- **Quelle:** [S98](SOURCES.md#s98), E3; betrifft A03.
- **Befund:** Direkter originaler Radio-A-Callback ändert dessen eigenen State; erneute tatsächliche Vue-SSR gibt aria-checked=true aus, während B unverändert false bleibt. Fehlender State wirft den originalen Fehler. Insgesamt zwölf Erwartungen erfüllt.
- **Bedeutung/Grenze:** A03 bleibt U: kein lebender DOM-/Accessibility-Updatepfad oder ursprünglicher Ergebnis-/Meldungsvertrag ausgeführt. Zustand, Namensbindung und Meldungsinhalt getrennt. Das unveränderte Kriterium wird nicht um eine allgemeine Live-Region-/AT-Pflicht für jeden Teilbeitrag verschärft.
- **Nächste Prüfung:** Originalen lebenden Host-/Accessibility-Updatepfad beziehungsweise konkrete ursprüngliche Meldungsbindung gezielt prüfen; SSR-Neuausgabe und direkter Handleraufruf nicht als physische oder AT-Interaktion ausgeben.

## C492

- **Quelle:** [S99](SOURCES.md#s99), vorhandene E3-Ergebnisse kriteriumsbezogen erneut ausgewertet; betrifft I03.
- **Befund:** CSS-P46-Ergebnisse gesondert gegen I03 ausgewertet: tatsächlicher CSS-Anker-/Selektorbeitrag ist über den zusätzlichen Binder an benannte ursprüngliche CEM-input/popup-Teile derselben Komponentendefinition und A/B-Hostinstanz gebunden. Kontroll-/Umbenennungsfälle gültig, falscher Teil und fremde Instanz abgewiesen.
- **Bedeutung/Grenze:** CSS Layout I03 A für diesen konkret ausgeführten zusätzlichen Teilbinder. Anatomie stammt aus dem getrennten CEM-Modell, nicht aus einer behaupteten nativen CSS-Teilesprache. Separater kriteriumsbezogener Beleg, keine automatische Übertragung von X03 und keine neue Bedingung gezählt.
- **Nächste Prüfung:** Andere domänenfremde Felder brauchen ihren eigenen Nachweis; native CSS-Kaskade/Boxzulässigkeit und allgemeine Komponenten bleiben separat.

## C493

- **Quelle:** [S99](SOURCES.md#s99), vorhandene E3-Ergebnisse kriteriumsbezogen erneut ausgewertet; betrifft I03.
- **Befund:** ARIA-P36-Ergebnisse gesondert gegen I03 ausgewertet: vier benannte ursprüngliche CEM-Teile werden mit typisierten Pointern/Definitionsmitgliedschaft den Hostteilen beider ARIA-Instanzen zugeordnet. Fremder gleichnamiger Part, falsche Zielart/falscher Partname und fremdes Hostziel werden tatsächlich abgewiesen.
- **Bedeutung/Grenze:** WAI-ARIA I03 A für den zusätzlichen CEM-/ARIA-Host-Teilbinder. ARIA bleibt für Rollen/Hostbeziehungen, CEM für die Anatomie zuständig; der Adapter leistet die Zuordnung. Kein nativer ARIA-Anatomiekatalog, kein Live-/AT-Nachweis und keine neuen Versuchsfälle.
- **Nächste Prüfung:** WAI-ARIA V06/X08 und sonstige CSS-/ARIA-Felder separat weiterprüfen; keine automatische Fremdmodellzurechnung.

## C494

- **Quelle:** [S100](SOURCES.md#s100), E3; betrifft A01.
- **Befund:** Öffentliche Original-Szene/Komponenteninstanziierung, Projektion, Behaviour-/Roleklassifizierung und ursprüngliche Vue-Statefactory bis Reka SwitchRoot/Host ausgeführt. TEXT-Inhalt erzeugt den tatsächlichen benannten Switch; bloßer Knotenname tut dies nicht. Passende Original-Namensregel und Browser-Accessibility-Snapshots bestätigen die benannten Instanzen und zeigen die negativen Namensfälle.
- **Bedeutung/Grenze:** OpenPencil A01 R ausschließlich für diesen gebundenen Switch-Webpreview-/Namensinhaltbeitrag. Vorhandene ReKa/HTML/ARIA-Referenzsemantik, keine neue neutrale Anatomie-/Accessibility-Dateisprache und keine Behauptung beliebiger externer Widgetbeziehungen. Graphtext/Name bleibt gekoppelt; X01/X08 nicht dadurch erledigt.
- **Nächste Prüfung:** Andere Kinds, externe Label-/Fehler-/Controlziele, unabhängige Namensownership und native/AT-Zielabnahmen getrennt behandeln.

## C495

- **Quelle:** [S100](SOURCES.md#s100), E3; betrifft A03.
- **Befund:** Sechs gespeicherte Browser-Liveschritte verbinden ursprünglichen Switch-Controlstate über Vue/Reka mit genau dessen aria-checked: A/B getrennt ein/aus, Namen stabil, disabled-A blockiert nativen programmgesteuerten Click. WAI-ARIA1.2 definiert diese on/off-Werte; Modell-/DOM- und Snapshotbeobachtungen erhalten.
- **Bedeutung/Grenze:** OpenPencil A03 R für diese definierte zugängliche Switch-Zustandsrückmeldung. Kein allgemeiner Suchergebnis-/Fehler-/Ladeansagevertrag, keine Live-Region-Pflicht für jedes Widget und keine behauptete Screenreader-, physische Tastatur-, Editor- oder Graphpersistenzabnahme.
- **Nächste Prüfung:** Produktspezifische Meldungen und weitergehende Plattform-/AT-Abnahmen separat konkretisieren; keine Ausweitung des begrenzten Switchbeitrags auf alle Komponenten.

## C496

- **Quelle:** [S100](SOURCES.md#s100), E3; betrifft A01.
- **Befund:** Erste drei axe-Bedingungen mit aria-toggle-field-name auf nativen Buttons ergeben keine anwendbaren Prüfknoten; zwei Diagnoseerwartungen widerlegt, alle Ausgangsergebnisse erhalten. Originalmatcher überspringt native Benennungsmethoden. Danach passende button-name-Regel: drei Radio- und vier Switchbedingungen mit tatsächlichen Pass-/Violationknoten erfüllen sämtliche gezielten Erwartungen.
- **Bedeutung/Grenze:** Leeres Originalcheckergebnis ist kein positiver Namensnachweis. Unterschiedliche Regelsubjekte/Anwendbarkeit und vollständige Conformance getrennt; ursprüngliche Fehlwahl nicht verborgen und nicht als Produktfehler erklärt.
- **Nächste Prüfung:** Vor Namens-/Semantikabnahme immer tatsächliche Regelanwendbarkeit und Zielknoten prüfen; nicht aus null Violations auf universelle Konformität schließen.

## C497

- **Quelle:** [S100](SOURCES.md#s100), E2/E3; betrifft A01, A03.
- **Befund:** Veröffentlichte dom-css/scene-graph0.16.0 ohne RegistrygitHead separat gepinnt. Source-Map-Projektion hat gegenüber Repo-ab2875 andere Importpfade, sämtliche Nicht-Import-Deklarationen dieser Datei textgleich. Vierzehn unveränderte Repo-Vue-Deklarationen an tatsächliche Originalpakete gebunden; eigener API-/Buildharnisch repariert und Protokolle erhalten.
- **Bedeutung/Grenze:** Konkretes gebundenes Laufzeitprofil, keine globale Repo-/Releaseidentität. Unbenutzter Node-Dateiexport nach ausdrücklicher Buildkonfiguration vollständig aus Browserbundle entfernt, keine Bibliotheksattrappe. Zwölf Graphbedingungen plus drei ursprüngliche und sieben passende Namensbedingungen plus sechs Liveschritte zählen28 unterschiedliche Bedingungen, Wiederholungen nicht zusätzlich.
- **Nächste Prüfung:** Andere Originalmodule und Gesamtbuilds separat binden; festgestellte Scope-/Buildgrenzen und historische Fehlversuche sichtbar erhalten.

## C498

- **Quelle:** [S101](SOURCES.md#s101), E3; betrifft V06.
- **Befund:** Vollständige ursprüngliche Graph→DesignDocument→HTML-Projektion und nativer Host mit begrenztem Frame/300px-Kind ausgeführt. clipsContent:true erzeugt feste hidden-Politik beider Achsen; Scrollpositionen80/80 funktionieren. false erzeugt visible/0/0. maxHeight60 begrenzt einen ursprünglich300px-hohen Frame tatsächlich auf60px bei derselben programmierten Scrollpolitik.
- **Bedeutung/Grenze:** OpenPencil V06 A für die konkret ausgeführte feste Zielpolitik des bestehenden Webadapters. Originales Clippingboolean, tatsächliche Übersetzung und CSS-Plattformsemantik getrennt. Kein frei wählbarer auto-/Scrollbar-/Wheelmodus, kein neutraler universeller Scrollvertrag und keine Behauptung verlustfreien Fremd-CSS-Imports.
- **Nächste Prüfung:** Bei künftigem neutralem Visualprofil diese konkrete Policybindung explizit erhalten; andere Scrollpolitiken/Zielplattformen und UX-Eingabeabbildung brauchen eigene Nachweise.

## C499

- **Quelle:** [S101](SOURCES.md#s101), E3; betrifft V04.
- **Befund:** Drei vollständige Original-Koordinatenexporte im Browser gemessen: Input20/Popup-y28 ergibt Abstand8; Inputwachstum auf40 bei unverändertem Popup-y28 ergibt Abstand-12 und verletzt die gewünschte8px-Ankerrelation. Bewegung des gemeinsamen Parents50/50 bewegt beide gemeinsam und erhält Abstand8.
- **Bedeutung/Grenze:** OpenPencil V04 bleibt U. Definierter Parentkoordinatenbezug ist positiv belegt, aber keine Relation zur Unterkante des anderen Inputs. Gewünschte Beziehung im Gegenfall ausdrücklich false; erfüllte Beobachtungserwartungen nicht zu erfüllten Produktanforderungen umgedeutet. Kein pauschaler Editor-/Constraint-Fehlerbefund.
- **Nächste Prüfung:** Benannten Originalziel-/Abstandspfad oder ausdrücklich zusätzlichen Ankerbinder mit Größen-/Änderungssemantik nachweisen; statische Koordinaten allein nicht erneut als Ankerprobe zählen.

## C500

- **Quelle:** [S101](SOURCES.md#s101), E3; betrifft V04, V06.
- **Befund:** Sechs vollständige Originalexporte plus sechs native Messbedingungen mit allen Beobachtungserwartungen erfüllt; ursprüngliche Größen-/Clippingfelder unverändert genutzt, keine neue Layoutbibliothek oder Policygrammatik eingeführt. Dynamische Input-Ankerakzeptanz bleibt im Wachstumsfall unerfüllt.
- **Bedeutung/Grenze:** Neuer positiver Beleg der eigenen festen Overflow-Outputpolitik hebt den früheren clip/auto/scroll-Importverlust nicht auf. Vollständiger öffentlicher Export, isolierte frühere Fragmente, fester Webhost und nicht ausgeführter Editor-/Resize-/AT-Pfad bleiben getrennt. Kriterien/Methodik unverändert.
- **Nächste Prüfung:** UXSpec/uSpec und alternative Originalmodelle nur mit ihren eigenen tatsächlichen Einstiegen prüfen; kein pauschaler Fähigkeitsübertrag aus diesem Originaladapter.

## C501

- **Kandidat / Anforderung:** XState; X01; **A**.
- **Quellen:** [S102](SOURCES.md#s102), ergänzend S28/S29/S81; E3.
- **Befund:** Eigenständige XState-SDK-Konfiguration mit drei bytegleichen ursprünglichen Fachartefakten und explizitem zusätzlichem Quellen-/Instanzbinder; acht Bedingungen erfüllt. Zwei Actors bleiben unabhängig, echte CSS-Änderung erfordert keinen Behaviorumbau, drei falsche Profile werden erkannt.
- **Bedeutung/Grenze:** A für den begrenzten SDK-Webbeitrag. Kein neutrales XState-Schema und keine vollständige Autocomplete-/Emissions-/Host-/AT-Integration; X06 N/C464 bleibt bestehen.
- **Weiterer Bedarf:** Andere Kandidatenpflichten und gesonderte Emissions-/Typbindungen prüfen. [Gespeicherter Bericht](experiments/2026-10-25/xstate-independence/REPORT.md).

## C502

- **Kandidat / Anforderung:** uSpec; X08; **U**.
- **Quellen:** [S103](SOURCES.md#s103), S52; E3.
- **Befund:** Vollständiger Originalbuilder und Cache-/Zielvalidator mit zehn Gegenfällen ausgeführt: Plan-/Rendererhash und konkrete Identitätskonflikte werden zurückgewiesen; abweichender Spezialistenhash und widersprechende Höhenwerte im Pfad ohne Domain-Evidence akzeptiert. Separate Ausgabe, Quellcaches bei normalizeCaches:false unverändert.
- **Bedeutung/Grenze:** U für die nach wie vor fehlende unabhängige Vier-Domänen-/Ownershipbindung. Tatsächliche Originalmechanismen und begrenzte akzeptierte Gegenfälle anerkannt; kein globales Versagen aus minimalen Fixtures ohne Obligation-Evidence ableiten.
- **Weiterer Bedarf:** Nur konkrete zusätzliche Originalevidence-/Ownershipbindung oder benannten anderen Pfad bearbeiten; keine Wiederholung derselben Root-/Hashproben. [Bericht](experiments/2026-10-25/uspec-ownership/REPORT.md).

## C503

- **Kandidat / Anforderung:** uSpec; X01; **U**.
- **Quellen:** [S103](SOURCES.md#s103), S52; E3.
- **Befund:** Originalbuilder verarbeitet getrennte API-/Dictionary-/Structure-/Color-/Voice-Caches und erzeugt daraus Canonical-JSON. Die tatsächliche Trennung und gemeinsame Pflichtausgabe sind ausgeführt; der Schnitt ist nicht der gewünschte Vier-Domänen-Schnitt, externer Behaviorvertrag weiterhin ungebunden.
- **Bedeutung/Grenze:** U für die nach wie vor fehlende unabhängige Vier-Domänen-/Ownershipbindung. Tatsächliche Originalmechanismen und begrenzte akzeptierte Gegenfälle anerkannt; kein globales Versagen aus minimalen Fixtures ohne Obligation-Evidence ableiten.
- **Weiterer Bedarf:** Nur konkrete zusätzliche Originalevidence-/Ownershipbindung oder benannten anderen Pfad bearbeiten; keine Wiederholung derselben Root-/Hashproben. [Bericht](experiments/2026-10-25/uspec-ownership/REPORT.md).

## C504

- **Kandidat / Anforderung:** WAI-ARIA; X08; **A**.
- **Quellen:** [S104](SOURCES.md#s104), S54/S81/S85; E3.
- **Befund:** Genau eine zusätzliche Namens-Ownershipkette von Accessibility-HTML/list-a/aria-label zur getrennten Hostableitung; Vorher-/Nachherhashes und Revisionen dokumentiert. Zehn Konflikt-/Bindungsfälle und zwei native listbox-Namenspaare erfüllen Erwartungen. Andere drei Fachartefakte bytegleich.
- **Bedeutung/Grenze:** Eigene zusätzliche Ownershipregel; WAI-ARIA1.2 liefert die Rollen-/Namenssemantik. Keine native ARIA-Governance, Live-DOM-/AT-/persistente Atomaritäts-/APG-Zusage. Konkurrierendes aria-labelledby ist ein eigener nicht abgedeckter Bindingpfad.
- **Weiterer Bedarf:** Andere konkrete Informationen separat binden. [Bericht](experiments/2026-10-25/aria-ownership/REPORT.md).

## C505

- **Kandidat / Anforderung:** OpenPencil; X03; **A**.
- **Quellen:** [S105](SOURCES.md#s105), S53/S100; E3.
- **Befund:** Ursprünglicher Switch-Booleanwert bindet über expliziten zusätzlichen Pointer-/Owner-/ID-/Hashbinder auf ein separat beschriebenes CEM-checked-Feld. Elf Referenzbedingungen und zwei CEM-Schemafälle erfüllt; ursprüngliche Property-ID bleibt bei Rename erhalten, Instanzwerte A/B getrennt.
- **Bedeutung/Grenze:** Zusatzbinder statt nativer CEM-Unterstützung. Primitive Boolean- und Ausschnittsrevisionbindung; kein Universalresolver, keine Library-/Gesamtfigversion oder automatische X01-/X08-/A11y-Abdeckung. Originalresolver nimmt bei gleichnamigen Properties ersten Treffer; Zusatzbinder weist dies ab.
- **Weiterer Bedarf:** Andere konkrete Informationsarten/Referenzmechanismen separat prüfen. [Bericht](experiments/2026-10-25/op-external-reference/REPORT.md).

## C506

- **Kandidat / Anforderung:** Panda CSS; X08; **A**.
- **Quellen:** [S106](SOURCES.md#s106), S51/S93; E3.
- **Befund:** Ursprüngliches Merge/Tracking/Spec-Source-Annotation liefert die konkrete führende Wertquelle, einschließlich Beschreibungserweiterung und DEFAULT-Normalisierung. Neun Bedingungen erfüllt; eigener Zusatzbinder bindet Valuepointer/Quellhash an CSS-Ableitung und dokumentiert160→192px.
- **Bedeutung/Grenze:** A für genau diese Provenienz-/Ableitungskette; eigene Spec-Fixture und Zusatzjournal, keine Rust-/Gesamtcompilerprüfung oder allgemeine Vier-Domänen-Paketgovernance. X01 unverändert offen.
- **Weiterer Bedarf:** Andere tatsächlich benannte Informationsarten separat. [Bericht](experiments/2026-10-25/panda-source-ownership/REPORT.md).

## C507

- **Kandidat / Anforderung:** AgentsORG; X08; **A**.
- **Quellen:** [S107](SOURCES.md#s107), S48; E3.
- **Befund:** Vollständiger Original-CSS-Exporter und Originaldiff mit acht originalschemafähigen eigenen Fällen ausgeführt. .design-Token führt160→192px, tatsächliche Regeneration überschreibt manipuliertes generiertes CSS ohne Quellrückschreibung. Pointer-/Quell-/Exporthashes im Zusatzjournal.
- **Bedeutung/Grenze:** A nur für diese Tokenquelle/CSS-Kette. Konkreter shadcn-Gegenfall trotz map_from_tokens bleibt widersprüchlicher Literalexport; kein allgemeines Governance-, Freigabe-, SemVer-, Figma-/UI-/AT-Versprechen. X01 unverändert offen.
- **Weiterer Bedarf:** Andere konkrete Original-/Bindungsbeiträge separat prüfen. [Bericht](experiments/2026-10-25/agentsorg-export-ownership/REPORT.md).

## C508

- **Kandidat / Anforderung:** AgentsORG; X01; **A**.
- **Quellen:** [S108](SOURCES.md#s108), S107/S81; E3.
- **Befund:** Schemafähiger eigenständiger Visualvertrag mit tatsächlichen Original-CSS-Exporten an drei bytegleiche Fachartefakte und vorhandene A/B-Partziele gebunden. Zwei tatsächliche ursprüngliche SCXML-Instanzen open; native Popuphöhen192→160 bei unveränderten anderen Quellen. Vier neue Beobachtungserwartungen erfüllt.
- **Bedeutung/Grenze:** Zusätzliche begrenzte Webbindung, statische Hosts; kein genereller Eventadapter, keine portable Produktsprache oder Gesamt-Autocomplete-/AT-Konformität. Frühere Schema-/Exportfälle nicht doppelt gezählt, shadcn-Gegenbefund unverändert.
- **Weiterer Bedarf:** Übrige Kandidaten separat. [Bericht](experiments/2026-10-25/agentsorg-independence/REPORT.md).

## C509

- **Kandidat / Anforderung:** UXSpec; X03; **A**.
- **Quellen:** [S109](SOURCES.md#s109), S49; E3.
- **Befund:** Separater DTCG-duration-Originalwert via expliziter Zusatzprojektion an ursprünglichen Import/Compiler und extractMs gebunden:1s/1000ms→1000. Zehn Referenz-/zwei Originalschemabedingungen erfüllen Beobachtungserwartungen; umhüllter unveränderter Originalwert bleibt akzeptiert mit falschem Zeitwert1 statt1000.
- **Bedeutung/Grenze:** Gewählte Forschungsbeziehung Visualzeit→UX-Timereingang, keine beschlossene Produktkopplung/native DTCG-Konformität. Projektionsbibliothek mit explizitem generiertem, nicht ausgeführtem Maschinenpflichtgerüst; kein tatsächlicher Hook/Timer/Interpreter/UI/AT oder X01-Nachweis.
- **Weiterer Bedarf:** Übrige konkrete Referenzarten separat. [Bericht](experiments/2026-10-25/uxspec-duration-reference/REPORT.md).

## C510

- **Kandidat / Anforderung:** Zag; X03; **A**.
- **Quellen:** [S110](SOURCES.md#s110), S81; E3.
- **Befund:** Tatsächlicher ursprünglicher Combobox1.45.0-React-useMachine/Connect-Pfad mit zwei Instanzen und benannten Root-ID-Änderungen an separate CEM-Partknoten und HTML/ARIA-Zielrollen/-beziehungen zusätzlich gebunden. Vier Zagfälle erfüllen Erwartungen; ursprünglicher Renderpfad akzeptiert kollidierende IDs, Zusatzbinder weist ab.
- **Bedeutung/Grenze:** X03 A nur für den jeweiligen tatsächlich ausgeführten ursprünglichen SSR-Beitrag und zusätzliche CEM-Part-/HTML-Rollen-/Relationsbindung. Keine native CEM-/Universalresolverfähigkeit; ursprüngliche Akzeptanz der Gegenfälle erhalten. Kein DOMmount, Interaktions-/AT-/X01-/X08-Nachweis oder globale Repo-/Distributionsidentität.
- **Weiterer Bedarf:** Verbleibende X01-/Ownershipfragen und andere tatsächliche Zielarten separat, keine erneute identische ID-/SSR-Probe. [Bericht](experiments/2026-10-25/zag-ark-references/REPORT.md).

## C511

- **Kandidat / Anforderung:** Ark UI; X03; **A**.
- **Quellen:** [S110](SOURCES.md#s110), S81; E3.
- **Befund:** Tatsächlicher ursprünglicher Ark5.39.3-Root-/Context-/Komponentenpfad mit zwei Instanzen an separate CEM-/HTML/ARIA-Ziele gebunden. Vier Arkfälle erfüllen Erwartungen; Root-ids konsistent, einzelne Input.id-/Content.id-Overrides brechen ursprüngliche Zielbeziehungen im SSR, erst Zusatzbinder weist ab.
- **Bedeutung/Grenze:** X03 A nur für den jeweiligen tatsächlich ausgeführten ursprünglichen SSR-Beitrag und zusätzliche CEM-Part-/HTML-Rollen-/Relationsbindung. Keine native CEM-/Universalresolverfähigkeit; ursprüngliche Akzeptanz der Gegenfälle erhalten. Kein DOMmount, Interaktions-/AT-/X01-/X08-Nachweis oder globale Repo-/Distributionsidentität.
- **Weiterer Bedarf:** Verbleibende X01-/Ownershipfragen und andere tatsächliche Zielarten separat, keine erneute identische ID-/SSR-Probe. [Bericht](experiments/2026-10-25/zag-ark-references/REPORT.md).

## C512

- **Kandidat / Anforderung:** uSpec; X03; **U**.
- **Quellen:** [S111](SOURCES.md#s111), S52/S103; E3.
- **Befund:** Vollständiger ursprünglicher Cachevalidator mit vorhandener Evidence prüft lokale Outputpointer/Zielart/Feldtyp, löst fremde Datei-/Fragmenttargets nicht auf. sourcePaths darf im Test nicht existieren; geänderte tatsächliche Fremdquelle bleibt bei eingefrorenen Facts/Outputs unbemerkt. Acht Beobachtungserwartungen erfüllt.
- **Bedeutung/Grenze:** Lokale Originalfähigkeit anerkannt; kein ausreichender externer Domänenreferenznachweis. Keine globale N-Behauptung oder neuer Universaladapter.
- **Weiterer Bedarf:** Konkreter ursprünglicher oder zusätzlicher Fremdmodell-/Revisions-/Instanzbinder. [Bericht](experiments/2026-10-25/uspec-external-reference/REPORT.md).

## C513

- **Kandidat / Anforderung:** APG; X03; **A**.
- **Quellen:** [S112](SOURCES.md#s112), S55; E3.
- **Befund:** Tatsächliche unveränderte APG-Beispielklasse auf zwei Native-DOM-Kontexten mit zusätzlichem CEM-Pointer-/Klassenfeld-/Native-Typ-/Instanzbinder auf comboboxNode gebunden. Falscher HTMLDivElement-Typ, falscher Instanzkontext und fehlender CEM-Zielknoten werden zusätzlich abgewiesen; Original-CEM-Schema allein akzeptiert die Typmetadaten.
- **Bedeutung/Grenze:** A nur für den konkret ausgeführten ursprünglichen Referenzbeispielbeitrag samt zusätzlicher Host-/Interfacebindung. Kein normativer/stabiler APG-APIvertrag, neutraler allgemeiner Komponenten-/Fremdmodellstandard, Keyboard-/AT-/Lifecycle- oder X01-/X08-Nachweis.
- **Weiterer Bedarf:** Übrige unabhängige Ownership-/X01-Fragen; andere Klassenfelder und Interaktionen nicht automatisch übertragen, diesen unveränderten Fall nicht erneut ohne neuen Originalbeitrag zählen. [Bericht](experiments/2026-10-25/apg-original-reference/REPORT.md).

## C514

- **Kandidat / Anforderung:** APG; X04; **A**.
- **Quellen:** [S112](SOURCES.md#s112), S55; E3.
- **Befund:** Dieselbe tatsächliche unveränderte APG-Konstruktordefinition erzeugt zwei unterschiedliche Originalinstanzen mit eigenen list/none-Parametern und Optionsarrays. Ursprüngliche setValue/open-Methoden und nativer synthetischer Optionklick zeigen eigene A/B-Daten und Zustände in der gespeicherten Folge.
- **Bedeutung/Grenze:** A nur für den konkret ausgeführten ursprünglichen Referenzbeispielbeitrag samt zusätzlicher Host-/Interfacebindung. Kein normativer/stabiler APG-APIvertrag, neutraler allgemeiner Komponenten-/Fremdmodellstandard, Keyboard-/AT-/Lifecycle- oder X01-/X08-Nachweis.
- **Weiterer Bedarf:** Übrige unabhängige Ownership-/X01-Fragen; andere Klassenfelder und Interaktionen nicht automatisch übertragen, diesen unveränderten Fall nicht erneut ohne neuen Originalbeitrag zählen. [Bericht](experiments/2026-10-25/apg-original-reference/REPORT.md).

## C515

- **Kandidat / Anforderung:** OpenPencil; X08; **A**.
- **Quellen:** [S113](SOURCES.md#s113), S100/S105; E3.
- **Befund:** Ursprüngliche behaviourOwner-/Property-Vorrangregeln und tatsächliche behaviourControls-Projektion ausgeführt: Component Set führt vor Variante, explizite Instanzzuweisung vor Default. Nichtführende Änderung bleibt ohne Wirkung, führende Änderung erreicht den Consumer; zusätzliche Quelle/Ableitung-Hashes dokumentieren die Änderung.
- **Bedeutung/Grenze:** A nur für diese konkrete ursprüngliche Behavior-/Boolean-Quellkette mit zusätzlichem Änderungsjournal. Gespeicherte Konflikte werden priorisiert, nicht allgemein abgewiesen; keine signierte Provenienz, vollständige Graphpersistenz, universelle Governance oder Vier-Domänen-Integration.
- **Weiterer Bedarf:** X01 und andere Domänen-/Informationsarten separat prüfen; diesen Originalpfad ohne neue entscheidende Frage nicht erneut zählen. [Bericht](experiments/2026-10-25/op-owner-precedence/REPORT.md).

## C516

- **Kandidat / Anforderung:** uSpec; X08; **U**.
- **Quellen:** [S114](SOURCES.md#s114), S103; E3.
- **Befund:** Vollständiger ursprünglicher Normalisierer löst unbekannte Variant-ID per Fallback auf und markiert falsche Layerzugehörigkeit unresolved bei weiterhin geliefertem Builderergebnis. Zurückgegebener Anchor und sourceModel teilen variantProperties per Objektalias; JSON-Neuladen trennt sie, Quelldateien bleiben unverändert.
- **Bedeutung/Grenze:** Fünf Beobachtungserwartungen erfüllt, aber kein unabhängiges führendes Domänenartefakt-/Änderungs-/Konfliktmodell belegt. Rückgabealias ist keine behauptete Verletzung zugesicherter API-Unveränderlichkeit.
- **Weiterer Bedarf:** Neuer tatsächlicher Fremddomänen-Quellführungspfad. [Bericht](experiments/2026-10-25/uspec-normalizer-ownership/REPORT.md).

## C517

- **Kandidat / Anforderung:** APG; X08; **A**.
- **Quellen:** [S115](SOURCES.md#s115); E3.
- **Befund:** HTML-Modusattribut führt bei ursprünglicher Konstruktion die Flags und Filterung; zusätzliche Konsistenz-/Änderungsbindung weist Quell-/Flagkonflikte ab. Frischer Kontext folgt geänderter Quelle, keine native Livesynchronisation.
- **Bedeutung/Grenze:** Nur ein Konstruktor-Snapshot mit zusätzlichem Journal/Guard; keine allgemeine APG-Governance.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/apg-mode-ownership/REPORT.md).

## C518

- **Kandidat / Anforderung:** Zag; X01; **A**.
- **Quellen:** [S116](SOURCES.md#s116); E3.
- **Befund:** Tatsächlicher ursprünglicher Machine/connect-SSR-Beitrag mit eigenständigen Props neben CEM-Anatomie/Inputtyp, CSS und HTML/ARIA geführt. Unabhängige Visualrevision lässt drei andere Quellen und ursprünglichen Consumer zulässig.
- **Bedeutung/Grenze:** Kandidatenspezifisches zusätzliches semantisches Binding, keine montierten Interaktionen oder Gesamt-Contractkonformität.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/domain-independence-final/REPORT.md).

## C519

- **Kandidat / Anforderung:** Ark UI; X01; **A**.
- **Quellen:** [S116](SOURCES.md#s116); E3.
- **Befund:** Tatsächlicher ursprünglicher Root-/Komponenten-/Context-SSR-Pfad mit eigener Propsquelle neben CEM, CSS und HTML/ARIA; getrennte Visualrevision geprüft.
- **Bedeutung/Grenze:** Eigener Ark-Pfad, keine automatische Übertragung aus Zag; keine DOM-/Event-/AT-Gesamtzusage.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/domain-independence-final/REPORT.md).

## C520

- **Kandidat / Anforderung:** UXSpec; X01; **A**.
- **Quellen:** [S116](SOURCES.md#s116); E3.
- **Befund:** Ursprünglicher Compiler verarbeitet ein originalschemafähiges Behaviorroot ohne fremde Fachdefinitionen; zusätzliche Zustands-/Teilbindung auf getrenntes CEM/CSS/HTML. Visualrevision ohne Änderung der drei übrigen Quellen.
- **Bedeutung/Grenze:** Kein eigenständiges Visual-only-UXSpec-Root, keine Interpreter-/Timer-/Payloadruntime oder Reparatur des früheren Zeitverlusts.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/domain-independence-final/REPORT.md).

## C521

- **Kandidat / Anforderung:** Panda CSS; X01; **A**.
- **Quellen:** [S116](SOURCES.md#s116); E3.
- **Befund:** Eigenständiges Original-DesignSystemSpec-JSON wird vom tatsächlichen Originalreader/index.resolve als Visualbeitrag verarbeitet; konkrete zusätzliche CSS-Projektion auf separate CEM/SCXML/HTML-Teile.
- **Bedeutung/Grenze:** Eigene Originalformat-Fixture, kein Rustgenerator/gesamter Konfigurationscompiler; flacher Reader bleibt begrenzt.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/domain-independence-final/REPORT.md).

## C522

- **Kandidat / Anforderung:** APG; X01; **A**.
- **Quellen:** [S117](SOURCES.md#s117); E3.
- **Befund:** Vollständige ursprüngliche Beispielklasse neben getrenntem tatsächlichem CEM-Feldtyp, CSS und HTML/ARIA: native Visualrevision160→192 und separate Labelrevision bei unveränderten übrigen Quellen/Filterung.
- **Bedeutung/Grenze:** Nur illustrativer ursprünglicher Implementierungsbeitrag mit zusätzlicher Hostbindung; keine neutrale normative APG-API oder AT-Prüfung.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/apg-independence/REPORT.md).

## C523

- **Kandidat / Anforderung:** Google DESIGN.md; X01; **A**.
- **Quellen:** [S118](SOURCES.md#s118); E3.
- **Befund:** Tatsächlicher Original-lint-Coloroutput aus separatem DESIGN.md an explizite CSS-Foregroundziele im getrennten HTML/CEM/SCXML-Profil gebunden; Quellrevision erreicht Ableitung, drei andere Fachquellen bytegleich.
- **Bedeutung/Grenze:** Zusätzliche Projektion verwendet originales hex; kein Dokument-Schemaentscheid, X06 U unverändert.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/google-independence/REPORT.md).

## C524

- **Kandidat / Anforderung:** OpenUI; X01; **A**.
- **Quellen:** [S119](SOURCES.md#s119); E3.
- **Befund:** Einfacher String-Propertybeitrag des unveränderten tatsächlichen interfaces/Spec.ts per zusätzlicher Literal-/Originaltypbindung neben eigenständigem SCXML/CSS/HTML geführt; Interface-Beschreibungsrevision ohne Fremdquelländerung.
- **Bedeutung/Grenze:** Nur benannter Originaltypgegenstand, keine kanonische Vorrangentscheidung oder ursprüngliche JSON-Schemavalidierung; X06 U bleibt.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/openui-independence/REPORT.md).

## C525

- **Kandidat / Anforderung:** OpenPencil; V04; **R**.
- **Quellen:** [S120](SOURCES.md#s120); E3.
- **Befund:** Ursprüngliche Slider-SLOT-/Behavior-/Vue-Generatorkette verweist tatsächlich auf Reka-Parts. Referenzierte Root-/Startkanten-/Contain-Offsetsemantik nativ bei25/75 und Rootbreiten200/300 gemessen.
- **Bedeutung/Grenze:** Nur SliderRoot→Thumb-Geometrie. Zwei ursprüngliche SSR-Thumb-Erwartungen widerlegt erhalten; dritter nativer Host eigene CSS-Rootrevision. Frühere Popup/Inputankerrelation bleibt unerfüllt.
- **Weiterer Bedarf:** Stärkere vollständige Integration bleibt separat. [Bericht](experiments/2026-10-25/op-slider-geometry/REPORT.md).

## C526

- **Kandidat / Anforderung:** CSS Layout; I01; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** CEM-maxHeight:number ist konkret an px und den tatsächlichen CSS-Maximalhöhenparameter gebunden: A192/B160 bei Inhaltshöhe224. Falscher Werttyp, Einheit und abgeleiteter Propertytyp werden zusätzlich abgewiesen.
- **Bedeutung/Grenze:** Keine native CSS-Komponenten-API; enger zusätzlicher primitiver Typ-/Einheitsbinder.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C527

- **Kandidat / Anforderung:** CSS Layout; I02; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Tatsächlicher ursprünglicher SCXML-Parentsend liefert value-change/value/query; zusätzliche CEM-/Instanzprüfung routet das öffentliche Hostevent bei tatsächlich geschlossenem CSS-Zustand. Ursprünglich geliefertes query42 und fremder Parent werden zusätzlich abgewiesen.
- **Bedeutung/Grenze:** Eventziel ist die eigene Forschungssection, kein implementiertes Custom Element. Originale CEM-/SCXML-Prüfer übernehmen keine Zusatzpayload- oder CSSrouteprüfung.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C528

- **Kandidat / Anforderung:** CSS Layout; B01; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Tatsächliche ursprüngliche closed→open→closed-Folge ist mit CSS none→block→none gebunden; B bleibt closed. CSS führt die Displayregel, der Binder nur den tatsächlichen Zustandsmarker.
- **Bedeutung/Grenze:** Kein CSS-eigener UX-Automat oder allgemeiner Layoutfallback als UX-Logik.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C529

- **Kandidat / Anforderung:** CSS Layout; B02; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Tatsächliche ursprüngliche SET_ENABLED-Assign-/cond=enabled-Auswertung blockiert OPEN bei false; true erlaubt open und tatsächliches CSS-block.
- **Bedeutung/Grenze:** Guard-/Aktionssemantik kommt aus dem ausgewiesenen externen Original-SCXML; Zusatzbinder wertet Guard nicht selbst aus.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C530

- **Kandidat / Anforderung:** CSS Layout; B03; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Ereignisquery wird durch ursprüngliches Assign im Kontext gehalten und neben dem bestätigten value per ursprünglichem Parentsend ausgegeben. Falscher öffentlicher Inputtyp wird zusätzlich abgewiesen.
- **Bedeutung/Grenze:** Primitiver CEM-Datenbinder, kein vollständiger TypeScriptwertvalidator; akzeptierter interner query42-Bypass bleibt als Originalgrenze sichtbar.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C531

- **Kandidat / Anforderung:** CSS Layout; B04; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Synthetische native Input-ArrowDown-Events durchlaufen ausdrücklich zusätzlichen Keyrouter, steuern tatsächliche ursprüngliche Maschine und CSS-Ausgabe; A/B-Zustand und DOM-Fokus separat beobachtet.
- **Bedeutung/Grenze:** Zusatzrouter statt nativer CSS-/SCXML-Keysemantik, keine physischen vertrauenswürdigen Tasten oder AT-Prüfung.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C532

- **Kandidat / Anforderung:** CSS Layout; A01; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Konkrete CSS-Popupziele sind an richtige HTML/ARIA-Listbox-/Namens-/Kontrollziele gebunden. Falscher Labeltext und fremdes Controls-Ziel werden erkannt; tatsächlicher Browser-AX-Baum bestätigt Search A/B und Results A.
- **Bedeutung/Grenze:** Enger expliziter Zusatzbinder, keine automatische Erzeugung zugänglicher Semantik durch CSS-Nähe oder allgemeine Accname-Konformität.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C533

- **Kandidat / Anforderung:** CSS Layout; A02; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Gepinnter APG-Combobox-Listboxbezug bestimmt zusätzlichen endlichen Keypfad: Escape schließt bei erhaltenem Inputfokus, Enter übernimmt aktive Option und schließt. Abweichende abgeleitete Keyroute wird abgewiesen.
- **Bedeutung/Grenze:** ArrowDown-/Instanzfolge separat P91; nicht doppelt gezählt. Keine vollständige APG-Optionaltasten-/Popup-/Plattform-/AT-Konformität.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C534

- **Kandidat / Anforderung:** CSS Layout; A03; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Tatsächliches bestätigtes Originalevent ist an eigene status/polite/atomic-Region gebunden; Präfix führt HTML, native AX-Region bestätigt Eigenschaften und Text. CSS-only-Änderung bleibt ohne Meldung; falsches live wird abgewiesen.
- **Bedeutung/Grenze:** Explizite zusätzliche Ereignis-/A11y-Bindung statt CSS-Meldungssprache; native AX-Beobachtung bestätigt keine Screenreader-Sprachausgabe.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C535

- **Kandidat / Anforderung:** WAI-ARIA; V06; **A**.
- **Quellen:** [S121](SOURCES.md#s121); E3.
- **Befund:** Tatsächliche aria-controls-Liste ist an ihren richtigen CSS-Scrollport gebunden.7×32px in160px, aktive7. Option sichtbar bei scrollTop64. Fremde Liste und clip-Variante mit unsichtbarer aktiver Option liefern eigene Bindungskonflikte.
- **Bedeutung/Grenze:** ARIA definiert keine eigene CSS-Overflowpolitik. clip ist gültiges CSS und scheitert nur am konkret verlangten Sichtbarkeitsprofil; keine universelle Scroller-/AT-Zusage.
- **Weiterer Bedarf:** Vollständige Integration bleibt separat. [Eigener kriteriumsbezogener Nachweis](experiments/2026-10-25/css-complement-runtime/REPORT.md).

## C536

- **Kandidat / Anforderung:** uSpec; X03; **A**.
- **Quellen:** [S122](SOURCES.md#s122); E3.
- **Befund:** Tatsächliche externe CEM-Datei/Pointer/Field-/Modul-/Definitions-/Typ-/Revisionsauflösung an ursprünglichen Evidence-Fact/sourcePaths und tatsächlichen lokalen APIoutput gebunden; gezielte fremde/missing/stale Targets abgewiesen.
- **Bedeutung/Grenze:** Zusätzlicher eng begrenzter Definitionsresolver, keine native uSpec-Fremdauflösung oder erfundene konkrete UI-Instanzreferenz.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/uspec-cem-ownership/REPORT.md).

## C537

- **Kandidat / Anforderung:** uSpec; X08; **A**.
- **Quellen:** [S122](SOURCES.md#s122); E3.
- **Befund:** CEM-Propertyname/-Typ führt ausdrücklich Fact/equals/APIoutput. Tatsächliche Quellenrevision und erneutes Dateilesen zur Ableitung werden samt Konflikten und vorher/nachher-Journal dem Originalvalidator zugeführt.
- **Bedeutung/Grenze:** Zusätzliches per-information-Ownershipjournal, kein originales allgemeines Governance-/Rechte-/Transaktionssystem. Dieselben14 Bedingungen wie X03 nur einmal gezählt.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/uspec-cem-ownership/REPORT.md).

## C538

- **Kandidat / Anforderung:** uSpec; X01; **A**.
- **Quellen:** [S123](SOURCES.md#s123); E3.
- **Befund:** Tatsächlich eigenständig prüfbarer ursprünglicher APIcache mit Evidence neben separatem SCXML/CSS/HTML; CEM führt Interface, Cache/Fact sind Ableitung. Visualrevision und tatsächliche ursprüngliche SCXML-Publicwertrevision ohne Fremdmasteränderung.
- **Bedeutung/Grenze:** Nur ursprünglicher APIcache-Teilgegenstand, kein unabhängig ladbarer partieller Canonical-Gesamtroot oder vollständige Autocomplete-/Figma-Pipeline.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/uspec-api-independence/REPORT.md).

## C539

- **Kandidat / Anforderung:** OpenPencil; X01; **A**.
- **Quellen:** [S124](SOURCES.md#s124); E3.
- **Befund:** Vier tatsächliche CEM/OPS/CSS/HTML-Master erzeugen den Scenegraph ausdrücklich als Ableitung. Original-SG/OPS/Instanz/Control/Projektions- und unveränderte isolierte Vue-/Reka-SSR-Kette folgt getrennten Visual-/Namens-/Defaultrevisionen; Behavior/A11y-Rollenkonflikt zusätzlich erkannt.
- **Bedeutung/Grenze:** Kein zweiter Graphmaster, universeller Importer oder ganzer Editor. Exakte A/B-Namen und aria-checked im tatsächlichen Original-SSR geprüft; keine native UI-/AT-Abnahme.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/op-four-masters/REPORT.md).

## C540

- **Kandidat / Anforderung:** UXSpec; V04; **A**.
- **Quellen:** [S125](SOURCES.md#s125); E3.
- **Befund:** Tatsächlich kompilierter ursprünglicher Visualslot an separates CEM-/DOM-Ziel und eigene explizite CSS-Ankerrelation gebunden. Abstand8 bleibt bei Input20→40; fremde/fehlende Ziele und nicht unterstützte Einheit abgewiesen.
- **Bedeutung/Grenze:** Zusätzliche Ziel-/Richtungs-/Abstandssemantik, keine native UXSpec-Inputankerfähigkeit. Original-Runner/React-Renderer nicht ausgeführt.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/layout-final-bindings/REPORT.md).

## C541

- **Kandidat / Anforderung:** UXSpec; V06; **A**.
- **Quellen:** [S125](SOURCES.md#s125); E3.
- **Befund:** Tatsächlicher Originalcompiler/Stylemapper liefert Slot/160px, ignoriert ursprüngliches overflow weiterhin. Explizite zusätzliche auto-/feste-Zeilenpolitik ergibt native160/224/64; fehlende Politik/fremder Port abgewiesen.
- **Bedeutung/Grenze:** A nur mit zusätzlichem Overflow-/Zeilensizing. Initiale eigene Erwartung scheiterte an tatsächlicher Original-Flexschrumpfung und bleibt erhalten; Originalmapper unverändert.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/layout-final-bindings/REPORT.md).

## C542

- **Kandidat / Anforderung:** uSpec; V04; **A**.
- **Quellen:** [S125](SOURCES.md#s125); E3.
- **Befund:** Tatsächlich vom Originalbuilder normalisierter Section-Messanker an richtigen CEM-/DOM-Instanzkontext und zusätzliche native CSS-Zielkantenrelation gebunden. Abstand8 bleibt20→40; fremder und tatsächlich unresolved ausgegebener Anker abgewiesen.
- **Bedeutung/Grenze:** Messanker bleibt ursprüngliche Messidentität, Runtimegeometrie ist Zusatzbinding. Keine behauptete eigene ursprüngliche Overlay-/Targetsemantik.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/layout-final-bindings/REPORT.md).

## C543

- **Kandidat / Anforderung:** uSpec; V06; **A**.
- **Quellen:** [S125](SOURCES.md#s125); E3.
- **Befund:** Vollständige unveränderte ursprüngliche extractDims/sg-Funktion erhält clipsContent auf clipping-only Minimalnodes; Originalbuilder bewahrt den Beleg. Zusatzmapping true→CSSclip/false→visible nativ anhand letzter gemalter Zeile geprüft; fehlender/untypisierter Beleg abgewiesen.
- **Bedeutung/Grenze:** Kein Figma-SDK oder ausgeführter numerischer Bindingbranch. Kein auto/scroll aus Clipping erfunden; feste zusätzliche Clip/Visible-Politik und Testviewport, kein universeller Scrollvertrag.
- **Weiterer Bedarf:** Globale Integration bleibt stärkerer separater Gegenstand. [Nachweis](experiments/2026-10-25/layout-final-bindings/REPORT.md).
