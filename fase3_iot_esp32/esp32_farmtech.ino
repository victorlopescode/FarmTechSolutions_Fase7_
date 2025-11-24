#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Falha ao ler do DHT!");
  } else {
    Serial.print("Umidade: ");
    Serial.print(h);
    Serial.print(" %  | Temperatura: ");
    Serial.print(t);
    Serial.println(" °C");
  }

  delay(2000);
}
