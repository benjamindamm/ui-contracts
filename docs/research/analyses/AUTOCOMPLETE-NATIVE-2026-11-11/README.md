# Autocomplete auf iOS und Android · 11. November 2026

**Der Pilot ist im geprüften Umfang bestanden.** Auf beiden Plattformen stimmen die gemessenen Hauptmasse und Farbstichproben des Zustands `active` mit der gemeinsamen Vorgabe überein. Auf Android wurden zusätzlich Scrollen, Tastaturnavigation, Bestätigen, Abbruch und das Antippen eines deaktivierten Treffers geprüft.

## Aufbau

Zwei neue Builder arbeiteten ohne Elternhistorie in getrennten Arbeitsverzeichnissen. Sie erhielten dieselben 21 hashgeprüften Quelldateien des eingefrorenen Web-Profils für `example` und dieselbe Abnahme. Die Eingaben waren über die Arbeitsaufträge begrenzt. Der unabhängige Prüfer installierte die gelieferten Apps, nahm eigene Screenshots auf und bewertete sie vor Einsicht in die Builder-Berichte. [Protokoll](../../protocols/AUTOCOMPLETE-NATIVE-PILOT.md) · [Vorab festgelegte Abnahme](acceptance.md)

| Merkmal | iPhone 17 Pro · iOS 26.5 | ARM64-Emulator · Android 17 |
| --- | ---: | ---: |
| Eingabefeld, Soll 320 × 44 | 320 × 44 pt | 320 × 44,19 dp |
| Abstand Feld → Ergebnisfläche, Soll 8 | 8 pt | 8 dp |
| Zeilenhöhe und Viewport, Soll 32 und 160 | 32 und 160 pt | 32 und 160 dp |
| Aktiver und deaktivierter Treffer | Hamburg hervorgehoben, München in deaktivierter Textfarbe | Hamburg hervorgehoben, München in deaktivierter Textfarbe und im UI-Baum deaktiviert |

In beiden Aufnahmen sind fünf vollständige Zeilen sichtbar. Die Stichproben für Text, Flächen, Rand, Hervorhebung und Fehlermeldung stimmen mit den sRGB-Werten aus den Quellen überein. Die Schatten unterscheiden sich. Die tatsächliche Schriftgrösse und das Innenpadding wurden nicht unabhängig vermessen. [iOS-Aufnahme](output/ios-active.png) · [Android-Aufnahme](output/android-active.png) · [Messwerte](output/measurements.txt)

## Noch offene Prüfungen

- [ ] iOS-Bedienung auf dem laufenden Ziel prüfen, insbesondere Wischen, Bestätigen, Abbruch und Fokus. Das Listenende wurde bisher als eigener Zustand gerendert.
- [ ] Auf beiden Plattformen eine verspätete Provider-Antwort gezielt auslösen und Bestätigungsereignisse unabhängig zählen.
- [ ] Den zugänglichen Namen und dynamische Meldungen mit VoiceOver und TalkBack auf den jeweiligen Zielen prüfen.

Der Pilot belegt die Übertragung für diese Komponente und die dokumentierten Simulatorfälle. Ein allgemeiner iOS-/Android-Adapter bleibt offen. Die ausführbaren Erstlieferungen liegen lokal unter `.runtime/autocomplete-native-cold-01/`. Der unabhängige Bericht, die Rohbelege und ihre Prüfsummen sind hier archiviert. [Unabhängige Erstprüfung](output/first-review.md) · [Prüfsummen](output/freeze.sha256)
