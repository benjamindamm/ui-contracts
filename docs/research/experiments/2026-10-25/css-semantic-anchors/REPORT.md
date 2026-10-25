# Statische CSS-Ankerbindung an Originalteile und Hostinstanzen

Stand: 25. Oktober 2026. **14 unterschiedliche Bedingungen, 14 Erwartungen erfüllt.** Zusätzlicher Forschungsresolver für CSS Layout X03; keine neue Produktsprache oder Komponentenimplementierung. Die beiden externen X06-Originalklärungen aus dem vorigen Paket werden nicht erneut untersucht.

## Konkrete Lücke und Paketendbedingung

Der vorhandene Vier-Domänen-Fall hatte CSS-Ankernamen und zwei DOM-Instanzen. Die typisierte CEM-/SCXML-/ARIA-Referenzprüfung pinnte zwar die CSS-Bytes, löste die CSS-Referenzen aber ausdrücklich nicht auf. Fehlend war die konkrete zusätzliche Kette von position-anchor über anchor-name und ein bestimmtes Hostelement zum richtigen CEM-Komponententeil derselben Instanz.

Endbedingung dieses Pakets: Original-CSS und CEM/HTML unverändert getrennt lassen; genau die deklarierten Ankerbeziehungen des gespeicherten einfachen Zwei-Instanz-Falls auslesen; Originalteile und tatsächliche Host-IDs zuordnen; fehlende, mehrdeutige oder instanzfremde deklarierte Ziele abweisen. Nicht unterstützte CSS-Mechanismen dürfen keine bestandene vollständige Bindung ergeben. Die Endbedingung ist erreicht; native CSS-Ankerauflösung bleibt ein anderer Nachweis.

## Originalbeitrag und zusätzliche Regeln

Originalquelle: CSS Anchor Positioning WD vom 27.03.2026, §§2.1–2.4 und **§7 Accessibility Implications**, über BrowserOS gezielt gelesen. Die genaue Abschnittsnummer im gebundenen Draft lautet §7; ältere pauschale §9-Verweise werden hier nicht wiederholt.

- anchor-name benennt ein Ankerelement, sofern es eine entsprechende Box erzeugt.
- position-anchor wählt den standardmäßigen Ankerbezug, der unter anderem durch Ankerfunktionen verwendet wird.
- Die originale native Zielwahl berücksichtigt Scope, zulässige Boxen und Baum-/Layoutreihenfolge. **Mehrere gleichnamige Anker sind im Original erlaubt.** Eine Auswahl kann über nächsten Vorfahren oder letztes geeignetes Element erfolgen.
- position-anchor ist eine durch position zurücksetzbare Untereigenschaft. Eine spätere position-Deklaration darf nicht als bedeutungslos behandelt werden.
- Visuelle Anker erzeugen ausdrücklich keine Accessibility-Beziehung; diese muss im zuständigen Markup entstehen.

Der zusätzliche Resolver bildet diese native Suche **nicht** nach. Sein enges Profil fordert für die unterstützte deklarierte Bindung genau einen benannten Zielkandidaten und einfache eindeutige ID-Selektoren. Mehrdeutigkeit ist daher ein Fehler **dieser zusätzlichen Instanzbindung**, kein behaupteter CSS-Normverstoß. Andere zulässige CSS-Formen bleiben unsupported. Dass ein deklarierter Zielname zum richtigen Input gehört, beweist weder die tatsächliche Existenz einer geeigneten Layoutbox noch dessen effektive Auswahl nach Kaskade und Layout.

## Verwendete Artefakte und Werkzeuge

artifacts.json enthält bytegleich die vier bestehenden Forschungsfixtures aus typed-references: CEM interface.json, SCXML behavior.scxml, CSS visual.css und HTML accessibility.html. Die Ausgangshashes bleiben identisch. Neue CSS-Varianten sind eigene Testfixtures; ihre Quellenpins werden ausdrücklich aktualisiert, außer im Fall eines absichtlich veralteten Pins. Es werden keine Originalstandarddateien verändert.

css-tree 3.2.1 liest die echte CSS-AST einschließlich Deklarationsorten, Selektoren und Ankerfunktionen. Die zwei verwendeten Wertgrammatiken und der Originaltypalias kommen unverändert aus der bereits gespeicherten zusätzlichen Originalgrammatikbindung (P44), ohne das native Paketwörterbuch zu ändern. Dies ist **keine vollständige Stylesheet-Konformitätsprüfung**. CEM wird einmal gegen das bestehende unveränderte Originalschema geprüft; eigene JSON-Pointer-/Hostbindungen benutzen Python/lxml. Die ursprünglichen SCXML-Zustands- und ARIA-Prüfungen werden nicht erneut als neue Nachweise gezählt.

