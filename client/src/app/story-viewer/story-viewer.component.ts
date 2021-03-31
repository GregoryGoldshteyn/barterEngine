import { Component, OnInit, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-story-viewer',
  templateUrl: './story-viewer.component.html',
  styleUrls: ['./story-viewer.component.css']
})
export class StoryViewerComponent implements OnInit {

  @Input() playerData;
  @Input() testData;

  public storyTitle;
  public storyShortDescription;
  public storyLongDescription;

  constructor(private http: HttpClient) { 
    this.getPlayerData()
  }

  ngOnInit(): void {
    
  }

  ngOnChanges(): void {
    this.handleUIChangeToStoryObject();
  }

  handleUIChangeToStoryObject(): void {
    if(this.testData == null)
    {
      return;
    }
    this.storyTitle = this.testData["STORIES"][0]["name"];
    this.storyShortDescription = this.testData["STORIES"][0]["short"];
    this.storyLongDescription = this.testData["STORIES"][0]["long"];
  }

  getPlayerData() {
    const url = 'http://localhost:5000/player/0/stories';
    this.http.get(url).subscribe((res) => {
      console.log(res)
      return res
    })
  }

}
