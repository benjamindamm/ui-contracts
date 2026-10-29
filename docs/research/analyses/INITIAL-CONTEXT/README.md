# Separater Audit · Einstiegskontext und Nachladen

Stand: 29. Oktober 2026. Teil der Skillweiterentwicklung [RD-001](../../decisions/RD-001-STAGED-GENERATION.md), kein neuer Reproduktionslauf. Die bisherigen Studien bleiben unverändert.

## Ergebnis und Geltungsbereich

**Alles muss auffindbar bleiben; nicht alles muss sofort gelesen werden.** Verweise sind Nachlademöglichkeiten. Der Einstieg einer Rolle enthält nur den zugewiesenen Auftrag und den Weg zur eigenen Rollenkarte. Originalquellen, abhängige Lieferungen und ihre Belege werden für den jeweiligen Schritt nachgeladen. Notwendige Querverweise dürfen nicht durch zu enge Ausschnitte verloren gehen.

Geprüft wurden lokale Skilldateien, ihre Leseanweisungen und der Kontext-Helper. Die tatsächlich an frühere Modelle übermittelten Gesamtrequests liegen nicht vor. Eine genaue Anfangstokenzahl oder Ursache der HTTP-413-Ausfälle ist damit weiterhin **nicht belegt**.

## Was kommt wann in den Kontext?

