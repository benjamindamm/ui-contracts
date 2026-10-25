# Originaler Szenenbaum bis zum zugänglichen Switch-Update

Stand: 25. Oktober 2026. **28 unterschiedliche Bedingungen in fünf neuen Gruppen; 26 numerische Erwartungen erfüllt, zwei anfängliche Namensprüfer-Erwartungen widerlegt und erhalten.** Der anschließend passend abgegrenzte Originalpfad einschließlich lebendem Host funktioniert im beschriebenen Umfang. OpenPencil A01 und A03 werden für den konkret gebundenen Switch-Webpreviewbeitrag als R eingeordnet.

## Fehlende Aussage und Endbedingung

Die vorherige Radio-SSR-Probe begann mit bereits vorbereiteten Role-/Element-/Stateobjekten. Offen waren deren Ursprung aus dem tatsächlichen Scenegraph, die ursprüngliche Roleklassifizierung und die lebende Verbindung vom Original-Controlstate zum zugänglichen Hostzustand.

Endbedingung: konkrete Originalkomponenteninstanzen erzeugen; Originalprojektion, Behaviour-/Roleauflösung und Statefactory aufrufen; Namen-/Zustandsursprung bis zur tatsächlichen Ausgabe verfolgen; anschließend zwei Switchinstanzen im Browser getrennt umschalten und Rolle, Name sowie aria-checked beobachten. Diese Endbedingung ist für den genannten Switchpfad erreicht. Vollständiger Editor, Graphpersistenz, universelle Meldungen und Assistenztechnik waren keine ersetzten oder still mitbewerteten Gegenstände.

## Originalstände und ausdrückliches Laufzeitprofil

- Veröffentlichte @open-pencil/scene-graph **0.16.0** und @open-pencil/dom-css **0.16.0**, Registryintegrität und Paketlock gebunden. Die Registry liefert hier keinen gitHead; Identität mit dem früheren Repo-Commit wird nicht unterstellt.
- Originale Vue-Islandfunktionen vom zuvor gebundenen OpenPencil-Commit **ab2875cc761ee6cff17d389ff1c85fedae50aeab**, unverändert anhand des TypeScript-AST isoliert.
- Tatsächliches **Vue 3.5.41**, einschließlich Serverrenderer, und **reka-ui 2.10.5**. Beide liegen in den bereits dokumentierten Original-Abhängigkeitsbereichen; das ist das explizite Forschungsprofil, kein behaupteter Lockstand eines kompletten Editors.
- Vorhandenes **axe-core 4.14.0** und BrowserOS/Chromium 155. Die Bundleintegrität der Prüfbibliothek wird vom Browser kontrolliert.

Die mitveröffentlichte Original-Source-Map von dom-css enthält projection.ts. Ihre Importpfade unterscheiden sich vom Repo-Capture. **Alle Nicht-Import-Deklarationen dieser einen Datei sind textgleich**; vollständige Quellhashes bleiben dennoch verschieden. version-comparison.json bindet diesen konkreten Vergleich. Daraus wird keine Identität aller Repo-/Paketdateien oder ihrer Abhängigkeiten abgeleitet.

## Tatsächlich ausgeführter Pfad

Die öffentlichen Originalpakete führen SceneGraph, createNode, **SceneGraph.createInstance**, emptyBehaviour/withBehaviour, missingBindings, sceneGraphToDesignDocument, behaviourControls und controlRoles aus. Keine erfundene Graph- oder Roleimplementierung ersetzt diese Schritte.

Anschließend laufen vierzehn unveränderte Original-Vue-Deklarationen, darunter createIslandState mit seinen echten Helfern, wrapRole/root/asChild, stateOf/disabled/interaction und renderNode/renderElement. Die tatsächlichen ursprünglichen Imports booleanOf, numberSettings, layerPath sowie BUTTON_RESET werden an die gepinnten Originalpakete gebunden. SwitchRoot und Toggle stammen aus dem echten Reka-Paket. Die eigenen Rahmen stellen ausschließlich Forschungsinputs, SSR-Aufruf und Browser-Appstart bereit. Dieses minimale Hostfixture ist keine neue Produktkomponente.

Die Graphfixtures enthalten eine Componentdefinition mit Booleanproperty, ursprünglichem Switch- beziehungsweise Radiobehaviour und gezeichnetem TEXT-Kind. Zwei tatsächliche Komponenteninstanzen werden aus dieser Definition erzeugt. Im Livefall stammen die verschiedenen Namen aus konkreten Textlayer-Overrides der Instanzen, nicht aus nachträglich eingefügten aria-label-Attributen. Der Renderer erhält seine Role-/Stateobjekte aus den ursprünglichen Funktionen.

## Zwölf Graph-/Klassifizierungs-/SSR-Bedingungen (P50)

