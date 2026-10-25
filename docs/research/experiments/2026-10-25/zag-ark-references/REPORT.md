# Zag und Ark UI: getrennte tatsächliche Referenzpfade

Stand:25. Oktober2026. **Zag X03 A/C510 und Ark UI X03 A/C511**, begrenzt auf die jeweils tatsächlich ausgeführte Part-/Rollen-/Zielbindung. **32 U:17 Integration,15 weitere.519 Bedingungen/70 Gruppen.** Acht vorab gespeicherte Beobachtungserwartungen erfüllt; vier tatsächlich gerenderte widersprüchliche Fälle bleiben erhalten.

## Endbedingung

Nicht allein DOM-ID-Gleichheit feststellen: Originalparts müssen auf konkrete separat beschriebene CEM-Zielknoten sowie Rollen und Beziehungen eines unabhängigen HTML/ARIA-Artefakts gebunden sein. Tatsächliche zwei Instanzkontexte und deren zulässige Root-ID-Änderung prüfen; je Kandidat seine eigenen Originalpfade und konkreten Gegenfälle ausführen. Keine bloße Umbenennung eines allgemeinen Booleanbinders.

## Exakte ursprüngliche Ausführung

Neue isolierte, unveränderte Installation: @zag-js/combobox/@zag-js/react/@zag-js/core1.45.0, @ark-ui/react5.39.3, React/ReactDOM19.2.0. [Versionen](versions.json), Lock und Originaldateihashes im Manifest. Zag1.45.0 ist hier der tatsächliche Comboboxpfad; die früher separat untersuchte direkte Core1.46.0-Installation wird nicht gleichgesetzt oder verändert. Ebenso keine globale Byteidentität mit früheren Repository-Snapshots behauptet.

**Zagpfad:** tatsächliches originales useMachine(combobox.machine, props), combobox.connect(service, normalizeProps) und deren getRootProps/getLabelProps/getInputProps/getContentProps/getListProps/getItemProps. Der eigene React-SSR-Prüfhost setzt diese ursprünglichen Props auf native Elemente. Kein falscher Service, keine nachgebaute Maschine oder geänderte Originalfunktion.

**Arkpfad:** tatsächliche originale Combobox.Root/Label/Control/Input/Content/List/Item/ItemText-Komponenten einschließlich ihrer ursprünglichen useCombobox-, Context-, Presence- und Zagdelegation. Die Root-ids gehen durch den echten Komponentenpfad. Kein Direkt-Connect-Output als Arkoutput ausgegeben.

ReactDOMServer erzeugt tatsächlich HTML. Effekte werden nicht im DOM gemountet; keine Eventfolge, Fokus-/Tastaturfunktion, native Browserdarstellung, Hydration oder AT geprüft. Die einfachen eigenen Reactfunktionen sind ausschließlich Forschungs-SSR-Hosts, keine Produktionskomponente oder fertige Komponentenumsetzung. open:true ist ein kontrollierter Initialbeobachtungspunkt.

## Separat beschriebene Ziele und zusätzliche Semantik

Die CEM-Datei ist bytegleich aus S81 übernommen. Die relevanten Zielknoten sind /modules/0/declarations/0/cssParts/0=input, /1=popup und /3=option. Der zusätzliche Binder benennt ihre kontextuelle Zielart CEM-cssParts-Eintrag und prüft die tatsächlichen ursprünglichen data-scope=combobox/data-part-Werte. Ursprüngliches content wird ausdrücklich dem externen popup-Part zugeordnet, item dem option-Part. Diese Zuordnung ist zusätzliche Integrationsarbeit, keine native CEM-Unterstützung.

Die eigene separat gespeicherte HTML/ARIA-Quellfixture beschreibt pro A/B-Instanz die Combobox, das kontrollierte Listbox-Popup, Labelziel und Option. Sie ist eigenes Forschungsartefakt in ursprünglicher HTML/ARIA-Syntax; nicht aus den Kandidatenergebnissen als vermeintliche unabhängige Norm generiert. Rollen-/Beziehungsanforderungen werden im vorbereiteten Hostausdruck getrennt gesetzt. Der Zusatzvergleich liest tatsächliche SSR- und Quell-HTML-Strukturen, prüft globale ID-Eindeutigkeit, Label-for-Ziel, aria-controls-Ziel, Rollen, aria-expanded und Popup-aria-labelledby samt realem Labelziel.

Quell-CEM, externe HTMLdatei und tatsächlicher SSR-Output sind je aufgelöstem Ziel gehasht; Paket-/Lockstände binden den ausführbaren Beitrag. IDs allein wären nicht genug: der konkrete Listboxtyp und seine Beziehungen müssen zum externen Ziel passen. Nicht gebundene Teile, etwa der zusätzliche list-Part, werden nicht als automatisch nachgewiesen ausgegeben. Die Zuordnung zur CEM-Deklaration Autocomplete ist explizit; ursprünglicher Comboboxscope wird nicht mit beliebigen gleichnamigen Widgets verwechselt.

## Vier Zagbedingungen P69

