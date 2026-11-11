# Nativer Autocomplete-Versuch für iOS und Android

Status **im geprüften Umfang bestanden**. Der Versuch prüft, welche Regeln aus dem bestehenden Web-Profil auf iOS und Android erhalten bleiben und wo eine plattformspezifische Entscheidung nötig ist. [Ergebnis und verbleibende Prüfungen](../analyses/AUTOCOMPLETE-NATIVE-2026-11-11/README.md)

## Gemeinsame Eingabe

Ausgewählt ist die Bibliothek `example` mit `ui-contracts:Autocomplete` 0.3.0 und den gebundenen Komponenten Overlay und ScrollArea. Als Eingabe dient der eingefrorene Quellenstand des Web-Nachweises. Die drei Komponentenordner und die Design-Tokens wurden byteweise mit der aktiven Bibliothek abgeglichen.

- [Komponentenquelle und Domänenverweise](../analyses/WEB-RUNTIME-2026-10-31/evidence/browser/sources/components/autocomplete/component.json)
- [Web-Manifest mit Quellenrevision und SHA-256](../analyses/WEB-RUNTIME-2026-10-31/evidence/browser/manifest.json)
- [Web-Prüffälle und Ergebnisse](../analyses/WEB-RUNTIME-2026-10-31/README.md)

## Voraussetzung für einen gültigen Lauf

Für jede Plattform arbeitet ein neuer Subagent ohne Elternhistorie in einem eigenen Arbeitsverzeichnis. Er erhält die Auftragsdatei, die passende Rollenkarte, die gebundenen Originalquellen sowie vorab festgelegte Testdaten und Abnahmekriterien. Bisherige native Implementierungen, Screenshots und Bewertungen bleiben ausserhalb seiner Eingabe. Der Agent hält den Quellenstand und die tatsächlich geladenen Eingaben fest.

Die visuelle Abnahme verwendet auf beiden Plattformen denselben benannten Zustand mit identischen Eingaben und Ergebnissen. Ein separater Prüfer gleicht die Ausgabe mit den vorab festgelegten Kriterien ab.

## Setup und Abnahme

- **iOS.** Kompatibles Xcode und iOS-Simulator installieren. Die SwiftUI-App lokal bauen und im Simulator starten. Für den Nachweis gesprochener Meldungen separat VoiceOver auf einem iPhone prüfen.
- **Android.** Android Studio, SDK und ein ARM64-Emulatorabbild installieren. Die Android-App lokal bauen und im Emulator starten. Für den Nachweis gesprochener Meldungen TalkBack separat prüfen.

| Domäne | Gemeinsame Erwartung | Nachweis je Ziel |
| --- | --- | --- |
| Schnittstelle | Suchtext, aktiver Vorschlag und bestätigter Schlüssel bleiben getrennt. Bestätigen meldet den Schlüssel genau einmal. | Eingaben und ausgegebene Ereignisse mit festen Testdaten protokollieren. |
| Visuelles Design | Benannte Teile und relevante Tokens für geschlossen, Laden, Treffer, leer und Fehler bleiben nachvollziehbar. | Token-Zuordnung und Screenshots je Zustand festhalten. Unterschiede bei Einheiten, Layout und nativen Controls begründen. |
| Verhalten | Antworten einer früheren Suche überschreiben aktuelle Ergebnisse nicht. Deaktivierte Treffer bleiben unbestätigbar. Abbruch verändert den bestätigten Wert nicht. | Providerantworten in vorgegebener Reihenfolge auslösen und die Zustände vor und nach jeder Aktion prüfen. |
| Barrierefreiheit | Das Suchfeld hat einen zugänglichen Namen. Ergebnisse und Lade-, Leer- und Fehlerstatus sind zugänglich. | Native Semantik und Fokus prüfen. Gesprochene Statusmeldungen getrennt mit VoiceOver oder TalkBack nachweisen. |

Für jeden Lauf OS, SDK, Gerätetyp und Quellenstand festhalten. Touch, Hardwaretastatur und assistiven Fokus getrennt protokollieren. HTML/ARIA bleibt die Web-Referenz. Native Rollen, Fokus und Ansagen werden im jeweiligen Ziel begründet und geprüft.
