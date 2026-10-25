# OpenPencil: Flächenbegrenzung, Positionierung und Clipping

Stand 24. Oktober 2026. Zusätzlicher Originalumfang gegenüber dem ursprünglichen Behaviour-Beitrag: SceneNode, Layoutfelder und dom-css-Projektion der Revision ab2875cc761ee6cff17d389ff1c85fedae50aeab. E2-Quellprüfung, kein neuer Laufzeitversuch.

## V05: bestehender Adapterbeitrag belegt

SceneNode definiert minWidth/maxWidth/minHeight/maxHeight als number|null. fields/layout.ts zählt sie ausdrücklich zu den erhaltenen Größenbegrenzungen und den layoutrelevanten Feldern. In dom-css/export/projection.ts schreibt addSizeConstraints jeden nicht-null-Wert über px() beziehungsweise die vorhandene Tokenreferenz nach min-width/max-width/min-height/max-height. styleFromSceneNode ruft diese Funktion tatsächlich auf. sceneNodeToDesignNode liefert die Styles als inlineStyle; der separat gelesene HTML-Serializer gibt inlineStyle aus.

Damit ist eine konkrete geometrische Begrenzung mit vorhandenem CSS-Adapter belegt: V05 wird wie beim bereits geprüften UXSpec-Webadapter als A eingeordnet. Kein generisches neues Maximalflächenformat erfunden. Eine maximale Zahl sichtbarer Zeilen, variable Zeilenhöhen, tatsächlich gemessene Boxen, Tokenauflösung in diesem Pfad und native Renderer sind nicht mitgeprüft. null bedeutet in der gelesenen Ausgabe, dass keine entsprechende Größenregel geschrieben wird; negative Werte werden in dieser Funktion nicht als eigener Fall abgefangen. Keine Behauptung, dass alle vorgelagerten Schreiber negative Größen erlauben.

## V04 bleibt U

addPositioning entscheidet anhand Layoutpositionierung und Elternlayout. Es schreibt absolute linke/obere Koordinaten aus node.x/node.y oder stellt einen relativen Elterncontainer her. Das ist konkrete Positionierung, aber noch keine definierte dynamische Overlay-zu-Input-Beziehung mit eigenem Ankerziel, Richtung und Abstand. Elternkoordinaten werden nicht als nachgewiesener externer Ankervertrag umgedeutet. Andere Editor-/Prototypingpfade sind damit nicht widerlegt.

## V06 bleibt U

styleFromSceneNode schreibt bei clipsContent overflow:hidden. Das ist ein belegter begrenzter Clippingbeitrag; er erfüllt nicht allein die untersuchte Scrollcontainersemantik mit überlaufenden Optionen. Im vollständig gelesenen Projektionsmodul ist keine auto/scroll- oder achsenspezifische Auswahl für diesen Feldpfad vorhanden. Eine Preview-Wheelweiterleitung und CSS-Ausgabemöglichkeiten eines anderen Moduls wären gesonderte Gegenstände.

## Quellen und Grenzen

Alle fünf vollständigen Originaldateien und ihre gepinnten URLs/UTF-8-Hashes sind im source-manifest.json erfasst. Originaldateien werden nicht mitverteilt. Kein Originalcode verändert oder mit Ersatzfunktionen ausgeführt. Kein Browserrendering, kein Layoutmessversuch, kein Export-Roundtrip, kein Assistenztest. Die Ausgabe übernimmt weiterhin die vorhandene Web-/Szenenbaum-Bindung; keine Vier-Domänen-Integration bewiesen.
