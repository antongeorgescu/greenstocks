import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';
import { IndustryListComponent } from './greenstock/industry-list.component';
import { StockComponent } from './greenstock/stock.component';

const routes: Routes = [
  {
    path: "",
    redirectTo: "dashboard",
    pathMatch: "full",
  },
  {
    path: "dashboard",
    component: DashboardComponent
  },
  {
    path: "industry-list",
    component: IndustryListComponent
  },
  {
    path: "sub-industry/:id",
    component : IndustryListComponent
  },
  {
    path: "stocks/:id",
    component : StockComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
