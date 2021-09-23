import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from './../environments/environment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  // переменная для слов из запроса
  wordList: any = [];

  constructor(private http: HttpClient) {

  }

  getWordList() {
    console.log('hello');
    this.http.get(`${environment.backendUrl}/v1/english/`).subscribe((res: any) => {
      this.wordList = res;
      console.log(this.wordList);
    }
  )}
}
