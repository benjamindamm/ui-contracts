# AC-R01 · Studienprotokoll

Stand: 25. Oktober 2026. **Explorative Replikationsstudie an einer Komponentenbeschreibung.** Dieses Protokoll beschreibt den tatsächlich begonnenen Ablauf. Der Wunsch nach Studienaufbereitung kam nach dem Start der Builder. Die unveränderten Eingaben waren vor deren Start eingefroren; die unabhängigen Prüfkriterien wurden vor dem Zugriff des Prüfers auf Ausgaben lokal gespeichert und versiegelt. Es gibt keine externe öffentliche Präregistrierung.

## Fragestellungen

1. Können zwei neue Agenten ohne übernommenen Gesprächsverlauf aus derselben eingefrorenen Autocomplete-Definition jeweils ein editierbares OpenPencil-Design erzeugen?
2. Erfüllt jedes Ergebnis die ausdrücklich bestimmten Anforderungen der Definition?
3. Welche Unterschiede bleiben zwischen beiden Ergebnissen: Regelverletzung, erlaubte Freiheit oder unzureichend bestimmte beziehungsweise widersprüchliche Angabe?

Ein ähnliches Bild allein beantwortet Frage 2 nicht. Beide Ausgaben müssen zuerst unabhängig an den Quellen gemessen werden.

## Untersuchungsgegenstand und Eingabe

