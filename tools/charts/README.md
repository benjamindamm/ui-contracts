# Modulare Diagrammgeometrie · erster SVG-Proof

`d3-shape` **3.2.0**, isoliert unter tools/charts installiert und über package-lock.json gebunden. Es wird nicht das gesamte D3-Framework eingebunden. Die bisherige OpenPencil-Abhängigkeitsdatei bleibt unverändert. Die transitive Pfadbibliothek ist d3-path 3.1.0; beide Pakete deklarieren ISC als Lizenz.

```sh
npm ci --prefix tools/charts --ignore-scripts --no-audit --no-fund
node --test tools/charts/test_pie.mjs
node tools/charts/proof.mjs examples/charts/pie-chart/input.json /tmp/pie-proof-new
```

Voraussetzung: gepinnte OpenPencil-Abhängigkeiten und die lokalen Inter-Assets der example-Bibliothek. Neue Ausgabedateien werden exklusiv angelegt; bestehende Proofs nicht überschreiben. Das Proofskript ist ein Demonstrationsadapter für die konkrete Vorlage, kein allgemeiner Diagrammrenderer.

## Einsatz durch Agenten

Bei datenabhängigen Sektoren oder Kurven zuerst die [Agent-Anleitung](../../skills/ui-contracts/references/geometry.md) lesen. Einfache native Formen, runde Buttons und Balken benötigen diesen Adapter normalerweise nicht. Die Pie-API ist wiederverwendbar, das Proofskript bildet nur die konkrete Referenz ab.

Minimaler Aufruf aus einem ESM-Skript im Repository-Stamm:

```js
import {pieGeometry, sectorsSvg} from "./tools/charts/pie.mjs";
const geometry = pieGeometry([
  {id: "first", label: "Erster Anteil", value: 60, color: "#FFD54A"},
  {id: "second", label: "Zweiter Anteil", value: 40, color: "#1C5363"}
], {radius: 100});
const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240">
${sectorsSvg(geometry, {cx: 120, cy: 120})}</svg>`;
```

`svg` enthält echte Sektorpfade und kann an den vorhandenen SVG-Import übergeben werden. Für andere Chartfamilien die benötigte D3-Shape-Funktion gezielt anbinden und deren native Ausgabe separat prüfen.

## Trennung von Geometrie und Gestaltung

`pie.mjs` stellt `pieGeometry(data, {radius, innerRadius})` und `sectorsSvg(...)` bereit. D3 berechnet die Winkel und SVG-Pfade. Reihenfolge, Farben und Daten kommen vom Aufrufer; das Modul fügt weder Achsen, Skalenbeschriftungen noch Legenden hinzu. Die Legende und Typografie im Proofskript sind eine getrennte, frei gestaltete SVG-Zusammenstellung passend zur Nutzerreferenz. Es wurde keine eigene Kreisbogen-/Bézierkonstruktion als Ersatz für D3 implementiert.

Die erzeugte SVG-Datei wird über OpenPencils vorhandenes `createSVGNodes` importiert, als FIG exportiert, wieder eingelesen und headless als `preview.png` gerendert. Jedes Segment bleibt ein eigener editierbarer VECTOR, Beschriftungen bleiben TEXT-Nodes. Die Datei ist kein Bitmap-Chart. Eingebettete Datenbindung, Interaktivität oder nachträgliche automatische Neuberechnung im Editor werden nicht behauptet; geänderte Daten werden durch den Generator erneut aufgebaut.

## Nachweis

[Ergebnis und konkrete Prüfungen](../../examples/charts/pie-chart/README.md). 15 Regressionen prüfen Winkelabdeckung, Nachbarschaft, Proportionen, Reihenfolge, Null-/Fehlerwerte, Radien, Pie-/Donut-Geometrie, SVG-Ausgabe, Artefakthashes und native editierbare Segmente. Ein Gegenfall mit einem Vollkreis hat keinen Sektormittelpunkt als Vertex und würde die Native-Sektorprüfung verfehlen.

Der eigentliche End-to-End-Nachweis gilt für das gezeigte **dreiteilige Pie Chart**. Die Donut-/Einzelwertprüfungen decken die Geometriefunktion ab, keine vollständige native Donut-/Chartfamilienfreigabe. Weitere komplexe Charts benötigen eigene repräsentative SVG-/FIG-/Rendering-Gegenfälle.

Quellen: [D3-Pie-Winkel](https://d3js.org/d3-shape/pie), [D3-Arc-Pfade](https://d3js.org/d3-shape/arc). Die Daten-JSON ist eine Testfixture, kein neuer Komponentenstandard. Keine Änderung der bestehenden Komponenten-Contracts oder Forschungsruns.
