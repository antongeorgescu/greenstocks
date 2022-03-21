import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GreenStockService } from './services/greenstock.service';
import { IndustryListComponent } from './greenstock/industry-list.component';
import { DashboardComponent } from './dashboard.component';

@NgModule({
  declarations: [
    AppComponent, IndustryListComponent, DashboardComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [GreenStockService],
  bootstrap: [AppComponent]
})
export class AppModule { }
