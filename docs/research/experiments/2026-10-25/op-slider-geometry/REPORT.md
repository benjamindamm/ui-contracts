# OpenPencil: ursprünglicher Slider-Partpfad und referenzierte Geometrie

25. Oktober2026. **V04 R/C525**, nur für die konkret referenzierte Slider-Root-/Thumb-Geometrie. Der frühere unerfüllte Popup→Input-Unterkantenfall C499 bleibt erhalten und wird hierdurch nicht repariert.

## Ursprüngliche Referenzkette

Unveränderte veröffentlichte SceneGraph-/dom-css-Pakete0.16.0 erzeugen echte Komponenten, drei echte ursprüngliche SLOT-Properties track/range/thumb, ursprünglichen behaviourFromSpec mit numerischem Bereich0..100 und zwei unterschiedlichen Defaults25/75. Tatsächliche Instanziierung, behaviourControls, controlRoles und fehlende Bindungen werden gelesen. Die tatsächliche ursprüngliche layerComponents(...,'vue')-Ausgabe importiert SliderRoot/SliderTrack/SliderRange/SliderThumb aus reka-ui. Originale Exportregeln geben gezeichnete left/right/transform-Werte der bewegten Teile frei; das ist ein ausdrücklicher Delegationspfad, keine selbst erfundene Placementfunktion.

Die referenzierte tatsächliche Reka-Version2.10.5 definiert Prozentposition aus value/min/max, horizontale startEdge, Thumbgröße und contain-Offset. Der tatsächlich positionierte Bezugscontainer ist hier die SliderRoot, nicht eine beliebige gezeichnete Trackbox oder ein fremder Input. Die Originalausgabe hat Track/Range/Thumb als Geschwister im positionierten Root. Der Ursprung/Targetcontainer, Richtung/Startkante und Größenoffset sind damit formal definiert. Keine universelle Popup-/Overlayankerung aus dem Slider abgeleitet.

## Zwei ursprüngliche SSR-Versuche, Erwartung nicht erfüllt

[cases.json](cases.json) erwartete eine sofortige Thumbposition25/75%. Originalgraph und Generator lösen alle drei Parts auf, missingBindings leer. Tatsächliches isoliertes Reka-SSR zeigt aber noch keinen registrierten Thumbindex: Thumbwert fehlt, display:none und korrekte Thumbkante calc(0% + 0px). Range berücksichtigt den Wert bereits. [Ergebnisse](results.json). Beide ursprünglichen positiven Thumb-Erwartungen bleiben **widerlegt**; das ist kein positiver Konformitätspass.

initial-selector-results.json/initial-run.mjs bewahren davor den eigenen Beobachtungsfehler: Der erste Regex las die Range-Kante0% statt des role=slider-Thumbs. Nach Korrektur blieb der entscheidende ursprüngliche SSR-Befund bestehen. Der Selektorfehler und die ursprüngliche SSR-Grenze werden nicht vermischt.

## Drei getrennte native Bedingungen

Die tatsächlich vom Original erzeugten Vue-SFCs werden mit dem tatsächlichen Vue-Compiler und unverändertem Reka gebündelt und in einem eigenen Browserhost gemountet. Keine nachgebaute Thumbformel und keine veränderte Originalfunktion. [Vorab native Erwartungen](native-cases.json), [native Ergebnisse](native-results.json).

| Fall | Tatsächlicher Bezug |
| --- | --- |
| Wert25, Root200, Thumb16 | center54, ursprüngliches left calc(25% + 4px). |
| Wert75, Root200, Thumb16 | center146, ursprüngliches left calc(75% - 4px). |
| Wert25, Root300, Thumb16 | center79 bei unveränderter Prozent-/Offsetformel. |

Dritter Host: ausdrücklich eigene **nachgelagerte CSS-Revision** des generierten Rootwidth200→300. Der gezeichnete Track bleibt200. Das zeigt gerade, dass die referenzierte Layoutsemantik den Root als Bezugscontainer verwendet, nicht pauschal den Track. Keine neue Original-Scenegraph-Exportrevision für diese dritte CSS-Änderung behauptet. Native Messung beginnt nach Mount/Frames; keine physische Sliderbedienung, Tastatur oder AT.

V04 R ist durch den ausdrücklichen ursprünglichen Referenzpfad und die tatsächliche referenzierte geometrische Semantik begründet. Die eigene SFC-Kompilation/Hostprüfung ist zusätzlicher Nachweis, keine eigene neue Vertragsregel. Keine Behauptung zu UIKit/Swift/Android, allgemeiner Inputankergeometrie oder vollständigem Editor. X01 bleibt separat offen.

Reproduktion: run.mjs erzeugt zwei Originalgraph-/Generator-/isolierte Referenz-SSR-Beobachtungen; sein Exitstatus1 ist wegen der erhaltenen SSR-Erwartungswiderlegung beabsichtigt. prepare-native.cjs kompiliert die tatsächlich erzeugten SFC-Dateien und schreibt drei Hosts, dann lokale HTTP-Auslieferung und native-browser-capture.json lesen. Originalpakete/Browserbundles werden nicht als eigene Implementierung verteilt; Manifeste binden Quellen, Compiler, Lockdatei und Buildhashes.
