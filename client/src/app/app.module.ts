import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { InventoryComponent } from './inventory/inventory.component';
import { HubViewerComponent } from './hub-viewer/hub-viewer.component';
import { StoryViewerComponent } from './story-viewer/story-viewer.component';
import { TradeButtonComponent } from './trade-button/trade-button.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LoginPageComponent } from './login-page/login-page.component';
import { AuthInterceptor } from './auth/auth.interceptor';
import { UseHttpsInterceptor } from './auth/use-https.interceptor';

const HttpInterceptorProviders = [
  { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
//  { provide: HTTP_INTERCEPTORS, useClass: UseHttpsInterceptor, multi: true },
]

@NgModule({
  declarations: [
    AppComponent,
    InventoryComponent,
    HubViewerComponent,
    StoryViewerComponent,
    TradeButtonComponent,
    LoginPageComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    NgbModule,
    FormsModule
  ],
  providers: [
    HttpInterceptorProviders
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
