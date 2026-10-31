# AI Elements · Nutzen prüfen, Kern bewahren

**31. Oktober 2026 · Forschungsaufnahme, keine Architekturübernahme.** AI Elements liefert interessante Beispiele für das Zusammenspiel von UI-Bausteinen. Der nächste sinnvolle Schritt für UI Contracts ist eine kleine Kompositionsprobe mit den bestehenden Contracts. Eine zusätzliche Rezept-Sprache, Registry oder React-Abhängigkeit ist bislang nicht begründet.

## Maßstab: unsere Mission

UI Contracts soll als formalisiertes digitales UX-/Design-Handbuch beschreiben, was Komponenten leisten, wie sie aussehen, reagieren und zugänglich bedienbar sind. Agenten sollen diese Originalregeln auffinden, zielgerecht umsetzen und Ergebnisse prüfen können. CEM, DTCG/CSS, SCXML und HTML/ARIA bleiben führend. Generelle Agentenorchestrierung, Chatoberflächen und Modelloptimierung sind keine Voraussetzung dieses Ziels.

Jede Erweiterung muss eine konkrete Lücke schließen, vorhandene Mechanismen zuerst nutzen, einen beobachtbaren Prüffall ermöglichen und den normalen Einstieg schlank halten. Mehr Frameworks oder Beschreibungsdateien sind für sich kein Fortschritt.

## Was die angesehenen Originalseiten zeigen

