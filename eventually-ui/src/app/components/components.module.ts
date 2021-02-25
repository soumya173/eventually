import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { JwBootstrapSwitchNg2Module } from 'jw-bootstrap-switch-ng2';
import { NouisliderModule } from 'ng2-nouislider';
import { NgxSimpleCountdownModule } from 'ngx-simple-countdown';
import { DropdownModule } from 'primeng/dropdown';
import { BasicelementsComponent } from './basicelements/basicelements.component';
import { ComponentsComponent } from './components.component';
import { CreateEventsComponent } from './events/create-events/create-events.component';
import { EventsComponent } from './events/events.component';
import { NgbdModalBasic } from './modal/modal.component';
import { NavigationComponent } from './navigation/navigation.component';
import { NotificationComponent } from './notification/notification.component';
import { NucleoiconsComponent } from './nucleoicons/nucleoicons.component';
import { ProfileComponent } from './profile/profile.component';
import { TypographyComponent } from './typography/typography.component';
import { CountDownTimerComponent } from './count-down-timer/count-down-timer.component';
import { RegisterComponent } from './events/register/register.component';


@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        NgbModule,
        NouisliderModule,
        RouterModule,
        JwBootstrapSwitchNg2Module,
        ReactiveFormsModule,
        DropdownModule,
        NgxSimpleCountdownModule
      ],
    declarations: [
        ComponentsComponent,
        BasicelementsComponent,
        NavigationComponent,
        TypographyComponent,
        NucleoiconsComponent,
        NotificationComponent,
        NgbdModalBasic,
        EventsComponent,
        ProfileComponent,
        CreateEventsComponent,
        CountDownTimerComponent,
        RegisterComponent,
    ],
    exports:[ ComponentsComponent ]
})
export class ComponentsModule { }
