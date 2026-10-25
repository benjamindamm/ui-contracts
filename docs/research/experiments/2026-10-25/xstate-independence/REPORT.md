# XState: unabhängig geführter SDK-Verhaltensbeitrag

Stand: 25. Oktober 2026. **X01 A/C501**, begrenzt auf den nachgewiesenen getrennten Web-Forschungsfall. **40 U: 25 Integration, 15 weitere. 443 Bedingungen in 57 Gruppen.**

## Gegenstand und unverändertes Kriterium

X01 prüft unabhängig beschreibbare Domänen ohne erzwungene fachfremde Definitionen. Es fordert hier weder ein neutrales Original-XState-JSON-Schema noch eine vollständige Autocomplete-Implementierung. X06 bleibt begrenzt N/C464; Originalimport-/APIpflichten werden nicht durch ein eigenes Originalschema ersetzt.

Tatsächliches xstate@5.33.3 aus dem bereits eingefrorenen Werkzeugverzeichnis, CommonJS-Originalexport createMachine/createActor/getInitialSnapshot. Eine eigene einfache SDK-Konfigurationsdatei enthält ausschließlich id, initial, context und states mit OPEN/CLOSE-Übergängen. Sie importiert keine CEM-, CSS- oder ARIA-Datei. Ein separater eigener Forschungsrunner lädt sie über CommonJS und übergibt sie der ursprünglichen API. Der Originalkernel verlangt in diesem ausgeführten Pfad keine Visual-/Interface-/Accessibility-Felder.

Interface, Visual und Accessibility sind bytegleiche CEM-, CSS- und HTML/ARIA-Fixtures aus dem bereits geprüften Vier-Domänen-Fall. Deren frühere Einzelprüfungen werden referenziert, nicht erneut als neue Fälle gezählt. Die externen Beiträge werden weder in SDK-Properties eingebettet noch von XState validiert. [Hashes und Originaldistributionsinventar](source-manifest.json).

## Zusätzliche konkrete Bindung

Das eigene Forschungsprofil benennt getrennte Quelldateien und Hashes, die tatsächliche CEM-Deklaration Autocomplete, die SDK-Maschinen-ID, vorhandene closed/open-Zustände und benannte A/B-Hostteile. Die eigene Prüfung vergleicht CEM-cssParts mit den expliziten IDs der festen HTML-Fixture und weist Quellenalias, veralteten Behaviorhash und A→B-Teilverwechslung zurück. Der ID-Abgleich ist auf diese Fixture beschränkt und kein allgemeiner HTML-/ARIA-Parser. IDs werden nicht als universelle Semantik ausgegeben. Deshalb A: zusätzliche Bindung, kein nativer Vier-Domänen-Paketresolver.

## Acht vorher benannte Bedingungen

[Erwartungen](cases.json), [Ergebnis](results.json), [Runner](run.cjs), [Profil](profile.json), [SDK-Datei](fixtures/behavior.cjs).

1. Vier getrennte Eingaben binden auf tatsächliche CEM-Deklaration und SDK-Maschine.
2. Beide ursprünglichen Actors starten closed.
3. OPEN bei A lässt B closed.
4. OPEN bei B und CLOSE bei A ergeben A closed/B open.
5. Eine geänderte Visualrevision mit max-height:192px statt160px lässt Behavior-, Interface- und Accessibility-Quellen unverändert und die ursprüngliche Maschine startfähig.
6. Visualdatei als Behaviorquelle im Profil wird vom Zusatzbinder zurückgewiesen.
7. Veralteter Behaviorhash wird vom Zusatzbinder zurückgewiesen.
8. A-Popupverweis auf B wird vom Zusatzbinder zurückgewiesen.

Acht Erwartungen erfüllt. Die erste Fassung der fünften Bedingung änderte lediglich einen Kommentar; sie bleibt als initial-comment-change-results.json erhalten. Der entscheidende Lauf ändert eine echte CSS-Eigenschaft. Diese Präzisierung zählt nicht als zusätzliche Bedingung. Keine ursprüngliche Fehlermeldung wurde verborgen.

## Grenzen

Der Beitrag zeigt unabhängig geführte Quellen und tatsächliche SDK-Ausführung, keine vollständige semantische Gleichheit aller vier Verträge. Das zweizuständige Behavior bildet insbesondere weder COMMIT noch value-change, Auswahltypbindung, Fokus, Tastatur oder Meldungen ab; die vorhandene Interface-Signatur ist keine hier geprüfte Emission. stateView ist eine ausdrücklich zusätzliche Zuordnung, keine zweite Zustandsmaschine. Es wurden keine DOM-Updates, CSS-Layouts oder AT-Nutzung in dieser Gruppe ausgeführt. Frühere Validator-/Browserergebnisse gelten nur in ihrem gespeicherten Umfang. Kein Produktionsformat und keine Komponente erstellt, kein Commit/Push.

## Reproduktion

Die eigenen Fixtures und Programme sind gespeichert. Der Runner erwartet die isolierte unveränderte xstate@5.33.3-Installation im relativen Forschungspfad ../xstate-validator/tool/node_modules/xstate. Installationsstand und Dateihashes sind dokumentiert; Originalpaketcode wird nicht als eigener Code verteilt. prepare.cjs erstellt Profil und Erwartungen aus den gespeicherten Quellen; run.cjs führt die acht Bedingungen aus. METHODS.md und REQUIREMENTS.md bleiben unverändert.
