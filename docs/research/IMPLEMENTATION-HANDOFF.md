# Übergabe: IP-01 schrittweise nachweisen

**Recherche abgeschlossen:** [Abschluss und Lesereihenfolge](RESEARCH-CLOSEOUT.md). iOS/Android sind spätere Perspektiven und keine Abschlussbedingung dieser Phase.


Stand: 25. Oktober 2026. **Dokumentierter Umsetzungsauftrag.** Arbeitspaket 1 wurde inzwischen begrenzt ausgeführt: [sechs erfüllte und zwei verletzte Erwartungen](experiments/2026-10-25/ip01-lifecycle/REPORT.md). Die [anschließenden Folgevarianten](experiments/2026-10-25/ip01-followup/REPORT.md) erfüllen sechs neue Bedingungen und acht nicht erneut gezählte Regressionen; die zwei alten Verletzungen bleiben dokumentiert. [Arbeitspaket 2 ist statisch ausgeführt](experiments/2026-10-25/ip01-static/REPORT.md): 27 Bedingungen erfüllt, gemeinsamer Quellenabschluss mit drei Definitionen und vier Domänen vorhanden. [Arbeitspaket 3 ist als ausgewählter Webreferenzlauf ausgeführt](experiments/2026-10-25/ip01-browser/REPORT.md): 20 Bedingungen erfüllt, eigene Behavior-/Hostquellen explizit ergänzt. Keine Produktionskomponentenimplementierung. Arbeitsgrundlage: [Integrationsprofil](INTEGRATION-PROFILE.md), [Bindungsentwurf](INTEGRATION-BINDING-DRAFT.md), [15 geplante Abnahmefälle](INTEGRATION-ACCEPTANCE.md), [vorhandene Belege](INTEGRATION-PROFILE-EVIDENCE.json).

## Ziel und Arbeitsgrenze

Ein gemeinsames, reproduzierbares Webreferenzpaket soll dieselben zwei Autocomplete-Verwendungen durch Interface, Visual, Behavior und Accessibility verbinden. Einzelne Gates dürfen vorgezogen werden, wenn sie keine endgültige Syntax- oder Produktentscheidung benötigen. Jede tatsächlich ausgeführte Teilprüfung wird mit ihrem engen Umfang dokumentiert. Ein erfolgreicher Runtimekern ist noch keine vollständige Abnahme.

Die ersten Arbeiten verändern keine Originalstandards. Bestehende Originalprüfer, Zusatzadapter, erwartete Ergebnisse und widersprochene Erwartungen bleiben getrennt. Google DESIGN.md X06 und OpenUI X06 bleiben ohne neue Originalinformation offen. Wiederholte alte Proben liefern dafür keinen neuen Beleg. Keine Autorenanfragen, neuen Chats, parallelen Agenten, Commits oder Pushes sind Bestandteil dieser Übergabe. Produktive UI, veröffentlichter Skill und native Portierung folgen später.

## Arbeitspaket 1: unabhängiger Lifecyclekern

**Warum zuerst:** Der bekannte Defaultinvoker kann Kinddaten derselben Quelle koppeln. Der vorhandene isolierende Forschungsadapter wurde nur für eine enge lokale Childdatei geprüft. Die Erweiterung auf zwei Kompositionsebenen ist ein technischer Engpass, der sich ohne endgültiges Bindungsformat untersuchen lässt.

### Eingänge und erlaubte Änderung

- Gepinnte Originalruntime samt Lockdatei aus [SCXML-Runtime](experiments/2026-10-25/scxml-runtime/REPORT.md) verwenden.
- [Defaultinvoke-Gegenbefunde und begrenzten Adapter](experiments/2026-10-25/scxml-invoke/REPORT.md) einschließlich Originalresultaten erhalten.
- Eigene minimale Forschungsmaschinen Parent/Overlay/ScrollArea erstellen. Nur Kontext, Parameter, Nachrichtenzustellung und Lifecycle untersuchen; keine vorgetäuschte DOM-/Scroll-/Keyboardfunktion.
- Den ausgewiesenen Adapter für einen expliziten lokalen Quellenbestand erweitern. Originalcode unverändert lassen. Frische Modellvorbereitung je Verwendung; ursprüngliche Send-/Parent-/Cancelmechanismen soweit tatsächlich verwendet benennen.
- Fallliste und Sollausgaben **vor** Ausführung speichern. Kontrollierte Verzögerungen über eine dokumentierte Testschnittstelle erzeugen; keine zeitabhängigen Zufallsschleifen als Beweis.

