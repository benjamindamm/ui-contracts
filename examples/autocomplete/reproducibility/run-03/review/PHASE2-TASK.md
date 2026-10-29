# Prüfer · Phase 2 (Vergleich) · autocomplete-reproducibility-03

Diese Datei ist der komplette Auftrag für die Vergleichsphase. Repository: `/Users/kcnpxcp/Dev/GitHub/ui-contracts`.

## Provenienz-Fakten
- Phase 1 (Ableitung und Versiegelung der Prüfkriterien allein aus der Definition) wurde in einer anderen, inzwischen durch einen technischen Providerfehler (HTTP 413) verlorenen Session durchgeführt. Die Ergebnisse liegen versiegelt in diesem Ordner: `preregistered.json`, `preregistered.md`, `preregistration-seal.json`.
- Du arbeitest in einer frischen Session. Deine Kriterienbasis ist ausschließlich das versiegelte Kriterienset auf Datenträger. Das ist beabsichtigt und gilt als **Provenienz-Limitation des Laufs** (muss im Bericht ausgewiesen werden).
- Beide Builder sind abgeschlossen; ihre Ordner sind dir freigegeben.

## Freigabe und Verbote
- Erlaubt zu lesen: `examples/autocomplete/reproducibility/run-03/builder-a/`, `run-03/builder-b/`, `run-03/review/` (dein Ordner), `components/`, `tools/openpencil/` (gepinnte Werkzeugumgebung, inkl. `node_modules`).
- Builder-Artefakte sind **READ-ONLY**: keine Änderung, kein Überschreiben, **keine erneute Ausführung von `generate.mjs`**.
- Streng verboten: alle anderen Pfade (insbesondere `examples/autocomplete/**` außerhalb von `run-03/`, `docs/`, `scripts/`, `skills/`, `.git`, Root-`README.md`/`TASKS.md`), jegliche Git-Befehle, frühere Läufe/Designs/Recherche.
- Du schreibst nur in `run-03/review/`.

## Schritt 0 — Siegel verifizieren
Prüfe, dass `preregistration-seal.json` zu den aktuellen Bytes von `preregistered.json` und `preregistered.md` passt (frisch berechnete SHA-256). Passt es nicht: **stoppe und melde es**. Ab dann gelten die Kriterien unverändert; du darfst sie auch nach Einsicht in die Ausgaben **nicht** ändern.

## Verfahren (strikte Reihenfolge)
1. **Originaldateien zuerst, selbst gemessen**: Schreibe Skripte, die beide `autocomplete.fig`-Dateien mit dem Original-Reader der gepinnten Werkzeugumgebung wieder einlesen (vollständige Population) und strukturierte Auszüge schreiben:
   - `inspect-original.mjs` → `original-a.json`, `original-b.json`
   - `render-original.mjs` → `render-a.png`, `render-b.png` (aus den Wiedereingelesenen Graphen gerendert)
2. **Dann** liest du die beiden `REPORT.md` (und die `checks.json` der Builder) und ordnest deren Angaben gegen deine eigenen Messungen ein.
3. **Kriterienprüfung**: Prüfe alle Kriterien aus `preregistered.json` maschinell, wo möglich, an den Originaldateien. `verify.py` schreibt:
   - `native-checks.json` — alle Einzelbeobachtungen pro Artefakt (Wert für Wert)
   - `normalized-a.json`, `normalized-b.json` — normalisierte Komponentenwerte beider Designs (Zustände, Teile, Texte, Maße, visuelle Regeln, Clipping)
4. **Vergleich und Einordnung**: Definitionstreue zuerst; danach semantische, komponentenlevel Unterschiede zwischen A und B. Jede Abweichung wird eingeordnet als: **Verletzung klarer Regel | erlaubte Freiheit | unzureichend bestimmte Regel**. Freie Seitenanordnung, generierte IDs und bytegleiche Dateien sind keine Erfolgsbedingungen.
5. **Auswertung**:
   - `REVIEW.md` — vollständiger Prüfbericht auf Deutsch: Methode und Reihenfolge, Provenienz/Limitationen (Prüfer-Phase 1 und 2 in getrennten technischen Sessions; Phase 2 arbeitet von den versiegelten Kriterien; Builder-A-Metadaten s. u.), Befund pro Kriterium (erfüllt/verletzt/nicht anwendbar mit Werten), Unterschiedsanalyse A↔B, Paarübereinstimmung mit Maß und Band, Grenzen des Laufs.
   - `results.json` — maschinenlesbar: Gesamturteil je Design, Kriterien-Zählung je Design (erfüllt/verletzt/nicht anwendbar, getrennt explizit/abgeleitet), gemeinsame Verletzungen, Paarübereinstimmung (Maß + Band), Provenienz/Limitationen, Artefakthashes.
   - `hashes.json` — SHA-256 (frisch aus den Bytes) aller Laufdateien `builder-a/*`, `builder-b/*`, `review/*` (ausgenommen `hashes.json` selbst), mit relativen Pfaden.
6. **Integrität am Schluss**: Eingabehashes der 22 Definitiondateien unter `components/` neu berechnen und als unverändert bestätigen; Siegel-Konsistenz erneut bestätigen; beide Ergebnisse in REVIEW.md/results.json festhalten.

## Koordinations-Metadaten (Builder-Provenienz, für Bericht und results.json)
- Builder B: einzelne durchgehende Session, keine Unterbrechung.
- Builder A: die Erzeugungssession wurde nach dem Schreiben aller Artefakte (`autocomplete.fig`, `generate.mjs`, `checks.json`, `preview.png`, `preview.svg`, `source-sha256.json` — alle 11:07 Uhr geschrieben) durch denselben Providerfehler (HTTP 413) beendet, **bevor** `REPORT.md` existierte; Fortsetzung derselben Session war unmöglich. `REPORT.md` wurde von einer neuen Session geschrieben, die ausschließlich die vorhandenen Artefakte, `components/` und die gepinnte Werkzeugumgebung las. Kein Zugriff auf verbotene Eingaben durch beide Sessions.

## Regeln
- Jeder Befund braucht eine Beobachtung (Wert, Knotenname, Dateistelle); keine Bewertung aus Annahmen.
- Bilder (Renders, Previews) ersetzen keine Knoten-/Wertbeobachtungen.
- Zustandsfälle und Assert-Felder sind Teilbeobachtungen derselben Komponente — keine unabhängigen Stichproben; keine Signifikanztests, keine Erfolgsquoten über den Lauf hinaus.
- Weise beide Provenienz-Limitationen (getrennte Prüfer-Sessions; Builder-A-REPORT aus zweiter Session) in REVIEW.md und results.json aus, samt Auswirkung auf die Aussagekraft.
- **Kontext-Disziplin**: Halte Tool-Ausgaben schlank — gezielt suchen (grep/awk/jq), Zwischenergebnisse in Dateien schreiben statt im Kontext zu halten, große Dateien nicht mehrfach neu einlesen.

## Abschluss
Kurze Zusammenfassung am Ende: Urteil je Design, gemeinsame Verletzungen, Paarübereinstimmung, wichtigste Grenzen, Bestätigung der Siegel-/Integritätsprüfung.
