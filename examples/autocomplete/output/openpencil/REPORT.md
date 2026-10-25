# Cold-Context-Proof: Autocomplete → OpenPencil

## Ergebnis

`autocomplete.fig` ist eine echte binäre FIG-Datei, geschrieben durch den unveränderten OpenPencil-Writer 0.16.0. Sie enthält eine Seite, zehn benannte Fallframes und insgesamt 164 editierbare Nodes. Alle Texte sind TEXT-Nodes, keine Bildflächen. `preview.png` wurde aus dieser gespeicherten Datei mit OpenPencil exportiert und visuell kontrolliert.

## Quellen und Zuordnung

Eingaben ausschließlich aus `components/`; vollständige Dateiliste und konkrete Node-IDs stehen in `verification.json`.

- `README.md`, `library.json`, `autocomplete/README.md`, die drei `component.json`: Zielumfang, Komposition, Layerstruktur und benannte Fälle.
- `autocomplete/interface.json`, `overlay/interface.json`, `scroll-area/interface.json`: Daten, Teile, Eigentümerschaft.
- `tokens.json`, die drei `layout.css`: 320px Breite, 44px Input, 20px Label, 8px Label-/Popup-/Statusabstand, 32px Zeilen, 160px Viewportmaximum, Inter 14px/20px, Status 12px, Farben, Radien, Rand, Schatten.
- `autocomplete/stories.json`: sämtliche Inputs, Ergebnislabels, Keys, aktive Optionen, deaktivierte Option und bestätigter Wert.
- Die drei `accessibility.html` und `autocomplete/accessibility.rules.json`: Rollen als Layernamen, genaue Meldungen, Sichtbarkeit und Statusprojektion.
- Die drei `behavior.scxml` und die referenzierte `autocomplete/error-relay.scxml`: Zustandsbeziehungen und fachliche Abgrenzung; keine Canvasausführung behauptet.

Jeder Fall besitzt `label`, `input`, `overlay.surface`, `overlay.scroll.viewport`, `overlay.scroll.content`, `list` und `status`. Optionen sind eigene Frame-/Textlayer mit fachlichem Key im Namen. Unsichtbare Popupgruppen bleiben vorhanden, belegen aber keinen Raum in der sichtbaren Komponente.

| Fall | Sichtbare Darstellung |
|---|---|
| closed | Platzhalter, Popup verborgen, leerer Status |
| opening | Fokusrand, Popup verborgen, Öffnungsmeldung |
| loading | Query Be, einzeilige Lademeldung im Popup und Status |
| ready | sieben editierbare Ergebnisoptionen, fünf sichtbar, Status mit Anzahl 7 |
| active | ready mit Hamburg hervorgehoben; kein bestätigter Wert |
| scroll-end | alle sieben Optionslayer erhalten, Inhalt um −64px versetzt; Zürich sichtbar und aktiv |
| selected | geschlossen, Berlin im Input und Auswahlmeldung; Ergebnislayer im verborgenen Popup erhalten |
| empty | Query Atlantis, einzeilige Leermeldung im Popup und Status |
| error | Query Be, einzeilige Fehlermeldung, roter Status |
| disabled | geschlossen, Popup verborgen, leerer Status |

## Tatsächliche Prüfungen

1. `node examples/autocomplete/output/openpencil/generate.mjs` erfolgreich: binäre Datei gespeichert, anschließend von OpenPencils IORegistry gelesen und alle Seiten materialisiert. Zehn Fallframes und 28 Optionsframes sind nach dem Reimport vorhanden. Die 28 sind je sieben Optionen in ready, active, scroll-end und selected.
2. CLI-PNG-Export aus der gespeicherten Datei erfolgreich, nicht aus einem allein im Speicher gehaltenen Graphen. Visuell geprüft: Texte vollständig, zehn Fälle getrennt, Hamburg/Zürich aktiv, München deaktiviert, Scroll-Ende korrekt sichtbar, Meldungen unter dem tatsächlich sichtbaren Popup.
3. Struktur und Maße beim erneuten Einlesen in `verify.mjs` geprüft, einschließlich Editieren eines Textnodes und erneutem FIG-Writer-/Reader-Roundtrip im Speicher.
4. Öffnen in der installierten Desktop-App versucht. `open -a OpenPencil` wurde angenommen; CLI `documents open ... --json` scheiterte mit „Could not read MCP discovery file“. Anschließende native Fensterprüfung über CUA scheiterte, weil der Mac gesperrt ist und automatische Entsperrung fehlschlug. Ein tatsächlich sichtbares Öffnen in der Desktop-App ist daher **nicht bestätigt**. Der erfolgreiche Original-Reader-Import und PNG-Export ersetzen diesen noch offenen Desktopnachweis nicht.

## Lücken, Spannungen und offengelegte Adapterentscheidungen

- Die Definition legt für die einzeiligen Popupmeldungen keinen eigenen CSS-Selektor, keinen Innenabstand und keine vertikale Textposition fest. Dieser Export richtet sie ausdrücklich wie Optionszeilen aus (12px links, 6px oben). Das ist eine offengelegte Adapterentscheidung, keine zusätzlich gefundene Regel. Inputtext steht vertikal mittig; Fontgewicht ist CSS `normal` (400).
- `:disabled` setzt die Textfarbe des Inputs auf disabled, `::placeholder` aber ausdrücklich auf muted. Der disabled-Fixture hat nur Platzhalter, keinen Querytext; der Export zeigt deshalb muted. Eine gesonderte disabled-Platzhalterfarbe ist nicht definiert.
- Der README-Satz „die drei unsichtbaren Daten“ stimmt rechnerisch nicht mit den Fixtures und Maßen überein: sieben Zeilen bei fünf sichtbaren ergeben zwei vollständig unsichtbare Zeilen. Der Export folgt den verbindlichen 7 × 32px und 160px und erhält alle sieben.
- Eine plattformspezifische Scrollbar ist weder visuell definiert noch ergänzt. Clipping und statischer Versatz sind vorhanden; dynamisches Scrollen ist nicht Teil des Ziels.
- Komponentenframes und Teile sind editierbar; es wird kein Variantenset, keine interaktive Combobox und kein laufendes ARIA-/SCXML-Verhalten behauptet.
- Freie Außenanordnung: drei Spalten, Falltitel, Seitentitel und Hinweis. Innerhalb der Komponente sind keine neuen Icons oder Bedienelemente ergänzt.

## Reproduktion

Vom Repositoryverzeichnis mit der vorhandenen gepinnten Werkzeugumgebung:

```sh
node examples/autocomplete/output/openpencil/generate.mjs
node examples/autocomplete/output/openpencil/verify.mjs
node tools/openpencil/node_modules/@open-pencil/cli/bin/openpencil.js export examples/autocomplete/output/openpencil/autocomplete.fig -f png -o examples/autocomplete/output/openpencil/preview.png
```

Keine Definition geändert; keine Recherchedateien, Beispiele, frühere Renderings oder Webharnesses als Eingaben gelesen. Alle erzeugten Dateien liegen ausschließlich in diesem Ausgabeordner.
