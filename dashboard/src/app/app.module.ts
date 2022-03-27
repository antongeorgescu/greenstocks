import { APP_INITIALIZER, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GreenStockService } from './services/greenstock.service';
import { IndustryListComponent } from './greenstock/industry-list.component';
import { DashboardComponent } from './dashboard.component';
import { ConfigService } from './config.service';
import { StockComponent } from './greenstock/stock.component';

export function init_app(configService: ConfigService) {
  return () => configService.load();
}

@NgModule({
  declarations: [
    AppComponent, IndustryListComponent, DashboardComponent,StockComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [GreenStockService,ConfigService,
    {
      provide: APP_INITIALIZER,
      useFactory: init_app,
      deps: [ConfigService],
      multi: true,
    }],
  bootstrap: [AppComponent]
})
export class AppModule { }
