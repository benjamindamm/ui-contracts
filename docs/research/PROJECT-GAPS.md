# Was dem Projekt nach den Einzelprüfungen noch fehlt

Stand:25. Oktober2026. Abgleich von study.json, TASKS, REQUIREMENTS, INTEGRATION, INTEGRATION-REVIEW und BINDINGS. **Zwei offene Kandidatenmatrixzellen sind nicht gleich zwei verbleibende Projektaufgaben.** Dieser Abgleich erzeugt keine neuen Matrixbewertungen oder Prüfbedingungen und wählt kein Produktformat.

## 1. Zwei fehlende Originalklärungen

Unverändert offen: Google DESIGN.md X06/C483 und OpenUI X06/C484. Die genau fehlenden Herausgeberinformationen und ausgeschöpften Prüfpfade stehen in [REMAINING-2](OPEN-QUESTIONS.md). Diese Fragen betreffen die jeweils untersuchten Originalstände; sie sind kein generelles Hindernis für jede mögliche Formatkombination.

## Fortschritt: konsolidierter Vorschlag

[IP-01](INTEGRATION-PROFILE.md) und der [gemeinsame Abnahmeplan](INTEGRATION-ACCEPTANCE.md) beschreiben jetzt einen konkreten ersten Webfall. Die folgenden Lücken sind damit als zusammenhängender Vorschlag bearbeitet, aber noch nicht als ausführbares Gesamtpaket geschlossen: Rollen und Versionen, Referenz-/Instanzregeln, Unterkomposition, begrenzter Typumfang, Versionspolitik und Abnahmefälle. Die vorgeschlagenen Entscheidungen bleiben reviewbar. Ein ausgewählter gemeinsamer Browserlauf ist inzwischen ausgeführt; allgemeine Produkt-/Variantenfreigabe folgt daraus nicht.

## 2. Ausgangslücken des ursprünglichen Abgleichs

Die folgende Tabelle bewahrt den damaligen Arbeitsbedarf. Inzwischen sind konkreter Vorschlag, statisches Referenzpaket und begrenzter Browserlauf vorhanden; maßgeblich für den Abschlussstand sind [CURRENT-STATUS](CURRENT-STATUS.md) und [TASKS](../../TASKS.md). Allgemeiner deklarativer Runtime-Resolver und stärkere Plattform-/AT-/Produktnachweise bleiben offen.

| Arbeitsblock | Was vorhanden ist | Was tatsächlich noch fehlt |
| --- | --- | --- |
| Konkrete Zusammenstellung | Kandidatenvergleich und viele begrenzte Original-/Adapterversuche | Eine begründete konkrete Kombination mit gebundenen Versionen und klarer Rollenverteilung je Domäne. Kein beliebiger Mix aller Kandidaten und kein beschlossener Formatstapel. |
| Gemeinsame Bindungsregeln | Ausgeführte einzelne Referenz-, Typ-, Instanz-, Ownership- und Layoutbindungen | Ein zusammenhängender Satz für dieselben Definitionen, Instanzen und Teile: erlaubte Zielarten, Geltungsbereiche, Quellenstände und per-information Zuständigkeit. Die einzelnen Forschungsprofile sind noch kein einheitlicher Integrationsvertrag. |
| Unterkomposition | Originale Wiederverwendung und einzelne Child-/Invoke-/Scrollbeiträge | Eine vollständige Kette Autocomplete A/B → jeweiliges Overlay → eigene referenzierte ScrollArea, mit Parametern, Ereignissen, Fokus-/Scrollverantwortung und Lebenszyklus. Vorhandene Teilnachweise nicht als diese komplette Kette ausgeben. |
| Typen und Daten | Ausgeführte begrenzte primitive Typ-/Payload- und Einheitenbindungen | Festgelegter benötigter Typumfang einschließlich Optionalität, Defaults, Objekten, Arrays und Fehlerfällen; dokumentierte Grenzen zwischen den gewählten Originalmodellen. Keine Verpflichtung zu beliebigen Typen, solange der Zielumfang offen ist. |
| Versionen und Änderungen | Gepinnte Quellen, Hashbindungen und konkrete Konfliktfälle | Einheitliche Regeln für Paket-/Formatversion, kompatible Aktualisierung, Migration, Namespaces, erlaubte Rekursion/Zyklen und reproduzierbare Auflösung. Einzelne Pins ergeben noch keine gemeinsame Updatepolitik. |
| Durchgängiger Akzeptanzfall | Zahlreiche echte Originalruntime-/Browser-/AX-Versuche mit erhaltenen Gegenbefunden | Ein zusammenhängendes Paket derselben gewählten Originalartefakte, das den vollständigen ausgewählten Ablauf samt beschädigten Verbindungen gemeinsam prüft. Die641 Bedingungen stammen aus102 unterschiedlichen Gruppen und bilden keinen einzigen vollständigen Produkttest. |

