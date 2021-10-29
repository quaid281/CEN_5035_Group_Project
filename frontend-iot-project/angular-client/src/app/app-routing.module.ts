import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import{ ClassificationEditorComponent } from './classification-editor/classification-editor.component';
import { DatasetimagesComponent } from './datasetimages/datasetimages.component';

const routes: Routes = [
  { path: '', component: DatasetimagesComponent },
  { path: 'classification/:image', component: ClassificationEditorComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
