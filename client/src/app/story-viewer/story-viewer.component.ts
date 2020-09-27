import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-story-viewer',
  templateUrl: './story-viewer.component.html',
  styleUrls: ['./story-viewer.component.css']
})
export class StoryViewerComponent implements OnInit {

  @Input() playerData;

  constructor() { }

  ngOnInit(): void {
    
  }

}