| Fall | Ursprüngliche Beobachtung und Zusatzprüfung |
| --- | --- |
| zag-original-connect | Tatsächliche zwei ursprüngliche Services/Connect-Props rendern die erwarteten Part-/Rollen-/Zielbeziehungen; Zusatzbindung auf CEM/HTML-Ziele akzeptiert. |
| zag-custom-root-ids | Ursprüngliches ids-API ändert alle benannten Ziel-IDs auf die vorbereitete zweite Quellrevision, Beziehungen bleiben konsistent. |
| zag-colliding-content-ids | Ursprünglicher Renderpfad akzeptiert für A/B dasselbe Contentziel popup-b und erzeugt doppelte IDs; Zusatzbinder weist die Kollision zurück. |
| zag-external-role-conflict | Ursprüngliches Popup ist listbox, separat vorbereitete Quellrolle button widerspricht dem konkreten Zieltyp; Zusatzbinder weist ab. |

## Vier Arkbedingungen P70

| Fall | Ursprüngliche Beobachtung und Zusatzprüfung |
| --- | --- |
| ark-original-context | Tatsächlicher originaler Komponenten-/Contextpfad erzeugt zwei konsistente Part-/Rollen-/Zielbindungen; Zusatzbinder akzeptiert. |
| ark-custom-root-ids | ids am echten Root wird durch die ursprünglichen Contextkomponenten konsistent weitergegeben; Zusatzbindung bleibt gültig. |
| ark-input-prop-id-override | Einzelnes originales Input.id überschreibt gerenderte ID, Label-for bleibt beim Contextziel input-a; der Zielknoten fehlt. SSR akzeptiert, Zusatzbinder weist zurück. |
| ark-content-prop-id-override | Einzelnes originales Content.id überschreibt das gerenderte Popupziel, ursprüngliches Input-aria-controls bleibt popup-a; kontrolliertes Ziel fehlt. SSR akzeptiert, Zusatzbinder weist zurück. |

[Erwartungen](cases.json), [Originalrender-Ergebnisse mit vollständigem HTML](render-results.json), [zusätzliche Bindungsresultate](results.json), [SSR-Prüfprogramm](render.mjs), [Zusatzvergleich](check.py). Acht Erwartungen erfüllt. Die vier Fehlerfälle werden vom Originalrenderer nicht abgewiesen; sie sind keine ursprünglichen Typ-/Referenzvalidierungserfolge. Root-ids und einzelne Unterkomponenten-id-Overrides sind unterschiedliche geprüfte Pfade. Keine Behauptung, dass sämtliche ID-Overrides oder sämtliche ursprünglichen APIs fehlerhaft seien.

## Bewertung und verbleibender Rest

Zag X03 A/C510 für seinen tatsächlichen Machine/Connect-Partbeitrag mit zusätzlichen externen CEM-/HTML-Rollen-/Relationszielen. Ark X03 A/C511 für seinen zusätzlich tatsächlich ausgeführten Komponenten-/Contextpfad und dessen eigene Overridegrenzen. Die Bewertungen werden nicht allein wegen gemeinsamer Zag-Abhängigkeit übertragen.

Keine universelle typisierte Fremdmodellauflösung, externe Versionsmigration oder zusätzliche Originalschemafähigkeit daraus ableiten. X01 bleibt bei beiden offen: ein zusätzlicher Vergleich eines Accessibility-Beobachtungspunkts beweist noch keine vier unabhängig führenden Domänen ohne zweite Fokus-/ARIA-/Behaviorquelle. Auch X08 und praktische Interaktions-/AT-Konformität werden nicht automatisch übertragen.

## Reproduktion

Die isolierte tool/package-lock.json pinnt den vollständigen tatsächlichen JS-Baum. Nach Bereitstellen dieser unveränderten Abhängigkeiten im relativen tool/node_modules erzeugt render.mjs tatsächliche SSR-Dateien und die separat vorbereiteten HTML/ARIA-Quellfixtures; check.py vergleicht ihre Struktur gegen die bytegleiche CEM-Datei. Keine Originalmodule/Services gestubbt. Eigene Hosts, Quell-/Outputfixtures, Erwartungen, Ergebnisse und Hashinventar sind gespeichert; installierte Fremdbibliotheken nicht als eigener Code verteilt. METHODS.md und REQUIREMENTS.md unverändert. Kein Commit/Push, keine Produktionskomponente oder neue gewählte Produktsprache.

**Eigene Inventarvorprüfung:** Eine anfängliche angenommene Distributionsdatei use-machine.js existiert in diesem Paket nicht; vor der Registeränderung wurde sie anhand des tatsächlichen Paketbaums auf machine.js/machine.mjs korrigiert. integration-preflight-error.json hält diesen eigenen Metadatenfehler fest; die acht Original-SSR-Fälle waren davon nicht betroffen und zählen nicht erneut. P69/P70 besitzen zusätzlich getrennte [Zag-](zag-results.json) beziehungsweise [Ark-Ergebnisdateien](ark-results.json) mit je vier Fällen.
