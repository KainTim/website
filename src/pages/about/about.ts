import { Component } from '@angular/core';
import { CardComponent } from '../../components/card/card';

export interface Pillar {
  title: string;
  description: string;
}

@Component({
  selector: 'app-about',
  imports: [CardComponent],
  templateUrl: './about.html',
  styleUrl: './about.css',
})
export class About {
  readonly pillars: Pillar[] = [
    {
      title: 'Angular UI',
      description:
        'Component-driven interfaces with a strong focus on clarity, speed, and accessibility.',
    },
    {
      title: 'C# Backend',
      description:
        'Reliable APIs and services shaped with clean architecture and maintainable domain logic.',
    },
    {
      title: 'Flutter Mobile',
      description: 'Polished mobile apps with shared design systems and a smooth native feel.',
    },
  ];

  readonly values: string[] = [
    'Ship practical features with a thoughtful product mindset.',
    'Keep the codebase simple, testable, and easy to evolve.',
    'Balance visual polish with performance and real-world usability.',
  ];
}

export {};

