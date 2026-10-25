# IP-01: ausgeführter zweistufiger Lifecyclekern

Stand: 25. Oktober 2026. **Acht vorregistrierte Bedingungen ausgeführt: sechs erfüllt, zwei verletzt.** LC-06 und LC-07 bleiben technische Blocker. Kein erfolgreicher Gesamtintegrationslauf, keine neue Matrixklassifikation. [Vorregistrierte Erwartungen](cases.json), [vollständige Resultate mit Ereignisjournalen und Endzuständen](results.json), [Original-/Eigenartefakthashes](source-manifest.json).

## Tatsächlich ausgeführter Pfad

Unverändertes `@scion-scxml/scxml` 4.3.28 aus dem bestehenden gepinnten Runtimeverzeichnis; Node v24.13.1. Eigene Parent-/Overlay-/Scroll-Forschungsmaschinen mit zwei Eltern A/B, identischen lokalen Quellen und jeweils `overlay`/`scroll` als lokalen Invoke-IDs. Die drei XML-Dateien bestehen das vorhandene originale SCXML-XSD: [Preflight](schema-preflight.json). Das ist ein unterstützender Schema-Vorlauf, keine zusätzliche neunte gezählte Bedingung.

[Zusätzlicher Adapter](adapter.cjs): Erweiterung des früheren eng begrenzten Fresh-prepare-Adapters auf genau zwei lokale Quellen. Jedes Kind erhält eine eigene originale Modellvorbereitung, eigene Statechart-Instanz und explizite Parameter. Der Adapter wird den Kindinstanzen ebenfalls übergeben, damit die zweite Ebene denselben ausgewiesenen Pfad verwendet. Send, Parentzustellung und Cancel verwenden den Originalinterpreter. Originalmodule wurden nicht verändert. Der Start prüft zusätzlich Elternzustand, Finalstatus und Epoche. Diese Prüfung ist eigener Code und keine Originalgarantie.

Gesteuerte Barrieren halten die jeweilige Initialisierung vor der Modellvorbereitung zurück. Der Runner schließt oder öffnet den Parent und gibt danach die Barriere frei. Fehlerfälle werfen an derselben Testschnittstelle absichtlich einen Initialisierungsfehler; sie prüfen Callback-/Promise-/Fehlerpfade, nicht alle möglichen Compiler- oder Transportfehler. Zeitgrenzen begrenzen ausschließlich das Warten auf erwartete Beobachtungen; sie werden nicht als Nachweis von Abwesenheit beliebiger späterer Effekte ausgegeben.

Snapshots werden über öffentliche Runtime-APIs gelesen. Zustände werden nicht durch Schreiben in private Daten hergestellt. Ereignisjournale enthalten Eintritte, tatsächliche Bigstep-Eingangsereignisse, Fehler, Childinitialisierungen und Start-/Abbruchentscheidungen. LC-07 hält beide Fehlerebenen einschließlich Aufräumzuständen getrennt fest.

## Acht Ergebnisse

| Fall | Ergebnis | Tatsächlicher Befund |
| --- | --- | --- |
| LC-01 | Erfüllt | Vier eigene Kindobjekte, Parameter owner A/B und Epoche 1 sowie getrennte Parentkontexte trotz gleicher Quellen und wiederholter lokaler IDs. |
| LC-02 | Erfüllt | A meldet Offset 40 über Scroll→Overlay→Root. B bleibt bei Offset 0 ohne entsprechenden Rootreport. Es wird ein Modellwert gemessen, kein DOMscroll. |
| LC-03 | Erfüllt | Native Parentrouten für A=11/B=22 stimmen. Zusätzlich eingespeiste fremde owner/epoch-Payloads werden durch ausdrücklich eigene SCXML-Guards verworfen. Diese Guards sind keine Authentifizierung; ein passend gefälschter Payload ist damit nicht ausgeschlossen. |
| LC-04 | Erfüllt | CLOSE während gehaltener Overlayinitialisierung: nach Freigabe ist das späte Overlay final, kein Scrollkind startet, kein READY zählt; B bleibt aktiv und unverändert. |
| LC-05 | Erfüllt | CLOSE während gehaltener Scrollinitialisierung: Overlay und nachgeliefertes Scrollkind sind final, kein READY zählt; B bleibt unverändert. |
| LC-06 | **Verletzt** | Neue Epoche 2 startet mit frischen Daten; alter Childkontext wird beendet und alte Meldungen werden verworfen. Nach Auflösung des alten Invokes funktioniert aber die neue Route `#_overlay` nicht mehr: Originalsend meldet `error.execution`, weil der Eintrag für die Invocation fehlt. Erwarteter neuer Report bleibt aus. |
| LC-07 | **Verletzt** | Getrennte kontrollierte Fehler beim Overlay und beim Scrollkind erzeugen abgelehnte Invocation-Promises. Der betroffene Root erhält keinen vorgesehenen init.failed-Übergang und bleibt geöffnet; bei Scrollfehler bleibt zusätzlich das Overlay aktiv. B unverändert und kein falsches READY. |
| LC-08 | Erfüllt | Normales und wiederholtes CLOSE ergeben stabile geschlossene Rootdaten und finale A-Kinder. B bleibt aktiv und unverändert. |

