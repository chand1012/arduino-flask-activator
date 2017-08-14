#include "ESP8266WiFi.h"
// The micro controller I am using is an ESP8266 built into a board similar
// to an arduino uno
char ssid[] = "";
char pass[] = "";
char host[] = "";
void setup(){

  Serial.begin(115200);
  delay(10);
  Serial.println("Connecting to " + String(ssid));
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print('.');
  }
  Serial.println("");
  Serial.println("Wi-Fi connected successfully!");

}
void loop(){
  post_request();
  delay(8000);
}
void post_request(){
  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }

   String data = "pst=coffee>" + String(random(0,100)) +"||make>" + String(random(0,100)) + "||coffee>text";
   Serial.print("Requesting POST: ");
   // Send request to the server:
   client.println("POST / HTTP/1.1");
   client.println("Host: server_name");
   client.println("Accept: */*");
   client.println("Content-Type: application/x-www-form-urlencoded");
   client.print("Content-Length: ");
   client.println(data.length());
   client.println();
   client.print(data);

   delay(500); // Can be changed
  if (client.connected()) { 
    client.stop();  
  Serial.println();
  Serial.println("closing connection");
}
}
