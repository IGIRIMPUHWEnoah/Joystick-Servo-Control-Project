#include <Servo.h>

#define SERVO_PIN 6
#define JOY_VCC A2
#define JOY_GND A3
#define JOYSTICK_X A0

Servo gateServo;

void setup() {
  pinMode(JOY_VCC, OUTPUT);
  pinMode(JOY_GND, OUTPUT);
  digitalWrite(JOY_VCC, HIGH);
  digitalWrite(JOY_GND, LOW);

  gateServo.attach(SERVO_PIN);
  gateServo.write(0); 

  Serial.begin(9600);
  Serial.println(" Servo Joystick Control Initialized...");
}

void loop() {
  int joystickX = analogRead(JOYSTICK_X);
  Serial.print("Joystick X: ");
  Serial.println(joystickX);

  int servoPos = map(joystickX, 0, 1023, 0, 180);
  gateServo.write(servoPos);

  delay(50); 
}