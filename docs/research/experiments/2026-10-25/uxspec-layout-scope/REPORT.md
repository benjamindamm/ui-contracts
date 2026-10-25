# UXSpec: deklarierte Geometrie gegenüber tatsächlicher Weitergabe

Stand: 25. Oktober 2026. Begrenzter Originalquellenabgleich, keine neue Laufzeitgruppe. **V04 und V06 bleiben U/C420.** Die 41 offenen Zellen und 435 Bedingungen ändern sich nicht.

## Geprüfter Gegenstand

Originalrevision `20dfae0e7224d952e198afdf4ffed26d6fd67180` von johnlindquist/uxspec. [Quelleninventar](source-review.json) mit URLs und Hashes der gelesenen Kopien. Der Abgleich umfasst SPEC, Format Reference, JSON Schema, VisualSpec-Typ, style-map und die tatsächlichen Aufrufer UXRunner → SlotRenderer → ElementRenderer → Container. Keine Aussage über alle zukünftigen Erweiterungen oder alle denkbaren Renderer.

## Festgestellte Grenzen

**V04:** SPEC, Abschnitte Layout Primitives und Element Types, definiert `layer` als Schichtung und ordnet es CSS `position:relative` beziehungsweise ZStack/Box/Stack zu. Der vorhandene Layer-Renderer setzt Kinder absolut mit top/left/right/bottom=0 in diesen Parent. Das belegt gemeinsame Parentgeometrie. Eine definierte Beziehung mit benanntem Zielinput, Richtung und Abstand folgt daraus nicht. SPEC Dynamic Expressions beschreibt berechnete Eigenschaften wie height/opacity; es definiert damit noch keine Referenz auf die gemessene Unterkante eines anderen Elements.

**V06:** VisualSpec und Schema lassen zusätzliche Eigenschaften beziehungsweise ein offenes Containerobjekt zu. Die tatsächlichen Stylemapper bauen jedoch neue Objekte aus ausgewählten Eigenschaften. SlotRenderer reicht ausschließlich mapContainerStyle weiter; die Container kombinieren diesen Mapper mit mapElementStyle. Die gelesenen Aufrufer reichen keine beliebigen Container-/Elementfelder als CSS durch. Ein im JSON akzeptiertes overflow-Feld wäre daher noch kein Nachweis seiner Interpretation. Maximalabmessungen sind bereits separat als V05 erfasst und ersetzen keine Overflowpolitik.

## Präzise fehlender Nachweis

Für V04 fehlt entweder eine Originaldefinition samt Ausführung der Ziel-/Richtungs-/Abstandsbeziehung oder ein ausdrücklich zusätzliches Binding, das diese Beziehung mit benanntem Ziel und Instanz erhält. Für V06 fehlt eine Originaldefinition samt Weitergabe der Überlauf-/Scrollpolitik oder ein ausdrücklich zusätzliches Binding mit genau festgelegter Politik. Offenheit des Schemas und frei benennbare dynamische Eigenschaften entscheiden diese Fragen nicht.

Es wurde kein neuer Adapter erfunden und kein fehlender Rendererzweig durch einen eigenen ersetzt. Eine fehlende Semantik im untersuchten Pfad ist kein Beweis, dass das gesamte Format eine solche Erweiterung verbietet; deshalb keine Umwertung auf N. Die allgemeinen Absichtserklärungen einer vollständigen visuellen Beschreibung werden ebenfalls nicht als Implementierungsnachweis gewertet.

## Fortsetzung

Die nächsten ursprünglichen Layoutfragen betreffen uSpecs Messanker und Clipping-Export. UXSpecs zwei Fragen werden erst durch eine konkrete der oben genannten Bindungen erneut geöffnet, nicht durch dieselben Mapperproben. Dieser Abgleich fügt null Laufzeitbedingungen hinzu; bestehende Gegenfälle und Bewertungen bleiben erhalten. Kein Commit oder Push.
