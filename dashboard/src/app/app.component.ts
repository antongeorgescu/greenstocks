import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GreenStockService } from './services/greenstock.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'dashboard';

  constructor(private greenStockService:GreenStockService)
  {

  }

  ngOnInit()
  {
    // this.greenStockService.getStocks().subscribe(data =>{
    //   console.log(data);
    // })
  }
}
