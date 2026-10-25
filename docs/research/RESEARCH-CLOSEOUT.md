# Abschluss der Recherche

Stand: 25. Oktober 2026. **Die Recherchephase ist abgeschlossen und für die spätere Umsetzung dokumentiert.** iOS, Android und weitere native Ziele sind nach Nutzerfestlegung Zukunftsperspektive; deren fehlende Tests blockieren diesen Abschluss nicht. Es läuft keine weitere Recherche- oder Testrunde.

## Ergebnis

Ein konkreter Vorschlag verbindet vier Kernbeiträge: CEM für Schnittstellen/Teile, DTCG für Designwerte, SCXML für Verhalten und WAI-ARIA für zugängliche Websemantik. HTML/CSS bilden das Webziel ab; APG ergänzt Bedienmuster. Die Originaldateien behalten ihre Fachmodelle. Zusätzliche Bindungsregeln und Adapter verbinden Definitionen, Instanzen, Teile, Zustände und Ereignisse.

Das gemeinsame statische Paket und der begrenzte gemeinsame Webreferenzlauf sind tatsächlich geprüft. Alle 20 finalen Browsererwartungen für Events, Fokus, Scrollen, Lifecycle, Providerfälle und AX-Zustände sind erfüllt. Der eigene Webadapter ist konkret, aber noch kein allgemeiner deklarativer Runtime-Resolver. Die Auswahl bleibt ein dokumentierter Vorschlag für die Umsetzung, keine beschlossene universelle Produktsprache.

## Empfohlene Lesereihenfolge

1. [Integrationsprofil IP-01](INTEGRATION-PROFILE.md): gemeinsamer Vorschlag und Rollen der vier Domänen.
2. [Bindungsentwurf](INTEGRATION-BINDING-DRAFT.md): Identitäten, Referenzen, Quellführung und Diagnosen.
3. [Browser-Abschlussbericht](experiments/2026-10-25/ip01-browser/REPORT.md): tatsächlich ausgeführte Gesamtfolge, Ergebnisse und Grenzen.
4. [Übergabe an einen Coding-Agenten](IMPLEMENTATION-HANDOFF.md): vorhandene Artefakte und spätere Umsetzung.
5. [Aktueller Status](CURRENT-STATUS.md) und [Aufgaben](../../TASKS.md): abgeschlossenes Wissen, externe Restklärungen und spätere Projektarbeit.

## Wo welche Daten liegen

| Inhalt | Maßgeblicher Einstieg |
| --- | --- |
| Gesamtes Dokumentenverzeichnis | [Dokumentenindex](DOCUMENT-INDEX.md) |
| Alle 16 Kandidaten / 416 Bewertungen | [Matrix](MATRIX.md), maschinenlesbar [study.json](study.json) |
| 543 begründete Befunde und ihre Grenzen | [Claims](CLAIMS.md) |
| Quellen S01–S129 mit geprüften Ständen | [Quellenregister](SOURCES.md) |
| 106 ausgeführte Gruppen / 702 Bedingungen | [Vollständiger Experimentindex](experiments/INDEX.md) |
| Originaldateien, Zusatzcode, Vorregistrierungen, Rohresultate | Jeweilige verlinkte Experimentordner und ihre source-manifest.json-Dateien |
| Tatsächliche Browserereignisse und AX-Bäume | [Browserresultate](experiments/2026-10-25/ip01-browser/results.json) und deren Rohaufnahmen |
| Nachvollziehbare Bezüge des Integrationsvorschlags | [Belegindex mit Dateihashes](INTEGRATION-PROFILE-EVIDENCE.json) |
| Methodik und ursprüngliche Anforderungen | [Methode](METHODS.md), [Anforderungen](REQUIREMENTS.md) |
| Entwicklung, frühere Zwischenzahlen und Gegenbefunde | [Kontext](CONTEXT.md), [vollständiges früheres README](README-RESEARCH-ARCHIVE.md), ausdrücklich historische Dokumente und Originalberichte |

Die Zähler sind keine Behauptung, dass alle Erwartungen in allen historischen Versuchen erfüllt waren. Verletzungen und eigene Korrekturen bleiben erhalten. Aktuelle Zahlen werden aus study.json abgeleitet; ältere Angaben in archivierten Berichten beschreiben deren damaligen Stand.

## Grenzen ohne weitere Recherchepflicht

**Zwei externe Originalklärungen bleiben offen:** Google DESIGN.md X06/C483 und OpenUI X06/C484. Die fehlenden Herausgeberinformationen sind [konkret dokumentiert](REMAINING-2.md); erneutes Zählen oder Wiederholen derselben Proben würde sie nicht lösen. Beide sind keine Voraussetzungen der ausgewählten Webreferenzkombination und blockieren den Rechercheabschluss nicht.

**Spätere Umsetzung:** produktive Bindungssyntax, allgemeiner Resolver, vollständige API-/Theme-/Änderungsvarianten und ausführbare spezialisierte Agenten-/Skillabläufe. Das sind weitere Projektarbeiten, keine vergessenen Rechercheergebnisse.

**Spätere Validierung:** echte Assistenztechnik und IME, weitere Browser/Widgets und gegebenenfalls Produktreife. Diese stärkeren Zusagen wurden nicht erteilt und werden nicht aus AX-/Forschungsfixtures abgeleitet.

**Zukunftsperspektive:** iOS, Android und weitere native Ziele. Sie bleiben ausdrücklich außerhalb der abgeschlossenen aktuellen Recherche. [Ziel und Einschätzung](ARCHITECTURE-DIRECTION.md).

## Dokumentationsabschluss

Aktuelle Einstiege, Dokumenten- und Experimentindex, Matrix-/Claim-/Quellenbezüge, lokale Verweise und Belegdateihashes sind abgeglichen. Historische Berichte und Erstfehler bleiben erhalten. Das Dokumentationspaket enthält den abschließenden Stand. Commit und Push dieses Abschlussstands sind auf ausdrücklichen Nutzerauftrag freigegeben; der konkrete Gitstand ist im Repositoryprotokoll nachvollziehbar.
