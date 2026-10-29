# Fehlerregister · Ursachen, Reparaturen und Wiedererkennung

Ein Eintrag bleibt nach der Reparatur erhalten. „Setup repariert“ bedeutet eine aktuelle technische oder instruktionale Gegenmaßnahme mit Prüfung, **keine** Änderung des historischen Belegs und keine Garantie gegen alle zukünftigen Varianten. Noch fehlende technische Fähigkeiten bleiben sichtbar offen.

## R02 · 29. Oktober 2026

Führender Befund: [externe Analyse](../research/analyses/AC-R02/README.md), [reproduzierte Belege und Gegenfälle](../research/analyses/AC-R02/audit-results.json). Modelle des Laufs laut Nutzer: DeepSeek V4.1 Flash; getrennte Rollenmetadaten fehlen.

| ID | Fehler / Wiedererkennungsmerkmal | Ursache / ursprünglicher Beleg | Reparatur im aktuellen Setup | Regression / verbleibende Grenze |
| --- | --- | --- | --- | --- |
| R02-001 | Falscher disabled-Platzhalter wird als korrekt akzeptiert | AS15, ST10/COL08 in run-02; Quelle setzt `::placeholder` ausdrücklich auf muted | Quellvorrang im Skill; Zusatzchecker prüft sichtbaren Platzhalter unabhängig von Input-disabled-Farbe | `test_delivered_placeholder_detected`, `test_positive_source_correct_placeholder_passes_limited`. Historische Designs unverändert. |
| R02-002 | 9-px-Kontur besteht „1 px“-Check | GEO08 prüft nur Konturanzahl | Echter Vergleich `stroke.weight` im Zusatzchecker | `test_stroke_weight_counterexample`. Keine allgemeine Stroke-/Vektorprüfung behauptet. |
| R02-003 | Zweite Optionsschrift mit 28 px bleibt unbemerkt | TY02 prüft eine Beispieloption | Alle nativen Textgrößen/Familien/Zeilenhöhen innerhalb jedes Falls vergleichen | `test_second_option_font_counterexample`; Glyphmetriken bleiben ungeprüft. |
| R02-004 | Fehlerrot im normalen Inputwert besteht Farbprüfung | COL02 prüft nur Labels; COL11 nur Tokenzugehörigkeit | Farben nach fachlichem Einsatz prüfen, nicht nur Palettenmitgliedschaft | `test_input_color_usage_not_only_token_membership`. |
| R02-005 | `1,000` trotz unverglichener Pflichtmerkmale / fehlende Werte verschwinden | Selektiver Merkmalsvektor, `None` wird übersprungen; Protokollformel ungleich Implementierung | Zusatzvergleich zählt alle aufgezeichneten Schlüssel und meldet fehlende; kein allgemeiner Ähnlichkeitsscore | `test_pair_does_not_skip_missing_values`; Traversierungsreihenfolge und explizite Abdeckungsgrenze bleiben dokumentiert. |
| R02-006 | Manuelles Urteil erscheint als neu gemessener pass | Konstante Wahrheitswerte in `verify.py`, unter anderem A08/TY05/A11Y | Automatik-/Manual-/notChecked-Trennung vorgeschrieben; reale Inputhashprüfung und erneuter Readback vor aktuellem Ergebnis | Profil-Tests für geänderte Quellen/Toolchain; `audit.py` prüft tatsächliche Hashes. Historischer Checker wird nicht verändert. |
| R02-007 | Canvas wird an nicht vereinbartem ARIA-Annotationsformat gemessen | Abgeleitete A11Y-Kriterien ohne verbindlichen nativen Metadatenkanal; Dump erfasst kein pluginData | Aktueller Zusatzchecker führt statische Semantik und Runtime-AX als **notChecked**; Skill verbietet daraus pauschales pass/fail | Falscher Freigabeanspruch verhindert. **Offen:** eigener Semantikvertrag samt tatsächlichem Roundtrip-Validator. Nicht als umgesetzt ausgeben. |
| R02-008 | Erfolgreicher dritter Abschnitt zählt als dritter „Stopp“ | Review/results nennen drei; Laufprotokoll enthält zwei Abbrüche pro Builder | Start/stop/resume/complete-Ereignisse mit Stopverweis und Checkpointdatei; neuer Metadatenprüfer | `test_completion_not_extra_stop`, `test_neutral_continuation`. Historische exakte Schrittzahlen bleiben unbekannt. |
| R02-009 | Modellrangfolge trotz fehlender Rollenmetadaten und unterschiedlicher Prüfmaßstäbe | Modell/Reasoning/Prompts nicht im Lauf; andere Kriterien als run-01 | Gemeinsamer eingefrorener Prüfkern für beide Läufe; Metadatenvertrag je Rolle, Unknown blockiert Vergleichsanspruch | `test_unknown_model_not_inferred`, `test_missing_historical_metadata_blocks`; vollständige damalige Konfiguration nicht rekonstruierbar. |
| R02-010 | Nachcoaching oder geänderter Fortsetzungsauftrag ist nicht prüfbar | Fortsetzungstexte und entfernte Zwischenartefakte fehlen | Exakte Prompt-/Skill-/Fortsetzungsdateien mit Hash; neutrales Resume; semantische Änderungen explizit markieren | `test_prompt_hash_detects_drift`, `test_coaching_changes_condition`. Kein Hash beweist Zugriffstrennung oder historischen Zeitpunkt. |
| R02-011 | Prüfer kann Definitionsrevision nicht nachrechnen | Hashalgorithmus nicht in erlaubten Eingaben | Technischer Laufvertrag dokumentiert Algorithmus; `audit.py` rechnet den tatsächlichen Hash nach | `audit-results.json` bestätigt Revisionshash. Künftigen Agenten muss dieses technische Laufblatt tatsächlich erlaubt werden. |
| R02-012 | Token-/Font-/ZIP-Unterschiede verfälschen Bewertung | B kopiert Token falsch, meldet Fallback; ZIP-Zeiten unterscheiden Bytes | Tokenabweichung bleibt als Warnung sichtbar; Fontnachweis und Byte-/Semantik-/Bildvergleich getrennt vorgeschrieben | `test_one_channel_token_drift_visible`. **Offen:** portabler Font-/Glyphmetriken-Nachweis; archivierte Generatoren bleiben unverändert. |
| R02-013 | Textdefinition widerspricht Zeilenarithmetik | README nennt drei unsichtbare Zeilen; 7×32−160 ergibt zwei | Externe Errata dokumentiert; Skill verlangt Konfliktbericht statt stiller Wahlfreiheit | **Offen für neue Definitionsrevision:** Text korrigieren und `{count}` explizit festlegen. Eingefrorene `components/` bleiben erhalten. |
| R02-014 | Skills sollen verbessert werden, ihre tatsächliche Nutzung ist aber unbelegt | Erlaubte Laufeingaben nennen Skill nicht; kein Read-/Versionsreceipt | Skill-Dateihashes oder explizite Nichtnutzung im Rollenprotokoll | `test_missing_historical_metadata_blocks`; keine rückwirkende Schuldzuweisung an einen unbewiesen geladenen Skill. |

