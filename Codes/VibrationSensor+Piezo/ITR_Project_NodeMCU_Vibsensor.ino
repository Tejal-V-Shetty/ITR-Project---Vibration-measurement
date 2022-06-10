/*  ESP8266 NodeMCU-Sensor module 1 to Ubidots
    Sensors : vibration and piezoelectric(voltage measurement)
    Protocol : UDP  */
    
#include "Ubidots.h"

const char* UBIDOTS_TOKEN = "BBFF-W2AbfQXqUrCmjTQic2RDh9Ow3Kqv34";  // Put here your Ubidots TOKEN
//const char* WIFI_SSID = "VOLTAS";      // Put here your Wi-Fi SSID
//const char* WIFI_PASS = "moparjeep";      // Put here your Wi-Fi password
const char* WIFI_SSID = "AndroidAPAE9B";      // Put here your Wi-Fi SSID
const char* WIFI_PASS = "ncvz1500"; 
long sensorval=0, pval=0, analogsensorval=0, analogpval=0;
int dataread=0;
Ubidots ubidots(UBIDOTS_TOKEN, UBI_UDP);

void setup() {
  Serial.begin(9600);
  ubidots.wifiConnect(WIFI_SSID, WIFI_PASS);
  // ubidots.setDebug(true);  // Uncomment this line for printing debug messages
}

void loop() {
  sensorval=pulseIn(D0,HIGH);
  analogsensorval=analogRead(A0);
  analogsensorval-=5;
  if(analogsensorval<0)
    analogsensorval=0;
    if(sensorval!=0||(sensorval==0&&sensorval!=pval))
    {
      ubidots.add("Sensor reading", sensorval);
      dataread=1;
    }
    if(analogsensorval!=0||(analogsensorval==0&&analogsensorval!=analogpval))
    {
      ubidots.add("Analog Sensor reading", analogsensorval);
      dataread=1; 
    }
    if(dataread)
    {
      bool bufferSent = false;
      bufferSent = ubidots.send();  // Will send data to a device label that matches the device Id

      if (bufferSent) {
        // Do something if values were sent properly
        Serial.println("Values sent by the device");
      }
    }
  pval=sensorval;
  analogpval=analogsensorval;
  dataread=0;
  delay(20);
}
