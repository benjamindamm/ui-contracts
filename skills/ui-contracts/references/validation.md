# Reale Prüfungen und begrenzte Abdeckung

Alle Projektpfade beziehen sich auf das ausgewählte Repository. Nur den benötigten Prüfweg nachladen: Originalartefakte/Bibliotheksreferenzen über `tools/libraries/check.py` und den Helper; UX-/Policy über `tools/ux/README.md`; aktuelle unterstützte Webprofile über `tools/web/README.md`; native Designs über `tools/design-review/README.md`. Nur für das historische IP01-Referenzpaket zusätzlich `docs/validation/README.md`, `tools/validation/inventory.json` und `tools/validation/README.md` laden. Der Skill dupliziert keine Erfolgskriterien.

Für native statische Designausgaben ist diese Originalformat-/Webkette keine vollständige Abnahme. Der zusätzliche, exakt gebundene Gegenprüfer unter `tools/design-review/` prüft nur seinen dokumentierten `covered`-Umfang. Lies dessen README vor Ausführung. Keine historische Reviewerdatei im Originalpfad erneut ausführen, wenn sie Belege überschreibt; temporäre Kopie verwenden. Automatische Assertions, manuelle Einordnung und `notChecked` trennen. Eine Stichprobe oder ein konstanter Wahrheitswert darf nicht als Prüfung aller Elemente erscheinen; neue Prüflogik an gültigen und fehlerhaften Gegenfällen prüfen.

## Helper aufrufen

`SKILL` bezeichnet den tatsächlichen Ordner dieses Skills; `REPO` den Repositorypfad, `CANDIDATE` die Datei/den Ordner der Originalartefakte. Ersetze diese Bezeichnungen durch konkrete Pfade, sie sind keine automatisch gesetzten Variablen.

```sh
python3 "$SKILL/scripts/contracts.py" inspect --repo "$REPO" --candidate "$CANDIDATE" --output /tmp/contract-inspection.json
python3 "$SKILL/scripts/contracts.py" validate --repo "$REPO" --scope static --output /tmp/contract-static.json
python3 "$SKILL/scripts/contracts.py" validate --repo "$REPO" --browser-run /tmp/current-ui-run --output /tmp/contract-web.json
```

`inspect` nutzt die Projektlaufzeit und Originalschemas aus dem vorhandenen Werkzeugbestand. Es prüft striktes JSON, CEM 2.1.0 beziehungsweise SCXML 1.0, CSS-Syntax und HTML-Parsebarkeit soweit passend. Für component.json/library.json ergänzen eigene Mindestschemas die begrenzte Referenz-/Identitäts-/Aliasprüfung. Andere JSON-Dokumente bleiben Syntaxprüfungen. HTML-Parsebarkeit bedeutet keine HTML-/ARIA-Konformität. Fehlende Quellziele, falsche Zielarten, doppelte Identitäten und Kompositionszyklen werden zusätzlich konkret geprüft. Guards, beliebige Typsemantik, CSS-Tokenabbildung und vollständige Ownership bleiben außerhalb dieser Teilprüfung. Daher endet eine sonst gültige neue Komponente weiterhin mit `BLOCKED`/`SEMANTIC_PROFILE_UNSUPPORTED` und separat bestandenen Teilprüfungen.

`validate` ruft unverändert `tools/validation/check.py` mit dem gewählten Paket/Umfang auf und übernimmt dessen Ergebnis. Die unterstützte Referenz liegt unter `docs/research/experiments/2026-10-25/ip01-static/reference/`; `--candidate` bedeutet hier eine Kopie dieses vollständigen Pakets. Eine Bibliothek unter `libraries/<id>/` ist ein anderes Autorenartefakt und darf nicht allein durch passende Ordnernamen zu diesem Profil erklärt werden.

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

Für Originalartefakte einer ausdrücklich ausgewählten Bibliothek: `inspect --library ID` ohne `--candidate`. Kein Default auf example. `validate --library` ist absichtlich nicht unterstützt; die Referenzpaketprüfung ist keine allgemeine Bibliotheksabnahme.

Für UX-Eignung bzw. Auswahl: [UX-Referenz](ux.md) gezielt laden. Die neuen Tools unter tools/libraries/check.py und tools/ux/ arbeiten mit der ausdrücklich gewählten Bibliothek; sie ersetzen weder das historische Referenzprofil noch die Zielabnahme. Fehler bleiben FAIL, auch wenn eine spätere Zusatzprüfung nicht unterstützt ist.

## Aktuelle Bibliotheksprofile

Für die vier aktuell unterstützten Profile gibt es zusätzlich den gezielt ladbaren Repository-Einstieg `tools/web/README.md`: `tools/web/prepare.py --library ID --out NEUER_ORDNER`, `serve.py`, fünf BrowserOS-Skripte und `tools/test.py --browser-run LAUF --out NEUER_ORDNER`. Er erzeugt eigene aktuelle Quellenbindungen und prüft reale Events, Fokus und Scrollgeometrie. Er erweitert **nicht** das historische IP01-Referenzprofil oder `validate --library`; beliebige neue Komponenten bleiben außerhalb seiner Abdeckung. Neue native Profile und Browseradapter benötigen eigene konkrete Gegenfälle.

## Korrigieren und berichten

Syntax-/Schema-/Bindungsfehler bleiben Fehler. Kandidatendaten dürfen repariert werden; danach betroffene Prüfungen erneut ausführen. Originalschemas, Assertions, Kriterien sowie Quell-/Zeitbindungen nicht passend lockern. Ein tatsächlich fehlerhafter Prüfer braucht einen eigenen belegten Gegenfall und eine nachvollziehbare neue Prüferrevision.

Ergebnis mit Artefaktpfaden/Revision, tatsächlich ausgeführten Prüfungen und Belegdateien, bestandenem Umfang, Fehlern/Blockern, Warnungen und ungeprüften Teilen liefern. Helperberichte inhaltlich prüfen, nicht nur den Exitcode. Bei contracts.py: 0 für den ausdrücklich begrenzt bestandenen Umfang, 1 für Fehler, 2 für Blockierung. Ein blockierter Entwurf darf als Entwurf übergeben werden, nicht als freigegebene Komponente. Im historischen IP01-Webprofil bleibt `releaseScope:exact-pinned-bounded-web-reference-only` und `productionRelease:false`; diese Bindung nicht auf beliebige neue Ziele übertragen.
