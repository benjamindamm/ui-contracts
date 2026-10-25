# OpenPencil-Radiopfad: Namen, Zustandsattribute und Instanzkontext

Stand: 25. Oktober 2026. **Zwölf vorab gespeicherte Bedingungen, zwölf Erwartungen erfüllt.** Originale Render-/Role-/State-Helfer mit tatsächlichem Vue 3.5.41 und Serverrenderer ausgeführt. OpenPencil A01 und A03 bleiben U: Der Eingangs- und Renderpfad ist präziser belegt, der vollständige Ursprung der semantischen Bindungen und die Live-/Meldungskette noch nicht.

## Frage und Endbedingung

Der [endliche Restplan](../../../REMAINDER-PLAN.md) priorisiert den konkreten Accessibility-Beitrag. Fehlend war ein ausgeführter Beleg, ob der bekannte Radiozweig Namen-/Beziehungsattribute überhaupt erhält, ob Designerattribute die von der Steuerung gesetzte Rolle beziehungsweise checked-Werte überschreiben und ob zwei Kontextverwendungen mit demselben lokalen Controlpfad getrennt bleiben.

Endbedingung dieses Pakets: Originalfunktionen für genau den Radiozweig und seine tatsächlich aufgerufenen Helfer identifizieren; mit zwei expliziten Instanzkontexten positive/negative Eingaben ausführen; VNode-Properties und tatsächliche SSR-Ausgabe sichern. Diese Endbedingung ist erreicht. Ein Original-Scenegraph, ursprüngliche Roleklassifizierung, vollständiger Editor und lebender Accessibility Tree sind andere Gegenstände und wurden nicht durch Hilfsobjekte als erfolgreich ausgegeben.

## Original- und Laufzeitidentität

OpenPencil ab2875cc761ee6cff17d389ff1c85fedae50aeab. render.ts und controls/index.ts stammen bytegleich aus der vorherigen Recherche. Neu über BrowserOS gelesen wurden controls/shared.ts, state.ts und der originale BUTTON_RESET. Der bekannte Peerbereich verlangt Vue ^3.5.41; für diese isolierte Probe wurde **Vue 3.5.41 exakt** aus der offiziellen Registry gebunden und ohne Lifecycle-Skripte installiert. Das Paket bringt @vue/server-renderer 3.5.41 mit. Registryintegrität, Paketlock und Dateien sind protokolliert. Das ist ein ausdrücklich neuer gebundener Laufzeitstand, kein behaupteter Lockstand einer OpenPencil-Installation. Reka wird in diesem Radiozweig nicht ausgeführt.

Die folgenden acht vollständigen Originaldeklarationen wurden anhand des TypeScript-AST isoliert und unverändert transpiliert: root, renderElement, renderNode, stateOf, disabled, interaction, isDisabled und BUTTON_RESET. Keine dieser Funktionen wurde durch eine Ersatzfunktion implementiert. Der eigene Rahmen liefert die ausdrücklich begrenzten DesignElement-/Role-/State-Eingaben und ruft den originalen Radiozweig auf. Nicht durchlaufene Switch-/Slider-/Shader-/Graphzweige werden nicht als unterstützt ausgegeben. Der originale Roleclassifier und createIslandState werden nicht ausgeführt; die zwei State-Maps sind kontrollierte Probeinputs.

## Beobachtete Originalmechanismen

stateOf liest ausschließlich den zum übergebenen island gehörenden Mapkontext und wirft bei fehlendem Pfad. Der Radiozweig setzt role=radio und aria-checked aus seinem Booleanwert; der Originalcallback setzt diesen Wert auf true. disabled stammt aus dem State oder designedDisabled. renderElement übernimmt Attribute und anschließend override.props. Dadurch haben in diesem Pfad die steuerungsseitige Rolle und der checked-Wert Vorrang vor widersprechenden Designerattributen. Das interne data-open-pencil-node-id wird entfernt, die öffentliche id bleibt erhalten.

## Zwölf Bedingungen

