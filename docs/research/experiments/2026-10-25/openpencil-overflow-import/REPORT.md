# OpenPencil: Overflow-Verlust im originalen Feldpfad

Stand: 25. Oktober 2026. **Zwölf Originalanweisungsbedingungen und drei native CSS-Browserbedingungen ausgeführt, alle 15 Erwartungen erfüllt.** OpenPencil V06 bleibt U: Der neue Befund erklärt eine konkrete Verluststelle und ersetzt keinen vollständigen Scrollvertrag.

## Gegenstand und Endbedingung

Bisher bekannt war die Exportregel clipsContent → overflow:hidden. Noch ungeprüft war die Gegenrichtung: Welche unterschiedlichen originalen CSS-Overflowwerte erhält der Dom-CSS-Import tatsächlich in diesem Feld, und hat ihre Zusammenführung eine beobachtbare fachliche Folge?

Endbedingung dieses Pakets: die ursprüngliche Importstelle und ihren Aufruf-/Initialisierungskontext identifizieren, ihre unveränderten Anweisungen mit vorab gespeicherten Gegenfällen ausführen und die relevante hidden/clip-Unterscheidung in einem echten CSS-Host kontrollieren. Diese Endbedingung ist erreicht. Ein vollständiger Import-/Export-Roundtrip und ein bedienbarer OpenPencil-Scrollcontainer waren ausdrücklich andere, hier nicht ausgeführte Gegenstände.

## Originalquellen und Aufrufkontext

OpenPencil-Commit ab2875cc761ee6cff17d389ff1c85fedae50aeab, unverändert gegenüber dem vorigen Layoutbeitrag. Neu gezielt geöffnet: dom-css/src/import/scene-graph.ts, css-values.ts und flow.ts. Der offizielle Repositorybaum wurde nur zur Lokalisierung dieser Dateien verwendet, nicht als Abwesenheitsbeweis. Original-Exportquelle projection.ts stammt bytegleich aus dem vorhandenen Recherchebestand.

createElementNode erstellt im normalen Elementpfad einen FRAME mit clipsContent:false und ruft applyElementStyle mit dem Ergebnis von mergedStyle auf. Die gelesene Funktion schreibt clipsContent bei exakt hidden oder clip auf true. Sie definiert hier keine Achse und keine gesonderte auto-/scroll-Auswahl. mergedStyle übernimmt zuerst inlineStyle und danach computedStyle. Der Export setzt bei true den Wert hidden. Diese Quellzusammenhänge sind E2; daraus wird keine Ausführung aller aufgerufenen Layout-/Bild-/Textfunktionen abgeleitet.

## Tatsächlich ausgeführte Originalfragmente

Der zusätzliche Prüfharnisch isoliert mit dem TypeScript-AST:

- die beiden vollständigen originalen Helfer pickStyle und mergedStyle;
- die ursprüngliche overflow-Zuweisung und direkt folgende clipsContent-Bedingung innerhalb applyElementStyle;
- die ursprüngliche clipsContent-Bedingung innerhalb styleFromSceneNode.

Die Anweisungen werden unverändert transpiliert und nur durch ausdrücklich eigene kleine Aufrufrahmen verbunden. Andere Import-/Exportfunktionen werden weder ausgeführt noch durch Platzhalter als erfolgreich simuliert. **Es handelt sich um einen originalen Feldpfadtest, keinen vollständigen Roundtrip.** extraction.json bindet jede Originalstelle mit Quellhash, Zeile und Fragmenthash.

Der erste Harnischstart scheiterte vor jeder Fallausführung: Der eigene Selektor benutzte condition statt expression für einen TypeScript-IfStatement. harness-repair.json hält Ursache und Korrektur fest. Keine Originalquelle und keine Erwartung geändert; dieser Harnischfehler ist kein Produktfehler und keine zusätzliche Prüfbedingung.

## Zwölf vorab gespeicherte Feldbedingungen

| Eingabe / Kontext | clipsContent danach | Projizierte Overflowangabe dieses Feldpfads |
| --- | --- | --- |
| visible, vorher false | false | keine |
| hidden | true | hidden |
| clip | true | hidden |
| auto | false | keine |
| scroll | false | keine |
| Nur overflow-y:scroll | false | keine |
| Nur overflow-x:hidden | false | keine |
| overflow:hidden scroll als Rohwert | false | keine |
| Inline auto, computed hidden | true | hidden |
| Inline hidden, computed auto | false | keine |
| Keine Overflowangabe | false | keine |
| Bereits true, danach visible im isolierten Setter | true | hidden |

