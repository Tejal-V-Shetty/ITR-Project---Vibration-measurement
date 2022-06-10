/*  ESP8266 NodeMCU-Sensor module 1 to Serial monitor
    Sensors : Vibration */

long sensorval=0,pval=0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorval=pulseIn(D0,HIGH);
  Serial.println("\nS1= ");
  Serial.println(sensorval);
  
  pval=sensorval;
  delay(10);
}
