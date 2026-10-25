# Tatsächliche SCXML-Kindinstanzen: Lebenszyklus und Cachegrenze

Stand: 25. Oktober 2026. **Sechs Ausgangsbedingungen ausgeführt: drei Erwartungen erfüllt und drei verletzt. Ein separat vorregistrierter Diagnosefall erfüllt seine Erwartung.** Alle Ausgangsergebnisse bleiben erhalten; kein Wegzählen von Fehlern.

## Originalpfad und Forschungsgegenstand

Dasselbe Originalpaket @scion-scxml/scxml 4.3.28 mit gepinnten Abhängigkeiten aus dem Laufzeitblock. Neu selektiv gelesen: lib/runtime/invokers.js, originale invoke/cancelInvoke-Implementierung und öffentliche getSnapshot/isFinal-API. Der Defaultinvoker lädt echte lokale SCXML-Dateien. Kein eigener Invoker, kein überschriebenes send, kein gefälschter Childprozess.

parent.scxml und child.scxml sind **neue eigene Forschungsmodelle**, keine nachträgliche Änderung der vorherigen behavior.scxml und keine Original-Autocomplete-/ScrollArea-Komponente eines Herstellers. Die benannte ResearchScrollArea besitzt hier nur owner und offset, einen Zustand active, READY-/REPORT-Ereignisse und einen SCROLL-Handler. Sie ist kein vollständiger visueller oder zugänglicher Scrollvertrag. DOM, CSS und reale Scrollereignisse werden in diesem Block nicht ausgeführt.

Zwei Eltern werden aus separat vorbereiteten Modellfunktionen gestartet, erhalten instance A/B und rufen beim Eintritt in open jeweils dieselbe child.scxml mit invoke id scroll und Parameter owner auf. Der Defaultinvoker erzeugt reale Statechart-Kindinstanzen und native Parentzustellungen. Öffentliche Snapshots dienen als Beobachtung, kein Schreiben in private Laufzeitdaten. Eingaben und Erwartungen liegen vor den Ausgaben in cases.json.

## Sechs Ausgangsbedingungen

| Fall | Erwartung | Beobachtung | Ergebnis |
| --- | --- | --- | --- |
| Start A | Ein Kind, owner A, offset 0, Elternzustand open | Wie erwartet | Erfüllt |
| Start B / getrennte Daten | owner A/B, beide offset 0 | Beide Kind-Snapshots zeigen owner B | **Verletzt** |
| SCROLL an A | A meldet owner A/offset 40, B bleibt offset 0 | Nur Parent A erhält Report, aber owner B und beide Kinddaten offset 40 | **Verletzt** |
| CLOSE A | Kind A final, Kind B weiterhin aktiv | Wie erwartet | Erfüllt |
| Wieder OPEN A | Neues Objekt, A owner A/offset 0, B weiter owner B | Neues Kindobjekt entsteht; beide Daten zeigen nun owner A | **Verletzt** |
| Cancel Parent B | Parent und Kind B final | Wie erwartet | Erfüllt |

Der erste Lauf endet absichtlich mit Status 1. **Getrennte Objektidentität, getrennte Zustandskonfiguration und korrekte Ereignisroute reichen nicht für getrennte Daten.** Beim Wiederöffnen wird ein neues Objekt erzeugt, ohne damit schon einen neuen unabhängigen Datenkontext nachzuweisen.

## Diagnose mit anderem Cache-Schlüssel

Originalcode bindet einen Modulcache an SCXML-URL beziehungsweise Inhalt und verwendet daraus bereits vorbereitete Modellfunktionen wieder. Dies ist ein anderer Vorbereitungspfad als das direkte per-Instanz-prepare des vorigen Blocks. Die dortige Lösung für direkt erzeugte Instanzen beseitigt deshalb nicht automatisch die Defaultinvoke-Grenze.

Separat vorab gespeicherter Diagnosefall: dieselben Kindbytes als child-A.scxml und child-B.scxml unter unterschiedlichen Datei-URIs. Elternmodelle bleiben semantisch gleich, ändern nur den jeweiligen src-Verweis. Original-Defaultinvoker unverändert. Beobachtung nach SCROLL A: owner A/B, offset A=40, B=0 und Report owner A. Erwartung erfüllt, Status 0. Bytegleichheit der Kinddateien ist im Manifest nachgewiesen.

