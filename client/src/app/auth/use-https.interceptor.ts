import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class UseHttpsInterceptor implements HttpInterceptor {

  constructor() {}

  // Force all communications over https
  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    const cloned = request.clone({
      url: request.url.replace('http://', 'https://')
    });

    // Return the new request with authorization token
    return next.handle(cloned);
  }
}
