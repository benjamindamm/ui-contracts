# Autocomplete · Builder A

## Ergebnis

`autocomplete.fig` ist eine echte binäre, mit dem Original-Writer `exportFigFile` aus @open-pencil/core 0.16.0 geschriebene OpenPencil/Figma-Datei. Der Original-Reader `parseFigFile` hat genau diese gespeicherte Datei mit `populate: all` wieder eingelesen. `preview.png` wurde aus diesem wieder eingelesenen Graphen durch den Original-CanvasKit-Exporter erzeugt und visuell geprüft. Keine eingebettete Rasterkopie der Komponente: 127 Knoten, darunter editierbare Texte, Frames und einzelne Ergebniszeilen. Die zehn Fälle sind getrennt benannte Frames.

Ausführen, vom Projektverzeichnis:

```sh
node examples/autocomplete/reproducibility/run-01/builder-a/generate.mjs
```

Die gepinnte installierte Werkzeugumgebung unter `tools/openpencil/node_modules` wird verwendet. Der Generierungsschritt liest die führenden Tokens, Stories und Meldungsregeln direkt. Geometrie und Zustandsübertragung entsprechen dem expliziten Adapter im Skript. Er überschreibt ausschließlich seine eigenen Ausgaben in diesem Ordner. Kein Browser, keine Fremdergebnisse, keine Recherchedateien, keine Änderungen an Definitionen und kein Commit.

## Tatsächliche Prüfung

- Original-Writer erzeugte 31.310 Byte; Original-Reader las die gespeicherten Bytes vollständig wieder ein.
- Alle zehn Fallnamen vorhanden; Input jeweils 320 × 44 px, y=28.
- Popuppräsenz gegen die Projektionen geprüft, insbesondere opening und disabled ohne Popup.
- Sichtbares Popup hat dieselbe linke Kante wie der Input, Oberkante bei Inputende + 8 px.
- Statusposition und exakter Meldungstext in jedem Fall gegen die berechnete Erwartung geprüft.
- Geclippter Viewport und sieben erhaltene Optionsframes in ready, active und scroll-end geprüft.
- scroll-end: Listbox bei y=-64 px; letzte aktive Zeile endet genau am Viewportende 160 px. Alle sieben Datenlayer bleiben erhalten. Die Definition enthält sieben Zeilen und fünf sichtbare Zeilen; daraus folgen zwei vollständig unsichtbare Zeilen, obwohl README an einer Stelle „drei unsichtbaren Daten“ sagt. Die explizite Anzahl, Höhe und 160-px-Grenze wurden angewendet.
- Anzahl editierbarer Textknoten bleibt beim Schreiben/Lesen gleich.
- Visuelle Prüfung der exportierten PNG: zehn Fälle, korrekte Texte, sichtbares Zürich, aktive Fläche, deaktiviertes München und rote Fehlermeldung; kein abgeschnittener Meldungstext.

Einzelwerte und Prüfergebnisse stehen in `checks.json`. Keine Behauptung einer durchgeführten macOS-GUI-Öffnung: die Öffnungs-/Reimportprüfung erfolgte über den Original-Reader und den Original-Renderer. Kein interaktives Verhalten oder tatsächliche ARIA-Ausführung wird behauptet.

## Quellenzuordnung

| Ergebnis | Führende Quelle in components/ |
| --- | --- |
| Umfang, editierbarer Zieltyp, zehn benannte Fälle, Platzierung und scroll-end | README.md, library.json, autocomplete/README.md, autocomplete/component.json |
| Fallinputs, Ergebnisreihenfolge, aktive Keys, bestätigter Wert | autocomplete/stories.json |
| 320 px Breite, 44 px Input, 32 px Zeilen, 160 px Viewport, Inter 14/12, Zeilenhöhe 20, Farben und Abstände | tokens.json |
| Label-/Input-/Options-/Statusgeometrie, Fokus-, Aktiv- und Disabledfarben | autocomplete/layout.css |
| Popupanker, Radius und Schatten 0 2px 8px #0003 | overlay/layout.css |
| Clipping, Inhalts- und Listboxstruktur | scroll-area/layout.css |
| Meldungen, Popuppräsenz, aktive Auswahlprojektion | autocomplete/accessibility.rules.json |
| Interface, Anatomie, Rollen und Zielgrenzen | autocomplete/interface.json, autocomplete/accessibility.html; overlay/{component.json,interface.json,accessibility.html}; scroll-area/{component.json,interface.json,accessibility.html} |
| Phasen, bestätigter Wert vs. Navigation, Unterkomponenten | autocomplete/behavior.scxml, autocomplete/error-relay.scxml, overlay/behavior.scxml, scroll-area/behavior.scxml |

Alle genannten Definitionen wurden gelesen. Verhalten wird als statische Fallauswahl wiedergegeben, nicht in OpenPencil ausgeführt. Ergebniszeilen heißen nach stabilen fachlichen Keys; Reihenindizes dienen nur der Geometrie.

## Fehlende oder mehrdeutige Angaben / Adaptergrenzen

- Popupmeldungen haben laut README genau eine Zeile, aber keine eigene explizite CSS-Paddingregel. Der Adapter verwendet hierfür 12 px horizontal und 6 px vertikal wie bei Optionszeilen. Das ist eine offengelegte Layoutannahme und kein vollständig quelleneindeutig bestimmter Wert.
- Die leere deaktivierte Eingabe trifft sowohl `::placeholder` (muted) als auch `:disabled` (disabled). Der Adapter verwendet für den deaktivierten Platzhalter disabled. Die Definition legt die Priorität dieser kombinierten Darstellung nicht ausdrücklich fest.
- Schriftgewicht ist nicht explizit tokenisiert. Es wird CSS-normal als 400 abgebildet. Inputtext wird in der 44-px-Fläche mit der 20-px-Zeile zentriert; die native Inputbaseline ist nicht spezifiziert.
- CSS-Schattendaten werden auf OpenPencil DROP_SHADOW mit Radius 8 übertragen. CSS-Blur und Skia-Schatten können rastertechnisch differieren.
- Die Scrollbar hat keine definierte Geometrie oder Farbe; es wurde keine frei gestaltete Scrollbar hinzugefügt. Clipping und statischer Scrollversatz werden dargestellt.
- Separate Overlay-content- und ScrollArea-content-Wrapper sind in den HTML-Vorlagen enthalten, haben hier jedoch keine zusätzliche sichtbare Geometrie. Listbox liegt direkt im benannten Scrollviewport. Die fachlich explizit verlangten editierbaren Teile Input, Overlayfläche, Viewport, Listbox, Optionen und Status sind vorhanden.
- Die freie Außenanordnung verwendet drei Spalten mit Fallüberschriften und einen Seitentitel. Sie gehört nicht zur Komponentenabmessung.
- layerbasierte statische Semantik wird über verständliche Namen transportiert; keine ausführbare Combobox, Tastatursteuerung oder Screenreader-Anbindung.
