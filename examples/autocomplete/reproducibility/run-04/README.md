# run-04 · Autocomplete-Reproduktionslauf · 2026-10-29

Zwei unabhängige Builder und ein unabhängiger Prüfer, alle mit frischem Kontext (keine Elternhistorie), ein einziger eingefrorener statischer Gegenprüfer. Ergebnis: beide FIGs bestehen die eingefrorene Gegenprüfung ohne Abweichung; die Reportabgleich-Phase bestätigt 21/21 Claims ohne Widerspruch. `release: false` durchgehend; kein Commit, kein Push.

## 1. Ergebnis (Kurzform)

| Stufe | Ergebnis | Beleg |
|---|---|---|
| Builder A → Handoff | `HANDOFF_READY` (Builder- und Koordinator-Receipt) | `builder-a/check-receipt.json`, `builder-a/coordinator-check.json` |
| Builder B → Handoff | `HANDOFF_READY` (Builder- und Koordinator-Receipt) | `builder-b/handoff-check-receipt.json`, `builder-b/coordinator-check.json` |
| Countercheck (Prüfer, Blindphase) | Exit 0, `PASS_LIMITED` je FIG, 0 Failures/Warnings, Paar 572/572 exakt | `review/countercheck-receipt.json` |
| Unabhängiges Reviewer-Readback | 449/449 Checks je FIG | `review/readback-reviewer.json` |
| Eingefrorene Erstbewertung | 364 Soll/Ist-Zeilen je FIG, alle pass; Paar: 0 normative Differenzen | `review/first-review.json` (frozen) |
| Countercheck (Koordinator, Kreuzlauf) | Exit 0, `PASS_LIMITED`, identisch zum Prüfer-Receipt | `coordinator-countercheck.json` |
| Blind-Handoff → | `HANDOFF_READY` (Koordinator-Receipt) | `review/coordinator-check-blind.json` |
| Report-Check → | 21/21 Claims bestätigt, 0 Widersprüche, 0 unbelegte Pässe; No-Override: `first-review.json` unverändert, kein Nachtrag erforderlich | `review/report-check/REPORT.md`, `review/report-check/coordinator-check.json` |
| Provenienz-Metadaten | `METADATA_COMPLETE` (0 Fehler) | `process-check-receipt.json` |

Hinweis: Wertgleichheit ist kein Korrektheitsbeweis; `PASS_LIMITED` ist ein begrenzter statischer Nachweis ohne ARIA-/Runtime-Aussagen. Die Policy-`notChecked`-Liste bleibt gültig (vgl. `policy.json`).

## 2. Eingefrorene Eingaben (vor allen Outputs)

| Eingabe | SHA-256 | Anmerkung |
|---|---|---|
| Definitionsrevision (22 Dateien unter `components/`) | `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727` | Referenz `autocomplete-openpencil-0.1.0`; intakt verifiziert |
| `input-manifest.json` | `74aa9eabcfe7301a0845d230cc1ff4acd6ce14cf0435ec1ed0e6cba0b6e25eb2` | 22 Originaldateien mit Hashes |
| `run.json` | `fdb5368d67034fa4e95f04056ab1b808d92a294a31ed04fd93568b2021214847` | `definitionFiles` == Profil-Map (Anforderung von `check.py`) |
| `policy.json` | `8656349c4af0ae48568e462bd481b257ec002968fd8b9cd5072c9f673c56fb98` | Id `ac-run04-static-countercheck-01`; bindet `check.py`, `read-fig.mjs`, `profile.json`; Toleranzen ±0.01 px, Farbkanal-Drift ≤3 = Warning, Paarexaktvergleich ohne Ähnlichkeitswert; `frozenBeforeOutputs: true` |
| Toolchain-Lock | `ebdba8523251984285705a8b03bc15220d41773131b72c66e7a05706837749e6` | OpenPencil core/scene-graph 0.16.0; verifiziert |
| `runsheet-technical.md` | `3ee3d5707c9271be61a5356ff676e34850f9d5b91c3010036ff1945198e7e496` | Hashalgorithmus, Toolchain-Nutzung, Lesegrenzen, Receipt-Regeln |
| Review-Specs (vor Outputs eingefroren) | `task-blind.spec.md` `f2abba27…`, `task-report.spec.md` `35ebdf2b…` | Formale Tasks werden nach Lieferung aus den Specs instanziiert (dokumentierte technische Notwendigkeit: FIG-Hashes existierten vorher nicht) |
| Werkzeugtests (vor Dispatch) | — | `test_review.py` 12 OK, `test_process.py` 7 OK |