Ein zusätzliches Integrationsartefakt, seine Serialisierung und ein Resolver bleiben Entscheidungen nach diesem Abgleich. Daraus folgt weder, dass zwingend eine neue Sprache nötig ist, noch dass bestehende Referenzen bereits alle Beziehungen abdecken. Vorhandene Originalsyntax und Originalprüfungen sollen erhalten bleiben.

## 3. Für den Akzeptanzfall noch festzulegende Regeln

Die Dokumentation nennt noch offene Varianten für freie Eingabe gegenüber ausschließlicher Listenauswahl, Öffnung bei Fokus/Eingabe, Lade-/Leer-/Fehlerzustände, asynchrone und veraltete Ergebnisse, Abbruch sowie Fokusverlust. Wiederholte Optionen benötigen eine ausdrücklich bestimmte Identität bei Sortierung/Ergebnisaktualisierung.

Aktive Option, zugänglich gemeldete Auswahl und bestätigter Produktwert bleiben drei Bedeutungen. Im ausgewählten Fall muss feststehen, wann sie zusammenfallen und welches öffentliche Event beziehungsweise welche Rückmeldung ausgelöst wird. Autocomplete bleibt ein Referenzfall, kein beschlossenes Produkt.

## 4. Spätere Zielplattformen und Agentenübergabe

iOS/Android und weitere native Ziele sind ausdrücklich Zukunftsperspektive außerhalb der abgeschlossenen Recherche, keine fehlende Abnahme dieser Phase.

- Webbezüge und native Browserbeobachtung sind belegt. Eine zugesagte Swift/SwiftUI-/sonstige native Supportmatrix, konkrete Typ-/Layout-/Fokusabbildungen und echte Assistenztechnikprüfungen fehlen. Diese stärkeren Nachweise sind nicht still in die Kandidatenmatrix eingerechnet.
- Der Agentenablauf ist konzeptionell beschrieben. Ausführbare spezialisierte Skills, ein gemeinsamer Prüfaufruf und eine abgesicherte Änderungs-/Übergabeprozedur sind nicht fertiggestellt. Implementierung bleibt spätere Arbeit.
- Der erforderliche produktive Mindest-Reifegrad, unterstützte Versionen und Abnahmekriterien sind noch nicht ausgewählt. Erfolgreiche Forschungsfixtures sind keine Produktionsfreigabe.

## 5. Dokumentationslücke dieses Abgleichs

TASKS führte zuletzt nur die zwei Matrix-U-Zellen als offen. Die oben stehenden projektweiten Integrationsarbeiten waren zwar in den Entwürfen erwähnt, aber nicht als eigene aktuelle Aufgaben sichtbar. Die Integrationsdateien enthielten außerdem historische Zahlen unter der Überschrift „Aktueller Stand“. Diese Angaben sind nun als historische Zwischenstände markiert; maßgeblich für Matrixzahlen bleibt [CURRENT-STATUS](CURRENT-STATUS.md).

## Abschluss und spätere Arbeit

Die aktuelle Recherche ist abgeschlossen. [Gemeinsamer Vorschlag](INTEGRATION-PROFILE.md), [statisches Paket](experiments/2026-10-25/ip01-static/REPORT.md) und [Browserlauf](experiments/2026-10-25/ip01-browser/REPORT.md) liegen vor. Es startet keine neue Runde. Die historische Tabelle beschreibt den damaligen Ausgangspunkt; spätere Produkt-/Resolver-/Variantenarbeit steht in [TASKS](../../TASKS.md). Native Ziele blockieren diesen Abschluss nicht.

[Abschlussübersicht](RESEARCH-CLOSEOUT.md) · [Dokumentenindex](DOCUMENT-INDEX.md) · [Aktueller Status](CURRENT-STATUS.md)
