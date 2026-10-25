# Gepinnte OpenPencil-Werkzeuge

Diese Umgebung enthält Originalpakete für die Erzeugung und Prüfung editierbarer Designdokumente. Sie enthält keine Vorlage für das Autocomplete und keine führenden Komponentenregeln.

```sh
cd tools/openpencil
npm ci --ignore-scripts
npm run openpencil -- --help
```

Die Paketversionen und transitiven Abhängigkeiten stehen in package.json und package-lock.json. Die Definitionsbibliothek liegt unter ../../components/. Neue Zielausgaben gehören in den jeweiligen Beispielordner. Die automatische Installation von Paket-Lifecycle-Skripten ist zunächst deaktiviert; notwendige zusätzliche Schritte müssen explizit begründet werden.
