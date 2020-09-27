import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-hub-viewer',
  templateUrl: './hub-viewer.component.html',
  styleUrls: ['./hub-viewer.component.css']
})
export class HubViewerComponent implements OnInit {

  @Input() playerData;

  constructor() { }

  ngOnInit(): void {
  }

}
