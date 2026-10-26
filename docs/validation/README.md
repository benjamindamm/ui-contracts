# Gemeinsame Prüfkette · aktueller Webprüfer angebunden

Stand: 26. Oktober 2026. Der reproduzierbare Einstieg verbindet jetzt die statische Prüfung mit einem **tatsächlich neu ausgeführten Browserlauf**. Dies ist ein begrenzter Werkzeugnachweis für die fest gepinnte IP-01-Webreferenz, kein allgemeiner Komponentenvalidator. Der [separate lokale Agent-Skill](../skills/README.md) nutzt diese Kette mit denselben Grenzen.

## Ergebnis

Der aktuelle Lauf `e8d7f7ca6d76afb7cf3be99aec861b65` erfüllt die bisherigen **20 Browserfälle**. Tatsächliche Tastatur-/Fokusaktionen, öffentliche Events, Scrollmessungen, Chromium-AX-Bäume und ausgewählte Lifecycle-/Fehlerfälle wurden neu aufgezeichnet. Die 20 bekannten Fälle sind Regressionen; Wiederholungen werden nicht als neue Kandidatenmatrixbedingungen gezählt.

- [Gemeinsames strukturiertes Ergebnis](../../tools/validation/evidence/web-current.json): alle sechs Stufen bestanden, `PASS_LIMITED`, `release:true` ausschließlich für `exact-pinned-bounded-web-reference-only`; `productionRelease:false`.
- [31 neue Browser-Gegenfälle](../../tools/validation/evidence/browser-countercases.json): alle Erwartungen erfüllt; fehlende, veraltete oder manipulierte Ergebnisse sowie fachliche Fehler verhindern die Freigabe.
- [47 bisherige Gegenfälle erneut geprüft](../../tools/validation/evidence/countercases.json): alle Erwartungen weiterhin erfüllt.
- [Zwei tatsächliche negative Collector-Kontrollen](../../tools/validation/evidence/collector-negative-controls.json): falsche Lauf-Challenge und doppelter Capture werden mit HTTP 400 abgewiesen.

Der erfolgreiche Bericht ist ein datierter Nachweis. Er bleibt keine zeitlich unbegrenzte Freigabe: Der Prüfer akzeptiert explizit übergebene Laufdaten höchstens zwei Stunden nach Vorbereitung und nur für unveränderte Quellen und Prüfer. Ohne aktuelles `--browser-run` blockiert der Standardaufruf weiterhin.

## Einstieg und Nachweise

- [Ausführung, Abdeckung, Reparaturregeln und sechs Schritte](../../tools/validation/README.md)
- [Inventar der Original- und Zusatzprüfer](../../tools/validation/inventory.json)
- [Statisches Profil](../../tools/validation/profile.json), [feste Paket-/Hostbindung](../../tools/validation/browser-profile.json)
- [Gemeinsamer Aufruf](../../tools/validation/check.py), [Browseradapter und Collector](../../tools/validation/browser_gate.py)
- Aktueller Lauf: [Auftrag/Quellbindung](../../tools/validation/evidence/browser-2026-10-26-run03/request.json), [Capture- und Ausführungsbelege](../../tools/validation/evidence/browser-2026-10-26-run03/collection.json), [Auswertung](../../tools/validation/evidence/browser-2026-10-26-run03/results.json)
- [Evidenzübersicht einschließlich erhaltener Vorstufen](../../tools/validation/evidence/README.md)

## Was die Verbindung tatsächlich bedeutet

Das statische Referenzpaket und der spätere ausführbare Browserhost sind verschiedene Artefakte. Die Verbindung ist deshalb eine **explizite feste Zuordnung**: Der Adapter akzeptiert ausschließlich die bekannte statische Paketrevision und die festgelegten Host-/Runtimebytes. Er erzeugt daraus keinen beliebigen Host. Ändert sich eine ansonsten statisch gültige Kandidatenkopie, blockiert die Webfreigabe, bis eine begründete neue Zuordnung und ein aktueller Lauf vorliegen.

Jeder Lauf erhält eine neue Kennung und zufällige Challenge. Sein Auftrag bindet Paketdateien, Hostdateien, Runtime, Prüfer und Erfolgskriterien. Vier Browseroperationen und sämtliche notwendigen Captures müssen vollständig, erfolgreich und demselben Lauf zugeordnet sein. Die Auswertung liest die Rohdaten erneut und prüft zentrale Events/Fokus-/Scroll-/Lifecyclewerte zusätzlich zu den erhaltenen fachlichen Assertions. Ein vorhandenes Ergebnis-JSON mit `allPassed:true` genügt nicht.

Diese lokale Belegkette verhindert versehentliche Wiederverwendung fremder oder alter Ergebnisse. Sie ist keine kryptografische unabhängige Attestation gegenüber einem böswilligen lokalen Betreiber, der alle Dateien kontrolliert.

## Erhaltene Grenzen und Vorstufen

CEM-/SCXML-Originalschemas und die zusätzlichen Typ-/Referenz-/Token-/Hostprüfungen bleiben getrennt ausgewiesen. Das lose SCXML-XSD deckt nicht sämtliche Recommendation-Regeln ab; CSS/DTCG/HTML/ARIA/APG sind nicht vollständig originalvalidiert. Reale IME, Screenreader-Ausgabe, physische Tastaturprüfung, iOS und Android sind nicht abgenommen. Die aufgezeichnete Geometrievariation ist kein allgemeiner Theme-/Quellenänderungsnachweis.

Die ersten Adapterläufe bleiben erhalten. Nach Ergänzung der Ausführungsreceipts und abschließender Prüfer-/Berichtshärtung wurden alle 20 Browserfälle erneut durchgeführt; maßgeblich ist run03 mit der aktuellen Prüferbindung. Diese Wiederholungen erhöhen keine Forschungszähler. Alte Ergebnisse werden vom aktuellen Prüfer wegen abweichender Prüferbindung zurückgewiesen.

Der [Skill `$ui-contracts`](../skills/README.md) ist inzwischen separat erstellt, lokal installiert und funktional geprüft; er erweitert die Validatorabdeckung nicht. Nichts wurde veröffentlicht. Historische Forschung und AC-R01 bleiben unverändert; die 702 Bedingungen/106 Gruppen, 416 Bewertungen und 543 Claims der ursprünglichen Kandidatenrecherche werden nicht fortgeschrieben.