Keine früheren Laufergebnisse (run-01..03, `examples/autocomplete/output|review`, `docs/research`) wurden als Vorlage für Builder oder Prüfer verwendet.

## 3. Rollen, Kontexte und Modelle

| Rolle | Session (frisch) | Auftrag | Initial-Prompt (frozen) |
|---|---|---|---|
| Builder A | `ses_e782e5013ffe7oJTqrGPIGJfX7` | `builder-a/task.json` (`051a1474…`) | `prompts/builder-a.txt` `9a1e3797…` |
| Builder B | `ses_e782e5012ffeaELX5uRA1UH6XD` | `builder-b/task.json` (`1dac121a…`) | `prompts/builder-b.txt` `aa0249bc…` |
| Prüfer | `ses_e780199c8ffeJrMeoPzs58w2Qj` | `review/task-blind.json` (`68faf096…`), dann `review/task-report.json` (`66397f4c…`) | `prompts/reviewer-blind.txt` `ebb7ab9d…`; Fortsetzung `prompts/reviewer-report.txt` `b14df1eb…` |

- Alle Subagent-Sessionen wurden ohne `sessionID` gestartet (frischer Kontext, keine Elternhistorie); der Model-Parameter wurde nie gesetzt.
- Modellidentität wurde gemäß Laufanweisung **bewusst nicht recherchiert**; in `run-process.json` als nicht-identifizierende Werte dokumentiert (`configured-default (identity not researched per run instruction)`, Revision/Reasoning `not-researched`).
- Prüfer: zwei formale Tasks in einer Session (Blindphase, dann Report-Check) als dokumentierte Fortsetzung gemäß `task-report.spec.md` (Kontextregel); keine semantische Nachsteuerung; keine Stop/Resume-Events (keine Unterbrechung aufgetreten).
- Skill-Bindung pro Rolle (Rollenkarten, hashgebunden): builder.md `8497e284…`, reviewer.md `50aee08a…`.
- Harness: opencode v2.2.1 (Subagent-Kind-Sessionen), keine erzwungene Schrittgrenze.

## 4. Zeitachse (UTC, Datei-Mtime-Evidenz)

| Zeit | Ereignis |
|---|---|
| 13:17:26Z | `run.json` + `policy.json` eingefroren |
| 13:18:18Z | Review-Specs (`task-blind.spec.md`, `task-report.spec.md`) eingefroren |
| 13:19:09–18Z | Builder-Tasks erstellt, Bootstraps `BOOTSTRAP_READY` |
| 13:19:39Z | **Builder A und B gestart** (Prompts eingefroren, gleichzeitiger Dispatch) |
| 14:03:15Z | Builder A fertig (letztes Artefakt: `check-receipt.json`) |
| 14:04:09Z | Koordinator-Check A: `HANDOFF_READY` |
| 14:06:26Z | Builder B fertig |
| 14:07:15Z | Koordinator-Check B: `HANDOFF_READY` |
| 14:08:17–50Z | Blind-Task instanziiert + gebootstrapt; **Prüfer gestartet** |
| 14:12:49Z | Countercheck-Receipt (Prüfer) geschrieben |
| 14:33:21Z | Reviewer-Readback (449/449 je FIG) |
| 14:36:02Z | **`first-review.json` eingefroren** (vor jeglichem Reportzugang) |
| 14:40:22Z | `handoff-blind-v1.json`; 14:41:18Z Koordinator-Check: `HANDOFF_READY` |
| 14:44:11–18Z | Report-Task instanziiert + gebootstrapt (`BOOTSTRAP_READY`) |
| 14:45:23Z | Fortsetzungsprompt eingefroren; Report-Check in derselben Prüfer-Session gestartet |
| 15:17:47Z | Report-Check fertig; 15:18:37Z Koordinator-Check: `HANDOFF_READY` |
| danach | `run-process.json` + `process-check-receipt.json` (`METADATA_COMPLETE`), Koordinator-Kreuzlauf `check.py`, dieses README |

