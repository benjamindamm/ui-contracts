# Lokale Schriftdateien pro Bibliothek

Stand: 29. Oktober 2026. Fonts sind Bibliotheksassets; DTCG beschreibt weiterhin die typografischen Werte. Die optionale `libraries/<id>/fonts.json` verbindet Font-Family-Tokens mit konkreten Dateien. Das Assetmanifest ist eine **eigene Projektkonvention**, kein DTCG-Originalstandard und kein allgemeiner Fontresolver.

## Beispiel: Inter 4.1

In [example/fonts.json](../../libraries/example/fonts.json) sind Inter Regular (400) und Bold (700), normal, an den bestehenden Token `autocomplete.fontFamily` gebunden. Die vier unverändert übernommenen Dateien liegen unter [assets/fonts](../../libraries/example/assets/fonts/): pro Schnitt eine TTF für den lokalen OpenPencil-Adapter und eine WOFF2 fürs Web. Die originale [SIL Open Font License 1.1](../../libraries/example/assets/fonts/LICENSE.txt) liegt bei.

Quelle: [offizielle Inter-Release 4.1](https://github.com/rsms/inter/releases/tag/v4.1), Commit `e3a3d4c57d5ecc01453a575621882a384c1995a3`, [Downloadarchiv](https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip). Download über BrowserOS neo am 29. Oktober 2026. Archiv-SHA-256 und originale ZIP-Eintragspfade stehen im Manifest. Die internen TTF-Namen melden `Version 4.001;git-9221beed3`; Releasebezeichnung und interner Fontversionsstring sind getrennte Angaben.

## Für eine andere Bibliothek

```text
libraries/meine-app/
  library.json
  tokens.json
  fonts.json
  assets/fonts/
    MeineSchrift-Regular.ttf
    MeineSchrift-Regular.woff2
    LICENSE.txt
```

Eine Family nennt `tokenPaths` und je Schnitt `weight`, `style`, `openpencilStyle`, `postScriptName` sowie Datei-/Formathashes. Keine lokale Betriebssysteminstallation oder Onlineauflösung wird als Assetnachweis behandelt. Die Lizenz muss die beabsichtigte Nutzung und Weitergabe zulassen; Manifestangaben ersetzen keine Prüfung der tatsächlichen Lizenz.

Aktuell unterstützt der begrenzte Adapter statische normale TrueType-Schnitte plus WOFF2. Variable Fonts, Italic, andere Formate und Fallbackketten sind nicht allgemein umgesetzt. Nicht unterstützte Angaben blockieren, statt still durch eine andere Schrift ersetzt zu werden. Ein neues `init` kopiert weiterhin keine Fonts aus example.

## Prüfen und Vorschau erzeugen

Vom Repository-Stamm, nach Installation der gepinnten OpenPencil-Abhängigkeiten:

```sh
python3 tools/fonts/check.py --library example --output /tmp/example-font-check.json
node tools/fonts/preview.mjs example /tmp/example-font-preview-new
python3 tools/fonts/test_fonts.py
```

Der Ausgabeordner der Vorschau muss neu oder leer sein; Libraries und historische Autocomplete-Ausgaben dürfen nicht überschrieben werden. `contracts.py inspect --library ID` führt diese zusätzliche Prüfung ebenfalls aus, wenn die ausgewählte Library eine `fonts.json` besitzt; beschädigte Fontassets führen dann zu FAIL, gültige Assets heben den allgemeinen semantischen BLOCKED-Status nicht auf.

Der Validator prüft Dateihashes, Bibliotheksgrenzen, Lizenzdatei, Tokenbindung, TTF-Metadaten (Familie/PostScriptname/Gewicht/statisch) und WOFF2-Header. Das ist keine vollständige OpenType-Konformitätsprüfung oder vollständige WOFF2-Decodierung.

Die Vorschau lädt die hashgeprüften TTF-Bytes explizit über `fontManager.markLoaded` der gepinnten OpenPencil-Core-Version 0.16.0. CanvasKit muss die Familie erkennen und für den Probetext ausschließlich vorhandene Glyphen melden. Der Adapter exportiert ein FIG, liest die Text-/Familien-/Gewichtswerte zurück und rendert ein PNG. Netzwerk-Fetch ist dabei gesperrt; geladene Quellen werden nach dem Rendern erneut geprüft. CSS und HTML referenzieren ausschließlich die lokalen WOFF2-Dateien, ohne `local()`-Abkürzung.

Für die **im Repository abgelegte** Webprobe:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
# Browser: http://127.0.0.1:8765/examples/fonts/example/
```

Bei frei gewählten Vorschauordnern außerhalb des Repositories muss ein gemeinsamer HTTP-Root die erzeugten relativen Assetpfade erreichbar machen. Die Vorschau kopiert keine zweite Fontbibliothek in ihren Ausgabeordner.

## Ausgeführter Nachweis

[PNG-Schriftprobe](../../examples/fonts/example/fonts.png) · [editierbares FIG](../../examples/fonts/example/fonts.fig) · [Webprobe](../../examples/fonts/example/index.html) · [OpenPencil-Receipt](../../examples/fonts/example/openpencil-receipt.json) · [Browser-Receipt](../../examples/fonts/example/browser-receipt.json) · [Gesamtverifikation](verification.json).

- Dateiprüfung: zwei statische Schnitte, vier passende Fontdateien, Lizenzhash und vorhandener Inter-Token.
- OpenPencil/CanvasKit: beide Familien erkannt, alle 49 Zeichen des Probetexts je Schnitt abgedeckt; vier Textnodes mit je drei zurückgelesenen Sollwerten. PNG visuell kontrolliert, keine Netzwerk-Fetchversuche.
- BrowserOS neo / Chromium: beide lokalen WOFF2-Dateien geladen; SHA-256 der Browserantworten stimmt mit dem Manifest überein. FontFace-Status `loaded` für 400 und 700. Die gemessenen Probetextbreiten unterscheiden sich: 613,88671875 bzw. 631,1015625 px bei 24 px Schriftgröße.
- Fünfzehn positive/negative Prüferregressionen, unter anderem falscher Hash, fehlende Datei/Lizenz, falsches Gewicht/Familie, unlesbares TTF, falsche WOFF2-Länge, falscher Token und unsicherer Pfad.

Alle Ergebnisse sind `PASS_LIMITED`, `release:false`. Nicht nachgewiesen: vollständige Unicode-Abdeckung, identische Pixel auf allen Plattformen, automatische Bereitstellung im laufenden OpenPencil-Editor auf dem Server, Native-App-Einbettung oder allgemeine Accessibility-Konformität. Ein FIG-Familienname allein garantiert keine auf jedem Ziel vorhandenen identischen Fontbytes. Die Schriftdateien bleiben ausdrücklich bereitzustellende Assets.

## Revision und historische Forschung

Die ursprünglichen 22 Definitionsdateien wurden nicht geändert; alte Studien und ihre eingegrenzten Prüfprofile behalten diese Quelle. Die zusätzlich aufgenommenen Assets und `fonts.json` ergeben jedoch eine **neue Gesamtbibliotheksrevision**. Neue Läufe müssen das vollständige aktuelle Librarymanifest einfrieren. Die alten 22-Datei-Nachweise werden dadurch nicht nachträglich zu Fontdatei-Nachweisen. [Bibliotheksmigration](../libraries/MIGRATION.md).
