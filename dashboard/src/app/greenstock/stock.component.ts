import { Component } from "@angular/core";
import { ActivatedRoute, Router } from "@angular/router";
import { GreenStockService } from "../services/greenstock.service";

@Component({
    templateUrl: './stock.component.html',
    styles: [`
    .section {
        height: 100%;  
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }
    `]
})
export class StockComponent{
    stockName: any = ""
    stockScore: string = "15";
    stockRank: string = "Good"
    constructor(private router:Router,private greenStockService:GreenStockService,
        private route:ActivatedRoute){}
    ngOnInit()
    {
        const id = this.route.snapshot.paramMap.get('id');
        this.stockName = id;

        this.greenStockService.getStocksFinancials(this.stockName).subscribe(data =>{
            console.log(data);
        });

        this.greenStockService.getStocksRecommendations(this.stockName).subscribe(data =>{
            console.log(data);
        });

    }
    gotoDashboard()
    {
        this.router.navigate(["./industry-list"])
    }
}