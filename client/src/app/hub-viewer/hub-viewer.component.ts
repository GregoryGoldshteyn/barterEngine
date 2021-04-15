import { Component, OnInit, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-hub-viewer',
  templateUrl: './hub-viewer.component.html',
  styleUrls: ['./hub-viewer.component.css']
})
export class HubViewerComponent implements OnInit {

  @Input() playerData;

  constructor(private http: HttpClient) { 
    this.getPlayerData()
  }

  ngOnInit(): void {

  }

  ngOnChanges(): void {
    this.handleUIChangeToHubObject();
  }

  handleUIChangeToHubObject(): void {
    if(this.playerData == null)
    {
      return;
    }
  }

  getPlayerData() {
    const url = 'http://localhost:4999/placer/player/0/hubs';
    this.http.get(url).subscribe((res) => {
      console.log(res)
      return res
    })
  }

}
