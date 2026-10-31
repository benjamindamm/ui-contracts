# Aktive UX-Revision und abgesicherte Auswahl · 31. Oktober 2026

**Paket 1 und 2 umgesetzt im ausdrücklich begrenzten Umfang.** Die aktive example-Bibliothek enthält Select mit Suche und die verfeinerten UX-Merkmale. Eine reine Fähigkeitsbehauptung genügt nicht mehr für eine nachweisgestützte Empfehlung. Neue Quellen-/Identitäts-/Aliasprüfungen ergänzen den bisherigen Prüfeinstieg; Syntaxfehler bleiben vor späteren Blockiergründen sichtbar.

[Operativer Einstieg](../../../../tools/ux/README.md) · [Neue Belege](verification.json) · [Befundstatus](resolution-status.json) · [Ausgangspunkt: Framework-Audit](../FRAMEWORK-AUDIT-2026-10-31/README.md)

## Aktiver Aufbau

- `libraries/example/library.json` führt sechs Komponenten einschließlich **SelectWithSearch**, die eigene Bibliotheksrevision **0.3.0** und die explizite `selection`-Bindung zu Policy und Fähigkeitsschema.
- Die vier beteiligten `component.json`-Einträge verlinken ihre `ux.json`. Deren eigene Projektion ist auf Version **0.3** erweitert: Wertevertrag, Editierbarkeit, Suchmodus, Zweck und Verhalten unbekannter Eingaben bleiben getrennt. CEM, DTCG/CSS, SCXML und HTML/ARIA behalten ihre Originalsyntax.
- `verification.profile` wählt ein implementiertes Prüfprofil, behauptet aber keinen Erfolg. Der Checker führt aktuelle Prüfungen aus; ein selbst gesetztes Pass-Feld oder ein altes Receipt sind keine akzeptierten Nachweise.
- **Select, Input und SelectWithSearch:** aktuelle, begrenzte CEM-/HTML-Struktur-, TypeScript-Signatur- und native SCXML-Contractprüfungen. **Autocomplete:** derzeit `declared`. Der komplexe Invoke-/Hostpfad erhält keine pauschale aktuelle Abnahme aus einer anderen Referenz.
- Die Daten- und Quellenprüfung des Runners ist operativ. Die fachliche Rankinglogik bleibt in der **DMN-Datei** und wird von der gepinnten Originalengine ausgeführt, nicht durch eine zweite Python-Rankingimplementierung.

Der zugelassene Wertebereich bleibt entscheidend. Eine freie Adress-Schreibhilfe ist weiterhin ein eigener, noch nicht implementierter Vertrag. Der vorhandene Autocomplete bestätigt feste Ergebniskeys. [UX-Leitlinie](../../../ux/AUTOCOMPLETE.md).

## Behauptung, Nachweis und Zielabnahme

`verified-limited` heißt: die für das Profil unterstützten Signaturen und die statische Quellstruktur stimmen; die definierten positiven und negativen SCXML-Fälle wurden tatsächlich ausgeführt. Die Profile sind nicht an den Bibliotheksnamen example gebunden. Die Regressionen führen sie auch in einer separaten consumer-Bibliothek aus.

Für die Auswahl kritische Eigenschaften werden nur mit diesem Status als erfüllt an DMN übergeben. Ein unbekanntes Profil bleibt `unverified`. Ein bloßes `declared-only` wird nicht als eligible durchgereicht. Widersprüchliche Behauptungen oder fehlgeschlagene Contractfälle stoppen die Wahl mit FAIL. Fehlende fachliche Fakten bleiben unbekannt und führen zu `needs-clarification`; keine Konvertierung von „nicht bekannt“ zu false.

`interactionIntent` ist eine fachlich gesetzte Zweckzuordnung und wird ausdrücklich nicht als runtimebewiesene Eigenschaft geführt. Ebenso bleibt etwa ein vorhandener Filterprovider eine deklarierte Kontextvoraussetzung; der Runner beweist nicht die Wahrheit beliebiger mitgelieferter Fakten.

**Keine Produktfreigabe:** alle neuen Ergebnisse bleiben `release:false`; eine gewählte Komponente hat `targetValidationRequired:true`. Browseradapter, Fokus/Scrollen, reale IME, Screenreader, freie Typ-/SCXML-Semantik und Nativeplattformen sind nicht allgemein abgenommen. Ein erfolgreiches Quellen-/SCXML-Profil ersetzt die Prüfung des erzeugten Targets nicht. Endlich viele Gegenfälle sind kein formaler Beweis beliebiger ECMAScriptprogramme.

