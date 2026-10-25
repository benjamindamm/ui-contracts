# UXSpec: ausgeführte Referenz- und Bündelprüfung

Stand: 24. Oktober 2026. **14 explorative Fälle mit den Originalfunktionen des gespeicherten UXSpec-Snapshots ausgeführt.** Keine UI, kein Actor-/Fokus-/Scrollruntime und kein zusätzlicher Produktionsresolver. Die vorhandenen Quellen wurden nicht repariert. Die Aussagen gelten für die genannten Import-/Resolve-/Compile-/Bundlepfade.

## Werkzeug und Versuchsform

Sechs Originaldateien wurden über BrowserOS neo neu gelesen; source-manifest.json nennt URLs und Text-Hashes. TypeScript 5.9.3 transpiliert sie für den isolierten Versuch nach CommonJS/ES2022 mit esModuleInterop. Der Quellinhalt blieb unverändert; die Modulform wurde durch den Compiler übertragen. Dies ist keine TypeScript-Gesamttypprüfung des Kandidatenprojekts. Node 24.22.1 führt die resultierenden Funktionen aus.

Alle Eingaben, Diagnosen und beobachteten Ergebnisse stehen in results.json. Absolute Fixturepfade werden dort als `<probe-root>` notiert. Die Ausführung war explorativ. Die Akzeptanzkriterien wurden anschließend explizit gegen die gespeicherten Ergebnisse ausgewertet; es wird weder eine Präregistrierung noch eine unabhängige Replikation behauptet. Frühere E2-Befunde C390/C391/C395 enthielten bereits Hypothesen für Teilfälle.

## Zuerst die Originalschema-Voraussetzungen beachten

Eine getrennte Vorprüfung umfasst die 24 tatsächlich beteiligten UXSpec-Dateien: **15 bestehen das Originalschema, neun werden abgewiesen.** Die Compilerfunktionen rufen diesen vollständigen Originalschemapfad nicht automatisch auf. Deshalb dürfen deren Ergebnisse nicht pauschal als Verhalten garantiert schema-konformer Eingaben ausgegeben werden.

Normale `$ref`-Objekte ohne type passen im Originalschema gleichzeitig zu mehreren element-oneOf-Zweigen; die tatsächliche Meldung nennt Container, Leaf und Ref. Das betrifft unter anderem die Referenzkontrollen und importierten Elementfälle. Der transitive Untermaschinenfall enthält zusätzlich die bereits bekannte machineInvoke-oneOf-Kollision. Die vollständigen Vorprüfungen stehen in schema-preflight.json.

**Für die schema-konformen Kollisions-/Einheitenfälle gilt diese Einschränkung nicht:** Dort sind die beteiligten Originaldokumente tatsächlich akzeptiert. Diese Trennung ist für die Interpretation entscheidend.

## Ergebnisse je Fall

