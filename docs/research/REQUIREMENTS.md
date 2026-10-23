# Anforderungskatalog

Stand: 23. Oktober 2026. Die Kriterien sind vor der nachfolgenden Zellenbewertung definiert. Beispielwerte sind keine allgemeinen Produktpflichten.

## Herkunft

**O** bezeichnet die Nachrichtenposition im vollständig als Text gelesenen [Originalgespräch](https://chatgpt.com/share/6adba3c9-accc-83ed-adbf-a78f5a880760): 71 Nachrichten, 36 Nutzerbeiträge. Die Nummerierung entspricht `conversation-turn-N` der öffentlichen Seite zum Abrufzeitpunkt. Nutzeräußerungen und Assistentenvorschläge bleiben unterscheidbar.

- O11: Agentenlesbarer Contract mit verschiedenen Ausgaben; OpenPencil als gegenwärtiges Werkzeug.
- O13: Nutzer bestätigt die vier Domänen; O15 verlangt vorhandene Standards statt sofort eigenem Format.
- O24/O26: Konzeptionsphase, formale visuelle Beschreibung, Tailwind als verständliche Analogie.
- O28/O30: Designsystem und präzise Gestaltung; keine Subpixelgleichheit als Ziel.
- O32: Tokens, Varianten und Dark Mode ausdrücklich bestätigt.
- O34: Präferenz, Googles Kandidaten genauer zu untersuchen; keine Eignungsgarantie.
- O36/O38: Konkretes UX-Beispiel mit relativer Position, Begrenzung, Scrollen, Navigation, Aktualisierung und Ergebnisrückmeldung.
- O40/O42: Weitere Vorarbeiten recherchieren, besonders agentische Formate; Requirements as Code als Analogie.
- O44/O46: UXSpec-Versuch angefragt; bloße visuelle Freitextbeschreibung ausdrücklich als unzureichend kritisiert.
- O48: Kombination von Substandards erlaubt; bestehende Entwicklungen nutzen und eigenes langfristiges Umbau-/Pflegerisiko reduzieren.
- O50: Strikte Abgrenzung wegen Agentenwidersprüchen; abstrakte Schnittstellen über Swift, TypeScript, Angular und React hinweg.
- O51/O53/O55/O57/O59: Vom Assistenten konkretisierte Ownership-, Referenz- und Prüfmodelle; Nutzerbestätigungen in O52/O54/O56/O58/O60. Konkrete Syntax und behauptete Fähigkeiten sind dadurch nicht technisch verifiziert.
- O59/O60: Bestätigte Detailvergleiche DESIGN.md gegen deklarative Layoutmodelle und UXSpec gegen SCXML.

**P01:** Spätere Nutzerpräzisierung im Voice-Chat: Allgemeines Projektziel; Anforderungen als Matrixzeilen und Kandidaten als Spalten; Beispielkomponente nur Illustration.

**P02:** Anschließende Präzisierung, über denselben koordinierenden Chat übermittelt: gemeinsames Contract-Paket zunächst vor Rendererwahl; vier getrennte Dateien bevorzugt; JSON/YAML mögliche Serialisierungen; stabile element- und domänenübergreifende Referenzen, wiederverwendbare Komponenten, externe/versionierte Referenzen und Validierung. URN ist eine Idee, keine Technikentscheidung. P02 wird als übermittelte Präzisierung dokumentiert; ihre Nachricht ist nicht Teil des öffentlichen Originals.

## Operationalisierte Kriterien

| ID | Domäne | Anforderung | Woran eine Abdeckung erkennbar wäre | Herkunft |
| --- | --- | --- | --- | --- |
| G01 | Grundlagen | Maschinenlesbare Beschreibung | Dokumentierte Datensyntax für Komponenten oder den fachlichen Teilbeitrag; alleinige natürlichsprachliche Beschreibung genügt nicht. | O11, O15, O24, O42 |
| G02 | Grundlagen | Sprachneutrale fachliche Semantik | Der bewertete Kern benötigt keine React-/JavaScript-Funktionen. Gleiche Serialisierung allein genügt nicht; konkrete Zieladapter sind separat zu prüfen. | O11, O50 |
| I01 | Interface | Öffentliche Eigenschaften mit Typangaben | Benannte Properties mit ausdrücklichen Typmetadaten; Durchsetzung komplexer Typen wird separat geprüft. | O50; bestätigter Vorschlag O51–O56 |
| I02 | Interface | Öffentliche Ereignisse mit Payload | Öffentlicher Eventname und strukturierte Payload-Felder sind im Modell zugeordnet, getrennt vom Auslösezeitpunkt. Interne Maschinenereignisse allein genügen nicht. | O50; O51–O56 |
| I03 | Interface | Benannte Komponentenbestandteile | Anatomie oder Teile sind strukturiert benannt, sodass andere Beschreibungen auf sie bezogen werden können. Noch kein Nachweis instanzstabiler IDs. | O50; O51–O56 |
| V01 | Visual | Typisierte Designwerte | Farben, Dimensionen oder Typografie sind als strukturierte Werte mit definierter Bedeutung beschreibbar. | O30, O32, O46 |
| V02 | Visual | Visuelle Zustandsvarianten | Benannte visuelle Varianten besitzen strukturierte Styles oder Tokenreferenzen. Zuordnung zu einer externen UX-Maschine bleibt X03. | O32, O46; O55 |
| V03 | Visual | Themes und Dark Mode | Modi besitzen dokumentierte Auswahl-/Auflösungsregeln für unterschiedliche Werte; nur ein Farbname dark genügt nicht. | O32 |
| V04 | Visual | Formale relative Geometrie | Anker/Ziel, Richtung/Position und Abstand sind definierte Eigenschaften mit Semantik. Beispiel: Overlay relativ zum Input; acht Pixel sind nur ein Testwert. | O30, O36, O46 |
| V05 | Visual | Formale Flächenbegrenzung | Maximale Fläche oder Höhe besitzt eine definierte geometrische Bedeutung. Beispiel: Höhe für fünf sichtbare Zeilen; variable Zeilenhöhen zusätzlich prüfen. | O38, O46 |
| V06 | Visual | Overflow und Scrollen | Verhalten überlaufender Inhalte ist ausdrücklich und formal beschrieben; eine sichtbare Zeilenzahl wird daraus nicht allein abgeleitet. | O38, O46 |
| B01 | Behavior | Zustände und Ereignisübergänge | Benannte Zustände, Initialzustand und durch Ereignisse bestimmte Übergangsziele sind beschrieben. | O38; O51–O56 |
| B02 | Behavior | Guards und Aktionen | Bedingung und Aktion haben definierte Auswertungs-/Ausführungssemantik; freie Funktionsnamen allein reichen nicht. | O48; O55, O59 |
| B03 | Behavior | Ereignis- und Kontextdaten | Zustandsdaten und Ereignisdaten können in der Logik ausdrücklich verarbeitet werden. Kein Ersatz für I02. | O38; O55 |
| B04 | Behavior | Bindung von Eingaben an UX-Aktionen | Tastatur/Fokus/Eingabe lassen sich ausdrücklich auf Aktionen oder Maschinenereignisse abbilden. | O36, O38 |
| A01 | Accessibility | Rollen, Namen und Beziehungen | Zugängliche Semantik hat definierte Begriffe und Zielbeziehungen. Metadatencontainer allein beweist keine Konformität. | O38; O51 |
| A02 | Accessibility | Fokus- und Tastaturanforderungen | Ein referenzierbares Interaktionsmuster beschreibt Bedienung und Fokus. Ausführbare formale Prüfung zusätzlich erforderlich. | O38; O51–O56 |
| A03 | Accessibility | Dynamische Rückmeldungen | Eine definierte Semantik für zugängliche Aktualisierungen ist vorhanden; produktbezogene Auslöser und Inhalte bleiben explizit. | O38 |
| X01 | Integration | Vier unabhängig beschreibbare Domänen | Teilmodelle lassen sich ohne erzwungene fachfremde Definitionen führen; gemeinsame Dateien sind keine Voraussetzung. | O50; spätere Präzisierung P02 |
| X02 | Integration | Stabile Elementidentität | Explizite Elementidentifikatoren oder Bindungs-IDs sind vorhanden. Stabilität bei mehreren Instanzen und Änderungen ist ein weiterer Nachweis. URN optional. | O51–O59; P02 |
| X03 | Integration | Domänenübergreifende Referenzen | Ein Ziel aus einer separat beschriebenen Domäne wird eindeutig adressiert und semantisch zugeordnet; interne Tokenreferenzen allein genügen nicht. | O50; O51–O59; P02 |
| X04 | Integration | Wiederverwendbare Komponenteninstanzen | Definition und Verwendung sind getrennt; referenzierte Komponente wird mit eigenem Instanzkontext/Parametern wiederverwendet. Beispiel: Overlay verwendet ScrollArea. | P02; Vorläufer Elementreferenzen O59 |
| X05 | Integration | Externe versionierte Abhängigkeiten | Externe Komponenten-/Teilmodellreferenz enthält eine reproduzierbar gebundene Version und definierte Auflösung. Ein Dateipfad oder Versionsfeld allein genügt nicht. | O48; O51–O59; P02 |
| X06 | Integration | Eigene Schemavalidatoren erhalten | Separates Domänenartefakt kann gegen sein Originalschema geprüft werden; keine stille Erweiterung desselben Formats. | O59; P02 |
| X07 | Integration | Referenz- und Konfliktprüfung des Pakets | Fehlende/falsche Ziele, Instanzkollisionen und widersprüchliche Anforderungen verschiedener Domänen werden abgewiesen. Interne Tokenprüfung genügt nicht. | O50; O51–O59; P02 |
| X08 | Integration | Eindeutige führende Quelle | Ownership und Vorrang sind je Information dokumentiert, Änderungen zwischen Originalformaten und Integrationsschicht nachvollziehbar. | O48, O50; O51–O59 |

## Auslegung der Beispiele

Eine Komponente kann aus separat identifizierten Teilen bestehen, die zugleich eigenständige Komponenten verwenden. Ein Overlay könnte eine ScrollArea instanziieren. Dafür sind mindestens Definition, Instanzidentität, erlaubte Parameter, Ereignisbindung und Zuständigkeit für Fokus/Scrollen zu unterscheiden. Eine Tokenreferenz löst nur einen Wert auf und ist kein Ersatz für diese Komposition.

Das ursprüngliche Autocomplete ist ein anschaulicher Fall, kein Projektprodukt. Eine andere Komponente darf dieselben generischen Kriterien mit anderen Szenarien prüfen. Acht Pixel und fünf sichtbare Einträge sind Testdaten für V04/V05/V06. Enter/Escape und sieben Ergebnisse wurden im bestätigten Arbeitsvorschlag ergänzt; nicht jede Komponente muss diese Interaktionen besitzen.

Noch offene Auslegungen: Granularität der Typen, Verhalten bei Versionskonflikten, Zyklusregeln, Mehrfachinstanzen, Namensräume, genaue Accessibility-Zielplattformen und Anforderungen an deterministische Ausgabe. Diese müssen vor konkreten Konformitätsversuchen festgelegt werden.
