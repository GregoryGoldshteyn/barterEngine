import { Component, OnInit, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-hub-viewer',
  templateUrl: './hub-viewer.component.html',
  styleUrls: ['./hub-viewer.component.css']
})
export class HubViewerComponent implements OnInit {

  @Input() gameData;

  constructor() { 

  }

  ngOnInit(): void {

  }

  ngOnChanges(): void {
    this.handleUIChangeToHubObject();
  }

  handleUIChangeToHubObject(): void {
    if(this.gameData == null)
    {
      return;
    }
  }
}
