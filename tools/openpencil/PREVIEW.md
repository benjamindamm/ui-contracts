# Native Präsentation

[Layoutregeln, Aufruf, Quellschutz und Grenzen](../../docs/skills/OPENPENCIL-PREVIEW.md).

`preview.mjs` liest eine vorhandene FIG und schreibt `<komponente>.fig`, `preview.png` und `preview-check.json` direkt in den Komponenten-Ergebnisordner. Es gibt keinen zusätzlichen presentation-Ausgabeordner. `layout.mjs` liest die zentrale Vorlage `templates/presentation.json`. Das ist interne Renderer-Konfiguration, kein neuer Komponentenstandard. Forschungseingaben und frühere Outputs werden nicht überschrieben.
