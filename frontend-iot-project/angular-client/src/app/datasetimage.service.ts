import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { DatasetImage } from './dataset_image';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DatasetimageService {
  imagesUrl = "/cloudimages";

  constructor(private http: HttpClient) { }

  getImagesFromCloud(): Observable<DatasetImage[]> {
    return this.http.get<DatasetImage[]>(this.imagesUrl)
    .pipe(
      tap(_ => console.log('fetched images')),
      catchError(this.handleError<DatasetImage[]>('getImagesFromCloud ', []))
    );
    // let images: DatasetImage[] = [{
    //   name: 'testimage',
    //   publicUrl: 'https://storage.googleapis.com/eric-bucket-test/438.png'
    // }];
    // return of(images);
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
  
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
  
      // TODO: better job of transforming error for user consumption
      console.log(`${operation} failed: ${error.message}`);
  
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
