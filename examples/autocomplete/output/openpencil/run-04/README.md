# Einheitliche Präsentation · vorhandene run-04-Ergebnisse

Dies sind **nachträgliche Präsentationsausgaben**, kein neuer Reproduktionslauf und keine Änderung der Forschungsartefakte. Die Eingaben kommen unverändert aus run-04; ihre alten freien Seitenanordnungen werden hier durch dasselbe native Layout ersetzt.

| Build | Darstellung | Native Datei | Beleg |
| --- | --- | --- | --- |
| A | [PNG](builder-a/preview.png) | [FIG](builder-a/autocomplete.fig) | [Receipt](builder-a/preview-check.json) |
| B | [PNG](builder-b/preview.png) | [FIG](builder-b/autocomplete.fig) | [Receipt](builder-b/preview-check.json) |

Beide mit zehn Fällen in gleicher Reihenfolge und demselben Raster. Alle verglichenen Komponenteneigenschaften unverändert: 142 Nodes bei A, 162 bei B. Die verschiedenen internen Layerstrukturen werden nicht künstlich vereinheitlicht. [Zusätzliche begrenzte Gegenprüfung](countercheck.json): beide PASS_LIMITED, keine Fehler/Warnungen, 572/572 gleiche Paarwerte. Das ist keine allgemeine Freigabe.

Die eingetragene alte Definitionsrevision stammt aus dem unveränderten run-04-Manifest. Die PNGs verwenden die jetzt lokal gebundenen Inter-Fontdateien und sind kein rückwirkender Nachweis der damaligen Glyphmetriken. [Werkzeug, Wiederholung und Grenzen](../../../../../docs/skills/OPENPENCIL-PREVIEW.md).

Ablage wie bei anderen Komponenten-Ausgaben: `autocomplete.fig` und `preview.png` liegen je Builder zusammen. Der run-04-Ausgabeunterordner trennt diese nachträgliche Probe von den unveränderten historischen Originalen; für neue Komponenten ist kein eigener presentation-Bereich vorgesehen.
