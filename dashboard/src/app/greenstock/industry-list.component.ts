import { Component } from "@angular/core";
import { tick } from "@angular/core/testing";
import { ActivatedRoute, Router } from "@angular/router";
import { GreenStockService } from "../services/greenstock.service";


@Component({
    templateUrl: './industry-list.component.html'
})
export class IndustryListComponent{
    sectorsList:any;
    subIndustry:any;
    type: string = "Industry";
    selectedIndustry: string = "";
    constructor(private router:Router,private greenStockService:GreenStockService,
        private route:ActivatedRoute){}
    gotoDashboard() {
        this.router.navigate(["./dashboard"])
    }

    gotoIndustry()
    {
        this.router.navigate(["./industry-list"])
    }

    ngOnInit() {
        const id = this.route.snapshot.paramMap.get('id');
        if(id) {
            this.selectedIndustry = id;
            this.type = "SubIndustry";
            this.greenStockService.getSubIndustry(id).subscribe(data =>{
                this.sectorsList = data;
            });
        }else{
            this.greenStockService.getIndustries().subscribe(data =>{
                this.sectorsList = data;
            });
        }
    }

    onClick(id:any)
    {
        this.router.navigate(["sub-industry/"+id]);
    }

    onSubIndustryClick(ticker:string,industry:string)
    {
        this.router.navigate(["stocks/"+ticker+":"+industry]);
    }
} 