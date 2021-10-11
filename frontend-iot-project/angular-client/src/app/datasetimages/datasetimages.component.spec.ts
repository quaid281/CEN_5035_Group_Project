import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DatasetimagesComponent } from './datasetimages.component';

describe('DatasetimagesComponent', () => {
  let component: DatasetimagesComponent;
  let fixture: ComponentFixture<DatasetimagesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DatasetimagesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DatasetimagesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
