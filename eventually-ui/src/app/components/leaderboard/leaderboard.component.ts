import { Component, OnInit } from '@angular/core';
import { ApiserviceService } from '../../shared/apiservice.service';

@Component({
  selector: 'app-leaderboard',
  templateUrl: './leaderboard.component.html',
  styleUrls: ['./leaderboard.component.css']
})
export class LeaderboardComponent implements OnInit {

  eventList = [];
  backgroundColorList = ['aliceblue', 'antiquewhite', 'azure', 'beige', 'aliceblue', 'antiquewhite', 'azure', 'beige'];

  constructor(private apiService: ApiserviceService) { }

  ngOnInit(): void {
    this.fetchEvents();
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

}