## Verifikation der aktuellen Gegenmaßnahmen

- [12 Regressionen](../../tools/design-review/test_review.py) für den begrenzten nativen Zusatzchecker; positive und negative Gegenfälle, keine Originaländerung.
- [7 Regressionen](../../tools/design-review/test_process.py) für Rollen-/Prompt-/Unterbrechungsmetadaten.
- Aktuelle Gegenprüfungen derselben 22 Definitionen und gepinnten Toolchain: [run-01](../research/analyses/AC-R02/static-countercheck-run01.json), [run-02](../research/analyses/AC-R02/static-countercheck-run02.json). Jeder der vier Builder hat die gleiche explizite Platzhalterabweichung; B von run-02 zusätzlich drei Kanalabweichungswarnungen beim Inputrahmen.
- Keine neuen Prozentwerte oder vollständige Design-/Accessibilityfreigabe. Die Zusatzprüfung ist enger als eine vollständige Abnahme; ihr Bericht nennt `covered` und `notChecked`.

## Neue oder wiederkehrende Fehler

Bei neuem Befund mindestens festhalten: ID, Datum, betroffene Revision, exakter Beleg, führende Sollquelle, beobachtetes Ist, Ursache (belegt / Hypothese), Reproduktionsschritte, isolierter Gegenfall, Reparaturdateien, ausgeführter Nachweis und verbleibende Grenze. Bei Wiederauftreten den neuen Beleg ergänzen und die bisherige Gegenmaßnahme hinterfragen; frühere Ergebnisse nicht überschreiben. Fehlende Daten niemals als nachträglich verifiziert markieren.

