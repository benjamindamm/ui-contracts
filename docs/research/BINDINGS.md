**Einordnung dieses Entwurfs:** Die folgenden Zahlen und „noch nicht ausgeführt“-Aussagen bewahren frühere Prüfrunden. Aktuelle Matrixnachweise stehen in [CURRENT-STATUS](CURRENT-STATUS.md); zusätzlich offene gemeinsame Integrationsarbeit in [PROJECT-GAPS](PROJECT-GAPS.md). Die begrenzten späteren Adapterversuche ersetzen noch keine fertige gemeinsame Architektur.

**Konsolidierter Vorschlag vom 25. Oktober 2026:** [IP-01](INTEGRATION-PROFILE.md) mit [geplanter Gesamt-Abnahme](INTEGRATION-ACCEPTANCE.md). Der folgende Text bewahrt den historischen Arbeitsstand.


**Historischer Zwischenstand – 25. Oktober 2026:** 41 offene Nachweise (26 Integration, 15 weitere), 435 benannte Prüfbedingungen in 56 Gruppen. Vollständige Integration, Produkt-UI und Assistenztechnik sind weiterhin nicht nachgewiesen; statische HTML-Host-Fixtures wurden inzwischen im Browser geprüft. Historische Zahlen und „nicht ausgeführt“-Aussagen unten beziehen sich auf die jeweils benannte frühere Runde. Maßgeblich ist das [aktuelle Register](OPEN-FIELDS.md).

**Typisierte Referenzbindung geprüft:** [ARIA-Host → externe CEM-/SCXML-Knoten](experiments/2026-10-25/typed-references/REPORT.md), 16 Erwartungen erfüllt, Original-CEM/SCXML-Schemas separat akzeptiert. WAI-ARIA X03 begrenzt A/C462 durch Zusatzresolver; keine native ARIA-Modellreferenz. Aktuell 54 U, 299 Bedingungen/36 Gruppen.

**Neu: informationsbezogene Ownership geprüft.** [Originalpaket, Quelländerung und Konflikte](experiments/2026-10-25/ownership-conflicts/REPORT.md): zwei führende Informationen mit Ableitungen, 15 Änderungsfälle, eine erhaltene und korrigierte Revisionsverletzung sowie vier praktische Gegenbedingungen. CSS Layout X08 begrenzt A/C459; aktuell 41 U (26 Integration, 15 weitere), 283 Bedingungen in 35 Gruppen. Keine generische Ownership-/Transaktions-/Identitätsgarantie.

**Neue Laufzeitgrenze:** [Original-Defaultinvoke](experiments/2026-10-25/scxml-invoke/REPORT.md) koppelt bei gleichem Child-src die Daten zweier Instanzen trotz separater Elternvorbereitung: drei von sechs Erwartungen verletzt. Cancel/Neustart als Lebenszyklus sind begrenzt ausgeführt; ein Diagnosefall mit unterschiedlichen URIs besteht. Keine gewählte Lösung. Zum damaligen Teilabschluss 56 U-Zellen; in jenem Lauf keine Neubewertung. Sechs zusätzliche Fälle mit eigenem instanzgetrenntem Invokeradapter bestehen; die Originalverletzungen bleiben erhalten (C458).

**DTCG-Folgeprüfung:** [Getrennte Visualquelle mit zusätzlichem Webadapter](experiments/2026-10-25/dtcg-binding/REPORT.md), zwölf Bindungs-/Übersetzungsfälle und vier Browserbedingungen erfüllt. X01 DTCG A/C454 im begrenzten Referenzfall; zum damaligen Teilabschluss 56 U-Zellen. Kein vollständiger DTCG-Validator.

**Ergänzung 25.10.2026 – SCXML-Laufzeit:** [Gespeicherter Prüfblock](experiments/2026-10-25/scxml-runtime/REPORT.md) mit 17 Bedingungen: 9/10 im Ausgangslauf, 2/2 Diagnosefälle und 5/5 Browserfälle. Getrennte Vorbereitung verhindert die beobachtete Datenkopplung. Native Parent-Sendung und ein zusätzlicher interaktiver Forschungs-Host sind ausgeführt; keine Produktionskomponente, physische Tastatur- oder AT-Prüfung. Ältere Aussagen zu ausschließlich statischer Prüfung gelten für die damaligen Teilversuche. Historischer Zwischenstand nach DTCG: 56 U-Zellen.

