import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'client';
  public playerData = {};
  constructor(private http: HttpClient) {
    this.getPlayerData()
  }

  getPlayerData(){
    const url = 'http://localhost:5000/player/0';
    this.http.get(url).subscribe((res) => {
      this.playerData = res
      console.log(res)
    })
  }

  ngOnInit() {
    
  }
}
