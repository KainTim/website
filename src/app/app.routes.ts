import { Routes } from '@angular/router';
import { AboutComponent } from '../pages/about/about.component';
import { Contact } from '../pages/contact/contact';
import { Home } from '../pages/home/home';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: Home },
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: Contact },
];
