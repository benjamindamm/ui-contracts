# Untersuchungsmethode

**Endlicher Originalumfang für X06:** [Gepinnte offizielle Oberflächen und konkrete Restzugriffe](experiments/2026-10-25/x06-official-scope/REPORT.md); WAI-ARIA 1.2 eigenes Format-/Schemasubjekt anhand §8 geklärt, X06 N/C471. Originale Ark-Dokumentationsextraktion geklärt, X06 weiter U/C473. Aktuell 52 U; weiterhin 330 Bedingungen/42 Gruppen, keine neue Laufzeitbedingung.

**XState-Originalprüfgegenstand geklärt:** [Core 5.33.3, SDK-Typen und Snapshot getrennt](experiments/2026-10-25/xstate-validator/REPORT.md); sechs API- und drei SDK-Bedingungen erfüllt. X06 begrenzt N/C464 für den neutralen Originalartefaktschema-Pfad im veröffentlichten Core, keine pauschale Validatorabwesenheit. Aktuell 53 U, 308 Bedingungen/38 Gruppen.

**Ergänzung 25.10.2026 – SCXML-Laufzeit:** [Gespeicherter Prüfblock](experiments/2026-10-25/scxml-runtime/REPORT.md) mit 17 Bedingungen: 9/10 im Ausgangslauf, 2/2 Diagnosefälle und 5/5 Browserfälle. Getrennte Vorbereitung verhindert die beobachtete Datenkopplung. Native Parent-Sendung und ein zusätzlicher interaktiver Forschungs-Host sind ausgeführt; keine Produktionskomponente, physische Tastatur- oder AT-Prüfung. Ältere Aussagen zu ausschließlich statischer Prüfung gelten für die damaligen Teilversuche. Historischer Zwischenstand nach DTCG: 56 U-Zellen.

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

Die ursprüngliche dokumentarische Lieferung enthielt E1/E2 und keine E3-Versuche. Seit der Folgeprüfung vom 24. Oktober liegen zusätzlich 217 benannte E3-Prüfbedingungen in 22 Gruppen vor; siehe [Versuchsbericht](experiments/2026-10-24/REPORT.md). In der ursprünglichen Runde wurden keine Kandidaten installiert oder Compiler ausgeführt. Die neue E3-Runde nutzt isoliert bereitgestellte Prüfwerkzeuge und einzelne Originalfunktionen; keine UI-Komponente wurde implementiert. Ein Schemafeld vom Typ `object` ist kein Nachweis typisierter Semantik aller darin erlaubten Eigenschaften. Ein akzeptiertes unbekanntes Feld wäre ebenfalls kein Nachweis seiner Interpretation.

## Nachweisprotokoll für spätere Versuche

Je Versuch speichern: Anforderungs-ID, Kandidat und exakten Stand, Eingabe, Aufruf, Laufzeitumgebung, erwartetes Ergebnis, tatsächliches Ergebnis, Exitstatus, Fehler und Interpretation. Mindestens ein gültiger und ein gezielt ungültiger Fall sind nötig: etwa existierendes und fehlendes Referenzziel, gültige und falsche Einheit, eindeutige und kollidierende Instanz-ID. Für Laufzeitverhalten sind Ereignisfolgen und beobachtete Zustände nötig.

Eigene Schemas validieren ihre Domäne. Eine zusätzliche Paketprüfung müsste domänenübergreifende Identität, Typkompatibilität, Referenzen und Ownership prüfen. Das bloße Bestehen von vier Einzelvalidatoren belegt diese Beziehungen nicht.

## Umgang mit Quellenständen und Reproduzierbarkeit

Quellen wurden am 23., 24. und 25. Oktober 2026 über BrowserOS neo konsultiert; einzelne erneute Auswertungen bereits gespeicherter Vollauszüge sind ausdrücklich gekennzeichnet. [SOURCES.md](SOURCES.md) nennt Dokumentversionen, sichtbare dateibezogene Commits oder ausdrücklich einen veränderlichen Dokumentationsstand. Ein sichtbarer letzter Dateicommit wird nicht als Version des gesamten Projekts ausgegeben. Wo noch kein unveränderlicher Stand vorliegt, ist die Nachweisstärke begrenzt; vor E3 muss gepinnt werden.

Die Recherche ist gezielt und anforderungsorientiert, keine systematische Vollerhebung aller UI-Formate. Die Kandidaten stammen aus dem Originalgespräch; CSS-Layoutmodule wurden für den dort bestätigten Layoutvergleich ergänzend aufgenommen. Fehlende Quellen oder 404-Antworten begründen U, niemals N. UI-Textextraktion und Teilprüfungen können Details übersehen. Eine unabhängige zweite Prüfung wurde nicht durchgeführt.

