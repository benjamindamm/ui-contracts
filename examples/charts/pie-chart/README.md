# Pie Chart · D3 → SVG → OpenPencil

Nachbau der zuletzt vom Nutzer bereitgestellten [Zielvorlage](reference.png): Titel oben, drei Kreissegmente, Legende unten. Dies ist ein technischer Geometrie-/Import-Proof, kein neuer Reproduktionslauf einer modellgenerierten Komponente.

[PNG-Vorschau](preview.png) · [Editierbares FIG](pie-chart.fig) · [Berechnetes SVG](chart.svg) · [Eingabedaten](input.json) · [Messbeleg](verification.json) · [Werkzeug und Wiederholung](../../../tools/charts/README.md).

## Ergebnis

| Position | Beschriftung aus der Vorlage | Normalisierter Winkel |
| --- | --- | --- |
| Test 1 | 62.64% | 225,481452° |
| Test 2 | 24.18% | 87,039296° |
| Test 3 | 13.19% | 47,479252° |

Die angezeigten Zahlen ergeben 100,01 %. Für die Geometrie werden sie durch ihre Summe normalisiert; die Legendenbeschriftungen bleiben unverändert. Die Summe der Winkel ergibt numerisch 360° innerhalb der dokumentierten Floattoleranz. Die gerundeten Prozentwerte der Vorlage sind nicht deren unbekannte ursprüngliche Rohdaten.

## Tatsächlich geprüft

- Drei von D3 berechnete, zusammenhängende Sektoren ohne zusätzliche Achsen-/Legendenvorgaben aus einer Chartoberfläche.
- Nach SVG-Import und FIG-Roundtrip: **3 getrennte native Sektor-Vektoren**, 3 Vektor-Legendenpunkte und 7 native Textnodes.
- Mittelpunkt und beide radialen Begrenzungspunkte jedes Sektors passen zur berechneten D3-Geometrie, Toleranz 0,005 px. Ein übereinandergelegter Vollkreis erfüllt dieses Sektorkriterium nicht.
- Native Vektorflächen unabhängig numerisch vermessen: kubische Konturen mit 1.000 Stützpunkten pro Segment, anschließend Shoelace-Fläche. Maximale relative Abweichung zur analytischen Kreissektorfläche **0,022863 %**, Prüftoleranz 0,1 %. Die Abweichung berücksichtigt die Bézierapproximation der importierten Bögen.
- Beschriftungen und Segmentfarben nach erneutem Einlesen geprüft; tatsächliche lokale Inter-TTF gehasht und registriert. Kein Netzwerkzugriff beim Rendern.
- PNG direkt aus dem erneut eingelesenen FIG gerendert und visuell mit der Zielvorlage verglichen.
- **15 Regressionstests bestanden.**

## Grenzen

`PASS_LIMITED`, `release:false`: belastbarer Nachweis des konkreten statischen SVG-/FIG-Wegs. Farben wurden visuell angenähert, Inter bewusst als verfügbare Schrift verwendet; kein Anspruch auf pixelidentische Rekonstruktion der unbekannten Ursprungsschrift oder Farbprofile. Das SVG referenziert die Schriftfamilie und enthält keine eingebettete Fontdatei; der nachgewiesene PNG-Render verwendet die lokale gebundene Datei.

Keine Live-Editor-/GUI-Speicherrunde, keine Interaktivität oder Accessibility-Abnahme und keine allgemeine Garantie für beliebig komplexe SVGs. Die zugrunde liegenden Testdaten, Werkzeugversionen und Artefakthashes stehen im Messbeleg. Historische Forschungen und die ursprüngliche OpenPencil-Toolchain wurden nicht verändert.
