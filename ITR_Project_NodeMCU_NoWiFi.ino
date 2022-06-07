#include "Ubidots.h"

int sensorval=0,pval=0;

void setup() {
  Serial.begin(9600);
  // ubidots.setDebug(true);  // Uncomment this line for printing debug messages
}

void loop() {
  sensorval=analogRead(A0);
  sensorval-=12;
  if(sensorval<0)
    sensorval=0;
  if(sensorval!=0||(sensorval==0&&sensorval!=pval))
  {
    Serial.println("\nS1= ");
    Serial.println(sensorval);
  }
  pval=sensorval;
  delay(10);
}
