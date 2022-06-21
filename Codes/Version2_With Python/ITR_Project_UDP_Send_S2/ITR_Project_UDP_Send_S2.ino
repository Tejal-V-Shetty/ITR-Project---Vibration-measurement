#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#ifndef STASSID
#define STASSID "AndroidAPAE9B"
#define STAPSK  "ncvz1500"
#endif

unsigned int localPort = 4210;      // local port to listen on
long sensorval=0,pval=0;
// buffers for receiving and sending data
char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1]; //buffer to hold incoming packet,
char  ReplyBuffer[30] = "0";       // a string to send back
char *sval;

WiFiUDP Udp;

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(STASSID, STAPSK);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(500);
  }
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());
  Serial.printf("UDP server on port %d\n", localPort);
  Udp.begin(localPort);
}

void loop() {
sensorval=pulseIn(D0,HIGH);
sval=ltoa(sensorval,ReplyBuffer,10);
if(sensorval!=0||(sensorval==0&&sensorval!=pval))
{
  Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
  Udp.write(sval);
  Udp.endPacket();
  Serial.print("\nS2= ");
  Serial.print(sval);
}
pval=sensorval;
delay(100);
}
