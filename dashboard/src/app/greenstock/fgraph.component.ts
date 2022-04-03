import { Component } from "@angular/core";
import { Chart } from 'angular-highcharts';
import { GreenStockService } from "../services/greenstock.service";



@Component({
    selector: 'fgraph',
    templateUrl: './fgraph.component.html'
})
export class FutureGraphComponent {
    data = [];
    chartDate:any = [];
    chart:any = null;
    xAxisData:any = [];
    stockName:any = "";
    webService:any = null;
    constructor(private greenStockService:GreenStockService) {
      this.webService = greenStockService;
      (async () => {await this.waitForElement(".clsStockName")})();
    }

    getChartData(){
      this.webService.getStocksHistory(this.stockName).subscribe((data:any)=>{
        this.data = data;
        this.data.forEach((val:any) =>{
          val.Date = val.Date.split('T')[0];
          this.xAxisData.push(val.Date);
          this.chartDate.push(val.Close);
        });
        this.drawChart();
      })
    }

    drawChart() {
      this.chart = new Chart({
        chart: {
          type: 'line'
        },
        title: {
          text: 'Stock History (last 3 months)'
        },
        credits: {
          enabled: false
        },
        xAxis: {
          categories: this.xAxisData
        },
        yAxis: {
          categories: ['0','1','2','3','4','5','6','7','8','9','10']
        },
        series: [
          {
            name: 'Days',
            data: this.chartDate,
            type: 'line'
          }
        ],
        colors: ['#008000']
      });
    }

    waitForElement(selector:any) : Promise<void> {
      // this observer based function takes as parameter a jquery class name attached to HTML element
      return new Promise(resolve => {
        // if respective selector is already loaded, return  
        if (document.querySelector(selector)) {
              return resolve(document.querySelector(selector));
          }
    
          // if selector is not loaded, create an observer
          const observer = new MutationObserver(mutations => {
              if (document.querySelector(selector)) {
                  resolve(document.querySelector(selector));
                  observer.disconnect();
                  this.stockName = document.getElementById("stockName")?.innerText;
                  if (this.stockName)
                    this.getChartData();
              }
          });
    
          // run the observer till selector is loaded
          observer.observe(document.body, {
              childList: true,
              subtree: true
          });
      });
    }
}


