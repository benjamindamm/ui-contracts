# Rückwege und Draftlücken · 6. November 2026

**Neuer begrenzter Arbeitsweg:** Design- und Codebeobachtungen können als Ausgangspunkt für Contracts dienen. Unbekannte Entscheidungen bleiben Draftlücken. Ein deterministischer Check liefert aktuelle Quellenbezüge und stabile Rückfrage-IDs; er behauptet keine vollständige semantische Erschliessung.

[Nutzerentscheidung RD-003](../../decisions/RD-003-REVERSE-COVERAGE.md) · [Werkzeugeinstieg](../../../../tools/completeness/README.md) · [Skill-Rückwege](../../../../skills/ui-contracts/references/reverse.md).

## Was geändert wurde

- Bestehender UI-Contracts-Skill erhält einen kurzen Router zu Design-, Code- und Draft-Arbeitswegen. Die vier Domänen und ihr Quellvorrang bleiben erhalten. Keine vier parallel geladenen Skills oder neue UI-Beschreibungssprache.
- `tools/completeness/check.py` und eigene versionierte Profile/Recordschema prüfen die Zuordnung von Fragen zu Quellen. Zwei explizite Profile: interaktives Control und rein dekorative Darstellung. Unbekannte Profile/IDs und beliebiges N/A werden nicht still akzeptiert.
- Teil-Drafts können in diesem Check fehlende Domänen auslassen. Die bestehende Komponenten-/Originalschemaprüfung bleibt unverändert streng. Eine Verknüpfung allein oder eine nichtleere beliebige Stelle genügt nicht: endliche Formprüfungen erkennen unter anderem fehlenden CEM-Typ, falsche Transitionzuordnung und verlorene Labelbeziehung.
- Fragen-IDs bleiben bei Wiederholung erhalten. Quellen-/Komponentenänderungen öffnen betroffene Zuordnungen erneut. Kein Checklauf schreibt in Eingaben oder setzt den Komponentenstatus hoch. Fragenberichte liefern gezielte Klärungspunkte; technische Belegfehler soll der Agent zuerst selbst bearbeiten.
- Gemeinsamer Testtreiber enthält die neue Suite. Der gemeinsame Reportformatter gibt Coveragefragen in derselben JSON-Ausgabe wie den Status aus. Menschliche Einstiege in Dokumentation/Bibliotheken und aktueller Status verlinken den neuen Weg.
- Alter OpenPencil-Werkzeugeinstieg verwies noch pauschal auf `components/`. Er benennt nun die explizite Bibliothekswahl und den neuen Design-Rückweg. Eingefrorene Quellen und historische Belege bleiben unverändert.

## Tatsächlich ausgeführte Beispiele

Neue synthetische Testbibliothek unter `tools/completeness/examples/`; keine echte Figma-Datei und kein produktiver Import. Die Rohbeobachtungen bzw. TypeScript-Eingabe und die vorbereiteten Contracts sind als kleine Testeingaben erhalten. Semantische Gleichwertigkeit wurde nicht automatisch bewiesen.

| Fall | Ergebnis | Offene Fragen |
| --- | --- | --- |
| Nur Gestaltung zugeordnet | DRAFT_INCOMPLETE | 9, insbesondere API, Verhalten, Accessibility und UX |
| Code-/Verhaltenszuordnung | DRAFT_INCOMPLETE | 6, einschliesslich Namen, Fokus/Tastatur und UX |
| Escape-Konflikt | DRAFT_INCOMPLETE | BEH-003 bleibt blockierend |
| Alle Profilfragen belegt | COVERAGE_RECORDED | 0 Locator-/Coveragefragen; weiterhin Draft, Bedeutungs- und Zielprüfung nötig |
| Tatsächlicher Teil-Draft ohne Verhaltensdatei | DRAFT_INCOMPLETE | 11; keine Dummy-SCXML erforderlich |

[Finale CLI-Receipts](evidence/current/example-checks.json) binden Befehle, Exitcodes und Berichte. Die Kurz- und Vollausgabe enthalten dieselben offenen Frage-IDs. Der positive Zuordnungsfall ist ausdrücklich keine vollständige Selectdefinition: unter anderem fehlen ausgereifte Membership-/Fokusregeln. Das Ergebnis beweist also die Abdeckung des gewählten endlichen Profils, keine universelle fachliche Vollständigkeit.

Die Regression zur schrittweisen Klärung belegt: Nur BEH-003 schliessen reduziert neun Fragen auf acht; alle anderen IDs bleiben offen. `examples/README.md` zeigt, wie der Agent Bestätigung und Escape zu einer verständlichen Fachfrage bündeln kann. Keine unabhängige Agentenbefolgung wurde getestet.

