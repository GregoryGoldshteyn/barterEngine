import { Component, OnInit, Input, DebugElement } from '@angular/core';
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

  public tradeButtonData = {"trades" : {}, "items" : {}};

  constructor(private http: HttpClient) { 
    this.getPlayerData()
  }

  ngOnInit(): void {
    
  }

  ngOnChanges(): void {
    console.log("OnChangesCalled");
    this.generateTradeButtonData();
    this.handleUIChangeToStoryObject();
  }

  handleUIChangeToStoryObject(): void {
    if(this.testData == null)
    {
      return;
    }
    this.storyTitle = this.testData["STORIES"]["3"]["name"];
    this.storyShortDescription = this.testData["STORIES"]["3"]["short"];
    this.storyLongDescription = this.testData["STORIES"]["3"]["long"];
  }

  generateTradeButtonData(): void {
    if (this.testData == null) {
      return;
    }
    this.tradeButtonData = {"trades" : {}, "items" : {}};
    for (let tradekey in this.testData["STORIES"]["3"]["trade_to_story"]){
      let trade = this.testData["TRADES"][tradekey];
      for(let itemkey in trade["items_in"]){
        this.tradeButtonData["items"][itemkey] = this.testData["ITEMS"][itemkey]
      }
      for (let itemkey in trade["items_out"]) {
        this.tradeButtonData["items"][itemkey] = this.testData["ITEMS"][itemkey]
      }
      this.tradeButtonData["trades"][tradekey] = trade
    }
  }

  getPlayerData() {
    const url = 'http://localhost:5000/player/0/stories';
    this.http.get(url).subscribe((res) => {
      console.log(res)
      return res
    })
  }

}