| Ebene | Befund | Konsequenz |
| --- | --- | --- |
| Skillangebot | Laut offizieller Dokumentation zunächst Name und Beschreibung, in Codex auch Pfad; vollständiger SKILL.md-Text bei Aktivierung | Vorhandene Referenzdateien werden damit nicht pauschal eingelesen. [OpenAI-Dokumentation](https://learn.chatgpt.com/docs/build-skills) |
| Aktivierter UI-Contracts-Skill | Vor der Änderung 6.201 Zeichen. Potenzielle Kette aus Skill, Workflow, Übergabevertrag und Builderkarte: 17.492 Zeichen | Das war eine mögliche Folge unserer Leseanweisungen, keine gemessene automatische Anfangsladung. Rollen direkt zur eigenen Karte routen. |
| Elternhistorie | Das in dieser Sitzung verfügbare Delegationswerkzeug hat `fork_turns="all"` als Standard | Für unabhängige neue Worker ausdrücklich `none`; bei anderen Plattformen entsprechende Einstellung nachweisen. Kein Nachweis, dass frühere Läufe falsch gestartet wurden. |
| Neuer Bootstrap | Nur Taskpfad/Hash, Rollenkarte/Hash, Rolle/Phase und Lesereihenfolge | Keine Quelleninhalte, Vorgängerclaims, vollständigen Berichte oder anderen Rollenkarten inline. |
| Auftrag und eigene Karte | Nach dem Bootstrap zu lesen; Quellenliste, Schreibgrenzen und Abnahme auffindbar | Diese Inhalte zählen zusätzlich zum Bootstrap. Vor Erstellung Abnahme und Schreibgrenzen lesen. |
| Erweitertes `context` | Bei ausdrücklichem Bedarf ausgewählte Claims samt Quellenverweisen; derzeit auch alle Fragen und Grenzen der jeweiligen Übergabe | Nicht als Standard-Starteintrag verwenden. Bei großen Aufgaben eigene kleine Aufträge erzeugen. |
| Hash-/Integritätsprüfung | Der Helper liest lokal Manifest, referenzierte Dateien und Abhängigkeiten zur Prüfung | Lokales Dateilesen durch Code ist nicht gleich Übermittlung des Dateiinhalts als Modellkontext. |
| Plattform | System-/Entwicklervorgaben, Toolbeschreibungen, weitere Skillbeschreibungen und globale Laufzeitvorgaben | Auch bei leerer Gesprächshistorie vorhanden; hier kein vollständiger Requestdump und keine genaue Größenmessung. |

Keine zusätzliche AGENTS.md-Datei an den geprüften übergeordneten Pfaden von `/` bis zum Repository sowie unter `~/.codex` gefunden. Das schließt andere durch Plattform oder Laufzeit injizierte Anweisungen nicht aus.

## Reparatur und Nachweis

- [Skillrouting](../../../../skills/ui-contracts/SKILL.md): zugewiesene Rollen lesen ihre Karte und ihren Auftrag; Workflow/Übergabevertrag nur bei entsprechender Aufgabe. Keine pauschale Leseanweisung für alle Referenzen.
- [Workflow](../../../../skills/ui-contracts/references/workflow.md): Verweiskette, frischer Gesprächskontext und stufenweises Nachladen ausdrücklich festgelegt.
- [Helper](../../../../skills/ui-contracts/scripts/handoffs.py): neuer Befehl `bootstrap`; vorhandenes `context` bleibt als nachladbare Erweiterung erhalten. Aktuelle Quellen-/Abhängigkeitshashes werden auch im Bootstrap geprüft.
- Bootstrap-Standard: maximal **2.000 Zeichen für die vollständige erzeugte JSON-Datei**, einschließlich Wrapper, Einrückung und Zeilenende. Überschreitung blockiert; kein Abschneiden. Lokale Konvention, keine Token- oder Providergrenze.
- Synthetischer kleiner Builderauftrag: **959 Zeichen Bootstrap**, **1.447 Zeichen Auftragsdatei**, **2.440 Zeichen erweitertes Kontextpaket**. Das sind unterschiedliche Stufen und keine vergleichbaren Gesamtrequestgrößen. Temporäre Pfadlängen können die Zahlen verändern.
- **37 Funktionstests** auf Quell- und installierter Skillkopie bestanden; darunter fünf neue Bootstrapfälle. Beide Skillstrukturprüfungen bestanden. Keine Modellgeneration ausgeführt und keine Qualitätssteigerung behauptet.

[Baseline vor Änderung](../../../../tools/skill-tests/ui-contracts/initial-context-baseline.json) · [Messdaten](../../../../tools/skill-tests/ui-contracts/initial-context-audit.json) · [Messskript](../../../../tools/skill-tests/ui-contracts/audit_initial_context.py) · [Tests Quelle](../../../../tools/skill-tests/ui-contracts/results-bootstrap-source.json) · [Tests Installation](../../../../tools/skill-tests/ui-contracts/results-bootstrap-installed.json) · [Tests](../../../../tools/skill-tests/ui-contracts/test_handoffs.py).

## Unterschiedliche Agentenprogramme

[Separate Einstiegskontrolle für Claude, Gemini, OpenCode und andere Hosts](ENTRYPOINTS.md): gemeinsamer kurzer AGENTS-Einstieg, dünne alternative Wegweiser und Prüfung globaler/automatischer Kontexte vor einem Lauf.

## Verbindliche Kontexthygiene und offene Messung

1. Neuer unabhängiger Worker: keine Elternhistorie übernehmen; Startkonfiguration im Studienmanifest dokumentieren. Das erzwingt der Helper nicht.
2. Einstieg: schlanker Auftrag und eigene Rolle; keine README-/Research-/Index-Sammlung vorsorglich lesen. Ein Index vermittelt Pfade, keinen Auftrag, alle Ziele zu öffnen.
3. Quellen: nur aktuell benötigte Dateien oder Abschnitte nachladen; zugehörige Originalquellen und notwendige Beziehungen erreichbar halten. Abgeleitete Aussagen bleiben als solche markiert.
4. Austausch: kleine versionierte Übergabedatei; große Messungen und Artefakte hinter hashgebundenen Verweisen. Keine fremden Chatprotokolle als Standardübergabe.
5. Werkzeuge: nur relevante Fähigkeiten entdecken; große Toolausgaben in Dateien halten und konkrete Diagnosen zurückgeben. Browserbilder und Binärartefakte nicht vorsorglich inline übertragen.
6. Vor einem neuen Pilot die tatsächliche Startkonfiguration erfassen: Plattform/Modell/Tokenizer, Historienübernahme, Skill-/Auftragsrevision, geladene Pfade und Reihenfolge, Toolschemas, Ausgabegrößen und soweit verfügbar Requestbytes/Inputtokens. Der Bootstrap allein deckt dies nicht ab.
7. Wachstum während der Arbeit getrennt messen: Nachladeumfang, Werkzeugresultate und Fortsetzungen. Bei Bedarf checkpointen und einen fokussierten Nachfolgeauftrag erstellen, statt den ganzen Verlauf weiterzugeben.

Offen: Die vollständige Auftragsdatei und der aktivierte Skill benötigen ebenfalls Kontext; das Bootstraplimit begrenzt sie nicht. Das bestehende Limit des erweiterten Pakets zählt dessen JSON-Inhalt ohne den CLI-Wrapper; es ist kein Gesamtrequestlimit. Bessere Leistung schwächerer Modelle und weniger Providerabbrüche müssen im geplanten kontrollierten Pilot erst nachgewiesen werden. Die bisherigen HTTP-413-Ursachen bleiben ohne vollständige Fehlerantworten/Requestgrößen ungeklärt.
