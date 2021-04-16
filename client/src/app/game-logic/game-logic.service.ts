import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GameLogicService {

  constructor(private http: HttpClient) { }

  public getPlayerData() {
    const url = 'http://localhost:4999/placer/player/0';
    this.http.get(url, { responseType: 'json' as const }).subscribe((res) => {
      return res;
    })
  }

  public testPost() {
    this.makeTrade("0", "1", "2");
  }

  private makeTrade(playerId, tradeId, storyId) {
    const url = 'http://localhost:4999/makeTrade';
    this.http.post(url, { "playerId": playerId, "tradeId": tradeId, "storyId": storyId }, { responseType: 'json' as const }).subscribe((res) => {
      return res
    })
  }
}
