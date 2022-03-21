import { Component } from "@angular/core";
import { Router } from "@angular/router";


@Component({
    templateUrl: './industry-list.component.html'
})
export class IndustryListComponent{
    constructor(private router:Router){}
    gotoDashboard() {
        this.router.navigate(["./dashboard"])
    }
} 