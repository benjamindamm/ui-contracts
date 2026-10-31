# Paket 4 · Schlanker Einstieg, nachvollziehbarer Gesamtabgleich

**Stand: 31. Oktober 2026.** Schwerpunkt sind allgemeine Agentenarbeit und die Informationsarchitektur nach der **umgekehrten Pyramide**. Modellvergleiche bleiben optionale Forschung und sind kein hartes Einsatzkriterium: [Nutzerentscheid RD-002](../../decisions/RD-002-AGENT-WORKFLOW-SCOPE.md).

## Was sich ändert

- [Skillkern](../../../../skills/ui-contracts/SKILL.md): kurze Handlungsregeln und gezielte Routen. Detailregeln bleiben in passenden Referenzen; Rollen laden zunächst nur ihre Karte und den Auftrag.
- [Dokumentationswege](../../../README.md): oben Vorhaben und nächste Handlung, dann Arbeitswege, konkrete Quellen/Regeln und zuletzt Belege. [Architektur](../../../ARCHITECTURE.md), [aktueller Stand](../../../STATUS.md) und [Entwicklungsgeschichte](../../../EVOLUTION.md) haben getrennte Aufgaben. Die frühere README und Skilldokumentation sind vollständig erhalten.
- [Gemeinsamer Auswahlablauf](../../../../tools/ux/WORKFLOW.md): neue UX-Aufträge verwenden den bestehenden Task-/Handoff-v1-Vertrag statt ein studienspezifisches Sonderformat. Auswahl, Bauauftrag, Blindreview und Reportabgleich sind explizite Schritte mit eigenen Schreibbereichen und unveränderten Vorgängerversionen.
- [Gesamtabgleich](../../../../skills/ui-contracts/references/integration-review.md): Fachanforderungen/UX, Interface, Visual, Behavior, Accessibility und Integration werden abschließend berücksichtigt oder ausdrücklich als ungeprüft geführt. Pass/Fail benötigt führende Quelle und separaten Beleg. Große Prüfungen können bereichsweise mit gespeicherten Befunden stattfinden.

Die sechs Abdeckungsgruppen sind eine Arbeitsübersicht; sie ersetzen weder die vier führenden Domänen noch Originalstandards. Ein geordnetes Verfahren garantiert keine guten Modellergebnisse oder semantisch vollständige Prüfung beliebiger UIs.

## Technische Nachweise

**262 automatisierte Regressionserwartungen erfüllt:** darunter 18 Workflow-, fünf Kontext- und fünf Navigationsfälle. Der Skillkern umfasst 2.928 statt 7.246 Zeichen; die optionale erweiterte Builderübergabe 4.104 statt 7.152 Zeichen.


[verification.json](verification.json) bindet ausgeführte Prüfungen und Kontextmaße; [Navigation](evidence/navigation.json) erfasst den öffentlichen Repositorybestand und prüft die aktuellen Einstiegslinks; [Kontextguard](evidence/context.json) kontrolliert lokale Einstiegslängen und Nachladeziele. Das sind **Zeichen-/Dateimaße**, keine tatsächlich gemessenen Modellrequesttokens.

Die Integrationsprobe verwendet ausdrücklich `example` 0.4.0 und drei feste Werte. [Native Entscheidung](probe-02/work/selection/decision.json) und [Handoff](probe-02/work/selection/handoff-v1.json) sind tatsächlich erzeugt und geprüft; der gemeinsame Validator akzeptiert die Lieferung. Daraus entsteht ein [gültiger Builderauftrag](probe-02/tasks/build-v1.json) mit Bootstrap und gezielten Dateiverweisen. **Keine neue UI und kein Modelllauf wurden erzeugt.** Die unabhängigen Reviews innerhalb der Funktionstests sind klar als synthetische Strukturfixtures gekennzeichnet, keine echte Agentenstudie.

Die Funktionstests umfassen unter anderem falsche Bibliothek, geänderte Quellen, gefälschte Policywahl, partielle und übergroße Lieferungen, geschützte Erstbewertung, Quellen-/Artefaktbezüge und fehlende Abdeckungsgruppen. Ein fertiger Ablauf mit ausdrücklich ungeprüften Zielanforderungen bleibt ohne Ziel-Freigabe.

## Prüfung der Informationsarchitektur

