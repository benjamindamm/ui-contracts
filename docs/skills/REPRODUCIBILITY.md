# Reproduktionsläufe: Auftrags- und Nachweisvertrag

Gilt für künftige explizit beauftragte Reproduktions-/Modellvergleiche. Normale Komponentenarbeit muss nicht dieses vollständige Forschungsprotokoll führen. Herkunft: [AC-R02-Analyse](../research/analyses/AC-R02/README.md) und [Fehlerregister](ISSUES.md).

Für die eigentliche Aufgabenzerlegung und Wissensübergabe gilt der [operative Skill-Workflow](../../skills/ui-contracts/references/workflow.md) mit [Auftrags-/Übergabevertrag](../../skills/ui-contracts/references/handoff-contract.md). Dieser funktioniert auch außerhalb einer Studie; das vorliegende Dokument ergänzt die Forschungsprovenienz. Übergaben sind kleine versionierte Ergebnisse mit Originalquellen und benötigten Artefakten, keine vollständigen fremden Gesprächsverläufe.

## Vor dem Lauf

1. Zielumfang festlegen: statisches editierbares Design, ausführbares Webziel und native Plattformen sind verschiedene Prüfaufträge. Für ein statisches Design keine nicht vereinbarte ARIA-Laufzeitkonformität verlangen.
2. Originaldateien, Revision und Hashalgorithmus in erlaubten technischen Laufmetadaten festhalten. Das Label wird als SHA-256 über das UTF-8-kodierte, kompakte JSON-Objekt der nach Pfad sortierten `Pfad -> Datei-SHA-256`-Paare berechnet (`sort_keys=True`, `separators=(',', ':')`). Dateihashes getrennt erhalten.
3. Einen gemeinsamen quellengebundenen Prüfkern und seine Toleranzen für alle verglichenen Modelle einfrieren. Ein unabhängig von jedem Modell abgeleiteter Prüferkatalog ist zusätzlich interessant, ersetzt aber nicht dieselbe Messlatte. Im Prüferkatalog jede Annahme gegen die führende Quelle und gegen andere Kriterien gegenprüfen, bevor sie versiegelt wird.
4. Modellname, Modellrevision, Reasoning-Stufe und Harness-/Budgetkonfiguration **je Builder und Prüfer** dokumentieren. Unbekannt bleibt `null`; keine Vermutung aus dem Modell der koordinierenden Session übernehmen. Skill-Dateien und Erstaufträge mit exaktem Wortlaut und Hash ablegen; ein nicht benutzter Skill ist eine explizite leere Liste.
5. Alle Eingrenzungen und Aufträge vor Einsicht in Ausgaben festhalten. Bei gewünschter Kontexttrennung getrennte Sessions, dieselbe erlaubte Eingabe und getrennte Ausgabeordner verwenden. Das allein belegt keine statistische Unabhängigkeit oder technische Zugriffssperre.

## Während der Erzeugung

Eine kurze technische Probe darf technische Unsicherheit klären. Anschließend zuerst eine minimale vollständige Lieferung aller geforderten Fälle exportieren und zurücklesen; danach verfeinern und Bericht schreiben. Keine vollständige generische Toolanalyse betreiben, bevor irgendein prüfbares Artefakt existiert. Der genaue Lieferplan hängt vom Auftrag ab.

Vor dem absehbaren Budgetende Checkpoint mit Lieferstatus, verbleibenden Aufgaben, Annahmen und Dateihashes schreiben. Bei einem tatsächlichen Stopp einen eigenen Event aufzeichnen. Fortsetzung in derselben Session mit neutraler Nachricht, z. B. „Setze den unveränderten Auftrag aus deinem eigenen Checkpoint fort.“ Den exakten Fortsetzungstext speichern. Neue fachliche Hinweise oder eine geänderte Priorisierung gesondert kennzeichnen; sie dürfen nicht als unveränderte Versuchsbedingung verschwinden.

Ein erfolgreicher Abschluss ist ein `complete`-Event, kein weiterer `stop`. Zwischenstände für die Forschung im vorgesehenen Checkpointordner behalten; Proben nicht still löschen. Aufbewahrung muss ohne Zugangsdaten oder andere Geheimnisse erfolgen.

## Prüfung und Fehlerbehandlung