Eine Komponentenbeschreibung: Autocomplete mit den referenzierten Overlay- und ScrollArea-Definitionen. Der erlaubte semantische Input ist ausschließlich die 22 Dateien unter components/. Der eingefrorene Stand besitzt die Revision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`. [Dateiliste, Einzelhashes und Ausgangscommit](../../../../examples/autocomplete/reproducibility/run-01/run.json).

Die Definition umfasst Interface/CEM, Visual/DTCG und CSS, Behavior/SCXML, Accessibility/HTML und ergänzende eigene Projektionsregeln sowie konkrete Darstellungsfälle. Es ist ein Autoren-/Erzeugungsexperiment mit diesen vorhandenen Formaten, kein Vergleich sämtlicher UI-Standards.

## Versuchsaufbau

| Rolle | Kontext und Aufgabe |
| --- | --- |
| Builder A | Neuer Agent, Kontextübernahme `none`; nur Definition und normale technische OpenPencil-Hilfsmittel. Eigener Ausgabeordner. |
| Builder B | Neuer Agent, Kontextübernahme `none`; derselbe Auftrag mit anderem Ausgabeordner. Keine Einsicht in A oder frühere Lösungen. |
| Unabhängiger Prüfer | Neuer Agent, Kontextübernahme `none`; zunächst nur Definition lesen und Kriterien speichern. Erst nach Abschluss beider Builder ihre Originaldateien prüfen, dann Berichte lesen. |
| Koordination | Hält Versionen und zeitlichen Ablauf fest, versiegelt Kriterien, prüft Unverändertheit und führt die Studie zusammen. Kennt den früheren Pilotversuch; dessen Ergebnis ist kein erlaubter Input für Builder oder Prüfer. |

Alle Agenten übernehmen die Modell-/Reasoningkonfiguration des aufrufenden Systems; es wurde keine unterschiedliche Modellwahl verlangt. Exakte Modellrevision, Samplingparameter und Seeds werden von der verwendeten Agentenschnittstelle nicht als verifizierbare Laufmetadaten zurückgegeben und bleiben deshalb unbestimmt. Wir behaupten keine unterschiedlichen Modelle oder statistische Unabhängigkeit ihrer Fehler.

Die Gesprächskontexte sind getrennt. Die Eingabe- und Ausgabegrenzen wurden im Auftrag festgelegt; es wurde keine zusätzliche Dateisystemsandbox eingerichtet. Ob ein Modell intern auf ähnliche Trainingsmuster zurückgreift, kann dieser Versuch nicht kontrollieren.

## Kontrollierte Bedingungen

- Dieselben unveränderten Definitionsbytes für beide Builder und den Prüfer.
- Dieselben installierten Originalwerkzeuge: OpenPencil 0.16.0; transitiver Stand durch den Werkzeug-Lock gebunden.
- Gleicher Builderauftrag bis auf den eigenen Ausgabepfad.
- Keine früheren Designs, Screenshots, Webharnesses, Recherchedokumente oder fremden Lösungen als erlaubte Eingaben.
- Keine nachträgliche Änderung der Definition oder Builderdateien zur Anpassung an das Review.
- Das Ziel ist ein **editierbares Design**, keine interaktive Combobox-Preview und kein HTML-/TypeScript-Vergleich.

Technische Zwischenschritte und Code dürfen die Builder eigenständig wählen. Diese Freiheit ist Bestandteil des Tests, keine kontrollierte identische Implementierung.

## Ablauf und Zeitordnung

1. Definition und Werkzeug-Lock prüfen; Eingabe-/Rollenzuordnung speichern.
2. Zwei Builder mit getrenntem Kontext und getrennten Schreibverzeichnissen starten.
3. Den Prüfer mit reinem Definitionszugriff starten; er leitet seine Kriterien eigenständig ab und beendet die Vorbereitungsphase.
4. Prüfkriterien hashen und versiegeln, bevor der Prüfer Zugriff auf Builderausgaben erhält. Die Builder dürfen währenddessen bereits arbeiten; dies ist keine Behauptung einer vor jedem Generierungsbeginn abgeschlossenen Kriterienregistrierung.
5. Beide Builder liefern echte Dateien, Vorschau, Generierungsschritt und Bericht.
6. Prüfer ausdrücklich zur Vergleichsphase freigeben. Er liest die gespeicherten Dateien selbst mit Originalwerkzeugen und ordnet anschließend Angaben der Builder ein.
7. Quellen-, Kriterien- und Ergebnisintegrität prüfen und Ergebnisse einschließlich Widersprüchen und Grenzen festhalten.

[Versiegelte Vorabkriterien](../../../../examples/autocomplete/reproducibility/run-01/review/preregistered.json) · [Lesbare Kriterien](../../../../examples/autocomplete/reproducibility/run-01/review/preregistered.md) · [Siegel](../../../../examples/autocomplete/reproducibility/run-01/review/preregistration-seal.json).

## Auswertung

Der Prüfer verwendet vorab abgeleitete Kategorien wie erfüllt, verletzt, unbestimmt und außerhalb des Umfangs. Er prüft die ausdrücklich bestimmten Zustände, Anatomie, Texte, Maße, Farb-/Typografieregeln, Clipping und Editierbarkeit. Anschließend vergleicht er beide Ergebnisse auf Komponentenebene.

Die freie Seitenanordnung, technische IDs und bytegleiche Dateien sind keine Erfolgsbedingungen. Eine unterschiedliche Knotenanzahl kann auf unterschiedliche zulässige Struktur oder einen Fehler hinweisen; die Anzahl allein ist kein Konformitätsurteil. Bilder unterstützen die Auswertung, ersetzen aber die tatsächlichen Knoten-/Wertbeobachtungen nicht.

Zustandsfälle und einzelne Assert-Felder sind Teilbeobachtungen innerhalb derselben Komponente, keine zusätzlichen unabhängigen Stichproben. Die Studie hat zwei Erzeugungsläufe für eine Definition. Es werden keine Signifikanztests oder Erfolgsquoten für beliebige Agenten, Komponenten oder Plattformen berechnet.

## Grenzen

Kleine gezielt gewählte Stichprobe, ein Komponentenpaket, gleiche technische Umgebung, nicht verifizierbar unterschiedliche Modellinstanzen/Seeds, nur ein unabhängiger Prüfer. Die Koordination kennt einen vorherigen Pilotexport; Builder und Prüfer dürfen ihn nicht lesen. Eine tatsächliche Desktopöffnung oder Assistenztechnikprüfung wird nur behauptet, wenn sie ausgeführt wurde. Native Ziele und interaktive OpenPencil-Preview gehören nicht zu diesem Versuch.

Gemeinsame Fehler beider Builder können trotz Übereinstimmung bestehen. Umgekehrt können unterschiedliche Ergebnisse beide zulässig sein, wenn die Definition Freiheit lässt. Die Studie untersucht deshalb Definitionstreue und Reproduzierbarkeit getrennt und dokumentiert Mehrdeutigkeiten als Befunde.

## Daten und Abschluss

Die Originaldateien und Rohprüfungen bleiben in den getrennten Laufordnern unter examples/autocomplete/reproducibility/run-01/. Diese Studiendokumentation verweist darauf, statt zweite führende Ergebnisdateien zu pflegen. Das tatsächliche Review ist abgeschlossen; Ergebnis und Grenzen stehen im [Studienbericht](README.md), sämtliche Dateien im [Agenteneinstieg](AGENT-GUIDE.md). Frühere Research-Zähler werden nicht rückwirkend um diese andersartige neue Studie erweitert.
