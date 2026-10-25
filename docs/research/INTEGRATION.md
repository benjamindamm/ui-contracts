**Einordnung dieses Entwurfs:** Die folgenden Zahlen und „noch nicht ausgeführt“-Aussagen bewahren frühere Prüfrunden. Aktuelle Matrixnachweise stehen in [CURRENT-STATUS](CURRENT-STATUS.md); zusätzlich offene gemeinsame Integrationsarbeit in [PROJECT-GAPS](PROJECT-GAPS.md). Die begrenzten späteren Adapterversuche ersetzen noch keine fertige gemeinsame Architektur.

**Historischer Zwischenstand – 25. Oktober 2026:** 41 offene Nachweise (26 Integration, 15 weitere), 435 benannte Prüfbedingungen in 56 Gruppen. Vollständige Integration, Produkt-UI und Assistenztechnik sind weiterhin nicht nachgewiesen; statische HTML-Host-Fixtures wurden inzwischen im Browser geprüft. Historische Zahlen und „nicht ausgeführt“-Aussagen unten beziehen sich auf die jeweils benannte frühere Runde. Maßgeblich ist das [aktuelle Register](OPEN-FIELDS.md).

**Typisierte Referenzbindung geprüft:** [ARIA-Host → externe CEM-/SCXML-Knoten](experiments/2026-10-25/typed-references/REPORT.md), 16 Erwartungen erfüllt, Original-CEM/SCXML-Schemas separat akzeptiert. WAI-ARIA X03 begrenzt A/C462 durch Zusatzresolver; keine native ARIA-Modellreferenz. Aktuell 54 U, 299 Bedingungen/36 Gruppen.

**Neu: informationsbezogene Ownership geprüft.** [Originalpaket, Quelländerung und Konflikte](experiments/2026-10-25/ownership-conflicts/REPORT.md): zwei führende Informationen mit Ableitungen, 15 Änderungsfälle, eine erhaltene und korrigierte Revisionsverletzung sowie vier praktische Gegenbedingungen. CSS Layout X08 begrenzt A/C459; aktuell 41 U (26 Integration, 15 weitere), 283 Bedingungen in 35 Gruppen. Keine generische Ownership-/Transaktions-/Identitätsgarantie.

**Neue Laufzeitgrenze:** [Original-Defaultinvoke](experiments/2026-10-25/scxml-invoke/REPORT.md) koppelt bei gleichem Child-src die Daten zweier Instanzen trotz separater Elternvorbereitung: drei von sechs Erwartungen verletzt. Cancel/Neustart als Lebenszyklus sind begrenzt ausgeführt; ein Diagnosefall mit unterschiedlichen URIs besteht. Keine gewählte Lösung. Zum damaligen Teilabschluss 56 U-Zellen; in jenem Lauf keine Neubewertung. Sechs zusätzliche Fälle mit eigenem instanzgetrenntem Invokeradapter bestehen; die Originalverletzungen bleiben erhalten (C458).

**DTCG-Folgeprüfung:** [Getrennte Visualquelle mit zusätzlichem Webadapter](experiments/2026-10-25/dtcg-binding/REPORT.md), zwölf Bindungs-/Übersetzungsfälle und vier Browserbedingungen erfüllt. X01 DTCG A/C454 im begrenzten Referenzfall; zum damaligen Teilabschluss 56 U-Zellen. Kein vollständiger DTCG-Validator.

**Ergänzung 25.10.2026 – SCXML-Laufzeit:** [Gespeicherter Prüfblock](experiments/2026-10-25/scxml-runtime/REPORT.md) mit 17 Bedingungen: 9/10 im Ausgangslauf, 2/2 Diagnosefälle und 5/5 Browserfälle. Getrennte Vorbereitung verhindert die beobachtete Datenkopplung. Native Parent-Sendung und ein zusätzlicher interaktiver Forschungs-Host sind ausgeführt; keine Produktionskomponente, physische Tastatur- oder AT-Prüfung. Ältere Aussagen zu ausschließlich statischer Prüfung gelten für die damaligen Teilversuche. Historischer Zwischenstand nach DTCG: 56 U-Zellen.

