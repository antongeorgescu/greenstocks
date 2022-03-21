import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable()
export class GreenStockService{
    constructor(private http:HttpClient) {}

    getStocks(){
        return this.http.get("http://127.0.0.1:5000/api/v1/resources/stocks/sector/list");
    }
}