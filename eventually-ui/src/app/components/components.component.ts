import { Component, OnInit, Renderer2, OnDestroy } from '@angular/core';
import { NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { NgbAccordionConfig } from '@ng-bootstrap/ng-bootstrap';
import * as Rellax from 'rellax';
import { ApiserviceService } from '../shared/apiservice.service'
import { Router } from '@angular/router';

@Component({
    selector: 'app-components',
    templateUrl: './components.component.html',
    styles: [`
    ngb-progressbar {
        margin-top: 5rem;
    }
    `]
})

export class ComponentsComponent implements OnInit, OnDestroy {
    data: Date = new Date();
    date: {year: number, month: number};
    model: NgbDateStruct;

    public isCollapsed = true;
    public isCollapsed1 = true;
    public isCollapsed2 = true;

    // Eventually variables
    eventList = [];
    topEvents = [];
    backgroundColorList = ['aliceblue', 'antiquewhite', 'azure', 'beige'];

    state_icon_primary = true;

    constructor( private renderer: Renderer2,
        config: NgbAccordionConfig,
        private apiService: ApiserviceService) {
        config.closeOthers = true;
        config.type = 'info';
    }
    isWeekend(date: NgbDateStruct) {
        const d = new Date(date.year, date.month - 1, date.day);
        return d.getDay() === 0 || d.getDay() === 6;
    }

    isDisabled(date: NgbDateStruct, current: {month: number}) {
        return date.month !== current.month;
    }

    ngOnInit() {
      var rellaxHeader = new Rellax('.rellax-header');

        var navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.add('navbar-transparent');
        var body = document.getElementsByTagName('body')[0];
        body.classList.add('index-page');
        this.fetchEvents();
    }
    ngOnDestroy(){
        var navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.remove('navbar-transparent');
        var body = document.getElementsByTagName('body')[0];
        body.classList.remove('index-page');
    }

    fetchEvents() {
        this.apiService.getApi('event').subscribe(
            resp => {
                this.eventList = resp;
                this.setTopEvents(this.eventList);
            }, err => {
                console.log('eRROR :::::', err);
            }
        )
    }
    setTopEvents(eventList: any[]) {
        if (eventList.length) {
            if (eventList.length > 3) {
                return this.topEvents = eventList.slice(0, 3);
            } else {
                return this.topEvents = eventList
            }
        }
        return this.topEvents = [];
    }

}
