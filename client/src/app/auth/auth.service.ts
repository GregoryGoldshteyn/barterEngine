import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  // Auth things
  login(secret_code) {
    return this.http.post('http://localhost:4999/authenticator/login', { 'player_id' : secret_code });
  }

  logout() {
    localStorage.removeItem("id_token");
    localStorage.removeItem("expires_at");
  }

  public isLoggedIn() {
    if(localStorage.getItem("expires_at") == "undefined"){
      return false;
    }
    if (localStorage.getItem("id_token") == "undefined") {
      return false;
    }
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

  public setSession(authResult) {
    // Sever sends the time since current epoch in seconds. Convert to ms
    const expiresAt = 1000 * authResult.expiresAt;
    localStorage.setItem('id_token', authResult.idToken);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf));
  }
}
