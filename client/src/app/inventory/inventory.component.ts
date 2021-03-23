import { Component, OnInit, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-inventory',
  templateUrl: './inventory.component.html',
  styleUrls: ['./inventory.component.css']
})
export class InventoryComponent implements OnInit {

  @Input() playerData;

  constructor(private http: HttpClient) { 
    this.getPlayerData()
  }

  ngOnInit(): void {
  }

  getPlayerData() {
    const url = 'http://localhost:5000/player/0/inventory';
    this.http.get(url).subscribe((res) => {
      console.log(res)
      return res
    })
  }

}
