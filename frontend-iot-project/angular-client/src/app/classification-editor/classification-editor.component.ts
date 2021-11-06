import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { DatasetImage } from '../dataset_image';
import { DatasetimageService } from '../datasetimage.service'
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-classification-editor',
  templateUrl: './classification-editor.component.html',
  styleUrls: ['./classification-editor.component.css']
})

export class ClassificationEditorComponent implements OnInit {
  @Input() image: DatasetImage;
  @Output() close = new EventEmitter();
  navigated = false;
  error: any;
  constructor(private datasetimageservice: DatasetimageService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.forEach((params: Params) => {
      if (params['image'] !== undefined) {
        const img = params['image'];
        this.navigated = true;
        this.datasetimageservice.getImage(img).subscribe(img => this.image = img);
        console.log(this.image.name);
      } else {
        this.navigated = false;
        this.image = new DatasetImage();
      }
    });
  }

  save(): void {
    this.datasetimageservice.save(this.image).subscribe(image => {
      this.image = image;
      this.goBack(image);
    }, error => (this.error = error));
  }

  goBack(savedImage: DatasetImage = null): void {
    if (this.navigated) {
      window.history.back();
    }
  }

}
