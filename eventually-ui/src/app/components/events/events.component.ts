import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Globals } from '../../shared/global';
import { ApiserviceService} from '../../shared/apiservice.service'

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css'],
  providers: [Globals]
})
export class EventsComponent implements OnInit {
  eventList = [];
  expandEvent = false;
  selectedEvent = {};

  constructor(private router: Router, public globals: Globals, private apiService: ApiserviceService) { }

  ngOnInit(): void {
    this.fetchEvents();
  }

  activeEvents(n) {
    return n;
  }

  routeToCreateEvent() {
    this.router.navigate(['/createEvent']);
  }

  fetchEvents() {
      this.apiService.getApi('event').subscribe(
          resp => {
              this.eventList = resp;
          }, err => {
              console.log('eRROR :::::', err);
          }
      )
  }

  viewEvent(e) {
    this.expandEvent = true;
    this.selectedEvent = e;
    console.log('Selected Event:::', this.selectedEvent)
  }

  backtoevents() {
    this.expandEvent = false;
  }

}
