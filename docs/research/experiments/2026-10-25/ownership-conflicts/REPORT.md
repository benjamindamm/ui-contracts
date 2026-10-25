# Führende Quelle, nachvollziehbare Ableitung und Konflikte

Stand: 25. Oktober 2026. **Unabhängiger P1-Nachweis zu X08 am bestehenden Originalartefaktpaket.** 20 benannte Bedingungen in fünf Gruppen; eine zunächst verletzte Zusatzprüfer-Erwartung bleibt samt Korrektur gespeichert. Wiederholungen nach Korrektur zählen nicht als neue Bedingungen.

## Fragestellung und vorab gesetzte Endbedingung

X08 verlangt eine je Information dokumentierte führende Quelle und nachvollziehbare Änderungen zwischen Originalformaten und Integrationsschicht. Bisherige Kategorien wie geometry=visual sagen noch nicht, welches Originalfeld führt, wie eine Ableitung nachverfolgt wird und was bei widersprüchlichen Änderungen geschieht.

Endbedingung dieses Pakets: zwei konkrete Informationen im bestehenden CEM-/SCXML-/DTCG-/CSS-/HTML-Paket adressieren, zulässige Änderungen mit Herkunft und Vorher-/Nachherhash annehmen, widersprüchliche/veraltete/unvollständig weitergegebene Änderungen ablehnen und tatsächlich angenommene Änderungen mit originalen Schemas, Original-SCXML-Ausführung beziehungsweise Browserlayout gegenprüfen. Alle Bedingungen wurden jeweils vor ihrer Ausführung gespeichert. Die zusätzliche Policy ist ausdrücklich ein Forschungsprofil, keine ausgewählte Produktsprache oder neue Originalstandardfunktion.

## Zwei begrenzte Zuständigkeitsketten

| Information | Führender Originalort | Zulässige abgeleitete Verwendung | Ausdrücklich nicht übertragen |
| --- | --- | --- | --- |
| Popup-Maximalhöhe | tokens.json: /base/maxHeight/$value; Visualrolle | Zusätzliche Übersetzung in generated-vars.css: --autocomplete-max-height, Verwendung durch unveränderte layout.css an A/B | Verhalten, Auswahlzustand, Anzahl sichtbarer Zeilen, ARIA-Regeln |
| Öffentlicher Eventname | interface.json: /modules/0/declarations/0/events/0/name; Interfacerolle | Genau das SCXML-send/@event und profile.json:/publicEvent dürfen als deklarierte Ableitungen gemeinsam geändert werden | Zeitpunkt/Transition/Aktion der Emission, Payloaddaten, andere SCXML-Struktur |

Bytegleiche Ausgangsquellen stammen aus dem vorherigen DTCG-Paket. baseline.json hält ihre tatsächlichen Bytes einschließlich des zusätzlichen generierten CSS fest. policy.json führt Feldpfade, ableitbare Zielorte, deklarierte synthetische Agentenrollen und Quellhashes. revision.json bindet Quellhashmanifest und Policyhash. Die vorhandene Accessibility-Datei ist eine eigene, unverändert gepinnte Quelle; deren inhaltliche Änderungs-/Ownershipregeln werden hier nicht zusätzlich erfunden.

Eigene Rollenbezeichnungen sind **keine authentifizierten Identitäten**. Ein policykonformer Actorstring ist kein Berechtigungs- oder Sicherheitsbeweis. Das Journal ist eine lokal nachvollziehbare Forschungsaufzeichnung, kein manipulationssicherer Auditdienst.

## 15 Transaktionsbedingungen

| Fall | Erwartetes und beobachtetes Verhalten |
| --- | --- |
| Kein Änderungsantrag | Ausgangswerte akzeptiert |
| Führende Tokenhöhe 160 → 192px | Akzeptiert; generierte CSS-Variable und Hashpins mit Herkunft aktualisiert |
| Generiertes CSS direkt 184px | non-leading-target, Gesamtkandidat verworfen |
| Gleichzeitige Quellvorschläge 192/224px | concurrent-source-conflict, keine Last-write-wins-Auswahl |
| Veraltete Paketrevision | stale-base |
| Veralteter Einzelquellhash | stale-source |
| Fehlende Änderungsherkunft | missing-origin |
| Interfacerolle ändert Visualwert | wrong-role |
| Eventname gemeinsam CEM/SCXML/Profil geändert | Akzeptiert; jeweils Vorher-/Nachherhash und Ableitung protokolliert |
| Nur CEM-Name geändert | public-event-conflict |
| Behavior ändert öffentlichen Namen eigenständig | non-leading-target |
| Abgeleitete Änderung ohne Änderung der führenden Quelle | missing-leading-change |
| Anderer Policyhash | policy-revision |
| Zusätzliche nicht deklarierte Gap-Änderung | undeclared-edit |
| em als dimension-Einheit | dimension-unit |

