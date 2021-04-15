import { Component, Input, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  public newPlayer = true;
  public secretCode = "";

  @Input() authData;

  constructor(private modalService: NgbModal, private http: HttpClient) { }

  public open(content) {
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title' }).result.then((result) => {

    }, (reason) => {
      console.log(this.authData['loggingIn']);
      this.authData['loggingIn'] = false;
      console.log(this.authData['loggingIn']);
    });
  }

  getPlayerData() {
    const url = 'http://localhost:4999/placer/login';
    this.http.post(url, {'secretCode' : this.secretCode}, { responseType: 'json' as const }).subscribe((res) => {
      if(res['error'] == null){
        this.authData = res
      }
    })
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