## W01 · Wissensübergaben und Kontext · 29. Oktober 2026

Diese Einträge beschreiben präventive Gegenmaßnahmen zur beschlossenen Skillweiterentwicklung [RD-001](../research/decisions/RD-001-STAGED-GENERATION.md). Sie behaupten nicht, dass die genaue Ursache der HTTP-413-Abbrüche von run-03 bereits diagnostiziert oder behoben ist. Requestgrößen und vollständige Fehlerantworten fehlen weiterhin.

| ID | Mögliche Fehlerquelle | Umgesetzte Gegenmaßnahme | Funktionaler Nachweis / Grenze |
| --- | --- | --- | --- |
| W01-001 | Zu breite Aufträge und komplette fremde Gesprächsverläufe überlasten den Kontext | Fünf selektiv geladene Rollen-Karten; Kontextpaket aus Auftrag, relevanten Quellen und ausgewählten Claims | `test_context_does_not_inline_source_or_artifact`, `test_only_selected_claims_transferred`; bessere Modellleistung noch nicht empirisch belegt. |
| W01-002 | Verdichtete Vorgängerannahme wird zur scheinbaren Originalregel | `explicit/derived/assumption/observation`, Quellenlocator und Belegverweise; Originale führen | `test_rule_needs_original_source`, `test_assumption_stays_labeled`, `test_observation_needs_evidence`; keine automatische semantische Wahrheitsprüfung. |
| W01-003 | Nachfolger konsumiert veraltete oder unvollständige Lieferung | Hashgebundener Produzentenauftrag, Quellrevision, Handoffrevision und Input-Receipts; partial blockiert benötigte Verbraucher | Tests für stale artifact/dependency, partial dependency und receipts; keine technische Zugriffssandbox. |
| W01-004 | Erklärungen des Builders prägen das unabhängige Urteil vor | Blindphase ohne Handoffs/Reports; Reportabgleich als eigener Task nach hashgebundener Erstbewertung | `test_blind_reviewer_rejects_handoff`, `test_blind_reviewer_rejects_builder_report`, `test_report_check_requires_frozen_first_review`; falsch klassifizierte oder eingebettete Texte bleiben menschlich zu prüfen. |
| W01-005 | Fertigmeldung ohne erforderlichen Nachweis | `ready` nur mit Artefakt, Pflichtchecks mit Beleg und ohne blockierende Frage; stets `release:false` | Positive/negative Status-, Beleg- und Frage-Tests; Beleginhalt und wirkliche Ausführung weiterhin separat prüfen. |
| W01-006 | Große Übergabe wird unbemerkt abgeschnitten | Explizite Zeichenbudgets, Blockierung statt Trunkierung; Details bleiben nachladbar | `test_context_overflow_blocks_instead_of_truncation`, `test_handoff_overflow_blocks`; kein Nachweis einer sicheren HTTP-/Tokenobergrenze. |
| W01-007 | Parallele Arbeit überschreibt Quellen, Fremdartefakte oder alte Receipts | Getrennte Schreibbereiche, Hashkontrolle, keine vorhandene Helperausgabe überschreiben | Output-/Pfad-/CLI-Tests; Koordinator muss Schreibbereiche verschiedener Tasks zusätzlich planen, der Helper sperrt Dateizugriffe nicht. |

