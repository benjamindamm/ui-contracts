# CSS X06: explizite Anbindung unveränderter Originalgrammatiken

Stand: 25. Oktober 2026. **Zwölf vorher festgelegte Stylesheetbedingungen ausgeführt, sämtliche Erwartungen erfüllt.** Vier Original-Propertygrammatiken werden an den vorhandenen Lexer gebunden; der mitgelieferte Wörterbuchstand bleibt unverändert. Keine neue Layout-/Browserprüfung.

## Endlicher Gegenstand und Quellen

Vorige offene Grenze: css-tree 3.2.1 unterstützt mehr Anchor-Syntax als 3.1.0, sein originales Propertywörterbuch entspricht aber nicht vollständig dem gespeicherten Anchor-Draft. Insbesondere normal/match-parent werden dort abgewiesen. Ein neueres Paket allein ist daher kein Originalversionsnachweis.

Dieser Restzugriff prüft genau den bereits vorhandenen öffentlichen createLexer-/matchProperty-Einstieg und die ursprünglich ausgewählten Originalgrammatikstellen. BrowserOS hat die Propertydefinitionen erneut direkt aus den gepinnten W3C-Publikationen gelesen:

| Quelle | Unveränderte Wertgrammatik |
| --- | --- |
| Anchor Positioning 1, WD 27.03.2026: anchor-name | none oder die originale #-Liste aus anchor-name |
| Derselbe Draft: anchor-scope | none, all oder dieselbe Liste |
| Derselbe Draft: position-anchor | normal, none, auto, anchor-name oder match-parent |
| Derselbe Draft: Typalias anchor-name | dashed-ident |
| Overflow 3, WD 07.10.2025: overflow-y | visible, hidden, clip, scroll, auto |

Die **exakten** Originalsyntaxstrings einschließlich Operatoren/Wiederholung stehen in anchor-source.json, overflow-source.json und profile.json. Die Tabelle oben erläutert sie, ersetzt ihre Grammatik nicht. Keine neu erfundenen Keywords oder Defaultwerte und kein ungepinnter aktueller Editor-Draft.

css-tree **3.2.1** und die bestehende Installation/Lock aus css-grammar/tool-current werden unverändert wiederverwendet. Seine originalen createLexer-/matchProperty-Implementierungen und generischen Typen sind lokal gelesen. Der zusätzliche Lexer erhält nur diese Originaltypen/-properties als explizite Konfiguration; generische Token-/Identifierprüfung stammt aus dem gebundenen Backend. Die globale originale css.lexer-Instanz und ihre Propertydefinitionen werden nicht überschrieben.

## Zusätzliche Prüfbindung und bewusst begrenzte Reichweite

Eigener Zusatzcode liest tatsächliche CSS-Stylesheets mit dem ursprünglichen Parser und führt deren Deklarationswerte gegen die vier gebundenen Originalgrammatiken. Die Formatdefinitionen bleiben Original-CSS; der zusätzliche Teil ist Zuordnung/Versionierung und der explizite Checkeraufbau. Das ist **kein nativer unveränderter Wörterbuchbeitrag des css-tree-Pakets**.

Nur die vier genannten Properties sind als geprüft klassifizierbar. Eine unbekannte oder andere Property führt für den Gesamtfall zu unsupported_scope, auch wenn eine benachbarte bekannte Deklaration gültig ist. Fehlende Variablensubstitution wird als unsupported_value bewahrt, nicht als Nachweis ungültigen CSS ausgegeben. Beobachtungen der einzelnen Deklarationen einschließlich ursprünglicher Matcherfehler bleiben gespeichert.

Das Profil ist ein enger Forschungsprüfumfang. Keine Behauptung, sämtliche Stylesheetregeln, CSS-Escapes, At-Rules, Funktionen, Draftproperties, globalen Kaskadenfragen oder semantischen Modulbedingungen vollständig abzudecken. Generische Backendtypen werden nicht zur Vollkonformität aller referenzierten CSS-Spezifikationen aufgewertet.

## Zwölf Bedingungen

| Fall | Originalwörterbuch / zusätzlich gebundener Prüfpfad |
| --- | --- |
| position-anchor normal | Originalwörterbuch weist ab; Originalgrammatikbindung akzeptiert |
| position-anchor match-parent | Ebenso |
| Vier-Property-Kontrolle mit zwei Selektoren | Zusätzliche Bindung akzeptiert |
| anchor-name als Kommaliste | Akzeptiert gemäß ursprünglichem #-Operator |
| Ankername ohne erforderliche Form | invalid |
| overflow-y banana | invalid |
| Zusätzlicher fremder Wert nach normal | invalid |
| Gültige bekannte und unbekannte Property gemischt | Gesamtfall unsupported_scope, kein falsches grünes Gesamturteil |
| Syntaktisch gültiger, im DOM fehlender Ankername | Akzeptiert als Syntax; DOM-/Instanzziel bewusst nicht geprüft |
| var() | Originalbackend meldet nicht unterstütztes Matching; unsupported_value |
| top mit verschachteltem ungültigem anchor-Argument | unsupported_scope, keine Wiederholung des früheren falschen vollständigen Matchurteils |
| max-height | unsupported_scope, obwohl ein früherer Standardwörterbuchversuch diesen Wert akzeptieren konnte |

Alle zwölf Voraberwartungen erfüllt. Insbesondere wird die alte beobachtete Unterstützungslücke nicht gelöscht: Das native Wörterbuch bleibt für normal/match-parent negativ, der zusätzliche Originalgrammatikpfad ist der neue Gegenstand. Die aus früheren Proben bekannte calc-/var-/DOM-Lücke wird nicht durch einen kleinen positiven Propertykorpus verdeckt.

## X06-Einordnung

**CSS Layout X06: U → A/C479 für diese explizite Originalgrammatik-/Checkerbindung an die vier Properties.** Originalsyntax ist vorhanden und hier unverändert aufrufbar; zusätzliche Versionierungs-/Zuordnungsarbeit ist erforderlich. Die neutralen CSS-Quelldateien werden nicht in eine neue Produktsprache umgebaut.

A ist ein begrenzter tatsächlicher Adapterbeitrag, keine pauschale Zusage vollständiger Original-Draftprüfung oder eines geeigneten nativen Gesamtvalidators. Ob eine vollständige CSS-Datei im später gewählten Produktprofil alle übrigen Originalregeln erfüllt, bleibt gesondert zu prüfen. DOM-Referenzsemantik X03 und reale Geometrie-/Plattformintegration werden nicht durch dieses Syntaxpaket geschlossen.

Aktuell **49 U: 29 Integration und 20 weitere**. X06 **8 D, 2 A, 2 begrenzte N, 4 U**. **348 Bedingungen in 44 Gruppen.** Keine Produktionskomponente, Technologieauswahl, Commits oder Pushes.

## Reproduktion

Originales css-tree3.2.1 gemäß dem bisherigen tool-current-Lock bereitstellen. prepare.py übernimmt ausschließlich die gespeicherten Originalsyntaxstrings in das ausdrückliche Zusatzprofil und speichert die zwölf Erwartungen. run.cjs verwendet den ursprünglichen Parser und createLexer/matchProperty, protokolliert native und zusätzlich gebundene Resultate. Source-/Profil-/Toolhashes im Manifest. Kein Browser, UI-/Assistenztest oder Beweis sämtlicher CSS-Conformance-Regeln.
