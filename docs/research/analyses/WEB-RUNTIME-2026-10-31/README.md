# Paket 3 · Reproduzierbare Laufzeit und aktuelle Webprüfung

**31. Oktober 2026 · begrenzter Engineeringnachweis, keine neue unabhängige Modellstudie.** Die aktiven vier Profile werden aus ihren aktuellen Originalquellen geprüft. Historische Studien, Erstlieferungen und ihre Urteile bleiben erhalten. `release:false`.

## Ergebnis und Einstieg

- [Einrichtung](../../../../tools/setup.py): gepinnte Python-/Node-Pakete und 15 SHA-256-gebundene Originalengine-JARs lokal bereitstellen. Voraussetzung: Python mit venv, Node 22+/npm und JDK 17+. Kein mitkopierter `/tmp`-Enginebestand und kein fest eingebauter Mac-Pfad. Ein expliziter lokaler JDK-Pfad ist auf diesem Host weiterhin erforderlich.
- [Gemeinsamer Testbefehl](../../../../tools/test.py): `python3 tools/test.py --browser-run .runtime/web-run --out .runtime/test-run`. Ohne aktuellen Browserlauf ist der volle Umfang blockiert. `--unit-only` benennt ausdrücklich den kleineren Umfang.
- [Webablauf](../../../../tools/web/README.md): Quelle vorbereiten, lokalen Collector starten, fünf eingefrorene BrowserOS-Skripte auf eigener Seite ausführen, Rohdaten extern prüfen. Unterstützt Input, Select, SelectWithSearch und den komponierten Autocomplete; kein allgemeiner Generator.
- [Aktuelle Bibliothek](../../../../libraries/example/README.md) 0.4.0. [Vorheriger 59-Datei-Stand](../../../libraries/frozen/example-active-ux-03.json) bytegleich archiviert. Keine Umdeutung früherer Receipts.

## Tatsächlich geprüft

**243 automatisierte Regressionserwartungen erfüllt; 17 tatsächliche Browserfälle bestanden.** Die vollständigen Ergebnisse stehen in [verification.json](verification.json); [ARTIFACTS.json](ARTIFACTS.json) indexiert alle Dateien mit SHA-256. [Gemeinsame Regressionen](evidence/complete-suites/results.json), [Browserauswertung](evidence/browser-result.json), [native Profile](evidence/browser/native.json) und [saubere Einrichtung](evidence/clean-setup.json) sind getrennte Nachweise.

Der Browserlauf hat **17 Fälle**: Ausgangszustand; Loading/Busy; Providerreihenfolge und Ready; Tastaturnavigation samt Scrollen; Commit; zweite isolierte Instanz; veraltete Antwort; leere und ungültige Ergebnisse; Disabled; Inputeingabe und ReadOnly; native Select-Auswahl; getrennte Suchfilterung; Suchnavigation; Such-Commit und Escape. Die externe Auswertung enthält zusätzlich Quellen-/Werkzeug-/Laufbindungen und Fehlerfreiheit je Capture. Diese Einzelassertionen sind keine weiteren unabhängigen Studienfälle.

Konkrete Messung: Autocomplete A navigiert unter Überspringen einer deaktivierten Zeile bis A-12. Die ScrollArea misst **scrollTop 224 px**, clientHeight 160 px und scrollHeight 384 px. Die letzte Zeile liegt danach vollständig im Viewport; DOM-Fokus bleibt `A-input`. Enter löst genau ein öffentliches `value-change` mit `{value:"A-12"}` aus. Der Browser-AX-Baum meldet eine fokussierte, expandierte Combobox. Das belegt Browsersemantik, keine tatsächliche Screenreader-Ausgabe.

Beim Select mit Suche bleibt der aktive Schlüssel bis zum Commit vom Auswahlwert getrennt. Suchtext reduziert die Liste tatsächlich auf K30; erneute breitere Query erlaubt Navigation und Scrollen. Commit und Escape stellen Triggerfokus wieder her; Escape erhält den bestehenden Auswahlwert ohne zusätzliches Commitereignis. Die Providerdaten für Autocomplete und Host-Propertyupdates sind explizite Fixtures; Benutzereingaben erfolgen durch BrowserOS. Reale IME wurde nicht getestet.

## Saubere Arbeitskopie

[Exportprotokoll](evidence/export-manifest-final.json): Export der aktuellen getrackten und nicht ignorierten Arbeitsdateien, **kein Clone des unveränderten HEAD**. `.git`, `.runtime`, node_modules und venv wurden nicht übernommen. Der Setupbefehl installierte Python-/Node-Abhängigkeiten in neue lokale Umgebungen und lud die 15 Engine-JARs über die gepinnten URLs. Normale globale Paketmanagercaches wurden dabei nicht deaktiviert. Das Originalprojekt und die saubere Kopie liefen auf demselben macOS-Host; installiertes Python 3.9, Node 24.13.1 und JDK 25 waren Hostvoraussetzungen. Die Java-Bridge wird mit `--release 17` frisch kompiliert. Keine Prüfung eines frisch installierten Betriebssystems, von Windows/Linux oder eines ausgeführten JDK 17 behauptet.

