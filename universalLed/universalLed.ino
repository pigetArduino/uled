#include <FastLED.h>
// Universal USB LED
// -----------------
// Components:
// WS led (NEOPIXEL)
// Arduino

/*
   Color Table
   0 Off
   1 White
   2 Red
   3 Green
   4 Blue
   5 Yellow
   6 Orange
   7 Purple
*/

//USB
const String usb_name = "OpenLightHUD\n";

//Leds
const int DATA_PIN = 6; //Neo Pixel RGB led
const int NUM_LEDS = 5;

CRGB leds[NUM_LEDS];

//Serial
String readString;

void changeLed(int pos, int color) {
  switch (color) {
    case 0:
      leds[pos] = CRGB::Black;
      break;
    case 1:
      leds[pos] = CRGB::White;
      break;
    case 2:
      leds[pos] = CRGB::Red;
      break;
    case 3:
      leds[pos] = CRGB::Green;
      break;
    case 4:
      leds[pos] = CRGB::Blue;
      break;
    case 5:
      leds[pos] = CRGB::Yellow;
      break;
    case 6:
      leds[pos] = CRGB::Orange;
      break;
    case 7:
      leds[pos] = CRGB::Purple;
      break;
  }
  FastLED.show();
}


void BlinkLeds(int color) {
  for (int i = 0; i < NUM_LEDS; i++) {
    changeLed(i, color);
  }

  delay(100);
  for (int i = 0; i < NUM_LEDS; i++) {
    changeLed(i, 0);
  }
}

void setup() {
  // Setup Led
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  // Test Led (All White)
   for (int i = 0; i < NUM_LEDS; i++) {
     changeLed(i, 1);
   }

  //Setup Serial
  Serial.begin(115200);
}

void loop() {
  //Get Serial as a string
  while (Serial.available()) {
    delay(3); // Wait for data

    if (Serial.available() > 0) {
      char c = Serial.read();
      readString += c;
    }
  }

  //If string received
  if (readString.length() > 0) {
    //Serial.println(readString); //Show order sent

    if (readString == usb_name) {
      Serial.print("OK");
      BlinkLeds(3);
    } else {
      int led = readString.substring(0).toInt() - 1;
      int color = readString.substring(2).toInt();
      //Serial.println(led);
      //Serial.println(color);
      if (led != -1) {
        changeLed(led, color);
        Serial.print("OK");
      }
    }
  }
  readString = "";
}