### Vorab festzuhaltende Fälle

| ID | Aufbau / Aktion | Erwartung und notwendige Beobachtung |
| --- | --- | --- |
| LC-01 | A/B verwenden identische Overlay-/Scrollquellen und wiederholte lokale IDs `overlay`/`scroll`. | Beide Ketten starten mit eigenen Parametern. Tatsächliche Sitzungen, Parentbezüge und mutable Daten sind getrennt. |
| LC-02 | Nur A/overlay/scroll verändern; danach beide Eltern abfragen. | Änderung erreicht ausschließlich A; Daten und Rückmeldungen von B bleiben unverändert. Objektidentität und beobachtete Werte getrennt protokollieren. |
| LC-03 | Nachricht mit gleichem Ereignisnamen an beide gleich benannten Kinder; falschen Kontext gezielt einspeisen. | Parentroute bleibt instanzbezogen. Zusatzprüfung weist fremde Kontextbindung sichtbar zurück; ursprüngliche Zustellung und zusätzliche Schutzwirkung werden nicht vermischt. |
| LC-04 | A schließen, während Overlay vorbereitet wird; Freigabe der Initialisierung danach. | Später erzeugtes Overlay wird beendet und wirkt nicht auf geschlossene/neue Sitzung; keine verwaisten gestarteten Enkel. |
| LC-05 | A schließen, während ScrollArea vorbereitet wird; Vorbereitung danach abschließen. | Auch der zweite Kompositionslevel kann kein Kind nachträglich wirksam einhängen. Beide Ebenen und Parentbezüge tatsächlich beobachten. |
| LC-06 | A öffnen, schließen, wieder öffnen; alte READY-/Datenrückmeldung zustellen. | Neue Epoche und frische Childdaten. Alte Rückmeldung wird ohne Wirkung verworfen; B bleibt währenddessen unverändert. |
| LC-07 | Overlayinitialisierung beziehungsweise Scrollinitialisierung getrennt fehlschlagen lassen. | Fehler erreicht den richtigen Parent; bereits erzeugte Ressourcen werden beendet. Kein falsches READY, keine Veränderung von B. |
| LC-08 | Einen normalen Abschluss sowie mehrfaches CLOSE ausführen. | Deterministischer Abschluss ohne weitere Zustandsänderung durch doppelte Beendigung; keine nachlaufenden wirksamen Rückmeldungen. |

Diese IDs sind **Planungskennungen, keine neuen gezählten Bedingungen**. Bei Ausführung Erwartungen weiter zerlegen, wenn ein Fall mehrere unabhängige Beobachtungen verlangt; neue Zählung erst aus tatsächlich gespeicherten Resultaten ableiten. Für Initialisierungsfälle sind Erfolg und Abbruch beider Ebenen zu beobachten, nicht nur ein zuletzt sichtbarer Parentzustand.

### Fertigkriterium des ersten Pakets

Report mit reproduzierbarem Aufruf, Laufzeit-/Adapter-/Quellhashes, vorab gespeicherten Erwartungen, tatsächlichem Ereignisjournal und Endzuständen aller Instanzen. Ergebnisse enthalten auch Fehlversuche und Änderungen am eigenen Adapter. Kontrollierte lokale Modelle bleiben als solche bezeichnet. Kein Anspruch auf Remotequellen, allgemeines SCXML-Invoke, beliebige Fremdmaschinen, Host-UI oder Assistenztechnik.

Ein scheiternder Fall ist ein Ergebnis und wird nicht durch eine weichere Erwartung nachträglich zum Erfolg gemacht. Eine korrigierte eigene Implementierung erhält neue Ausgaben und bewahrt den ursprünglichen Gegenbefund. Erst dann IP-A05/A06 als **teilweise belegt** beziehungsweise weiterhin offen präzisieren; vollständige Host-/Datenanforderungen bleiben gesondert.

