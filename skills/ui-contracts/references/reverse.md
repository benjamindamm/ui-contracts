# Rückweg: Design oder Code in Contracts überführen

Nur beim Erschließen oder Abgleichen bestehender Artefakte laden. Der Auftrag benennt Repository, Bibliothek, Komponente, Eingaberevision und ob nur analysiert oder auch übernommen werden soll. Bestehende Bibliothek und betroffene Originalquellen zuerst lokalisieren; kein impliziter Import aus example.

- Native Designdatei/Editor: [Design-Rückweg](reverse-design.md).
- Codebase/Implementierung: [Code-Rückweg](reverse-code.md).
- Fehlende Entscheidungen und Quellenbezüge: [Draft-Vollständigkeit](completeness.md).

## Gemeinsamer Ablauf

1. Eingabestand und betroffene Teile/Instanzen mit Pfad/Hash oder versioniertem Editor-Export binden. Für externe Dateien und große Codebases nur den benötigten Bereich lesen. Werkzeugzugriff und tatsächlich verfügbaren Exportumfang klären.
2. Kleine Quellenkarte erstellen: Beobachtung mit Locator, Domäne, Zustand/Einheit, Zuordnung zur Komponente, vorhandene Contractregel und Unterschied. `observation`, `derived`, `assumption` und `explicit` gemäß bestehendem Übergabevertrag trennen. Eingabeartefakte sind Belege, nicht automatisch führende Vorgaben.
3. Bei fehlender Definition einen Draft mit stabiler Komponenten-ID anlegen. `component.json` darf im Draft fehlende Domänenverweise auslassen; keine Dummy-SCXML oder erfundene ARIA-Regel zum Füllen erzeugen. Vorhandene Regeln innerhalb des Auftrags in führenden Originaldateien festhalten. Vollständige Komponentenprüfung bleibt davon getrennt.
4. Passendes Anforderungsprofil ausdrücklich wählen und begründen. Mit dem Vollständigkeitscheck fehlende Entscheidungen abfragen. Ein Konflikt zwischen Design, Code und bisheriger Regel bleibt offen; keine automatische Mehrheits- oder „Code gewinnt“-Regel.
5. Dem Nutzer die nächste fachlich zusammengehörige Gruppe blockierender Fragen mit ihren IDs vorlegen. Bereits belegte Entscheidungen nicht nochmals fragen. Antwort und Fundstelle nachvollziehbar dokumentieren; Regeln in den passenden Originaldateien festhalten, statt eine zweite Wahrheit im Fragenbericht aufzubauen. Übernahme nur innerhalb des Nutzerauftrags; ungelöste Entscheidungen bleiben offen.
6. Neue Quellrevision und betroffene Abhängigkeiten benennen. Geänderte Belege erneut lesen und erst danach Coveragezuordnungen neu hashen. Keine alten Passwerte umetikettieren. Vollständigkeitscheck wiederholen, anschließend betroffene Original-/Zielprüfungen und [Gesamtabgleich](integration-review.md).

## Lieferung

Quellenkarte, neue Draftquellen bzw. konkreter Änderungsvorschlag, Coverage-Record und Checkbericht. Stabile Frage-IDs, offene Widersprüche, bestätigte Entscheidungen, Quellenrevisionen und nicht geprüfte Bereiche auffindbar halten. Für mehrstufige Arbeit bestehende `task.json`/`handoff-vN.json` nutzen: blockierende Fragen verhindern `ready`. Ohne Rollenauftrag genügt ein kleiner Bericht; nicht allein deswegen zusätzliche Agenten starten.

Das Verfahren ist ein neuer, begrenzt werkzeuggeprüfter Arbeitsweg. Es verspricht weder allgemeine Figma-/Code-Synchronisation noch die Richtigkeit automatisch erschlossener Absichten.
