# AC-R01 · Einstieg für weiterarbeitende Agenten

## Lesereihenfolge und Zuständigkeit

1. [Studienbericht](README.md): Ergebnis, Aussagekraft und Grenzen. Beide Designs erhalten FAIL; gemessene Paarübereinstimmung ist kein Konformitätsnachweis.
2. [Protokoll](PROTOCOL.md): Rollen, zulässige Eingaben, Zeitordnung und Kontexttrennung.
3. [Laufmetadaten](../../../../examples/autocomplete/reproducibility/run-01/run.json): eingefrorene Definition, Einzelhashes, Werkzeugbindung und Lieferungen.
4. [Vorabkriterien](../../../../examples/autocomplete/reproducibility/run-01/review/preregistered.md) und ihr Siegel: maßgebliche Erwartungen vor Einsicht des Prüfers in die Ausgaben.
5. [Unabhängiges Review](../../../../examples/autocomplete/reproducibility/run-01/review/REVIEW.md), danach Ergebnisdaten und Originalreader-Auszüge. Builderberichte sind Selbstauskünfte und ersetzen die unabhängige Prüfung nicht.

Die führende semantische Eingabe liegt in [components/](../../../../components/README.md). `run.json` bindet alle 22 Dateiversionen; vor Weiterarbeit deren Hashes prüfen. Die Revision ist eingefroren. Kriterien, Builderausgaben und Review sind historische Belege und bleiben unverändert. Neue Definitionen oder Erzeugungen erhalten eine neue Version beziehungsweise einen neuen Lauf. Die ältere Kandidatenrecherche hat eigene Zählungen und wird nicht um die Einzelbeobachtungen dieser Studie erweitert.

## Dateien richtig einordnen

- `autocomplete.fig`: tatsächliches natives Ergebnis; `preview.*`: Darstellung des Builders.
- `generate.mjs`: Generierung des jeweiligen Builders; `checks.json`: dessen eigene Prüfungen.
- `original-*.json`: mit dem Originalreader aus den gespeicherten FIG-Dateien gelesene Knoten.
- `render-*.png`: separat durch den Prüfer erzeugte Originalrenders.
- `native-checks.json`: einzelne tatsächliche Soll-/Ist-Vergleiche; `normalized-*.json`: erfasste Komponentenwerte für den Paarvergleich.
- `results.json`: ausgearbeitete Urteile einschließlich manueller Einordnung und Grenzen. Das Prüfskript allein ersetzt diesen Bericht nicht.
- `hashes.json`: versiegelte Review-Belege; `evidence-manifest.json`: abschließendes Gesamtinventar der Studie, ohne sich selbst.
- `native-css-control.json`: zusätzliche Kontrolle nach dem Review, ausdrücklich kein vorab registrierter Bestandteil.

## Nachvollziehen und erneut ausführen

Lesen und Hashvergleich benötigen Python 3. Für die Originalreader-/Render-Skripte wurde Node.js 24 mit der gepinnten [Werkzeugkonfiguration](../../../../tools/openpencil/package.json) und dem [Lockfile](../../../../tools/openpencil/package-lock.json) verwendet. Abhängigkeiten lassen sich im Werkzeugordner mit `npm ci` installieren. Native Renderer benötigen außerdem ihre Laufzeitabhängigkeiten und Fonts; gleiche Hashes der Eingabe garantieren keine pixelidentische Rasterung auf jeder Umgebung.

**Erneute Skriptläufe nur in einer separaten Kopie des Repositorys:** `generate.mjs` überschreibt Builderdateien; `inspect-original.mjs`, `render-original.mjs` und `verify.py` überschreiben Review-Belege. Die ursprüngliche Evidenz und deren Hashes nicht durch einen Nachlauf ersetzen. Vom Stamm der Kopie aus ist die Reihenfolge für den technischen Review:

```sh
node examples/autocomplete/reproducibility/run-01/review/inspect-original.mjs
node examples/autocomplete/reproducibility/run-01/review/render-original.mjs
python3 examples/autocomplete/reproducibility/run-01/review/verify.py
```

Dies wiederholt die technische Auswertung, nicht das unabhängige Erzeugungsexperiment und nicht die manuelle Betrachtung. Ein echter neuer Versuch braucht neue Agenten mit leerem Kontext und einen eigenen Ausgabeordner. Wer die vorhandenen Lösungen gelesen hat, erfüllt diese Bedingung für einen Builder nicht mehr.

## Vollständiges Dateiverzeichnis

Alle fachlichen Dateien dieses Studienpakets sind unten direkt verlinkt. Installierte Abhängigkeiten und Betriebssystemdateien gehören nicht zum Studienkorpus. Der Hashmanifest ist die maschinenlesbare Ergänzung; er ist keine zweite Ergebnisquelle.

