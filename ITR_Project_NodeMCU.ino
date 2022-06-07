#include "Ubidots.h"

const char* UBIDOTS_TOKEN = "BBFF-W2AbfQXqUrCmjTQic2RDh9Ow3Kqv34";  // Put here your Ubidots TOKEN
const char* WIFI_SSID = "AndroidAPAE9B";      // Put here your Wi-Fi SSID
const char* WIFI_PASS = "ncvz1500";      // Put here your Wi-Fi password
int sensorval=0,pval=0;
Ubidots ubidots(UBIDOTS_TOKEN, UBI_TCP);

void setup() {
  Serial.begin(9600);
  ubidots.wifiConnect(WIFI_SSID, WIFI_PASS);
  // ubidots.setDebug(true);  // Uncomment this line for printing debug messages
}

void loop() {
  sensorval=analogRead(A0);
  sensorval-=12;
  if(sensorval<0)
    sensorval=0;
  if(sensorval!=0||(sensorval==0&&sensorval!=pval))
  {
    ubidots.add("Sensor reading", sensorval);

    bool bufferSent = false;
    bufferSent = ubidots.send();  // Will send data to a device label that matches the device Id

    if (bufferSent) {
      // Do something if values were sent properly
      Serial.println("Values sent by the device");
    }
  }
  pval=sensorval;
  delay(100);
}
