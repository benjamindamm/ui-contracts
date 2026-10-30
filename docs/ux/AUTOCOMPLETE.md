# Autocomplete · UX-Eignung und Abgrenzung

Status: fachliche Anforderungen und Projektentscheidungen aus dem Nutzergespräch vom 30. Oktober 2026. Kein empirisch validiertes allgemeines UX-Gesetz. Die Aussagen verfeinern das Auswahlmodell; sie ändern keine eingefrorene Komponentendefinition rückwirkend.

## Zweck: Schreiben unterstützen oder verbindlich auswählen?

Autocomplete kann das Ausfüllen erleichtern, indem es beim Schreiben passende Vorschläge anbietet und eine gewünschte Schreibweise übernimmt. **Schreibhilfe und Auswahl aus einer abgeschlossenen Wertemenge sind verschiedene Aufgaben.** Ein ähnliches Suchfeld bedeutet nicht, dass beide denselben Wertevertrag besitzen.

| Aufgabe | Geeignete Eigenschaft | Bedeutung unbekannter Eingaben |
| --- | --- | --- |
| Frei bearbeitbaren Text mit Vorschlägen erfassen | Autocomplete als optionale Schreibhilfe; übernommene Vorschläge bleiben editierbar | Darf zulässig sein. Keine Übereinstimmung mit dem Vorschlagsdienst beweist keine Ungültigkeit. |
| Genau einen festen Wert aus wenigen Einträgen wählen | Select mit stabilen Schlüsseln | Nur tatsächlich angebotene Werte übernehmen. |
| Genau einen festen Wert aus einer langen Liste wählen | Select mit separater Suche; Suchtext und ausgewählter Wert getrennt | Unbekannter Suchtext filtert auf keine Treffer, erzeugt aber keinen neuen Auswahlwert. |
| Feste Schlüssel über ein editierbares Vorschlagsfeld auswählen | Explizit darauf ausgelegte Autocomplete-Variante, wenn die Aufgabe das begründet | Mitgliedschaft muss die Komponente beim Übernehmen durchsetzen. Ein nachträglicher Formularvalidator allein genügt nicht. |

Die Länge allein entscheidet nicht. Wertevertrag, Editierbarkeit, Suchbedarf, tatsächliche Komponentenfähigkeiten und Projektpräferenzen müssen zusammenpassen. Eine konkrete Zahl wie „mehr als 15“ ist eine deklarierte Studienpolicy, keine universelle Grenze.

## Beispiel Adresse: Vorschläge sind keine vollständige Wahrheit

Nach fachlicher Vorgabe des Nutzers dient die Vervollständigung durch einen Kartendienst vor allem als Schreibhilfe. Nutzer sollen beispielsweise „Strasse“ oder „Str.“ schreiben bzw. einen übernommenen Vorschlag anpassen dürfen. Dass ein Dienst eine Straße nicht kennt, darf **allein** keine Ablehnung auslösen: Der Dienst kann unvollständig sein.

Das Beispiel illustriert den gewünschten Produktvertrag, keine Garantie der postalischen Zustellbarkeit jeder Abkürzung. Eine tatsächlich benötigte postalische Prüfung wäre ein gesonderter, begründeter Anwendungsfall mit eigenen Datenquellen und Fehlerregeln. Vorschlagsabgleich und fachliche Gültigkeit sind zu trennen.

Für diesen Schreibhilfe-Modus wären festzulegen: freier Text als führender Wert, optionale Vorschlagsübernahme, anschließende Editierbarkeit und Verhalten bei fehlendem/unerreichbarem Anbieter. Eine solche freie Variante ist im bisherigen example-Autocomplete **nicht** definiert. Ein Agent darf sie nicht allein aus dem Namen ableiten.

## Beispiel Ländervorwahl: feste Werte, separate Suche

Die Vorwahl wird aus den bereitgestellten Ländern ausgewählt. Bei drei Einträgen genügt im Studienfall ein Select. Bei vielen Einträgen soll Suche helfen, ohne den gewählten Wert selbst zu einem editierbaren Freitext zu machen. Ein Select mit Suche passt deshalb hier besser zur fachlichen Absicht als die Verlagerung dieser Begrenzung in eine zusätzliche Validierung eines Freitextfeldes.

Die Suchabfrage ist nur ein Hilfsmittel. Formularwert ist der vorhandene Länderschlüssel; gleiche Vorwahlen wie +1 dürfen unterschiedliche Länder nicht zusammenführen. Die im Beispiel gesetzte Reihenfolge priorisiert CH/DE/FR und ordnet den Rest numerisch nach Vorwahl. Das ist eine explizite Projektvorgabe und keine automatisch ermittelte geografische Plausibilität.

Die Zugehörigkeit zur Liste beweist weder die Gültigkeit noch die Erreichbarkeit der anschließend eingegebenen Telefonnummer. Diese Prüfung gehört, falls gefordert, zu einem separaten fachlichen Vertrag.

## Konsequenz für Agenten

Vor der Wahl ausdrücklich bestimmen:

1. Ist der führende Wert freier Text oder ein vorhandener Schlüssel?
2. Dürfen unbekannte Texte akzeptiert werden? Welche Quelle darf über Gültigkeit entscheiden?
3. Soll der ausgewählte Text bearbeitbar bleiben oder nur eine getrennte Suchabfrage?
4. Wie viele Einträge gibt es, wie sind sie geordnet und ist Suche erforderlich?
5. Welche tatsächlich definierten Varianten erfüllen das – ohne nachträglich neue Fähigkeiten zu erfinden?

Bei festen Werten im hier vereinbarten Projektprofil zuerst Select bzw. Select mit Suche prüfen. Autocomplete ist nicht pauschal ungeeignet: Die konkrete Variante und der fachliche Zweck führen. Fehlt die passende Variante, die Lücke benennen statt die nächstähnliche Komponente als optimale Wahl darzustellen. Fehlende entscheidende Angaben dürfen eine gezielte Rückfrage auslösen; bekannte Fakten müssen nicht erneut erfragt werden.

## Was die bisherige Studie tatsächlich belegt

[SELECTION-01](../research/studies/UX-RULES-01/studies/SELECTION-01/README.md) bot nur Select und ein auf vorhandene Ergebniskeys begrenztes Autocomplete an. Dessen Query ist editierbar; freie Texte werden jedoch nicht als neue Ergebniswerte bestätigt. Das ist **nicht** der oben beschriebene freie Adressmodus. Die damalige Wahl für 30 Einträge erfüllte die damalige Policy, beweist aber keine optimale Komponentenwahl bei vollständigerem Angebot.

[SELECTION-02](../research/studies/UX-RULES-01/studies/SELECTION-02/README.md) ergänzt eine separate Kandidatenrevision mit Select mit Suche und expliziten Merkmalen für Interaktionszweck, Suchoberfläche und unbekannte Eingaben. Die erste Studie wird nicht nachträglich auf die neue Erwartung umbewertet. Ein Agentenlauf testet die Anwendung unserer Vorgaben, keine tatsächliche Benutzerfreundlichkeit im Nutzertest.