| Eingabe / Fall | Tatsächliche Beobachtung |
| --- | --- |
| Zwei Islands, identischer lokaler Pfad | getrennte IDs und Werte; beide als radio gerendert |
| Explizites aria-label | Attribut und Inhalt bleiben in VNode/SSR erhalten |
| aria-labelledby | Referenzstring bleibt erhalten; Zielauflösung nicht damit behauptet |
| Designerrolle button | ursprünglicher Radio-Override gewinnt |
| Designer-checked=false, Modellwert=true | ursprünglicher Modellwert gewinnt |
| Internes Node-ID-Attribut | entfernt, öffentliche id erhalten |
| Direkter Aufruf des originalen A-Callbacks | nur A wechselt auf true; B unverändert; erneutes SSR erhält dieselben IDs/Inhalte |
| Disabled im State | disabled=true am erzeugten Button |
| designedDisabled | ebenfalls disabled=true |
| Fehlender Controlstate | Originalfehler statt beliebigem Zustand |
| Kein Text/Label | Ausgabe wird trotzdem erzeugt; kein Namensvalidator im ausgeführten Pfad |
| Nicht existierendes labelledby-Ziel | String bleibt erhalten; kein Resolver/Validierungsfehler in diesem Pfad |

Alle zwölf Erwartungen erfüllt. Der Callbackaufruf ist keine physische Tasten-/Mausaktion. Disabled-Buttons wurden nicht durch direkte Callbackaufrufe als fehlerhaft bewertet; die tatsächliche native Eingabesuppression ist hier nicht geprüft. SSR ist eine tatsächliche Vue-Ausgabe, aber keine lebende DOM-Reaktivitäts- oder Accessibility-Tree-Messung. Ein Textinhalt oder aria-label im Ergebnis belegt in diesem Paket den Transport; die komplette Berechnung des zugänglichen Namens wurde nicht ausgeführt.

## Konsequenz für A01 und A03

**A01 bleibt U/C490.** Die bisher nur gelesene Attributweitergabe ist nun am konkreten Original-Radiopfad ausgeführt. Instanzkontext, Rolle, explizite Namensattribute und Overrides sind nachvollziehbar. Noch nicht belegt ist, wie die benötigten Namen und externen Beziehungsziele aus den ursprünglichen Behaviour-/Scenegraph-Bindungen entstehen und überprüft werden. Die negativen Namens-/Referenzfälle zeigen, dass dieser Renderer selbst diese Verantwortung nicht vollständig übernimmt. Das ist kein pauschales Urteil über andere Autoren- oder Prüfwerkzeuge.

**A03 bleibt U/C491.** Originaler Modellcallback und danach gerenderter aria-checked-Wert sind verbunden. Zustandssemantik und eine neue Ergebnis-/Fehler-/Lademeldung sind jedoch verschiedene Vorgänge. Das unveränderte Kriterium verlangt definierte zugängliche Aktualisierung; es wird nicht nachträglich um eine allgemeine Pflicht zu eigenen Live-Regions oder Assistenztests für jede reine Schemaeinordnung verschärft. Die hier tatsächlich ausgeführte SSR-Neuausgabe allein belegt noch keinen lebenden Host-/Accessibility-Updatepfad und keine ursprüngliche Meldungsbindung. Ein nächster eigenständiger Nachweis muss genau diesen neuen Zusammenhang prüfen, statt dieselben Attributfälle erneut zu zählen.

Der Restplan ist eine Arbeitsklassifikation: 44 unabhängig untersuchbare Zellen, zwei konkrete Originalklärungen. Daraus folgt keine Zusage, dass jede Frage nach einem einzelnen Lauf positiv abgeschlossen werden kann. Neue tatsächliche Grenzen werden spezifisch nachgeführt. Native Plattformen, tatsächliche AT-Umgebungen und abschließende Produktregeln bleiben getrennte spätere Abnahmen.

Aktuell weiterhin **46 U: 26 Integration und 20 weitere**, jetzt **395 Bedingungen in 49 Gruppen**. Keine Deckungszelle durch diesen begrenzten Rendernachweis geschlossen. Keine neue Produktionskomponente, Autorenanfrage, Agenten, Commits oder Pushes.

## Reproduktion

cases.json wurde vor Ausführung gespeichert; results.json enthält Eingaben, VNode-Beobachtungen, beide tatsächlichen SSR-Strings und alle Erwartungen. extraction.json nennt jede unveränderte Originaldeklaration mit Quellhash und Zeile. source-notes.json und vue-registry-pin.json dokumentieren Originalpfade und Laufzeitbindung; tool/package-lock.json pinnt die reine Forschungsinstallation. Vollständige Originalquellen/node_modules werden nicht als eigene Implementierung exportiert. run.cjs benötigt die dokumentierten Originaldateien und den zuvor gebundenen TypeScript-Compiler. Keine Shell-/Projektinstallationsanweisungen aus Webseitentext wurden ausgeführt.
