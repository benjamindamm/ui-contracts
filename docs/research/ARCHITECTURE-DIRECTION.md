# Einordnung: gemeinsame Bauanleitung für Web, iOS und Android

**Recherche abgeschlossen:** [Abschluss und Lesereihenfolge](RESEARCH-CLOSEOUT.md). iOS/Android sind spätere Perspektiven und keine Abschlussbedingung dieser Phase.


Stand: 25. Oktober 2026. **Ziel und begründeter Vorschlag**, keine native Umsetzung oder Plattformfreigabe. Diese Notiz hält die im Gespräch präzisierte Absicht und die Grenzen der ausgewählten Webreferenz fest.

## Ziel

Eine gemeinsame Beschreibung soll einem Coding-Agenten als prüfbare Bauanleitung dienen. Er soll daraus Web-, iOS- und Android-Komponenten erzeugen können, die in den ausdrücklich vereinbarten Merkmalen nahezu gleich aussehen und gleich reagieren. Die Beschreibung soll die fachlichen Entscheidungen tragen; der Agent soll sie nicht aus Bildern oder lückenhaften Plattformbeispielen erraten müssen.

Nahe visuelle Gleichheit und gleiche fachliche Ereignisse sind Ziele, keine bereits erbrachten Ergebnisse. Schriftmetriken, Eingabeverfahren, Fokus, Scrollverhalten und zugängliche Bedienung benötigen explizite Plattformregeln und eigene Abnahme. Falls native Standardcontrols die vereinbarte Darstellung nicht erlauben, wäre eine eigene Darstellung eine zu reviewende Umsetzungsvariante. Sie ist hier nicht ausgewählt.

## Vier Kernbeiträge und unterschiedliche Formate

| Beitrag | Rolle im konkreten Webvorschlag | Format / Grenze |
| --- | --- | --- |
| CEM | Signaturen, Property-/Eventmetadaten und benannte Teile | JSON mit eigenem Schema; Web-/JavaScript-orientiert, noch keine belegte native API-Abbildung. |
| DTCG | Typisierte Designwerte und Tokens | JSON mit anderem Fachmodell; beschreibt allein kein vollständiges Layout. |
| SCXML | Zustände, Übergänge, Guards und Aktionen | XML; ausgewählte Referenz nutzt ECMAScript und eine konkrete Runtime. Native Laufzeitabbildung offen. |
| WAI-ARIA | Zugängliche Websemantik und Beziehungen | Normregeln mit konkreter HTML-Hostabbildung; kein eigenständiges neutrales Contractdateischema für alle Plattformen. |

HTML/CSS bilden das Webziel ab; APG liefert ergänzende Bedienmuster. „Vier Kernstandards“ bedeutet damit nicht vier allein vollständige und direkt kompatible Sprachen. Die tatsächliche Kombination besitzt zusätzliche Ziel- und Bindungsregeln.

## Was Zusammenführen bedeuten soll

Ein gemeinsames Paket referenziert die Originaldateien, statt sie in eine neue große Sprache umzuschreiben. Die zusätzliche Bindungsbeschreibung benennt Definitionen, Verwendungen, Teile, Ports, Zustände, führende Quellen und konkrete Zielbeziehungen. Eigene Resolver und Plattformadapter transportieren die Beziehungen und prüfen Konflikte; Originalprüfer bleiben erhalten.

[IP-01](INTEGRATION-PROFILE.md) beschreibt dieses Modell. Das [statische Referenzpaket](experiments/2026-10-25/ip01-static/REPORT.md) und der [abgeschlossene Browserlauf](experiments/2026-10-25/ip01-browser/REPORT.md) zeigen begrenzte statische und tatsächliche Webbindungen. Der Browseradapter verwendet noch konkrete Codekonventionen. Eine vollständig generische deklarative Bindung und native Adapter sind nicht fertig.

## Einschätzung und überprüfbares Erfolgskriterium

Die Richtung ist sinnvoll, wenn das Ergebnis ein überprüfbarer Vertrag mit ausdrücklich benannten Plattformabbildungen wird. Der Webreferenzlauf unterstützt die technische Machbarkeit einer solchen Verbindung, beweist aber nicht, dass die vier gewählten Beiträge bereits einen universellen neutralen Kern bilden.

Ein späterer Crossplattformnachweis müsste dieselbe Komponente und dieselben fachlichen Akzeptanzfälle auf mindestens einem nativen Ziel ausführen: gleiche Inputs und Outputs, Zustands- und Auswahlregeln sowie vereinbarte Geometrie; dazu jeweils passende Fokus-/Accessibilityregeln. Erst dieser Vergleich kann zeigen, welche Gemeinsamkeiten tragen und welche Ergänzungen notwendig sind. Für diese spätere Phase ist hier keine Implementierung beauftragt oder ausgeführt.

**Abschluss dieser Runde:** konkreter Webvorschlag und begrenzte Nachweise liegen vor. Kein Versprechen automatischer plattformübergreifender Gleichheit, kein beschlossenes Produktformat und keine weiterlaufende native Forschungsrunde.
