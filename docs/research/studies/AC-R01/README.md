# AC-R01 · Reproduzierbarkeit einer Autocomplete-Definition

**Explorative Studie · 25. Oktober 2026 · Auswertung abgeschlossen.**

Zwei neue Agenten ohne übernommenen Gesprächskontext erzeugten aus derselben eingefrorenen Definition jeweils ein editierbares OpenPencil-Design. Ein dritter Agent prüfte beide Originaldateien anhand zuvor gespeicherter Kriterien. **Alle erfassten normalisierten Komponentenwerte stimmen zwischen den beiden Ergebnissen überein. Dennoch verletzen beide dieselbe explizite Farbregel. Vollständige Definitionstreue wurde in diesem Durchlauf nicht erreicht.**

[Einstieg für Agenten und vollständiges Dateiverzeichnis](AGENT-GUIDE.md).

## Fragestellung und Methode

Kann eine gemeinsame Definition getrennte Agenten zu konformen und vergleichbaren Designs führen? Untersucht wurden **zwei Erzeugungen einer Komponente** mit je zehn statisch dargestellten Fällen. Die Definition umfasst 22 Dateien der Bibliothek `components/`, eingefroren auf Revision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`. Beide Builder nutzten dieselbe gepinnte OpenPencil-Werkzeugbasis 0.16.0 und erhielten getrennte Ausgabeordner.

Die Kontextübernahme war bei beiden Buildern und dem Prüfer deaktiviert. Frühere Designs und die jeweils andere Ausgabe waren keine erlaubten Eingaben. Diese Trennung beruhte auf Auftragsvorgaben; eine physische Dateisystemsandbox bestand nicht. Die genaue Modellrevision und Seeds wurden nicht erfasst. Unterschiedliche Modelle oder statistische Unabhängigkeit werden nicht behauptet.

Der Prüfer leitete Kriterien ausschließlich aus der Definition ab. Ihre Hashes wurden vor seiner Einsicht in Builder-Ausgaben versiegelt. Dies ist eine lokale Vorabfestlegung, keine öffentliche Präregistrierung. Die Entscheidung, den Versuch als Studie zu dokumentieren, fiel nach Beginn der Builds; Eingaben und Kriterien wurden deswegen nicht geändert. Anschließend las und renderte der Prüfer zunächst die tatsächlichen FIG-Dateien mit den Originalwerkzeugen; erst danach las er die Builderberichte. Das [Studienprotokoll](PROTOCOL.md) beschreibt Ablauf, Forschungsfragen und Grenzen ausführlich.

## Ergebnisse

| Beobachtung | Builder A | Builder B |
| --- | --- | --- |
| Originaldatei lesbar und mit Originalrenderer darstellbar | erfüllt | erfüllt |
| Zehn geforderte Fälle vorhanden | erfüllt | erfüllt |
| Getrennte native Texte, Teile und Ergebniszeilen ohne Locks | erfüllt | erfüllt |
| Geometrie, Texte, Daten, Sichtbarkeit und Clipping im registrierten Umfang | erfüllt | erfüllt |
| Visuelle Regeln vollständig erfüllt | **nein** | **nein** |
| Gesamturteil gegen eingefrorene Definition | **FAIL** | **FAIL** |
| Native Knoten, rein beschreibende Größe | 127 | 136 |

Die Auswertung enthält 396 Einzelbeobachtungen je Artefakt. Diese sind voneinander abhängig und keine zusätzlichen Stichproben. Es werden keine Erfolgswahrscheinlichkeit, Signifikanz oder allgemeine Agentenleistung daraus berechnet.

### Gemeinsamer Fehler

Beide Designs zeigen den deaktivierten Platzhalter in **#94A3B8**. Die explizite Regel für `::placeholder` verlangt **#64748B**. Die Farbe des deaktivierten Inputs überschreibt die ausdrücklich gesetzte Farbe seines Platzhalter-Pseudoelements nicht. Diese Erwartung war bereits vor Einsicht in die Ergebnisse festgehalten. Beide Builder legten ihre abweichende Entscheidung offen; das ersetzt die Quellvorgabe nicht.

Eine **nach der Auswertung ergänzte Browserkontrolle** mit dem Originalstylesheet bestätigt die Unterscheidung: Inputfarbe `rgb(148, 163, 184)`, Platzhalterfarbe `rgb(100, 116, 139)`, Platzhalterdeckkraft 1. Dieser [Kontrollnachweis](native-css-control.json) stützt die Auslegung der CSS-Regel; er gehört nicht zur vorab registrierten Prüfung und zählt nicht als weiterer Erzeugungslauf.

### Übereinstimmung und erlaubte Unterschiede

Nach Zuordnung der Fälle und Normalisierung der äußeren Positionen sind sämtliche erfassten Komponentenwerte gleich, einschließlich der gemeinsamen falschen Farbe. Das bedeutet weder Bytegleichheit noch Gleichheit aller nativen Eigenschaften. Unterschiedliche Seitenanordnung, Fallrahmenhöhen, technische IDs und zusätzliche Wrapper sind erlaubt. A verschiebt für das Scroll-Ende die Liste, B deren Container; beide ergeben dieselbe geprüfte sichtbare Projektion.

### Offene Definitionseigenschaften

Schriftgewicht, genaue native Textbaseline, Gestaltung von Popupmeldungen, Scrollbarstil, native Metadaten, exakte Schattenrasterung und zusätzliche Rundclipregeln sind nicht vollständig bestimmt. Übereinstimmende Entscheidungen beider Builder machen diese Eigenschaften nicht nachträglich verbindlich.

Ein Textwiderspruch bleibt erhalten: Die Beschreibung nennt drei unsichtbare Datenzeilen; sieben Ergebnisse mit Zeilenhöhe 32 und Viewporthöhe 160 ergeben fünf sichtbare und zwei außerhalb liegende Zeilen. Für die Prüfung waren die eindeutigen Zahlen und das Erhalten aller sieben editierbaren Zeilen maßgeblich. Weder Definition noch Ergebnisse wurden für diese Studie korrigiert.

## Aussagekraft und Grenzen

Der Versuch liefert konkrete Evidenz für eine übereinstimmende statische Umsetzung im gemessenen Umfang. **Übereinstimmung allein ist kein Korrektheitsnachweis:** Beide Erzeugungen reproduzieren denselben Regelverstoß. Der unabhängige Abgleich mit den Quellen bleibt erforderlich.

Die Editierbarkeit ist durch native, getrennte und ungesperrte Text-/Frame-Strukturen, Originalimport und Originalrender gestützt. Eine GUI-Öffnung mit manueller Änderung und erneutem Speichern wurde nicht durchgeführt. Interaktives Verhalten, Tastatur, IME, Provider, SCXML-Ausführung, dynamisches Scrollen, tatsächliche ARIA-/Screenreaderzustände und HTML-/TypeScript-Ausgaben wurden in dieser Studie nicht geprüft. iOS und Android bleiben Zukunftsperspektiven.

Zwei Erzeugungen derselben Komponente und Werkzeug-/Modellkonfiguration erlauben keine Verallgemeinerung auf andere Komponenten, Modelle oder Plattformen. Die Übereinstimmung kann gemeinsame Modellannahmen widerspiegeln. Die vorangegangene Kandidatenrecherche mit ihren eigenen Zählungen bleibt getrennt.

## Nachweiskette

- [Eingabehashes, Revision, Werkzeugbindung und Auftragsrahmen](../../../../examples/autocomplete/reproducibility/run-01/run.json)
- [Vorabkriterien](../../../../examples/autocomplete/reproducibility/run-01/review/preregistered.md) und [Versiegelung](../../../../examples/autocomplete/reproducibility/run-01/review/preregistration-seal.json)
- Builder A: [Originaldesign](../../../../examples/autocomplete/reproducibility/run-01/builder-a/autocomplete.fig), [Vorschau](../../../../examples/autocomplete/reproducibility/run-01/builder-a/preview.png), [Bericht](../../../../examples/autocomplete/reproducibility/run-01/builder-a/REPORT.md)
- Builder B: [Originaldesign](../../../../examples/autocomplete/reproducibility/run-01/builder-b/autocomplete.fig), [Vorschau](../../../../examples/autocomplete/reproducibility/run-01/builder-b/preview.png), [Bericht](../../../../examples/autocomplete/reproducibility/run-01/builder-b/REPORT.md)
- [Unabhängiger Prüfbericht](../../../../examples/autocomplete/reproducibility/run-01/review/REVIEW.md), [Ergebnisdaten](../../../../examples/autocomplete/reproducibility/run-01/review/results.json), [Einzelmessungen](../../../../examples/autocomplete/reproducibility/run-01/review/native-checks.json)
- Unabhängige Originalrenders: [A](../../../../examples/autocomplete/reproducibility/run-01/review/render-a.png), [B](../../../../examples/autocomplete/reproducibility/run-01/review/render-b.png)
- [Hashes der geprüften Artefakte und Review-Belege](../../../../examples/autocomplete/reproducibility/run-01/review/hashes.json); [ergänzendes Studienmanifest](evidence-manifest.json)

## Folgestudie als Vorschlag

Eine neue Definitionsversion könnte offene Darstellungsentscheidungen ausdrücklich regeln und die Platzhalterregel zusätzlich als konkretes Beispiel hervorheben. Ein weiterer Versuch müsste diese neue Version erneut einfrieren und seine Kriterien vorab festlegen. Dies ist ein Vorschlag, kein in AC-R01 ausgeführter Korrektur- oder Wiederholungslauf.
