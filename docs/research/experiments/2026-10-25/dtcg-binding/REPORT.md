# DTCG-Tokens als getrennte Visualquelle im Webreferenzfall

Stand: 25. Oktober 2026. **Begrenztes Paket ausgeführt: zwölf zusätzliche Übersetzungs-/Bindungsbedingungen und vier Browserbedingungen erfüllen ihre vorher gespeicherten Erwartungen.** Keine universelle Integration, kein vollständiger DTCG-Validator, keine Technologieauswahl.

## Quellen und Trennung

DTCG Format Module 2025.10, Final Community Group Report vom 28.10.2025, erneut über BrowserOS gelesen: §7.2.2 verkettete Tokenreferenzen, §7.2.3 Zyklen, §8.2 Dimensionen. Dimensionen führen einen numerischen Wert mit px/rem. Das Modul ist ein Community-Group-Bericht, keine W3C Recommendation. Quelle und Abrufhash stehen im Manifest; keine neue Veröffentlichung oder vollständige Quellenprüfung behauptet.

Eigene tokens.json verwendet nur dimension-Tokens mit explizitem $type, numerischen $value-Objekten und Curly-Brace-Aliasen. Keine fremden Interface-, Zustands- oder ARIA-Definitionen darin. Separate layout.css beschreibt die geometrischen Regeln und nimmt nur drei übersetzte CSS-Variablen entgegen. Interface.json, behavior.scxml und accessibility.html des vorherigen Vier-Domänen-Falls sind bytegleich. Ihre ursprünglichen Format-/Hostprüfungen und Bindungsgrenzen bleiben im Vorgängerbericht dokumentiert; sie werden hier nicht als neue Tests gezählt.

Die zusätzliche profile.json benennt originale Quelldateien und Hashes, dieselben Instanzen A/B und deren Teile sowie drei Tokenpfade, Zielselektoren, CSS-Eigenschaften und führende Visualquelle. layout.css und Tokens sind gemeinsam der Visualbeitrag. Die Zusatzdatei ist ein Forschungsprofil, keine DTCG-Erweiterung oder gewählte Produktsprache. DTCG liefert keine originale domänenübergreifende Bindung.

## Ausgeführte Übersetzungs- und Bindungsbedingungen

| Bedingung | Gespeicherte Beobachtung |
| --- | --- |
| Kontrollfall | Drei dimension-Werte aufgelöst; keine Zusatzregelfehler |
| Alias-Kette | Zusätzliche Zwischenreferenz bis zum expliziten Wert aufgelöst |
| Fehlendes Token | missing-token |
| Zyklische Referenz | alias-cycle |
| Einheitloser Skalar | dimension-value |
| em statt px/rem | dimension-unit |
| Zeichenfolge als Zahl | dimension-value |
| number statt dimension | dimension-type |
| Behavior als führende Tokenquelle | leading-source |
| Unbekannter Popupselektor | target-binding |
| Veralteter Tokenhash | source-integrity |
| rem-Variante | 0.5rem / 10rem / 2rem aufgelöst |

Alle zwölf Erwartungen erfüllt. run.py ist bewusst eigener Zusatzcode mit enger Teilmenge: keine $ref-/JSON-Pointer-Auflösung, Gruppenvererbung, $extends, Resolver-Kontexte, komplexen Tokenarten oder vollständige Dokumentkonformität. Das Profil verlangt explizite Typen an jedem verwendeten Token; diese Einschränkung ist keine allgemeine DTCG-Pflicht. Ziele werden gegen die festgelegten selektierten Bindungen geprüft, keine generische DOM-Semantik erschlossen. Ein abgelehnter Fall beweist nur diese konkrete Regel.

## Vier Browserbedingungen

Die ursprüngliche Zwei-Instanzen-HTML-Fixture wurde in einem eigenen leeren Prüftab mit layout.css dargestellt. Zusätzlicher Übersetzer löst Tokens und setzt CSS-Variablen, der Browser führt das CSS aus. Für jede Instanz wurde die px- und rem-Variante gemessen; Rootschriftgröße explizit 16px. Alle vier Erwartungen erfüllt:

- Abstand Input → Popup: 8px.
- Popuphöhe: 160px, Overflow auto.
- Sieben Zeilen à 32px; Scrollinhalt 224px.

Damit sind für diesen Snapshot gleiche geometrische Ergebnisse aus erhaltenen Einheiten belegt. rem ist an die Rootschriftgröße gebunden; keine allgemeine px/rem-Identität behauptet. Kein dynamischer Wechseltest mit veränderter Schriftgröße. Keine Zeilennavigation, kein Screenreader, keine native Zielplattform. Dieser Browserlauf führt nicht zusätzlich den SCXML-Interpreter aus; dessen begrenzter Nachweis liegt im separaten Laufzeitblock.

## Bewertung und Restgrenzen

X01 bei DTCG wird **U → A** für denselben begrenzten zusätzlichen Webreferenzfall eingeordnet: unabhängige Originalartefakte und konkrete zusätzliche Bindungs-/Übersetzungsregeln sind vorhanden und an zwei Instanzen ausgeführt. A bezeichnet den erforderlichen Zusatzadapter. DTCG wird dadurch nicht zum Format für alle vier Domänen. Keine weiteren Felder umbewertet.

Damit 56 offene Matrixzellen, davon 36 Integration und 20 weitere. Der Gesamtauftrag ist nicht abgeschlossen. Originalvalidatoren, vollständige Interaktion, native Profile, Komposition, Ownership-/Versionskonflikte und Migration bleiben in ihrem jeweiligen Umfang offen. Keine Implementierung einer Produktionskomponente, kein Commit oder Push.

## Reproduktion

run.py benötigt nur Python-Standardbibliothek und schreibt results.json sowie die beiden resolved-Dateien. prepare.py erzeugt die eigenen Ausgangsdateien aus dem benachbarten Vier-Domänen-Paket; Fälle/Erwartungen wurden vor Ausführung festgelegt. browser-function.js enthält den Browserprüfer; browser-run.js enthält die tatsächlich verwendeten serialisierten Inputs. Zum erneuten Lauf einen eigenen leeren Prüftab wählen; die Tabwahl im Browser-Runner auf diesen eigenen Tab ausrichten. Die Ergebnisse wurden nicht nachträglich durch Wiederholung als zusätzliche Bedingungen gezählt.
