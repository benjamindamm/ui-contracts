# Konkrete Feldbindungen und verbleibende Integrationsfragen

Stand: 24. Oktober 2026. Fortsetzung des [Integrationsabgleichs](INTEGRATION-REVIEW.md). **Dokumentarische Feldprüfung; keine Auswahl eines Formatstapels, keine erzeugten kompatiblen Contractdateien und keine ausgeführten Validatoren.** Die hier nebeneinander betrachteten Kandidaten dienen dazu, konkrete Bindungsprobleme sichtbar zu machen.

## 1. Verlässliche Zählung

Die Matrix enthält weiterhin **73 U-Zellen**: **45 in X01–X08**, **28 in anderen Anforderungen**. Das sind offene Nachweise je Kandidat und Anforderung, keine Zahl fehlender Komponenten oder unabhängiger Probleme. Alle 16 Kandidaten-Durchgänge sind abgeschlossen. Eine zusätzliche Quellprüfung hebt eine U-Zelle nicht automatisch auf.

Das vollständige [Register der offenen Felder](OPEN-FIELDS.md) hält jede U-Zelle mit Befund, Frage, Priorität und nächstem Schritt fest. Es wurde aus dem gespeicherten Prüfregister abgeleitet. Triage bedeutet Einordnung, keine abgeschlossene Nachprüfung aller 73 Fragen.

## 2. Originalfelder und notwendige Bindung

