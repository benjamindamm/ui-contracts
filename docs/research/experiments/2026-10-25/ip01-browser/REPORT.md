# IP-01: gemeinsamer Browserlauf abgeschlossen

Stand: 25. Oktober 2026. **20 vorregistrierte Bedingungen tatsächlich ausgeführt, alle finalen Erwartungen erfüllt.** Der eigene Forschungs-Host verbindet CEM, DTCG/CSS, SCXML und HTML/ARIA in einer gemeinsamen gepinnten Browserrevision. Tatsächliche Browseraktionen, Original-SCXML-Interpreter, DOM-/Fokus-/Scrollmessung und originale Chromium-Accessibility-Bäume sind ausgeführt. Dies ist ein begrenzter Webreferenznachweis, keine universelle Komponenten-/Plattform- oder Assistenztechnikfreigabe.

[Ergebnisse](results.json) · [Vorregistrierung](cases.json) · [Hostquellen](host/index.html) · [gemeinsamer Quellenabschluss](host/manifest.json) · [Original-/Eigenartefakthashes](source-manifest.json)

## Konkretes Ergebnis für das Vorhaben

Die vier ausgewählten Kernbeiträge lassen sich für diesen Webfall tatsächlich zusammenführen:

- CEM führt die untersuchte öffentliche Signatur einschließlich `{value:string}` und die benannten Teile. Der zusätzliche abgeleitete TypeScript-AST-Typsichtbaum prüft Providerdaten und die öffentliche Eventpayload.
- DTCG führt die verwendeten Dimensionstokens. CSS führt Ankergeometrie, Zeilengestaltung und Overflow. Tokenwerte werden im Host als CSS-Variablen gesetzt; das Layout wird vom wirklichen Browser berechnet.
- SCXML führt Query, Wert, aktive Option, Zustände, Navigation, Komposition, Anfragegeneration, Commitzeitpunkt und die zweistufige Unterkomposition.
- HTML/ARIA führt die semantischen Hostelemente und Rollen. Der zusätzliche Webadapter projiziert den tatsächlichen Behaviorzustand in Beziehungen, Status und zugängliche Zustände.

**Die Verbindung benötigt zusätzliche Bindungs- und Adapterlogik.** Der hier ausführbare Adapter verwendet ausgewiesene Hostkonventionen und Code für die Zuordnungen. Er ist noch kein vollständig generischer Verbraucher des vorherigen deklarativen bindings.json. Beispielsweise Statusvorlagen und Zustandsprojektionen sind im zusätzlichen Hostcode konkret festgelegt; eine universelle Informationssprache lässt sich daraus nicht als bereits fertig ableiten. Die gesamte CEM-API einschließlich der nur statisch untersuchten T0-Hilfsfelder ist ebenfalls nicht als produktive Komponente implementiert.

Das Ergebnis stützt den vorgeschlagenen Aufbau als **Webreferenz**. Für iOS/Android fehlen weiterhin explizite Layout-/Typ-/Laufzeit-/Fokus-/Accessibilityabbildungen und tatsächlich ausgeführte Vergleichsfälle. Ein Agent darf diese Lücken nicht beiläufig durch eigene Produktentscheidungen füllen. Siehe [Einordnung des plattformübergreifenden Ziels](../../../ARCHITECTURE-DIRECTION.md).

## Tatsächlicher Aufbau

Neue eigene Forschungsdateien unter `host/sources/`: je Interface/CEM, Behavior/SCXML, Accessibility/HTML und Visual/CSS für Autocomplete, Overlay und ScrollArea; geteilte DTCG-Tokens. Die Behaviorgerüste der statischen Runde wurden für den hier untersuchten Ablauf erweitert. Es ist deshalb eine **neue, eigene Quellenrevision**; die vorherigen statischen Dateien sind nicht nachträglich als diese volle Maschine ausgegeben.

