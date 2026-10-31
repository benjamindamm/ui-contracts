# Fokussierte Rollen und Wissensübergaben

Für zusammengesetzte Komponenten oder explizite Zusammenarbeit. Bei einer kleinen Änderung im bestehenden Vertrag reicht der normale Autoren-/Prüfablauf; keine künstlichen Rollen oder zusätzlichen Agenten erzeugen. Delegation nur innerhalb des tatsächlich autorisierten Auftrags.

## Schlanker Start

Für eine neue Rolle zunächst nur `bootstrap` übergeben: Auftragspfad und Hash, Rolle, Rollenkarte und Lesereihenfolge. Keine Quelltexte, Vorgängerclaims oder Forschungsberichte inline. Der Worker liest danach Auftrag und eigene Rollenkarte; daraus lädt er nur aktuell benötigte Originalquellen, Querverweise und Inputs nach. Abnahmekriterien vor der Erstellung prüfen. Workflow und Übergabevertrag muss nur lesen, wer den Ablauf plant oder die entsprechenden Dateien verfasst.

Neue unabhängige Agenten ohne übernommene Gesprächshistorie starten. Beim hier verfügbaren Delegationswerkzeug ausdrücklich `fork_turns="none"` verwenden; dessen Standard `all` übernimmt die Elternhistorie. Andere Plattformen benötigen ihre entsprechende Einstellung. „Frischer Chat“ entfernt keine Systemvorgaben, Toolbeschreibungen oder Plattformregeln. Der Helper startet selbst keine Agenten und erzwingt diese Einstellung nicht.

## Kontext nach Bedarf

Ein Arbeitsauftrag ist eine Datei pro Rolle/Teilaufgabe. Bibliotheks-ID ausdrücklich benennen; das gebundene Definitionsmanifest setzt `root: libraries/<id>`. Gleichnamige Komponenten verschiedener Bibliotheken sind keine identische Quelle. Keine impliziten Imports aus example. Übergeben werden Ziel, Definition/Version, ausgewählte Originalquellen mit Zweck, benötigte Vorgängerdateien, Schreibbereich, offene Fragen und Abnahmekriterien. Gesprächsverläufe und fremde Zwischenversuche sind keine Standardübergabe. Alle vier führenden Domänen bleiben über die Quellenkarte auffindbar; eine Rolle darf eine notwendige Querverbindung nachladen, statt aus einem zu engen Ausschnitt zu raten.

Der Koordinator schneidet Aufgaben nach Abhängigkeiten, nicht starr nach Dateityp: gemeinsame Identität und Ownership zuerst; danach unabhängige Teile parallel; Zusammenführung nach deren Lieferung; unabhängige Prüfung; gezielte Reparatur. Nicht gleichzeitig denselben Teil oder dieselbe Übergabedatei schreiben. Änderungen am Interface oder an einer geteilten Annahme invalidieren davon abhängige Übergaben.

Lade nur die zutreffende Rollenkarte:

| Rolle | Karte | Benötigter Kontext |
| --- | --- | --- |
| Koordination | [roles/coordinator.md](roles/coordinator.md) | Nutzerziel, Quellmanifest, Abhängigkeiten und Lieferstatus. Keine fachlichen Details aller Teilaufgaben vorsorglich sammeln. |
| Quellenzuordnung | [roles/mapper.md](roles/mapper.md) | Relevante Originalquellen und Querverweise; genau eine zugewiesene Domäne oder Verbindung. |
| Builder / Integration | [roles/builder.md](roles/builder.md) | Geprüfte Zuordnungen, relevante Originalquellen, technische Werkzeuge und benötigte Teil-Artefakte. |
| Unabhängige Prüfung | [roles/reviewer.md](roles/reviewer.md) | Gemeinsame Policy, Originalquellen und Zielartefakt; Buildererklärungen erst nach eingefrorener Erstbewertung. |
| Reparatur | [roles/repair.md](roles/repair.md) | Vorheriges Artefakt, konkrete Soll-/Ist-Diagnosen, Quellen und betroffene Regressionen. |

## Persistente Austauschdokumente

Pro Teilaufgabe: `task.json` als Auftrag und versionierte `handoff-v1.json`, `handoff-v2.json` als Lieferungen. Keine gemeinsam wachsende Sammeldatei. Eine kleine Koordinationsübersicht zeigt nur aktive Versionen, Abhängigkeiten und Status. Alte Versionen bleiben erhalten; eine neue Revision benötigt eine neue Datei. Noch nicht geliefert ist nicht gleich fehlgeschlagen.