## 5. Abweichungen vom eingefrorenen Plan (dokumentiert)

1. **Report-Task-Ausgabeordner:** Die eingefrorene `task-report.spec.md` nennt `outputs: run-04/review`. Der Helper verbietet strikt, dass eine Aufgabeingabe im eigenen Ausgabeordner liegt (`input overlaps own output directory`); die Report-Check-Phase verlangt zwingend eine hashgebundene `first-review`-Input — und die eingefrorene `first-review.json` muss in `review/` bleiben (No-Override). Die formale `task-report.json` setzt daher `outputs: run-04/review/report-check/` (alle neuen Artefakte bleiben im Review-Bereich). Sämtliche inhaltlichen Eingrenzungen (goal, scope, acceptance, inputs, sources) sind unverändert aus der Spec übernommen.
2. **Späte Instanziierung der Reviewer-Tasks:** Die FIG-Hashes existierten vor der Lieferung nicht; die formale `task-blind.json`/`task-report.json` wurde nach Lieferung aus den vorab eingefrorenen Specs instanziiert. Die Eingrenzungen stammen vollständig aus den Specs.
3. **Koordinator-Receipts:** Jeder `handoffs.py check`-Aufruf (Helper- und Koordinator-Ebene) schreibt an einen frischen Temp-Pfad; die empfangene JSON wird danach als Receipt in den Laufordner kopiert (Helper verweigert existierende Ausgabe-Pfade und Schreibzugriff in die Laufbereiche).

## 6. Lieferungen und Hashes (SHA-256)

### Builder A (`builder-a/`, Aufgabe `ac-run04-builder-a`)
| Datei | SHA-256 |
|---|---|
| `autocomplete.fig` (31 635 B, 1 Seite, 156 Nodes) | `974ecd154e27b816a0410c354e5d655eb4ca27d22a02f3b3de9d88a6e1eaf6dc` |
| `readback.json` (6 Checks, 197 Fidelity-Stichproben, 0 Fehler) | `01c729a2f24fbe0953aeb49532eabd8175718bc92944c4c2938c2ccb58cef6c3` |
| `REPORT.md` | `fa40a84f6ca21e22beec9a913ec0e3b337ab61f524cfb815f022ae79b963765a` |
| `handoff-v1.json` (status `ready`) | `06c18fee9592256b345022d21246be51f63ed37915c1f8eae68cb3f106f0e5b3` |
| `build-fig.mjs` / `readback.mjs` | `d463c18b26699e36276dcac9c08c049799a85026345c0959821515d3b3dd7680` / `cc770f5fd8e49873421da10a80af645efa83687b863820e86f98a073377a27be` |
| `check-receipt.json` = `coordinator-check.json` | `8dc7034f8e567bf9d6f7ecd8ec398433fe9e97bdb10ffa78492f348f0cf23daa` |
| `task.json` / `bootstrap.json` | `051a14745998d9fffba819666860e7c0718108180d0718ca5bd2bab98b1d9356` / `3bcb3618bbb4f9816d8d1e39329c0d9f09ef9008f7f1dea6973a11f7593f0f3f` |

