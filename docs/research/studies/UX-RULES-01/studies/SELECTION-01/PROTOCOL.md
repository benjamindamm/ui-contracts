# SELECTION-01 · Komponentenwahl beim Bau eines Personenformulars

Prospektiv vor den Builderaufträgen festgelegte Studie, 30. Oktober 2026. Zwei frische Agentenkontexte ohne Elternhistorie erhalten dasselbe fachliche Formularziel, dieselbe Bibliothek und dieselbe Projektpolicy. Unterschied: drei bzw. 30 vorgegebene Länder-/Vorwahloptionen. Erwartungen sind vor Builderausgaben eingefroren. Der Koordinator kennt sie; keine doppelt verblindete oder statistisch aussagekräftige Studie.

## Zweck und Hypothese

Nachweisen, ob Agenten beim Erstellen einer konkreten UI aus fachlichen Anforderungen die bereitgestellten UX-/Fähigkeitsinformationen tatsächlich für die Wahl zwischen Select und Autocomplete nutzen. Input wird für die freie Personen-/Rufnummerneingabe bereitgestellt. Das Experiment misst diese zwei Fälle im gegebenen Setup, keine generelle Modellüberlegenheit oder universelle UX-Richtigkeit.

Die Projektpolicy fordert bei mehr als 15 Optionen in diesem Szenario Suchbarkeit. Diese Grenze ist bewusst gesetzte Test-/Produktpolicy, kein universelles Usability-Gesetz. Bei wenigen Optionen und ohne Präferenz für Texteingabe bevorzugt sie das einfache Select. Autocomplete ist in der kleinen Variante technisch weiterhin geeignet; Abweichung von der Projektpräferenz wird getrennt von fehlender Eignung bewertet.

## Eingaben und Unabhängigkeit

Bibliotheksmanifest, beide fachlichen Aufgaben, Eingabedaten, Kriterien und Anfangsprompts werden vor Dispatch gehasht. Ein Builder sieht nur seine Aufgabe/Optionsdaten, die aktuelle Library, die generischen Skill-/Rolleninformationen und ausdrücklich erlaubte lokale Werkzeuge. Keine früheren Forschungsdesigns, Runergebnisse, Prüfkriterien oder andere Builderausgaben. Prompts nennen keine gewünschte Komponentenwahl. Helper-Ausgabe der formalen Projektpolicy darf genutzt werden: Das ist Teil der zu prüfenden Frameworkanwendung, kein Zugriff auf den unabhängigen Prüfbericht.

Agenten werden per fork_turns=none gestartet, ohne Modelloverride und ohne weitere Delegation. Konfiguriertes Standardmodell bleibt unbestätigt, sofern keine technische Identität vorliegt; Agenten recherchieren ihre Identität nicht. Prozessunabhängigkeit wird durch getrennte Kontexte/Dateibereiche angestrebt, nicht technisch als Dateisandbox garantiert. TRACE.json ist Builder-Selbstauskunft; ein vollständiger unabhängiger Pfadaudit wird dadurch nicht behauptet.

## Primäre Endpunkte

1. Komponente für den Ländervorwahlbereich wird vor Erstellung der UI in decision.json festgehalten, mit Kontextfakten, Quellen und Begründung.
2. Harte Eignung und Einhaltung der Projektpräferenz werden getrennt geprüft. Vorregistrierte Erwartung: A bevorzugt Select, B benötigt die definierte suchfähige Autocomplete-Variante. Ein nicht definierter SelectWithSearch zählt nicht als vorhandener Bibliotheksbaustein.
3. Tatsächliche Ausgabe muss dieser Auswahl entsprechen; ein data-component-Label allein genügt nicht. B muss wirklich filtern, ausschließlich vorhandene Country-Keys bestätigen und unbekannte Eingaben beim Abschicken ablehnen.
4. Beide Formulare verwenden den Input-Contract für Vorname, Nachname, E-Mail und lokale Rufnummer. Rufnummer bleibt String mit führenden Nullen. Kein Backend, Versand oder externe Datenübermittlung.

## Weitere Prüfungen

Sichtbare Labels, eindeutige IDs, native Semantik bzw. rollen-/zustandsgebundene Combobox, Tastaturbedienbarkeit in der tatsächlich geprüften Stichprobe, korrekte Anzahl und Reihenfolge der Optionen. Nur Testdaten verwenden. Prioritätsliste CH/DE/FR ist vorgegeben, keine Standortermittlung. Danach numerische Vorwahlsortierung und Country-Key als deterministischer Gleichstandsschlüssel. Gemeinsame Vorwahl +1 erlaubt; Auswahlidentität ist Country-Key, nicht Vorwahl.

HTML-/TypeScript-Artefakte werden statisch und soweit verfügbar in einem gemeinsamen Browserprüfumfang untersucht. Automatische Prüfungen und manuelle Beobachtung getrennt protokollieren. Keine Screenreader-, plattformübergreifende oder vollständige Accessibility-Abnahme aus einer DOM-/Tastaturstichprobe ableiten.

## Erhaltung, Fehler und Grenzen

Erstlieferungen nicht nachträglich passend ändern. Bei fehlerhaftem Build bleiben Entscheidung und Originalartefakte erhalten; Reparaturen bekommen einen neuen Unterordner und getrennte Erst-/Endbewertung. Unterbrechungen und Limitprobleme mit bekannten Folgen dokumentieren; keine unbekannten internen Providerereignisse erfinden. Kein Commit/Push ohne Nutzerauftrag.

Der Vor-Select-Stand mit 28 Dateien wurde vor Erweiterung vollständig unter prior-library gesichert. Bisherige UX-Pilotmanifeste bleiben unverändert und sind nach der Libraryerweiterung gegenüber der Livebibliothek erwartbar veraltet. Für Wiederholung den erhaltenen alten Stand verwenden; kein stiller Alias auf die neue Revision. Der damalige Befund wird nicht zurückdatiert aktualisiert.
