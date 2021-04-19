import { Component, Input, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  public newPlayer = true;
  public secretCode = "";

  @Input() authData;

  constructor(private modalService: NgbModal, private authService: AuthService) { 
    
  }

  public open(content) {
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title' }).result.then((result) => {

    }, (reason) => {

    });
  }

  attemptLogin() {
    this.authService.login(this.secretCode).subscribe((res) => {
      if (res['Error'] == null) {
        this.authData['loggedIn'] = true;
        this.authService.setSession(res);
      }
      else {

      }
    });
  }

  ngOnInit(): void {
    if (this.authService.isLoggedIn()) {
      this.authData['loggedIn'] = true;
    }
    else {
      this.authData['loggedIn'] = false;
    }
  }

  newPlayerClick(newPlayerModal): void {
    this.secretCode = "12345678-1234-1234-1234-1234567890ab";
    this.open(newPlayerModal);
  }
}