## Arbeitspaket 2: Originalartefakte und statischer Abschluss

1. Referenzdateien für die drei Definitionen erstellen, vorhandene Originalsyntax verwenden. Erforderliche T0-/T1-Signaturen, Parts und Ports ausdrücklich deklarieren. Typtext in CEM benötigt einen ausgewiesenen unterstützten Parser-/Prüfpfad; nicht aus einem String bereits einen Runtimevalidator ableiten.
2. Den kleinen Bindungsentwurf für tatsächliche Dateien präzisieren: konkrete Locator, erlaubte Zielarten, Instanzpfade, Typumfang und Quellführung. Erst jetzt ein enges Schema und einen Prüfeinstieg erstellen. Illustrative Null-Locator dürfen nicht aufgelöst erscheinen.
3. Tatsächlichen Quellenabschluss aufzeichnen. Originalprüfung → Zusatzbindung → semantische Negativfälle getrennt ausführen. Änderungen mit aktualisierten Hashes prüfen, damit falsche Instanz/Zielart nicht nur als Integritätsfehler auffällt.
4. IP-A01–A04 und IP-A15 statisch soweit möglich ausführen. T1-Datenprüfung ist ein neues Gate; primitive Altbelege reichen dafür nicht.

**Fertig:** Ein korrektes Paket löst eindeutig auf; jede geplante fehlerhafte Beziehung erzeugt eine konkrete Diagnose. Fehlender Prüfumfang bleibt sichtbar. Eine statische Auflösung gilt nicht als Runtimeabnahme.

## Arbeitspaket 3: Hostbindung und vollständiger Ablauf

- Den nachgewiesenen Lifecyclekern mit echten Input-/Overlay-/Viewport-/Listbox-/Option-/Statuszielen verbinden. Keine Auswahlentscheidung in einen unsichtbaren Integrator verschieben.
- Aktive Option über Datenkey führen; tatsächliche DOM-Lage und Scrollsichtbarkeit messen. Öffnen, Navigation, Commit, Schließen und Reopen mit unabhängiger Instanz B protokollieren.
- Requests einschließlich vertauschter Antworten, Empty/Loading/Fehler und programmatischer Änderung prüfen.
- Tokens einschließlich expliziter Einheiten und begrenzter Farb-/Themeübersetzung mit dem tatsächlichen Host prüfen. Zeilen-/Flexgegenbefund und gültiges, aber für dieses Profil ungeeignetes `clip` erhalten.
- Öffentliche Eventfolge, Fokus, aktive/zugänglich ausgewählte/bestätigte Werte sowie AX-Rückmeldungen gemeinsam ausführen. Echte Assistenztechnik gesondert mit benannter Umgebung prüfen.

**Fertig:** Sämtliche beanspruchten IP-Gates sind an derselben aufgelösten Paketrevision ausgeführt. Nicht ausgeführte Browser-/AT-/Nativevarianten bleiben offen. Dokumentations- oder Schemaprüfung darf nicht als tatsächlich bediente Oberfläche ausgegeben werden.

## Noch zu präzisierende fachliche Randfälle

Die nachfolgenden Regeln sind **zusätzliche Vorschläge zur Review**, keine bereits nachgewiesenen Eigenschaften und keine allgemeinen APG-Pflichten. Sie verhindern, dass ein Coding-Agent diese Varianten beiläufig entscheidet.