# Konkrete Feldbindungen und verbleibende Integrationsfragen

**Aktuelle Fortschreibung nach diesem dokumentarischen Stand:** [49 E3-Proben](experiments/2026-10-24/REPORT.md) sind inzwischen ausgeführt. CEM I02 ist nun A/C421; damaliger Stand 65 U (41 Integration, 24 weitere). Frühere Aussagen „keine Ausführung“ und damalige Zählungen unten dokumentieren den Entstehungsstand. Keine vollständige UI-/AT-/Integrationsprüfung.


Stand: 24. Oktober 2026. Fortsetzung des [Integrationsabgleichs](INTEGRATION-REVIEW.md). **Dokumentarische Feldprüfung; keine Auswahl eines Formatstapels, keine erzeugten kompatiblen Contractdateien und keine ausgeführten Validatoren.** Die hier nebeneinander betrachteten Kandidaten dienen dazu, konkrete Bindungsprobleme sichtbar zu machen.

## 1. Verlässliche Zählung

Die Matrix enthält aktuell **41 U-Zellen**: **26 in X01–X08**, **20 in anderen Anforderungen**. Das sind offene Nachweise je Kandidat und Anforderung, keine Zahl fehlender Komponenten oder unabhängiger Probleme. Alle 16 Kandidaten-Durchgänge sind abgeschlossen. Eine zusätzliche Quellprüfung hebt eine U-Zelle nicht automatisch auf.

Das vollständige [Register der offenen Felder](OPEN-FIELDS.md) hält jede U-Zelle mit Befund, Frage, Priorität und nächstem Schritt fest. Es wurde aus dem gespeicherten Prüfregister abgeleitet. Nach der ursprünglichen Triage und UXSpec V05 U→A sind nun alle 72 Restzellen dokumentarisch erneut ausgewertet: [Gesamtprüfung](ALL-FIELDS-REVIEW.md). Fünf Neubewertungen ändern die aktuelle Zahl; 67 technische Nachweise bleiben offen.

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
| X01 – Vier unabhängige Domänen | 11 | CEM/SCXML/CSS/WAI-ARIA und DTCG sind im begrenzten zusätzlichen Webprofil A; andere Kandidatenbindungen bleiben unbewiesen | Weitere Originalbeiträge getrennt prüfen; dynamische Gesamtintegration nicht aus dem statischen Profil ableiten |
| X02 – Identität | 0 | Alle Kandidaten bereits eingeordnet; positive Teilbeiträge sind nicht gleichbedeutend mit Paketidentität | Definition/Instanz/Teil/DOM-ID für den Referenzfall nachvollziehbar zuordnen |
| X03 – Gemeinsame semantische Referenzen | 6 | Zielarten und konkrete Feldgrenzen präzisiert | Bestehende Resolver mit externen Originalzielen und dokumentierter Bedeutung nachweisen oder erforderliche Zusatzbindung benennen |
| X04 – Eigenständige Unterkomponenten | 1 | Definition, Verwendung und Maschinenkontext unterschieden | ScrollArea mit eigenem Kontext und reproduzierbarer Definition vollständig binden; Feldexistenz allein genügt nicht |
| X05 – Externe Versionen | 0 | OpenPencil ist nun A/C411: tatsächlicher Libraryresolver und explizite Revision, keine fertige neutrale Fremdmodellbindung | Praktischen Import-/Update-/Exportnachweis und Revisionspin beibehalten; Format- und Paketversion unterscheiden |
| X06 – Originalprüfungen erhalten | 2 | Vorhandenes Schema, Validator, Typechecker und Beispieltest liefern unterschiedliche Nachweise | Für jedes gewählte Originalartefakt vorhandene Prüfung und tatsächliche Regelabdeckung benennen |
| X07 – Paketkonflikte | 0 | Bereits eingeordnete N/A-Befunde sind keine bestandene Paketprüfung | Geeignete Prüfung für Ziele, Typen, IDs, Instanzgrenzen und widersprüchliche Fachregeln nachweisen |
| X08 – Ownership | 6 | CSS-Zusatzprofil für zwei Informationen ausgeführt; übrige Kandidaten bleiben offen | Weitere Informationsarten und Originalartefakte konkret binden; keine allgemeine Abdeckung ableiten |
| **Summe** | **26** | **Einordnung vollständig, Nachweise weiterhin offen** | **Keine automatische Umwertung der Matrix** |

