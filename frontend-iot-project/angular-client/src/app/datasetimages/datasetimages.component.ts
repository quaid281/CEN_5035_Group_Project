import { Component, Inject, OnInit } from '@angular/core';
import { DatasetImage } from '../dataset_image';
import { DatasetimageService } from '../datasetimage.service'
import { Router } from '@angular/router';

@Component({
  selector: 'app-datasetimages',
  templateUrl: './datasetimages.component.html',
  styleUrls: ['./datasetimages.component.css']
})
export class DatasetimagesComponent implements OnInit {
  datasetImages: DatasetImage[] = null;
   
  constructor(private datasetimageservice: DatasetimageService, private router: Router) { }

  ngOnInit(): void {
    console.log("Initialized image component")
    this.datasetimageservice.getImagesFromCloud().subscribe(images => {
      this.datasetImages = images;
    });
  }

  gotoClassification(image: DatasetImage): void {
    const link = ['/classification', image.name];
    this.router.navigate(link);
  }

}
