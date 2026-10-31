# Aktueller Web-Prüfhost

Der Host ist ein **begrenzter Adapter für vier ausdrücklich unterstützte Profile**, kein universeller Webgenerator. Er unterstützt ausdrücklich die geprüfte Dateikonvention (interface.json, behavior.scxml, accessibility.html, bei Autocomplete zusätzlich die gebundene layout.css/rules-Datei und Root-Tokens); abweichende Domainpfade werden abgewiesen, nicht still durch ähnlich benannte Dateien ersetzt. Bibliothek immer angeben; er übernimmt HTML-Vorlagen, die tatsächlichen SCXML-Dateien und bei Autocomplete DTCG/CSS samt Overlay/ScrollArea. Die anderen drei Adapter prüfen Verhalten und Semantik, keine vollständige visuelle Umsetzung.

```sh
python3 tools/setup.py
# JDK 17+ und Node.js 22+ müssen vorhanden sein; bei Bedarf --java PFAD.
tools/validation/.venv/bin/python tools/web/prepare.py --library example --out .runtime/web-run
python3 tools/web/serve.py --run .runtime/web-run --port 8770
```

Dann über BrowserOS neo einen **eigenen Tab** für `http://127.0.0.1:8770/` öffnen. [Browserablauf](browseros/README.md) und fünf nummerierte Skripte ausführen. `cases.json` legt die erwarteten Fälle vorab fest. Bei anderer Portwahl die explizite URL in den Skripten ersetzen. Neue Wiederholung = neues Ausgabeverzeichnis; Collector verweigert überschriebene Captures.

```sh
python3 tools/test.py --browser-run .runtime/web-run --out .runtime/test-run
```

Der gemeinsame Testbefehl führt Quellen-, native SCXML-, DMN-, Font-, Design-, Handoff-, Chart-, Layout- und Setupregressionen sowie den Browsergegencheck aus. Ohne Browserbeleg bleibt der volle Auftrag blockiert. `--unit-only` grenzt den Auftrag ausdrücklich auf Tests ohne Browser ein. Alle Ergebnisse bleiben `release:false`.

Die Bindung enthält Bibliotheksrevision, Host-/Werkzeughashes, Lauf-Challenge und eingefrorene Browserfälle. Der Host prüft die geladenen Bytes. Der externe Checker wertet rohe Events, Zustände, Fokus, reale DOM-Messungen und den Browser-Accessibility-Baum aus; ein behauptetes „pass“ wird nicht übernommen. Gegenfälle verändern Kopien: falscher Commitwert, fehlende Messung, synthetisches Keyboardjournal, falscher Fokus, fehlender AX-Baum, veränderte Hostdatei und wiederverwendete Challenge müssen scheitern.

**Vertrauensgrenze:** Das ist ein lokaler Testharness mit Agent/Browserprotokoll, keine kryptografische Attestierung gegen einen Angreifer, der sämtliche Dateien und Prüfer gemeinsam verändert. Providerantworten und Host-Properties werden absichtlich als Fixtures geliefert; Tastatur-/Formularhandlungen erfolgen über den Browser. Ein synthetisches `MEASURED` im nativen Contracttest ist ausdrücklich **kein** Scrollbeleg; nur der Browserlauf misst Geometrie.

Nicht abgedeckt: reale IME, Screenreader-Ausgabe, Pixelgleichheit, andere Browser/Betriebssysteme, beliebige neue Komponentenprofile oder Produktionsfreigabe. Der Browserhost lädt ausführbare ECMAScript-Ausdrücke aus der ausdrücklich gewählten Bibliothek; nur vertrauenswürdige Contracts verwenden.

Historische Experimente bleiben unverändert und werden nicht durch neue Quellen ersetzt. Die aktuelle Implementierung nutzt deren eigenen Isolationsansatz als Ausgangspunkt, mit neuen Quellenbindungen und erneuter Prüfung.

[CI](../../.github/workflows/contracts.yml) führt ausdrücklich nur `--unit-only` mit den nativen Engines aus. Die Workflowdefinition ist bereitgestellt; ein erfolgreicher GitHub-/Linux-Lauf wird erst nach tatsächlicher Ausführung behauptet. Browserbelege werden dort weder simuliert noch aus Forschungsarchiven übernommen.
