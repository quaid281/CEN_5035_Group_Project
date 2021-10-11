import { TestBed } from '@angular/core/testing';

import { DatasetimageService } from './datasetimage.service';

describe('DatasetimageService', () => {
  let service: DatasetimageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DatasetimageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
