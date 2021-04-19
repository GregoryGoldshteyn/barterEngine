import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor() {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {

    // Get token from localStorage
    const idToken = localStorage.getItem("id_token");

    // If token, add it to authorization headers
    if (idToken) {
      const cloned = request.clone({
        headers: request.headers.set("Authorization", idToken)
      });

      // Return the new request with authorization token
      return next.handle(cloned);
    }

    // Else, pass the request with no token
    return next.handle(request);
  }
}
