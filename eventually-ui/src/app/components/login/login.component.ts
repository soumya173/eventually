import { Component, OnInit, ViewEncapsulation, ViewChild } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Globals } from '../../shared/global'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  encapsulation: ViewEncapsulation.None,
  providers: [Globals]
})
export class LoginComponent implements OnInit {

  closeResult: string;
  @ViewChild('content') content;

    constructor(private modalService: NgbModal, public globals: Globals) {}

    ngOnInit() {
      this.khulja();
    }

    khulja() {
        this.modalService.open(this.content, { size: 'sm' })
    }

    open(content, type) {
        if (type === 'sm') {
            console.log('aici');
            this.modalService.open(this.content, { size: 'sm' }).result.then((result) => {
                this.closeResult = `Closed with: ${result}`;
            }, (reason) => {
                this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
            });
        } else {
            this.modalService.open(this.content).result.then((result) => {
                this.closeResult = `Closed with: ${result}`;
            }, (reason) => {
                this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
            });
        }
    }

    private getDismissReason(reason: any): string {
        if (reason === ModalDismissReasons.ESC) {
            this.globals.loginFlag = false;
            return 'by pressing ESC';
        } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
            this.globals.loginFlag = false;
            return 'by clicking on a backdrop';
        } else {
          this.globals.loginFlag = false;
            return  `with: ${reason}`;
        }
    }
}

