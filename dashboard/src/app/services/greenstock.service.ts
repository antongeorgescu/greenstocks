import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { ConfigService } from "../config.service";
@Injectable()
export class GreenStockService{
    constructor(private http:HttpClient, private configService:ConfigService) {
       
    }
    getIndustries(){
        return this.http.get(this.configService.config.API + "api/v1/resources/stocks/sector/list");
    }

    getSubIndustry(id:any){
        return this.http.get(this.configService.config.API + "api/v1/resources/stocks/sector/"+ id);
    }
}