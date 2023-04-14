int PulseSensor = A0;
int Myo1 = A3;
int Myo2 = A5; 

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A3, INPUT);
  pinMode(A5, INPUT);
}


void loop() {
  int PulseReading = analogRead(PulseSensor);
  int Myo1Reading = analogRead(Myo1);
  int Myo2Reading = analogRead(Myo2);

  Serial.print(PulseReading);
  Serial.print(" ");
  Serial.print(Myo1Reading);
  Serial.print(" ");
  Serial.println(Myo2Reading);
  delay(30);
}
