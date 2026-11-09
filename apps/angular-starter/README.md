# Angular-Starter

Diese Infrastrukturprobe nutzt eine Angular-Komponente mit einem Zähler. Sie ist bibliotheksfrei.

Für Angular 22.2 unterstützt dieses Projekt Node.js 22 ab 22.22.3, Node.js 24 ab 24.15.0 oder Node.js 26. Lokal mit Node.js 24.19.0 und npm 11.17.0 geprüft. [Offizielle Kompatibilitätstabelle](https://angular.dev/reference/versions#actively-supported-versions)

Aus dem Repository-Stamm:

```sh
cd apps/angular-starter
npm ci
npm start
```

Die Vorschau läuft unter [http://127.0.0.1:4200/](http://127.0.0.1:4200/) parallel zum [HTML-Starter auf Port 8765](http://127.0.0.1:8765/). „Zähler erhöhen“ erhöht den Wert um 1. „Zurücksetzen“ stellt den Startwert 0 wieder her. Mit Strg+C den Server beenden. Wenn Port 4200 belegt ist, zum Beispiel `npm start -- --port 4201` verwenden und die URL entsprechend anpassen.

`npm run build` erstellt den Produktionsbuild in `dist/angular-starter/browser/`.
