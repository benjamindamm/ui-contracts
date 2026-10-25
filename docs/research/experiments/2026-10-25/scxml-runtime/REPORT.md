# Tatsächliche SCXML-Laufzeit und zusätzliche Hostbindung

Stand: 25. Oktober 2026. Endbedingung dieses begrenzten Pakets: die vorhandene behavior.scxml tatsächlich ausführen, getrennte Instanzzustände und Daten untersuchen, native Parent-Ereignisse nachweisen und Zustände/Ereignisse durch sichtbaren Zusatzcode ins Browser-DOM projizieren. **Dieses Paket ist ausgeführt und gespeichert; die vollständige Autocomplete-/Plattformintegration bleibt offen.**

## 1. Originalwerkzeug und unveränderte Eingabe

Originalpaket **@scion-scxml/scxml 4.3.28**, RegistrygitHead ce920c0df2cbf1e96b0ebafa658c1019c43f81d7. Nodeauflösung enthält core 2.6.25 und core-base 1.0.26. Paketlock, zentrale Originaldateien und Browserbundles sind gehasht. README, Typdeklarationen, Vorbereitungscode und native Parent-send-Implementierung sind lokal aus der Originaldistribution gelesen; Hersteller-Konformitäts-/Reifeversprechen wurden nicht als eigene Prüfung übernommen.

Die vorhandene behavior.scxml aus dem Vier-Domänen-Paket wird bytegleich benutzt: SHA-256 f30796022ba2e8bde7d8f80f4b8c4223e7ff89a8abf7ca2f8a48a48ceeebfa2a. Sie nutzt das ECMAScript-Datenmodell, closed/open/selected und send/param mit #_parent. Der Compiler documentStringToModel und die Originalklasse core.Statechart führen sie aus; keine eigene Zustandsmaschine als Ersatz geschrieben.

Der Browser nutzt das mitgelieferte unveränderte dist/scxml.min.js derselben Paketversion. Sein SHA-384 wird beim Laden browserseitig erzwungen. Daraus wird keine ungeprüfte Identität aller intern eingebündelten Browserabhängigkeiten mit der Node-Auflösung abgeleitet. Die Paketversion und die tatsächlichen Bytes sind für beide Pfade separat nachvollziehbar.

## 2. Zehn vorab definierte Node-Laufzeitfälle

| Fall | Beobachtung |
| --- | --- |
| Getrennte Zustände A/B | OPEN A, OPEN B, CLOSE A → A closed, B open |
| Unveränderte öffentliche Sendung | OPEN/COMMIT → selected durchlaufen, danach closed; echte Parentinstanz empfängt value-change mit value=alpha |
| Unbekanntes Ereignis | Keine Transition oder öffentliche Ausgabe |
| COMMIT in closed | Keine Transition oder öffentliche Ausgabe |
| Parameterdaten bei gemeinsam vorbereiteter Modellfunktion | **Erwartung widerlegt:** A und B liefern beta-B statt eigener alpha-A/beta-B-Werte |
| Fehlendes Transitionziel | Originalcompiler/-initialisierung weist fehlenden Zielzustand zurück |
| Zahlenpayloadvariante | Originalruntime führt sie aus; zusätzliche CEM-basierte Hostprüfung weist öffentlichen Payload ab |
| Anderer öffentlicher Ereignisname | Native Parentzustellung erfolgt; zusätzliche Schnittstellenbindung blockiert undeclarierten DOM-Export |
| Falsch gebundene Parentinstanz | Ereignis kommt bei B an; zusätzliche invokeid-/Instanzregel verhindert falsche öffentliche Zuordnung |
| #_parent ohne Parent | Originalruntime meldet Kommunikationsfehler; keine erfundene öffentliche Zustellung |

**9/10 ursprüngliche Erwartungen erfüllt, Gesamtlauf Exitstatus 1.** Die fehlerhafte Isolationserwartung wurde nicht verändert, gelöscht oder nachträglich als erwartetes Verhalten ausgegeben. Die negativen Varianten ändern ausschließlich den im Fall benannten Originalinput; sie sind als Varianten protokolliert.