Wesentliche Beobachtungen (im Report/Handoff dokumentiert): `enabled` liegt in `stories.json` unter `inputs.enabled` (nicht top-level); `exportFigFile` ist nicht bytestabil (pro Lauf erzeugte Dokument-Ids + ZIP-Zeitstempel; Inhalt deterministisch — Readback ist der Zuverlässigkeitsnachweis).

### Builder B (`builder-b/`, Aufgabe `ac-run04-builder-b`)
| Datei | SHA-256 |
|---|---|
| `autocomplete.fig` (31 501 B, 1 Seite, 163 Nodes) | `4972198fe30b878f6e16733450c45acd9fbe4362235c590fce8016b40e6e47df` |
| `readback.json` (5/5 Checks, gepinnte Core 0.16.0) | `b817525e0cb81595b9ad757930e505b76b4e83f659847826f6e381180c5647c1` |
| `REPORT.md` | `9d611f8656bdd70fd84344a1afc9e085f2e4549fd0ae76566ef463f81de099aa` |
| `handoff-v1.json` (status `ready`) | `e519d69142cab7e4c90e5190e2bef92785b07b4abc7caf31b5614cd5ed1f325d` |
| `generate-fig.mjs` / `readback.mjs` | `d1ed3c6e0cca04d815f6c961443758b80144f99eb3410213bf6a31ba340c796d` / `d3e810c847c5330bbac6c37f186a93f535662e9df4e802b345e1df02f0022ec9` |
| `handoff-check-receipt.json` = `coordinator-check.json` | `58eb865feb451692f6bfa4472bb48a1cbd2500dc9853612045e87c174f76134b` |
| `task.json` / `bootstrap.json` | `1dac121a371793add151e5126f6fc9b77b5f81eac7a67df7851d203b8f795f79` / `939fe3f076a1d1e95ac58ff233081ad4489915cfa56d98b63495e75a1add179d` |

Wesentliche Beobachtungen: 7 dokumentierte Gaps (u. a. keine CSS-Regel für die Meldungszeile, kein font-weight in den Quellen, keine Scrollbar-Definition); 1 offene, nicht blockierende Frage `q-msgrow-color` (Antwort in `review/report-check/REPORT.md` §5.2: Quellen normieren keine Muted-Farbe; gemessenes `#172B4D` ist der geerbte text-Token; eine Muted-Entscheidung wäre eine neue Definitionsrevision).

### Prüfer — Blindphase (`review/`)
| Datei | SHA-256 |
|---|---|
| `countercheck-receipt.json` (check.py, Exit 0, PASS_LIMITED, Paar 572/572) | `ca0b47ab5c6f02b82a76ae7318d3b159a8a9b6f75ec1c458ff95a609c95382d4` |
| `readback-reviewer.json` (449/449 Checks je FIG) | `4b80cc36d48889e660b6ec7a67b630b14e9e9c00cd8366c1fafa02df33494f3b` |
| `first-review.json` (**frozen**, 364 Zeilen/FIG, release:false) | `99a6589c83663bb6d37ab455a0feddc4bd272be4274f99674d1d321d727f148b` |
| `handoff-blind-v1.json` (`ready`) | `05cd0d2bd14a97f557524e0f7e583ba543cff378dd057abeabb74b2b949e22d1` |
| `task-blind.json` / `bootstrap-blind.json` | `68faf096a29a353fe2a1aea0e7d1937db776b13d92c5291000c99828bbd2555b` / `990f76c52419f4346f3b4659f68acb681e7d64df7d95dc601d3c4f069c672b01` |
| `coordinator-check-blind.json` | `788dbb7933d1bf8ab7a3c8d4cfde4745eeb693cc38484a226d37e8ab48586e3f` |

Blindphase-Nachweis: Die Prüfer-Inputs umfassten nur Originalquellen, Policy, Laufblatt, hashgebundene Werkzeuge und die beiden FIGs; `first-review.json` wurde (Mtime 14:36:02Z) vor dem ersten Zugriff auf Builder-Handoff/-Report geschrieben.