Die eigene Zusatzregel löst den CEM-Komponentenpointer und die zugehörigen input-/popup-Partpointer auf, prüft ihre tatsächliche Mitgliedschaft und führt sie über die A-/B-Instanzzuordnung zu den eindeutigen Hostelementen. Das tatsächliche CSS muss den referenzierten Ankernamen auf genau diesem Input deklarieren. Ein gleichnamiger Anker auf der anderen Instanz oder auf dem Listenteil ist kein gültiger Ersatz.

## 14 Bedingungen

| Fall | Beobachtung |
| --- | --- |
| Bytegleiches Kontrollpaket | beide deklarierte Instanzbindungen aufgelöst |
| Konsistente Umbenennung des A-Ankernamens | Bindung bleibt korrekt; Name allein ist nicht die Identität |
| Popup A nennt Anker B | foreign-anchor-part |
| Fehlender Ankername | missing-css-anchor |
| Zwei gleichnamige deklarierte Anker | nonunique-css-anchor; zusätzliche Profilverletzung, kein CSS-Syntaxfehler |
| A-Anker auf Listenteil statt Input | foreign-anchor-part |
| Geänderte CSS-Datei mit altem Hash | source-revision |
| Ankerbezug über var() | unsupported-value |
| Klassen- statt einfachem ID-Selektor | unsupported-selector |
| Bedingte verschachtelte Ankerregel | unsupported-nesting |
| Explizites anchor-scope | unsupported-scope |
| Impliziter auto-Anker | unsupported-value; gültige Originalform, außerhalb dieses Profils |
| Späteres position nach position-anchor | unsupported-reset |
| Expliziter anderer Name in anchor()-Funktion | unsupported-named-function; nicht als Defaultankerbindung übersehen |

Die ersten 13 Erwartungen waren vor ihrem Lauf gespeichert und wurden bestätigt. Danach wurde die noch nicht abgedeckte explizite Ankerfunktionsreferenz als 14. Erwartung vor deren Ausführung ergänzt; der Erstlauf bleibt in initial-13-results.json erhalten. Der abschließende Lauf bestätigt alle 14. **Gezählt werden 14 unterschiedliche Bedingungen, nicht 13 plus 14.** Keine ursprüngliche Erwartung wurde geändert oder ein Fehlschlag verborgen.

results.json enthält pro Bedingung geänderten Quellhash, tatsächliches Profil, CSS-AST-Auszug, alle Issues und Auflösungszeugen mit CEM-Pointern, Instanz, CSS-Deklarationsposition und Host-ID. bound bezeichnet ausschließlich die beschriebene statische Zusatzbindung; unsupported bezeichnet keine ungültige CSS-Sprache und keinen bestandenen Gesamtcheck.

## Einordnung und verbleibende Grenzen

**CSS Layout X03 U → A/C485** für den konkret ausgeführten zusätzlichen Resolver zwischen Original-CSS-Ankerdeklarationen, Original-CEM-Teilen und zwei HTML-Hostinstanzen. Original-Ankernamen werden nicht als bereits vorhandene fremde Modelladressen ausgegeben. Die zusätzliche Art-, Zugehörigkeits-, Versions- und Instanzprüfung ist ausdrücklich erforderlich.

Kein automatischer Abschluss von CSS I01–I03/B01–B04/A01–A03 oder anderen Kandidatenspalten. Insbesondere gibt die CSS-Bindung weder zugängliche Namen noch Tasten-, Fokus- oder Meldungssemantik vor. Diese bleiben in den zuständigen getrennten Domänen. WAI-ARIA I03 wird nicht durch Mitbenutzen von CEM automatisch neu bewertet.

Weiter offen: native Anchorbox-Zulässigkeit und tatsächliche Zielwahl, Kaskade einschließlich all/Inline-Styles/Stylesheets, Shadow Trees, Pseudoelemente, Popover-/Top-Layer-Fälle, dynamische CSS-Variablen und Layoutänderungen, explizite Scope-/Ankerfunktionsbezüge und tatsächliche Assistenztechnik. Für diese Formen gibt dieses Paket keine allgemeine Abnahmegarantie. Das Ergebnis darf nicht als native CSS- oder vollständige Vier-Domänen-Integration dargestellt werden.

Aktuell **46 U: 26 Integration und 20 weitere**, insgesamt **368 Bedingungen in 46 Gruppen**. Dieses Paket verbessert eine Referenzzelle, keine der 20 anderen offenen Fachzellen. Kein Browserlayout, SCXML-Lauf, Tastatur-/AT-Test, Commit oder Push.

## Reproduktion

prepare.py kopiert die vorhandenen Fixtures/Zuordnungen und speichert die Erwartungen; run.py ruft parse-css.cjs als reinen AST-/Grammatikleser auf und führt danach die zusätzliche Referenzprüfung aus. Gepinnte bestehende Laufzeiten und Werkzeuge, Originalgrammatikprofil und CEM-Schema sind im source-manifest.json gehasht. source-notes.json speichert die genau gelesenen Originalabschnitte als Fundstellen/Hashes und eigene Befunde, ohne vollständige Originaltexte zu verteilen. Der lokale Browsercapture wird nicht mitexportiert.
