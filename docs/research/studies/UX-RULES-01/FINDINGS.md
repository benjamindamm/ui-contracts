# Praktischer Zwischenstand · UX-RULES-01

30. Oktober 2026. Zwei abgegrenzte Messblöcke abgeschlossen; die Gesamtuntersuchung bleibt offen. [Lauf 01](runs/01/README.md): 38/39 Check-Erwartungen erfüllt, ein Fehler in eigener Rego-Proberegel. [Lauf 02](runs/02/README.md): 6/6 nach separater Reparatur. Diese Zahlen sind **keine** Prozentbewertung der UX-Eignung und kein vollständiger gemeinsamer Benchmark.

## Was jetzt belegt ist

| Beitrag | Praktischer Befund | Bedeutung für unser Regelmodell |
| --- | --- | --- |
| FEEL | Fehlende Variable und null ergeben im Rohprädikat null; die fehlende Variable erzeugt eine Warnung. Zusätzliche Typprüfung unterscheidet unzulässige Eingaben. | Diagnostik und Typmodell müssen mitgeführt werden; nacktes Boolean/Default reicht nicht. |
| Rego | Roher candidate-Wert fehlt bei unbekanntem Fakt. Eigener erster Else-Guard liefert unerwünscht unsuitable; korrigierter Guard behandelt denselben Fall als unknown. | Viel Ausdrucksfreiheit, aber keine automatische fachliche Semantik. Eigene Regeln benötigen Gegenfälle und Versionierung. |
| SHACL | Fehlende Fakten führen bei der geprüften minCount-Bedingung zu Nichtkonformität, nicht zu einer fachlichen unknown-Aussage. allow_warnings verändert den pySHACL-Konformitätswert. | Gut als Constraint-Prüfer untersuchbar; Ergebnis-Severity, Evaluatoroption und fachliche Verbindlichkeit strikt trennen. |
| DMN und SBVR | Originalschemas lokal verfügbar und verwendbar; DMN-XML akzeptiert, ungültiges Attribut abgewiesen. SBVR-XSD kompiliert. | Realer Formatnachweis, aber kein voller DMN-/SBVR-Ausführungsnachweis. |
| Komponentenbindung | Eigener Hash-/Ankeradapter prüft CEM, Visualtoken, SCXML und HTML-Ziel; mehrere falsche/veraltete Referenzen werden erkannt. | Verbindung mit unserem Bestand technisch plausibel und begrenzt erprobt. Dies bleibt eigener Integrationscode, nicht native Fähigkeit der Kandidaten. |

## Vorläufige Richtung, keine Entscheidung

Die bisherige Evidenz spricht gegen die Annahme, eine generische Regelengine bringe bereits das gesuchte UX-Handbuchmodell mit. Wir müssen mindestens Kontextbegriffe, Regelstärke, Zielbindung, Status und Ergebnisinterpretation fachlich festlegen. Das bedeutet noch nicht, eine neue Ausdruckssprache zu erfinden.

Als nächste Vertiefung sind FEEL/DMN und Rego für ausführbare Bedingungen sinnvoll vergleichbar; SHACL separat für Beziehungs-/Constraintprüfungen. SBVR weiter auf praktikablen Autoren-/Evaluatorweg prüfen. ACT und EARL ergänzen mögliche Prinzipien für Regelqualität und Ergebnisbelege, ersetzen aber bisher keine geprüfte UX-Bedingungssprache. UGL/GDL sind relevante UX-nahe Forschungsspuren mit noch ungeklärter aktueller Werkzeuglage.

Keine Kombination beschlossen, keine Dateien in Bibliotheken/Skills migriert. Weiter offen: Pflicht versus Empfehlung und begründete Ausnahme (T05/T06 vollständig), gemeinsame/lokale Regeln (T11), gezieltes Nachladen und Modellverständnis (T12), vollständige Originalformat-Ausführung und eine belastbare Wartungs-/Lizenz-/Aufwandsbewertung. Erst danach Auswahl oder enges Integrationsprofil vorschlagen.

## Fehlerquellenregister dieser Untersuchung

