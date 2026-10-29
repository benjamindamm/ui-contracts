# Definitionsbibliothek

Diese Bibliothek wird über Definitionen gepflegt. Die Dateien in autocomplete/, overlay/ und scroll-area/ sind die führenden Quellen. Erzeugte Zielartefakte gehören nicht hierher und werden nicht unabhängig nachbearbeitet.

## Erster Baustein

[Autocomplete](autocomplete/README.md) verwendet die separat beschriebenen Komponenten Overlay und ScrollArea. [library.json](library.json) ist der Index. component.json verbindet Originaldateien und konkrete Teile; diese kleine Bindungssyntax ist ein Arbeitsentwurf, kein bereits standardisiertes Produktformat.

| Domäne | Quelle |
| --- | --- |
| Interface | CEM-JSON: Properties, Typen, Events, Teile. |
| Visual | DTCG-Tokens und CSS-Regeln. CSS beschreibt hier Geometrie und visuelle Zustandsabbildungen; ein Canvasadapter muss diese explizit übertragen. |
| Behavior | SCXML: Zustände, Aktionen und Übergänge. Die vorhandenen Guards/Ausdrücke verwenden ECMAScript. |
| Accessibility | HTML-Semantik plus ergänzende, ausdrücklich eigene Projektions-/Meldungsregeln. Das ergänzende JSON ist kein WAI-ARIA-Originalschema. |

Die Dateien beschreiben die Komponente; es gibt keine daneben gepflegte handgeschriebene TypeScript-Komponentenimplementierung. SCXML-Ausdrücke sind dennoch ausführbare Ausdrücke und keine Behauptung einer vollständig ausdrucksfreien Sprache. Wiederverwendbare technische Adapter und Compiler gehören nach tools/, Beispiele und erzeugte Dokumente nach examples/.

## Unabhängiger erster Proof

Ein neuer Agent erhält nur dieses Verzeichnis und normale OpenPencil-Dokumentation beziehungsweise die Originalwerkzeuge. Er soll daraus ohne Gesprächsverlauf, Rechercheordner, Webharness oder fertige Bilder ein editierbares OpenPencil-Dokument erzeugen. Der Agent darf Definitionen nicht ändern. Fehlende oder widersprüchliche Angaben werden protokolliert und nicht still ergänzt.

Ziel dieses Schritts ist ein editierbares Design mit allen benannten Zuständen. Interaktive Combobox-Preview in OpenPencil und das spätere HTML-/TypeScript-Ziel sind separate Prüfumfänge. Die nachfolgende Prüfung vergleicht das Ergebnis mit diesen unveränderten Quellen, nicht mit einer nachträglich auf das Design zugeschnittenen Definition.