Der [Übergabevertrag](handoff-contract.md) legt die Felder fest. [Vorlagen](../assets/handoffs/task.json) und [Lieferungsvorlage](../assets/handoffs/handoff.json) sind auszufüllen, keine einsatzfertigen Forschungsdaten. `scripts/handoffs.py` prüft Referenzen und erzeugt bei Bedarf ein kleines Kontextpaket mit Pfaden und ausgewählten Aussagen. Es verteilt keine Tasks, startet keine Agenten und liest keinen Chatverlauf.

```sh
python3 SKILL/scripts/handoffs.py bootstrap --repo REPO --task PFAD/task.json --output /tmp/task-bootstrap.json
# Nur bei Bedarf: erweitertes Kontextpaket mit ausgewaehlten Aussagen
python3 SKILL/scripts/handoffs.py context --repo REPO --task PFAD/task.json --output /tmp/task-context.json
python3 SKILL/scripts/handoffs.py check --repo REPO --task PFAD/task.json --handoff PFAD/handoff-v1.json --output /tmp/handoff-check.json
```

`SKILL`, `REPO`, `PFAD` durch tatsächliche Pfade ersetzen. Die Vorlagen nicht im Skillordner ausfüllen; die Arbeitsdateien gehören in den neuen vorgesehenen Arbeitsbereich. Ausgabeordner außerhalb eingefrorener Läufe wählen. Bootstrap: höchstens 2.000 Zeichen für die vollständige JSON-Ausgabedatei inklusive Wrapper/Einrückung, mit `context.maxBootstrapChars` ausdrücklich änderbar. Das ist nur der von uns erzeugte Starteintrag, kein Budget für den gesamten Modellrequest. Die lokale Hashprüfung darf Dateien lesen, ohne deren Inhalte dem Modell zu übergeben.

Erweitertes Paket klein halten: Standard höchstens 16.000 Zeichen je Übergabe und 8.000 Zeichen je Kontextpaket; nötige Details über explizite Dateiverweise nachladen. Bei Überschreitung wird blockiert statt unbemerkt abgeschnitten. Diese Werte sind lokale Arbeitskonventionen, keine Modell- oder Providergrenzen.

## Gegen falsche Verdichtung

Eine Übergabe nennt Aussagen als `explicit`, `derived`, `assumption` oder `observation`, jeweils mit nachvollziehbarer Quelle beziehungsweise Messbeleg. Verbindlich bleibt die führende Originaldatei. Nicht aus „Annahme des Vorgängers“ eine Regel machen. Bei Konflikt die konkreten Quellen und Folgen melden; zuerst unabhängig mögliche Arbeit fortsetzen, abhängige Schritte blockieren.

Das Tool validiert Struktur, aktuelle Dateien/Hashes, Quellenbindung und deklarierte Zugriffsgrenzen. Es bestätigt keine fachliche Richtigkeit, tatsächliche Zugriffssperre oder Ausführung der berichteten Prüfungen. Der Koordinator muss Aussagen und Messbelege weiterhin sachlich prüfen. `HANDOFF_READY` bedeutet verwertbare Übergabe, keine Komponentenfreigabe.

## Abschließende Integration und optionale Forschung

Die kurze Handlungsessenz steht in SKILL.md. Beim Abschluss den [Gesamtabgleich](integration-review.md) laden: betroffene Regeln/Quellen und ihre Verbindungen schrittweise prüfen; offene Bereiche bleiben explizit im Abdeckungsplan. Das Gesamtwissen bleibt über Quellen und Verweise erreichbar, ohne pro Rolle vollständig in den Kontext zu wandern.

Modell-/Tokenmetadaten und kontrollierte Vergleichsläufe sind optionale Forschungsaufträge, keine Voraussetzung normaler Arbeit oder Garantie guter Ergebnisse. Für künftige Auswahl-/UI-Aufträge bietet `tools/ux/workflow.py` im Repository einen Adapter zum vorhandenen Task-/Handoff-Vertrag; `tools/ux/WORKFLOW.md` nur beim Planen dieses konkreten Ablaufs laden. Er startet keine Agenten und gibt kein Ziel pauschal frei.