Nach dem Setup wurden eng begrenzte Quellkorrekturen am neuen Testeinstieg und Dokumentations-/Prüfdateien in die Kopie synchronisiert; die exakte Liste und finale Datei-Hashes stehen im Exportprotokoll. Dependency-Locks blieben dabei unverändert. [Frischer Testlauf](evidence/clean-sealed-suites/results.json) ist ausdrücklich ohne Browser und verwendet die neu eingerichtete Engine. Die Browserprüfung lief separat im Hauptarbeitsbaum.

[CI-Definition](../../../../.github/workflows/contracts.yml): nur Unit-/native Prüfungen, ohne Browserbehauptung. Der Workflow wurde lokal vorbereitet; ein erfolgreicher GitHub-/Linux-Lauf ist damit nicht belegt.

## Neue Fehler und Reparaturen

| ID | Beobachtung | Ursache und Reparatur | Gegenbeleg |
| --- | --- | --- | --- |
| WR-001 | Programmatisches SET_VALUE übernimmt deaktiviertes OFF | Membership-Guard prüfte nur Schlüsselgleichheit. Aktive SCXML verlangt jetzt zusätzlich `!disabled` und einen String. | [Fehlgeschlagener Originalfall](preflight/ac-before.json); erneutes Entfernen des Guards wird von test_ux.py erkannt. |
| WR-002 | Nativer Reveal-Test bricht mit „Cannot call gen during a big-step“ ab | Synthetische MEASURED-Antwort erfolgte noch im laufenden Callback. Gemeinsamer Invoker verschiebt sie in einen nachfolgenden Microtask. | 16 aktuelle native Kompositionschecks; keine DOM-Geometrie daraus abgeleitet. |
| WR-003 | Letzte Option bleibt außerhalb der ScrollArea, deren scrollTop bleibt 0 | Allgemeine Host-ul-Regel erzeugte einen zweiten Scrollcontainer in der Liste. Regel auf den Suchselect-Host beschränkt. | [Erster Browserbefund](preflight/browser-first.json), rohe Messungen unter preflight/browser-01; aktueller Messwert 224 px. |
| WR-004 | Suchnavigation erzeugt erneute native Big-Step-Fehler, Commitfokus landet auf BODY | Neuaufbau einer fokussierten Option löste focusout im Rendering aus. Renderingphase explizit geschützt, tatsächliche externe Fokuswechsel weiter anhand relatedTarget; Trigger erhält stabile ID und Fokus. | Vollständiger neuer Browserlauf ohne Fehler; negative BODY-Fokusprobe scheitert. |
| WR-005 | Neuer Sammelrunner ruft Handoff-Suite ohne Initialisierung auf | Suite benötigt ihren vorhandenen CLI-Einstieg mit --output statt unittest-discovery. Nur Runner korrigiert; 37 Kriterien unverändert. | Initialer Runnerlog unter preflight/runner-initial; final 37/37. |
| WR-006 | Quellcodeprüfung: Host las feste Dateinamen, auch wenn Domainpfade umgeleitet würden | Endliches Adapterlayout ausdrücklich abgleichen; abweichende Interface-/SCXML-/HTML-/Visualpfade blockieren. Keine behauptete Laufzeitbeobachtung vor Reparatur. | Zwei Gegenfälle für Behavior- und Tokenumleitung; keine stillen Ersatzquellen. |

Weitere Zwischenläufe scheiterten erwartungsgemäß, sobald neue Checker oder die Bibliotheksdokumentation die gebundene Revision änderten. Alte Captures wurden nicht umgebunden: neue vollständige Browserläufe ersetzen sie nur als aktuelle Nachweise. Der erste fehlgeschlagene Lauf bleibt unverändert erhalten. Die zusätzliche abschließende Quellenlayout-Grenze verweigert umgeleitete Domain-/Tokenpfade, statt nebenliegende alte Dateien still auszuführen; zwei negative Bindungsfälle sichern dies ab. [Befundstatus](resolution-status.json) ordnet die früheren Auditpunkte ein.

## Grenzen und nächste Arbeit

Endliche Profiltests sind kein formaler Beweis beliebiger SCXML-/JavaScriptprogramme. Der Host übernimmt für Autocomplete Visualregeln/Tokens, für die anderen Controls prüft er Verhalten/Semantik; daraus folgt keine vollständige visuelle Implementierung dieser Controls. Keine AT-, Pixel-, Mobile-, Produktions- oder universelle Plattformfreigabe. Der lokale Harness ist keine manipulationssichere externe Attestierung.

Nächstes separates Paket bleibt die Konsolidierung der Studien-/Übergabeformate und anschließend der gestufte Modellvergleich. Diese Engineeringreparaturen allein beweisen keine verbesserte Erfolgsquote schwächerer Modelle.
