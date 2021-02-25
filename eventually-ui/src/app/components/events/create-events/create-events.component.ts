import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-events',
  templateUrl: './create-events.component.html',
  styleUrls: ['./create-events.component.css'],

})
export class CreateEventsComponent implements OnInit {
  title;
  desc;
  eventStartDate:Date;
  eventEndDate:Date;
  regStartDate:Date;
  regEndDate:Date;
  maxUser:number;
  minUser:number;
  location;
  acceptFileType;
  acceptFileVideo:boolean;

  constructor(private router: Router) {

  }

  ngOnInit(): void {
  }

  save(){
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
  }

}
