import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  // Auth things
  login(secret_code) {
    return this.http.post('http://localhost:4999/login', { secret_code })
      .subscribe(res => this.setSession);
  }

  logout() {
    localStorage.removeItem("id_token");
    localStorage.removeItem("expires_at");
  }

  public isLoggedIn() {
    return Date.now() < this.getTokenExpiration();
  }

  public isLoggedOut() {
    return !this.isLoggedIn();
  }

  getTokenExpiration() {
    const expiration = localStorage.getItem("expires_at");
    const expiresAt = JSON.parse(expiration);
    return parseInt(expiresAt);
  }

  private setSession(authResult) {
    const expiresAt = Date.now() + 1000 * authResult.expiresIn;
    localStorage.setItem('id_token', authResult.idToken);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf));
  }
}
