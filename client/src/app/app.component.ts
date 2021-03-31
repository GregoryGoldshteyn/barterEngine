import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ThrowStmt } from '@angular/compiler';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'client';
  public playerData;// this.getPlayerData();
  public testData;
  constructor(private http: HttpClient) {
    this.getPlayerData();
    this.testPost();
  }

  getPlayerData(){
    const url = 'http://localhost:5000/player/0';
    this.http.get(url, {responseType: 'json' as const}).subscribe((res) => {
      this.playerData = res
    })
  }

  testPost(){
    this.makeTrade("0","1","2");
  }

  makeTrade(playerId, tradeId, storyId){
    const url = 'http://localhost:4999/makeTrade';
    this.http.post(url, { "playerId": playerId, "tradeId": tradeId, "storyId": storyId }, { responseType: 'json' as const }).subscribe((res) => {
      this.testData = res
    })
  }

  ngOnInit() {
    //this.playerData = this.getPlayerData();
  }
}
