import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";


@Injectable()
export class ConfigService{
    config:any;
    constructor(private http:HttpClient) {}
    load(): Promise<any> {
        return new Promise(resolve => {
        this.http.get(this.getBaseUrl() + "/config.json").subscribe(res => {
            this.config = res;
            resolve(this.config);
        }, () => { console.log('error loading config file') })
        })
    }

    getBaseUrl() {
        let url = window.location.href.split('//')[0] + "//" + window.location.host;
        return url;
    }
}