| Dokumentationsbeobachtung | Quelle | Einordnung |
| --- | --- | --- |
| AI Elements beschreibt kopierbare Patterns aus shadcn/ui-Komponenten. | [Übersicht](https://ui.shadcn.com/docs/ai-elements) | Dokumentierter Ansatz, hier nicht installiert oder ausgeführt. |
| Chat verbindet Message, Message Scroller und Eingabe; die Dokumentation beschreibt Scrollanker und das Folgen einer Antwort am Live-Rand. | [Chat](https://ui.shadcn.com/docs/ai-elements/base/chat) | Interessante konkrete Interaktionsregel für eine Komposition. Keine eigene Prüfung der Implementierung. |
| Confirmation verbindet die Freigabeanfrage und ihre Antwort mit der anschließenden Tooldarstellung. | [Confirmation](https://ui.shadcn.com/docs/ai-elements/base/confirmation) | Beispiel einer übergreifenden Zustandsfolge. |
| Die Skills-Dokumentation nennt Projektinformationen über info --json und gezielte Komponenten-/Dokumentationssuche. | [Skills](https://ui.shadcn.com/docs/skills) | Inspiration für bedarfsgerechte Entdeckung. Eine Qualitätsgarantie der dortigen Agenten wurde nicht geprüft. |

Gelesen über BrowserOS neo am genannten Datum; keine Prüfung eines bestimmten Git-Commits, keine Installation und kein Runtimevergleich. Auf den angesehenen Seiten steht React-basierte UI-Komposition im Mittelpunkt. Eine standardisierte Vier-Domänen-Beschreibung wurde dort nicht untersucht oder nachgewiesen; daraus folgt keine Aussage über sämtliche anderen shadcn-Dokumente.

## Was davon unser Problem löst

| Idee | Bei uns vorhanden | Verbleibender möglicher Nutzen | Empfehlung |
| --- | --- | --- | --- |
| Wiederverwendbare Komposition | component.json mit Unterkomponenten; Autocomplete → Overlay → ScrollArea | Fachliche Beziehungen zwischen mehreren Controls als wiederholbaren, prüfbaren Vertrag ausdrücken | Eine begrenzte Probe mit bestehenden Formaten |
| Passenden Baustein auswählen | ux.json, Faktenkontext, native DMN-Policy | Auswahl in einer größeren Aufgabe mit gemeinsamem Wert/Fokus/Fehlern verbinden | Vorhandene Policy weiterverwenden |
| Agent findet relevante Informationen | Explizite Bibliothek, Index, kompakte CLI-Ergebnisse, Skillrouten und rollenbezogene Übergaben | Echte Such-/Orientierungsprobleme später an konkreten Aufgaben messen | Aktuell kein weiterer Discovery-Dienst nötig |
| Konkrete Beispiele für Zustände/Interaktion | Stories und begrenzte Zielprüfungen | Querbeziehungen als Akzeptanzfälle festhalten, statt nur fertige Bilder zu zeigen | Gezielt auf den nächsten fachlichen Fall anwenden |

Die Zuordnung ist unsere Bewertung, keine Behauptung, AI Elements liefere bereits diese Contractlösung.

## Baseline: nicht noch einmal implementieren

Für die ausdrücklich gewählte Bibliothek `example` 0.4.0 wurden die vorhandenen Faktenfälle erneut durch Quellen-/SCXML-Prüfungen und die Original-DMN-Engine ausgewertet:

- [Drei feste Werte](evidence/three.json): Select.
- [30 feste Werte](evidence/thirty.json): SelectWithSearch.

Beide Ergebnisse bleiben `PASS_LIMITED`, `release:false`, `targetValidationRequired:true`. Die Optionsanzahl und Suchgrenze stammen aus der konkreten Projektpolicy. Das ist eine erneute Baselineausführung, keine neue unabhängige Forschungsbedingung und kein Nachweis einer neuen Formularimplementierung.

Diese Auswahl braucht keine neue Rezeptregel. Der vorhandene [Kompositionsvertrag](../../../../libraries/example/components/autocomplete/component.json) zeigt außerdem schon eine Verbindung mehrerer Teilverträge. Die aktuellen Input-/Select-Verträge beschreiben noch keinen eigenen zusammengesetzten Telefonfeld-Vertrag. Ob dafür eine neue Komponente sinnvoll ist, bleibt eine zu prüfende Produkt-/Modellierungsfrage.

## Abgegrenzte nächste Probe: Telefonnummer erfassen

**Vorschlag, noch nicht umgesetzt.** Derselbe vertraute Anwendungsfall wird mit vorhandenen Mitteln präzisiert. Die erste Aufgabe ist die Klärung der Beziehungen, nicht der Entwurf eines neuen Dateiformats.

1. **Umfang festlegen:** Rufnummerneingabe und Länderauswahl. Keine automatische geografische Priorisierung, E.164-Normalisierung, externe Telefonnummernvalidierung oder Adressvervollständigung hinzufügen, solange der Fachauftrag das nicht verlangt.
2. **Vorhandene Quellen nutzen:** Input, Select/SelectWithSearch, ihre UX-Eignung und die gebundene Auswahlpolicy. Keine Schwelle oder Membershipregel in ein zusätzliches Rezept kopieren.
3. **Fehlende Verbindungen benennen:** Wer besitzt die Werte? Wie bleiben Länderschlüssel und eingegebene Rufnummer getrennt? Welche Events, Labels, Fokus- und Fehlerbezüge gehören zum Zusammenspiel? Ob ein gemeinsames öffentliches API verlangt wird, ist ausdrücklich zu entscheiden.
4. **Mit bestehenden Mitteln modellieren:** Falls eine eigenständige wiederverwendbare UI-Einheit mit gemeinsamem Vertrag gebraucht wird, zuerst einen normalen zusammengesetzten Komponentenkandidaten mit CEM, DTCG/CSS, SCXML, HTML/ARIA und der bestehenden Bindung prüfen. Für eine bloße Anordnung kann ein Beispiel genügen.
5. **Gesamtwirkung prüfen:** Instanz-/Wertisolation, unveränderte Optionsreihenfolge, getrennte Suchquery und Commitwert, tatsächliche Events sowie die vereinbarten Fokus-/Fehlerbeziehungen am ausführbaren Ziel messen. Vorhandene Einzelprüfungen werden weiterverwendet; sie ersetzen keine Kompositionsprüfung.

Eine lokale Zuordnung von Anforderung → führende Datei → Verbindung → Akzeptanzfall reicht zunächst als Forschungsarbeitsmittel. Sie wird keine zusätzliche normative Quelle. Nur ein dabei konkret belegter Ausdrucks-/Prüfbedarf rechtfertigt eine spätere Formaterweiterung.

## Bedingungen für eine spätere Übernahme

- Es entsteht eine wiederverwendbare, fachlich bestimmte und überprüfbare UI-Beschreibung, nicht nur eine hübschere Demo.
- Jede Regel hat genau eine führende Quelle; Auswahl, Verhalten und Darstellung werden nicht parallel in einem Rezept neu definiert.
- Gute und fehlerhafte Kompositionen lassen sich am gleichen vereinbarten Prüfumfang unterscheiden. Nichtprüfbares bleibt sichtbar.
- Der Agent benötigt zum Start weiterhin nur kurze Handlungsregeln und den konkreten Auftrag; eine große Pattern-Sammlung wird nicht automatisch Kontext.
- Die Erweiterung löst einen beobachteten Bedarf, den die bestehenden Contracts nicht angemessen ausdrücken. Sonst bleibt es beim Beispiel bzw. einer normalen Komponente.

Das sind vorgeschlagene Übernahmekriterien, keine bereits bestandene Abnahme.

## Bewusst nicht Teil dieser Aufnahme

Übernahme von shadcn/React/Tailwind als Kernabhängigkeit; Bau eines Chat-/Agenten-UI-Frameworks; neue universelle Rezept-Sprache; neuer Registry-/MCP-Dienst; automatische Wissensinjektion in jeden Turn; neue Modellvergleichspflicht. Konkrete Zieladapter können später gesondert untersucht werden, wenn ein Auftrag dafür besteht.

Die vorhandenen Prioritäten zu Änderungsfolgen, breiteren UX-Regeln und nachvollziehbarer Prüfung werden dadurch nicht ersetzt. Der [abgeschlossene Commitstand](https://github.com/benjamindamm/ui-contracts/commit/d29b652) ist Ausgangspunkt; aktive Bibliothek, Skills und historische Belege wurden in dieser Aufnahme nicht verändert. [Maschinenlesbarer Prüfstand](verification.json).