- Quellen sind führend, nicht der visuelle Geschmack des Builders. `::placeholder` hat einen eigenen gesetzten Wert; `:disabled` am Input macht daraus keine freie Farbwahl. Eine erkannte ausdrückliche Regel darf für „bessere Unterscheidbarkeit“ nicht überschrieben werden.
- Automatische Prüfungen müssen messen und assertieren. Manuelle Urteile separat mit Beleg dokumentieren; ein konstantes `True` ist keine neu ausgeführte Prüfung. Jeder neue Prüfmechanismus bekommt einen gültigen und einen fehlerhaften Gegenfall. Stichproben als Stichproben kennzeichnen, nicht auf alle Optionen/Zustände hochrechnen.
- Benötigte Eigenschaften, für die ein Format keinen vereinbarten Kanal hat, sind `notChecked` beziehungsweise für die Freigabe dieses Umfangs `BLOCKED`; keine pauschalen A11Y-Fails oder -Passes erfinden. Ein statischer Semantikvertrag muss erst Format, Node-/Instanz-/Statebindung und Roundtrip-Nachweis festlegen. Bis dahin keine vollständige Semantikabnahme behaupten.
- Schriftfamilien-Strings sind kein Fontdatei-Nachweis. Renderer, tatsächliche Fonts, Hashes und Fallbacks festhalten, wenn Bildgleichheit bewertet werden soll. Native Werte und gerenderte Pixel getrennt berichten.
- Nach einem Fund: ID, Originalbeleg, Quellregel, Gegenfall, Ursache, aktuelle Reparatur, Regressionstest und Restgrenze in [ISSUES.md](ISSUES.md) ergänzen. Bei Wiederauftreten denselben Ursachenbezug verwenden, statt den früheren Befund zu überschreiben. Historische Ergebnisse bleiben unverändert, Korrekturen als datierter Nachtrag außerhalb des Laufs.

## Prozessdaten für den Metadatenprüfer

`tools/design-review/check_process.py` prüft folgende Struktur. Verweise sind relativ zur Prozessdatei. Die Kurzfassung ist ein **Strukturbeispiel**, keine behauptete reale Aufzeichnung; Rollen und Start-/Abschlussereignisse sind für `builderA`, `builderB`, `reviewer` jeweils auszufüllen.

```json
{
  "runId": "NEUER-LAUF",
  "definitionRevision": "SHA256_DER_EINGABEMAP",
  "toolchainLockSha256": "SHA256_DES_LOCKS",
  "comparisonPolicyId": "EINGEFRORENE_POLICY",
  "comparisonPolicy": {"path": "policy.json", "sha256": "SHA256"},
  "harnessVersion": "EXAKTE_VERSION",
  "roles": {
    "builderA": {
      "model": "MODELLNAME", "modelRevision": "REVISION", "reasoning": "STUFE_ODER_NOT_APPLICABLE",
      "harnessStepLimit": 100,
      "contextPolicy": "fresh-session; own context on continuation",
      "initialPrompt": {"path": "prompts/builder-a.txt", "sha256": "SHA256"},
      "skills": []
    }
  },
  "events": [
    {"id": "a-start", "actor": "builderA", "kind": "start", "at": "2026-10-29T10:00:00Z"},
    {"id": "a-stop-1", "actor": "builderA", "kind": "stop", "at": "2026-10-29T10:10:00Z",
     "cause": "step-limit", "stepsUsed": 100,
     "checkpoint": {"path": "checkpoints/a-1.json", "sha256": "SHA256"}},
    {"id": "a-resume-1", "actor": "builderA", "kind": "resume", "at": "2026-10-29T10:11:00Z",
     "stopId": "a-stop-1", "sameSession": true, "semanticCoaching": false,
     "message": {"path": "prompts/a-resume-1.txt", "sha256": "SHA256"}},
    {"id": "a-complete", "actor": "builderA", "kind": "complete", "at": "2026-10-29T10:20:00Z"}
  ]
}
```

Nur vorhandene, geprüfte Angaben eintragen; unbekannte Werte nicht zur erfolgreichen Metadatenprüfung erfinden. Zusätzlich nach Möglichkeit Zeit-/Tokenverbrauch und tatsächliche Skill-Read-/Zugriffsreceipts speichern. Der Prüfer bestätigt Datei-Integrität und Vollständigkeit dieser Mindestfelder, keine historische Wahrhaftigkeit, semantische Neutralität des Textes oder ausreichende technische Isolation. Eine Selbstangabe `semanticCoaching:false` muss beim Forschungsreview weiterhin am tatsächlichen Nachrichtentext geprüft werden.

Für AC-R01/02 fehlen Teile dieser Angaben dauerhaft. Das neue Protokoll repariert die zukünftige Erfassung; die verlorene historische Provenienz lässt sich damit nicht zurückholen.

## Bibliotheksauswahl

Für neue Läufe die Bibliotheks-ID und den tatsächlichen Root `libraries/<id>/` vorab festhalten. Die bisherige Forschungsdefinition liegt bytegleich unter `libraries/example/`; alte Manifeste und deren components-Locators bleiben erhalten. Eigene Bibliotheken übernehmen keine Beispiele automatisch. Pro Lauf eine explizite Quellrevision; Details zur historischen Wiederholung in [Migration](../libraries/MIGRATION.md).
