# Unabhängige Projektgegenprüfung · 31. Oktober 2026

## Auftrag und Umfang

Unabhängiger Worker ohne Elternhistorie. Repositoryweit risikoorientiert geprüft wurden Einstieg, Informationsarchitektur, vier führende Domänen, Bibliotheksstruktur, UX-Quellen-/Policyanbindung, Validierungsgrenzen und Forschungsprovenienz. Keine Bibliothek wurde für Erstellung oder Änderung ausgewählt; `example` wurde ausdrücklich nur als vorhandene Prüfeingabe in einer isolierten Gegenprobe verwendet. Keine bestehenden Dateien verändert; kein Commit/Push. Vorgefundener Arbeitsbaum: `docs/research/DOCUMENT-INDEX.md` bereits geändert und `docs/research/analyses/AI-ELEMENTS-FIT-2026-10-31/` ungetrackt. Diese Änderungen stammen nicht aus dieser Prüfung.

Gezielt gelesen: AGENTS.md, docs/README.md, README.md, docs/ARCHITECTURE.md, docs/STATUS.md, libraries/README.md, aktive library.json/Input-component.json, Repository-Skill, Autoren-/Validierungsanleitung, tools/ux/README.md und WORKFLOW.md, tools/web/README.md und prepare.py, Bibliothekschecker/-schemas/-tests, manage.py, gemeinsamer Testtreiber, Navigationstool/-tests, STUDIES.md, RD-002 sowie aktueller Übernahmebericht und früherer Frameworkaudit als Gegenbelege. Historische Auditbefunde wurden nicht unbesehen als aktuelle Fehler übernommen.

## Befunde

### IA-01 · P2 · Aliasabschluss wird trotz fehlenden Aliasziels gemeldet

- **Datei/Zeile:** `tools/libraries/check.py:99` und `:108`; Sammellogik `:87–91`.
- **Beobachtung:** `resolve()` folgt Aliasstrings nur, wenn der komplette `$value` ein String ist. Objekt-/Arraywerte werden unverändert zurückgegeben. Trotzdem wird für die Datei `kind: token-alias-closure` ausgegeben. Ein hinzugefügtes Shadow-Token mit `color: "{does.not.exist}"` innerhalb seines `$value` wird akzeptiert. Der direkte Alias auf dasselbe fehlende Ziel wird dagegen mit `TOKEN_ALIAS_MISSING` abgewiesen. Der vollständige Bibliothekscheck der isolierten Kopie meldet `PASS_LIMITED`, 6 Komponenten und keine Fehler.
- **Interpretation:** Die tatsächlich geprüfte Aliasform ist enger als der unqualifizierte Closure-Nachweis. Die aktuellen Dokumente weisen CSS-Abbildung und allgemeine Semantik als Grenzen aus, nennen aber keine Begrenzung auf vollständige skalare Aliaswerte. Eine gezielte Diagnose „zusammengesetzter Tokenwert nicht unterstützt“ wäre ebenfalls korrekt; ein universeller Tokenvalidator ist dafür nicht nötig.
- **Auswirkung:** Neue visuelle Quellen können fehlende Verbindungen behalten, obwohl ihr Bericht Aliasabschluss suggeriert. Keine Produktionsfreigabe umgangen; der heutige Beispielbestand ist dadurch nicht als fehlerhaft nachgewiesen.
- **Reproduktion/Beleg:** Mit dem vorhandenen Python aus `tools/validation/.venv` `Inspector.tokens()` einmal auf `{"bad":{"$type":"color","$value":"{does.not.exist}"}}` und einmal auf `{"bad":{"$type":"shadow","$value":{"color":"{does.not.exist}","offsetX":{"value":0,"unit":"px"},"offsetY":{"value":0,"unit":"px"},"blur":{"value":0,"unit":"px"},"spread":{"value":0,"unit":"px"}}}}` anwenden. Zweite Probe zusätzlich als neues Token in eine Kopie der aktiven Bibliothek einfügen und `inspect(copy, repo)` ausführen. Ergebnisse: [kleine Gegenprobe](independent-alias-probe.json), [vollständiger Kopiencheck](independent-full-library-probe.json). Kopie unter `.runtime/independent-audit/alias-probe/library-copy/`.
- **Lösungsvorschlag:** Unterstützte Aliaspositionen in zusammengesetzten Werten explizit rekursiv prüfen oder diese Wertformen als nicht unterstützt diagnostizieren. Namen/Umfang des ausgegebenen Abschlussnachweises daran anpassen. Positive/negative Gegenfälle für nested Aliasziele ergänzen; keine pauschale semantische Vollprüfung behaupten.
- **Nachweisgrenze:** Nur fehlendes Ziel in einem Objektwert ausgeführt; verschachtelte Zyklen, Arrays, alle DTCG-Typregeln und tatsächliches Rendering nicht ausgeführt. Keine Aussage, dass ein produktiver Zieladapter dieses zusätzliche Token verwendet.

