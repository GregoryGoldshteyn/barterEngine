import { Component, OnInit, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-story-viewer',
  templateUrl: './story-viewer.component.html',
  styleUrls: ['./story-viewer.component.css']
})
export class StoryViewerComponent implements OnInit {

  @Input() playerData;

  constructor(private http: HttpClient) { 
    this.getPlayerData()
  }

  ngOnInit(): void {
    
  }

  getPlayerData() {
    const url = 'http://localhost:5000/player/0/stories';
    this.http.get(url).subscribe((res) => {
      console.log(res)
      return res
    })
  }

}
