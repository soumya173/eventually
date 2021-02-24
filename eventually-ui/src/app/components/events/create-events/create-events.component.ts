import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-events',
  templateUrl: './create-events.component.html',
  styleUrls: ['./create-events.component.css'],

})
export class CreateEventsComponent implements OnInit {
  createEventForm: FormGroup;
  frequencyOptions = []


  constructor(public fb: FormBuilder) {
    this.frequencyOptions = [
      { label: 'Hourly', value: 'Hourly' },
      { label: 'Daily', value: 'Daily' },
      { label: 'Weekly', value: 'Weekly' },
      { label: 'Monthly', value: 'Monthly' },
      { label: 'Yearly', value: 'Yearly' }
  ];
   }

  ngOnInit(): void {
    this.buildCreateEventForm();
  }

  buildCreateEventForm() {
		this.createEventForm = this.fb.group({
			title: ['', [Validators.required]],
      desc: ['', [Validators.required]],
		});
	}

}
