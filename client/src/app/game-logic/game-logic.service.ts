import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GameLogicService {

  constructor(private http: HttpClient) { }

  public getPlayerData() : Observable<any> {
    const url = 'http://localhost:4999/placer/player/0';
    return this.http.get(url, { responseType: 'json' as const });
  }

  public testPost(): Observable<any> {
    return this.makeTrade("0", "1", "2");
  }

  private makeTrade(playerId, tradeId, storyId) : Observable<any> {
    const url = 'http://localhost:4999/makeTrade';
    return this.http.post(url, { "playerId": playerId, "tradeId": tradeId, "storyId": storyId }, { responseType: 'json' as const });
  }
}
