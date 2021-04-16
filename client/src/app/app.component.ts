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

  public playerData;// this.getPlayerData();
  public testData;
  public authData = {'loggingIn' : true};
  
  constructor(
    private authService: AuthService,
    private gameLogicService: GameLogicService
  ) {
    this.playerData = this.gameLogicService.getPlayerData();
    this.testData = this.gameLogicService.testPost();
  }

  ngOnInit() {
    //this.playerData = this.getPlayerData();
  }
}
