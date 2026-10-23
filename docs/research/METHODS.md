# Untersuchungsmethode

Stand: 23. Oktober 2026. Erste dokumentenbasierte Untersuchung, keine abgeschlossene Eignungsprüfung.

## Fragestellung und Untersuchungseinheit

Welche konkrete Anforderung an die Beschreibung einer UI-Komponente wird von welchem Kandidaten abgedeckt, in welcher Rolle und mit welchem verbleibenden Integrationsbedarf? Untersuchungseinheit ist die Kombination aus Anforderung, Kandidat und geprüftem Quellenstand. Es gibt keine globale Bestenliste.

Das Zielartefakt ist zunächst ein gemeinsames Contract-Paket. Vier getrennte Beschreibungen für Interface, Visual, Behavior und Accessibility sind ausdrücklich bevorzugt, damit Verantwortlichkeiten und vorhandene Validatoren erhalten bleiben. JSON und YAML sind mögliche Serialisierungen; SCXML verwendet XML. Es ist noch keine einheitliche Serialisierung beschlossen.

## Reihenfolge und Operationalisierung

1. Anforderungen aus Nutzeräußerungen, bestätigten Arbeitsvorschlägen und späteren Präzisierungen unterscheiden.
2. Vor der Bewertung den [Anforderungskatalog](REQUIREMENTS.md) mit beobachtbaren Teilkriterien festlegen. Kombinierte Anforderungen werden aufgeteilt, damit ein Tokenwert nicht irrtümlich als vollständiges Layout gilt.
3. Identität und Rolle jedes Kandidaten feststellen. Dokumentationsformat, Spezifikation, Bibliothek und Leitfaden sind unterschiedliche Beiträge.
4. Primärquelle und Stand erfassen. Marketingziele getrennt von konkreten Feldern und Ausführungssemantik behandeln.
5. Jede bewertete Zelle mit einem eng gefassten Claim verbinden. Befund und daraus gezogene Integrationsfolgerung unterscheiden.
6. Für verbleibende Ungewissheit einen nächsten widerlegbaren Prüfschritt angeben.

## Abdeckungslegende

| Zeichen | Bedeutung | Vergaberegel |
| --- | --- | --- |
| D | Direkt unterstützt | Das operationalisierte Teilkriterium besitzt im eigenen Modell eine dokumentierte Darstellung oder Semantik. Gilt nur in der Kandidatenrolle, nicht automatisch für das Gesamtpaket. |
| R | Über Referenz unterstützt | Ein dokumentierter Referenzmechanismus erschließt ein bereits definiertes Zielmodell; keine neue fachliche Bedeutung erforderlich. Ziel, Namensraum und Grenze müssen genannt sein. |
| A | Adapter erforderlich | Ein konkreter vorhandener Mechanismus ist belegt, aber zur geforderten neutralen Form ist zusätzliche Übersetzung oder Bindung erforderlich. Das ist eine begründete Integrationsfolgerung, kein implementierter Adapter. |
| N | Nicht abgedeckt | Die konkret untersuchte Anforderung fehlt im ausdrücklich begrenzten Modell oder ist als zukünftige Arbeit ausgewiesen. Die Aussage wird auf den geprüften Stand und Umfang beschränkt. |
| U | Ungeprüft | Kein ausreichender Nachweis für eine Bewertung. Kann trotz gelesener Übersichtsseite gelten. Bedeutet weder ungeeignet noch nicht vorhanden. |

„Nicht anwendbar“ wird in dieser ersten Matrix nicht verwendet: Auch ein spezialisierter Kandidat kann im Paket einen Beitrag leisten. Sachfremde Zellen bleiben U, statt daraus negative Bewertungen abzuleiten. Es gibt keine Gesamtpunkte und keine implizite Gewichtung.

## Evidenzstufen – unabhängig von der Abdeckung

| Stufe | Was tatsächlich geprüft wurde | Was nicht daraus folgt |
| --- | --- | --- |
| E1 | Originale Spezifikation oder Dokumentation gelesen | Validator, Compiler oder Laufzeit funktionieren wie beschrieben |
| E2 | Konkrete Schema-/Quelltextdefinition manuell gelesen | Ein Beispiel wurde validiert; alle semantischen Regeln werden erzwungen |
| E3 | Konkreter reproduzierbarer Versuch mit gespeichertem Input, Werkzeugstand, Ausgabe und Erwartung | Vollständige Produkt- oder Plattformkonformität |

In dieser Lieferung gibt es E1- und E2-Befunde, **keine E3-Versuche**. Es wurden keine Kandidaten installiert, keine Compiler ausgeführt und keine Komponenten implementiert. Ein Schemafeld vom Typ `object` ist kein Nachweis typisierter Semantik aller darin erlaubten Eigenschaften. Ein akzeptiertes unbekanntes Feld wäre ebenfalls kein Nachweis seiner Interpretation.

## Nachweisprotokoll für spätere Versuche

Je Versuch speichern: Anforderungs-ID, Kandidat und exakten Stand, Eingabe, Aufruf, Laufzeitumgebung, erwartetes Ergebnis, tatsächliches Ergebnis, Exitstatus, Fehler und Interpretation. Mindestens ein gültiger und ein gezielt ungültiger Fall sind nötig: etwa existierendes und fehlendes Referenzziel, gültige und falsche Einheit, eindeutige und kollidierende Instanz-ID. Für Laufzeitverhalten sind Ereignisfolgen und beobachtete Zustände nötig.

Eigene Schemas validieren ihre Domäne. Eine zusätzliche Paketprüfung müsste domänenübergreifende Identität, Typkompatibilität, Referenzen und Ownership prüfen. Das bloße Bestehen von vier Einzelvalidatoren belegt diese Beziehungen nicht.

## Umgang mit Quellenständen und Reproduzierbarkeit

Alle Quellen wurden am 23. Oktober 2026 über BrowserOS neo konsultiert. [SOURCES.md](SOURCES.md) nennt Dokumentversionen, sichtbare dateibezogene Commits oder ausdrücklich einen veränderlichen Dokumentationsstand. Ein sichtbarer letzter Dateicommit wird nicht als Version des gesamten Projekts ausgegeben. Wo noch kein unveränderlicher Stand vorliegt, ist die Nachweisstärke begrenzt; vor E3 muss gepinnt werden.

Die Recherche ist gezielt und anforderungsorientiert, keine systematische Vollerhebung aller UI-Formate. Die Kandidaten stammen aus dem Originalgespräch; CSS-Layoutmodule wurden für den dort bestätigten Layoutvergleich ergänzend aufgenommen. Fehlende Quellen oder 404-Antworten begründen U, niemals N. UI-Textextraktion und Teilprüfungen können Details übersehen. Eine unabhängige zweite Prüfung wurde nicht durchgeführt.

## Wissenschaftliche Nachvollziehbarkeit

Anforderung → operationalisiertes Kriterium → Quelle/Stand → Claim → Matrixzelle → offener Versuch bildet die Prüfkette. Die erste Matrix enthält eine qualitative Abdeckung, keine statistische Aussage und keinen Wirksamkeitsnachweis für Agenten. Herstellergröße, Sternezahl und Selbstaussagen wie „verlustfrei“ sind keine Nachweise von Eignung. Eine spätere Gewichtung muss aus erklärten Projektprioritäten entstehen und Sensitivität gegenüber diesen Gewichten zeigen.
