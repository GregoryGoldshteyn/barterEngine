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
    
  }

  getPlayerData() {
    this.gameLogicService.getPlayerData().subscribe(
      res => this.playerData = res
    );
  }

  getTestData() {
    this.gameLogicService.testPost().subscribe(
      res =>  this.testData = res
    );
  }

  ngOnInit() {
    this.getPlayerData();
    this.getTestData();
  }
}
