import { Injectable } from '@angular/core';
import {HttpHeaders, HttpClient, HttpParams, HttpEventType} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map, timeoutWith, finalize } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiserviceService {
  private readonly baseApiUrl = 'http://10.54.3.36:8080/';
  headers: HttpHeaders;

  private static handleError(error: Response) {
    if (error.status === 0) {
        return throwError('Looks like our services are down');
    }
    return throwError(error || 'Server error');
}

  constructor(private _http: HttpClient) {
    this.headers = new HttpHeaders()
  }

  public getApi = (resrc: String ): Observable <any> => {
    return this._http.get(this.baseApiUrl + resrc, {
      headers: this.headers
    })
    .pipe(
        map((response: Response) => response),
        catchError(ApiserviceService.handleError),
        finalize(() => {
        })
      );
  }
}