| Fall | Beobachtung |
| --- | --- |
| Gezeichneter Radiotext | Inhalt wird durchgehend übernommen; role=radio |
| Nur Szenenknotenname, kein Textkind | kein Beschriftungsinhalt erzeugt |
| Unsichtbares Textkind | nicht als sichtbarer Hostinhalt übernommen |
| Zwei gleichnamige Radioinstanzen | getrennte ursprüngliche Layerpfade/Controlstates |
| Booleanassignment=true | ursprüngliche Statefactory liest den tatsächlichen Propertywert |
| Fehlende erforderliche Valuebindung | missingBindings meldet value; das Control wird dennoch aufgebaut und fällt im Renderpfad auf false zurück |
| Tokenpfad aktiviert | gleicher Namensinhalt im getesteten Graph ohne zusätzliche Variablen |
| Source-ID-Attribute deaktiviert | Roleklassifizierung und Inhalt bleiben im ursprünglichen Pfad verbunden |
| Gezeichneter Switchtext | echtes SwitchRoot erhält den projizierten Inhalt |
| Switch mit bloßem Knotennamen | keine automatisch erzeugte Beschriftung |
| Switchassignment=true | ursprünglicher State erreicht Reka/SSR als checked |
| Zwei gleichnamige Switchinstanzen | beide Controls mit getrennten Pfaden/States ausgegeben |

Zwölf Erwartungen erfüllt. Die ersten acht erfolgreichen Fälle bleiben zusätzlich in initial-eight-success-results.json erhalten. Die vier Switchfälle wurden vor ihrer Ausführung ergänzt. Wiederholungen der acht früheren Inputs werden nicht zusätzlich gezählt.

Ein eigener erster Harnischversuch verwendete irrtümlich die interne Standalone-Signatur createInstance als Rootexport. Die tatsächlich öffentliche Klassenmethode wurde danach korrekt verwendet. initial-api-path-error.json und harness-repair.json erhalten diesen Fehler. Originalpakete und Voraberwartungen wurden nicht geändert; es ist kein Produktfehler und keine zusätzliche Prüfgruppe.

## Namensprüfung: zunächst unpassender Matcher, dann passende Originalregel

Die drei ersten Browserbedingungen (P51) verwendeten aria-toggle-field-name auf den tatsächlichen nativen Buttonhosts. Die Regel liefert hier keine anwendbaren Pass-/Violationknoten. Ihre Original-Matcherfunktion überspringt Hosts mit vorhandener nativer Benennungsmethode. Daher trifft nur eine von drei ursprünglichen **numerischen** Erwartungen zu; zwei Erwartungen an eine Diagnose wurden widerlegt. Ein leeres Ergebnis wird ausdrücklich nicht als gültiger Namensnachweis ausgegeben.

Die passend ausgewählte unveränderte Originalregel **button-name** liefert drei vorab gespeicherte Diagnosebedingungen (P52): gezeichneter Text besteht mit tatsächlichem Passknoten; bloßer Knotenname und unsichtbares Textkind erzeugen jeweils den erwarteten Namensverstoß. Alle drei Erwartungen erfüllt. Die frühere Fehlwahl bleibt mit ihren Ergebnissen erhalten.

Vier zusätzliche Switchbedingungen mit derselben passenden Regel (P53) prüfen gezeichneten Text, fehlenden Inhalt, true-Wert und zwei Instanzen. Drei Varianten bestehen mit einem beziehungsweise zwei tatsächlichen Passknoten, die unbenannte Variante erzeugt den erwarteten Verstoß. aria-checked enthält die erwarteten false-/true-Werte. Alle vier Erwartungen erfüllt. Es handelt sich um abgegrenzte Namens-/Attributchecks, nicht um einen vollständigen axe-/WCAG-/ARIA-Audit.

Die unveränderten ursprünglichen Radioausgaben sind trotz Laufzeitinstallation bytegleich; ihre Browserergebnisse bleiben an den ursprünglichen Ergebnisdateihash gebunden. Die Switchprüfungen verweisen auf den neuen Zwölf-Fälle-Output. Keine Quelle wurde nachträglich unter einem alten Hash ausgetauscht.

## Sechs lebende Switchschritte (P54)

Der zusätzliche kleine Appstart verwendet denselben Originalgraph-/Projektions-/Role-/Statepfad und dieselben unveränderten Vue-/Reka-Funktionen im Browser. BrowserOS-Aktionen betätigen die tatsächlich gerenderten Controls. Der letzte Fall verwendet nach dem Sperren einen nativen programmgesteuerten click-Aufruf. Das ist keine physische Tastatur- oder Assistenztechnikprüfung.

| Schritt | Controlstate A/B | Tatsächliches aria-checked A/B | Zugängliche Namen |
| --- | --- | --- | --- |
| Initial | false / false | false / false | Option A / Option B |
| A einschalten | true / false | true / false | unverändert |
| B einschalten | true / true | true / true | unverändert |
| A ausschalten | false / true | false / true | unverändert |
| B ausschalten | false / false | false / false | unverändert |
| A disabled, nativen programmgesteuerten Click versuchen | false / false | false / false | unverändert; A disabled |

Alle sechs Voraberwartungen erfüllt. Browser-Snapshots melden jeweils zwei benannte Switches; der zugehörige DOM- und Original-Controlstate stimmt in jedem Schritt überein. Der andere Instanzkontext bleibt getrennt. Die Backendknoten bleiben in den gespeicherten Beobachtungen erhalten. Es wurde keine graphweite Persistenz, visuelle Variantenneuberechnung oder Wiederherstellung nach Dokumentreload geprüft.

