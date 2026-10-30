# SELECTION-02 · Ergebnis

**Die neuen Builder wählen Select bei drei und SelectWithSearch bei 30 Optionen.** Beide Entscheidungen entsprechen dem vorab eingefrorenen Profil für feste Werte. Die tatsächliche B-Ausgabe besitzt einen nicht editierbaren Auswahlbutton und ein separates Suchfeld im Picker. Sie ist damit keine lediglich umbenannte editierbare Autocomplete-Eingabe.

Der Folgeversuch behebt die Angebotslücke aus SELECTION-01. Er beweist keine allgemeine optimale UX: Kandidatenangebot, fachliche Anforderungen und Policy wurden gemeinsam geändert. Ein Builder pro Bedingung und eine Koordinatorprüfung ersetzen weder kausalen Modellvergleich noch Nutzertest. **release:false.**

## Geprüft und erhalten

| Umfang | Ergebnis |
| --- | --- |
| Neue führende Dateien | Original-CEM-Schema, loses SCXML-XSD, JSON/XML/CSS-Syntax und HTML-Parsebarkeit akzeptiert. Der allgemeine Helper bleibt korrekt BLOCKED / SEMANTIC_PROFILE_UNSUPPORTED. [Inspektion](../preflight/original-inspection.json). |
| Native Auswahlregel | Vier tatsächliche DMN-Fälle: drei Optionen → Select, 30 → SelectWithSearch, fehlende Suchmöglichkeit bzw. fehlender Provider → kein definierter Kandidat. Vier Fähigkeitsprofile mit Quellenhashes geprüft. [Beleg](../preflight/policy-checks.json), [lesender Nachprüfer](../preflight/check-policy.py). |
| SCXML-Verhalten | 13 begrenzte Prüfungen in SCION: Query/Wert getrennt, feste Schlüssel, deaktivierte/ausgefilterte Optionen, doppelte IDs, Escape, Hostupdates und Events. [Ergebnis](../preflight/component-behavior.json), [Prüfcode](../test-component.cjs). |
| Browser-Erstprüfung | **36 von 37** abgeleiteten begrenzten Checks erfüllt; der Fokusfehler SEL2-B01 bleibt als Erstfehler bestehen. [Auswertung](results.json), [Rohbelege](browser-first.json), [Auswertungscode](summarize.py). |
| Separate Reparatur | **10 von 10** gezielte Browserregressionen erfüllt. Keine rückwirkende Korrektur der Erstlieferung. [Reparaturbelege](browser-repair.json), [separate Ausgabe](../outputs/b-repair-01/REPORT.md). |
| Unabhängiges Recompile | A, B und B-Reparatur kompilieren strikt; erzeugte JavaScriptbytes stimmen mit gelieferten überein. [Compilerbeleg](compiler-checks.json). |

### Browserverhalten

Der Koordinator bediente die echten lokalen Seiten über BrowserOS neo mit synthetischen Daten. Beide Formulare besitzen vier erforderliche Input-Felder und eine erforderliche Länderwahl, sichtbare Labels und eindeutige IDs. Tatsächliche Input-Ereignisse wurden erfasst, die führende Null der Telefonnummer bleibt erhalten. Leere Pflichtfelder verhindern lokalen Erfolg; Änderungen entfernen vorherige Erfolgsmeldungen. Es wurde nichts versendet; eine vollständige Datenschutz-/Sicherheitsprüfung wurde nicht ausgeführt.

Bei B öffnet der Trigger den Picker und fokussiert die Suche. „Indien“ liefert IN. Pfeilnavigation bewegt den Fokus auf die Option, ohne den Wert bereits zu ändern; Enter bestätigt IN und stellt Triggerfokus wieder her. Danach filtert „+1“ Kanada und USA, während bestätigter Schlüssel und angezeigtes Label Indien unverändert bleiben. Escape verwirft nur die Suchabfrage. Die beiden +1-Länder sind getrennt auswählbar. End-Navigation erreicht SK und scrollt die Zeile tatsächlich in den sichtbaren Bereich. Unbekannte Suche erzeugt weder Option noch neuen Schlüssel.

