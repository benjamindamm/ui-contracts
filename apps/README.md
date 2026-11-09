# Anwendungswerkstatt

Hier entstehen ausführbare Anwendungen für direktes Feedback im Browser. Jede App liegt in einem eigenen Ordner unter `apps/`. [Agentenanleitung](AGENTS.md)

## Lokale Vorschau

Für den HTML-Starter genügt Python 3. Aus dem Repository-Stamm starten:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory apps/html-smoke
```

Im Browser [http://127.0.0.1:8765/](http://127.0.0.1:8765/) öffnen und „Zähler erhöhen“ betätigen. Der sichtbare Zähler beginnt bei 0 und steigt pro Betätigung um 1. Nach Dateiänderungen die Seite neu laden. Falls der Port belegt ist, im Befehl und in der URL dieselbe freie Portnummer verwenden. Mit Strg+C den Server beenden.

Der [HTML-Starter](html-smoke/index.html) ist eine Infrastrukturprobe ohne Bibliotheksbindung. Für weitere statische Apps den eigenen App-Ordner als Dokumentwurzel angeben. React- und Angular-Apps verwenden ihren jeweils im App-Ordner dokumentierten Startbefehl und die dort angegebene lokale URL.

Der [Angular-Starter](angular-starter/README.md) läuft auf [Port 4200](http://127.0.0.1:4200/) und kann parallel zur HTML-Vorschau auf Port 8765 gestartet werden.

## Weiteres Projekt hinzufügen

Lege die App als Geschwisterordner unter `apps/<name>/` an. Gib Node-Projekten jeweils eine eigene `package.json` und Lockdatei. Führe Installation, Start und Build im jeweiligen Projektordner aus. Dokumentiere dort die Voraussetzungen, die Befehle und einen eigenen lokalen Port, damit mehrere Vorschauen parallel laufen können.

Für profilgebundene Contract-Prüffälle gibt es den separaten [Web-Prüfhost](../tools/web/README.md).