## 7. Präzisierung des Prüfungstors

Die frühere Formulierung, Originalvalidatoren müssten alle vier Domänenartefakte akzeptieren, ist als späteres Erfolgskriterium zu präzisieren: Ein vorhandener Standard ist nicht automatisch ein separates Dateiformat mit Originalvalidator. Insbesondere ARIA-Semantik und APG-Muster ergeben noch kein originales neutrales Accessibility-Dateischema.

**Arbeitsvorschlag:** Für jede ausgewählte Quelle separat festhalten: formales Originalschema, vorhandenes Werkzeug, benötigte Host-/Implementierungsbindung und verbleibende manuelle Anforderungen. Wo eine zusätzliche Accessibility- oder Integrationsbeschreibung nötig ist, wird diese als neue Ergänzung offengelegt und erhält keine erfundene Originalkonformität. Bestehende eigene Prüfungen sollen weiterhin erhalten bleiben.

Dies senkt keine fachlichen Anforderungen. Es verhindert einen scheinbaren Nachweis durch ein Werkzeug, das für das betreffende Artefakt gar nicht belegt ist. Ein späterer praktischer Auftrag muss Formate und Werkzeuge konkret festlegen; die gegenwärtige Arbeit bleibt Dokumentation.

## 8. Was jetzt festgehalten ist und was weiter offen bleibt

Die Originalfelder, drei konkrete Bindungsketten und sämtliche Integrationszeilen sind dokumentarisch abgeglichen. Das offene Register verhindert, dass dieselben Fragen bei jeder Fortsetzung neu gezählt werden.

Weiter offen bleiben insbesondere die tatsächliche Kombination unveränderter Originalartefakte, ein geeignetes Accessibility-Artefakt, vollständige Typabbildung, formales Layout, externe Unterkomponentenauflösung und native Zielprofile. Diese Fragen benötigen gezielte Quellen-/Formatentscheidungen und teilweise spätere praktische Nachweise. Ein eigenes Manifest oder eine neue Referenzsprache wird aus diesem Befund noch nicht ausgewählt.

**Fortschreibung:** Beide Detailvergleiche sind jetzt dokumentarisch ausgearbeitet; siehe [UXSpec/SCXML](COMPARE-UXSPEC-SCXML.md) und [DESIGN.md/Layout](COMPARE-DESIGN-LAYOUT.md). Drei X04-Beiträge sind A für vorhandene Mechanismen plus zusätzliche UI-Bindung. Keine vollständige Kompositionskette wurde ausgeführt.

## Ausgeführter begrenzter Interface-/Behavior-Nachweis

Das [statische Referenzprofil](experiments/2026-10-24/scxml/REPORT.md) bindet nun eine separate öffentliche CEM-Signatur an statisches SCXML-send/param. Alle vier SCXML-Fälle bestehen ihr Original-XSD; der zusätzliche Forschungschecker erkennt falschen Ereignisnamen, falsches Feld und falschen Typ. Das ist ein konkreter Teilnachweis für zusätzliche Typ-/Bedeutungsbindung, keine vollständige Vier-Domänen-Kette und kein gerenderter Host. I02 ist bei CEM und SCXML jeweils A für dieses eingeschränkte Profil.

## Originalresolver tatsächlich geprüft

Die [Referenz-Folgeprüfung](experiments/2026-10-24/references/REPORT.md) belegt jetzt konkrete Grenzen statt bloßer Hypothesen: importierter Namenskontext, stille globale Modul-ID-Überschreibungen und Token-Einheitenverlust. Die Import-/Rekursionsfälle sind gemeinsam mit ihrer Originalschema-Vorprüfung zu lesen; valide Kollisionsfälle und separat abgewiesene Referenzformen werden nicht gleichgesetzt. Keine gemeinsame Vier-Domänen-Identität daraus abgeleitet.

## Ausgeführte Ziel-/Instanzgegenfälle

[Original-Hostchecker plus eigenes Instanzprofil](experiments/2026-10-25/aria-host-bindings/REPORT.md) zeigen praktisch: ein gültiges DOM-ID-Ziel kann fachlich die falsche Instanz sein. Ein explizites A/B-Mapping erkennt die Kreuzbindung; seine Herkunft aus vier Originaldomänen bleibt noch zu belegen. Zehn Original- und zehn Zusatzbedingungen gespeichert, keine Produkt- oder AT-Konformität.
