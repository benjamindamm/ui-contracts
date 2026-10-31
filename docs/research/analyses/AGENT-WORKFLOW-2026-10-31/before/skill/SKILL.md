---
name: ui-contracts
description: UI-Komponenten als CEM-, DTCG/CSS-, SCXML- und HTML/ARIA-Contracts erstellen, bearbeiten und begrenzt prüfen; auch für UX-Eignung und Komponentenwahl anhand einer ausdrücklich gewählten Contractbibliothek. Nicht für beliebige App-Implementierung oder allgemeine Konformitätszertifizierung.
---

# UI Contracts

Erstelle nachvollziehbare Originalartefakte und benenne den tatsächlich geprüften Umfang. Die vorhandene Prüfkette unterstützt eine feste Forschungsreferenz, keinen allgemeinen Renderer oder Validator für neue Komponenten.

## Projekt und Auftrag bestimmen

Finde das vom Nutzer gemeinte UI-Contracts-Repository anhand von `tools/validation/check.py`, `tools/validation/profile.json` und dem Verzeichnis `libraries/` (alte Checkouts: `components/library.json`); arbeite in dessen tatsächlichem Pfad. Der Skill enthält keine zweite führende Kopie von Definitionen, Schemas, Browserdaten oder Prüfern. Fehlt dieser Projektstand, melde `BLOCKED` und die fehlende Voraussetzung.

Bestimme aus dem Auftrag Bibliotheks-ID, Komponente, Ziel, gewünschte Änderung und Prüfanspruch. Wähle `libraries/<id>/library.json` ausdrücklich; keine implizite aktive Bibliothek. Komponenten liegen unter `components/`, gemeinsame Dateien unter `assets/`; Index, Tokens und optionale Fontbindung bleiben am Bibliotheksroot. `example` ist die erhaltene Forschungsbibliothek, keine automatisch zu lesende Vorlage. Neue Bibliotheken über `tools/libraries/manage.py init ID` leer anlegen; Details nur bei Bedarf in `libraries/README.md`. Nutze vorhandene Entscheidungen; frage nur nach fachlich entscheidenden fehlenden Angaben. Autorenarbeit, editierbares Design und ausgeführte Webkomponente sind unterschiedliche Ziele. Kein Commit, Push, Deployment oder fremder Kontakt wird allein durch diesen Skill autorisiert.

Bei Reproduktionsläufen, Modellvergleichen oder der Analyse solcher Ergebnisse lies [references/reproducibility.md](references/reproducibility.md). Historische Ergebnisse von außen prüfen; identische Designs und identische Kriterienurteile sind getrennte Aussagen.

Bei einem bereits zugewiesenen Rollenauftrag zuerst nur die zugehörige Karte unter `references/roles/` und die Auftragsdatei lesen. Vollständiger Workflow, Übergabeschema, Forschungsgeschichte und andere Rollenkarten gehören nicht automatisch in den Einstieg. Für Planung oder das Verfassen von Aufträgen/Übergaben lies [references/workflow.md](references/workflow.md); weitere Details nach Bedarf. Ein Verweis ist eine Nachlademöglichkeit, kein pauschaler Leseauftrag. Bei Reproduktionsaufträgen die oben genannte Reproduktionsreferenz zusätzlich nur für den eigenen Prüfumfang nutzen. Kleine Änderungen benötigen keinen mehrstufigen Forschungsablauf.

## Contractartefakte erstellen oder ändern

Nur beim Schreiben führender Originalartefakte: Lies [references/authoring.md](references/authoring.md) sowie die betroffene Definition. Bewahre die vier getrennten führenden Domänen und explizite Verbindungen zwischen Definition, Instanz, Teil und Zustand. Erfinde keinen neuen Universalstandard und keine unabhängige Zielimplementierung als zusätzliche Wahrheit.

Historische Forschungs-/Studienartefakte und eingefrorene Definitionen bleiben als Belege erhalten. Nutze für eine neue Revision eine eigene Kandidatenkopie beziehungsweise den vom Nutzer vorgesehenen neuen Bibliothekseintrag. Verändere bei einer eingefrorenen Eingabe weder Definition noch Erwartungen, um ein Zielbild nachträglich passend zu machen.