### SEL2-B01: Fokusverlust beim Schließen

In der Erstlieferung B schloss ein focusout-Microtask das Popup zu früh: Während der internen Fokusübertragung von Suchfeld zu „Schließen“ war document.activeElement vorübergehend BODY. Die dadurch verborgene Schaltfläche konnte keinen Klick mehr empfangen; der Fokus blieb auf BODY. Zweimal reproduziert und mit tatsächlicher pointer-/focus-Ereignisfolge erfasst. [Erstbewertung vor Reparatur](first-assessment.json).

Derselbe Builder erstellte b-repair-01 und berücksichtigt nun relatedTarget für interne Fokuswechsel. HTML, CSS und Entscheidung sind bytegleich übernommen; Erstdateien bleiben unverändert. Schließen, interner Fokuswechsel, Commit, Escape und echtes Verlassen per Tab wurden im Browser erneut geprüft. Im Rohbeleg bezeichnet tabOutside zunächst den noch internen Schließen-Button; erst der separat protokollierte dritte Tab verlässt das Popup. Diese Prüfschrittbezeichnung wird ausdrücklich klargestellt, nicht als bestandener externer Übergang ausgegeben.

## Herkunft, Grenzen und Lernpunkte

Zwei neue Builder ohne Elternhistorie wurden angefordert; sie sahen laut Auftrag nur eigene Aufgabe, Eingabe und relevante Kandidaten-/Skillquellen. Exact Prompts, Eingaben, Kriterien und Bibliotheksmanifest wurden vor Dispatch gehasht. Diese Bindung beweist keine vollständige technische Zugriffsisolation. Ein unabhängiger blinder Reviewer oder ein vollständiges Pfadaudit liegt nicht vor. Die Modellidentität wurde nicht recherchiert und ist nicht separat belegt. Es wurden keine Provider-/Limitabbrüche gemeldet; das ist keine Aussage über unbekannte interne Anbieterereignisse.

Beide Builder leiteten ihre Wahl manuell aus den gelesenen Originalregeln ab; die native DMN-Vorprüfung wurde zentral ausgeführt. Die Dateizeiten stützen die berichtete Entscheidung vor der ersten UI-Datei; sie versiegeln nicht rückwirkend den damaligen Inhalt. Originale, Quellen und Reparaturhashes stehen in first-deliveries.json, repair-delivery.json und integrity.json.

Eine kopierte ältere Select-Notiz behauptet noch, eine Suchvariante sei nicht definiert. Builder A erkannte die Inkonsistenz; im neuen Manifest und in eigenen Originaldateien ist die Variante tatsächlich vorhanden. Diese Dokumentationsabweichung bleibt im eingefrorenen Kandidaten erhalten und ist in [ERRATA](../ERRATA.md) korrigierend eingeordnet. Sie ist kein Beleg dafür, dass ein Agent Varianten frei erfinden darf.

**Fachlicher Gewinn:** Das Modell braucht mindestens Wertevertrag, Interaktionszweck, Suchoberfläche und Verhalten unbekannter Eingaben als getrennte Merkmale. Der Name „Autocomplete“ allein reicht nicht. Die [UX-Leitlinie](../../../../../../ux/AUTOCOMPLETE.md) hält die Nutzerbeispiele Adresse und Vorwahl vollständig fest. Eine freie Adress-Schreibhilfe ist weiterhin ein eigener, noch nicht implementierter Vertrag. Trefferlosigkeit eines Anbieters wäre dort allein kein Ablehnungsgrund.

Nicht geprüft: vollständige Interface-/SCXML-Gleichheit der manuellen Hosts, gesamte Geometrie/Themes/Fontmetriken, vollständiger AX-/Screenreader-Nachweis, reale IME, iOS/Android und statistische Übertragbarkeit. Der neue Kandidat liegt bewusst in einer separaten Forschungsrevision; live-example und frühere Studienquellen bleiben unverändert. Die Suchgrenze >15 bleibt Produktpolicy, kein allgemeiner UX-Schwellwert.
