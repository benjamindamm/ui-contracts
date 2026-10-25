# Google DESIGN.md: eigener Visualbeitrag neben drei Originalsprachen

25. Oktober2026. **X01 A/C523**, getrennt von der weiterhin offenen Dokument-Schemafrage X06/C483. Zwei vorab definierte Bedingungen erfüllt.

Tatsächliches originales @google/design.md0.4.0 lint verarbeitet die eigene DESIGN.md mit allein name/version/colors.primary; keine Interface-, Behavior- oder Accessibilitydefinition erzwungen. Tatsächlich ausgegebene typisierte Color enthält hex/RGB/Luminanz. Der zusätzliche begrenzte Binder verwendet ausdrücklich hex als CSS-Foregroundfarbe an den beiden externen HTML-listbox-IDs. Die CEM- und SCXML-Dateien führen weiterhin Anatomie/Signaturen beziehungsweise Zustände/Emissionen; HTML führt Namen/Rollen/Beziehungen. Keine fremde Definition wird in DESIGN.md eingebettet.

Visualrevision #112233→#445566 erreicht den tatsächlichen ursprünglichen Coloroutput und die zusätzliche CSS-Ableitung; CEM/SCXML/HTML bleiben bytegleich. [Erwartungen](cases.json), [Resultate einschließlich Originalwarnungen und Herkunftshashes](results.json). Originalerrors jeweils0; Warnungen sind weiterhin sichtbar, nicht als vollständige Linterkonformität unterdrückt. Keine native CSS-/A11y-/Interaktionsprüfung aus diesem Datenversuch abgeleitet.

initial-color-shape-results.json und initial-run.mjs bewahren den eigenen ersten Fehler: Der Binder erwartete value statt des tatsächlich vorhandenen hex-Feldes. Das Original hatte beide Farben korrekt geliefert; die eigene Ableitung wurde korrigiert. Zwei ursprüngliche Erwartungen waren an diesem Harnessfehler gescheitert, keine neue Originalfähigkeit und keine Verdoppelung der Bedingungen.

A bedeutet dieses konkrete zusätzliche semantische Binding. Es entscheidet weder das Original-Dokumentprüfungsschema noch allumfassende Produkt-/Theme-/Validierungseignung. X06 bleibt U. Reproduktion: prepare.py und run.mjs mit unverändertem gebundenem Originalpaket. Kein Commit/Push.
