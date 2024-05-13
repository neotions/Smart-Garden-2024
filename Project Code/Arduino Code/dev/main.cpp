/*

found this boiler plate online for arduiono nano 33 iot

#include <WiFi.h>
#include <PubSubClient.h>

// WiFi credentials
const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";

// MQTT broker details
const char* mqttServer = "your_mqtt_broker_ip";
const int mqttPort = 1883;
const char* mqttUsername = "your_mqtt_username";
const char* mqttPassword = "your_mqtt_password";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
    Serial.begin(115200);
    delay(2000);

    // Connect to WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");

    // Connect to MQTT broker
    client.setServer(mqttServer, mqttPort);
    while (!client.connected()) {
        Serial.println("Connecting to MQTT broker...");
        if (client.connect("arduinoClient", mqttUsername, mqttPassword)) {
            Serial.println("Connected to MQTT broker");
        } else {
            Serial.print("Failed to connect to MQTT broker, rc=");
            Serial.print(client.state());
            Serial.println(" Retrying in 5 seconds...");
            delay(5000);
        }
    }
}

void loop() {
    // Your code here

    // Example: Publish a message to a topic
    client.publish("your_topic", "Hello from Arduino Nano IoT");

    delay(5000);
}


*/