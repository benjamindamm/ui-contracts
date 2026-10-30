# Vorschlag für die nächste Integrationsprobe

**Forschungsempfehlung, noch keine beschlossene Frameworkübernahme.** Grundlage sind Quellenvergleich und vier erhaltene Messblöcke. Kein Framework deckt nach den hier erbrachten Nachweisen unser gesamtes UX-Handbuchziel fertig ab. Das ist eine Aussage zum Prüfstand, kein universeller Negativbeweis.

## Vorschlag

**DMN/FEEL zuerst als ausführbaren Kern einer kleinen komponentengebundenen UX-Regelprobe erproben; Rego als praktisch getestete Alternative behalten.** DMN bringt ein standardisiertes Modell-/Austauschformat, definierte Ausdrücke und explizite Decision-Referenzen mit. Der lokale Nachweis reicht nun über alleinige FEEL-Ausdrücke hinaus: native XML-Ausführung, geteilte Decision, Konfliktfälle und eigene vorgelagerte Contractbindung sind ausgeführt.

Rego ist technisch ebenfalls tragfähig für die getestete Logik, verlangt aber ebenso ein selbst festgelegtes UX-Vokabular und einen Ergebnis-/Bindungsvertrag. Das ist keine gemessene Aussage über generelle Wartbarkeit oder Agentenleistung. Es gibt keinen Nutzenbeleg dafür, beide Engines gleichzeitig in jede Komponente einzubauen.

SHACL zunächst nicht zusätzlich verpflichtend einführen: Sein belegter Beitrag ist Graphvalidierung; die notwendige RDF-Projektion wäre weiterer Integrationsaufwand. SBVR als begriffliches Referenzmodell behalten, bis ein praktikabler Werkzeugweg nachgewiesen ist. ACT/EARL als Vorbilder für Regelqualität und Ergebnisbelege betrachten, nicht als bereits gewählte Gesamtlösung. ODRL und MBUI bleiben nach dokumentiertem Grenzvergleich ergänzende Referenzen.

## Was das kleine eigene Profil leisten müsste

1. Einen stabilen Regelbezug zu Bibliothek, Komponente, Revision und vorhandenen Originalankern herstellen. Native Datei-/URI-Felder ersetzen unseren Hash-/Typ-/Existenzgate nicht.
2. Ein kontrolliertes Kontextvokabular mit Datentypen und Herkunft der Fakten festlegen. Agenten dürfen unbekannte Fakten nicht zu false machen oder fehlende Tatsachen erfinden.
3. Pflicht, Empfehlung und begründete Ausnahme samt Entscheidungshoheit getrennt führen. Ausnahmen dürfen keine technisch nicht vorhandene Fähigkeit der Komponente herbeidefinieren.
4. Bestehende Behavior-/Visual-/ARIA-Regeln referenzieren. Regelstatus, Begründung und Beleg ergänzen; kein zweites führendes Verhalten schaffen.
5. Ausgaben mit zutreffender Regel-ID, Ergebnis, Diagnostik und verwendeter Revision versehen. Unbestimmt, nicht anwendbar und Fehler bleiben unterscheidbar.

Dieses Profil wäre unsere Integrationskonvention, nicht ein neuer universeller Standard. Die Bedingungslogik bliebe in der gewählten Originalsprache. Keine Prosa als formale Semantik ausgeben.

## Abnahme der nächsten Probe

Eine separate Kandidatenrevision für example/Autocomplete erstellen, bestehende Definition und Forschung bewahren. Wenige echte, fachlich begründete UX-Regeln mit positiven/negativen/fehlenden Kontextdaten und Contractverweisen verbinden. Vor Ausführung Eingaben und Erwartungen einfrieren. Danach eine begrenzte Agenten-Leseprobe auf verständliche Anwendung und Nachladen durchführen, sofern separat autorisiert. Die frühere synthetische Aggregation von mandatoryMet/preferenceMet ist kein Ersatz für diese echte Komponentenmodellierung.

Offene Vorbehalte: vollständiger Trace der tatsächlich zutreffenden Regel-/Tabellenzeilen samt Evidenz (die jetzige Java-Bridge gibt nur den Ergebniswert aus), native SBVR-Semantik, vollständige transitive Lizenzprüfung, allgemeine Framework-/DMN-Konformität und eine faire Agenten-/Aufwandsstudie. Deshalb keine Änderung an libraries/, component.json, Prüfgates oder installierten Skills in dieser Forschungsrunde.

## Nachfolgender Pilotstand

Auf Nutzerauftrag wurde [AC-UX-01](pilots/AC-UX-01/README.md) separat ausgeführt. Die drei Regeln haben nun komponentengebundene Faktenbedingungen und einen echten nativen Tabellenzeilentrace mit Quellenzuordnung; 43/43 Checks erfüllt. Das schließt den zuvor offenen Tracepunkt für diesen begrenzten Kandidaten, nicht für alle künftigen Regeln. Bibliotheksintegration, produktive Übernahme und unabhängige Agenten-Leseprobe sind nicht erfolgt.
