import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';

import { ComponentsComponent } from './components/components.component';
import { LandingComponent } from './examples/landing/landing.component';
import { LoginComponent } from './examples/login/login.component';
// import { ProfileComponent } from './examples/profile/profile.component';
import { EventsComponent } from './components/events/events.component';
import { CreateEventsComponent } from './components/events/create-events/create-events.component'
import { ProfileComponent} from './components/profile/profile.component'
import { NucleoiconsComponent } from './components/nucleoicons/nucleoicons.component';
import { RegisterComponent } from './components/events/register/register.component';
import { LeaderboardComponent } from './components/leaderboard/leaderboard.component';
import { NotificationComponent } from './components/notification/notification.component';

const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'login', component: LoginComponent },
    { path: 'home', component: ComponentsComponent },
    { path: 'register', component: RegisterComponent },
    { path: 'leaderboard', component: LeaderboardComponent },
    { path: 'notifications', component: NotificationComponent },
    { path: 'nucleoicons', component: NucleoiconsComponent },
    { path: 'examples/landing', component: LandingComponent },
    { path: 'examples/login', component: LoginComponent },
    // { path: 'examples/profile', component: ProfileComponent },
    { path: 'events', component: EventsComponent },
    { path: 'profile', component: ProfileComponent },
    { path: 'createEvent', component: CreateEventsComponent },
];

@NgModule({
    imports: [
        CommonModule,
        BrowserModule,
        RouterModule.forRoot(routes)
    ],
    exports: [
    ],
})
export class AppRoutingModule { }
