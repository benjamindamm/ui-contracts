# Autocomplete – unabhängiger Builder B

## Ergebnis und Reproduktion

`autocomplete.fig` ist ein binärer, vom Original-OpenPencil-Writer erzeugter FIG-Container (31 456 Bytes), kein umbenanntes JSON. Er enthält eine Seite mit zehn benannten Framelayergruppen und 136 wieder eingelesenen Knoten. FIG ist das vom installierten OpenPencil-Reader unterstützte Dokumentformat. Es wurde kein fremdes Ergebnis und keine Projektdatei außerhalb der Komponentenbibliothek und der unveränderten installierten OpenPencil-Pakete gelesen.

Aus dem Repository-Stamm ausführen:

```sh
node examples/autocomplete/reproducibility/run-01/builder-b/generate.mjs
```

Voraussetzung: die bereits installierten Node-Pakete unter tools/openpencil, OpenPencil 0.16.0. Das Skript schreibt ausschließlich in seinen eigenen Ordner. Es liest die Tokens und Geschichten bei jeder Ausführung neu. `preview.png` und `preview.svg` werden aus dem von der Festplatte erneut eingelesenen FIG exportiert. Die FIG-Datei lässt sich mit dem Original-Reader vollständig importieren; ein tatsächliches Öffnen der Desktop-App wurde nicht ausgeführt und daher nicht als geprüft behauptet.

## Tatsächlich ausgeführte Prüfungen

- Original `exportFigFile` schrieb die Datei; Original `parseFigFile` las die gespeicherten Bytes mit populate=all erneut ein.
- Alle zehn Story-Namen sind im erneut eingelesenen Graphen vorhanden.
- 21 einzelne Optionsframes sind erhalten (je sieben für ready, active und scroll-end). Jeder Optionsname verwendet den fachlichen Key.
- Alle Inputs haben 320 × 44 px, ihre Oberkante liegt 28 px unter dem Labelanfang.
- scroll-end besitzt einen geclippten 160-px-Viewport und einen um −64 px versetzten Inhalt. Zürich bleibt als aktive letzte Zeile im sichtbaren Viewport; sämtliche sieben Optionsframes bleiben editierbar.
- Original-Renderer exportierte nach Reimport erfolgreich PNG (83 283 Bytes). Original-SVG-Exporter exportierte ebenfalls.
- Die PNG wurde visuell betrachtet: zehn vollständige Fälle, sichtbarer aktiver Hamburg-Eintrag, deaktiviertes München, aktive letzte Option Zürich, Meldungswiederholungen und roter Fehlerstatus; keine Überlappung der Fälle.
- `checks.json` enthält die automatischen Prüfresultate, Fallkoordinaten und SHA-256-Zuordnungen sämtlicher gelesener Definitionsdateien. Diese Hashliste ist ein Fingerabdruck des verwendeten Standes, kein behaupteter Vorher/Nachher-Vergleich.

## Quellenzuordnung

| Quelle | Übertragung |
|---|---|
| components/README.md, library.json | Definitionsvorrang, editierbares Designziel, kein interaktiver Canvasanspruch |
| autocomplete/README.md, component.json | zehn Fallgruppen; getrennte Label-, Input-, Surface-, Viewport-, Content-, Listbox-, Options- und Statuslayer; Positionsformeln und Zielgrenzen |
| autocomplete/interface.json, stories.json | Eingabetexte, Platzhalter, Query, Wert und Ergebnisrecords; activeKey; enabled; konkrete Fälle |
| tokens.json | Farben in sRGB, Inter, Schriftgrößen, Zeilenhöhe, Breite, Input-/Zeilen-/Viewportmaße, Abstände, Radius, Rahmen |
| autocomplete/layout.css | Inputrahmen in Fokusphasen, Platzhalter-/deaktivierte Farben, aktive Optionsfläche, 6-px-Zeilenpadding, Statusfarbe und -größe |
| overlay/layout.css | gleiche linke Kante/Breite, 8-px-Abstand zum Inputende, weißer Hintergrund, Radius, Schatten 0 2px 8px #0003 |
| scroll-area/layout.css | geclipptes Viewport, ungepaddeter Inhalt und vertikale Liste |
| autocomplete/accessibility.html und accessibility.rules.json | Rollenbenennungen, Meldungstexte und Statusprojektionen; aktive Option ist keine Bestätigung |
| alle drei behavior.scxml und Interface-/Accessibility-Unterkomponentendateien | Trennung von Komponente, Overlay und ScrollArea; Fallphasen; keine zusätzliche Auswahlmaschine |
| autocomplete/error-relay.scxml | gelesen; keine zusätzliche sichtbare Darstellung daraus abgeleitet |

## Lücken, Mehrdeutigkeiten und Grenzen

- Die Definition legt Inter, Größe und Zeilenhöhe fest, aber kein explizites Schriftgewicht. Der Export verwendet den Originalwerkzeug-Standard Regular (400). Dies ist eine technische Standardauflösung, keine zusätzlich behauptete Fachregel.
- Für loading/empty/error verlangt die README eine Meldungszeile, definiert aber keinen eigenen Meldungszeilen-CSS-Selektor. Der Export verwendet die vorhandene Optionszeilengeometrie (32 px, 6/12 px Padding), normale Textfarbe und 14-px-Text. Diese Interpretation ist explizit; ein eigener Meldungstoken fehlt.
- Bei deaktiviertem, leerem Input treffen Platzhalterfarbe und disabled-Textfarbe aufeinander. Der Export setzt die sichtbare Platzhalterschrift auf disabled. Eine ausdrücklich priorisierte disabled-placeholder-Regel fehlt.
- Die README nennt bei scroll-end „die drei unsichtbaren Daten“. Konkrete Geschichten enthalten sieben Ergebnisse, 160/32 ergibt fünf sichtbare Zeilen und damit zwei außerhalb liegende Zeilen. Der Export folgt den expliziten Maßen und hält alle sieben Layer vor.
- Ein platformabhängiger Scrollbarstil ist nicht definiert. Der Export ergänzt keinen gezeichneten Scrollbar. Scroll-Ende wird ausschließlich durch den freigegebenen statischen Inhaltsversatz dargestellt.
- Die Component-Fallgruppen sind editierbare Frames, keine gekoppelte Varianten-/Instanzenbibliothek. Leere Statuslayer bleiben erhalten; verborgene Popups werden entsprechend den Regeln nicht angelegt und belegen keinen Platz.
- Seitentitel, dreispaltige Außenanordnung, Fallüberschriften und Außenabstände nutzen die ausdrücklich freie Seitengestaltung; die Fallkomponenten haben die vorgegebenen Maße.
- ARIA, tatsächliche Requests, Tastaturbedienung, Reveal-Messungen und SCXML-Ausführung werden auf dem Designcanvas nicht ausgeführt. Entsprechende Verhaltenserfüllung wurde nicht getestet oder behauptet. Das Dokument stellt ausschließlich die benannten Zustände dar.