# Integrationskonzept: getrennte Verträge, gemeinsame Bezüge

Stand: 24. Oktober 2026. **Diskussions- und Arbeitsentwurf, keine ausgewählte Technologie und kein implementiertes Paketformat.** Grundlage sind die abgeschlossenen Kandidatenprüfungen und die bereits bestätigten Projektanforderungen. Es wurden für diesen Entwurf keine neuen externen Quellen geprüft und keine Validatoren oder Laufzeiten ausgeführt.

## 1. Ausgangspunkt und Evidenz

**Bestätigte Projektentscheidungen:** Vier getrennte Domänenbeschreibungen sind bevorzugt. Bestehende Fachmodelle und deren eigene Prüfungen sollen erhalten bleiben. Die Beschreibung soll wiederverwendbare Komponenten und mehrere Instanzen verbinden können. JSON/YAML, URI/URN, Manifest und Resolver sind nicht ausgewählt.

**Belegter Forschungsstand im begrenzten Prüfumfang:** Die Kandidaten liefern unterschiedliche Teilbeiträge. Eine vollständige gemeinsame Verbindung aller vier Domänen wurde nicht nachgewiesen. Eine offene Matrixzelle bedeutet fehlenden Nachweis, nicht bewiesene Unmöglichkeit. Die Einzelbefunde stehen in [Matrix](MATRIX.md), [Begründungen](CLAIMS.md) und [Quellen](SOURCES.md); besonders relevant sind X01–X08.

**Vorschlag dieses Dokuments:** Eine kleine Integrationsschicht beschreibt ausschließlich die Beziehungen, die die Fachmodelle nicht bereits eindeutig abdecken. Sie soll keine zweite Sprache für Properties, Tokens, Zustandsmaschinen oder Accessibility werden. Ob dazu ein eigenes Artefakt nötig ist oder vorhandene Referenzmechanismen genügen, bleibt zu prüfen.

## 2. Drei verschiedene Fragen

| Frage | Benötigte Aussage | Verwechslungsgefahr |
| --- | --- | --- |
| Identität | Welche Definition, Instanz und welcher Teil ist gemeint? | Gleicher Name bedeutet nicht dieselbe Instanz |
| Bedeutung der Beziehung | Wie wird ein Zustand, Ereignis oder Teil auf das andere Modell bezogen? | Gleich geschriebene Zustände können unterschiedliche Bedeutung haben |
| Zuständigkeit | Welche Quelle definiert eine Information und wer konsumiert sie? | Zwei widersprüchliche Definitionen werden durch einen Verweis nicht konsistent |