**Prozessstatus 1 ist beabsichtigt**, weil zwei vorab festgelegte Erwartungen verletzt bleiben. Weder Deadline noch ausbleibende Rückmeldung werden als Erfolg gezählt. [Erster Lauf](results-initial.json) und [erster Runner](run-initial.cjs) sind erhalten. Anschließend wurde ausschließlich das Ergebnisprotokoll um explizite Aufräumsnapshots der beiden LC-07-Unterläufe ergänzt und derselbe Versuch erneut ausgeführt. Die acht Bewertungen bleiben gleich; Wiederholung und zusätzliche Snapshots werden nicht erneut gezählt. Keine Korrektur am Adapter oder an den Erwartungen wurde vorgenommen.

## Eingrenzung der beiden Fehler

**LC-06:** Der gelesene Originalpfad `@scion-scxml/core-base/lib/scion-core-base.js`, `cancelInvoke`, hält eine Promise für die lokale Invoke-ID. Sein späterer Callback beendet das alte Kind und löscht den Eintrag dieser ID. Wenn inzwischen eine neue Verwendung derselben ID registriert wurde, entfernt diese alte Bereinigung auch deren Eintrag. Das Journal zeigt frische Epoche/Children und erst nach Freigabe des alten Invokes den fehlenden neuen Sendpfad. Eine reine Epochenguard verhindert deshalb zwar veraltete Fachmeldungen, aber nicht diese Aufräumkollision.

**LC-07:** Der originale `invoke`-Callback weist bei Fehler die Promise zurück. Der gelesene Fehlerzweig in `cancelInvoke` enthält keine Weiterleitung in die Maschine. Der Runner zeichnet die beiden tatsächlichen unbehandelten Rejections explizit auf; er repariert sie nicht durch ein erfundenes Erfolgsereignis. Späteres Testcleanup kann die Rejection nachträglich behandeln; auch die entsprechende Node-Warnung bleibt in [stderr](stderr.txt) erhalten. Die Runtime hat damit keinen in diesem Versuch funktionierenden automatischen init.failed-Pfad.

Das sind Befunde zu diesem gepinnten Interpreterpfad mit eigenem Adapter, keine Aussage, dass SCXML als Standard diese Isolation oder Fehlerbehandlung unmöglich macht. Der frühere Defaultinvoker-Gegenbefund bleibt zusätzlich unverändert bestehen.

## Konsequenz für das Integrationsprofil

[IP-A05](../../../INTEGRATION-ACCEPTANCE.md) besitzt einen neuen begrenzten Teilnachweis für zweistufige lokale Parameter-/Daten-/Parentroutentrennung. [IP-A06](../../../INTEGRATION-ACCEPTANCE.md) bleibt offen: normales Cancel bei ausstehender Initialisierung ist im kontrollierten Fall belegt, sofortiges Reopen und Initialisierungsfehler sind nicht bestanden. Auch IP-A05 ist wegen noch fehlender Host-/Vollpaketbindung nicht komplett abgenommen.

Vor einer weiteren Variante zwei technische Möglichkeiten getrennt untersuchen: (1) ein expliziter Drain-/Closing-Ablauf, der alte native Invocationbereinigung vor Wiederverwendung derselben ID abschließt; oder (2) pro Generation eindeutige native Invoke-IDs bei weiterhin stabilen logischen Teilpfaden. Beide ändern konkrete Lifecycle-/Routingbindungen und benötigen neue vorregistrierte Fälle. Ein zusätzlicher Fehleradapter muss echte Fehler an die richtige noch aktuelle Instanz weiterreichen und alle bereits entstandenen Kinder beenden, ohne Rejections zu verdecken. Keine dieser Möglichkeiten ist hier implementiert oder als bestanden markiert.

## Grenzen und Reproduktion

Keine reale Autocompletekomponente, keine DOM-/CSS-/Fokus-/Scrollsichtbarkeit, keine Provider-/T1-Daten, keine Themes, keine Assistenztechnik, keine Remote-/Content-/Constructorinvoker, keine allgemeine Ressourcen-/Sicherheitsgarantie. Der Offset ist ausschließlich ein Forschungsdatenfeld. Keine endgültige Bindungssyntax und keine Produktionsentscheidung.

Nach Bereitstellung der unveränderten Abhängigkeiten aus der benachbarten `scxml-runtime/tool/package-lock.json`: `node run.cjs` im Verzeichnis dieses Berichts. Erwarteter Exitstatus 1; vollständige Ausgaben werden in results.json geschrieben. Die Quellen-/Lock-/Methodenhashes sind vor einer Reproduktion zu prüfen. Die Rohresultate enthalten die tatsächlich verwendeten lokalen file-URIs; Verschieben des Forschungsordners verändert diese URIs und ist bei neuer Ausführung zu dokumentieren. Kein Commit und kein Push.
