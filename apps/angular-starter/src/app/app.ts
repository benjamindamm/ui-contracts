import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <main>
      <p class="eyebrow">Anwendungswerkstatt</p>
      <h1>Angular-Starter</h1>
      <p>Lokale Vorschau mit einer interaktiven Angular-Komponente.</p>

      <p role="status">Zählerstand: <strong>{{ count() }}</strong></p>
      <div class="actions">
        <button type="button" (click)="increment()">Zähler erhöhen</button>
        <button type="button" (click)="reset()">Zurücksetzen</button>
      </div>
    </main>
  `,
})
export class App {
  protected readonly count = signal(0);

  protected increment(): void {
    this.count.update((value) => value + 1);
  }

  protected reset(): void {
    this.count.set(0);
  }
}
