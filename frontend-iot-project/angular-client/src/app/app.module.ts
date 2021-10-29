import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { DatasetimagesComponent } from './datasetimages/datasetimages.component';
import { ClassificationEditorComponent } from './classification-editor/classification-editor.component';

@NgModule({
  declarations: [
    AppComponent,
    DatasetimagesComponent,
    ClassificationEditorComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
