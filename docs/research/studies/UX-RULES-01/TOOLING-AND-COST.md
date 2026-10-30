# Werkzeuge, Kontext und Integrationsaufwand

Gemessene Rohdaten: [Lauf-01-Werkzeuge](runs/01/tooling.json), [Lauf-03-Runtime](runs/03/results/runtime.json), [gezieltes Laden](runs/03/results/focused-loading.json).

| Ansatz | In dieser Untersuchung tatsächlich nutzbar | Eigene zusätzliche Arbeit / offene Grenze |
| --- | --- | --- |
| DMN/FEEL | XML-Modelle über DMN Scala 1.12.6 ausgeführt; fünf Dateien zusätzlich originalschema-geprüft. | Java-Bridge/Runtime, UX-Faktentypen und Regelstärken, Referenz-/Evidenzprofil. Lokale Test-Runtime hat 15 JARs, zusammen 11.310.451 Bytes, ohne JDK/Maven. |
| Rego | OPA 1.21.2 lokal; geteilte und lokale Regeln ausgewertet. | UX-Vokabular, Ergebnisvertrag und Referenzadapter; eigene Guards brauchten eine erhaltene Reparaturrunde. |
| SHACL | pySHACL 0.30.1 lokal; positive/negative Graphen und Optionen geprüft. | RDF-Projektion und eigene Interpretation des Befunds; kein allgemeiner Ersatz für UX-Entscheidungen belegt. |
| SBVR | Originalschema und importiertes XMI lokal kompiliert. | Noch kein hier nutzbarer semantischer Autoren-/Ausführungsweg ausgewählt. Keine Vollausführung behaupten. |
| ODRL | Begriffs-/Konfliktvergleich und drei native JSON-LD-Kodierungsproben. | UX-Profil und Evaluator wären zusätzliche Aufgaben; keine normative Policy-Ausführung erfolgt. |
| UGL/GDL, ACT/EARL, MBUI | Dokumentarisch eingeordnet. | Unterschiedliche Rollen; heutige Ausführung/Anbindung nicht als erwiesen zählen. |

Lizenzdeklarationen der getesteten Pakete sind im Werkzeugnachweis erfasst; das ist keine juristische Freigabe. DMN Scala deklariert Apache-2.0 in seiner offiziellen Quelle. Alle tatsächlich aufgelösten JARs sind gehasht; eine vollständige transitive Lizenzprüfung steht aus. Vergleichbare Installationszeiten, Wartungsstunden und Laufzeitbenchmarks wurden nicht gemessen.

## Kontextmessung ohne Scheingenauigkeit

Die gezielte Rego-Probe lädt zwei Regeldateien und vier Contractreferenzen in insgesamt **2.058 Bytes**. Das verglichene DMN-Modell hat **971 Bytes**, enthält aber nicht dieselbe separate Bindungsmetadatenmenge. Diese Zahlen sind deshalb keine faire Rangfolge und kein Tokenvergleich. Ein absichtlich ungültiges fremdes Modul bleibt ungeladen; das belegt nur die kontrollierte technische Dateiauswahl.

Vollständiger Agentenrequest, System-/Werkzeugkontext, tatsächliches Verständnis und Auswahlsicherheit sind ungemessen. Dafür wäre später ein eigener Rollenauftrag mit begrenzten Quellen und einer frischen Agentenprobe nötig; hier wurde kein zusätzlicher Agent gestartet. Bibliotheken und installierte Skills unverändert.

## SBVR-Werkzeugrecherche: konkrete Grenze

Die offizielle SBVR-1.5-Seite führt XMI-Schemas/-Modelle; RuleSpeak ist dort ein informativer Anhang. Ein bloßer kontrollierter Text ist damit noch kein geprüfter formaler Modellinhalt. Das Projekt [SBeaVeR](https://sourceforge.net/projects/sbeaver/) beschreibt sich als Eclipse-Modellierungsplugin; auf der Projektseite stehen Pre-Alpha und letzte Aktualisierung 2013-03-22. Dies betrifft dieses Projekt, nicht das gesamte SBVR-Ökosystem. [RuleXpress](https://www.rulexpress.com/) war über den verwendeten Recherchezugang nicht abrufbar; daraus folgt nichts über Verfügbarkeit oder Funktionen des Produkts.

Begrenztes Ergebnis: Derzeit kein hier nachgewiesener lokaler SBVR-Evaluator für dieselben Fälle. Die Prüfung bleibt offen; SBVR wird weder als unmöglich noch aufgrund von Schemaexistenz als vollständige ausführbare Lösung bewertet. Keine alten Eclipse-Pakete, Dienste oder Lizenzkäufe auf Verdacht installiert.
