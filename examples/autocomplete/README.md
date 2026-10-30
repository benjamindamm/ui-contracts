# Autocomplete-Beispiel und unabhängiger erster Designexport

**Fest abgelegter erster Stand:** [Referenz 0.1.0](REFERENCE.md) mit [Definitions- und Artefakthashes](reference.json).


Die führenden Quellen liegen ausschließlich in [libraries/example/](../../libraries/example/README.md), der erste Bibliothekseintrag unter [libraries/example/components/autocomplete/](../../libraries/example/components/autocomplete/README.md). Hier werden daraus erzeugte Ausgaben und deren Prüfung gesammelt. **Der erste unabhängige OpenPencil-Export liegt vor:** [Design öffnen/herunterladen](output/openpencil/autocomplete.fig), [Vorschau](output/openpencil/preview.png), [unabhängige Prüfung](review/REPORT.md). Es gibt keine zweite unabhängig gepflegte Komponentenbeschreibung.

Ein neuer Agent ohne übernommenen Gesprächskontext hat aus diesen Definitionen ein editierbares OpenPencil-Dokument mit den zehn benannten Zuständen erzeugt. Er darf keine alten Researchbilder, Webharnesses oder bereits erzeugten Komponenten als Vorlage lesen. Die ausgewählte erste Abnahme betrifft editierbares Design, keine interaktive Combobox-Preview in OpenPencil. HTML/TypeScript soll anschließend aus demselben Definitionsstand folgen.

Das lokale Originalwerkzeug liegt mit gepinnten Abhängigkeiten unter tools/openpencil/. Das Werkzeug enthält die OpenPencil-Implementierung, keine Komponentenlösung. Die abgeschlossene Recherche ist weiterhin unter docs/research/ archiviert; sie wird nicht durch diesen neuen Anwendungsproof umgeschrieben oder nachträglich erweitert.

Die strukturelle Originaldatei-Prüfung ist erfüllt. Zwei konkrete Definitionslücken und die noch nicht bestätigte Desktop-GUI-Öffnung bleiben sichtbar im Bericht. Vor dem Zwei-Ziel-Vergleich folgt eine explizite Definitionsrevision; die erste eingefrorene Version wird nicht rückwirkend verändert.

## Einheitliches Layout der Vorschau

Neue native Ausgaben verwenden das [gemeinsame Layout](../../docs/skills/OPENPENCIL-PREVIEW.md); die gerenderte Datei heißt wie bisher `preview.png` neben `autocomplete.fig`. [Beide run-04-Proben im Komponenten-Ausgabebereich](output/openpencil/run-04/README.md) sind separate nachträgliche Ausgaben; die Forschungsoriginale bleiben unverändert.

## Themeabhängige Präsentation

[Light-/Darkmode-Vergleich](output/openpencil/theme-preview/README.md) mit ready und disabled. Separater Dark-Palettenvorschlag zum Test der Kartenhintergründe; keine Änderung der führenden example-Definition oder historischer Runs.