Der Bestandsaudit inventarisiert Pfade, Größen und Ebenen aller nicht ignorierten Dateien. Aktive Routen werden gesondert geprüft; historische Dokumente und kopierte Rohartefakte werden nicht massenhaft umgeschrieben oder als Pflichtlektüre eingesetzt. Details und Originalquellen bleiben erreichbar. Die Inventarisierung ist kein Beweis vollständigen Fachwissens oder tatsächlichen Lazy-Load-Verhaltens eines Hosts.

| Ebene | Aufgabe | Einstieg |
| --- | --- | --- |
| Essenz | Zweck, nächste Handlung, Arbeitsregeln | Root-README, AGENTS, Skillkern |
| Orientierung | Ziel und passenden Arbeitsweg wählen | docs/README, Fach-/Werkzeugeinstiege |
| Details | Nur die aktuelle Rolle/Frage bearbeiten | Referenzen, Aufträge und Abnahmeplan |
| Originalquellen | Konkrete fachliche Regel und Zusammenhänge | Ausgewählte Bibliothek, ihre Domänen/Komposition |
| Belege | Herleitung oder konkreten Befund nachvollziehen | Forschung, Beispiele, Messdaten und historische Fassungen |

Die Ebene beschreibt **Lesetiefe**, nicht Wahrheitsrang. Eine frühe Zusammenfassung darf eine später gelesene Originalregel nicht überstimmen.

## Gefundene Probleme und Reparaturen

| ID | Befund | Reparatur / Gegenfall |
| --- | --- | --- |
| IA-001 | Der Skillkern enthielt viele spezielle Prüf- und Sonderfallregeln im Einstieg. | Essenz und Routen verkürzt; Details ohne Verlust in Referenzen belassen/überführt. Budget-, Link- und Eager-Import-Gegenfälle kontrollieren künftiges Wachstum. |
| IA-002 | Die Validierungsreferenz forderte gleich mehrere historische Inventare für jede Prüfung. | Zuerst passenden Prüfpfad wählen; IP01-Inventare nur für diesen Referenzumfang laden. |
| IA-003 | Root-Navigation vermischte aktuellen Arbeitsweg, historische Nachweise und Modellpilot als nächsten Pflichtschritt. | Dokumentationswege, aktueller Stand und Entwicklung getrennt; Modellpilot optional. Alte Inhalte vollständig erhalten. |
| IA-004 | Der alte Indexgenerator schreibt fest den Stand vom 25. Oktober und würde neuere Navigation überschreiben. | Altes Script bytegleich unter before erhalten; operativer Aufruf endet vor Dateizugriff als blockiert. Neuer Audit schreibt ausschließlich in neue Ergebnisdateien. Gegenfall prüft unveränderten aktuellen Index. |
| IA-005 | Namenskollision zwischen Archivübersicht und kopierter Root-README während dieser Arbeit. | Übersicht nach INDEX.md getrennt; README aus erhaltener Arbeitskopie und dokumentiertem Zusatz rekonstruiert. Kein unabhängiger Originalhash vorhanden; Herkunft offen ausgewiesen. |
| WF-001 / FW-009 | Neuere UX-Sonderaufträge waren nicht zum gemeinsamen Taskformat kompatibel. | Neuer begrenzter Adapter erzeugt normale v1-Tasks/Handoffs; alte Studien bleiben bytegleich erhalten. |
| WF-002 | Ein strukturierter Review mit nur einem Check könnte Querverbindungen und ganze Domänen still auslassen. | Sechs Gruppen verpflichtend ausweisen, fehlende Abdeckung begründen, Pass/Fail an Quellen und Belege binden. Das ist keine automatische Inhaltsgarantie. |

Originalstände stehen unter [before](before/INDEX.md), Zwischenproben separat unter preflight. [Befundstatus](resolution-status.json) · [Fehlerregister](../../../skills/ISSUES.md).

## Grenzen und offene Arbeit

Keine neuen Modell- oder Providerbehauptungen, keine allgemeine Ranking-/Qualitätsgarantie, kein frischer Browserlauf dieses Pakets. Prozessintegrität und endgültige Zielqualität bleiben getrennt. Modell-/Host-/Tokenmetadaten sind für normale Arbeit nicht erforderlich; bei einer ausdrücklich kontrollierten Forschungsfrage müssen fehlende Angaben weiterhin ehrlich als unbekannt gelten.

Bibliotheksweite Pins bleiben unverändert streng. Allgemeine Änderungsfolgen (FW-006), breitere UX-Fälle (FW-008), Werkzeugabdeckung (FW-011) und weitergehende Accessibility-/IME-Prüfungen (FW-012) sind durch diese Arbeit nicht pauschal geschlossen.
