import { Component, OnInit } from '@angular/core';
import { ApiserviceService } from '../../../shared/apiservice.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  eventList = [];
  userList = [];
  eventSelected: String = '';
  selectedUsers = [];
  teamName: String = '';
  selectedUsersName = [];
  eventname: String = '';
  showTeams = true;
  myTeams = [];
  cardObj = {};

  constructor(private apiService: ApiserviceService) { }

  ngOnInit(): void {
    this.fetchEvents();
    this.fetchUsers();
    setTimeout(()=>this.fetchMyTeams(),2000);
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

  fetchUsers() {
    this.apiService.getApi('user').subscribe(
      resp => {
          this.userList = resp;
      }, err => {
          console.log('eRROR :::::', err);
      }
    )
  }

  selectedEvent(e) {
    this.eventSelected = e.id;
    this.eventname = e.title;
  }

  usersSelected(e) {
    this.selectedUsers.push(e.id);
    this.selectedUsersName.push(e.name);
  }

  register() {
    const obj = {
        'event_id': this.eventSelected,
        'user_ids': this.selectedUsers,
        'name': this.teamName,
        'reward_id': 1,
        'lead_user_id': 5,
        'id': 0,
        'type': 'participant'
      };
    this.apiService.addUsingObject('team', obj).subscribe(
      resp => {
          this.userList = resp;
          alert('Team Created!!!');
          this.eventSelected = '';
          this.selectedUsers = [];
          this.teamName = '';
          this.selectedUsersName = [];
          this.eventname = '';
      }, err => {
          console.log('eRROR :::::', err);
      }
    )
  }

  togglePage(val) {
    this.showTeams = val;
  }

  fetchMyTeams() {
    this.apiService.getApi('team').subscribe(
      resp => {
        // this.myTeams = resp;
        resp.forEach((team, i) => {
          let cardObj = {};
          cardObj['name'] = team.name;
          for (const user of this.userList) {
            if (user.id === team.lead_user_id) {
              cardObj['leader'] = user.name;
            }
          }
          let services = team.user_ids;
          services = services.split(',');
          services[0] = services[0].substring(1);
          services[services.length - 1] = services[services.length - 1].substring(
            0,
            services[services.length - 1].length - 1
          );
          services.forEach((x, i) => {
            services[i] = services[i].includes('"') ? services[i].replaceAll('"', "").trim()
              : services[i].replaceAll("'", "").trim();
          });
          const arr = [];
          console.log(services );
          for (const id of services) {
            for (const user of this.userList) {
              if (user.id == id) {
                arr.push(user.name);
                cardObj['teammates'] = arr;
              }
            }
          }
          this.myTeams.push(cardObj);
          console.log('card waale:::::::', cardObj)
        });
      }, err => {
          console.log('eRROR :::::', err);
      }
    )
  }
}
