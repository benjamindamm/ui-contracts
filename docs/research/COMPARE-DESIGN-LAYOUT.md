**Aktueller Stand – 25. Oktober 2026:** 41 offene Nachweise (26 Integration, 15 weitere), 435 benannte Prüfbedingungen in 56 Gruppen. Vollständige Integration, Produkt-UI und Assistenztechnik sind weiterhin nicht nachgewiesen; statische HTML-Host-Fixtures wurden inzwischen im Browser geprüft. Historische Zahlen und „nicht ausgeführt“-Aussagen unten beziehen sich auf die jeweils benannte frühere Runde. Maßgeblich ist das [aktuelle Register](OPEN-FIELDS.md).

# Detailvergleich: DESIGN.md und deklarative Layoutmodelle

**Aktuelle Fortschreibung nach diesem dokumentarischen Stand:** [49 E3-Proben](experiments/2026-10-24/REPORT.md) sind inzwischen ausgeführt. CEM I02 ist nun A/C421; aktuell 65 U (41 Integration, 24 weitere). Frühere Aussagen „keine Ausführung“ und damalige Zählungen unten dokumentieren den Entstehungsstand. Keine vollständige UI-/AT-/Integrationsprüfung.


Stand: 24. Oktober 2026. **Dokumentarischer Vergleich, keine gerenderte Oberfläche und keine Parser-/Browserprüfung.** Gemeint ist Google `design.md` am gespeicherten Alpha-Snapshot, nicht ein beliebiges Markdown-Designdokument. CSS wird als Web-Layoutbeitrag untersucht; die Modulstände und eine Zusatzquelle zur Modusauswahl werden ausdrücklich getrennt geführt.

## Ergebnis

DESIGN.md liefert strukturierte Designwerte und menschenlesbaren Gestaltungskontext. Die erneut gelesene Spezifikation beschreibt bei Layout vor allem Abstände und bei Komponenten bekannte Stylefelder. Das belegt noch keinen gemeinsamen formalen Vertrag für „dieses Popup relativ zu jenem Input, mit begrenzter Höhe und eigenem Scrollport“.

CSS Anchor Positioning und Overflow beschreiben konkrete Geometrie und Überlauf. DTCG liefert Werte und Auflösung, Panda einen CSS-orientierten Erzeugungs-/Bindungspfad, UXSpec eigene Layoutprimitiven mit einem vorhandenen Web-Größenmapper. Die Beiträge ergänzen sich, besitzen aber unterschiedliche Zielobjekte und Prüfgrenzen. Eine Datei oder Sprache wird hier nicht ausgewählt.

