# OpenPencil: separater Visualbeitrag und Grenzen der Bedingungsanalyse

Stand: 24. Oktober 2026. Ergänzung des Untersuchungsumfangs: Die bisherigen OpenPencil-Zellen bezogen sich auf Behaviour. Hier werden ausdrücklich zusätzlich Scenegraph-Variablen und der originale dom-css-Tokenexport derselben gepinnten Revision untersucht. Kein Nachweis einer Vier-Domänen-Integration.

## Dokumentarisch belegt (E2)

Die Originaltypen unterscheiden COLOR, FLOAT, STRING und BOOLEAN, typisierte Literalwerte, Aliase und Ausdrücke. Variablen besitzen eine Collection und Werte je Modus. Zahlen führen zusätzlich Einheiten; rem wird bei der CSS-Ausgabe aus gespeicherten Canvaspixeln mit der definierten Basis 16 umgerechnet. Die Ausgabe unterscheidet Farbe, Zahl, String und Alias. Das belegt einen eigenen Beitrag zu V01; keine vollständige typisierte Composite-Typografie und keine automatische DTCG-Konformität.

Die Auflösung besitzt aktive sowie Standardmodi und berücksichtigt Moduswahl am Knoten beziehungsweise seinen Vorfahren. Der Stylesheetexport schreibt Standardwerte und abweichende Moduswerte, mit voreingestellten Datenattributselektoren oder konfigurierten CSS-Bedingungen. Damit ist Modusauswahl samt Abbildung zu CSS belegt (V03). Keine Behauptung eines ausgeführten vollständigen Export-/Browserpfads oder nativer Plattformunterstützung.

Die Valibot-Variablenschemata verwenden ausdrücklich looseObject, Werte je Modus als unknown und Modi als unknown-Array. Typdefinitionen und gezielte Laufzeitprüfungen sind deshalb keine vollständige Originalschema-Validierung aller Visualwerte. Auch die Stylesheetvalidierung trennt Form-/Injektionsprüfung und CSS-Semantik.

## Ausgeführt (E3): zehn explorative Bedingungen

Unverändertes originales conditions.ts mit TypeScript 5.9.3 nach CommonJS/ES2022 übersetzt und mit Node 24.22.1 sowie css-tree 3.2.1 ausgeführt. Das Originalpaket verlangt css-tree ^3.2.1; sein TypeScript-Entwicklungsstand ist ~5.8.3. Kein vollständiger Projekt-Typecheck. Die Ergebnisse sind Beobachtungen, keine nachträglich als vorregistriert ausgegebenen Erwartungen.

Dark-Mode-Mediafeature, Schreibweisen/Kommentare und ein einzelnes Containerfeature werden erkannt. Selektoren, screen-Modifier, zusammengesetzte Bedingungen, @supports und Range-Syntax liefert dieser spezielle Helfer nicht als Einzel-Feature zurück. Das beweist nicht, dass der gesamte Export solche Bedingungen nicht verarbeiten kann: dieser verwendet weitere Validierungspfade.

Auch prefers-color-scheme:banana und min-width:640bananas werden als Featureform erkannt. Der Helfer ist folglich kein semantischer CSS-Validator. Ergebnisse stehen vollständig in results.json. Keine UI gerendert, kein Assistenztest, keine Komponente implementiert.

## Reproduktion und Abgrenzung

Originaldateien anhand source-manifest.json exakt beschaffen und UTF-8-Hashes vergleichen; sie werden nicht als eigene Quellen weiterverteilt. Der Runner erwartet sources/ relativ zu seinem Ordner und die separat gebundenen TypeScript-/css-tree-Abhängigkeiten aus den vorangegangenen Experimenten. run.cjs zeigt den tatsächlichen Workspacepfad dieser Ausführung; für einen anderen Ablageort müssen nur diese lokalen Abhängigkeitspfade angepasst werden. V04/V05/V06 und gemeinsame Paketbindungen werden hierdurch nicht geschlossen.