### Prüfer — Report-Check (`review/report-check/`)
| Datei | SHA-256 |
|---|---|
| `REPORT.md` (21/21 Claims bestätigt, 5 Anmerkungen, Gap-Verifikation) | `05bb3c9a9b293cf1212067ff923136ae13e35b6c653bdc64cbd5a5d70d625cf2` |
| `handoff-report-v1.json` (`ready`, 0 Fragen) | `72387f0e1cde7d40aad562c04b28182b75d0bd836f4918b8d240eaedbcd3af3b` |
| `handoff-check-receipt.json` = `coordinator-check.json` | `35505d9b38a1c5c4b409e3111c024f82a9993166ac84ab2a95a821ff6679c66d` |
| `task-report.json` / `bootstrap-report.json` | `66397f4c846d7e34e7caa56c338ca9b2424920acf3b0adf18450140eb200117a` / `1124a8338824eea55ca172702dd080630b914e917102726f394d532a36ba6669` |

**No-Override:** `first-review.json` nach der Report-Check unverändert (Hash `99a6589c…` re-verifiziert); kein Nachtrag erforderlich (`first-review-addendum.md` wird nicht erzeugt), da kein Fehler in der Erstbewertung gefunden wurde.

### Laufebene
| Datei | SHA-256 |
|---|---|
| `run-process.json` | `d149e36c6ad0c8327a8ff74da4e886c1e67146a799db9fdb3402f2d6b887839d` |
| `process-check-receipt.json` (`METADATA_COMPLETE`, 0 Fehler) | `361f8aec345574e7b760592a6985ff7f8b6e23e2224d533acc786e1de1645fb7` |
| `coordinator-countercheck.json` (Koordinator-Kreuzlauf, Exit 0) | `ca0b47ab5c6f02b82a76ae7318d3b159a8a9b6f75ec1c458ff95a609c95382d4` |
| `prompts/builder-a.txt` / `builder-b.txt` / `reviewer-blind.txt` / `reviewer-report.txt` | `9a1e3797…` / `aa0249bc…` / `ebb7ab9d…` / `b14df1eb…` (Vollhashes in §3) |

## 7. Wiederholbarkeit und Grenzen

- **Vergleichsbasis:** exakte Werte auf den in der Policy festgelegten semantischen Keys (Toleranzen nur für Pixel-Dimensionen ±0.01 px und Farbkanal-Drift ≤3 als Warning; Texte/Meldungen exakt; Paarexaktvergleich, fehlende Werte sind Unterschiede). Kein Ähnlichkeitswert.
- **Nicht geprüft (Policy `notChecked`):** vollständige Geometrie und Scroll-Offsets, Schatten, gerenderte Glyph-Metriken, statische semantische Annotationen, GUI-Edit-/Save-Roundtrip, Runtime-Verhalten und ARIA-Zugänglichkeit, Prozessunabhängigkeit.
- **Nicht bytestabil:** `exportFigFile` erzeugt pro Lauf neue Dokument-Ids (in Node-`source`-Records) und ZIP-Zeitstempel; Bytegleichheit zwischen Builds ist nicht zu erwarten (Builder-A-Befund, quellenkonsistent). Reproduktionsnachweis ist der Readback, nicht die Bytefolge.
- **Provenienz-Einschränkung:** Die Hashes in diesem README und in den Receipts belegen die Integrität der aktuellen Dateizustände; sie sind kein Authentizitäts- oder Zugriffs-/Timing-Nachweis. `run-process.json` dokumentiert die Vergleichbarkeitsmetadaten (Modelle nicht-identifizierend), keine Aussage über die Unabhängigkeit der Prozesse.
- **Kein Commit, kein Push:** Der gesamte `run-04/`-Ordner ist unveröffentlichter Arbeitsbaum-Inhalt.
