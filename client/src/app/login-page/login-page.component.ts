import { Component, Input, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth/auth.service';
import { GameLogicService } from '../game-logic/game-logic.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  public newPlayer = true;
  public secretCode = "";

  @Input() playerData;
  @Input() gameData;

  constructor(private modalService: NgbModal, private authService: AuthService, private gameLogicService: GameLogicService) { 
    
  }

  public open(content) {
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title' }).result.then((result) => {

    }, (reason) => {

    });
  }

  attemptLogin() {
    this.authService.login(this.secretCode).subscribe((res) => {
      if (res['Error'] == null) {
        this.playerData['playerId'] = this.secretCode;
        this.authService.setSession(res);
        this.playerData['loggedIn'] = true; // Do last, since this component will be disabled on logged in
      }
      else {

      }
    });
  }

  ngOnInit(): void {
    
  }

  newPlayerClick(newPlayerModal): void {
    this.secretCode = "12345678-1234-1234-1234-1234567890ab";
    this.open(newPlayerModal);
  }
}