## Wissenschaftliche Nachvollziehbarkeit

Anforderung → operationalisiertes Kriterium → Quelle/Stand → Claim → Matrixzelle → offener Versuch bildet die Prüfkette. Die erste Matrix enthält eine qualitative Abdeckung, keine statistische Aussage und keinen Wirksamkeitsnachweis für Agenten. Herstellergröße, Sternezahl und Selbstaussagen wie „verlustfrei“ sind keine Nachweise von Eignung. Eine spätere Gewichtung muss aus erklärten Projektprioritäten entstehen und Sensitivität gegenüber diesen Gewichten zeigen.

## Fortschreibung nach der Gesamtprüfung

Ein U kann trotz abgeschlossener dokumentarischer Prüfung bestehen bleiben: Die technische Evidenz genügt weiterhin nicht. Der Arbeitsstatus einer Nachprüfung und die fachliche Abdeckung sind deshalb getrennt in study.json erfasst. Bei X04 wird ein belegter eigener Instanz-/Kompositionsmechanismus mit zusätzlich erforderlicher UI-Bindung als A eingeordnet; die vollständige Vier-Domänen-Kette bleibt davon getrennt. CSS V03 und OpenPencil X05 besitzen ausdrücklich genannte Scopeergänzungen, keine pauschale Zurechnung aller Editor-/Webfähigkeiten.

Für E3 ist zwischen Schema-, Funktions-, Typauflösungs-, Hostchecker- und gerenderter UI-/AT-Prüfung zu unterscheiden. Die Bezeichnung runtime_trials im JSON ist eine historische Sammelrubrik; kind und ui_rendered weisen den tatsächlich ausgeführten Gegenstand aus. Eine Erwartungsabweichung bleibt gespeichert. Korrigierte Harness-Erwartungen erhalten ihren ursprünglichen Stand, statt den Kandidatenbefund umzudeuten.

**Begrenzte Scopeerweiterungen:** OpenPencil V01/V03 beziehen zusätzliche originale Variablen-/Tokenexportquellen ein; V05 den vorhandenen CSS-Projektionsadapter und A02 den konkreten Switch→Reka→APG-Webbezug. Die Neubewertungen gelten ausschließlich für diese Beiträge, nicht pauschal für alle Editor-/Bibliotheksfunktionen. Keine Gleichsetzung mit dem Autocomplete-Akzeptanzfall oder nativer Unterstützung.

**25.10.2026 – statische Host-Fixtures:** P18/P19 rendern synthetische HTML-Fixtures im isolierten Browser. ui_rendered=true bezeichnet hier ausdrücklich nur diese Host-Fixtures; static_host_fixture_only=true, component_implemented=false und at_tested=false grenzen sie von Produkt-/Assistenztests ab. Ein zusätzlicher eigener Mappingcheck ist getrennt von den Originalregeln protokolliert.

[Alle ausgeführten Nachweisgruppen mit Outputs und Prüfgrenzen](experiments/INDEX.md).

**X06 – präzisierte negative Modellgrenze:** Ein vollständig abgegrenzter Originaldistributions-/APIgegenstand kann N erhalten, wenn seine belegte Rolle und konkrete Originaldatenflüsse das operationalisierte separate Artefaktschema nicht bereitstellen. SDK-Typprüfung und Graphaufbau bleiben als eigene positive Nachweise sichtbar. Fehlende Suchtreffer allein reichen weiterhin nicht. Das N gilt nicht für unbekannte externe Produkte oder Erweiterungen; deren hypothetische Fähigkeiten erzwingen keine endlose U-Bewertung des tatsächlich geprüften Kerns. Beispiel: C464, xstate-Core 5.33.3.

**Endliche offizielle Oberfläche:** [X06-Umfangsregister](experiments/2026-10-25/x06-official-scope/REPORT.md) bindet jede Restfrage an den gespeicherten offiziellen Originalstand und konkrete Dateien/Entrypoints. Beliebige externe Plugins oder zukünftige Releases müssen nicht ausgeschlossen werden. WAI-ARIA 1.2 X06 N beruht auf der ausdrücklichen eigenen Modell-/Hostsprachenabgrenzung, nicht auf der Forderung nach einem vollständigen semantischen Allvalidator oder einem negativen Suchergebnis. Keine Änderung des X06-Kriteriums.