Quellen: [S42](SOURCES.md), [S51](SOURCES.md#s51), [S56](SOURCES.md#s56), [S59](SOURCES.md#s59), [S60](SOURCES.md#s60); gezielt erneut gelesen [S63](SOURCES.md#s63), neues CSS-Zusatzmodul [S65](SOURCES.md#s65). [C417](CLAIMS.md#c417) hält die eng begrenzte Schlussfolgerung fest.

## Derselbe Akzeptanzfall für alle Beiträge – Vorschlag

Zwei Autocomplete-Instanzen A und B verwenden dieselbe Definition. Jedes Popup gehört zu seinem eigenen Input. Vorgeschlagene Produktparameter: 8 px Abstand, maximal fünf vollständig sichtbare gleich hohe Zeilen, vertikales Scrollen bei weiteren Treffern, Light-/Dark-Auswahl. Eine ScrollArea kann als eigene Unterkomponente auftreten. Die Zahlen und das konkrete Muster sind Prüfparameter, keine universellen Standardpflichten.

Für variable Zeilenhöhen wird die Höhe der ersten fünf Zeilen einschließlich relevanter Abstände benötigt. Fünfmal Textzeilenhöhe ist dafür kein allgemeiner Ersatz. Auf verfügbarem Bildschirmraum kann zusätzlich eine kleinere Maximalhöhe erforderlich sein; die Priorität zwischen fünf Zeilen, Platz und Mindestnutzbarkeit ist eine Produktregel.

## Feldweiser Vergleich

| Information | DESIGN.md | DTCG / Panda | UXSpec / uSpec | CSS-Beitrag |
| --- | --- | --- | --- | --- |
| Abstand als Wert | Strukturierter spacing-Wert möglich | DTCG dimension mit Einheit; Panda Token-/Styleverwendung | UXSpec Größen-/Stylewerte; uSpec extrahierte Maße | Längenwert im Layout verwendbar |
| Ziel der Relation | Kein hinreichender Originalnachweis für benannten Inputanker in der erneut gelesenen Spezifikation | Token allein kennt kein UI-Ziel; Panda braucht konkrete CSS-/Patternbindung | UXSpec layer überlagert lokal; uSpec `_anchor` bezeichnet Figma-Quell-/Messziel | anchor-name / position-anchor verbinden konkrete Boxen |
| Richtung und Position | Prosa oder bekannte Stylefelder ergeben noch keine festgelegte relative Ankersprache | Ausgabe-/Layoutprofil erforderlich | Lokaler Layerwrapper ist kein allgemeines Input→Popup-Modell | position-area bzw. anchor()-bezogene Insets |
| Maximale Höhe | height/size-Felder sind nicht automatisch eine formale dynamische Flächenregel | Dimension liefert Wert; erzeugtes CSS liefert Zielbedeutung | UXSpec-Webmapper setzt maxHeight/maxWidth; uSpec-Messdaten sind keine Laufzeitregel | max-height/max-block-size; verfügbare Fläche gesondert |
| Überlauf | Kein vollständiger Scrollcontainervertrag belegt | Panda kann CSS erzeugen; Token selbst nicht | Gelesene UXSpec-Container reichen keine formale overflow-Achse durch; uSpec-Basispfad extrahiert clipsContent | overflow-x/y und Scrollcontainersemantik |
| Modusauswahl | Strukturierte Theme-/Designwerte nur mit tatsächlichen Modellregeln bewerten | DTCG Resolver und Panda-Bedingungen besitzen eigene Auflösung | Eigenes Visual-/Rendererprofil prüfen | Zusätzlich Media Queries 5: prefers-color-scheme; nicht aus Anchor/Overflow abgeleitet |
| Zweite Instanz | Komponentenname allein trennt keine Instanzen | Tokenname ist kein Instanzname | Maschinen-, Layer- und Figma-IDs haben unterschiedliche Namensräume | anchor-scope begrenzt Ankersuche im Elementteilbaum |
| Semantik und Fokus | Kein Ersatz für Behavior/A11y | Kein Ersatz durch Token-/Styleauflösung | Zusätzliche Bindungen nötig | Visuelle Lage erzeugt keine passende ARIA-Beziehung |
| Native Ziele | Keine nachgewiesene automatische Übertragung | Wert-/Propertyadapter erforderlich | Native Interpreter-/Rendererzusagen gesondert | CSS-Websemantik ist keine automatische SwiftUI-/andere native Layoutsemantik |

„Nicht belegt“ ist auf Quellen und Kandidatenrolle begrenzt. Insbesondere werden weder sämtliche Editorfunktionen noch beliebige CSS-Erweiterungen als geprüft ausgegeben.

## Illustrativer CSS-Entwurf für den begrenzten Webfall

Eigener Prüfvorschlag, **nicht ausgeführt**. Er setzt zwei Elementteilbäume voraus, in denen Input und Popup jeweils innerhalb derselben `.autocomplete` liegen; das Popup ist ein nachfolgendes Geschwister des Inputs. Ein Portal außerhalb dieses Teilbaums wäre eine andere Bindung und ist hier nicht abgedeckt. Schreibmodus, physische Unterkante und einheitliche Zeilenhöhe sind bewusst eingeschränkte Annahmen.

```css
.autocomplete {
  anchor-scope: --input;
  --gap: 8px;
  --row-height: 32px;
}
.autocomplete > input {
  anchor-name: --input;
}
.autocomplete > .popup {
  position: absolute;
  position-anchor: --input;
  top: calc(anchor(bottom) + var(--gap));
  left: anchor(left);
  width: anchor-size(width);
  max-height: calc(5 * var(--row-height));
  overflow-y: auto;
}
@media (prefers-color-scheme: dark) {
  .autocomplete { --surface: #171717; }
}
@media (prefers-color-scheme: light) {
  .autocomplete { --surface: #ffffff; }
}
.autocomplete > .popup { background: var(--surface); }
```

Dieser Ausschnitt beschreibt weder vollständiges Boxmodell noch Border/Padding/Zeilenabstände, Viewportausweichregeln oder zugängliche Bedienung. Die Fünf-Zeilen-Erwartung gilt nur, wenn die effektive Zeilenhöhe tatsächlich dem Parameter entspricht und weitere Boxanteile berücksichtigt werden. Auch eine Browserunterstützung genau der gespeicherten Draftkombination wird daraus nicht abgeleitet.

Das geprüfte Anchor-Modul lässt gleiche Ankernamen zu. Ohne passende Sichtbarkeit/Scoping kann eine andere Box zum Ziel werden; der Parser muss einen solchen fachlichen Fehler nicht zurückweisen. `anchor-scope` besitzt eine konkrete Teilbaumsemantik und wirkt nicht auf implizite Anker. Ein Portal oder Shadow-Tree-Wechsel muss daher eigens untersucht werden. [S56](SOURCES.md#s56), erneute Abschnitte 2.1/2.2 in [S63](SOURCES.md#s63).

Für Modusauswahl wird der Umfang ausdrücklich um **Media Queries Level 5, Working Draft vom 19. Februar 2026, §12.5** erweitert. `light` umfasst dort auch fehlende aktive Präferenz; `dark` bezeichnet die dunkle Präferenz. Das definiert einen Auswahlmechanismus für bedingte Werte, keine Produktregel für einen manuellen Theme-Schalter und keine native Themeabbildung. CSS V03 wird ausschließlich für diesen Zusatzbeitrag D. [C412](CLAIMS.md#c412)

## Was DESIGN.md im selben Fall festhalten kann

Ein spacing-Wert und die gewünschte Gestaltung können in DESIGN.md stehen. Eine Beschreibung wie „Popup unter dem Eingabefeld, 8 px Abstand, bis zu fünf Zeilen, dann scrollen“ bleibt ohne zusätzliche festgelegte Felder/Referenzsemantik eine Arbeitsanweisung an Autor oder Agent. Sie ist keine durch das Originalformat bereits bewiesene Anker-/Scrollbindung.

Die erneut gelesenen bekannten Komponentenfelder umfassen etwa background, text, typography, rounded, padding, size, height und width. Die Offenheit von Maps erlaubt zusätzliche Texte; sie verleiht einem frei erfundenen `anchorTarget` jedoch keine originale Ausführungs- oder Prüfsemantik. Ein neues Layoutprofil müsste ausdrücklich als Ergänzung geführt werden. Ebenso sind Variantennamen mit „hover“ keine automatische Verknüpfung zu einer externen Behavior-Maschine.

## Bestehende Beiträge erhalten – Integrationsvorschlag

| Führende Information | Unveränderter möglicher Beitrag | Explizit zusätzliche Bindung |
| --- | --- | --- |
| Typisierter Abstand | DTCG dimension oder gewählter Visualwert | Einheiten erhalten, konkrete CSS-/native Zielproperty bestimmen |
| Gestaltungskontext | DESIGN.md | Normative Werte von Prosa und Agenteninterpretation unterscheiden |
| Relative Geometrie | CSS oder anderes ausdrücklich gewähltes Layoutmodell | Fachlichen Input/Popupteil auf reale Boxen derselben Instanz abbilden |
| Sichtbare Höhe | Layout-/Produktprofil | Zeilenmessung, Boxanteile und verfügbare Fläche bestimmen |
| Scrollfunktion | Layout-/ScrollArea-Modell | Achse, Scrollport, Childkontext und „aktive Option sichtbar machen“ zuordnen |
| Öffnen/Schließen und Bestätigung | Behavior | Sichtbarkeit/Varianten und öffentliche Ausgaben binden |
| Zugängliche Beziehung | ARIA-/Plattformprofil | Tatsächliche Input-/Listbox-/Optionselemente, Fokus und Ansagen zuordnen |

Die Tabelle ist ein Vorschlag. Sie wählt keinen Stapel und erzeugt keine vermeintlich originale Integrationssprache. Aus DTCG nach UXSpec ist zudem ein gelesener Pfad bekannt, der value/unit auf eine Zahl reduziert. Jede neue Bindung muss den Einheitenverlust ausdrücklich verhindern. [C395](CLAIMS.md#c395)

## Vorgeschlagene Prüfmatrix

| Fall | Erwartung an die spätere Prüfung | Was reine Syntaxprüfung nicht belegt |
| --- | --- | --- |
| A und B geöffnet | Jedes Popup folgt nur seinem Input | Gleicher Ankername kann syntaktisch gültig und fachlich falsch gebunden sein |
| Ein Input fehlt | Klare Produktdiagnose oder ausdrücklich definierter Fallback | CSS-Fehlerbehandlung ist nicht automatisch eine Paketfehlermeldung |
| Andere Einheit | Abstand bleibt bedeutungsgleich oder Umrechnung wird dokumentiert | Eine einheitenlose exportierte Zahl ist nicht gleich dem Originaltoken |
| Sechs gleich hohe Treffer | Fünf vollständige Zeilen, restlicher Inhalt scrollbar | max-height allein erzwingt weder Zeilenzahl noch passendes Scrollverhalten |
| Unterschiedliche Zeilenhöhen | Vereinbarte Höhen-/Messregel wird angewandt | Fünfmal Standardhöhe reicht nicht |
| Viewport zu klein | Vereinbarte Ausweich-/Höhenpriorität | Ein erfolgreicher normaler Screenshot reicht nicht |
| Popup im Portal | Explizite Ziel-/Scopebindung | Lokales anchor-scope kann das externe Popup ausschließen |
| Tastaturnavigation | Aktive Option wird sichtbar, Fokus-/ARIA-Regeln bleiben konsistent | Scrollbarkeit bedeutet keine vollständige Tastatursteuerung |
| Dark / Light / keine aktive Präferenz | Dokumentierte Auswahl; Produktüberschreibung separat | Eine Farbe namens dark definiert keine Auflösung |
| Natives Ziel | Eigener Renderer-/Layoutbeleg | Erfolgreiches Web-CSS beweist keine native Semantik |

Keiner dieser Versuche ist ausgeführt. Für spätere Tests sind Browser-/Rendererstand, genaue Module, Eingabe und Beobachtung festzuhalten. Der dokumentarische Detailvergleich ist damit ausgearbeitet; eine technische Layoutintegration und plattformübergreifende Gleichheit bleiben nachzuweisen.