Die Originalschemas bestätigen drei CEM-Dateien und vier SCXML-Dateien einschließlich Fehlerrelay: [finaler Vorlauf](schema-preflight.json). HTML/ARIA erhalten kein erfundenes originales JSON-Schema. Der DTCG-Dimension-/Aliasleser und die Hostbindungen sind begrenzter eigener Code.

Originalbrowserruntime `@scion-scxml/scxml` 4.3.28 und ursprüngliches Babel-Polyfill 7.12.1 werden bytegleich aus den bereits gepinnten Abhängigkeiten über den lokalen Server bereitgestellt. Keine neuen externen Bibliotheksversionen, keine Änderungen an Originalmodulen. Jede Kindverwendung erhält eine frische originale Modellvorbereitung und eigene Interpreterdaten. Originale `invoke idlocation`-/Send-/Parent-/Cancel-Pfade werden verwendet; der isolierende Invoker und der Fehlerrelay sind sichtbar zusätzliche Forschungsbindungen.

Die JavaScript-Hostlogik entscheidet nicht unabhängig über die nächste Option oder den Commit: Diese Regeln stehen in der SCXML-Datei. Der Host validiert Daten, projiziert Zustand, verwaltet DOMelemente und misst echte Geometrie. Die ScrollArea erhält einen tatsächlichen Revealauftrag über die native Parent-/Kindkette. Der Host liest nach dem wirklichen Scrollen Offset und Sichtbarkeit; diese Messung wird über MEASURED/scroll.revealed/overlay.revealed zurück an die Maschine gegeben. Ein Wunschoffset wird nicht als Messung ausgegeben.

Die beiden Browserinstanzen sind gemäß dem gewählten Fokusverlustprofil im normalen Tastaturablauf nacheinander geöffnet. Die früheren separaten Lifecyclefälle prüfen zusätzlich gleichzeitige Interpreterketten. Dieser Browserlauf wird nicht nachträglich als gleichzeitiger Mehrpopup-Fokusfall ausgegeben.

## 20 finale Ergebnisse

| Fälle | Tatsächlich geprüfter Umfang | Ergebnis |
| --- | --- | --- |
| BR-01–BR-02 | Aktuelle Originalschema-Vorläufe; browserseitig geprüfte Hashes sämtlicher Quellen und Originalbrowserabhängigkeiten; geschlossene unabhängige Ausgangszustände | Erfüllt |
| BR-03–BR-04 | Browser-ArrowDown → echte Overlay-/ScrollArea-Interpreter → erste aktivierbare Option; deaktivierte dritte Option übersprungen; letzter Eintrag sichtbar bei 160px Viewport und tatsächlich positivem Scrolloffset; kein Wrap | Erfüllt |
| BR-05 | Echter Chromium-AX-Baum: zwei Namen, Expanded, Controls, aktiver tatsächlicher Optionsknoten, Selected, Status/polite/atomic; Inputfokus und keine zusätzlichen Container-Tabstopps | Erfüllt |
| BR-06–BR-08 | Browser-Enter emittiert genau einmal das deklarierte Event mit A-7, übernimmt Label/Key und schließt ohne Fokusverschiebung; B/Escape und programmatische Wertsetzung erzeugen keinen zusätzlichen Benutzercommit | Erfüllt |
| BR-09–BR-11 | Neueste Query/Anfrage gewinnt bei vertauschten Antworten; Empty/Providerfehler; typwidrige Records und doppelte Keys vor Teilrendering abgewiesen; bestätigter Wert bleibt erhalten | Erfüllt |
| BR-12–BR-13 | Ausdrücklich synthetische Kompositionsereignisse unterdrücken Zwischenanfragen/Commit/Navigation; Ende erzeugt genau die aktuelle Anfrage. Browser-Tab schließt ohne Commit und ohne verwaiste Beziehungen; Text bleibt erhalten | Erfüllt |
| BR-14–BR-15 | Gehaltene Originalchildinitialisierung, Close und sofortiger Reopen: altes Kind wird final, neue Route bleibt wirksam. Tatsächlich unvollständiges Child-XML läuft über expliziten Fehlerrelay in kontrolliertes Schließen und zugänglichen Fehlerstatus | Erfüllt |
| BR-16 | Eigener CSS-Anker je Input: gemessene 8px Unterkantenrelation nach Geometrieänderung. Explizite Testkontextvariation mit unterschiedlichen Zeilenhöhen wird tatsächlich sichtbar gescrollt | Erfüllt |
| BR-17–BR-18 | Alte Antwort nach neuer Epoche und tatsächlich nativ zugestellter Fremdreport haben keine fremde Fach-/UIwirkung; zusätzliche Epoch-/Instanzguards sind sichtbar | Erfüllt |
| BR-19–BR-20 | Tatsächliche AX-Bäume für Loading/Error/Closed/Ready; Busy/aktive Beziehung/Meldungstext folgen dem Zustand, alter Ladetext wird beim Schließen bereinigt. Abschließende Quellenhashes, finale Kinder und fehlerfreies Runtimejournal | Erfüllt |

