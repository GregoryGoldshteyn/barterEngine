import { Component, OnInit, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-inventory',
  templateUrl: './inventory.component.html',
  styleUrls: ['./inventory.component.css']
})
export class InventoryComponent implements OnInit {

  @Input() gameData;

  rowArr = [1, 2, 3, 4, 5];
  colArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

  constructor() { 

  }

  ngOnInit(): void {
  }

}
