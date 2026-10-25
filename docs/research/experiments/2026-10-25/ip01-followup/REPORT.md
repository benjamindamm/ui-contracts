# IP-01: begrenzte Folgevarianten für Reopen und Initialisierungsfehler

Stand: 25. Oktober 2026. **Sechs neue vorregistrierte Variantenbedingungen erfüllt; die acht bisherigen LC-Erwartungen bestehen als nicht erneut gezählte Regression im neuen Pfad.** Der [erste Gegenbefund](../ip01-lifecycle/REPORT.md) bleibt unverändert: sechs von acht Erwartungen erfüllt, LC-06/LC-07 verletzt. Dies ist eine zusätzliche Forschungsbindung, keine Reparatur der Originalmodule und keine Produktionsentscheidung.

[Vorregistrierung](cases.json) · [neue Variantenresultate](variant-results.json) · [Regressionsergebnisse](results.json) · [Original-/Eigenartefakthashes](source-manifest.json)

## Zwei getrennte Varianten

**Drain/Closing mit wiederverwendeter nativer ID:** Die Forschungs-Hostkoordination nimmt OPEN während der Bereinigung als wartenden Auftrag an. Sie öffnet erst wieder, wenn alle eigenen ausstehenden Kind-/Enkelvorbereitungen derselben Instanz und Epoche zurückgekehrt sind, deren tatsächliche Interpreter final sind und die native Callback-/Cancelbereinigung abgearbeitet ist. Die SCXML-Rootmaschine selbst bleibt dabei closed; `closing` ist hier ein ausdrücklich eigener Hostprotokollstatus, kein bereits implementierter SCXML-Zustand. Keine privaten Invocationmaps werden verändert. Die Adapterfunktion `researchDrain` dient ausschließlich diesem begrenzten Forschungsprotokoll.

**Generationseindeutige native IDs:** Die eigene SCXML-Fixture verwendet das originale `invoke idlocation` sowie `send targetexpr` anstelle eines konstanten nativen Invoke-IDs. Der unveränderte Originalcompiler erzeugt beim nächsten Invoke innerhalb derselben Parentinstanz einen anderen nativen Schlüssel. Logische Strukturpfade A/overlay/scroll und B/overlay/scroll bleiben stabil. Native Schlüssel sind weiterhin parentlokal und keine globalen fachlichen Identitäten. Ein alter Cancelcallback löscht damit den alten Schlüssel, während die neue Route bestehen bleibt. Die Prüfung gilt für die tatsächlich ausgeführten endlichen Abläufe, nicht für unbegrenzt lange Sitzungen oder andere Runtimeversionen.

**Explizite Fehlerweiterleitung:** Nach tatsächlich fehlgeschlagener Initialisierung wird ein eigener, eindeutig als `relay:true` protokollierter Fehlerakteur mit dem Originalinterpreter erzeugt. Dieser erhält Fehlermeldung, owner und Epoche und sendet `init.failed` über den originalen Parentpfad. Das ist keine erfolgreich initialisierte Overlay-/Scrollkomponente und erzeugt kein READY. Die native Invocation erhält einen verwaltbaren Fehlerakteur statt einer unbehandelten Rejection; der Fachfehler selbst bleibt im Journal und erreicht den aktuellen Root. Dort schließt die ausdrücklich eigene Fehlertransition die Kette und native Cancelpfade beenden bestehende Kinder einschließlich Fehlerakteur. Fehler einer alten Epoche werden vor Start des Relays als veraltet diagnostiziert und beendet. Scheitert die Fehlerakteurvorbereitung selbst, wird das weiterhin als Fehler zurückgegeben; dieser stärkere Fall wurde nicht nachgewiesen.

Der Adapter führt keine neue Auswahl-/Scroll-/Accessibilitysemantik ein. Er unterstützt nur die kontrollierten lokalen Forschungsquellen, frische Modellvorbereitung und die hier gezeigte Fehlerkonvention. Remotequellen, nicht zurückkehrende Initialisierungen, beliebige fremde Modelle und allgemeine Security-/Recoverygarantien bleiben außerhalb des Nachweises.

## Sechs neue Bedingungen

| ID | Variante | Beobachtung | Ergebnis |
| --- | --- | --- | --- |
| F-01 | Drain, Overlay gehalten | Reopen wartet bei Rootepoche 1/closed. Nach Freigabe ist die alte Kette final; neue Epoche und Report funktionieren mit weiterhin konstantem nativen `overlay`-ID. B unverändert. | Erfüllt |
| F-02 | Drain, Scrollkind gehalten | Auch die Enkelvorbereitung gehört zum Drain. Kein vorzeitiges Reopen; danach neue routbare Kette und finale alte Kinder. B unverändert. | Erfüllt |
| F-03 | Native idlocation | Neue Generation ist bereits bereit, während altes Overlay noch gehalten wird. Unterschiedliche native IDs, gleiche logische Rolle. Nach alter Bereinigung erreicht Offset 9 den neuen Root. B unverändert. | Erfüllt |
| F-04 | Tatsächlich fehlerhaftes Overlay-XML | Originalparser meldet `Unexpected end`. Expliziter Fehlerakteur leitet Fehler an A; Root schließt, alle A-Akteure final, kein READY, B unverändert und keine unbehandelte Rejection. | Erfüllt |
| F-05 | Tatsächlich fehlerhaftes Scroll-XML | Fehler wird über das schon erzeugte Overlay an A weitergereicht. Auch Overlay und Relay werden beendet; Originalfehlermeldung ist im Rootereignis erhalten. B unverändert. | Erfüllt |
| F-06 | Alter Initialisierungsfehler nach Reopen | Alte held Initialisierung schlägt erst nach READY der neuen Epoche fehl. Diagnose bleibt erhalten, alter Relay wird beendet; neue Sitzung bleibt geöffnet und routbar, B unverändert. | Erfüllt |