Fehlende fachliche Regeln werden als offene Entscheidungen ausgewiesen. Ein technisch erzeugbares Dokument ist kein Nachweis seiner Interaktion, Accessibility oder Plattformgleichheit. Erzeuge Zielartefakte nur im angefragten Ziel und mit tatsächlich vorhandenem Adapter/Werkzeug; erfinde keine funktionierende generische Abbildung.

Explizite Regeln nicht aus gestalterischer Plausibilität zu Wahlfreiheiten erklären. Element, Pseudoelement und geerbten Wert getrennt auswerten; ein eigener `::placeholder`-Wert wird nicht durch die Inputfarbe von `:disabled` ersetzt. Bewusste Quellabweichungen als solche melden. Neue belegte Fehler samt Gegenfall, Reparatur und Restgrenze im Projektregister `docs/skills/ISSUES.md` fortschreiben.

Bei Designausgaben: einfache Rechtecke, abgerundete Buttons, Kreise und Ellipsen direkt mit nativen Primitiven erstellen. Für datenabhängige Sektoren, Bögen oder zusammengesetzte Kurven – typischerweise Charts – die [Geometriehilfe](references/geometry.md) gezielt laden, statt Pfadkoordinaten zu schätzen.

Bei UX-Eignung oder Komponentenwahl die [UX-Referenz](references/ux.md) gezielt laden. Deklarierte Fähigkeiten sind kein Nachweis ihrer tatsächlichen Umsetzung.

## Prüfen und gegebenenfalls korrigieren

Lies [references/validation.md](references/validation.md) für die konkrete Prüfreihenfolge und den Browserablauf. Der portable Helper ist `scripts/contracts.py`; übergib `--repo` ausdrücklich, wenn das Arbeitsverzeichnis nicht im Zielrepository liegt.

- **Neue/geänderte Originalartefakte:** `inspect` führt unterstützte Syntax-/Originalschemaprüfungen sowie begrenzte Quellen-/Identitäts-/Aliasprüfungen tatsächlich aus. Auch bei gültigen Dateien lautet das Gesamtergebnis `BLOCKED`, solange kein passendes semantisches Profil und kein erforderlicher Laufzeitnachweis existieren. Bestandene Teilprüfungen separat berichten.
- **Unterstütztes Referenzpaket:** `validate --scope static` delegiert die vorhandene statische Prüfkette. Nur eine ausdrückliche statische Teilprüfung darf als `PASS_LIMITED`/`release:false` enden.
- **Gemeinsame Webprüfung:** `validate` verlangt ein explizites aktuelles `--browser-run`. Der Browseradapter akzeptiert ausschließlich die fest gebundene Paket-/Hostrevision. Neue oder auch nur statisch gültig geänderte Pakete dürfen alte Referenzcapturen nicht übernehmen.

Fehlt ein notwendiger Prüfer oder eine erforderliche Abdeckung, stoppe die davon abhängigen Schritte und die Freigabe. Syntax-/Schema-/Bindungsfehler sind keine Warnungen. Kandidatendaten dürfen korrigiert werden; danach müssen betroffene Prüfungen und notwendige abhängige Regressionen erneut bestehen. Ändere dafür weder Originalschemas, Profil/Prüfpolicy, Assertions noch Zeit-/Quellbindungen. Jede relevante Quellen-/Prüferänderung erfordert neue passende Nachweise.

Ein begrenztes erfolgreiches Webresultat ist nur für `releaseScope:exact-pinned-bounded-web-reference-only` zulässig. `productionRelease:false` bleibt sichtbar; fehlende Screenreader-, reale IME- oder Nativeprüfungen niemals als bestanden darstellen.

## Ergebnisvertrag

Liefere Artefaktpfade/Revision und Änderungen, tatsächlich ausgeführte Prüfungen samt Ergebnisdateien, bestandenen Umfang, blockierende Fehler/fehlende Abdeckung, Warnungen und ungeprüfte Teile. Der maschinenlesbare Helperbericht enthält `overall`, `release`, Diagnose und Umfang; prüfe seinen Inhalt zusätzlich zum Exitcode.

Exitcodes: `0` nur für den ausdrücklich begrenzten bestandenen Prüfumfang, `1` für Fehler, `2` für Blockierung. Ein `BLOCKED`-Entwurf kann als Entwurf übergeben werden, aber nicht als freigegebene Komponente. Frühere Gegenbefunde bleiben erhalten; Wiederholungen sind keine neuen Forschungsbedingungen.
