# UXSpec: externer DTCG-Zeitwert auf ursprünglichen UX-Timereingang

Stand:25. Oktober2026. **UXSpec X03 A/C509** für diese zusätzliche konkrete Visualzeit→UX-Timereingang-Bindung. **34 U:19 Integration,15 weitere.511 Bedingungen/68 Gruppen.** Zehn Referenz-/Übersetzungs- und zwei Originalschemabedingungen erfüllen ihre Beobachtungserwartungen. Der ursprüngliche, akzeptierte falsche Zeitwert bleibt ausdrücklich erhalten.

## Fehlende Aussage und Endbedingung

Interne Tokenreferenzen allein genügen X03 nicht. Zu prüfen war ein eigener separat gespeicherter DTCG-Originaltoken, seine konkrete Quellrevision/-zielart, eine ausdrücklich zusätzliche semantische Übersetzung und die tatsächliche ursprüngliche UXSpec-Import-/Compilerauflösung auf einen benannten UX-Timereingang. Vorhandene Tests lokaler Elementkollisionen werden nicht wiederholt.

Die Forschungsbeziehung verwendet einen visuellen Animationsdauerwert als Zahleneingabe eines UX-Timers. Das ist eine ausdrücklich gewählte begrenzte Zuordnung dieses Versuchs, keine durch DTCG vorgeschriebene Abschaltregel und keine beschlossene Produktkopplung. Gerade diese zusätzliche Zuordnung ist Teil von A; sie wird nicht als Originalfähigkeit erfunden.

## Originalquellen und tatsächliche Ausführung

DTCG Format2025.10 §8.5/8.5.1 beschreibt duration mit numerischem value und ms/s; eine Millisekunde ist ein Tausendstel einer Sekunde. Dies ist ein Final Community Group Report, keine W3C Recommendation. Der gelesene Originalabschnitt ist gespeichert.

UXSpec-Revision `20dfae0e7224d952e198afdf4ffed26d6fd67180`: unveränderte vollständige ursprüngliche Import-, Resolve-, Compile-, Statepfad- und Diagnosemodule aus dem bereits geprüften Referenzblock. Deren ursprüngliche Quellenhashes werden vor Verwendung abgeglichen. Zusätzlich unveränderte ursprüngliche extractMs-Funktion aus dem tatsächlichen use-auto-dismiss.ts nach AST-Auswahl transpiliert und ausgeführt. Der vollständige Hook wird gelesen: er verwendet die resultierende Zahl für setTimeout/AUTO_DISMISS. **useEffect, der Timeout, der Interpreter, eine UI und AT werden in dieser Gruppe nicht ausgeführt.**

## Warum eine zusätzliche Übersetzung nötig ist

Der Originalimporter liest $tokens eines UXSpec-Dokuments. Die direkte DTCG-Datei besitzt diesen Wrapper nicht; die nachfolgende ursprüngliche Auflösung meldet UNKNOWN_IMPORTED_TOKEN_REFERENCE. Bloßes Umschließen des unveränderten duration-Werts löst das Problem nicht: Der ursprüngliche Resolver reduziert value/unit auf die Zahl, und extractMs erhält1 für die ursprüngliche1s-Dauer. Der Compiler meldet dabei keinen Fehler. Die gewünschte Zeit1000ms ist in diesem akzeptierten Originalgegenfall **nicht** erhalten.

## Explizite zusätzliche Projektion und Zielbindung

Quellort: tokens.json, /motion/animationDuration, $type=duration, expliziter Dateihash. Der eigene Zusatzschritt prüft Zielknoten, positive endliche Zahl und ms/s. Er rechnet1s→1000ms beziehungsweise lässt1000ms unverändert. Diese begrenzte Übersetzung ist eigener Forschungscode, kein vollständiger DTCG-Resolver oder Originalvalidator.

Die erzeugte projektionelle UXSpec-Bibliothek besitzt einen number-Token delay mit dem Millisekundenwert. Sie ist ein vollständiges originalschemafähiges UXSpec-Rootdokument. Der dafür notwendige minimale namespace-Maschinenroot ist ausschließlich generiertes Pflichtgerüst; er wird nicht über imports.machine angefordert oder ausgeführt. Dieses Gerüst wird nicht verschwiegen und löst UXSpecs offene X01-Frage nicht. Der ursprüngliche DTCG-Quellvertrag bleibt unverändert und erhält keine fremde primäre Maschinenbeschreibung.

