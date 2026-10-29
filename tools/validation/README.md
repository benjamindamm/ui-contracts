# Gemeinsamer Prüfeinstieg · begrenztes IP-01-Profil

Stand: 26. Oktober 2026. **Statischer Prüfer und aktueller Browseradapter sind verbunden.** [Aktueller Ergebnisüberblick](../../docs/validation/README.md).

Der Einstieg prüft das [statische IP-01-Paket](../../docs/research/experiments/2026-10-25/ip01-static/reference/) und dessen ausdrücklich fest zugeordneten ausführbaren Webhost. Er ist kein allgemeiner Validator. Ein [separater lokaler Agent-Skill](../../docs/skills/README.md) orchestriert Autorenarbeit und diese begrenzten Prüfungen. Originaldaten, historische Captures und die AC-R01-Studie werden nicht verändert.

## Installation

Vom Repository-Stamm, mit Python 3.9 oder neuer und Node.js/npm (geprüft mit Node 24):

```sh
python3 -m venv tools/validation/.venv
tools/validation/.venv/bin/python -m pip install -r tools/validation/requirements.lock.txt
npm ci --prefix tools/validation --ignore-scripts --no-audit --no-fund
npm ci --prefix tools/openpencil --ignore-scripts --no-audit --no-fund
```

Der zweite Werkzeugbestand liefert die bereits gepinnte Original-SCXML-Runtime und Polyfillbytes. Fehlen sie oder stimmen ihre Hashes nicht mit der festgelegten Herkunft überein, blockiert die Vorbereitung.

## Statische Prüfung und Standardverhalten

```sh
# Ohne aktuellen Browserlauf: Exit 2 / BLOCKED.
tools/validation/.venv/bin/python tools/validation/check.py

# Explizit statisch: Referenzfall Exit 0 / PASS_LIMITED, release:false.
tools/validation/.venv/bin/python tools/validation/check.py --scope static --output /tmp/ip01-static.json
```

`--package PFAD` erlaubt eine separate Kandidatenkopie des unterstützten Pakets mit `bindings.json`, `resolved.json`, Quellen und `values.json`. Dies ist keine allgemeine Prüfung beliebiger Bibliotheken unter `libraries/`. Das Bindungsformat bleibt ein eigener Forschungsentwurf.

## Einen neuen Browserlauf durchführen

Jeder Versuch braucht ein **neues, noch nicht existentes Verzeichnis**. Beispiel vom Repository-Stamm:

```sh
tools/validation/.venv/bin/python tools/validation/browser_gate.py prepare --run-dir /tmp/ui-contracts-web-new
tools/validation/.venv/bin/python tools/validation/browser_gate.py serve --run-dir /tmp/ui-contracts-web-new
```

Der Server läuft lokal im Vordergrund, gibt seine URL aus und schreibt sie in `server.json`. Der Laufordner enthält die vier vorbereiteten `browser-01.js` bis `browser-04.js`. Ein Agent öffnet eine eigene Seite an dieser URL mit **BrowserOS neo**, wartet auf `body[data-ready="true"]` und führt die vier Dateien der Reihe nach jeweils als Code eines BrowserOS-`run`-Aufrufs aus. Sie sind Browser-SDK-Programme und werden **nicht mit Node gestartet**. Jeder Aufruf meldet sein eigenes erfolgreiches oder fehlgeschlagenes Ende an den Collector.

Bei einem Ausführungsfehler keine Teilfortsetzung als Erfolg ausgeben. Den Befund erhalten, Ursache korrigieren und mit einem neuen Laufverzeichnis erneut beginnen. Der Collector überschreibt keine bereits erhaltenen Captures oder Operationsergebnisse.

Nach vier erfolgreichen Aufrufen in einem weiteren Terminal:

```sh
tools/validation/.venv/bin/python tools/validation/browser_gate.py finalize --run-dir /tmp/ui-contracts-web-new
tools/validation/.venv/bin/python tools/validation/check.py --browser-run /tmp/ui-contracts-web-new --output /tmp/ip01-web.json
```

Anschließend den eigenen lokalen Server beenden. Die Auswertung benötigt keinen weiterlaufenden Server. Sie liest die Rohdaten erneut und wendet die aktuellen Originalschemas, Kriterien und zusätzlichen Rohbeobachtungsprüfungen an. Ein vorher vorhandenes `results.json` wird nicht als Erfolgseingabe vertraut.

