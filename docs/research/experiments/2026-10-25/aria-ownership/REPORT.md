# WAI-ARIA: führende Namensquelle und nachvollziehbare Hostableitung

Stand: 25. Oktober 2026. **WAI-ARIA X08 A/C504**, ausschließlich für die zusätzliche Namens-Ownershipkette unten. **39 U:24 Integration,15 weitere. 465 Bedingungen in60 Gruppen.** Kein normatives ARIA-Paket-Governancemodell daraus abgeleitet.

## Ursprünglicher Beitrag und begründete Ergänzung

WAI-ARIA1.2 REC vom6. Juni2023 beschreibt listbox mit benennungsbedürftiger, durch Autorinhalt festgelegter Semantik. aria-label liefert einen erkennbaren Objektnamen; vorhandenes aria-labelledby hat bei der Namensberechnung Vorrang. Diese ursprünglichen Rollen-/Attributregeln sagen nicht, welche Projektdatei führen oder wie eine abgeleitete Hoständerung protokolliert werden soll.

Der vorangegangene Ownershipversuch S85/C459 prüfte bereits konkrete Visualwert-/Eventnamensableitungen. Die dort ausdrücklich offene A11y-Ownership wird hier um genau eine bestehende Information ergänzt: den bereits vorhandenen Namen von list-a aus accessibility.html. Dafür ist eine zusätzliche Regel begründet. Sie ist ein Forschungsprofil, keine Originalfähigkeit von ARIA, kein allgemeines Format und keine neue Produktentscheidung.

## Konkrete Zuständigkeit

[policy.json](policy.json) legt ausschließlich resultListAccessibleName/A fest. Führend ist accessibility.html, Element list-a mit role=listbox, Attribut aria-label. Das CEM-Originalartefakt benennt den list-Part; der bereits vorhandene A/B-Host adressiert list-a/list-b. Im eingeschränkten Profil wird list-a als Instanz A gebunden. Die eigene Prüfung liest die tatsächliche HTML-Struktur, verlangt eindeutiges ID-Ziel und prüft den ursprünglichen Rollenbeitrag.

Zulässige Ableitung ist ausschließlich aria-label desselben Elements in der getrennten Hostkopie. CEM, SCXML und CSS bleiben bytegleich; sie definieren den Namen nicht ein zweites Mal. Die neue führende Quelle enthält Suchergebnisse A; der resultierende Host trägt exakt denselben Wert. Instanz B behält Ergebnisse B.

Jede angenommene Änderung trägt deklarierte Actorrolle/-bezeichnung, Informationsschlüssel, ursprünglichen Quellenort und abgeleiteten Zielort, Quell-/Hosthashes vor und nach der Änderung, Policyhash und gemeinsame Revisionshashes. Die Prüflogik stagiert in Speicher und verwirft abgelehnte Anträge ohne Änderung der Ausgangsbytes; keine persistente atomare Transaktion oder authentifizierte Agentenrolle nachgewiesen.

## Zehn zusätzliche Bindungsbedingungen P59

[Gespeicherte Erwartungen und Anträge](cases.json), [Resultate](results.json), [Journal der angenommenen Änderung](accepted.json), [Prüfer](run.py).

| Fall | Ergebnis |
| --- | --- |
| accepted-source-change | Führende Namensänderung und passende Hostableitung angenommen, Journal erzeugt. |
| host-only-edit | Änderung allein im abgeleiteten Host abgewiesen. |
| stale-source | Veralteter Quellhash abgewiesen. |
| stale-policy | Veralteter Policyhash abgewiesen. |
| wrong-owner | Deklarierte Visualrolle für diese Namensinformation abgewiesen. |
| foreign-instance | list-b als Ziel der A-Änderung abgewiesen. |
| unrelated-edit | Gleichzeitige sachfremde CSS-Änderung außerhalb des festgelegten Beitrags abgewiesen. |
| competing-label-reference | Antrag auf zusätzliches aria-labelledby als außerhalb des eingeschränkten Namenspfads abgewiesen. Das ist keine Behauptung, aria-labelledby sei ungültiges ARIA; sein ursprünglicher Vorrang erfordert eine andere konkrete Bindingregel. |
| mismatched-derived-label | Abweichender abgeleiteter Hostname abgewiesen. |
| concurrent-leading-values | Zwei konkurrierende führende Namenswerte abgewiesen. |

Alle zehn vorab benannten Beobachtungserwartungen erfüllt. Die synthetischen Antragsfelder sind ausschließlich Eingaben dieses Prüfers; es wurde keine universelle Autorisierungs-/Konfliktsprache eingeführt. Die ergänzende Policy wird nicht als ursprüngliche normative ARIA-Funktion ausgegeben.

## Zwei native Namensbedingungen P60

[Browserergebnis](browser-results.json). Die tatsächlichen Vorher-/Nachher-Hostdateien werden als getrennte statische Forschungsdokumente im nativen Chromium dargestellt. Sein Role-/Name-Snapshot zeigt listbox-Namen vor Änderung Ergebnisse A/Ergebnisse B und nach Änderung Suchergebnisse A/Ergebnisse B. Zwei Erwartungen erfüllt. Die DOM-Attribute sind zusätzlich gespeichert; die Namensfeststellung beruht auf dem zugänglichen Browserbaum, nicht allein auf dem Attributstring.

Keine Liveaktualisierung derselben DOM-Knoten, physische Tastatur, Fokusfunktion, Plattformübertragung oder Assistenztechnik geprüft. Die unveränderten Host-Fixtures sind keine vollständige Produktions-Autocompletekomponente. Unterstützte Rollen-/Namenssemantik und Prüfgrenzen werden nicht als Gesamt-Konformität ausgegeben.

## Bewertung und verbleibender Rest

WAI-ARIA X08 U→A/C504 für die ausdrücklich zusätzliche Autorquelle→Hostname-Kette mit nachvollziehbarer Revision. Wie bei CSS-X08 wird nur der konkrete Beitrag gewertet; ein Nachweis für alle Informationen ist daraus nicht abgeleitet. Andere ARIA-Zustände, Beziehungs- und Meldungswerte sowie Namensberechnung mit konkurrierendem aria-labelledby bleiben gesondert zu binden.

APG X08 bleibt U/C363: Der informative Guide ist weder diese Namensquelle noch ihr Änderungsjournal. Keine automatische Übertragung der Bewertung und keine Auswahl einer APG-Produktvariante. Der zuletzt geprüfte uSpec-Builder wird dadurch ebenfalls nicht zu einer unabhängigen Vier-Domänen-Ownershiplösung.

## Reproduktion

prepare.py kopiert beziehungsweise adressiert die bestehenden eigenen CEM-/SCXML-/CSS-/HTML-Fixtures und speichert Policy/Erwartungen; run.py verarbeitet die zehn Anträge und erzeugt Hostdokumente für einen isolierten lokalen Forschungsserver. browser-capture.json enthält tatsächliche native Vorher-/Nachher-Snapshots; browser-results.json wertet ausschließlich die zwei vorab festgelegten listbox-Namenspaare aus. source-manifest.json hält Quellen-/Input-/Methodenhashes fest. Kein Commit/Push, keine neue Produktionskomponente oder neue Originalstandardsprache.