[Resultate](variant-results.json) enthalten pro Fall sämtliche Prüfaussagen, Start-/Fehler-/Cancelentscheidungen, tatsächliche Ereignisse und Snapshots vor sowie nach Cleanup. Beide Varianten verwenden denselben gepinnten unveränderten Interpreter 4.3.28. Originalschemas bestätigen die sieben beabsichtigt gültigen Modellvarianten und den Relay: [Preflight](schema-preflight.json). Das absichtlich unvollständige XML ist die Fehlerquelle und wird nicht als gültiges Modell ausgegeben.

## Regression und erhaltene eigene Erstabweichung

LC-01–LC-08 wurden für den Pfad mit nativer idlocation und Fehlerrelay wiederholt. Alle acht Erwartungen sind erfüllt. Das zeigt im kontrollierten Umfang getrennte Parameter und Daten, native Parentroute, eigene Fremdkontextguards, Cancel auf beiden Vorbereitungsebenen, sofortiges Reopen, richtige Fehlerweiterleitung und wiederholtes CLOSE. Native IDs und logische Level stehen getrennt in den Snapshots. `sameLocalIds` im übernommenen Runner bezeichnet weiterhin die logischen Rollen overlay/scroll; **nicht** über Generationen konstante native IDs. Die getrennte neue F-03-Aussage prüft gerade deren Unterschied. Regressionsläufe erhöhen die Bedingungszahl nicht.

Der erste eigene Fehlerdatensatz enthielt `expr="???"`. Dieser erzeugte im untersuchten Originalpfad nicht den beabsichtigten Parser-/Preparefehler; der Adapter sah deshalb keinen gefangenen Vorbereitungsfehler und LC-07 blieb verletzt. Diese fehlerhafte Testannahme ist in [erster Fixture](invalid-initial.scxml), [ersten Resultaten](regression-initial-results.json), [erstem Runner](regression-initial.cjs) und seinen Rohlogs erhalten. Sie ist kein Nachweis, dass beliebige ungültige Ausdrücke schon bei der Vorbereitung erkannt werden. Der Fehlerfall wurde anschließend mit wirklich unvollständigem XML `<scxml` am Originalparser ausgelöst. Außerdem wartet der korrigierte Runner explizit auf Fehlerweiterleitung und finale Kinder statt nur auf kurze Ablaufpausen. Erwartungen an Fehlerweiterleitung wurden nicht abgeschwächt. Ein Diagnoseversuch mit syntaktisch auffälligem Script ist nicht als zusätzlicher Beleg oder neue Bedingung gezählt.

## Technische Einordnung und nächster Umfang

Für den **nächsten begrenzten Referenzversuch** ist die Variante mit originaler idlocation der kleinere Eingriff: Die bestehende Generationstrennung bleibt erhalten; hinzu kommen native IDspeicherung und dynamische Sendziele. Sie benötigt keine zusätzliche Warteschlange, welche bei nicht zurückkehrender Vorbereitung blockieren kann. Das ist eine technische Empfehlung innerhalb dieses Forschungsfalls, keine Wahl der produktiven Runtime oder Formatsyntax. Der Fehlerrelay ist in beiden Fällen zusätzliche fachlich sichtbare Adapterlogik und muss als solche erhalten bleiben.

Die ursprünglichen LC-06-/LC-07-Blocker sind damit für diesen ausgewiesenen neuen lokalen Adapterpfad begrenzt umgangen. Sie sind **nicht** im Original-Defaultpfad verschwunden. IP-A05/A06 bleiben als vollständige Gates offen: echte Hostviews, echte Fokus-/Scrollbeobachtung, Typ-/Resultatdaten und das gesamte aufgelöste Vier-Domänen-Paket fehlen hier weiterhin. Manuelle Assistenztechnik und andere Zielplattformen sind nicht ausgeführt.

Vor Fortsetzung der engen Forschung ist keine Nutzerentscheidung zwischen Drain und idlocation nötig. Der technisch kleinere Pfad kann als Forschungskandidat verwendet werden. Vor Produktumsetzung bleiben die fachlichen Auswahl-/Eingabevarianten, Zielplattformen und endgültige Bindungssyntax Gegenstand der Profilreview.

## Reproduktion und Zählung

Nach Bereitstellung der gepinnten benachbarten Runtimeabhängigkeiten: `node run.cjs` für die sechs neuen Varianten; `node regression.cjs` für die acht nicht erneut gezählten Regressionsfälle. Beide enden in diesem Stand mit Status 0. Der erste Runner und seine damalige Fehlerfixture sind Archivmaterial; für eine exakte Wiederholung ihres Fehlversuchs muss die damalige Fixture bereitgestellt werden, statt still die korrigierte invalid.scxml zu verwenden. Original- und Eigenartefakthashes vorher prüfen.

Es werden ausschließlich **sechs neue Bedingungen in einer neuen Gruppe** gezählt. Keine zusätzlichen Zähler für Regessionswiederholungen, Einzelaussagen eines Falls, schematische Vorläufe oder korrigierte eigene Testdaten. Frühere acht Fälle einschließlich beider Verletzungen bleiben in ihrer eigenen Gruppe unverändert. Keine Matrixklassifikation geändert, kein Originalmodul verändert, kein Commit oder Push.
