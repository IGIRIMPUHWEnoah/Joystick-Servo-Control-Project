#include <Servo.h>

#define x_pin A0
#define y_pin A1
#define hardcoded_vcc1 A2
#define hardcoded_gnd1 A3

const int trigPin = 9;
const int echoPin = 10;
const int buzzer = 8;

Servo myServo;
const int servoPin = 6;

long duration;
int distance;

void setup() {
  Serial.begin(9600);

  pinMode(hardcoded_vcc1, OUTPUT);
  pinMode(hardcoded_gnd1, OUTPUT);
  digitalWrite(hardcoded_vcc1, HIGH);
  digitalWrite(hardcoded_gnd1, LOW);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(buzzer, OUTPUT);

  myServo.attach(servoPin);
}

void loop() {
  int x_val = analogRead(x_pin);
  int y_val = analogRead(y_pin);
  Serial.print("X: ");
  Serial.print(x_val);
  Serial.print(", Y: ");
  Serial.println(y_val);

  int servoAngle = map(x_val, 0, 1023, 0, 180);
  myServo.write(servoAngle);

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  Serial.print("Distance: ");
  Serial.println(distance);

  if(distance < 10){
    digitalWrite(buzzer, HIGH);
  } else {
    digitalWrite(buzzer, LOW);
  }

  delay(200);
}
