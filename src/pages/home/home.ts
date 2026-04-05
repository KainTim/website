import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CardComponent } from '../../components/card/card';

interface Skill {
  name: string;
  category: 'Frontend' | 'Backend' | 'Mobile' | 'Cloud';
  level: string;
}

interface Project {
  title: string;
  description: string;
  stack: string[];
  impact: string;
}

interface TimelineItem {
  role: string;
  company: string;
  period: string;
  highlights: string[];
}

@Component({
  selector: 'app-home',
  imports: [RouterLink, CardComponent],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {
  readonly hero = {
    name: 'Tim Kainz',
    role: 'Fullstack Developer',
    intro:
      'I build polished web, backend, and mobile products with Angular, C#, and Flutter.',
    focus: 'Focused on performance, clean architecture, and product-minded delivery.',
  };

  readonly skills: Skill[] = [
    { name: 'Angular', category: 'Frontend', level: 'Advanced' },
    { name: 'TypeScript', category: 'Frontend', level: 'Advanced' },
    { name: 'C# / .NET', category: 'Backend', level: 'Advanced' },
    { name: 'REST APIs', category: 'Backend', level: 'Advanced' },
    { name: 'Flutter', category: 'Mobile', level: 'Advanced' },
    { name: 'Firebase', category: 'Cloud', level: 'Intermediate' },
  ];

  readonly projects: Project[] = [
    {
      title: 'ClinicFlow Platform',
      description: 'Patient scheduling and billing dashboard for multi-location clinics.',
      stack: ['Angular', 'C#', '.NET API', 'PostgreSQL'],
      impact: 'Reduced booking mistakes by 38% and improved team response speed.',
    },
    {
      title: 'FieldOps Mobile App',
      description: 'Offline-first mobile app for technicians to manage service tasks.',
      stack: ['Flutter', 'C#', 'SQLite', 'Azure Functions'],
      impact: 'Enabled same-day job updates even in low-connectivity zones.',
    },
    {
      title: 'Insights Portal',
      description: 'Real-time analytics workspace with modular report widgets.',
      stack: ['Angular', 'SignalR', 'C#', '.NET'],
      impact: 'Cut reporting time from hours to minutes for operations teams.',
    },
  ];

  readonly timeline: TimelineItem[] = [
    {
      role: 'Senior Fullstack Developer',
      company: 'Northline Digital',
      period: '2023 - Present',
      highlights: [
        'Led Angular frontend redesign for enterprise dashboard products.',
        'Built C# microservices and optimized API response times by 30%.',
      ],
    },
    {
      role: 'Software Engineer',
      company: 'CloudMotion Labs',
      period: '2020 - 2023',
      highlights: [
        'Delivered Flutter apps with shared design system and CI pipelines.',
        'Developed secure backend services with clean architecture patterns.',
      ],
    },
  ];
}
