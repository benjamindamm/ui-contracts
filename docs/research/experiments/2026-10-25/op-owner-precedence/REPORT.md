# OpenPencil: ursprüngliche Quellführung und tatsächliche Ableitung

25. Oktober 2026. **X08 A/C515**, begrenzt auf Behavior-Art und Boolean-Definitions-/Instanzwert der ausgeführten Originalkette. Acht vorher festgelegte Bedingungen erfüllt. Keine vollständige Vier-Domänen-Integration.

## Original und Zusatz

Vollständige unveränderte veröffentlichte Pakete @open-pencil/scene-graph und @open-pencil/dom-css, jeweils0.16.0, aus dem bereits eingefrorenen Werkzeugbestand ausgeführt. Der eigene Versuch erzeugt Graphdaten und echte ursprüngliche Instanzen. behaviourOwner, readBehaviour, behaviourProperties und der tatsächliche Consumer behaviourControls bestimmen Eigentümer und Ableitung. Keine nachgebaute Ownerfunktion und kein gemockter Consumer.

Zusätzlich speichert der Versuch vorher/nachher einen ausdrücklich begrenzten Graphmetadatenausschnitt und die tatsächlich abgeleiteten ControlModel-Werte samt Hashes. Dieses Journal ist eigene Forschungsbindung, keine native signierte Provenienz, vollständige .fig-Persistenz oder Bibliotheksrevision. Die strukturellen Vorrangregeln kommen aus dem Original; das Änderungsjournal ist Zusatzcode.

## Acht Bedingungen

| Bedingung | Beobachtung |
| --- | --- |
| Einzelkomponente | COMPONENT führt, switch wird abgeleitet. |
| Variante im Set | COMPONENT_SET führt; switch am Set gewinnt gegenüber gespeichertem radio am Kind. |
| Änderung am nicht führenden Kind | Kind wird button; tatsächlicher Consumer bleibt switch. |
| Änderung der führenden Quelle | Set switch→radio; Consumer folgt, Instanz-ID bleibt erhalten. |
| Fehlender Behavior am Set | Keine Controls, obwohl das Kind weiterhin radio speichert. Kein automatischer Fallback auf das Kind. |
| Gleiche Property-ID | Definition des Sets gewinnt: Default false statt true am Kind. Nur doppelte IDs werden so priorisiert; eindeutige Kind-Properties sind damit nicht ausgeschlossen. |
| Explizite Instanzzuweisung | false an der Instanz gewinnt gegenüber true als Definitiondefault. Das ist eine eigene Autoritätsebene, kein widersprechender Definitionsowner. |
| Frame | Gespeicherter Behavior macht einen FRAME nicht zum Behaviorowner; keine Controls. |

[Vorab-Erwartungen](cases.json), [vollständige Ergebnisse und Änderungsjournal](results.json), [ausführbarer eigener Versuch](run.mjs).

## Bewertung und Grenzen

X08 A/C515 für diese konkrete Information: ursprüngliche strukturelle Führung, ursprüngliche Vorrangregeln und tatsächlich beobachtete Ableitung, ergänzt um explizite Quelle/Ableitung- und Änderungsbindung. Keine erfundene allgemeine Governance, Bearbeitungsberechtigung, Konfliktwarnung oder automatische Fehlerbehebung. Insbesondere akzeptiert der Graph widersprechende gespeicherte Angaben; die ursprüngliche Projektion entscheidet anhand ihrer Regeln, statt jede Abweichung abzulehnen.

Keine Editoroberfläche, SSR-, DOM-, Tastatur-, AT-, Exportpersistenz-, Plattform- oder allgemeine Fremddomänenprüfung. X01 bleibt offen. Der konkrete Behaviorbeitrag kann Accessibilityfolgen haben, daraus entsteht keine gemeinsame Zuständigkeit über alle vier getrennten Domänen.

## Reproduktion

prepare.py speichert die acht Erwartungen vor der Ausführung; node run.mjs nutzt die unveränderten Geschwisterpakete unter ../op-projection-origin/tool/node_modules. Die Originalabhängigkeiten werden nicht mit dem Dokumentationspaket verteilt. Exakte Lockdatei und die relevanten Originaldateihashes stehen im Manifest; vollständiger ursprünglicher Werkzeugbestand ist bereits im vorherigen Projektionsnachweis eingefroren. Keine neue Produktionskomponente, kein Commit/Push.
