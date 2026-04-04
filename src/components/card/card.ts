import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-card',
  imports: [],
  templateUrl: './card.html',
  styleUrl: './card.css',
  host: {
    '[class]': 'hostClassName',
  },
})
export class CardComponent {
  @Input() cardClass = '';

  get hostClassName(): string {
    return this.cardClass ? `card ${this.cardClass}` : 'card';
  }
}