Der letzte Fall zeigt ausschließlich, dass dieser Setter false nicht zurückschreibt. Der normale createElementNode-Pfad startet laut Quelle mit false; daraus wird **kein** behaupteter fehlerhafter In-place-Updatepfad abgeleitet. Achsen- und Zweiwertfälle betreffen die dokumentierten Roh-Styleobjekte dieses Helferpfads; ein vollständiger CSS-Parser oder Browser-Computed-Style-Normalisierer wurde davor nicht ausgeführt. „Keine Angabe“ bedeutet die leere Ausgabe dieses Feldfragments, keine gemessene endgültige Browserpolitik.

## Warum hidden und clip fachlich verschieden sind

CSS Overflow WD vom 07.10.2025, Wertdefinitionen hidden/clip/scroll/auto über BrowserOS gelesen: hidden unterbindet die direkte Scrollbedienung, erlaubt aber programmgesteuertes Scrollen und bildet einen Scrollcontainer. clip verbietet auch programmgesteuertes Scrollen und bildet keinen Scrollcontainer. Die Zusammenführung ist deshalb keine bloße Umbenennung gleichwertiger Werte.

In einem eigenen festen Browserfixture wurden drei Boxen mit jeweils 60 Pixel Inhaltsfenster und 300 Pixel Inhalt gerendert. Der dritte Overflowwert wurde aus dem tatsächlich gespeicherten clip-Projektionsergebnis übernommen. Danach wurde scrollTop auf 80 gesetzt:

| Eigene native CSS-Box | Berechneter Overflowwert | scrollTop nach Zuweisung |
| --- | --- | ---: |
| Ursprünglicher CSS-Wert clip | clip | 0 |
| Kontrollwert hidden | hidden | 80 |
| Aus Feldprobe projizierter clip-Wert | hidden | 80 |

Alle drei vorher gespeicherten Erwartungen erfüllt. BrowserOS/Chromium 155.0.0.0; Browserkennung und tatsächliche Geometrie stehen im Ergebnis. Dies ist ein echter nativer CSS-Hostversuch, **kein** gerenderter OpenPencil-Build. Keine physische Tastatur, Scrollrad-, Touch-, Fokus- oder Assistenztechnikprüfung. Der Versuch beweist die konkrete programmgesteuerte Scrollunterscheidung; er misst nicht sämtliche Unterschiede der Formatting Contexts, Achsen oder Scrollbars.

## Bewertung und verbleibender Nachweis

**OpenPencil V06 bleibt U/C487.** Der benannte Dom-CSS-Feldpfad erhält die ursprüngliche Scrollpolitik nicht verlustfrei. Ein boolesches clipsContent plus hidden-Projektion ist daher kein positiver Nachweis für alle ursprünglichen Overflow-/Scrollregeln. Das widerlegt nicht sämtliche anderen OpenPencil-Renderer, Bibliothekswrapper oder zukünftigen Modellbeiträge.

Offen bleibt eine konkret benannte Originalrepräsentation beziehungsweise ein ausdrücklich zusätzliches Binding, das Achse, Scrollpolitik und Clipping unterscheidet und in seinem wirklichen Import-/Host-/Exportpfad nachgewiesen wird. Ein alleiniger CSS-Sidecar wäre erst nach belegter Zuordnung und Verlust-/Änderungsprüfung ein zusätzlicher Beitrag; er wird hier nicht als fertige Lösung eingeführt. Die vollständige Roundtrip-/Liveprüfung des Originalprogramms bleibt getrennt von den ausgeführten Fragmenten.

Aktuell weiterhin **46 U: 26 Integration und 20 weitere**, jetzt **383 benannte Bedingungen in 48 Gruppen**. Die neue Evidenz senkt keine Zahl künstlich. Schema-, Quellen-, Register- und Aufgabeneinträge sind gemeinsam fortgeschrieben. Keine universelle Produktsprache, Produktionskomponente, Autorenanfrage, neuer Agent, Commit oder Push.

## Reproduktion und Dateien

cases.json und browser-expectations.json wurden jeweils vor dem betreffenden Lauf gespeichert. results.json enthält zwölf Originalfragmentergebnisse; browser-results.json drei tatsächliche Browserbeobachtungen mit Bindung an den Hash des Projektionsergebnisses. host/index.html ist das eigene minimale Forschungsfixture; browser-run.js protokolliert die Browseraktion. Originalquellen sind durch URLs/Hashes und Extraktionsorte dokumentiert und werden nicht als eigene Quellen mitexportiert. run.cjs benötigt die genannten Quellen am dokumentierten Ort sowie den bereits gebundenen TypeScript-Compiler. prepare.py übernimmt lokale Originalcaptures und den bestehenden Exportquellstand. Das Manifest bindet sämtliche verwendeten Original-/Werkzeug-/Ergebnisdateien.
