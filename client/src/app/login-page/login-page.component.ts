import { Component, Input, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  public newPlayer = true;
  public secretCode = "";

  @Input() authData;

  constructor(private modalService: NgbModal) { }

  public open(content) {
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title' }).result.then((result) => {

    }, (reason) => {
      console.log(this.authData['loggingIn']);
      this.authData['loggingIn'] = false;
      console.log(this.authData['loggingIn']);
    });
  }

  ngOnInit(): void {

  }

  newPlayerClick(newPlayerModal): void {
    this.secretCode = "12345678-1234-1234-1234-1234567890ab";
    this.open(newPlayerModal);
  }

  attemptLogin(): void {

  }

}