Alle 15 gespeicherten Regelerwartungen erfüllt, vor und nach der unten beschriebenen Revisionskorrektur. Fehlgeschlagene Kandidaten geben die gesamten Ausgangsbytes zurück und veröffentlichen kein erfolgreiches Teiljournal. **Dies ist In-Memory-Staging** in eigenen Testdaten, kein Nachweis atomarer Dateisystem-/Datenbanktransaktionen, konkurrierender Prozesse oder dauerhafter Wiederherstellung. Dateischreibvorgänge im Originalrepository wurden nicht ausgeführt.

Das Journal nennt Transaktion, Information, führenden Feldpfad, deklarierten Actor, Art der Änderung, betroffene Datei und Vorher-/Nachherhashes sowie Policy-/Ausgangsrevision. Generierte Änderungen und revisionsbedingte Hashauffrischung sind als solche markiert; Originalquellen werden nicht still als fremde Standardformate erweitert.

## Erhaltene verletzte Erwartung und Korrektur

Ein anschließender, vorab gespeicherter Konsistenzfall kontrolliert, ob neue Revisionen exakt denselben kanonischen Algorithmus wie die Ausgangsrevision benutzen: Hash des Dateihashmanifests plus Policyhash. **Die Erstversion des eigenen Prüfers verletzt diese Erwartung:** Sie berechnete die neue Revision nur aus Dateihashes mit anderer Serialisierung; sogar der unveränderte Kontrollfall erhielt eine andere Revision.

run-initial.py, initial-results.json und revision-initial-results.json erhalten diesen Befund. run.py wurde auf denselben kanonischen Algorithmus korrigiert; revision-results.json belegt die nun übereinstimmenden Werte für den Kontrollfall und beide angenommenen Änderungen. Die 15 ursprünglichen Bedingungen wurden als Regression erneut ausgeführt und bestehen; diese Wiederholung wird nicht als 15 neue Nachweise gezählt. Kein Fehler eines Originalstandards wird daraus abgeleitet.

## Praktische Gegenprüfung angenommener Änderungen

1. **Zwei Browserbedingungen:** tatsächlich angenommene Tokenänderung samt generiertem CSS und unveränderter layout.css/HTML an Instanzen A/B dargestellt. Je 192px Popuphöhe, 8px Abstand, 224px Scrollinhalt. Erwartungen erfüllt. Keine Navigation oder Assistenzprüfung.
2. **Eine native SCXML-Ereignisbedingung:** tatsächlich angenommenes gemeinsam umbenanntes Paket wird mit @scion-scxml/scxml 4.3.28 ausgeführt. Native Parent-Sendung selection-change, value=alpha, invokeid=A und Endzustand closed wie erwartet. Kein fingierter Eventproduzent oder neuer CEM-Komponentencode.
3. **Eine Originalschema-Bedingung:** geändertes CEM und SCXML werden gegen dieselben zuvor gepinnten Originalschemata geprüft; beide akzeptiert. Originaldefinitionen unverändert. Dies belegt formale Schemaakzeptanz dieser Änderungen, keine allgemeine Ereignis-/Typ-/Verhaltenskonformität.

## Einordnung

**CSS Layout X08 wird U → A/C459** für diese begrenzte zusätzliche Ownership-/Ableitungskette: Der relevante Visualwert führt außerhalb des CSS, seine CSS-Ableitung und Änderungen sind explizit gebunden; widersprüchliche oder veraltete Vorschläge werden nicht durch die Kaskade aufgelöst. A ist der erforderliche Zusatzprüfer, keine native CSS-Provenienzfunktion. Die weitere Eventnamenskette zeigt eine zweite konkrete domänenübergreifende Bindung desselben Pakets, ohne weitere Kandidatenzellen automatisch umzuwerten.

Damit **55 U-Zellen: 35 Integration und 20 weitere**. Nicht abgeschlossen sind die übrigen Informationen/Kandidaten, vollständige A11y-Ownership, allgemeine Typabbildung, Schemaänderungen/Migration, Identitätsauthentifizierung, Signaturen, Mehrprozessrennen, persistente Transaktionen und plattformübergreifende Integration. Die zwei geprüften Ownershipketten werden nicht als Abdeckung aller Felder ausgegeben. Keine neue Produktentscheidung, Produktionskomponente, Commits oder Pushes.

## Artefakte und Wiederholung

prepare.py erzeugt eigene Ausgangsdaten/Erwartungen aus dem benachbarten DTCG-Paket. run.py prüft die gespeicherten 15 Anträge und erzeugt Annahmekandidaten/Journale. check_revision.py prüft die gespeicherte zusätzliche Revisionserwartung. browser-run.js enthält die tatsächlich eingesetzten Inputs; für Wiederholung einen eigenen leeren Prüftab auswählen. native-event.cjs benötigt den gepinnten scxml-runtime/tool-Ordner. check_schemas.py nutzt die vorher gebundenen CEM-/SCXML-Schemas sowie jsonschema 4.25.1 und lxml 6.1.1. Exakte Hashes der Inputs/Originalschemas und Abhängigkeiten stehen im Manifest und schema-results.json. Diese Werkzeuge sind Forschungsprüfer; keine CLI oder Bibliothek als fertiges Projektprodukt eingeführt.
