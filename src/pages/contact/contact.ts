import { Component } from '@angular/core';
import { CardComponent } from '../../components/card/card';

interface Channel {
  label: string;
  value: string;
  href?: string;
}

@Component({
  selector: 'app-contact',
  imports: [CardComponent],
  templateUrl: './contact.html',
  styleUrl: './contact.css',
})
export class Contact {
  readonly channels: Channel[] = [
    {
      label: 'Email',
      value: 'alex.carter.dev@mail.com',
      href: 'mailto:alex.carter.dev@mail.com',
    },
    {
      label: 'Location',
      value: 'Remote / UTC+2',
    },
    {
      label: 'Availability',
      value: 'Open to freelance and full-time roles',
    },
  ];
}
