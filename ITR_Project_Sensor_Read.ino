const int S1pin= A0;
  int S1val=0;
void setup() {
  Serial.begin(9600);
}

void loop() {
  S1val=analogRead(S1pin);
  Serial.print("\n S1= ");
  Serial.print(S1val);
  delay(100);
}