Der Browserbuild erforderte zwei ausdrücklich eigene Konfigurationskorrekturen: Auflösung der isolierten node_modules und Umgang mit einem unbenutzten Node-only-Dateiimport des allgemeinen HTML-/Tailwindexporters. Dieser Import wurde als extern markiert und ist nach Tree-Shaking **nicht im tatsächlichen Browserbundle enthalten**. Keine Ersatzfunktion beziehungsweise leere Bibliotheksattrappe eingeführt. live-build-repair.json hält die Fehler vor Ausführung der Livebedingungen fest. Das Ergebnis ist keine pauschale Aussage, dass alle öffentlichen Paketausgänge ohne weitere Konfiguration im Browser ausführbar sind.

## A01 und A03: begrenzte Referenzbeiträge

**A01 U → R/C494, ausschließlich für den überprüften Switch-Webpreviewbeitrag.** Die bestehende Kette ist jetzt ausgeführt: Original-Component/TEXT-Instanz → ursprüngliche Projektion/Roleklassifizierung → Reka SwitchRoot → benannter nativer Host. Name und Zustand entstehen aus den tatsächlich gebundenen Originaldaten. Die WAI-ARIA 1.2-Switchdefinition erlaubt den Namen aus Inhalt/Autor und definiert die zugehörige on/off-Semantik. Es wird keine neue fachliche Bedeutung eingeführt. Die Verbindung zwischen dem Control und seinem projizierten Namensinhalt ist konkret belegt; externe Label-/Control-/Fehler-IDREFs beliebiger Widgets sind damit nicht mitbewertet. Das ist dieselbe begrenzte Beitragsrolle wie der bereits als R geführte Switch-Tastaturmusterbezug, keine Behauptung einer allgemeinen neutralen Accessibility-Dateisprache.

**A03 U → R/C495, ausschließlich für die zugängliche on/off-Zustandsrückmeldung dieses Switchpfads.** Auslöser ist die ursprüngliche Controlaktivierung; Inhalt ist der Booleanwert; Ziel ist der zugehörige Switchhost; Übergabezeitpunkt ist der tatsächlich beobachtete Vue-/Reka-Updatepfad. aria-checked besitzt bereits definierte zugängliche Bedeutung. Die normative Definition wurde gezielt erneut gelesen und mit den tatsächlichen Zustandswechseln verbunden. Live-Regions, Suchergebnisanzahlen, Fehler-/Lademeldungen und produktbezogene Ansageformulierungen bleiben andere, nicht behauptete Beiträge. A03 wird nicht nachträglich um eine allgemeine Pflicht zu frei formulierten Meldungen für jedes Widget verschärft.

Der Namensinhalt stammt weiterhin aus dem gezeichneten TEXT und bleibt in diesem Originalpfad damit gekoppelt. Eine davon unabhängig geführte Accessibility-Masterdatei ist nicht nachgewiesen; X01/X08 werden hier nicht verändert.

R bedeutet vorhandene bibliotheks-/plattformbezogene Referenzsemantik im genannten Profil. Es bedeutet weder originale Sprachneutralität, vollständige Vier-Domänen-Trennung noch universelle Unterstützung aller OpenPencil-Kinds. Kein Screenreader, keine physische Tastatur, kein vollständiger Editorbuild und keine allgemeine Conformanceprüfung. Die negativen Namens-/Bindingsfälle bleiben sichtbar; korrektes Originaltooling ersetzt keine verantwortete Autoreneingabe.

## Ergebnis und Reproduktion

**42 U: 26 Integration und 16 weitere. 423 unterschiedliche Bedingungen in 54 Gruppen.** Dieses Paket fügt 28 Bedingungen hinzu (12+3+3+4+6), nicht die Summe sämtlicher wiederholter Aufrufe. Zwei anfängliche Prüferwartungen bleiben widerlegt; alle 12 abschließenden Graphbedingungen, drei passenden Radio-Namensdiagnosen, vier Switch-Namensbedingungen und sechs Liveschritte sind erfüllt.

cases.json, die vier Browser-/Live-Erwartungsdateien und ihre Ergebnisse halten Eingaben, Entscheidungen und beobachtete Knoten getrennt fest. extraction.json bindet die Original-Vue-Deklarationen, published-pins.json/Paketlock die veröffentlichten Pakete; version-comparison.json grenzt den Quellvergleich ab. Der Probehost wird durch prepare-live.cjs gebaut. Drittanbieterquellen, Originalbibliotheksbundle und axe.min.js bleiben lokal und werden nicht als eigene Produktionsimplementierung exportiert; deren Hashes werden im Manifest erhalten. Die eigenen Graphinputs, Builder, HTMLfixtures, Ergebnisse und Originalfundstellen bleiben nachvollziehbar.

Kein Commit/Push, keine neuen Agenten oder Chats, keine endgültige Plattform-/Produktsyntaxentscheidung. Der Restplan wird mit beiden konkret geschlossenen Beiträgen und allen noch offenen Original-/Integrationsfragen fortgeschrieben.
