import { Component} from "@angular/core";
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
    stockReferences0: string = "0";
    stockReferences1: string = "0";
    loading = true;
    stockAction0: string = "";
    stockAction1: string = "";
    stockAction2: string = "";
    constructor(private router:Router,
        private greenStockService:GreenStockService,
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
            var circleClassNames = ""
            if(data[0][0] == "green_score") {
                if(this.stockScore <= 4) {
                    this.stockRank = "Poor";
                    circleClassNames="circle border border-danger"
                    className = "btn-danger";
                }else if (this.stockScore >= 5 && this.stockScore <= 9){
                    this.stockRank = "Decent";
                    circleClassNames="circle border border-warning"
                    className = "btn-warning";
                }else if (this.stockScore >= 10 && this.stockScore <= 19){
                    this.stockRank = "Good";
                    circleClassNames="circle border border-success"
                    className = "btn-success";
                }else{
                    this.stockRank = "Excellent";
                    className = "btn-success";
                    circleClassNames="circle border border-success"
                }
            }
            this.loading = false;
            this.domReady(className,circleClassNames);
        });

        this.greenStockService.getStockRecommendedAction(this.stockName).subscribe((data:any) =>{
            this.stockAction0 = `${data['Action'].toUpperCase()}`;
            var fromGrade = '';
            var toGrade = '';
            if (data['From Grade'] == '')
                fromGrade = 'Unknown';
            else
                fromGrade = data['From Grade'];
            if (data['To Grade'] == '')
                toGrade = 'Unknown';
            else
                toGrade = data['To Grade']; 
            this.stockAction1 = `Graded from ${fromGrade} to ${toGrade}`;
            this.stockAction2 = `Estimator brokerage: ${data['Firm']}`;
        });

        this.greenStockService.getStocksReferences(this.stockName).subscribe((data:any) =>{
            this.stockReferences0 = `Total Tokens: ${data[0][1]}, Green Tokens: ${data[1][1]}`;
            this.stockReferences1 = `Green Score: ${data[2][1]}, Green Density: ${data[4][1]}`;
        });

    }

    domReady(className: string,circleClassNames: string) {
        setTimeout(()=>{
            var element = document.getElementById("scoreRankDisplay");
            if(element) {
                element.className += " " + className;
            }
            element = document.getElementById("scoreCircle");
            if(element) {
                element.className += " " + circleClassNames;
            }
        },100);
    }

    gotoDashboard()
    {
        this.router.navigate(["./industry-list"])
    }
}
