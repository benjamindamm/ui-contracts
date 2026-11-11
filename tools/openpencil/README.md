# Gepinnte OpenPencil-Werkzeuge

Diese Umgebung enthält Originalpakete für die Erzeugung und Prüfung editierbarer Designdokumente. Sie enthält keine Vorlage für das Autocomplete und keine führenden Komponentenregeln.

```sh
cd tools/openpencil
npm ci --ignore-scripts
npm run openpencil -- --help
```

Die Paketversionen und transitiven Abhängigkeiten stehen in package.json und package-lock.json. Bibliotheken liegen unter `libraries/<id>/`; die Bibliothek muss im Auftrag ausdrücklich gewählt sein. Neue Zielausgaben gehören in den jeweiligen Beispielordner. Die automatische Installation von Paket-Lifecycle-Skripten ist zunächst deaktiviert; notwendige zusätzliche Schritte müssen explizit begründet werden.

Beim Erschliessen vorhandener Designs: [Design-Rückweg](../../skills/ui-contracts/references/reverse-design.md). Der Reader liefert native Beobachtungen; unbekanntes Verhalten bleibt im [Draftcheck](../completeness/README.md) offen.