## Was konkret repariert wurde

| Befund | Umgesetzt | Restgrenze |
| --- | --- | --- |
| FW-001 | Die falsche Suchbehauptung aus dem Audit wird im aktiven Profil abgewiesen. Auch ein umbenanntes Suchprofil, gefälschte HTML-/CEM-Struktur, ein entfernter Membership-Guard bei ehrlich erneuerten Hashes sowie stilles Umsortieren werden geprüft. TypeScript-Records/Unionen werden strukturell verglichen; äquivalente Feld-/Literalreihenfolge ist erlaubt. | Unterstützte Prüfprofile und endlich viele tatsächliche Contractfälle; keine universelle Fähigkeitserkennung. |
| FW-002 | Such-Select und UX-Policy sind über den regulären aktiven Bibliothekseinstieg erreichbar. Veraltete Existenzhinweise wurden nur im neuen aktiven Stand korrigiert. | example bleibt eine bewusst begrenzte Bibliothek, kein fertiges Produktdesignsystem. |
| FW-003 | Eigene versionierte Mindestschemas und generische Quellen-, Zielart-, Identitäts-, Zustandsziel-, Kompositions- und Token-Aliasprüfungen. Der Inspector prüft seine Werkzeugvoraussetzungen direkt und benötigt dafür keinen bestandenen historischen Referenzlauf mehr. | Volle Typ-/Ownershipsemantik, CSS-Tokenabbildung und Targetabnahme bleiben offen. |
| FW-013 | Ein bereits erkannter Schemafehler behält Gesamt-FAIL und seine Hauptdiagnose. Zusätzliche Fontroot-/Checkerblockierungen werden separat geführt. | Es wird keine fehlende Prüfung zu pass umgedeutet. |
| FW-004 · Teilbeitrag | Java wird über PATH bzw. expliziten Parameter bestimmt; Runtimepfad ist explizit. Engine-JARs sind per Hash gepinnt; die Bridge wird aus Repositoryquelle frisch kompiliert. | Ein eigener Runtime-Provisionierungsweg und ein sauberer Clone-Test gehören weiterhin zu Paket 3. Kein vollständiger Portabilitätsnachweis. |

Die Ausgangsbefunde bleiben im früheren Audit erhalten. Aktuelle, begrenzte Zustände und Restarbeiten stehen separat in resolution-status.json; der Audit wird nicht nachträglich zu einer erfolgreichen Ursprungsprüfung umgeschrieben.

## Kontext klein halten

Die neuen CLIs geben standardmäßig kurze Zusammenfassungen aus. `--output NEUE_DATEI` hält den vollständigen Nachweis separat und liefert nur Pfad/Hash mit. `--details` lädt ihn ausdrücklich. Ein CLI-Gegenfall prüft die kleine Ausgabe und den vorhandenen vollständigen Beleg sowie den Schutz vor Überschreiben. Die neue Skillreferenz wird nur bei UX-/Auswahlaufträgen nachgeladen; AGENTS-/Claude-/Gemini-Einstiege wurden nicht vergrößert.

Die Repository-Skillquelle und die bereits identische lokale Installation wurden gemeinsam aktualisiert. Die Anweisungen erhalten keine zweite Policy-/Schemadatenkopie. Es wurden keine globalen Agenteneinstellungen verändert und keine neuen Worker oder Modellvergleichsläufe gestartet.

## Historie und Reproduktion

Vor der Übernahme wurde die vollständige **50-Datei-Eingabe von SELECTION-01 bytegleich** unter `docs/libraries/frozen/example-selection-01/` bewahrt. Metadaten und Originalmanifest liegen daneben unter `example-selection-01.json`. Das ist ein Archiv, keine zweite editierbare Bibliothek.

Der [externe Replay](replay_selection01.py) lädt den unveränderten ursprünglichen Helper und verlagert ausschließlich dessen Datenroot auf dieses Archiv. Er prüft zuerst Helper- und Eingabehashes und bestätigt dann die damalige Policy: **drei → Select, 30 → Autocomplete**. Das sind die damaligen Erwartungen, keine neue UX-Empfehlung. Im ursprünglichen inneren Resultat behalten Labels wie policySource ihren damaligen Locator; der effektive Datenroot ist im äußeren Replaybeleg ausdrücklich ausgewiesen. Die alte Enginevoraussetzung des historischen Helpers bleibt bestehen.

