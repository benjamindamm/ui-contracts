# Auswahl, Umsetzung und Prüfung mit gemeinsamen Übergaben

Dieser optionale Adapter richtet **künftige** Auswahl-/UI-Aufträge auf den vorhandenen `ui-contracts-task/1`- und `ui-contracts-handoff/1`-Vertrag aus. Er ist keine neue UI-Beschreibungssprache. Normale kleine Autorenänderungen brauchen diesen vierstufigen Ablauf nicht.

```mermaid
flowchart LR
  A[Auswahl] --> B[Bauen] --> C[Erstprüfung] --> D[Reportabgleich]
```

Der Adapter startet keine Agenten und generiert keine UI. Er erstellt versionierte Aufträge und prüft die Übergaben. Den vorhandenen UX-Nativprüfer benötigt nur der Schritt, der eine entsprechend nachgewiesene Policyentscheidung an einen Builder weitergibt. Andere Aufgaben können weiterhin direkt als generische Task-/Handoff-Dateien formuliert werden. Keine automatische Auswahl von `example`.

## Kurzer Einstieg

Eine JSON-Datei mit den fachlichen Anforderungen (`brief.json`) und der bekannte [Faktenkontext](README.md) reichen als Eingaben; das Briefing wird als Anforderungsdatei gebunden, nicht in neue UX-Regeln übersetzt. Bibliothek und Ziel ausdrücklich wählen.

```sh
tools/validation/.venv/bin/python tools/ux/workflow.py prepare \
  --library example --context tools/ux/contexts/fixed-three.json \
  --brief PFAD/brief.json --target web --id personenformular \
  --out .runtime/personenformular
```

Nur Bootstrap an eine beauftragte Rolle übergeben:

```sh
python3 skills/ui-contracts/scripts/handoffs.py bootstrap \
  --repo . --task .runtime/personenformular/tasks/selection-v1.json \
  --output .runtime/personenformular/selection-bootstrap.json
```

Der Auswahlauftrag liest Tatsachen und nötige Originalquellen nach. Mit `tools/ux/choose.py` speichert er `decision.json` innerhalb seines eigenen Schreibbereichs und liefert eine passende `handoff-v1.json`. Kleine technische Belege werden darin referenziert, nicht vollständig hineinkopiert. Erwartete Artefakt-IDs und Lieferkriterien stehen im Auftrag.

```sh
tools/validation/.venv/bin/python tools/ux/workflow.py advance \
  --workflow .runtime/personenformular/workflow-v1.json \
  --handoff .runtime/personenformular/work/selection/handoff-v1.json
```

Es entsteht `workflow-v2.json` plus `tasks/build-v1.json`. Beim nächsten Schritt dieselbe Form verwenden, jeweils mit der aktuellen Workflowdatei und neuen Lieferung. Bestehende Versionen werden nicht überschrieben. `inspect --workflow PFAD` prüft aktuelle Referenzen und zeigt den aktiven Schritt.

## Was ein Nachfolger erhält

| Schritt | Eingaben | Was zurückgehalten bleibt |
| --- | --- | --- |
| Auswahl · Mapper | Fachbriefing, Kontextfakten, Originalindex/Policy/Fähigkeiten; Domänen bei Bedarf über component.json | Frühere Studienergebnisse und fremde Lösungen |
| Bauen · Builder | Briefing/Fakten, tatsächliches Entscheidungsartefakt, gebundene Lieferrevision, Originalquellen | Fremde Gespräche; freie Mapperclaims werden nicht pauschal inline übernommen |
| Erstprüfung · Reviewer/blind | Fachanforderungen, Originalquellen und ausdrücklich als `target` gelieferte Dateien | Builderbericht und Mapper-/Builderhandoffs |
| Reportabgleich · Reviewer/report-check | Zusätzlich separat eingefrorene Erstprüfung und Builderbericht | Schreibzugriff auf Erstprüfung und Vorgängerartefakte |

Der Auswahlfortschritt wird gegen eine frisch ausgeführte native Policyentscheidung geprüft. Veränderte Schlüssel, Fakten oder Quellrevisionen blockieren die abhängige Aufgabe. Eine partielle Lieferung ist kein freigegebener Vorgänger. Die Bibliotheksbindungen bleiben streng; eine bloße README-Änderung wird hier nicht still aus dem Ganzbibliotheksmanifest herausgefiltert.

Ein Build benötigt Artefakt-ID `target` mit Art `target` und eine separat klassifizierte ID `report` mit Art `builder-report`; weitere benötigte Zieldateien ebenfalls als Art `target` liefern. Der Koordinator muss ehrliche Klassifizierung prüfen: Der Helper erkennt keine absichtlich versteckten Berichte oder Erläuterungen in einem Zielartefakt.

Die Erstprüfung liefert ID und Art `first-review` mit `definitionRevision`, exakten `targetHashes`, nichtleeren `checks` und expliziten `notChecked`. Die sechs Gruppen `requirements-ux`, `interface`, `visual`, `behavior`, `accessibility`, `integration` müssen ausdrücklich vorkommen. Checkstatus ist `pass`, `fail`, `not-checked` oder `undetermined`. Pass/Fail benötigen `sourceRefs` mit gebundenem Pfad, SHA-256 und Locator in Vertrag oder Fachanforderung sowie `evidenceRefs` auf eigene separate Artefakte; nichtgeprüft/unentscheidbar benötigt `reason`. Das prüft die Nachvollziehbarkeit, nicht die Wahrheit beliebiger Messdateien. Erst danach wird der Reportauftrag angelegt. Ein **vollständig durchgeführter Review mit gefundenen Fehlern** kann eine fertige Übergabe sein; daraus wird kein Qualitäts-Pass abgeleitet.

## Ergebnis statt Modellversprechen

Modellname, Anbieter, Tokens und Kontextfenster sind für den normalen Ablauf **keine Pflichtangaben**. Der Builder recherchiert seine Identität nicht. Bei Forschungsinteresse können belegte Launcher-/Verbrauchsdaten separat erfasst werden; Unbekannt bleibt unbekannt.

`HANDOFF_READY` prüft Integrität und deklarierte Vollständigkeit. `WORKFLOW_COMPLETE` bedeutet, dass die vorgesehenen Lieferungen vorliegen. Beide bleiben `release:false`, `targetApproval:not-inferred`: keine Garantie guter Modellarbeit, keine automatische fachliche, visuelle oder Accessibility-Freigabe. Zielbezogene echte Prüfungen bleiben dafür nötig. Ein solcher Ablauf kann Fehler leichter sichtbar und reparierbar machen; eine gemessene allgemeine Qualitätssteigerung wird daraus nicht behauptet.

[Technische Integrationsprobe und Grenzen](../../docs/research/analyses/AGENT-WORKFLOW-2026-10-31/README.md). Historische SELECTION-01/02-Aufträge bleiben unverändert; sie werden nicht nachträglich als v1-Aufträge ausgegeben.