Die Parentzustellung verwendet die ursprüngliche send-Implementierung und echte Statechart-Parentinstanzen. customSend/doSend wurden nicht ersetzt. Die Zuordnung parentSession/invokeid wird über die dokumentierten Original-Interpreteroptionen vom Forschungshost gesetzt; dies ist **kein bereits ausgeführter SCXML-invoke-Lebenszyklusnachweis**.

## 3. Datenisolation: Vorbereitung ist eine eigene Instanzgrenze

Die Originaldokumentation beschreibt prepare als Bindung an einen Ausführungskontext. Der Quellpfad erzeugt beziehungsweise nutzt diesen Kontext und evaluiert dort Datamodell und Modellfunktion. Zwei Interpreterkonstruktoren mit **derselben bereits vorbereiteten Modellfunktion** reichen im geprüften Pfad nicht aus, um die Daten zu trennen.

Zwei zusätzliche, separat vor ihrer Ausführung festgelegte Diagnosefälle prüfen die korrekte Grenze:

1. Dieselbe kompilierte Originalquelle, aber **prepare separat für A und B**: alpha-A und beta-B bleiben getrennt.
2. Zusätzlich separate Quellkompilierung je Instanz als Kontrolle: ebenfalls alpha-A und beta-B.

**2/2 Diagnoseerwartungen erfüllt, Exitstatus 0.** Der Browserhost verwendet deshalb den belegten dokumentierten Vorbereitungsschritt je Instanz. Die Ausgangsgrenze bleibt ausdrücklich bestehen; es ist keine allgemeine Garantie aus bloß zwei Statechart-Objekten abgeleitet.

## 4. Tatsächliche Browser-/DOM-Projektion

Die ursprünglichen HTML-/CSS-Dateien und das vorhandene Forschungsprofil aus dem Vier-Domänen-Paket werden wiederverwendet. Zusätzlicher Hostcode bindet native Fokusereignisse an OPEN und synthetische keydown-Ereignisse mit Escape/Enter an CLOSE/COMMIT. Originale onEntry-Meldungen steuern aria-expanded, hidden und den aktiven Optionsverweis. Das sind offen ausgewiesene Forschungsbindungen, keine in SCXML oder CEM bereits standardisierte DOM-Abbildung.

Die native #_parent-Sendung wird zuerst in der echten Original-Parentruntime empfangen. Erst danach prüft der Zusatzhost Ereignisname, erwartete Instanz und den begrenzten öffentlichen Payloadtyp. Der Stringtyp wird aus dem tatsächlichen CEM-TypeScript-Ausdruck abgeleitet; unterstützt ist hier ausdrücklich nur dieser primitive Detailfall. Der Host erzeugt anschließend ein echtes, bubbelndes DOM-CustomEvent. Ziel ist ein **expliziter Forschungs-Sectioncontainer**, kein implementiertes CEM-Custom-Element. Der Host schreibt außerdem den bestätigten Testwert in das Eingabefeld. Es wird keine allgemeine Verbindung von Querytext, aktiver Option und Produktwert erfunden.

| Vorab definierter Browserfall | Beobachtung |
| --- | --- |
| Initialisierung | A/B closed, beide Popups hidden, beide aria-expanded=false |
| Programmatischer Fokus auf A | Nur A open, Popup A sichtbar, aria-expanded A=true, tatsächlicher DOM-Fokus input-a |
| Synthetisches Escape an A | A closed, Popup verborgen, Fokus bleibt input-a |
| Erneuter Fokus und synthetisches Enter an A | selected tatsächlich durchlaufen, A wieder closed; genau ein value-change mit detail.value=alpha an Testcontainer A, keines an B |
| Danach Fokus auf B | Nur B open und aria-expanded B=true; A bleibt closed |

**5/5 Browsererwartungen erfüllt**, keine gemeldeten Runtime-/Bindingfehler im Kontrollhost. Die SCXML-Datei ist unverändert, die Vorbereitung erfolgt je Instanz. Tatsächliche Zustandsfolge, Raw-Parentereignis, DOM-Ereignisdetail und Beobachtungen sind vollständig gespeichert.

## 5. Browserabhängigkeit und Zwischenfehler erhalten