Der ebenfalls originalschemafähige Consumer importiert clock mit tokens:true und referenziert {clock:delay} genau in $machine.states.active.$visual.autoDismiss. Der ursprüngliche Compiler liefert die tatsächliche Zustandsvisualisierung mit1000; die tatsächliche ursprüngliche extractMs-Funktion erhält1000. AUTO_DISMISS und der Zielzustand done sind im Consumer ausdrücklich beschrieben; tatsächliches zeitgesteuertes Ausführen dieses Übergangs wird nicht behauptet.

Zusätzliche Quell- und Projektionshashes schützen die beiden Dateigegenstände vor still geändertem Input. Konversionsregel, Quellpointer/-typ/-einheit, Zielort und erzeugter Wert sind im Ergebnis gespeichert. Die Referenz löst damit nicht nur einen beliebigen gleichnamigen internen Token auf: eine separate Original-Visualinformation wird mit unveränderter Zeitbedeutung einem ausdrücklich anderen fachlichen Timereingang zugeordnet.

## Zehn vorab benannte Referenzbedingungen P67

[Erwartungen](cases.json), [Resultate und ursprüngliche Traces](results.json), [Prüfer](run.cjs).

| Fall | Beobachtung |
| --- | --- |
| raw-original-dtcg | Direkter DTCG-Root wird nicht als ursprünglicher $tokens-Namensraum erschlossen; ursprünglicher Compiler weist Referenz ab. |
| wrapped-original-duration | Nur umhüllte1s-Dauer wird vom ursprünglichen Compiler akzeptiert, ursprünglicher Timerleser liefert1 statt1000. Beobachtete Grenze, keine positive Zeitkonformität. |
| adapted-one-second | Zusatzprojektion ergibt1000; tatsächlicher ursprünglicher Import/Compiler/Timerleser erhält1000. |
| adapted-thousand-ms | Gleichwertige1000ms-Dauer ergibt ebenfalls1000. |
| missing-original-pointer | Fehlendes Originalziel vom Zusatzschritt abgewiesen. |
| wrong-original-token-type | number statt des verlangten Original-duration-Typs vom Zusatzschritt abgewiesen. |
| unsupported-original-unit | min statt ms/s vom Zusatzschritt abgewiesen. |
| stale-original-source | Veralteter Originaldateihash vom Zusatzschritt abgewiesen. |
| missing-imported-target | Fehlendes clock:missing vom ursprünglichen Compiler abgewiesen. |
| changed-derived-projection | Geänderte abgeleitete Bibliotheksdatei vom zusätzlichen Hashcheck abgewiesen. |

Alle Beobachtungserwartungen erfüllt; der gewünschte Zeiterhalt bleibt im umhüllten unveränderten Originalfall falsch. Keine pauschale Zusage aller Tokenarten, Aliase, Referenzzyklen oder Timerwerte. Es wird kein neuer generischer Paketresolver als Produkt eingeführt.

## Zwei Originalschemabedingungen P68

[Schemaergebnisse](schema-results.json): Consumer und erzeugte vollständige Projektionsbibliothek bestehen das unveränderte ursprüngliche UXSpec-Draft202012-Schema. Das ist keine vollständige Semantikprüfung und kein getarnter eigener Roottyp. Das DTCG-Original wird über die konkret benannte begrenzte Übersetzungsprüfung beurteilt, nicht als gegen ein nicht ausgeführtes Original-DTCG-Schema validiert ausgegeben.

## Bewertung und weitere Grenzen

X03 U→A/C509 nur für diese konkrete zusätzliche externe Zeitreferenz. Keine native direkte DTCG-Importkonformität, keine vollständige Timerlaufzeit und keine automatische Bewertung von X01/X06 oder Layout-/Scrollfeldern. Das notwendige generierte Maschinenpflichtgerüst bleibt eine Integrationsgrenze des Zielmodells. Andere Kandidaten und Referenzarten werden separat geprüft.

## Reproduktion

Eigene Quell-, Projektions- und Consumerdateien sowie alle Ergebnisse sind gespeichert. prepare.cjs erstellt Erwartungen und extrahiert die unveränderte ursprüngliche extractMs-Funktion per TypeScript5.9.3-AST; run.cjs nutzt die vorher gespeicherten vollständigen Originalmodule aus reference-probes/build. Deren Originalquellen/Hashbindung stehen im Manifest. check_schema.py nutzt das gepinnte ursprüngliche UXSpec-Schema mit jsonschema4.25.1. Normabschnitt und Hookabruf sind gespeichert; Originalbibliotheksquellen/-code werden nicht als eigene Implementierung ausgegeben. METHODS.md und REQUIREMENTS.md unverändert. Kein Commit/Push, keine Produktionskomponente oder beschlossene Produktsprache.
