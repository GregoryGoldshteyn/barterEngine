import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-story-viewer',
  templateUrl: './story-viewer.component.html',
  styleUrls: ['./story-viewer.component.css']
})
export class StoryViewerComponent implements OnInit {

  @Input() gameData;
  @Input() testData;

  public storyTitle;
  public storyShortDescription;
  public storyLongDescription;

  public tradeButtonData = {"trades" : {}, "items" : {}};

  constructor() { 

  }

  ngOnInit(): void {
    
  }

  ngOnChanges(): void {
    this.generateTradeButtonData();
    this.handleUIChangeToStoryObject();
  }

  handleUIChangeToStoryObject(): void {

  }

  generateTradeButtonData(): void {
    /*
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
    */
  }
}