Der erste Browserbootstrap ließ den im Original-README vorgesehenen Polyfill aus. Die unveränderte Distribution meldete deshalb regeneratorRuntime fehlt. Dieser Fehler ist gespeichert; kein Originalbundle wurde gepatcht. Anschließend wurde das Originalpaket @babel/polyfill 7.12.1 exakt gebunden und ebenfalls mit browserseitig erzwungenem SRI geladen. Damit werden die ursprünglichen SCXML-APIs verfügbar und die fünf Hostfälle ausgeführt.

Der Browserkontext wurde während der Arbeit geschlossen. Ein neuer eigener about:blank-Prüftab wurde eingerichtet; bereits gespeicherte Nodefälle wurden deswegen nicht neu gezählt. Die lokale explorative smoke-Probe und Bootstrapdiagnosen bleiben Kontextbelege, keine zusätzlichen benannten Abnahmebedingungen.

Die Originalpakete sind ältere Werkzeuge; Installation meldet unter anderem eine überholte Engineangabe einer Hilfsabhängigkeit. Die gemessene Ausführung belegt nur den gebundenen Node-24.22.1-/Chrome-155-Prüfstand, keine Produktionsfreigabe oder allgemeine Kompatibilitätszusage.

## 6. Nachweisgrenze und offene Arbeit

Dieses Paket ergänzt **17 benannte Bedingungen in drei Gruppen**: 10 ursprüngliche Runtimefälle (einschließlich einer widerlegten Erwartung), zwei separate Vorbereitungsdiagnosen und fünf Browserhostfälle. Keine neue Matrixzelle wird allein wegen der Zahl ausgeführter Bedingungen geschlossen. Die weitergehenden 57 U-Zellen betreffen andere beziehungsweise stärkere Original-/Integrationsanforderungen.

Tatsächlicher SCXML-Interpreter, Parent-send, instanzgetrennte Vorbereitung und begrenzte DOM-Ereignisprojektion sind nun belegt. Weiterhin offen: Navigation und Scroll-to-active, realer invoke-/Unterkomponentenlebenszyklus, asynchrone Ergebnisdaten, dynamische zugängliche Ansagen, native Ziele, vollständige Typabbildung, Roundtrip/Migration und Vertrauens-/Sicherheitsmodell fremder ausführbarer SCXML-Daten. Es wurden nur eigene kontrollierte Testdateien ausgeführt.

Programmatische Fokussierung und **synthetische KeyboardEvents** sind kein Test vertrauenswürdiger physischer Tastatureingaben oder einer Screenreaderinteraktion. Keine vollständige APG-/WCAG-/Assistenzkonformität behauptet. Es gibt eine interaktive Forschungs-Hostfixture mit Zusatzcode, keine Produktionskomponente oder ausgewählte neue Produktsprache. Keine freie Produktentscheidung für variable Zeilenhöhen. Kein Commit oder Push.

## 7. Reproduktion

Im isolierten tool-Ordner npm ci --ignore-scripts verwenden; Paketlock beibehalten. run.cjs führt die zehn Fälle mit originalem SCXML-Paket aus und endet wegen der erhaltenen Isolationserwartung mit Status 1. diagnose.cjs führt die zwei korrekten Vorbereitungspfade aus und endet mit Status 0. Die Runner beziehen Kontrollartefakte über dokumentierte benachbarte Vier-Domänen-Pfade. PROBE_TYPESCRIPT ist hier nicht generell ausgewertet; der TypeScript-Pfad in run.cjs verweist konkret auf den bereits gebundenen 5.9.3-Vorgängerordner.

Für den Browser einen eigenen leeren Prüftab wählen, bootstrap.js mit festem Polyfill-/SCXML-SRI ausführen, dann browser-run.js. Historische Page-ID in bootstrap-initial.js ist Teil des Ausgangsversuchs; aktuelle Skripte wählen einen eigenen about:blank-Tab. Eigene Funktionen, Inputs, Erwartungen und Outputs sind enthalten. Originalbibliotheken/-schemas werden nicht mitverteilt. Quellen-/Paketmanifeste enthalten die exakten Hashes und Versionen.
