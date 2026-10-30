# Reparatur SELECTION-02-b · Revision 01

Bezug: SEL2-B01 aus dem vom Koordinator gemeldeten Browserlauf. Die Erstlieferung unter `outputs/b` bleibt eingefroren.

## Minimale Änderung

Der focusout-Handler am Picker prüft jetzt `relatedTarget`. Liegt das Fokusziel innerhalb des Pickers, bleibt er offen. Dadurch wird der interne Wechsel vom Suchfeld zum Schließen-Button nicht wegen eines vorübergehenden `document.activeElement === BODY` als Verlassen behandelt. Bei einem externen oder fehlenden Fokusziel schließt er ohne Auswahländerung. Escape-, Commit- und explizite Schließen-Handler bleiben unverändert und stellen Triggerfokus her.

`index.html`, `styles.css`, `decision.json` und `FONT-LICENSE.txt` wurden bytegleich übernommen. Nur der relevante Handler in `form.ts` wurde geändert; `form.js` wurde neu kompiliert. Definitions- und Policydateien wurden nicht geändert.

## Tatsächlich ausgeführte Prüfung

Gepinnter TypeScript-Compiler mit `--target ES2020 --lib ES2020,DOM --strict`: Exit 0. Kompiliertes JS auf den neuen relatedTarget-Guard zurückgelesen. Hashvergleich der vier unverändert übernommenen Dateien erfolgreich. Dateien und Hashes in TRACE.json.

Kein eigener Browser- oder Screenreaderlauf für diese Reparatur. Die ursprüngliche Fehlerbeobachtung stammt vom Koordinator; die Browser-Nachprüfung übernimmt der Koordinator. Die Reparatur stellt keine allgemeine Fokus- oder Barrierefreiheitsfreigabe dar.
