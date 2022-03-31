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
    constructor(private greenStockService:GreenStockService) {
      this.greenStockService.getStocksHistory("CLNE").subscribe((data:any)=>{
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
          text: 'Stock History'
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
}