Das stützt zusammen mit dem gelesenen Originalcachepfad die Cache-/Ausführungskontextgrenze dieser konkreten Version. **Dateikopien oder instanzspezifische URIs werden nicht als Produktlösung gewählt.** Alternativen wie eine passende eigene Invokerbindung oder andere Runtime benötigen eine eigene Prüfung; keine davon ist hier implementiert oder als sicher behauptet.

## Konsequenzen und verbleibende Arbeit

Kein neuer Matrixwert: SCXML X04 bleibt A für vorhandene Kompositionsmechanismen mit Zusatzbindung; daraus folgt keine unbeschränkte Runtime-Isolation. Die neue harte Einschränkung gehört zu C456/C457 und in das aktuelle Integrationsrisiko. **56 U-Zellen bleiben offen.**

Belegt sind hier begrenzte echte invoke-Initialisierung, Parameterübergabe beim ersten Start, Parent-/Childroute und Cancel/Neustart. Nicht belegt: unabhängige Daten beim gleichen Default-src, vollständiger ScrollArea-UI-Vertrag, DOM-Fokus, dynamische Ansagen, native Profile oder Produktionsreife. Kein Commit/Push. Die Node-Warnung zu deprecated fs.F_OK ist gespeichert als Laufzeitkontext, kein Beleg gegen SCXML-Semantik.

## Reproduktion

Originalpaket und Lock aus dem benachbarten scxml-runtime/tool verwenden. run.cjs lädt parent.scxml und child.scxml über den originalen Dateiinvoker und schreibt results.json (Status 1 wegen drei erhaltenen Verletzungen). diagnose.cjs erzeugt die bytegleichen Kindkopien und schreibt diagnosis-results.json (Status 0). Beide benutzen neue Prozessläufe; Wiederholungen zählen nicht als zusätzliche Bedingungen. Timer sind begrenzte Fehlerfristen; auf native READY-/REPORT-Ereignisse wird über Listener gewartet. Keine Netzwerkdateien oder fremde ausführbare SCXML-Quellen.

## Ergänzung: eigener begrenzter Invokeradapter

Nach Erhalt des Originalfehlers wurden sechs eigene Adapterbedingungen vor Ausführung in adapter-cases.json gespeichert. Die ursprünglichen Erwartungen bleiben gleich; ein anderer Ausführungspfad ist jeweils ausdrücklich benannt. isolated-invoker.cjs nutzt die dokumentierte invokers-Option, liest ausschließlich dieselbe kontrollierte child.scxml und ruft je Kind die originalen documentStringToModel-/prepare-/Statechart-APIs auf. Kein gemeinsamer Modellcache, kein geerbter Ausführungskontext; Eingaben werden über die ursprüngliche params-Option übertragen. Native send-/Parent-/Cancel-Pfade bleiben erhalten.

**Alle sechs Adaptererwartungen erfüllt:** owner A/B unabhängig, SCROLL A verändert nur A, CLOSE beendet nur A, erneutes OPEN erzeugt unabhängige Anfangsdaten, Parentcancel beendet B. Gleiche Child-URI und bytegleiche Eltern-/Kindquellen wie im ursprünglichen Lauf. run-adapter.cjs endet mit Status 0. Die ursprünglichen drei Verletzungen werden dadurch weder geändert noch nachträglich als Erfolg gezählt.

Dieser Code ist eine **zusätzliche Forschungsbindung**, keine neue Originalfunktion oder gewählte Produktlösung. Er unterstützt nur die kontrollierte lokale Childdatei. Nicht geprüft: allgemeine Remote-/Content-/Constructorinvoker, Fehlerpropagation, vererbte Hostglobalen, Rennen bei Cancel während Initialisierung, Hierarchien über mehrere Ebenen, Wiederherstellung oder Vertrauen fremder Quellen. Insbesondere keine allgemeine Sicherheits- oder Konformitätsbehauptung. Der begrenzte Nachweis zeigt, dass instanzgetrennte Kindkontexte mit Original-Interpretermechanismen und explizitem Adapter möglich sind.

Gesamt dieses Blocks: 13 Bedingungen in drei Gruppen – sechs Originalpfadbedingungen, ein URI-Diagnosefall, sechs zusätzliche Adapterbedingungen. Keine weitere Matrixzelle geschlossen, weiterhin 56 U.