SELECTION-01/02, Originalprompts, Kriterien, Erstlieferungen, Reparaturen, frühere Captures und das 22-Datei-Archiv bleiben unverändert. Neue aktive Auswertungen übernehmen keine historischen Browserfreigaben. Die Tests vergleichen die vorhandenen alten getrackten Forschungs-/Belegbytes erneut gegen den Ausgangsstand.

## Tatsächlich ausgeführte Prüfungen

Der [maschinelle Abschlussbeleg](verification.json) enthält die aktuellen Zahlen und Hashes: **217 Testausführungen**, **47 statische Gegenfälle** und **18 Helperfälle** erfüllen ihre Erwartungen. Darin sind 37 Übergabefälle bewusst zweimal enthalten, für Quelle und Installation; diese Summe ist kein Zähler unabhängiger Forschungsbedingungen. Zu den neuen Fällen gehören:

- falsche Suchbehauptung und falsches Prüfprofil;
- nur scheinbar passende CEM-/HTML-Struktur ohne echte Suchlogik;
- entfernte Mitgliedschaftsprüfung, falsche Ereignissignatur und stilles Sortieren trotz neuer korrekter Quellenhashes;
- statisch editierbares Label in einer als nicht editierbar deklarierten Variante;
- fremde Bibliotheksfakten, fehlende Fakten und als Strings gelieferte Booleans;
- fehlende oder falsche Referenzen, Kompositionszyklen, Token-Aliaszyklen/-typkonflikte und doppelte Identitäten;
- Schemafehler vor zusätzlicher Blockierung und fehlende/abweichende Enginekonfiguration;
- tatsächliche Original-DMN-Auswahl für drei, 15, 16 und 30 Optionen sowie explizite Suche und fehlenden Provider;
- kleiner CLI-Kontext mit separat gespeicherter voller Evidenz und Schutz bestehender Dateien.

Bestehende Bibliotheks-, Font-, Übergabe-, Prozess-, Design-, Chart- und Präsentationsregressionen sowie die Originalformat-Helperfälle wurden erneut geprüft. Doppelte Ausführung des Übergabehelpers in Quelle und Installation ist im Beleg getrennt aufgeführt und kein zusätzlicher unabhängiger Forschungsfall. Es gab in diesem Arbeitspaket **keinen neuen Browserlauf**; die native SCXML- und Original-DMN-Ausführung sind tatsächliche neue Ausführungen.

### Erhaltene Vorbefunde während der Umsetzung

Die anfängliche Übernahme machte sichtbar, dass drei alte UX-Profile die ergänzenden A11y-Regeln noch nicht mitgehasht hatten. Die aktive Revision bindet sie nun ausdrücklich; die alten Profile blieben unverändert im Archiv.

Zwei Font-Integrationstests enthielten zuvor einen kopierten vollständigen Komponentenindex, aber keine dazugehörigen Komponenten. Die neue Bindungsprüfung wies dies korrekt zurück. Die aktuelle Font-only-Fixture deklariert nun keine nicht vorhandenen Komponenten; der unvollständige kopierte Index bleibt zusätzlich als eigener Negativfall erhalten. Bestehende Erwartungen wurden nicht gelockert.

Der erste Diagnoseanschluss verdrängte bei doppeltem JSON noch die ursprüngliche Fehlerdiagnose durch die neue Bindungsdiagnose. Der unveränderte Helper-Gegenfall erkannte dies. Die Reparatur erhält jetzt die vorhandene Hauptdiagnose und ergänzt den weiteren Fehler separat.

Ein zunächst verwendeter neuer Skriptname `select.py` kollidierte bei tatsächlicher CLI-Ausführung mit dem Python-Standardmodul. Vor der Veröffentlichung wurde der Einstieg `choose.py` verwendet; reale CLI-Ausführung ist Bestandteil der Regressionen. Diese Implementierungsanläufe sind keine Änderungen historischer Studienbedingungen.

## Weiter offen

Paket 3: gemeinsame Teststeuerung/Automatisierung, vollständige Runtimebereitstellung und wiederverwendbare tatsächliche Target-/Browserabnahme. Paket 4: einheitliche Studienaufträge, Änderungsfolgen und kontrollierter gestufter Modellvergleich. Zusätzliche UX-Fälle und ein freier Adressmodus benötigen eigene Definitionen. iOS/Android bleiben Zukunftsumfang.

Eine neue CLI-Testannahme verglich auf macOS zunächst den nicht aufgelösten /var-Pfad mit dem korrekten /private/var-Reportpfad. Der Test prüft nun die kanonische Dateidentität und weiterhin Beleginhalt, Hash und Überschreibschutz. Es wurde kein Toolergebnis passend zu einer falschen Pfadzeichenfolge verändert.
