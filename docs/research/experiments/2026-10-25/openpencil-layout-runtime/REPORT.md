# Vollständige Originalprojektion: feste Overflowpolitik und Koordinatengrenze

Stand: 25. Oktober 2026. **Sechs vollständige Originalexportbedingungen und sechs Browserbedingungen, zwölf numerische Voraberwartungen erfüllt.** Die gewünschte dynamische Input-Ankerbeziehung ist im Wachstumsgegenfall ausdrücklich **nicht** erfüllt. Kein vollständiges Layout-/Scrollsystem daraus abgeleitet.

## Frage und Paketendbedingung

Offen waren zwei unterschiedliche Aussagen: Kann der bereits identifizierte Scenegraph-/Webadapterpfad tatsächlich eine formal bestimmte Overflow-/Scrollpolitik bis zum Host erzeugen? Und bilden seine parent-/x-/y-Koordinaten bereits die gewünschte Input→Popup-Ankerbeziehung mit stabil bleibendem Abstand?

Endbedingung: Originalgraphen mit begrenzten Frames beziehungsweise Input-/Popup-Geschwistern erzeugen, die **vollständigen** Original-APIs sceneNodeToDesignDocument und serializeHTML aufrufen und die tatsächlichen Ausgaben im Browser messen. Es werden keine Fragmentkörper ersetzt und keine neue fremde Layoutbibliothek angebunden. Dieses Paket beantwortet beide Fragen im angegebenen Umfang; die übrigen UXSpec-/uSpec-/Overlaypfade sind keine mitgeprüften Gegenstände.

## Originalumfang

Unveränderte veröffentlichte @open-pencil/scene-graph 0.16.0 und @open-pencil/dom-css 0.16.0 aus dem vorherigen Paket, unverändertes Paketlock und Originalinventar. Keine neue Abhängigkeit installiert. Das bereits dokumentierte fehlende RegistrygitHead und die Grenze des Repo-/Distributionsvergleichs bleiben erhalten. Die vorherige Projektionquellanalyse beschreibt die beteiligten Funktionen, der neue Versuch führt deren öffentlichen vollständigen Aufrufpfad tatsächlich aus.

Die Eingaben verwenden vorhandene originale Felder: parentId/Hierarchie, x/y, width/height/maxHeight, layoutMode und clipsContent. Der eigene Harnisch erstellt ausschließlich Forschungsgraphen mit Original-APIs und fragt deren Ausgabe ab. Kein neues Ankerfeld, keine zusätzliche universelle Policy-/Produktsprache, keine Szenegraphattrappe und keine Originalquelländerung.

## Drei feste Overflowfälle

Ein Originalframe enthält einen größeren Originalframe als Kind. Der vollständige Export schreibt die tatsächlich vorhandene Größen-/Clippingsemantik in Inline-CSS. Im Browser werden die nativen Scrollpositionen auf 80 gesetzt:

| Originaleingabe | Tatsächliche Hostgeometrie | Berechnete Overflowpolitik | Scrollposition x/y danach |
| --- | --- | --- | --- |
| clipsContent=true; 180×60, Inhalt 300×300 |180×60; Scrollausdehnung 300×300| hidden |80/80|
| clipsContent=false; 180×60, Inhalt 300×300 |180×60; Scrollausdehnung 300×300| visible |0/0|
| clipsContent=true; Höhe 300, maxHeight 60 |180×60; Scrollausdehnung 300×300| hidden |80/80|

Dies ist ein positiver Nachweis einer **festen zweiachsigen Zielpolitik des bestehenden Original-Webadapters**. Die Bedeutung von hidden stammt aus dem bereits gebundenen CSS-Overflowstandard: Inhalt wird begrenzt, programmgesteuertes Scrollen ist möglich, direkte Benutzer-Scrollbedienung ist dadurch nicht freigegeben. Letztere wurde nicht mit Scrollrad/Touch getestet. Ein sichtbarer Scrollbar-/auto-Modus ist in diesen Fällen weder beschrieben noch hinzugefügt.

Das ist weitergehend als die vorherige isolierte Feldanweisungsprobe: Original-Graphinitialisierung, Hierarchie, Größen-/Maximalhöhenprojektion, vollständige HTML-Serialisierung und tatsächlicher Scrollhost sind hier zusammen ausgeführt. Es ist keine Wiederholung eines bloßen CSS-Schlüsselworttests. Die früher belegte Informationsverluststelle bei importierten Fremdwerten clip/auto/scroll bleibt dennoch unverändert wahr.

## Drei Geometriefälle

Ein Parentframe enthält die getrennten Input- und Popup-Grenzboxen. Die Originaleingabe positioniert das Popup bei y=28. Im Ausgangsfall ist der Input 20 Pixel hoch; der gewünschte Beispielabstand beträgt 8 Pixel. Der zweite Fall ändert ausschließlich die Original-Inputhöhe auf 40. Der dritte versetzt den gemeinsamen Parent um 50 Pixel auf beiden Achsen.