- **UXP-001:** Negativer FEEL-Syntaxtest war im eigenen Harness zunächst nicht abgefangen; Vorbereitung korrigiert und preflight-issue.json erhalten.
- **UXP-002:** Fehlender Fakt wurde durch eigene Rego-Else-Regel als unsuitable gewertet. Lauf 01 bleibt erhalten, Reparatur in Lauf 02, Wiederholungsfälle T03/T04.
- **UXP-003:** Nicht typgesicherte FEEL-Bedingung behandelt Text "true" als ungeeignet. Typisierte Vergleichsvariante im selben vorbereiteten Block; Warnungen/Typfehler nicht verwerfen.
- **UXP-004:** SHACL-Warning kann durch Evaluatoroption Konformität verändern. Optionen explizit protokollieren; nicht mit normativer Verbindlichkeit gleichsetzen.

Die Befunde betreffen diese konkreten Proben. Keine pauschale Aussage über schwache Modelle oder alle Implementierungen.

## Folgeblock: native DMN-Ausführung und Regelzusammenspiel

[Lauf 03](runs/03/README.md): 33/33 Check-Erwartungen erfüllt. DMN Scala führt jetzt die XML-Modelle aus; eine gemeinsame Decision wird über eine explizite Referenz verwendet. Acht eigene Normativitätsfälle stimmen mit Rego überein. Eine Empfehlungsausnahme hebt die Pflicht im geprüften Profil nicht auf, eine fremde Komponente/Bibliothek fällt nicht in den Geltungsbereich. Diese Prioritäts-/Scope-Semantik haben wir als Versuchspolicy festgelegt; sie ist kein eingebautes UX-Handbuch.

Der technische Dateiladetest umfasst nur relevante Rego-Module und Quellreferenzen. Reale Agentenrequests/Verständnis bleiben ungemessen. Ein eigener Referenzgate bindet alle vier Domänen vor DMN-Ausführung; bei falscher Revision wird die Engine nicht aufgerufen.

[Lauf 04](runs/04/README.md) enthält drei Kodierungschecks für ODRL-Konfliktstrategien, keine Policy-Evaluierungen. [Werkzeug-/Aufwandsvergleich](TOOLING-AND-COST.md) und [bedingte Empfehlung](RECOMMENDATION.md) führen den Stand zusammen. Die oben erhaltenen Erstbefunde waren zum damaligen Zeitpunkt richtig; die fehlende native DMN-Ausführung ist nun im beschriebenen Umfang ergänzt, SBVR-Ausführung bleibt offen.

Weitere dokumentierte eigene Setupfehler: UXP-005 (inkompatible explizite Jackson-Version im Java-Harness) und UXP-006 (nicht unterstützter tarfile-Parameter in Python 3.9). Beide vor den Messungen korrigiert und im Lauf-03-Preflight erhalten; keine Frameworkfehler.

## AC-UX-01 · Tatsächliche Komponentenregeln und nativer Trace

[Der separate Kandidat](pilots/AC-UX-01/README.md) geht über die bisherige Aggregation abstrakter mandatoryMet-Fakten hinaus: Anforderungen an Wertneuanlage und Auswahlkardinalität werden gegen konkrete Grenzen der bestehenden Autocomplete-Definition ausgewertet. Vertrautheit der Labels ist eine separat belegte Empfehlung mit explizit zu deklarierender Kontextbeurteilung.

43/43 Erwartungen erfüllt. Elf native Auswertungen liefern je drei echte matched-row IDs aus dem DMN-Audit, die das eigene Profil auf Regelstärke, Status, Begründung und Quellen zurückführt. Siebzehn Gegenfälle blockieren vor dem Engineaufruf, darunter fremde/veraltete Bindungen, fehlende Quellenanker, doppelte IDs, inkonsistente Metadaten und der Versuch, eine Fähigkeitsgrenze durch Ausnahme zu übersteuern.

Der frühere offene Tracepunkt ist damit für diese drei Tabellenregeln im Kandidaten nachgewiesen; keine allgemeine Zusage für beliebige DMN-Modelle. Faktwahrheit, tatsächliche Entscheidungshoheit des angegebenen Reviewers und Agentenverständnis bleiben ungemessen. Ein eigener Schemafehler in der Vorbereitung ist als UXP-007 im Pilot-Preflight samt Reparatur erhalten.
