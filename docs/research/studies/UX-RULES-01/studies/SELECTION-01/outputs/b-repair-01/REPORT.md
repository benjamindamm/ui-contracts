# SELECTION-01-b · Reparatur 01

Separate Reparaturfassung für SEL-B01 und SEL-B02. Die versiegelte Erstlieferung unter `../b/` bleibt unverändert. Diese Fassung übernimmt index.html, styles.css, decision.json und policy-evaluation.json bytegleich. Die kopierte Entscheidung und Policy-Ausgabe dokumentieren die ursprüngliche Quellenbindung und wurden für diese Reparatur nicht erneut erhoben.

## Ursachen und Änderungen

**SEL-B01:** Für die vier nativen Input-Felder fehlte die Übersetzung des nativen input-Ereignisses in das definierte value-change-Ereignis. Jedes Feld beobachtet jetzt seinen eigenen letzten Stringwert. Eine tatsächliche Änderung löst genau ein aufsteigendes CustomEvent mit `detail: {value: control.value}` aus. Ein gleich gebliebener Wert löst keines aus. Bei nativem disabled oder readOnly wird die Verarbeitung unterdrückt.

**SEL-B02:** Die lokale Erfolgsmeldung wurde nur beim Absenden gesetzt und bei anschließenden Änderungen nicht entwertet. Tatsächliche Änderungen eines Input-Werts, der Suchquery oder des bestätigten Länderschlüssels löschen sie jetzt. Dasselbe gilt für eine Änderung des angezeigten Querytexts beim Bestätigen oder Wiederherstellen auf Blur. Reine Navigation, unveränderte input-Ereignisse und erneutes Bestätigen derselben Auswahl mit unverändertem Label löschen keine Erfolgsmeldung. Die Query bleibt von dem bestätigten Länderschlüssel getrennt. Native disabled-/readOnly-Flags werden auch vor Queryverarbeitung und Auswahl berücksichtigt.

Die Optionsdaten, Komponentenwahl, Filterreihenfolge, Schlüsselprüfung, Tastatursteuerung und Scrolllogik sind übernommen. Die Reparatur ergänzt keinen freien Ländercommit und keine neue Komponente.

## Ausgeführte Prüfungen

- TypeScript erneut mit vorgegebenem Compiler kompiliert: `--target ES2020 --lib ES2020,DOM,DOM.Iterable --strict`; Exit 0.
- Gelieferte Quelldatei nach der Änderung zurückgelesen: Event-Payload ist der native Stringwert; pro Feld wird der vorherige Wert geprüft; disabled/readOnly sperren die Verarbeitung; Query-/Commit-/Bluränderungen löschen die Rückmeldung.
- Hashvergleich: index.html, styles.css, decision.json und policy-evaluation.json sind zur Erstlieferung bytegleich. TRACE.json und SHA256SUMS.json binden die Dateien dieser Reparatur und die Originaldateien.

## Testgrenzen

Kein eigener Browser-, Screenreader- oder realer IME-Lauf für die Reparatur ausgeführt. Der erfolgreiche Compilerlauf und der Quellreadback sind keine interaktive Abnahme. Die vom Auftrag mitgeteilte Browserstichprobe der Erstlieferung ist ein externer Vorgängerbefund und wurde hier nicht als eigener Test wiederholt. Keine neue Policy-Auswertung ausgeführt; Auswahl und Quelldaten wurden nicht verändert. Die zuvor dokumentierten Grenzen (Schriftfallback, synchroner Provider, keine vollständige SCXML-Runtime und keine regionale Telefonnummernvalidierung) bestehen fort. Keine Produktionsfreigabe.
