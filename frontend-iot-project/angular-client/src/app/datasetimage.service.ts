import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { DatasetImage } from './dataset_image';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Data } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class DatasetimageService {
  imagesUrl = "/api/datasetimages";

  constructor(private http: HttpClient) { }

  getImagesFromCloud(): Observable<DatasetImage[]> {
    return this.http.get<DatasetImage[]>(this.imagesUrl)
    .pipe(
      tap(_ => console.log('fetched images')),
      catchError(this.handleError<DatasetImage[]>('getImagesFromCloud ', []))
    );
  }

  getImage(image: string): Observable<DatasetImage> {
    const url = this.imagesUrl + '/' + image;
    return this.http.get<DatasetImage>(url)
    .pipe(
      tap(_ => console.log('fetched images')),
      catchError(this.handleError<DatasetImage>('getImagesFromCloud ', null))
    );
  }

  save(image: DatasetImage): Observable<DatasetImage> {
    if (image.name) {
      return this.http.put<DatasetImage>(this.imagesUrl, image);
    }
    return this.http.post<DatasetImage>(this.imagesUrl, image);
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      console.log(`${operation} failed: ${error.message}`);
  
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