| Datei | Bereich |
| --- | --- |
| [docs/research/studies/AC-R01/PROTOCOL.md](PROTOCOL.md) | Studienaufbereitung |
| [docs/research/studies/AC-R01/README.md](README.md) | Studienaufbereitung |
| [docs/research/studies/AC-R01/evidence-manifest.json](evidence-manifest.json) | Studienaufbereitung |
| [docs/research/studies/AC-R01/native-css-control.json](native-css-control.json) | Studienaufbereitung |
| [examples/autocomplete/reproducibility/run-01/README.md](../../../../examples/autocomplete/reproducibility/run-01/README.md) | Laufrahmen |
| [examples/autocomplete/reproducibility/run-01/builder-a/REPORT.md](../../../../examples/autocomplete/reproducibility/run-01/builder-a/REPORT.md) | Builder A |
| [examples/autocomplete/reproducibility/run-01/builder-a/autocomplete.fig](../../../../examples/autocomplete/reproducibility/run-01/builder-a/autocomplete.fig) | Builder A |
| [examples/autocomplete/reproducibility/run-01/builder-a/checks.json](../../../../examples/autocomplete/reproducibility/run-01/builder-a/checks.json) | Builder A |
| [examples/autocomplete/reproducibility/run-01/builder-a/generate.mjs](../../../../examples/autocomplete/reproducibility/run-01/builder-a/generate.mjs) | Builder A |
| [examples/autocomplete/reproducibility/run-01/builder-a/preview.png](../../../../examples/autocomplete/reproducibility/run-01/builder-a/preview.png) | Builder A |
| [examples/autocomplete/reproducibility/run-01/builder-a/source-sha256.json](../../../../examples/autocomplete/reproducibility/run-01/builder-a/source-sha256.json) | Builder A |
| [examples/autocomplete/reproducibility/run-01/builder-b/REPORT.md](../../../../examples/autocomplete/reproducibility/run-01/builder-b/REPORT.md) | Builder B |
| [examples/autocomplete/reproducibility/run-01/builder-b/autocomplete.fig](../../../../examples/autocomplete/reproducibility/run-01/builder-b/autocomplete.fig) | Builder B |
| [examples/autocomplete/reproducibility/run-01/builder-b/checks.json](../../../../examples/autocomplete/reproducibility/run-01/builder-b/checks.json) | Builder B |
| [examples/autocomplete/reproducibility/run-01/builder-b/generate.mjs](../../../../examples/autocomplete/reproducibility/run-01/builder-b/generate.mjs) | Builder B |
| [examples/autocomplete/reproducibility/run-01/builder-b/preview.png](../../../../examples/autocomplete/reproducibility/run-01/builder-b/preview.png) | Builder B |
| [examples/autocomplete/reproducibility/run-01/builder-b/preview.svg](../../../../examples/autocomplete/reproducibility/run-01/builder-b/preview.svg) | Builder B |
| [examples/autocomplete/reproducibility/run-01/review/REVIEW.md](../../../../examples/autocomplete/reproducibility/run-01/review/REVIEW.md) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/hashes.json](../../../../examples/autocomplete/reproducibility/run-01/review/hashes.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/inspect-original.mjs](../../../../examples/autocomplete/reproducibility/run-01/review/inspect-original.mjs) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/native-checks.json](../../../../examples/autocomplete/reproducibility/run-01/review/native-checks.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/normalized-a.json](../../../../examples/autocomplete/reproducibility/run-01/review/normalized-a.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/normalized-b.json](../../../../examples/autocomplete/reproducibility/run-01/review/normalized-b.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/original-a.json](../../../../examples/autocomplete/reproducibility/run-01/review/original-a.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/original-b.json](../../../../examples/autocomplete/reproducibility/run-01/review/original-b.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/preregistered.json](../../../../examples/autocomplete/reproducibility/run-01/review/preregistered.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/preregistered.md](../../../../examples/autocomplete/reproducibility/run-01/review/preregistered.md) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/preregistration-seal.json](../../../../examples/autocomplete/reproducibility/run-01/review/preregistration-seal.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/render-a.png](../../../../examples/autocomplete/reproducibility/run-01/review/render-a.png) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/render-b.png](../../../../examples/autocomplete/reproducibility/run-01/review/render-b.png) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/render-original.mjs](../../../../examples/autocomplete/reproducibility/run-01/review/render-original.mjs) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/results.json](../../../../examples/autocomplete/reproducibility/run-01/review/results.json) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/review/verify.py](../../../../examples/autocomplete/reproducibility/run-01/review/verify.py) | Unabhängige Prüfung |
| [examples/autocomplete/reproducibility/run-01/run.json](../../../../examples/autocomplete/reproducibility/run-01/run.json) | Laufrahmen |
| [docs/research/studies/AC-R01/AGENT-GUIDE.md](AGENT-GUIDE.md) | Studienaufbereitung |