Die genaue Zerlegung in erwartete/tatsächliche Prüfaussagen steht in [results.json](results.json). Rohaufnahmen `captures/BR-xx.json` enthalten Snapshot, vollständiges bisheriges natives Ereignisjournal, öffentliche Events, Messungen, Diagnosen, Browserumgebung und Quellenrevision. BR-05/BR-19 enthalten echte `Accessibility.getFullAXTree`-Resultate; keine nachgebildeten Accessibilitydaten.

BR-16 variiert Inputmaße und Zeilenhöhen ausdrücklich als dokumentierten DOM-/Style-Testkontext. Diese aufgezeichnete Variation ist kein nachgewiesener Originaltoken-Update-/Regenerationsprozess, keine Themeprüfung und kein allgemeiner Roundtripnachweis. Sourcehashkontrolle und Laufzeitkontext werden getrennt geführt.

## Browser und Eingabeherkunft

BrowserOS neo, tatsächlich gemeldetes `Chrome/155.0.8311.26`, CDP 1.3, JavaScript 15.5.35.14. Vollständige Version und UserAgent stehen im Ergebnis. Aus dem kompatibilitätsorientierten UserAgent wird keine reale macOS-Versionsnummer abgeleitet.

Fokus, Texteingabe, Pfeiltasten, Enter, Escape und Tab wurden über BrowserOS-Browseraktionen ausgelöst; das DOM protokolliert für diese Browserereignisse `isTrusted:true`. Das ist **keine physische Tastaturprüfung durch einen Menschen**. Komposition, Providerantworten, Fehler-/Initialisierungsbarrieren, Fremdreport und Geometrievariation sind ausdrücklich kontrollierte beziehungsweise synthetische Testeingaben. Das öffentliche CustomEvent selbst wird vom eigenen Adapter erzeugt und ist entsprechend nicht trusted; das wird nicht mit der Herkunft der Eingabetaste verwechselt.

Keine reale IME, keine Screenreader-Sprachausgabe, kein VoiceOver-/TalkBack-Lauf, keine iOS-/Android-Ausgabe. AX-Meldungstext und Live-/Atomic-Eigenschaften sind beobachtet; tatsächliche Ansage, Reihenfolge und Nutzbarkeit mit Assistenztechnik bleiben offen.

## Erhaltene Erstbefunde und Korrekturen

