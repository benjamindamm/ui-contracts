# Lauf 01 · Native Teilproben und eigener Bindungsadapter

30. Oktober 2026. **39 Beobachtungschecks, 38 Erwartungen erfüllt, ein unerfüllter Gegenfall.** [Zusammenfassung](results/summary.json) · [Einzelchecks](results/checks.json). Das ist kein vollständiger Zwölf-Fälle-Benchmark und kein allgemeiner Frameworkvergleich mit Sieger.

## Reproduzieren

```sh
npm ci --prefix docs/research/studies/UX-RULES-01/runs/01 --ignore-scripts --no-audit --no-fund
python3 -m venv /tmp/ux-rule-probe-env
/tmp/ux-rule-probe-env/bin/pip install -r docs/research/studies/UX-RULES-01/runs/01/requirements-lock.txt
```

OPA 1.21.2 darwin/arm64 wurde aus dem offiziellen Release geladen; URL, Hash, Plattform und Version stehen im Werkzeugnachweis. Binärdatei außerhalb Git. Ein erneuter Messlauf braucht eine neue Ergebniskopie: `probe.py` erstellt results exklusiv und überschreibt diese Beobachtungen nicht. `OPA=/pfad/opa` setzt den lokalen Binärpfad. Auf einem anderen System passende OPA-Binärdatei und deren Hash separat erfassen. Das Python-Lock bindet Versionen, ist aber kein plattformunabhängiges, vollständig hashgepinntes Wheelarchiv.

## Tatsächlich ausgeführt

- FEEL: sechs Faktenkontexte für rohe Bedingung, explizite Ausgabepolicy und zusätzliche Typabsicherung; negative Syntaxprobe. feelin ist ein FEEL-Interpreter, keine vollständige DMN-Engine.
- DMN: das eigene XML-Literalmodell gegen unveränderte Original-XSDs validiert; Gegenfall mit unerlaubtem Attribut abgewiesen. Die FEEL-Datei und das DMN-XML enthalten denselben ursprünglichen Ausdruck, aber kein vollständiger DMN-Modelllauf wurde ausgeführt.
- Rego: sechs Kontexte mit eigener Proberegel; native undefinierte Ausgabe und widersprüchliche Ergebnismenge beobachtet. Keine native UX-Verbindlichkeits- oder Ausnahmeauflösung behauptet.
- SHACL: sechs über eine eigene Projektion erzeugte RDF-Kontexte; zusätzlich Warning mit und ohne pySHACL-Option allow_warnings. Die Fehlend/null-Darstellung ist unsere Testkonvention, kein universeller RDF-Standard für UX.
- SBVR: offizielles XSD mit lokal aufgelöstem originalem XMI-Import kompiliert. Kein semantischer SBVR-Evaluator und kein vollständiges SBVR-Regelmodell ausgeführt.
- Bindung: eigener Adapter prüft vier Originaldomänen der example-Komponente sowie Fremdbibliothek, falsche ID/Revision, fehlenden Anker, falschen Wert, Pfadausbruch und mutierte Quelle. Kein Framework kann sich diese eigene Leistung als native Funktion zurechnen lassen.

## Unerfüllte Erwartung und erhaltene Reparatur

Die Rego-Proberegel liefert bei fehlendem existingEntriesOnly **unsuitable statt unknown**. Ursache ist die unzureichende eigene Guard-/Else-Konstruktion, kein Beweis eines OPA-Fehlers. Originalregel, Rohantwort, Exitcodes und fehlgeschlagener Check bleiben unverändert. [Lauf 02](../02/README.md) prüft eine separate Korrektur.

Der untypisierte FEEL-Ausdruck klassifiziert den String "true" ebenfalls ungeeignet; die zusätzliche typisierte Variante meldet invalid-input. Das ist eine beobachtete Notwendigkeit expliziter Typregeln, kein bestandenes UX-Urteil. Fehlende Variable und explizites null liefern beide null, unterscheiden sich hier aber in den Warnungen. Diese Diagnostik muss erhalten bleiben.

## Versuchsgrenzen

T01–T04 teilweise in den drei Engines, T06 nur widersprüchliche Rego-Ergebnismenge, T07–T10 mit eigenem Binder. T05, T11 und T12 noch nicht ausgeführt. Schemaprüfung, Engineausgabe und eigener Adapter sind getrennt. Modelleignung, vollständige Konformität, fachliche UX-Wahrheit, Lizenzfreigabe und Agentenverhalten nicht daraus ableiten.

Der Inputfreeze erfolgte nach offengelegter explorativer Vorbereitung, nicht blind vor Kenntnis aller Engineeffekte. Ein anfänglicher eigener Fehler beim Auffangen der negativen Syntaxprobe steht in preflight-issue.json. Originalschemas wurden bytegleich gespeichert; lokale Auflösung des XMI-Imports verändert das Schema nicht. Laufzeitaufrufe verwenden lokale Dateien; Netzwerkabwesenheit wurde nicht instrumentell bewiesen.
