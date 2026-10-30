# Erster Vergleich · 30. Oktober 2026

**Dokumentenprüfung, keine ausgeführten Frameworktests.** Quellen-IDs führen nach [sources.json](sources.json). Keine Aussage, dass eine universelle UX-Regelsprache existiert oder ausgeschlossen wurde. Die Zeile „Integrationsfrage“ ist jeweils unsere Forschungsfrage, kein Frameworkversprechen.

| Kandidat | Dokumentierter Beitrag / Originalformat | Einordnung für unseren Zweck (Hypothese) | Integrationsfrage / noch zu prüfen |
| --- | --- | --- | --- |
| DMN 1.5 / FEEL | Entscheidungsmodell; OMG veröffentlicht normative XML-Schemas und XMI (S01, S07). | Kandidat für auswertbare Eignungsentscheidungen. | Kontexttypen, Regelverbindlichkeit, unbekannte Werte, Tabellenüberlappung, externe Contractanker und Enginekonformität praktisch testen. |
| SBVR 1.5 | Fachvokabular und Regeln; normative XMI-bezogene XML-Schema-/Modellartefakte (S02, S08). | Kandidat für präzise Begriffe; nicht allein mit einem natürlichsprachlichen Template gleichsetzen. | Export-/Autorenweg, Evaluatorverfügbarkeit, Empfehlungen und komponentengenaue Bindung erproben. Ein XMI-Schema beweist keine vollständige Entscheidungsengine. |
| SHACL 2017 | RDF-Graphbedingungen und Validierungsberichte; Info/Warning/Violation sind Ergebnis-Severities (S03). | Kandidat für Constraints und Beziehungen in einer projizierten Komponenten-/Kontextbeschreibung. | RDF-Projektion unserer Originaldateien, fehlende Fakten und Konflikte getrennt testen. Warning bedeutet nicht automatisch „UX-Empfehlung erfüllt“. |
| OPA / Rego | Deklarative Policyauswertung strukturierter Daten wie JSON; eigene Regosyntax (S04). | Kandidat für direkt ausführbare Prüfregeln über bereitgestellte Contract-/Kontextdaten. | UX-Begriffe, Verbindlichkeit und Referenzprüfung wären zu modellieren. undefined nicht ungeprüft als fachlich negativ auslegen. Toolversion noch ungepinnt. |
| ODRL 2.2 | Modell für Nutzung von Inhalten/Diensten mit Permission, Prohibition, Duty, Constraints und Konfliktstrategien; u. a. JSON-LD-Beispiele (S05). | Gezielter Gegenvergleich für normative Regeln, nicht voreilig als UX-Sprache übernehmen. | Nutzungserlaubnis passt nicht automatisch zu gestalterischer Eignung oder Empfehlung. Profilbedarf und Evaluatorverhalten offen. |
| MBUI / CTT-Taskmodelle | UML-Metamodell und XML-Schema für Ziele/Aktivitäten und zeitliche Beziehungen; W3C Working Group Note (S06). | Relevanter Kontext für spätere Use-Case-Komposition; kein belegter Ersatz für die gesuchten komponentenbezogenen UX-Regeln. | Wartung/Tools und direkte Regelabdeckung offen; vollständige Taskmodellierung derzeit außerhalb der Abnahme. |

## Konkrete erste Befunde

**B01 · Maschinenlesbares Format ist nicht gleich Regelsemantik.** DMN und SBVR führen echte Modellartefakte auf ihren offiziellen Spezifikationsseiten. Die Existenz eines XSD sagt jedoch nichts über die hier noch ungeprüfte semantische Ausführung und UX-Eignung. Diese beiden Behauptungen werden getrennt geprüft (S01, S02).

**B02 · Warnung ist keine fachliche Empfehlungslogik.** SHACL definiert Severities; laut Spezifikation beeinflussen deren konkrete Werte die Validierung nicht. Ein Projekt, das Warning pauschal in „empfohlen“ umdeutet, fügt eigene Policy hinzu (S03, Abschnitt 2.1.4). Für uns muss Verbindlichkeit zusätzlich sauber erklärt werden.

**B03 · Fehlende Fakten brauchen einen eigenen Test.** Rego kann für fehlende Werte undefined liefern (S04). Unsere geforderte fachliche Einordnung „noch unbestimmt“ entsteht nicht automatisch durch ein Default-False. Welche Ergebnisse andere Kandidaten liefern, wird erst in den gemeinsamen Fällen geprüft.

**B04 · Konfliktmodelle sind domänenspezifisch.** ODRL hat die Strategien perm, prohibit und invalid, standardmäßig invalid bei nicht gesetzter Strategie (S05, Abschnitt 2.10). Daraus folgt nicht automatisch eine geeignete Rangfolge unserer Pflichten und Empfehlungen. Keine Übernahme ohne UX-Profilprüfung.

**B05 · Es fehlt bisher der praktische Verbindungsnachweis.** Keiner der hier ausgeführten Schritte hat eine referenzgebundene UX-Regel über unsere konkrete Library ausgewertet. Text-/IRI-Felder im Modell wären nur Anknüpfungspunkte. Der eigentliche Nachweis erfordert die Bindungsfälle in BINDING.md und cases.json. Das ist eine Aussage über unseren Prüfstand, kein Negativbeweis über alle Frameworks.

## Arbeitsreihenfolge, keine Auswahlentscheidung

DMN, SBVR, SHACL und Rego zunächst vertiefen. Sie untersuchen unterschiedliche Funktionen; weder „DMN gewinnt“ noch „wir benötigen alle vier“ ist beschlossen. ODRL anhand der normativen Grenzfälle mitführen. MBUI vorerst für Kontext-/Taskbegriffe berücksichtigen. Zusätzliche UX-spezifische Kandidaten vor einer abschließenden Auswahl gezielt suchen.

Der wichtigste Vergleich ist nicht Anzahl verfügbarer Features, sondern wie wenig eigene Semantik wir ergänzen müssen, um dieselbe UX-Regel präzise, quellengebunden und wartbar pro Komponente festzuhalten.

## Nachfolgende praktische Proben

Dieser Text bleibt der erste dokumentarische Vergleich. [FINDINGS.md](FINDINGS.md) ergänzt ihn um die tatsächlichen Teilproben und erhaltenen Fehlbefunde. Deren enger Umfang darf nicht nachträglich als praktischer Nachweis aller obigen Kandidaten ausgegeben werden.

[Native DMN-Folgeprobe und Regelzusammenspiel](runs/03/README.md) sowie [bedingter Integrationsvorschlag](RECOMMENDATION.md) ergänzen den anfänglichen Quellenstand. SBVR ist weiterhin nur schema-/dokumentengeprüft.