| Fall | Gemessene Inputhöhe | Popup relativ zum Parent | Gemessener Abstand zum Inputende | Gewünschte Relation erfüllt? |
| --- | ---: | --- | ---: | --- |
| Koordinatenausgang |20|0/28|8| ja, bei diesen festen Werten |
| Input wächst |40|0/28|-12| **nein** |
| Gemeinsamer Parent bewegt sich 50/50 |20|0/28|8| ja, beide folgen dem Parent |

Die relative Parentposition besitzt eine tatsächlich ausgeführte Koordinatenbedeutung. Daraus folgt jedoch keine benannte Relation zur **Unterkante des anderen Inputelements**. Das Popup bleibt bei der gespeicherten Koordinate, obwohl sich die Inputhöhe ändert. Die negative Ankerbedingung wurde vorab mit der erwarteten numerischen Abweichung gespeichert; das dazu getrennt gespeicherte Feld desiredRelationSatisfied bleibt false. Zwölf erfüllte Beobachtungserwartungen werden deshalb nicht als zwölf erfüllte Produktanforderungen ausgegeben.

Der Originalgraph versprach für diese bloßen Koordinateneingaben keine automatische Geschwisterankerung. Der Versuch ist kein pauschaler Fehlerbefund des Editors und widerlegt nicht beliebige weitere Originalmodelle. Insbesondere wurden ein anderer Constraint-/Prototypingpfad, ein Canvas-Resizeengineaufruf oder ein zusätzliches CSS-Ankerbinding nicht simuliert.

## Einordnung pro Feld

**OpenPencil V06 U → A/C498, begrenzt auf die feste Outputpolitik des bestehenden Scenegraph→Webadapters.** Die konkret belegte Kombination aus Größenbegrenzung, überlaufendem Inhalt und hidden-/visible-Projektion hat jetzt eine definierte und tatsächlich ausgeführte Scrollbedeutung. Der Beitrag wird als Adapter eingeordnet: Der Originalkern führt ein Clippingboolean, der vorhandene Webadapter bindet daran die konkrete CSS-Policy. Eine neutrale Visualbeschreibung muss diesen Ziel-/Policybezug ausdrücklich erhalten. Originalmodell, konkrete Übersetzung und Plattformsemantik werden nicht gleichgesetzt.

Das unveränderte V06-Kriterium fordert ausdrücklich beschriebene Overflow-/Scrollbedeutung; dieser Beitrag deckt die genannte feste Policy ab, keine freie Auswahl aller CSS-Politiken. Die Einordnung behauptet keine allgemeine auto-/Scrollbar-Komponente, keine native Zielgleichheit, keine UX-Eingabebindung und keinen verlustfreien Import beliebiger CSS-Overflowwerte. Insbesondere bleibt der ältere clip→hidden-/auto-/scroll-Verlustbefund erhalten. Ein vollständiger Autocomplete-Scroller ist damit nicht als Produkt gebaut oder abgenommen.

**OpenPencil V04 bleibt U/C499.** Originale Parentkoordinaten sind belegt; der noch fehlende Gegenstand ist eine ausdrücklich definierte und ausgewertete Relation Input-Unterkante→Popup mit Abstand unter Größenänderung. Der beobachtete Parentbezug wird nicht als dieser Zielbezug umetikettiert. Eine spätere zusätzliche Ankerabbildung muss Quelle, Zielelement, Abstand und Größen-/Änderungssemantik selbst belegen.

Keine Übertragung auf UXSpec/uSpec V04/V06 und keine Kriterienänderung bei den anderen Domänen. Im Layoutpaket bleibt nach dieser Einordnung genau diese OpenPencil-Ankerfrage neben vier ursprünglichen UXSpec-/uSpec-Fragen offen.

## Beobachtungen, Herkunft und Grenzen

cases.json ist vor den Ausführungen gespeichert. results.json enthält pro Originalexport Quellknoten-IDs, tatsächliche Projektionsstyles, vollständiges serialisiertes HTML und Erwartungsentscheidung. host/index.html enthält genau diese Originalausgaben mit eigenen isolierenden Prüfrahmen. browser-results.json bindet deren Ergebnisdateihash und bewahrt alle nativen Maße, Scrollpositionen sowie das nicht erfüllte gewünschte Ankerverhalten.

Der erste Browserzugriff fand den früheren Recherchetab nach einer Sitzungs-/Tabänderung nicht mehr; der Fehler vor der DOM-Messung bleibt protokolliert. Ein eigener neuer Hintergrundtab wurde verwendet. Infrastrukturwiederholungen werden nicht als weitere Bedingungen gezählt. Keine fremden Browserinhalte oder Projekte verändert.

Aktuell **41 U: 26 Integration und 15 weitere**, insgesamt **435 Bedingungen in 56 Gruppen**. Sechs neue Originalexport- und sechs Browserbedingungen gezählt, nicht jede erneute Abfrage. Keine physische Tastatur-/Wheel-/Touch-/AT-Prüfung, kein vollständiger Editorbuild oder Graphpersistenztest. Kein Commit/Push, keine neue Produktionskomponente oder Agenten.
