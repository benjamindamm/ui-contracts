# Panda CSS: Exportreader und spätere Abfragen getrennt ausgeführt

Stand: 25. Oktober 2026. Originalrevision 86f78a228204d63baa0b8bca2676d9f26190e449. E3-Folgeprüfung der offenen X06-Zelle, kein neues Originalschema und keine Implementierung eines Validators.

## Ergebnis

18 vorher festgelegte Fälle sind mit den unveränderten Funktionen parseDesignSystem und indexDesignSystem ausgeführt: 14 Eingabefälle und vier Abfragen. Alle 18 Erwartungen treffen zu. Das ist ein erfolgreicher Versuchslauf über definierte Grenzen, keine Konformitätsfreigabe aller Eingabedokumente. X06 bleibt U/C442.

## Bestätigte Prüfgrenzen

Der Reader akzeptiert einen leeren und einen kleinen vollständigen Tokenexport. Er weist fehlerhaftes JSON, ein Array als Root, fehlende Tabellen, falsche paths/values-Formen, einen textuellen Versionswert und eine höhere SchemaVersion zurück.

Wie im Quellkommentar ausdrücklich vorgesehen, prüft er Zeilen und manche Tabellen nicht vollständig. categories=7 und tokens=false werden angenommen, ebenso eine null-Zeile, negative/gebrochene numerische Versionswerte sowie fehlende conditions/themes. Letztere sind im TypeScript-Interface beschrieben, werden durch diesen Reader aber nicht verlangt. Das sind Befunde am Reader; der Generator kann stärkere Garantien besitzen und andere Panda-Prüfungen werden nicht ausgeschlossen.

## Abfragen sind keine Nachvalidierung

Die gültige Kontrollzeile wird aufgelöst. Bei zwei Basiswerten desselben Tokens liefert die ursprüngliche Suche den ersten Treffer; sie meldet keinen Widerspruch. Ein Verweis auf einen nicht vorhandenen Token erscheint als rückwärts indizierte Kante, ohne Zielprüfung. Eine zuvor akzeptierte null-Zeile führt beim Aufbau des Werteindex zu einem Fehler. Die Eigenschaft „Parsing wirft nicht“ gilt damit nicht automatisch für jede nachgelagerte Abfrage mit einem ungeprüften Dokument.

Keine Behauptung, dass der reguläre Panda-Generator solche beschädigten Dokumente erzeugt. Die Gegenfälle untersuchen externe Eingaben und den tatsächlichen Prüfumfang dieser Funktionen.

## Reproduktion

Originales read.ts und types.ts anhand source-manifest.json beschaffen; Hashes beziehen sich auf vollständige UTF-8-Lesefassungen. Der Ergebnisordner verteilt keine Originalquellen. read.ts enthält nur Typimporte; das vollständige Modul wurde mit TypeScript 5.9.3 nach CommonJS/ES2022 übersetzt, ohne Funktionsersatz oder Stubs. Node 24.22.1 führte den Runner aus. PROBE_TYPESCRIPT kann auf den exakt gebundenen TypeScript-5.9.3-Ordner zeigen; alternativ nutzt der Runner den lokalen Pfad der früheren TypeScript-Probe. Es gab keinen Projekt-Typecheck, keinen Compilerbuild und keinen CSS-/UI-Renderlauf.

cases.json enthält die vor Ausführung gespeicherten Kriterien, results.json sämtliche Inputs, Ausgaben, Hashes und Beobachtungen. Ein eigener Schema-/Integrationsprüfer wäre eine zusätzliche Entwicklung, keine unveränderte Panda-Fähigkeit. Kein Commit oder Push.
