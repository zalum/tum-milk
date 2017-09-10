#include <Adafruit_NeoPixel.h>

#define PIN 5
#define NUM_PIXELS 10
#define INPUT1 10
#define INPUT2 11
#define LED 13

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_PIXELS, PIN, NEO_GRBW + NEO_KHZ800);

void setup() {
  pinMode(INPUT1, INPUT);
  pinMode(INPUT2, INPUT);
  digitalWrite(INPUT1, LOW);
  digitalWrite(INPUT2, LOW);

//  pinMode(LED, OUTPUT);

    strip.begin();
    strip.show();
}
void loop() {
    if (digitalRead(INPUT1) == HIGH && digitalRead(INPUT2) == HIGH) {
        for (int i = 0; i < NUM_PIXELS; i++) {
          strip.setPixelColor(i, strip.Color(0, 100, 0, 0));
        }
        strip.show();
    } else if (digitalRead(INPUT1) == HIGH && digitalRead(INPUT2) == LOW) {
       for (int i = 0; i < NUM_PIXELS; i++) {
          strip.setPixelColor(i, strip.Color(100, 0, 0, 0));
        }
        strip.show();
    } else {
      for (int i = 0; i < NUM_PIXELS; i++) {
          strip.setPixelColor(i, strip.Color(100, 100, 0, 0));
        }
        strip.show();
    }
}
