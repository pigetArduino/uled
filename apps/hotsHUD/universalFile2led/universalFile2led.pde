/*
*    
 *   Universal Led
 *   Control Led by modifying text file
 */

// This is a prototype, don't expect things to works out of the box
// This will be replace by a python version (See UL)

import java.awt.*;
import processing.serial.*;

//Debug mode
boolean debug = false;

//File path
//You need to create 1.txt/2.txt/3.txt/4.txt/5.txt manually
String path = "Z:/leds";

//USB configuration
String usb_name = "ULed";
int serial_wait_delay = 1000;

//File
PrintWriter file;

//Serial
boolean status_serial = false;
int inByte = 0;
Serial arduino;
long lastTime = 0;
String COM = "";
String serialPort;
int leds[] = { 0,0,0,0,0};

//Find first serial port who answer "W"
void searchSerial() {

  for (String serialPort : Serial.list()) {
    print(serialPort + " -> ");


    try {
      arduino = new Serial(this, serialPort, 115200);
    }
    catch (Exception e) {
      println("Bad");
      //e.printStackTrace();
    }
    send(usb_name);
    if (status_serial) {
      println("OK");
      delay(1000);
      break;
    } else {
      println("NO");
    }
    //println(status_serial);
  }
}

//Send a message to the Arduino and wait for "OK"
void send(String message) {
  status_serial = false;
  lastTime = millis();
  boolean wait = true;
  while (wait) {
    if (millis() - lastTime > serial_wait_delay) {
      wait = false;
    }
    delay(100);
    arduino.write(message + "\n");
    //println(message);

    while (arduino.available() > 0) {
      //println("Waiting");
      String response = arduino.readString();
      //println(response);
      if (response.equals("OK")) {
        status_serial = true;
        wait = false;
      }
    }
  }
}

void checkFiles() {
  for (int i=1; i<=5; i++) {
    String filename = path + "/" + i + ".txt";
    String lines[] = loadStrings(filename);
    //println(filename);
    //println(lines[0]);
    try {
      int ledColor = int(lines[0]);
      if (leds[i-1] != ledColor) {
       
        println(i + "=>" + ledColor);
        println(leds[i-1]);
        println(ledColor);
        println(i + ";" + lines[0]);
        send(i + ";" + lines[0]);
      }
    leds[i-1] = ledColor;
  } 
  catch(Exception e) {
  }
}
}


void setup() {
  println("OpenLightHUD -----------");
  size(200, 300);
  surface.setResizable(true);
  surface.setTitle("OpenLightHUD");

  //Check and connect to serial
  searchSerial();
  println("Check File -------");
}

void draw() {
  if (status_serial) {
    checkFiles();
    delay(100);
  } else {
    if (COM != "") {
      arduino.stop();
      searchSerial();
    } else {
      println("NO openLightHUD founded");
      delay(1000);
      exit();
    }
  }
}