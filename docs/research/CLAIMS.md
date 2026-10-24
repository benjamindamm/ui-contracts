# Claim- und Befundregister

Abdeckung und Evidenzstufe folgen [METHODS.md](METHODS.md). Alle Quellenstände stehen in [SOURCES.md](SOURCES.md). Die Matrix verweist auf diese IDs; Interpretation und nächster Versuch sind Teil jedes Befunds. **Kein Eintrag behauptet einen ausgeführten Compiler-, Validator- oder Laufzeitversuch.**

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

- **Kandidat / Anforderung:** UXSpec; V04; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Layoutprimitiven stack/grid/layer und offene container-/Elementobjekte sind belegt; ein normatives Anker-Ziel-Richtung-Abstand-Modell wurde nicht gefunden. S Layout/Visual; J visual.container/elementBase; W.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Konkrete Frage: Welche originale dokumentierte Eigenschaft bindet ein Overlay geometrisch an ein benanntes anderes Element, mit Einheiten/Auflösung? Freie Felder und CSS des Webadapters reichen nicht für D; fehlender Fund allein führt nicht N.
- **Offene Frage / weiterer Bedarf:** Konkrete Frage: Welche originale dokumentierte Eigenschaft bindet ein Overlay geometrisch an ein benanntes anderes Element, mit Einheiten/Auflösung? Freie Felder und CSS des Webadapters reichen nicht für D; fehlender Fund allein führt nicht N.

## C191

- **Kandidat / Anforderung:** UXSpec; V05; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Dimensionen und Elementgrößen sind strukturiert möglich; kein ausreichender Originalnachweis für formale maximale Höhe/Fläche. S/F; J offene Visualfelder; W mapSize.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Welche originale Regel definiert maxHeight/max-area einschließlich Einheit/Bezug? Beliebiges zulässiges JSON-Feld ist keine bestätigte Semantik; fünf Zeilen/variable Zeilenhöhe nicht bewiesen.
- **Offene Frage / weiterer Bedarf:** Welche originale Regel definiert maxHeight/max-area einschließlich Einheit/Bezug? Beliebiges zulässiges JSON-Feld ist keine bestätigte Semantik; fünf Zeilen/variable Zeilenhöhe nicht bewiesen.

## C192

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

- **Kandidat / Anforderung:** UXSpec; X03; **U**.
- **Quellen:** [S49](SOURCES.md#s49); E1/E2, manuell gelesene Primärdefinitionen, keine Ausführung. Lokale Quellenkürzel des Befunds sind unter S49 aufgelöst.
- **Befund:** Aliasqualifizierte Imports erschließen getrennte Token-/Element-/Maschinenquellen; konkrete Namensauflösung in I/R. S/F Referenzen, M Composability, J imports.
- **Bedeutung/Grenze:** U im begrenzten untersuchten Modell (UXSpec am gepinnten Commit 20dfae0e7224d952e198afdf4ffed26d6fd67180). Starker Teilbefund, aber bisher UXSpec-eigene Teile: kein ausreichender Nachweis, dass Ziele in **separaten originalen Interface-/Visual-/Behavior-/A11y-Domänen** semantisch adressiert werden. Welche Originalartefakte/Bindungen bleiben unverändert? Tokenreferenz allein erfüllt X03 nicht.
- **Offene Frage / weiterer Bedarf:** Starker Teilbefund, aber bisher UXSpec-eigene Teile: kein ausreichender Nachweis, dass Ziele in **separaten originalen Interface-/Visual-/Behavior-/A11y-Domänen** semantisch adressiert werden. Welche Originalartefakte/Bindungen bleiben unverändert? Tokenreferenz allein erfüllt X03 nicht.

## C203

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