## Sechs Schritte und Freigabe

| Schritt | Tatsächlicher Umfang | Grenze |
| --- | --- | --- |
| 1 · Standards/Prüfer | Feste Formatversionen und Teilumfänge; Version/Ladbarkeit notwendiger Python-/Nodeprüfer; Originalschemahashes; Browseradapter und ausdrücklich übergebener Lauf | Fehlender notwendiger Prüfer oder fehlendes Browserresultat blockiert. |
| 2 · Syntax/Originalschemas | Striktes JSON, XML-Wohlgeformtheit, Paketabschluss; Original-CEM-JSON-Schema und loses SCXML-1.0-XSD | Kein vollständiger Originalvalidator für CSS/DTCG/HTML/ARIA/APG. |
| 3 · Bindungen | Hashes/Revisionen, Zielarten, Invoke-/Zustandsziele, IDs, begrenzte Typen/Defaults/Events, Instanzbezüge, Dimensionen/Aliase und Token-CSS-Beziehungen | Nicht jede TypeScript-/SCXML-Ausdrucksform oder alle Standardsyntax. |
| 4 · Ownership/Komposition | Quellführung gegen festes Profil, deklarierte Instanzhierarchie, Verbot rekursiver Expansion | Keine allgemeine Ownershipsprache oder generische Runtimeauflösung. |
| 5 · Aktuelles gemeinsames Verhalten | 20 erhaltene Browserfälle einschließlich öffentlicher Events, Fokus, tatsächlicher Scrollsichtbarkeit, originaler AX-Bäume, Stale-/Fremdinstanz-/Lifecycle-/Fehlerfälle | Ausschließlich der explizit gepinnte Host und dokumentierte Testkontext. |
| 6 · Ergebnis | Stufen, Diagnosen, bestandener Umfang, Warnungen, ungeprüfte Bereiche und eng begrenzte Freigabe | Kein allgemeines Produkt-/Plattform-/AT-Zertifikat. |

Exitcodes: **0** = `PASS_LIMITED` für den gewählten begrenzten Umfang, **1** = `FAIL`, **2** = `BLOCKED`. Fehler stoppen abhängige Fachschritte (`NOT_RUN`); die Berichterstellung läuft auch bei Fehlern. `PASS` an Schritt 6 heißt nur „Bericht erstellt“.

**Statisch:** `release:false`. **Erfolgreiche aktuelle Webkette:** `release:true`, aber ausschließlich `releaseScope:exact-pinned-bounded-web-reference-only` und `productionRelease:false`. Dies bestätigt die notwendigen Prüfungen dieses eng definierten Forschungsfalls; die Grenzen des Profils bleiben bestehen.

Ohne `--browser-run` wird kein automatisch gefundenes oder historisches Resultat verwendet. Die maximale Laufgültigkeit beträgt zwei Stunden ab Vorbereitung; neue Paket-/Hostbytes, Prüfer oder Kriterien machen einen alten Lauf unbrauchbar. Eine Veröffentlichung des damals erfolgreichen Ergebnisberichts verleiht ihm keine zeitlich unbegrenzte aktuelle Gültigkeit.

## Feste Paket-/Hostbindung und Herkunft

[profile.json](profile.json) bestimmt den unterstützten statischen Umfang unabhängig vom Kandidaten. [browser-profile.json](browser-profile.json) bindet die exakte statische Baseline an die festgelegten Host- und Runtimebytes. Ein geändertes, sonst statisch gültiges Paket kann diese Webfreigabe nicht übernehmen. Es fehlt weiterhin ein allgemeiner Generator/Resolver für beliebige Definitionen und Hosts.

Für den aktuellen Lauf wird ausschließlich die Capture-Hülle um Laufkennung und zufällige Challenge ergänzt. Diese Quelländerung wird sichtbar gehasht; die fachlichen Hostregeln bleiben unverändert. [browser_gate.py](browser_gate.py) bindet Request, Host, Checkerfingerprint, erfolgreiche Operationsreceipts, zeitlich geordnete Captures und Kriterien. Falsche Challenge und doppelte Captures werden zurückgewiesen.

Die lokale Hash-/Challengekette ist keine unabhängige kryptografische Attestation gegen einen böswilligen lokalen Betreiber. Bibliotheksversionen und übernommene Originalschemahashes werden geprüft; kein unabhängiges Audit jedes installierten Bibliotheksbytes wird behauptet.

