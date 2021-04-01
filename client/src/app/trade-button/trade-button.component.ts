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
    // Some test data
    this.buttonData = {
      "title" : "Test title",
      "short" : "This is short description",
      "in" : {"foo" : "1", "bar" : "1"},
      "out" : {"foobar" : "1"}
    }

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
    console.log("---------");
    console.log(this.tradeData.items_in);
    console.log(this.tradeData.items_in === {});
    console.log("---------");
  }

}
