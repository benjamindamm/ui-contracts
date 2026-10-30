# SELECTION-01 · Drei gegenüber 30 Ländervorwahlen

Neue, getrennt dokumentierte Agentenstudie. [Vorabprotokoll](PROTOCOL.md) · [Studienregister](study.json) · [eingefrorene Bibliothek](library-manifest.json) · [Prüfkriterien](review/criteria.json).

Zwei frische Builder erstellen dasselbe lokale Personenformular mit unterschiedlich großen festen Länderlisten. Die Prompts geben keine Komponentenwahl vor. Fähigkeitsprofile und die deklarierte Studien-/Projektpolicy sind Teil des Frameworks. Die 15er-Suchgrenze ist eine kontrollierte Annahme, kein universelles UX-Gesetz. Die Erstentscheidung, tatsächliche Implementierung, Eignung und Policypräferenz werden getrennt bewertet.

Vorherige Komponenten und Studien bleiben erhalten; Select und Input sind neue Definitionen. Der alte 28-Datei-Bibliotheksstand liegt unter prior-library, damit ältere UX-Pilotbindungen reproduzierbar bleiben. [Originalformat- und Verhaltensvorläufe](preflight/). Kein früheres Design wird in die Aufgaben übernommen.

## Ergebnis

Beide Builder wählen entsprechend der damaligen Policy: **Select bei drei, Autocomplete bei 30 Optionen.** [Prüfbericht](review/REVIEW.md): 30 von 32 begrenzten Checks erfüllt; zwei Fehler der ersten B-Lieferung bleiben dokumentiert und wurden in einer separaten Kopie repariert. Keine allgemeine Freigabe.

**Fachliche Grenze:** Select mit Suche fehlte im Angebot. Der Lauf belegt daher keine optimale UX-Wahl. Auf Nutzerhinweis trennt die [UX-Eignungsdokumentation](../../../../../ux/AUTOCOMPLETE.md) freie Schreibhilfe von festen Auswahlwerten; [SELECTION-02](../SELECTION-02/README.md) bietet eine separate suchfähige Select-Variante. Die ursprünglichen Kriterien und Ergebnisse bleiben erhalten.

[Browseransicht A](review/screenshots/a-first.png) · [Browseransicht B, Erstlieferung](review/screenshots/b-first.png). Dies sind tatsächliche Browseraufnahmen, keine Designexporte.