[32 Funktionstests](../../tools/skill-tests/ui-contracts/results-handoffs.json) · [Workflow-Verifikation](../../tools/skill-tests/ui-contracts/workflow-verification.json) · [Übergabevertrag](../../skills/ui-contracts/references/handoff-contract.md). Keine ursprünglichen Forschungsbedingungen hinzugezählt und keine alten Belege verändert.

## W02 · Initialer Kontext · 29. Oktober 2026

| ID | Befund / Risiko | Reparatur und Nachweis | Restgrenze |
| --- | --- | --- | --- |
| W02-001 | Rollenrouting konnte Workflow, Schema und eigene Karte vor Fachquellen auslösen; mögliche Kette 17.492 Zeichen | Direkter Rolleneinstieg, Bootstrap nur mit Pfaden/Hashes; [Audit](../research/analyses/INITIAL-CONTEXT/README.md) und fünf neue Funktionstests | Keine Messung des vollständigen tatsächlichen Modellrequests. |
| W02-002 | Der verfügbare Delegationsaufruf übernimmt standardmäßig Elternhistorie | Workflow verlangt für unabhängige Worker explizit `fork_turns="none"` und Protokollierung | Kein technisches Dispatch-/Zugriffsgate; frühere Läufe dadurch nicht nachträglich als falsch bewertet. |
| W02-003 | Ein Paketlimit kann irrtümlich als gesamtes Kontext-/Tokenlimit gelesen werden | Bootstraplimit auf komplette JSON-Datei getestet; Skill, spätere Dateilesungen und Plattformkontext ausdrücklich getrennt | Erweiterte Kontextpakete haben weiterhin ein Inhaltslimit; tatsächliche Tokens/Requestbytes im Pilot zusätzlich erheben. |

Keine nachgewiesene Reparatur der HTTP-413-Ausfälle. Die ursprünglichen Studien und der bisherige 32-Test-Beleg bleiben erhalten.


Zusätzlicher Hostbefund:

| ID | Risiko | Gegenmaßnahme | Grenze |
| --- | --- | --- | --- |
| W02-004 | Unterschiedliche Hosts laden andere Projekt-/Globaldateien und Erinnerungen | Gemeinsame kurze AGENTS.md, dünne CLAUDE.md/GEMINI.md-Wegweiser ohne automatische Imports; [Host-Prüfverfahren](../research/analyses/INITIAL-CONTEXT/ENTRYPOINTS.md) | Statische Prüfung bestanden; reale Startladung und globale Regeln pro konkretem Host noch zu messen. |

## L01 · Unabhängige Bibliotheken · 29. Oktober 2026

| ID | Fehlerquelle | Reparatur | Nachweis / Grenze |
| --- | --- | --- | --- |
| L01-001 | components war zugleich Beispiel und implizite einzige Autorenbibliothek | Bytegleiche Migration nach libraries/example; Auswahl über libraries/ID, Leerstart per manage.py init | Leere Tokens/Komponenten, getrennte Libraries, unveränderte 22 Dateihashes getestet. |
| L01-002 | Pfadmigration könnte alte Studien umschreiben oder ihre Hashbindung abschwächen | Alte Manifeste unverändert; explizite Legacy-Pfadauflösung mit weiterhin striktem Dateihash; Gegenprüfer bindet example | Legacy-/Stale-Hash-Tests und run-04-Gegenprüfung; alte Werkzeughashes bleiben an alte Revisionen gebunden. |
| L01-003 | Ausgabe eines Rollenauftrags könnte Quellen einer anderen Library überschreiben | Quellen-/Receipt-Schutz auf alle libraries ausgedehnt; Handoff-Ausgabeordner darin abweisen | Negativer Cross-Library-Ausgabetest plus positiver eigener work-Ordner. Keine technische Zugriffssandbox. |

[Migration, Dokumentationsumfang und Testbelege](../libraries/MIGRATION.md). Keine neue Modellgeneration oder allgemeine Komponentenfreigabe.
