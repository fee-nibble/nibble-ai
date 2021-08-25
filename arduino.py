#include<Servo.h> //Servo 라이브러리를 추가
Servo servo4; //Servo 클래스로 servo객체 생성

void setup() {
  servo4.attach(4);     //servo 서보모터 4번 핀에 연결
}

void loop() {
  int ed_degree[6] = {{0, 0, 0, 1}, {0, 0, 1, 1}, {0, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 0}, {1, 1, 0, 0}};
  
  for(int i = 0; i < 6; i++) {
      ed_degree[i] = ed_degree[i] == 1 ? 180 : 0;
  }

  for(int i = 0; i < 6; i++) {
    servo4.write(ed_degree[i]);
    delay(5000);
  }
}