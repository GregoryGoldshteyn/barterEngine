import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ThrowStmt } from '@angular/compiler';
import { AuthService } from './auth/auth.service';
import { GameLogicService } from './game-logic/game-logic.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'client';
  
  public playerData = {'loggedIn' : false};
  
  constructor(
    private authService: AuthService,
    private gameLogicService: GameLogicService
  ) {
    
  }

  ngOnInit() {
    if (this.authService.isLoggedIn()) {
      this.playerData['loggedIn'] = true;
    }
    else {
      this.playerData['loggedIn'] = false;
    }
  }
}