| Fall | Beobachtung | Grenze / Interpretation |
| --- | --- | --- |
| Lokale Unterreferenz | Inhalt LIBRARY, keine Resolverdiagnose | Positiver Funktionskontrollfall; normaler Ref wird vom Originalschema dennoch abgewiesen |
| Importierte Unterreferenz bei gleichnamigem Appziel | Inhalt APP, keine Resolverdiagnose | Der importierte Bezug wird im Appkontext weiter aufgelöst; Compilerpfad-Erkundung, keine Aussage über garantierte schema-konforme Referenzform |
| Derselbe Import ohne lokales Ziel | UNKNOWN_ELEMENT_REFERENCE | Die Bibliotheks-Unterreferenz wird nicht automatisch in deren Namespace gebunden |
| Angeforderter Tokenbereich fehlt | Namespace ohne Tokens, keine Importdiagnose | Beide beteiligten Dateien schema-konform; angeforderter Bereich allein wird nicht entsprechend abgesichert |
| Importdatei fehlt | IMPORT_NOT_FOUND | Positiver Diagnosekontrollfall |
| Unverändertes CEM als Elementquelle | UNKNOWN_IMPORTED_ELEMENT_REFERENCE, kein Elementbereich | Kein Fremdformatadapter im Originalresolver; wird nicht als Fehler eines zugesagten CEM-Features ausgegeben |
| Token mit value=1, unit=rem | Aufgelöster padding-Wert 1, keine Diagnose | Schema-konformer UXSpec-Tokenfall; Einheit geht in diesem Pfad verloren. Kein direkter DTCG-Originalimport wurde behauptet |
| Zwei statische Parameterexpansionen | A und B werden getrennt kopiert; Änderung der ersten lässt B unverändert | Positiver Kopiernachweis, keine unabhängigen Actor-/UI-Instanzen; Ref-Schemaproblem bleibt separat |
| Drei unterschiedliche Maschinen-IDs | root, child-a und child-b im Bundle | Schema-konformer positiver Bündelkontrollfall |
| Zwei Kinder mit gleicher Maschinen-ID | Bundle ok=true, nur root/shared; Wert B bleibt | Alle drei Eingaben schema-konform. Definition A wird ohne Diagnose durch B ersetzt |
| Eintritts-ID gleich Kind-ID | Bundle ok=true; Eintrittsmodul enthält Kindwert A statt ROOT | Beide Eingaben schema-konform. Auch der Einstieg wird ohne Diagnose ersetzt |
| Kind verwendet Großkind | Bundle ok=true, Module nur parent/child; Kindabhängigkeit zeigt weiter auf grand-Datei | Kein vollständiger transitiver Modulabschluss in diesem Pfad. Invoke-Eingabe scheitert separat am Originalschema; kein garantierter schema-konformer Runtimegegenfall |
| Element-Selbstreferenz | RangeError, Maximum call stack size exceeded | Keine strukturierte Resolverdiagnose für diese explorative Rekursion; Ref-Datei scheitert separat am Originalschema |
| Direkter Datei-Selbstimport | IMPORT_CYCLE | Positiver Importzyklus-Kontrollfall; keine Aussage über jede transitive Zyklusform |

Die Kriterienauswertung ergibt sechs erfüllte und acht nicht erfüllte Prüfziele. **Das sind keine acht pauschal bewiesenen Produktfehler:** Eingabevoraussetzungen, Quellenrolle und vorhandene Schemakollisionen müssen je Fall berücksichtigt werden.

## Konsequenz für gemeinsame Referenzen und Instanzen

Eine lesbare Datei und ein vorhandener Alias reichen nicht als Nachweis der richtigen fachlichen Herkunft. Eine zusätzliche Bindung muss Quelle/Namespace, Zielart, Definition und gegebenenfalls Instanzkontext erhalten. Globale Maschinen-IDs können im getesteten Bundler nicht unbesehen als konfliktfreie Identität verwendet werden.

Vor einer Vier-Domänen-Probe sind daher mindestens die stillen Modulüberschreibungen, die Einheitenbindung und die vollständige Erreichbarkeit verwendeter Untermaschinen zu behandeln. Ein eigener vorgeschalteter Konfliktcheck wäre zusätzliche Projektlogik, keine bereits bewiesene Originalfunktion. Es wurde keiner als Produktionswerkzeug implementiert.

UXSpec X03 bleibt U für semantische Ziele in unabhängigen Originaldomänen. Die neue Evidenz benennt konkrete interne Grenzen; sie erzeugt keinen Fremdmodellresolver. Vorhandene D-/N-Beiträge behalten ihren eng gefassten Rollenbezug. Die Gesamtzahl offener Matrixzellen wird durch negative Befunde nicht künstlich reduziert.

## Reproduktion

Die sechs Originaldateien anhand source-manifest.json unter sources/ ablegen. Im übergeordneten isolierten Werkzeugordner TypeScript 5.9.3 und python-jsonschema 4.25.1 bereitstellen. `cem-control.json` enthält den unveränderten synthetischen CEM-Kontrollinput der vorherigen Runde. Das Original-UXSpec-Schema unter ../sources/uxspec.schema.json bereitstellen.

```sh
node run.cjs
python schema_preflight.py
python assess.py
```

Der Runner transpiliert ausschließlich die sechs erfassten Quellen und arbeitet in fixtures/. Die tatsächlichen originalen Ergebnisse werden unabhängig von den gewünschten Akzeptanzregeln gespeichert. Keine UI wird gestartet. Das Feld PROBE_TYPESCRIPT kann einen anderen ausdrücklich gebundenen lokalen Compilerpfad setzen; für die gespeicherte Runde gelten die protokollierten Versionen.