## Regressionen und Kontext

- **35 finale neue Regressionen bestanden:** missing/stale sources, Teil-Drafts, leere/Platzhalterbelege, Quellenkonflikte, ungültige Profile/IDs/Statuswerte, fehlende Typen/Labelziele/Initialzustände, falsche Locatorarten, Verzeichnisgrenzen, Symlinks, Read-only-/Determinismus, explizite dekorative Ausblendung, einzelne Fragenauflösung und CLI-Ausgabe-/Überschreibeschutz.
- **Gemeinsamer Regressionstest:** 14 Suiten bestanden, `--unit-only`, release false. Seine Completeness-Suite enthielt zum Ausführungszeitpunkt 27 Tests. Anschliessend ergänzte Formprüfungen und Beispiele wurden mit der finalen 35-Test-Suite und frischen CLI-Berichten nachgeprüft; die anderen Suiten wurden unverändert übernommen. Keine Behauptung eines erneuten kompletten Browserlaufs.
- **Skillprüfung:** Quell- und installierter Skill mit dem offiziellen Quickvalidator bestanden. Vor Synchronisation waren beide Bestände hashgleich; vor dem Schreiben wurde die lokale Kopie erneut gegen diese Baseline geprüft. Danach identische Dateien. Skillkern: 3.037 Unicodezeichen, unter dem bestehenden lokalen 3.200-Zeichen-Budget. Das misst keinen gesamten Modellrequest.
- Die erste Quickvalidator-Ausführung mit der Projektvenv scheiterte an fehlendem PyYAML. Mit dem bereits vorhandenen Host-Python bestanden beide Prüfungen; keine Projektabhängigkeit wurde dafür geändert.
- Navigations-/Dateiverweisprüfung und Quellenhashes sind separat in [verification.json](verification.json) dokumentiert. Die gemeinsame Suite und finalen Einzelprüfungen stehen unter [tests](tests/results.json) und [finale Einzelprüfungen](evidence/current/final-completeness-command.json). Im Wurzelbereich von `evidence/` bleiben Zwischenstände und Skillprüfungen erhalten; für die finale Checkerversion führen die Berichte unter `evidence/current/`.

## Aufgedeckte Probleme und Reparaturen

**RC-001 · getrennte JSON-Ausgaben:** Der erste CLI-Entwurf gab Status und Fragen als zwei JSON-Dokumente aus. Der gemeinsame Formatter führt sie jetzt in einer maschinell lesbaren JSON-Ausgabe zusammen. Die CLI-Regressionsprüfung parst die gesamte Ausgabe und zählt sämtliche offenen Fragen. Die anfänglich fehlgeschlagene Testleselogik wurde entsprechend korrigiert.

**RC-002 · Locator allein zu schwach:** Ein nichtleerer Locator kann auf blosse Metadaten oder den falschen Feldtyp zeigen. Die endlichen Profil-Formprüfungen erkennen diese Gegenfälle. Falsche Zuordnung innerhalb passender Struktur bleibt eine ausdrückliche Grenze; `semanticReviewRequired:true` und Draftstatus wurden nicht entfernt.

**RC-003 · Metadatum als XML gelesen:** Der neue Gegenfall mit SCXML-Initialattribut statt Transition führte zunächst zu einer generischen Parserdiagnose. Vor dem Elementparser prüft der Übergangs-Formcheck jetzt die Elementgestalt und meldet gezielt `EVIDENCE_SHAPE_MISMATCH`. Der Gegenfall besteht.

## Verbleibende Grenzen

Keine allgemeine Figma-/Code-Synchronisation, kein Live-Editor-/GUI-/Screenreader-/IME-Nachweis, keine unabhängige Modellstudie und kein Nachweis der Workshopbeschleunigung. Der Checker beweist keine fachliche Absicht, vollständige Regelmenge, Originalstandardkonformität oder Wahrheit von Autorennotizen. Der Rückweg erfordert eine Quellenkarte und inhaltlichen Abgleich durch den Agenten bzw. fachlich Beteiligte. Eine bestätigte Änderung bildet eine neue Quellenrevision und braucht ihre betroffenen Zielprüfungen.

Kein Commit oder Push in diesem Arbeitspaket. Historische Studien wurden nicht verändert. [ARTIFACTS.json](ARTIFACTS.json) hält die Hashes der neuen Belege fest, ohne sich selbst zu hashen.
