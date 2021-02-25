import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ApiserviceService } from '../../../shared/apiservice.service';
import {Subject} from 'rxjs';
import {debounceTime} from 'rxjs/operators';
import {NgbAlert} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-create-events',
  templateUrl: './create-events.component.html',
  styleUrls: ['./create-events.component.css'],

})
export class CreateEventsComponent implements OnInit {
  private _success = new Subject<string>();
  title;
  desc;
  eventStartDate: Date;
  eventEndDate: Date;
  regStartDate: Date;
  regEndDate: Date;
  maxUser;
  minUser;
  location;
  acceptFileType;
  acceptFileVideo: boolean;

  staticAlertClosed = false;
  successMessage = '';

  @ViewChild('staticAlert', {static: false}) staticAlert: NgbAlert;
  @ViewChild('selfClosingAlert', {static: false}) selfClosingAlert: NgbAlert;

  constructor(private router: Router, private apiService: ApiserviceService) {

  }

  ngOnInit(): void {
  }

  routeToEvent() {
    this.router.navigate(['/events']);
  }


  convertDate(value) {
    let dateStr = '';
    for (var key in value) {
      if (value.hasOwnProperty(key)) {
        if (key === 'year') {
          dateStr = value[key];
        } else {
          dateStr = dateStr + '-' + value[key];
        }
      }

    }
    const time = dateStr + " " + '10:00:00';
    return time;
  }

  save() {
    console.log("Titile", this.title);
    console.log("Desc", this.desc);
    console.log("event start", this.eventStartDate);
    console.log("event End", this.eventEndDate);
    console.log("event Reg", this.regStartDate);
    console.log("event Reg end", this.regEndDate);
    console.log("max user", this.maxUser);
    console.log("min user", this.minUser);
    console.log("Location", this.location);
    console.log("accept file type", this.acceptFileType);
    console.log("accept video", this.acceptFileVideo);

    const eventStartDateFormat = this.convertDate(this.eventStartDate);
    const eventEndDateFormat = this.convertDate(this.eventEndDate);
    const regStartDateFormat = this.convertDate(this.regStartDate);
    const regEndDateFormat = this.convertDate(this.regEndDate);


    let obj = {
      "title": this.title,
      "description": this.desc,
      "event_start_date": eventStartDateFormat,
      "event_end_date": eventEndDateFormat,
      "reg_start_date": regStartDateFormat,
      "reg_end_date": regEndDateFormat,
      "max_user": parseInt(this.maxUser),
      "min_user": parseInt(this.minUser),
      "location": this.location,
      "accept_file_type": this.acceptFileType,
      "accept_video_file": this.acceptFileVideo
    }

    this.apiService.addUsingObject('event', obj).subscribe(
      res => {

        setTimeout(() => new this.staticAlert.close(), 20000);

        this._success.subscribe(message => this.successMessage = message);
        this._success.pipe(debounceTime(5000)).subscribe(() => {
          if (this.selfClosingAlert) {
            new this.selfClosingAlert.close();
          }
        });
        setTimeout(t => {
          this.routeToEvent();
        }, 3000);
      },
      err => {
        // this.toastMsg.createToast({ severity: 'error', summary: 'Failed', detail: err['error']['message'] });
      }
    );

  }

}