1. Die erste eigene Autocomplete-Datei enthielt Transitionen direkt unter dem SCXML-Root. Das Original-XSD wies sie ab. [Erster Schema-Vorlauf](schema-preflight-initial.json) und [erste Datei](autocomplete-initial.scxml) bleiben erhalten. Der korrigierte eigene Entwurf verwendet einen umschließenden Zustand; Originalschema unverändert.
2. Beim ersten Browsercommit löschte `active.onexit` den aktiven Key vor den Transitionaktionen. Dadurch scheiterte die Labelübernahme mit einem tatsächlichen `error.execution`, und das öffentliche Event fehlte. [Erste Hostrevision](host-initial/manifest.json), Quellen und [erste BR-06-Aufnahme](captures-initial/BR-06.json) bleiben erhalten. Die Bereinigung erfolgt jetzt beim Eintritt in closed, nach den Commitaktionen. Der volle finale Block wurde mit neuer Revision wiederholt.
3. Der erste Kompositionsharness las nach einem Animationsframe die letzte Anfrage zu früh und beantwortete noch eine alte Anfrage. [Aufnahme](composition-capture-initial.json) erhält diese widersprochene Erwartung. Der korrigierte Harness wartet auf das tatsächliche originale Parentereignis provider.request; keine Erwartung wurde abgeschwächt.
4. Ein AX-Vergleich zeigte einen nach Close übrig gebliebenen Ladetext. [Früherer AX-Baum](captures-before-status-fix/AX-closed.json), [Hostcode](host-before-status-fix.js) und [Revision](manifest-before-status-fix.json) bleiben erhalten. Der Host bereinigt Status beim tatsächlichen Übergang nach closed; ein später ankommender bestätigter Commit setzt seine eigene Meldung. Nach dieser Änderung wurde der gesamte gespeicherte Vier-Schritt-Browserablauf erneut ausgeführt.

Gezählt werden **20 Bedingungen in einer Gruppe**, keine zusätzlichen Bedingungen für Wiederholungen, einzelne Assert-Felder, zusätzliche AX-Aufnahmen oder Korrekturen. Die Original-Defaultinvoker- und die späteren LC-06-/LC-07-Gegenbefunde aus früheren Gruppen bleiben unverändert.

## Was abgeschlossen ist und was offen bleibt

Der beauftragte gemeinsame Browserprüfblock ist abgeschlossen. Ein konkreter Webablauf verbindet alle vier Beiträge mit ausgewiesenen zusätzlichen Adaptern und tatsächlichen Messungen. Das bestätigt die technische Machbarkeit dieses Referenzfalls.

Die komplette IP-Abnahme ist damit nicht pauschal bestanden: allgemeiner deklarativer Runtime-Resolver, alle API-/Typ-/Anatomievarianten, Farb-/Themeabnahme, vollständige Quelländerungs-/Migrationskette und manuelle Assistenztechnik fehlen. Pointer-/Touchbedienung, echte IME, mehrere Browser/OS, Portals/Virtualisierung, RTL und weitere Widgets wurden hier nicht nachgewiesen. Keine allgemeine Produktionsreife, identischen nativen Controls oder plattformübergreifende Gleichheit behauptet.

Die zwei ungeklärten Originalfragen Google DESIGN.md X06 und OpenUI X06 bleiben mangels neuer Herausgeberinformation offen. Sie sind vom erfolgreichen ausgewählten Webreferenzfall getrennt. Es wurden keine Autoren kontaktiert und keine neue Recherche nach weiteren Kandidaten gestartet.

## Reproduktion und Abschluss

`server.py` stellt nur den lokalen Forschungs-Host und die gebundenen Originalassets bereit. Die erforderlichen Abhängigkeiten stammen aus der früheren gepinnten Runtime, nicht aus diesem Dokumentationsarchiv. Der Server schreibt seine lokale Adresse nach server.json. Mit BrowserOS eine eigene Seite öffnen, `__HOST_URL__` in browser-01.js bis browser-04.js durch diese Adresse ersetzen und die vier SDK-Skripte nacheinander über BrowserOS run ausführen. evaluate.py wertet die tatsächlichen Rohaufnahmen aus. Die Source-/Methodenhashes sind vorher zu prüfen. Der Generator create_models.py ist Entwurfsprovenienz; zur exakten Reproduktion ist der bereits final gepinnte host/-Stand maßgeblich.

Bericht, Original-/Eigenartefakthashes, Matrixzähler und Aufgaben sind abgeglichen. Kein Commit, kein Push, keine neue automatische Folgerunde. Forschung und Tests sind für diesen beauftragten Abschlussstand beendet; offene Grenzen bleiben dokumentiert.
