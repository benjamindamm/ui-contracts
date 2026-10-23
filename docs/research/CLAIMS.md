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

