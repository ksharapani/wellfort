import { Component } from '@angular/core';
import { interval } from 'rxjs';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'wellfort';
  obs: any;
  userName: string = '';
  notification: any;
  timeInterval = TIME_INTERVAL;
  constructor(private http: HttpClient) {}
  ngOnInit() {
    interval(this.timeInterval).subscribe((x) => {
      this.http.get('http://localhost:8000/dashboard/test').subscribe((res) => {
        this.notification = res;
        if (this.notification.audio != null) {
          let audio = new Audio();
          audio.src = 'http://localhost:8000/' + this.notification.audio;

          audio.load();
          audio.play();
          console.log('audio playing...');
        }
      });
    });
  }
}

export interface Notification {
  status: string;
  user: string;
  display_message: string;
}

export const TIME_INTERVAL = 10000;