Ein gemeinsames ID-Format allein löst die letzten beiden Fragen nicht. Ein Verweis auf eine Schemadefinition ist außerdem keine Komponenteninstanz. Das ist bereits als Prüfgrenze in der [Forschungsplanung](RESEARCH-PLAN.md#1-gemeinsame-referenzen-und-komposition) festgehalten.

## 3. Identität und Komposition – vorgeschlagenes Begriffsmodell

Die folgenden Begriffe sind konzeptionell; sie legen keine Feldnamen oder Serialisierung fest.

- **Komponentendefinition:** Wiederverwendbarer Vertrag, etwa Autocomplete oder ScrollArea, mit einem gebundenen Quellenstand.
- **Komponenteninstanz:** Konkrete Verwendung einer Definition, etwa Suche A und Suche B. Instanzdaten und Fokusbeziehungen dürfen sich nicht vermischen.
- **Teil:** Fachlich benanntes Element einer Definition, etwa Eingabe, Overlay, Liste oder Option. Ein Teilname muss im richtigen Geltungsbereich aufgelöst werden.
- **Verwendung einer Unterkomponente:** Das Overlay verwendet eine eigenständige ScrollArea-Definition. Die Verwendung erhält eine eigene Instanz und explizite Parameter-/Ereignisbindungen.
- **Beziehung:** Ein typisierter Bezug zwischen solchen Zielen. Mögliche Arten sind Teilbindung, Zustand-zu-Variante, Ereignisbindung und Accessibility-Beziehung.

**Vorgeschlagene Mindestinformation einer auflösbaren Referenz:** Zieldefinition, reproduzierbarer Quellenstand, Zielart und gegebenenfalls Instanzpfad sowie Teil. Diese Informationen dürfen aus dem Kontext ableitbar sein; sie müssen nicht in jedem String wiederholt werden. Ein Versionsbereich allein reicht nicht als Nachweis reproduzierbarer Auflösung, solange der tatsächlich gewählte Stand nicht feststeht.

**Offen:** Lokale Namen, Namespaces, URI/URN, Paketauflösung, zulässige Rekursion und Migration. Es wird keine allgemeine Zyklusfreiheit verlangt: Unauflösbare oder im gewählten Modell verbotene Zyklen müssen erkannt werden; legitime Rekursion braucht eine ausdrückliche Regel.

## 4. Ownership – vorgeschlagene Verteilung

| Information | Führende Domäne | Andere Domänen dürfen |
| --- | --- | --- |
| Öffentliche Properties, Ereignisnamen und Payloadtypen | Technische Schnittstelle | referenzieren und auf Typverträglichkeit prüfen |
| Eintritt eines Zustands, Auswahlzeitpunkt, Auslösung eines öffentlichen Ereignisses | UX-Verhalten | Zustände und Auslöser referenzieren |
| Tokenwerte, Varianten, Themeauflösung und geometrische Regeln | Visuelles Design | Anforderungen an Sichtbarkeit oder Bedienbarkeit dagegen prüfen |
| Zugänglicher Name, semantische Beziehung und erforderliche zugängliche Rückmeldung | Accessibility | Auslöser aus Behavior und Teile aus der Schnittstelle binden |
| Konkrete Tastatur-/Fokusabläufe | UX-Verhalten innerhalb der gewählten Accessibility-Anforderungen | auf Widersprüche zum gewählten Pattern prüfen |
| Zuordnung derselben Definitionen, Instanzen und Teile | Integrationsbeziehungen, soweit nicht bereits eindeutig vorhanden | bestehende Identität wiederverwenden |

Diese Tabelle präzisiert die bestätigte Trennung, ist aber **noch keine verabschiedete Feldzuordnung für ein bestimmtes Format**. Accessibility formuliert Anforderungen an den zulässigen Fokusablauf; Behavior konkretisiert den Ablauf. Ein Widerspruch wird dadurch sichtbar, nicht automatisch zugunsten einer Datei entschieden.

Beispiel: Die Schnittstelle bestimmt den Typ des Auswahlereignisses. Behavior bestimmt, wann eine Auswahl bestätigt ist und dieses Ereignis auslöst. Visual bindet die Darstellung einer aktiven Option an einen referenzierten Zustand. Accessibility bestimmt die zugängliche Vermittlung dieses Zustands. Aktiv navigiert und endgültig ausgewählt sind getrennte Begriffe.

## 5. Überlappungen und Konfliktbehandlung

**Vorgeschlagener Ablauf:**

1. Für die konkrete Information die führende Quelle bestimmen.
2. Andere Vorkommen als Referenz, abgeleitete Darstellung, Anforderung oder doppelte Definition einordnen.
3. Referenzziel, Typen und Bedeutung getrennt prüfen.
4. Bei Widerspruch betroffene Stellen und verletzte Regel melden; keine stillschweigende Überschreibung.
5. Eine bewusste Produktentscheidung mit Begründung festhalten und sämtliche abhängigen Bindungen aktualisieren.

Ein allgemeines „Accessibility gewinnt immer“ ersetzt keine Konfliktregel. Im ausgewählten Zielprofil geltende Anforderungen müssen erfüllt sein; widersprüchliche Verträge bleiben bis zur Korrektur inkonsistent. Ebenso überschreibt die Reihenfolge der Dateien keine fachliche Zuständigkeit.

**Beispiele:** Ein sichtbares geschlossenes Overlay bei als offen gemeldetem Accessibility-Zustand; Fokusverschiebung auf Optionen bei vereinbartem Verbleib im Eingabefeld; Auswahlereignis mit falschem Payload; ScrollArea und übergeordnetes Overlay verwalten dieselbe Tasteneingabe unabhängig. Für jeden Fall ist eine konkrete Bindungs- oder Zuständigkeitsentscheidung nötig.

## 6. Fachmodelle erhalten, Adapter begrenzen

Die Kandidaten sind weiterhin Alternativen beziehungsweise Teilbeiträge, keine beschlossene Kombination. CEM-/OpenUI-Referenzen, UXSpec-Elementbezüge, Ark-IDs und OpenPencil-Bindungen dürfen nicht allein wegen ähnlicher Namen gleichgesetzt werden. DTCG-Tokenauflösung ist keine Auflösung von UI-Instanzen. ARIA und APG ersetzen keine allgemeine Paketprüfung.

**Vorschlag für jeden erforderlichen Adapter:** Quell- und Zielversion, abgebildete Begriffe, Voraussetzungen, nicht abbildbare Informationen und Prüfgrenzen dokumentieren. Abgeleitete Daten erhalten einen Herkunftsbezug. Eine erfolgreiche Konvertierung ist weder ein Nachweis verlustfreier Rückkonvertierung noch gleicher Laufzeitsemantik.

## 7. Autocomplete als begrenzter Akzeptanzfall

Dokumentarischer Referenzfall: Zwei unabhängige Autocomplete-Instanzen, jeweils mit Eingabe und Overlay; jedes Overlay verwendet eine eigene Instanz einer separat definierten ScrollArea. Die vier Domänen müssen dieselben Instanzen und Teile meinen.

| Fall | Erwartung an die spätere Prüfung | Nachweisebene |
| --- | --- | --- |
| Zwei Instanzen derselben Definition | Keine Vermischung von Werten, Zuständen oder Beziehungen | Referenzprüfung; Verhalten später praktisch |
| Öffnen bei Fokus | Gewählte Produktregel löst Zustand aus, Visual und Accessibility beziehen sich darauf | Bindungsprüfung; Laufzeit später |
| Navigation gegenüber Bestätigung | Aktive Option und ausgewählter Wert bleiben unterschieden | Semantikprüfung; Interaktion später |
| Neue Ergebnisse | Zustandswechsel und zugängliche Rückmeldung besitzen explizite Zuordnung | Vertragsprüfung; Assistenztechnik später |
| Overlay und ScrollArea | Parameter, Ereignisse und Zuständigkeiten der Unterkomponente sind nachvollziehbar | Kompositionsprüfung; Scrollverhalten später |
| Begrenzte Liste, Abstand, Themes | Formale visuelle Regeln beziehen sich auf korrekte Teile und Tokens | Fachvalidator; Geometrie später |
| Fehlendes Ziel oder falscher Teil | Präzise Fehlermeldung statt unbemerktem Verweis | Statische Paketprüfung, falls verfügbar |
| Doppelte Instanzidentität oder verwaiste Beziehung | Kollision beziehungsweise ungültiges Ziel erkannt | Statische Paketprüfung, falls verfügbar |
| Falscher Parameter-/Payloadtyp | Bindung abgewiesen oder klar als ungeprüft gemeldet | Typ-/Semantikprüfung |
| Unvereinbarer Quellenstand oder unauflösbarer Zyklus | Auflösung scheitert nachvollziehbar | Resolverprüfung, falls verfügbar |
| Widersprüchliche Fokusregel | Beteiligte Regeln und führende Anforderungen sichtbar | Fachliche Konfliktprüfung |

Acht Pixel Abstand und fünf sichtbare Einträge bleiben illustrative Werte. Lade-, Fehler-, Abbruch- und Fokusverlustregeln sind noch festzulegen. Diese Tabelle definiert künftige Erwartungen; **kein Fall wurde hier ausgeführt oder als bestanden markiert**.

## 8. Prüfungen und Plattformen

Vier Nachweise sind auseinanderzuhalten: Originalschema/Originalwerkzeug je Domäne; Referenzauflösung; fachliche Konsistenz; tatsächliches Verhalten der Zielplattform. Ein bestandener erster Schritt beweist keinen der folgenden. Nicht formal ausdrückbare Anforderungen brauchen dokumentierte manuelle Prüfung.

**Vorschlag:** Einen gemeinsamen begrifflichen Kern mit ausdrücklich benannten Zielprofilen verbinden. Web-Semantik, DOM-IDs und CSS-Geometrie dürfen nicht als native Abbildung ausgegeben werden. Für Swift/SwiftUI und andere native Ziele sind eigene Semantik-, Fokus- und Layoutabbildungen zu recherchieren. Bilder und Figma-Darstellungen können einzelne Zustände zeigen; sie belegen keine interaktive Ausführung. Es gibt noch keine zugesagte Plattform-Supportmatrix.

## 9. Agentenablauf als spätere Arbeitsgrundlage

1. Quellenstände, Zuständigkeiten und vorhandene Teilbindungen lesen.
2. Änderung in der führenden Domäne beschreiben; betroffene Beziehungen auflisten.
3. Eigene Domänenprüfung und anschließend die betroffenen gemeinsamen Bindungen prüfen.
4. Unaufgelöste Ziele, Informationsverluste und Konflikte ausdrücklich melden.
5. Änderungen und Nachweise gemeinsam zur Übernahme bereitstellen; erst nach tatsächlicher Übernahme Aufgaben abhaken.

Die vier spezialisierten Skills bleiben ein späteres Ziel. Dieser Ablauf erstellt noch keine Skills und setzt keine bereits existierende gemeinsame Validierungsinfrastruktur voraus.

## 10. Nächste Schritte und Entscheidungstor

- [x] Integrationsproblem, Begriffe, Ownership-Vorschlag und Akzeptanzfälle dokumentarisch zusammenführen.
- [x] Ersten begrenzten [Abgleich der Referenzmechanismen](INTEGRATION-REVIEW.md) speichern; sechs Quellpfade erneut prüfen und offene Bindungen zuordnen. Keine vollständige Originalformatkette nachgewiesen.
- [x] Minimalen [dokumentarischen Referenzfall mit zwei Instanzen und ScrollArea](INTEGRATION-REVIEW.md#4-referenzfall-ohne-neue-formatsprache) ausarbeiten; offene Produktregeln sichtbar lassen.
- [ ] Anhand dieses Falls entscheiden, welche bestehenden Mechanismen genügen und welche Zusatzregeln tatsächlich nötig sind.
- [ ] Erst danach über ein Integrationsartefakt, Identitätssyntax und Resolver entscheiden.
- [ ] Bei gesondertem praktischem Auftrag Originalvalidatoren und positive/negative Verbindungen tatsächlich prüfen; Ergebnisse getrennt erfassen.

**Noch offen:** Formatwahl, vollständige Typabbildung, Versionierung/Migration, native Zielprofile, maschinelle Accessibility-Regeln, Grenze automatischer Konflikterkennung und produktiver Mindest-Reifegrad. Die bestehenden Detailvergleiche und verbleibenden U-Fragen werden durch diesen Entwurf nicht erledigt.

## Ausgeführter begrenzter Webreferenzfall

[21 Bedingungen](experiments/2026-10-25/four-domain/REPORT.md) belegen vier getrennte Dateien in Originalsprachen, explizite zusätzliche Instanz-/Bedeutungsbindung und gemessene eigene Popupanker/Begrenzung für A/B. Variable Zeilenhöhen unterscheiden geometrische Höhe von sichtbarer Zeilenzahl. Das Profil ist Forschungszusatz, keine beschlossene Produktarchitektur; dynamischer UX-/Hostlauf und native Abbildung bleiben offen. X01 ist für die vier konkret beteiligten Beiträge nun A.
