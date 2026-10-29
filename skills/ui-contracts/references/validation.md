# Reale Prüfungen und begrenzte Abdeckung

Alle folgenden Projektpfade beziehen sich auf das ausgewählte Repository. Zuerst `docs/validation/README.md`, `tools/validation/inventory.json` und bei Ausführung `tools/validation/README.md` lesen. Diese Dateien führen tatsächliche Abdeckung, Abhängigkeiten und Aufrufe; der Skill dupliziert keine Erfolgskriterien.

Für native statische Designausgaben ist diese Originalformat-/Webkette keine vollständige Abnahme. Der zusätzliche, exakt gebundene Gegenprüfer unter `tools/design-review/` prüft nur seinen dokumentierten `covered`-Umfang. Lies dessen README vor Ausführung. Keine historische Reviewerdatei im Originalpfad erneut ausführen, wenn sie Belege überschreibt; temporäre Kopie verwenden. Automatische Assertions, manuelle Einordnung und `notChecked` trennen. Eine Stichprobe oder ein konstanter Wahrheitswert darf nicht als Prüfung aller Elemente erscheinen; neue Prüflogik an gültigen und fehlerhaften Gegenfällen prüfen.

## Helper aufrufen

`SKILL` bezeichnet den tatsächlichen Ordner dieses Skills; `REPO` den Repositorypfad, `CANDIDATE` die Datei/den Ordner der Originalartefakte. Ersetze diese Bezeichnungen durch konkrete Pfade, sie sind keine automatisch gesetzten Variablen.

```sh
python3 "$SKILL/scripts/contracts.py" inspect --repo "$REPO" --candidate "$CANDIDATE" --output /tmp/contract-inspection.json
python3 "$SKILL/scripts/contracts.py" validate --repo "$REPO" --scope static --output /tmp/contract-static.json
python3 "$SKILL/scripts/contracts.py" validate --repo "$REPO" --browser-run /tmp/current-ui-run --output /tmp/contract-web.json
```

`inspect` nutzt die Projektlaufzeit und Originalschemas aus dem vorhandenen Werkzeugbestand. Es prüft striktes JSON, CEM 2.1.0 beziehungsweise SCXML 1.0, CSS-Syntax und HTML-Parsebarkeit soweit passend. Andere JSON-Dokumente bleiben Syntaxprüfungen. HTML-Parsebarkeit bedeutet keine HTML-/ARIA-Konformität. Kein generischer Behavior-/Kompositions-/Ownershipprüfer für neue Komponenten wird behauptet. Daher endet eine sonst gültige neue Komponente weiterhin mit `BLOCKED`/`SEMANTIC_PROFILE_UNSUPPORTED` und separat bestandenen Teilprüfungen.

`validate` ruft unverändert `tools/validation/check.py` mit dem gewählten Paket/Umfang auf und übernimmt dessen Ergebnis. Die unterstützte Referenz liegt unter `docs/research/experiments/2026-10-25/ip01-static/reference/`; `--candidate` bedeutet hier eine Kopie dieses vollständigen Pakets. Die neue `components/`-Bibliothek ist ein anderes Autorenartefakt und darf nicht allein durch passende Ordnernamen zu diesem Profil erklärt werden.

Fehlende Projektlaufzeit oder fehlende notwendige Prüfer blockieren. Abhängigkeiten nur nach der Projektanleitung bereitstellen; kein unbekanntes Werkzeug als Ersatzvalidator ausgeben.

## Reihenfolge

1. Standards, Versionen, erforderliche Prüfer und unterstützten Umfang festlegen.
2. JSON/XML und tatsächliche Originalschemas prüfen; verbleibende Regeln ausweisen.
3. Referenzen, Zielarten, Typen, Einheiten, Events und Instanzkontext.
4. Ownership, Ableitung, Konflikte, Komposition und erforderlichen Lifecycleumfang.
5. Gemeinsame Verhaltensfälle mit tatsächlichen Events, Fokus, Scrollmessung und AX.
6. Strukturiert berichten; fehlende notwendige Schritte verhindern die entsprechende Freigabe.

Nur ausdrücklich angeforderte Teilprüfungen dürfen ohne vollständige Kette begrenzt erfolgreich heißen. Fehlende notwendige Prüfung niemals als bestandene Prüfung behandeln.

## Aktuellen Browsernachweis erzeugen

Der installierte BrowserOS-neo-Workflow ist hierfür der tatsächlich unterstützte Browserweg. Ist BrowserOS neo nicht verfügbar, bleibt die Webprüfung blockiert. Kein erfundener/headless Ersatzlauf.

Mit der Projektlaufzeit `tools/validation/.venv/bin/python`:

- `tools/validation/browser_gate.py prepare --run-dir NEUER_ORDNER` bindet exakte Paket-/Hostrevision und aktuelle Prüfer. Für eine andere Kandidatenkopie deren `--package` explizit übergeben; die feste Hostzuordnung ist dadurch nicht erweitert.
- `serve --run-dir NEUER_ORDNER` startet den eigenen lokalen Collector und erzeugt vier Browser-SDK-Skripte.
- Eigene Seite an der ausgegebenen URL öffnen, auf `body[data-ready="true"]` warten und die vier `browser-01.js` bis `browser-04.js` nacheinander als BrowserOS-`run` ausführen. Nicht mit Node starten und keine erforderlichen Assertions auslassen.
- Nach erfolgreichen Operationsreceipts `finalize --run-dir NEUER_ORDNER`; anschließend Helper `validate --browser-run NEUER_ORDNER`. Den eigenen Server danach beenden.

Die Prüfkette akzeptiert nur den explizit übergebenen, frischen, vollständigen und quellen-/prüfergleichen Lauf. Die aktuelle maximale Gültigkeit steht im Browserprofil (derzeit zwei Stunden ab Vorbereitung). Keine alten Captures umbenennen, keinen Zeitstempel zurücksetzen und keinen fehlgeschlagenen Lauf teilweise weiterführen. Nach relevanter Reparatur einen neuen Lauf beginnen.

Der zusätzliche Browserhost ist keine allgemeine Generierung aus jeder Definition. Eine statisch gültige Änderung braucht eine eigene begründete Host-/Profilabbildung und aktuelle Abnahme; der bestehende Skill stellt diese noch nicht bereit. Das ist ein blockierender Umfangsbefund, keine Aufforderung, die feste Profilbindung für die Reparatur zu lockern.