Die Feldpfade sind beschreibende Suchpfade mit Platzhaltern, keine allgemeine Referenzsyntax. Neue fachliche Namen für den Beispielcontract sind Vorschläge. Die Nachweise und Quellen dieser Runde stehen in [C394–C396](CLAIMS.md#c394) und [S58](SOURCES.md#s58).

| Bindungsfrage | Konkrete Originalfelder oder Regeln | Was sich daraus ergibt | Noch erforderliche Zuordnung |
| --- | --- | --- | --- |
| Welche Komponentendefinition? | CEM `modules[].path`, `declarations[].name`, `Reference.name/package/module` | Ein adressierbarer Deklarationsbezug | Gewählte Deklaration auf neutrale Definition abbilden; Paketstand separat binden |
| Welche Instanz? | UXSpec `$machine.id`; Element `name/testId`; Ark explizite IDs und eigener Maschinenkontext | Unterschiedliche ID-Arten mit eigenem Geltungsbereich | Definition, Actor-/Maschineninstanz, fachlicher Teil und DOM-ID ausdrücklich unterscheiden |
| Welcher Teil? | CEM `cssParts[].name`, `slots[].name`; UXSpec `$elements` | Benannte Stylingteile, Inhaltsplätze beziehungsweise Elementdefinitionen | Ein CSS-Part oder Slot ist nicht automatisch ein fokussierbares Element oder eine untergeordnete Komponenteninstanz |
| Welcher öffentliche Wert? | CEM `members[].type.text` und optionale Typreferenzen; UXSpec `$context.<Feld>.type` | Typbeschreibung auf verschiedenen Ebenen | Eingabe/Output, zulässige Werte, Optionalität, Default und Quelle des aktuellen Wertes binden |
| Welches Ereignis? | CEM `events[].name/type`; UXSpec `$events.<Ereignis>.payload`, `$actions` mit `kind: emit` | Öffentlicher Eventobjekttyp gegenüber lokalen Payloadfeldern und Auslösung | Öffentliches Ereignis, interner Auslöser und Payloadprojektion getrennt benennen |
| Welche visuelle Dimension? | DTCG `$type: dimension`, `$value.value/unit` | Typisierter Wert mit Einheit | Zielteil, Eigenschaft und Verwendung des Wertes festlegen; Einheit über Adapter erhalten |
| Welche Darstellung folgt welchem Zustand? | UXSpec `$machine.states`; Visualvariante im jeweils untersuchten visuellen Modell | Zwei getrennte Definitionsorte | Explizite Zustands-/Variantenbindung; keine Gleichheit durch identischen String voraussetzen |
| Welches zugängliche Ziel? | WAI-ARIA `aria-controls`, `aria-activedescendant`, Rollen und Eigentumsbedingungen | Web-Beziehung zwischen tatsächlichen Elementen | Fachlichen Teil auf reales Element derselben Instanz abbilden und zulässige Relation prüfen |
| Welche Unterkomponente? | UXSpec `invoke.src/id/input/onDone`; Ark eigener ScrollArea-Kontext | Maschinenkomposition beziehungsweise konkrete Web-Kontexte | Definition, Child-Instanz, UI-Anatomie, Eingaben, Ereignisse und Lebenszyklus gemeinsam bestimmen |

## 3. Konkrete Kette für Auswahl und Payload

**Vorgeschlagener Arbeitsfall:** Eine bestätigte Auswahl liefert einen einfachen fachlichen Schlüssel als String. Der tatsächliche öffentliche Ereignisname und die Zulässigkeit freier Texteingabe bleiben Produktentscheidungen.

1. Die technische Schnittstelle beschreibt das öffentliche Auswahlereignis und seinen Payload. Bei CEM ist `events[].type` der Typ des **gesamten Eventobjekts**. Ein Typtext allein ist noch kein gemeinsam validierter Payloadbaum.
2. Behavior unterscheidet navigierte Option und bestätigten Produktwert. UXSpec kann deklarierte Payloadfelder und eine Emit-Aktion ausdrücken. Die Kompatibilität mit dem CEM-Typ muss gesondert geprüft werden; ein internes `$events`-Ereignis wird nicht durch seinen Namen automatisch öffentlich.
3. Eine Bindung legt fest, welcher Kontextwert in welches öffentliche Payloadfeld gelangt. Ob ein Webadapter ein `CustomEvent` mit `detail` verwendet, ist eine konkrete Adapterentscheidung und keine allgemeine UXSpec-/CEM-Konvention.
4. Die Produktinstanz bestimmt, zu welcher Suche die Auswahl gehört. Der gleiche Definitionseventname kann in A und B vorkommen, ohne dass die Instanzen identisch sind.
5. Accessibility vermittelt den relevanten Zustand innerhalb desselben Instanzkontexts. Sie bestimmt nicht unabhängig einen zweiten Bestätigungszeitpunkt.

**Offener Typfall:** UXSpecs `contextField` führt primitive Typnamen einschließlich `object/array`, aber in dieser Definition keinen rekursiven Property-/Itemvertrag. Beliebige komplexe CEM-Typtexte lassen sich daher nicht ohne zusätzlich definierte Typabbildung als vollständig kompatibel ausgeben. Der einfache Stringfall begrenzt die spätere Prüfung; er löst die allgemeine Typfrage nicht. [C394](CLAIMS.md#c394)

## 4. Konkrete Kette für Werte und Einheiten

DTCG beschreibt eine Dimension durch Zahl und Einheit. Im erneut gelesenen UXSpec-Resolver reduziert ein bestimmter Auflösungspfad ein Objekt, das ausschließlich numerisches `value` und String-`unit` enthält, auf die Zahl. Das ist ein konkretes Informationsverlustrisiko bei einer entsprechenden Tokenintegration. Es wurde weder eine fertige Importkette noch ein Runtimefehler ausgeführt. Ein eigenständiges DTCG-Dokument wird außerdem nicht schon deshalb zu einem UXSpec-Import, weil beide `$value` verwenden. [C395](CLAIMS.md#c395)

**Vorgeschlagene Konsequenz:** Visuelle Originalwerte verbleiben in ihrer führenden Quelle. Eine Bindung muss Quelle, Zielproperty und Einheit beziehungsweise eine explizite Umrechnung erkennen lassen. Ein Adapter darf aus `rem` keinen einheitenlosen Wert machen und anschließend Gleichwertigkeit behaupten. DTCGs Hinweise für Plattformübersetzung ersetzen keinen Nachweis unseres nativen Zielprofils.

Der Abstand zwischen Eingabe und Popup benötigt zusätzlich ein relatives Ziel und Geometriesemantik. Ein gültiger Dimensionstoken allein definiert weder Anker noch Richtung, verfügbare Höhe oder Scrollport. Diese Felder bleiben Teil des bestätigten Layoutvergleichs.

## 5. Konkrete Kette für Fokus, Auswahl und Scrollen

Für den vorgeschlagenen editierbaren Webfall mit Listbox-Popup gilt als zu prüfende Abbildung:

| Bedeutung | Bindung im vorgeschlagenen Profil | Prüfbedarf |
| --- | --- | --- |
| Eingabe | Das Element mit passender Combobox-Semantik und tatsächlichem DOM-Fokus | Fachlicher Input und gerendertes Element stimmen überein |
| Popupziel | `aria-controls` verweist auf das semantisch passende Popup, hier die Listbox | Nicht versehentlich auf einen bloßen Overlay-/Scrollwrapper zeigen |
| Aktive Option | `aria-activedescendant` verweist auf die tatsächlich aktive Option im zulässigen Beziehungsbereich | Existenz, Instanz, Rolle und Eigentums-/Kontrollbedingungen prüfen |
| Zugänglich gemeldete Auswahl | Das gewählte APG-Muster berücksichtigt `aria-selected` und Auswahlfolge im Popup | Nicht pauschal behaupten, jede Navigation sei ohne Auswahlsemantik |
| Bestätigter Produktwert | Behavior legt Übernahme und öffentlichen Eventzeitpunkt fest | Von aktueller Popupauswahl getrennt beschreiben |
| Sichtbare aktive Option | Gewählte Scrollfunktion macht das aktive Element sichtbar | Zuständigkeit zwischen Combobox und ScrollArea prüfen |

WAI-ARIA definiert die zulässigen Beziehungen für aktive Nachfahren; die bloße Existenz einer Ziel-ID genügt nicht. Das APG-Muster beschreibt Fokus und Popupauswahl. **Aktive Option, zugänglich gemeldete Auswahl und endgültig bestätigter Produktwert sind deshalb als drei Bedeutungen zu behandeln.** Je Produktvariante können sie zusammenfallen; das muss ausdrücklich festgelegt werden. [C396](CLAIMS.md#c396)

Für Suche A ist eine formal existente Option in Suche B weiterhin das falsche fachliche Ziel. Ein zusätzlicher Instanzbezug ist daher als Integrationsregel vorgeschlagen. DOM-/Portalstruktur und die Gleichheit oder Trennung von Listbox und ScrollArea-Viewport bleiben konkret zu entscheiden.

## 6. Alle Integrationsfelder im Abgleich

| Feld | Noch offene U-Zellen | Befundstand | Was die Frage tatsächlich schließen würde |
| --- | ---: | --- | --- |
| X01 – Vier unabhängige Domänen | 16 | Getrennte Verantwortung bestätigt; vollständige Originalformatkette unbewiesen | Für ein begrenztes Paket alle vier führenden Artefakte, Bindungen und Prüfgrenzen konkret zeigen |
| X02 – Identität | 0 | Alle Kandidaten bereits eingeordnet; positive Teilbeiträge sind nicht gleichbedeutend mit Paketidentität | Definition/Instanz/Teil/DOM-ID für den Referenzfall nachvollziehbar zuordnen |
| X03 – Gemeinsame semantische Referenzen | 8 | Zielarten und konkrete Feldgrenzen präzisiert | Bestehende Resolver mit externen Originalzielen und dokumentierter Bedeutung nachweisen oder erforderliche Zusatzbindung benennen |
| X04 – Eigenständige Unterkomponenten | 4 | Definition, Verwendung und Maschinenkontext unterschieden | ScrollArea mit eigenem Kontext und reproduzierbarer Definition vollständig binden; Feldexistenz allein genügt nicht |
| X05 – Externe Versionen | 1 | Die eine U-Zelle betrifft OpenPencil; andere Bewertungen sind bereits vorhanden | Tatsächlichen Import-/Updatepfad und unveränderliche Bindung nachweisen; Format- und Paketversion unterscheiden |
| X06 – Originalprüfungen erhalten | 9 | Vorhandenes Schema, Validator, Typechecker und Beispieltest liefern unterschiedliche Nachweise | Für jedes gewählte Originalartefakt vorhandene Prüfung und tatsächliche Regelabdeckung benennen |
| X07 – Paketkonflikte | 0 | Bereits eingeordnete N/A-Befunde sind keine bestandene Paketprüfung | Geeignete Prüfung für Ziele, Typen, IDs, Instanzgrenzen und widersprüchliche Fachregeln nachweisen |
| X08 – Ownership | 7 | Feldverantwortung als Vorschlag dokumentiert, gemeinsame Änderungsregel unbewiesen | Führende Quelle, zulässige Ableitung, Konflikt und Änderungsherkunft pro Bindung festlegen |
| **Summe** | **45** | **Einordnung vollständig, Nachweise weiterhin offen** | **Keine automatische Umwertung der Matrix** |

## 7. Präzisierung des Prüfungstors

Die frühere Formulierung, Originalvalidatoren müssten alle vier Domänenartefakte akzeptieren, ist als späteres Erfolgskriterium zu präzisieren: Ein vorhandener Standard ist nicht automatisch ein separates Dateiformat mit Originalvalidator. Insbesondere ARIA-Semantik und APG-Muster ergeben noch kein originales neutrales Accessibility-Dateischema.

**Arbeitsvorschlag:** Für jede ausgewählte Quelle separat festhalten: formales Originalschema, vorhandenes Werkzeug, benötigte Host-/Implementierungsbindung und verbleibende manuelle Anforderungen. Wo eine zusätzliche Accessibility- oder Integrationsbeschreibung nötig ist, wird diese als neue Ergänzung offengelegt und erhält keine erfundene Originalkonformität. Bestehende eigene Prüfungen sollen weiterhin erhalten bleiben.

Dies senkt keine fachlichen Anforderungen. Es verhindert einen scheinbaren Nachweis durch ein Werkzeug, das für das betreffende Artefakt gar nicht belegt ist. Ein späterer praktischer Auftrag muss Formate und Werkzeuge konkret festlegen; die gegenwärtige Arbeit bleibt Dokumentation.

## 8. Was jetzt festgehalten ist und was weiter offen bleibt

Die Originalfelder, drei konkrete Bindungsketten und sämtliche Integrationszeilen sind dokumentarisch abgeglichen. Das offene Register verhindert, dass dieselben Fragen bei jeder Fortsetzung neu gezählt werden.

Weiter offen bleiben insbesondere die tatsächliche Kombination unveränderter Originalartefakte, ein geeignetes Accessibility-Artefakt, vollständige Typabbildung, formales Layout, externe Unterkomponentenauflösung und native Zielprofile. Diese Fragen benötigen gezielte Quellen-/Formatentscheidungen und teilweise spätere praktische Nachweise. Ein eigenes Manifest oder eine neue Referenzsprache wird aus diesem Befund noch nicht ausgewählt.
