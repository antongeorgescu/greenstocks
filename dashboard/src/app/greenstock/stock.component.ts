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
        height: 200px;
        font-weight: bold;
        width: 200px;
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
    stockName: any = ""
    stockScore: any;
    stockRank: string = "0";
    stockArticles: string = "";
    stockReferences: string = "0";
    constructor(private router:Router,private greenStockService:GreenStockService,
        private route:ActivatedRoute){}
    ngOnInit()
    {
        const id = this.route.snapshot.paramMap.get('id');
        this.stockName = id;

        //0-4% Poor, 5-9% Decent,10 - 19% Good, over 20% Excellent
        this.greenStockService.getStocksScoreV2(this.stockName).subscribe((data:any) =>{
            this.stockScore = Math.round(parseFloat(data[0][1]) * 100);
            console.log(this.stockScore);
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

            this.domReady(className);
        });

        this.greenStockService.getStocksReferences(this.stockName).subscribe((data:any) =>{
            this.stockReferences = data[0][1];
        });

        this.greenStockService.getStocksArticles(this.stockName).subscribe((data:any) =>{
            this.stockArticles = data.length;
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