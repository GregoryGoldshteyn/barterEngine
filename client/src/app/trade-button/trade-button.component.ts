import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-trade-button',
  templateUrl: './trade-button.component.html',
  styleUrls: ['./trade-button.component.css']
})
export class TradeButtonComponent implements OnInit {

  @Input() buttonData;
  @Input() tradeData;
  @Input() itemData;

  constructor() { 
    // Start empty - a button should never stay empty as soon as buttonData is sent from story component
    this.buttonData = {
      "title": "",
      "short": "",
      "in": {},
      "out": {}
    }
  }

  ngOnInit(): void {
  }

  ngOnChanges(): void {

  }

}
