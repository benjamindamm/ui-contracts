# Autocomplete · 0.1.0

Ein editierbares Suchfeld mit manueller Listenauswahl. **Dies ist der führende Bibliothekseintrag**, kein Auftrag zu einer unabhängig gestalteten Komponente. Der erste Export ist ein editierbares OpenPencil-Design; eine interaktive Canvas-Preview wird nicht gefordert.

## Die Definition lesen

1. component.json: Identität, Domänenquellen, Teile und Unterkomponenten.
2. interface.json: CEM-Signatur mit Label, Platzhalter, Query, optionalem bestätigtem Wert, Ergebnisrecords und enabled.
3. ../tokens.json und die drei layout.css-Dateien: sämtliche benannten Designwerte und konkrete Layout-/Zustandsregeln.
4. behavior.scxml: formale Zustände und Übergänge. Die referenzierten Overlay-/ScrollArea-Definitionen gehören dazu.
5. accessibility.html und accessibility.rules.json: Namen, Rollen, Zustandsprojektion und Meldungstexte.
6. stories.json: zehn konkrete Darstellungsfälle aus derselben Definition.

## Fachliche Regeln

Query ist der editierbare Entwurf; value ist der zuletzt ausdrücklich bestätigte Ergebniskey. value fehlt ohne Auswahl und wird nicht durch null ersetzt. Jeder Ergebnisrecord hat einen eindeutigen nichtleeren key und label; disabled ist optional und bedeutet ohne Angabe false. Eine aktive Option führt erst durch Bestätigung zum Wert. Die zugänglich gemeldete Popupauswahl folgt der aktiven Option.

Pfeilnavigation überspringt deaktivierte Optionen, läuft nicht zyklisch und verändert value nicht. Enter bestätigt einmal und schließt; Escape und Fokusverlust schließen ohne neue Bestätigung. Freier Text wird nicht als neuer Ergebniswert bestätigt. Queryänderungen behalten den letzten bestätigten Wert. Veraltete Antworten dürfen weder aktuelle Ergebnisse noch Meldungen ändern. Die tatsächliche Webausführung benötigt dazu den Plattformadapter; ein Designexport stellt diese Zustände dar.

Autocomplete besitzt Input, Listbox, Optionen und Status. Das Popup ist die eigene Overlay-Verwendung; darin liegt die eigene ScrollArea. Listbox, Overlayfläche und Scrollviewport sind unterschiedliche Teile. Die Option wird über den fachlichen Key identifiziert. Ein Overlay besitzt keine zweite Auswahlmaschine.

## Sichtbare Geometrie

Label oben, darunter nach labelGap der Input. Das Popup richtet seine Oberkante am Inputende plus gap aus, hat dieselbe Breite und dieselbe linke Kante. Die Viewporthöhe ist bei Ergebnislisten min(Ergebnisanzahl × rowHeight, maxHeight). Zeilen bleiben rowHeight hoch. Bei loading, empty und error zeigt der Popupinhalt eine Zeile mit der entsprechenden Meldung; die Statusregion wiederholt den Text als benannter Status darunter. Ein verborgener Popup belegt keinen Platz. Der Status steht nach statusGap unter dem tatsächlich sichtbaren Popup, sonst unter dem Input. Ohne Meldung ist sein Text leer.

Der Fall scroll-end muss die aktive letzte Option tatsächlich im sichtbaren Viewport darstellen. Für das Design darf dazu der Inhalt des geclippten Viewports entsprechend versetzt werden. Alle Ergebnislayer bleiben editierbar erhalten; nicht einfach die drei unsichtbaren Daten löschen. Das ist eine statische Darstellung dieses Zustands, kein Versprechen dynamischen Scrollens im Canvas.

Die zehn Fälle heißen closed, opening, loading, ready, active, scroll-end, selected, empty, error und disabled. active und scroll-end sind ready mit activeKey; selected ist closed mit value; disabled ist closed mit enabled=false. Es sind keine zusätzlich unabhängig geführten SCXML-Zustände. Bei selected steht das zu value gehörige Label im Input, und der Status nutzt die selected-Vorlage. Bei disabled sind keine Popupteile sichtbar. In allen Fällen kommen sichtbare Texte aus den Inputs, Ergebnislabels und accessibility.rules.json.

## Exportrahmen

Das OpenPencil-Dokument soll eine übersichtliche Seite mit den zehn benannten Fällen enthalten. Die Außenanordnung der Fälle, Seitentitel und beschreibende Hinweise sind frei; **die Komponente selbst** folgt den Quellen. Jeder Fall muss als Komponenten-/Framelayergruppe benannt sein. Input, Overlayfläche, Scrollviewport, Listbox, einzelne Optionen und Status sollen separat editierbar und verständlich benannt bleiben. Farbe, Typografie, Maße und Meldungen dürfen nicht still neu erfunden werden.

Fehlt eine notwendige Angabe, dokumentiert der Exporteur sie als Lücke. Er darf diese Definitionsdateien nicht passend zu seinem Ergebnis ändern. Die erzeugte Datei muss sich tatsächlich als OpenPencil-Dokument öffnen lassen. Ein Bild, eine umbenannte JSON-Datei oder ein allein im Speicher existierender Graph genügt nicht.
