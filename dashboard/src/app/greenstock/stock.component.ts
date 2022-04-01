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
      .block {
        text-align: center;
        vertical-align: middle;
    }
    .circle {
        background: #F0EDFB;
        border-radius: 200px;
        color: black;
        height: 150px;
        font-weight: bold;
        width: 150px;
        display: table;
        margin: 20px auto;
    }
    .circle p {
        vertical-align: middle;
        display: table-cell;
    }
    `]
})
export class StockComponent{
    stockDisplayName: any = ""
    stockName: any = ""
    stockScore: any;
    stockRank: string = "0";
    stockArticles: string = "";
    stockReferences: string = "0";
    loading = true;
    constructor(private router:Router,private greenStockService:GreenStockService,
        private route:ActivatedRoute){}
    ngOnInit()
    {
        const id = this.route.snapshot.paramMap.get('id');
        this.stockName = id?.split(":")[0];
        this.stockDisplayName = id?.split(":").join(" ( ");
        this.stockDisplayName = this.stockDisplayName + " )";
        //0-4% Poor, 5-9% Decent,10 - 19% Good, over 20% Excellent
        this.greenStockService.getStocksScoreV2(this.stockName).subscribe((data:any) =>{
            this.stockScore = Math.round(parseFloat(data[0][1]) * 100);
            var className = ""
            if(data[0][0] == "green_score") {
                if(this.stockScore <= 4) {
                    this.stockRank = "Poor";
                    className = "btn-danger";
                }else if (this.stockScore >= 5 && this.stockScore <= 9){
                    this.stockRank = "Decent";
                    className = "btn-warning";
                }else if (this.stockScore >= 10 && this.stockScore <= 19){
                    this.stockRank = "Good";
                    className = "btn-success";
                }else{
                    this.stockRank = "Excellent";
                    className = "btn-success";
                }
            }
            this.loading = false;
            this.domReady(className);
        });

        this.greenStockService.getStocksReferences(this.stockName).subscribe((data:any) =>{
            this.stockReferences = `Total Tokens: ${data[0][1]}, Green Tokens: ${data[1][1]}, Green Score: ${data[2][1]}, Green Density: ${data[4][1]}`;
        });

    }

    domReady(className: string) {
        setTimeout(()=>{
            var element = document.getElementById("scoreRankDisplay");
            if(element) {
                element.className += " " + className;
            }
        },100);
    }

    gotoDashboard()
    {
        this.router.navigate(["./industry-list"])
    }
}