| Randfall | Vorschlag für IP-01 | Zu ergänzende Abnahme |
| --- | --- | --- |
| Fokus verlässt die gesamte Suche | Schließen ohne neue Bestätigung; Query und letzter bestätigter Key bleiben bestehen. | Tatsächlicher Tab-/Fokuswechsel entfernt aktive Beziehungen und beendet Kinder; kein unerwartetes Commit. |
| Maus-/Touchbestätigung | Zunächst explizit außerhalb des ersten Keyboardreferenzlaufs. Eine produzierte interaktive Komponente benötigt später auch diesen Pfad. | Kein universeller Bedienbarkeitsanspruch aus Keyboardfällen; spätere Variante muss Blur-/Pointer-Reihenfolge prüfen. |
| Eingabe während Childvorbereitung | Neueste Query speichern; nach READY nur diese Generation anfordern. | Mehrere Eingaben in opening lösen keine wirksamen alten Antworten oder zusätzlichen Children aus. |
| IME-Komposition | Queryentwurf darf folgen; Commit/Navigation durch Enter-/Pfeiltasten während Komposition unterdrücken. Provideranfrage nach Composition-Ende für aktuellen Entwurf. | Zusammengesetzte Eingabe erzeugt keine Auswahl; erwartete Providerfolge und abschließende Query protokollieren. |
| Neue Query nach aktivierter Option | Aktivmarkierung löschen; neue Requestgeneration. Der bestätigte Wert bleibt gemäß IP-01 erhalten. | Keine versehentliche Bestätigung einer alten Option, auch vor Eintreffen neuer Daten. |
| Gültige Antwort bei ausschließlich deaktivierten Ergebnissen | Ready mit leerem activeKey; Navigation/Enter bestätigen nichts. | Kein Sprung zu deaktivierter Option und keine Endlossuche. |
| Aktive Option wird unter demselben Request neu geordnet | Vorhandenen Key erhalten und Sichtbarkeit neu anfordern; bei Entfernung activeKey löschen. | Neuer DOM-Bezug bleibt derselben fachlichen Option zugeordnet; kein neuer Commit. |
| Leere oder doppelte Keys | T1-Datensatz abweisen; Fehlerpfad statt teilweise erfolgreicher Übernahme. | Vorheriger aktueller Zustand wird nicht durch halb angewendete Ergebnisse inkonsistent. |
| Requestzähler ausgeschöpft | Weitere Requests kontrolliert mit Diagnose stoppen; kein stilles Zurücksetzen in derselben Epoche. | Grenzwert als unterstützte sichere Ganzzahl explizit festlegen und testen. |

Datenantworten sollten für das erste Profil atomar validiert und übernommen werden: Bei fehlerhaftem aktuellem Datensatz in den Providerfehlerpfad wechseln, aktive Liste bereinigen und bestätigten Wert erhalten. Diese Ergänzung gehört nach Review in Behavior und Interfacefehlerbindung; sie ist nicht durch einen Validator allein erledigt.

## Übergabestatus und offene Entscheidungen

**Vorhanden:** gemeinsamer Profilvorschlag, minimaler Strukturentwurf, explizite Beziehungsliste, Abnahmeplan und priorisierte Arbeitspakete. **Inzwischen vorhanden:** ein tatsächlich geprüftes statisches Forschungsreferenzpaket mit engem vorläufigem Resolver, T0/T1-Wertprüfung und rekonstruierbaren Quellenabschlüssen. **Inzwischen ebenfalls vorhanden:** ein konkret gemeinsam im Browser ausgeführter Forschungs-Host. **Noch nicht vorhanden:** allgemeiner deklarativer Runtime-Resolver und vollständige IP-/Produkt-/Native-/AT-Abnahme. Das erweiterte Lifecycleexperiment liegt vor; sofortiges Reopen und Fehlerweiterleitung sind im ersten Pfad verletzt und in den ausgewiesenen Folgevarianten begrenzt erfüllt. Der nächste Forschungsschritt kann native idlocation und den expliziten Fehlerrelay verwenden. Die neue Paketstruktur erfordert eine ausdrücklich angepasste lokale Quellenbindung; vollständige Host-/Paketabnahme fehlt weiterhin.

Für die Dokumentation ist keine zusätzliche Entscheidung erforderlich. Vor einer produktiven Architektur-/Formatauswahl sind der konkrete Webstack als Referenzumfang, die kleinste hinreichende Bindungssyntax und die fachlichen Varianten des Referenzfalls zu reviewen. Der begrenzte technische Lifecycleversuch kann unabhängig davon vorbereitet und ausgeführt werden, wie im inzwischen ausgeführten Teilversuch geschehen. Native Plattformen und produktiver Reifegrad bleiben spätere Auswahlpunkte; sie blockieren diesen engen Versuch nicht.
