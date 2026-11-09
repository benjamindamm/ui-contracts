# Lokaler Reader für Figma-Exporte

Der optionale [figma-reader v0.4.2](https://github.com/LeoGCode/figma-reader/tree/v0.4.2) liest vorhandene `.fig`-Dateien. Die Installation braucht Node.js ab 22 und npm. Version und Abhängigkeiten sind hier separat gepinnt.

## Benutzung

Vom Repository-Stamm aus ausführen. Die Beispieldatei liegt bereits im Repository.

```sh
npm --prefix tools/figma-reader ci --ignore-scripts --no-audit --no-fund

reader="$PWD/tools/figma-reader/node_modules/.bin/figma-reader"
fig="$PWD/examples/fonts/example/fonts.fig"
"$reader" load-file "$fig"
"$reader" get-tree "$fig" --depth 1 --max-nodes 100
"$reader" search "$fig" "Font specimen" --types FRAME --limit 20

node_id="1127126567:3"  # Font specimen, aus get-tree oder search
"$reader" get-tree "$fig" --node-id "$node_id" --depth 2 --max-nodes 100
"$reader" get-node "$fig" --node-id "$node_id" --depth 1
"$reader" get-text "$fig" --node-id "$node_id"
"$reader" get-components "$fig"
"$reader" get-variables "$fig" --format json
```

Für einen anderen Export `fig` auf den expliziten absoluten Pfad der vorhandenen `.fig`-Datei setzen und die ID aus diesem Export übernehmen. `load-file` meldet für diesen Weg `source: "local"`. Figma-URLs und Dateischlüssel können in der Upstream-CLI den Webmodus auslösen. Die gezeigten Aufrufe lesen nach der Installation lokal, ohne Login, Token, Upload, MCP oder OpenPencil. `get-tree` gibt eine Textübersicht aus. Die übrigen gezeigten Leseaufrufe liefern JSON auf stdout. `get-components` und `get-variables` erfassen die Datei als Ganzes.

## Befunde und Grenzen

- Die CLI dekodiert den Export je Aufruf. Die Node-ID grenzt die Ausgabe ein. Tiefe, Ergebnislimits und ausgeblendete Ebenen können den sichtbaren Ausschnitt weiter begrenzen. Bei Texten `truncated` und `unresolvedInstances` prüfen. Verborgene Texte lassen sich mit `--include-hidden` einbeziehen.
- `get-node` zeigt Instanzreferenzen und erkannte Variablenbindungen. `get-text` kann Text aus Instanzen und Overrides auflösen, soweit die nötigen Daten im Export vorliegen. Bei Variablen sind die enthaltenen Sammlungen, Modi und Werte sichtbar. Fehlende Referenzen auf Bibliotheken oder fehlende Exportdaten als Lücken festhalten.
- Dateirevision mit Pfad und SHA-256 sowie Befunde mit Node-ID und Abfrageumfang dokumentieren. Sensible JSON-Ausgaben lokal halten. Die Ausgaben sind Designbeobachtungen. Regeln für CEM, DTCG/CSS, SCXML und HTML/ARIA werden in den jeweiligen Originalquellen festgelegt.

Beim Einrichten wurden die Beispielbefehle mit dem Schriftmuster geprüft. Der öffentliche [Figma-Testexport des Readers](https://github.com/LeoGCode/figma-reader/blob/v0.4.2/test/files/real-export.fig) deckte zusätzlich Komponenten, verschachtelten Instanztext und eine Opazitätsbindung ab. Der beim Einfügen in OpenPencil gemeldete `truthy`-Variablenausdruck war in diesen Testdateien nicht reproduzierbar.