## Originalvalidatoren und Zusatzprüfer

[Inventar](inventory.json) · [unveränderte Originalschemas und Herkunft](schemas/provenance.json).

- CEM 2.1.0: Originalschema mit JSON-Schema-Draft-7-Engine; keine vollständige fachliche Signatursemantik.
- SCXML 1.0: loses Original-XSD mit lokalen Modulen; nicht strengere XSD-1.1-/vollständige Recommendation-Abdeckung.
- TypeScript 5.9.3: Originalparser mit **eigener** begrenzter AST-Interpretation (Primitive, optional, Array, geschlossene Records, geprüfter CustomEvent-Payload).
- css-tree 3.2.1: zusätzliche Syntax-/Deklarationsprüfung; tatsächliche ausgewählte Geometrie kommt aus dem Browser.
- DTCG 2025.10: zusätzliche Dimension-/Einheiten-/Alias-/CSS-Bindung, kein vollständiger Originalschema-Nachweis.
- HTML/ARIA/APG: zusätzliche feste Host-/Instanz-/Rollenbeziehungen und tatsächliche ausgewählte Chromium-AX-Beobachtungen; kein vollständiger Originalvalidator oder Screenreaderlauf.
- SCION 4.3.28: Originalruntime mit explizitem eigenem Invoker-/Fehlerrelay-/Webhostadapter.

Die losen Originalschema-Grenzen und frühere Gegenbefunde bleiben erhalten. Keine reale IME, physische Tastaturprüfung durch einen Menschen, Screenreader-Sprachausgabe oder native Ausgabe. Geometrievariationen sind ausdrücklich DOM-/Style-Testkontext, kein vollständiger Theme-/Quellenänderungsprozess.

## Gegenfälle und Regressionen

```sh
tools/validation/.venv/bin/python tools/validation/test_chain.py
tools/validation/.venv/bin/python tools/validation/test_browser_gate.py --run-dir /tmp/ui-contracts-web-new
```

[47 bisherige Gegenfälle](evidence/countercases.json) bleiben Regressionen. [31 Browser-Gegenfälle](evidence/browser-countercases.json) prüfen fehlende/alte/fremde/veränderte Laufdaten, fehlende Prüfer, fehlgeschlagene Operationen, ausgelassene Assertions, fehlerhafte AX-/Fokus-/Scroll-/Event-/Lifecyclewerte und eine abweichende statische Kandidatenkopie. Die Browser-Gegenfälle mutieren ausschließlich temporäre Kopien der aktuellen Belege; sie behaupten keine zusätzlichen Browsererzeugungen. Ein gefälschtes Erfolgs-`results.json` wird ignoriert und aus Rohdaten neu ausgewertet.

Der bewusst erhaltene Fall `runtime-guard-unchecked` kann weiterhin die statische Teilprüfung bestehen. Die Webfreigabe lässt sich daraus nicht ableiten: Die geänderte Paketrevision besitzt keine freigegebene Hostzuordnung. Dies ist eine ausdrücklich getestete Grenze statt eines vorgetäuschten allgemeinen Behaviorvalidators.

[Erste Testdiagnose und erhaltene Vorstufen](evidence/README.md) · [Werkzeugmanifest](manifest.json). Testläufe ersetzen aktuelle Werkzeugtestberichte, verändern aber keine historische Forschung und keine deren Zähler. Neue Browseraufnahmen liegen immer in einem neuen Laufordner.

## Reparaturregel und Skill

Ein späterer Agent darf Kandidatenkopien korrigieren. Danach müssen betroffene Prüfungen und die notwendigen abhängigen Regressionen für dieselbe beabsichtigte Freigabe erneut bestehen; nach Quellen-/Prüferänderungen ist ein neuer Browserlauf nötig. Originalschemas, Profil und Erfolgskriterien dürfen zur Reparatur nicht abgeschwächt werden. Neue Profile oder Checkerfassungen brauchen eigene begründete Prüfung und behalten frühere Gegenbefunde.

Der separate [Skill `$ui-contracts`](../../skills/ui-contracts/SKILL.md) ist lokal erstellt und geprüft. Er verwendet diese Kette unverändert und macht aus fehlender Abdeckung keine Freigabe. Eine Veröffentlichung ist nicht erfolgt.
