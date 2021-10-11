import { Component, Inject, OnInit } from '@angular/core';
import { DatasetImage } from '../dataset_image';
import { DatasetimageService } from '../datasetimage.service'

@Component({
  selector: 'app-datasetimages',
  templateUrl: './datasetimages.component.html',
  styleUrls: ['./datasetimages.component.css']
})
export class DatasetimagesComponent implements OnInit {
  datasetImages: DatasetImage[];
   
  //constructor() {}
  constructor(private datasetimageservice: DatasetimageService) { }

  ngOnInit(): void {
    // let images: DatasetImage[] = [{
    //   name: 'testimage',
    //   publicUrl: 'https://storage.googleapis.com/eric-bucket-test/438.png'
    // }];
    console.log("Initialized image component")
    this.datasetimageservice.getImagesFromCloud().subscribe(images => {
      this.datasetImages = images;
      console.log(`Images list: ${images}`);
    });
  }

}
