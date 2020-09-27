import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { InventoryComponent } from './inventory/inventory.component';
import { HubViewerComponent } from './hub-viewer/hub-viewer.component';
import { StoryViewerComponent } from './story-viewer/story-viewer.component';

@NgModule({
  declarations: [
    AppComponent,
    InventoryComponent,
    HubViewerComponent,
    StoryViewerComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
