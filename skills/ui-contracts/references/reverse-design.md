# Design → Contracts

Nur bei Designeingaben laden; gemeinsamer Ablauf in [Rückwege](reverse.md).

1. Eingabe unterscheiden: native FIG-Datei, erreichbarer Editor/MCP, SVG oder Screenshot. Für einen vorliegenden lokalen Figma-Export den optionalen [FIG-Reader](../../../tools/figma-reader/README.md) nutzen. Die Anleitung zeigt, wie Frame- und Node-IDs gefunden und Ebenen, Texte, Komponenten und Variablen aus dem Export gelesen werden. Die [historische Autocomplete-Gegenprüfung](../../../tools/design-review/README.md) hat ihren eigenen, an das Prüfprofil gebundenen OpenPencil-Import.
2. Teile, Texte, Varianten, Layout, Farben, Typografie, Clipping, Referenzen und vorhandene explizite Annotationen mit Node-/Varianten-IDs erfassen. Native Werte von gerenderten Pixeln unterscheiden. Screenshotmessung ist eine Beobachtung mit Unsicherheit; daraus keine exakten Tokens, Schriftdateien oder versteckten Varianten behaupten.
3. Kandidaten für CEM-Teile, DTCG/CSS und Zustandsdarstellungen getrennt zuordnen. Ein dargestellter „offen“-Zustand beweist weder seinen Auslöser noch einen Übergang. Designannotation als Aussage belegen; nicht als ausgeführte Interaktion ausgeben.
4. Fehlende API, Wertverträge, Commit-/Abbruchregeln, Tastatur, Fokus und zugängliche Namen im gewählten Profil offen halten. Sichtbarer Text beweist keine programmatische Labelbeziehung. Keine Eventpayload oder ARIA-Rolle aus der Optik erfinden.
5. Nach Klärung führende Contracts ergänzen und [Vollständigkeit](completeness.md) neu prüfen. Der Designexport bleibt Eingabebeleg; beschlossene Regeln führen anschließend die Originaldateien. Neue Ausgabe und Vergleich prüfen nur den tatsächlich abgedeckten Designumfang.
