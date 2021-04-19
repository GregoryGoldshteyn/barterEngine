import { Component, Input, OnInit } from '@angular/core';
import { GameLogicService } from '../game-logic/game-logic.service';

@Component({
  selector: 'app-game-container',
  templateUrl: './game-container.component.html',
  styleUrls: ['./game-container.component.css']
})
export class GameContainerComponent implements OnInit {

  public gameData;

  @Input() playerData;
  
  constructor(public gameLogicService: GameLogicService) { }

  ngOnInit(): void {
    this.gameLogicService.getGameData(this.playerData['playerId']).subscribe(res => {
      this.gameData = res;
    })
  }

}
