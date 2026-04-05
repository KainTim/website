import { Component } from '@angular/core';
import { CardComponent } from '../../components/card/card';

interface Channel {
  label: string;
  value: string;
  href?: string;
  hrefLabel?: string;
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
      value: 'tikaiz@gmx.at',
      href: 'mailto:tikaiz@gmx.at',
      hrefLabel: 'Send an email',
    },
    {
      label: 'Location',
      value: 'Remote / UTC+1',
    },
    {
      label: 'Availability',
      value: 'Open to freelance and full-time roles',
    },
  ];

  protected gotoHref(href: string) {
    window.location.href = href;
  }
}