### IA-02 · P3 · Aktiver Bibliotheksindex beschreibt Webziel als späteres Vorhaben

- **Datei/Zeile:** `libraries/example/library.json:16`.
- **Beobachtung:** `targets.web` lautet „HTML and TypeScript generated from these same definitions in a later comparison.“ Der aktuelle Web-Einstieg und docs/STATUS.md beschreiben dagegen bereits vorhandene, ausgeführte Adapterbelege für vier unterstützte Profile.
- **Interpretation:** Dies ist veraltete beziehungsweise zu unspezifische aktive Metadatenprosa, kein Nachweis eines defekten Adapters. Der Index ist für Autoren eine zentrale nachzuladende Quelle; die tatsächlichen Nachweisgrenzen sind in STATUS und Web-README genauer.
- **Auswirkung:** Ein Agent kann den vorhandenen begrenzten Webprüfweg aus der aktiven Bibliotheksquelle allein nicht erkennen und ihn unnötig als Zukunftsumfang behandeln.
- **Reproduktion/Beleg:** Textvergleich des aktiven library.json mit `docs/STATUS.md` (Zeile Einrichtung und Web) und `tools/web/README.md` (erster Absatz). Keine Ausführung nötig.
- **Lösungsvorschlag:** In einer neuen aktiven Bibliotheksrevision den verfügbaren begrenzten Webadapter und seinen operativen Einstieg referenzieren; allgemeine Generierung weiterhin als offen benennen. Historische Indizes unverändert lassen.
- **Nachweisgrenze:** Kein beobachteter Agentenfehler aufgrund dieser Prosa; P3-Dokumentationsbefund.

## Tatsächlich ausgeführte Prüfungen

1. Gitstatus nur lesend erfasst; Dateiinventare und relevante Dateien mit rg/Lesebefehlen untersucht.
2. Eigenständige lokale Markdown-Dateizielprüfung über getrackte Markdown-Dateien außerhalb `examples/`, historischer Analyse-/Studien-/Experimentordner und `docs/libraries/frozen/`: 0 fehlende Dateiziele. Gesamtinventar des Suchbefehls 285 Markdown-Dateien; dies ist keine Behauptung, alle 285 Inhalte gelesen zu haben. Anker, externe Links und bloße Textpfade wurden nicht geprüft.
3. `python3 tools/research/navigation.py --output .runtime/independent-audit/navigation.json`: `PASS_LIMITED`, keine Fehler der aktiven Einstiegsrouten. Tool weist seinen engen Umfang selbst aus.
4. Direkter Alias-Gegenfall verworfen; verschachtelter Gegenfall akzeptiert. Vollständiger Bibliothekschecker auf isolierter Kopie: `PASS_LIMITED`, 6 Komponenten. Nur `.runtime/independent-audit/` und die neuen Berichtsdateien beschrieben.

## Gegenbelege und nicht als Fehler gewertete Punkte

Vier Domänen und eigene Bindungskonventionen sind in den aktuellen Einstiegstexten klar getrennt. Beispielbibliothek wird nicht automatisch für neue Aufgaben gewählt. Historische Definitionen und moderne aktive Revisionen sind ausdrücklich getrennt; alte feste Toolpfade allein wurden deshalb nicht als aktueller Setupfehler gewertet. Native SCXML-, Browsergeometrie-, Accessibility-Baum- und Screenreadernachweise werden nachvollziehbar auseinandergehalten. STUDIES.md verlangt Metadaten für künftige Forschungsstudien; RD-002 entlastet normale Aufgaben und wahrt kontrollierte Studienbedingungen. Dies ist kein bestätigter Widerspruch. Das Navigationstool verspricht ausdrücklich keine rekursive historische Linkprüfung. Aktuelle Dokumente geben begrenzte Prüferfolge nicht als allgemeine Produktionsfreigabe aus.

## Nicht geprüft / Gesamturteil

Kein erneuter BrowserOS-, IME-, Screenreader-, Linux-CI-, Font-/OpenPencil-Rendering- oder kompletter Modellstudienlauf. Keine Wiederholung sämtlicher Regressionen; diese Prüfung ergänzt den koordinierten Hauptaudit. Keine vollständige Inhaltslektüre oder Hash-Neuverifikation aller historischen Archive. Externe Originalstandards und Weblinks nicht live erneut geladen. Hardware-, Host- und installierter Skillvergleich nicht ausgeführt.

**Gesamturteil:** Die aktuelle Architektur und ihre Einstiege sind überwiegend konsistent und formulieren ihre wesentlichen Grenzen deutlich. Eine reproduzierte Aliasprüflücke und eine kleinere aktive Metadatenabweichung bleiben. Dieses Urteil ist ein begrenzter Projektgegencheck und keine allgemeine Freigabe. [Quellhashes](independent-source-hashes.json) binden die entscheidenden Dateien zum Prüfzeitpunkt.
