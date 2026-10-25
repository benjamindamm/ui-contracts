# OpenPencil: vier führende Quellen, Graph ausdrücklich als Ableitung

Stand:25. Oktober2026. **X01 A/C539**, ausschließlich für die konkret ausgeführte Vier-Master→Graph-/Control-/SSR-Kette. Fünf Bedingungen P98 erfüllt.

## Führende Artefakte und originale Ableitung

Interface: ursprüngliches CEM mit Selected:boolean und seinem ausdrücklichen Default. Behavior: ursprüngliche OPS-Spec mit kind und value-Propertybindung. Visual: separate CSS-Regel für Rootbreite/-höhe in px. Accessibility: eigenes HTML mit Rollen und sichtbaren Namen für A/B. Der zusätzliche enge Konverter liest tatsächliche Dateien und erzeugt daraus einen Scenegraph als **abgeleitete Zwischenrepräsentation**; es gibt keine zweite manuell gepflegte führende Graphdatei.

Properties/Defaults stammen aus CEM, ursprüngliches behaviourFromSpec liest die OPS-Bindung auf den generierten tatsächlichen Propertynamen. Rootmaße stammen ausschließlich aus der begrenzten CSS-Projektion, gezeichnete Label-TEXT-Inhalte aus den jeweiligen A11y-HTML-Quellen. Statische A/B-Platzierung des Forschungshosts ist keine weitere Komponentenmasterquelle. Die CSS-Auswertung ist auf die gezeigten flachen positiven px-Dimensionen begrenzt; kein generischer CSS→Figma-Konverter.

Vollständige unveränderte veröffentlichte SceneGraph-/Komponenteninstanziierungs-/OPS-/Projektions-/ControlRoles-APIs0.16.0 laufen. Die bereits benannte unveränderte Original-Vue-Render-/State-Kette wird mittels TypeScript-AST isoliert ausgeführt, mit tatsächlichem Vue und tatsächlichem Reka-SSR. Keine nachgebaute Rolle oder Checkboxstate, keine Stubimplementierungen gelieferter Abhängigkeiten. Unbenutzte andere Renderbranches und gesamte Modulinitialisierung/Editor werden nicht behauptet. Quell- und Deklarationshashes in extraction.json.

## Fünf tatsächliche Bedingungen

[Erwartungen](cases.json), [Originalbeobachtungen](results.json), [Prüfung exakt gerenderter Kontexte/Namen/aria-checked](rendered-source-check.json).

| Fall | Ergebnis |
| --- | --- |
| control | Zwei ursprüngliche Instanzen, Breite100, Namen Choice A/B, tatsächliche ursprüngliche aria-checked=false. |
| visual-revision | Nur Visualbreite100→120; drei übrige Quellen bytegleich, reale Originalprojektion folgt der Breite. |
| accessibility-revision | Nur A-Name geändert; Original-TEXT/SSR-Name folgt, B unverändert, drei andere Quellen bytegleich. |
| interface-default-revision | Nur ursprünglicher CEM-Default false→true; abgeleitete originale Propertydefinition, ursprünglicher Controlstate und tatsächliches Reka-SSR-aria-checked folgen. Drei übrige Quellen bytegleich. |
| behavior-role-conflict | OPS-kind radio wird von der tatsächlichen Originalkette akzeptiert und als radio gerendert. Die eigene getrennte A11yquelle verlangt switch; erst der zusätzliche semantische Vergleich weist diese konkrete Kombination ab. |

CEM-Varianten bestehen das unveränderte Originalschema; Shapeprüfung ist Teil derselben Fälle, keine weitere Zählung. Namen und checked wurden nicht nur aus den Quellwerten übernommen: Exakte gerenderte A/B-Controls, Texte, Kontexte und aria-checked werden aus dem tatsächlichen Original-SSR geprüft.

Gemeinsamer Graph ist damit als Ableitung zulässig, ohne seine Inhalte als unabhängige Masterquellen auszugeben. X01 A ist ein konkretes zusätzliches Binding an existierende Originalsprachen/-APIs, keine native universelle Vierformat-Importfunktion von OpenPencil. Der ältere gemeinsame-Graph-Befund wird präzisiert, nicht als prinzipielle Untrennbarkeit umgedeutet.

Kein vollständiger Editor, native Geometrie-/Interaktions-/AT-Test, beliebige CSS-Syntax oder allgemeine Lifecycle-/Versionsarchitektur. Die schon vorhandenen Switch-/Slider-/Ownerfälle werden nicht erneut gezählt; neu ist die tatsächliche vierfache Herkunft und unabhängige Änderung bis zur Originalableitung. Reproduktion: prepare.py, run.mjs und unveränderte gebundene Originalbestände. Keine Produktionskomponente, Commit oder Push.
