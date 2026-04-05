import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CardComponent } from '../../components/card/card';

interface Skill {
  name: string;
  category: 'Frontend' | 'Backend' | 'Mobile' | 'Cloud' | 'Frontend / Backend';
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
    intro: 'I build polished web, backend, and mobile products with Angular, C#, and Flutter.',
    focus: 'Focused on performance, clean architecture, and product-minded delivery.',
  };

  readonly skills: Skill[] = [
    { name: 'Angular', category: 'Frontend', level: 'Advanced' },
    { name: 'React', category: 'Frontend', level: 'Advanced' },
    { name: 'Ionic', category: 'Frontend', level: 'Advanced' },
    { name: 'TypeScript', category: 'Frontend / Backend', level: 'Advanced' },
    { name: 'Javascript', category: 'Frontend / Backend', level: 'Advanced' },
    { name: 'Express', category: 'Backend', level: 'Advanced' },
    { name: 'C# / .NET', category: 'Frontend / Backend', level: 'Advanced' },
    { name: 'ASP.NET Core', category: 'Backend', level: 'Advanced' },
    { name: 'WPF', category: 'Frontend', level: 'Advanced' },
    { name: 'Java', category: 'Backend', level: 'Advanced' },
    { name: 'Spring Boot', category: 'Backend', level: 'Advanced' },
    { name: 'Flutter', category: 'Mobile', level: 'Advanced' },
  ];

  readonly projects: Project[] = [
    {
      title: 'Tasktimer',
      description:
        'Jira time-tracking app with custom reporting and connectivity, build for mobile and web.',
      stack: ['Ionic', 'React', 'Spring Boot', 'Oracle', 'Web', 'Android', 'iOS'],
      impact:
        'Led backend and architectural work: implemented Spring Boot backend, database access for Oracle with reporting capabilities, including reliable Jira connectivity.',
    },
    {
      title: 'Synopsis Platform Core',
      description: 'Main Synopsis Platform codebase (backend + frontend pieces).',
      stack: ['C#', 'TypeScript', 'HTML', 'Docker', 'Web'],
      impact:
        'Contributed via issues, code and investigations (plugin-loader, microfrontend research), influencing platform direction and stability.',
    },
    {
      title: 'Website SV Hofkirchen (Chess Club)',
      description: 'Club management web app for the SV Hofkirchen chess club.',
      stack: ['C#', '.NET', 'Blazor', 'SQLite', 'Web'],
      impact:
        'Designed the technical core across backend, database, and Blazor UI: implemented backend services, and partially built the Blazor frontend',
    },
  ];

  readonly timeline: TimelineItem[] = [
    {
      role: 'Internship - Backend & Architecture Engineer',
      company: 'Industrie Informatik GmbH',
      period: '2025',
      highlights: [
        'Implemented a Spring Boot API for the Tasktimer Application including database access and reporting capabilities.',
        'Designed and implemented a reliable Jira connectivity solution for the Tasktimer backend, ensuring consistent data synchronization and performance.',
        'Contributed to architectural discussions and decisions, influencing the overall direction and stability of the Tasktimer application.',
      ],
    },
  ];
}
