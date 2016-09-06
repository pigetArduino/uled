/*
*    Heroes of the Storm Life Status 
 *    Required: OpenLightHUD
 *   Only tested on 1920x1080, fake fullscreen
 */

import java.awt.*;
import processing.serial.*;

//File
int id_led = 1;
String path = "Z:/ledManager";

boolean debug = false; //Debug mode

//Life bar pixels position (we assume Y won't change)
int pos_lifebar_y = 977;
int pos_lifebar_75 = 390;
int pos_lifebar_50 = 330;
int pos_lifebar_25 = 300;
int pos_lifebar_0 = 240;

//Hex color of life pixel when full
String lifeColor = "FF4EDB1C";
String deadColor = "FF180C21";
String nexusColor = "FF0C0C18";

//Life bar 1 pixel screenshot
PImage image_lifebar_75;
PImage image_lifebar_50;
PImage image_lifebar_25;
PImage image_lifebar_0;

int lifeStatus = -1;

// File
PrintWriter file;
String filename = path + "/" + id_led + ".txt";


//Write a message to a file
void send(String message) {
  file = createWriter(filename);
  file.print(message);
  file.close();
}

void setup() {
  println("OpenLightHUD -----------");
  println("File: " + filename);
  //GUI setup
  size(200, 300);
  surface.setResizable(true);
  surface.setTitle("HOTS");

  //Search and connect to serial
  println("Health Bar -------");
}

void draw() {
    analysePixels();
   
    //Debug GUI display
    if (image_lifebar_75 != null) {
      image(image_lifebar_75, 0, 0, 100, 100);
    }
    if (image_lifebar_50 != null) {
      image(image_lifebar_50, 0, 100, 100, 100);
    }
    if (image_lifebar_25 != null) {
      image(image_lifebar_25, 0, 200, 100, 100);
    }
    delay(0);     //Delay to reduce CPU usage (TODO: test it)
}

//This is where the pixels are analyse, as much pixel as you want
void analysePixels() {
  try {

    //Screenshot
    image_lifebar_75 = new PImage(new Robot().createScreenCapture(new Rectangle(pos_lifebar_75, pos_lifebar_y, 1, 1)));
    image_lifebar_50 = new PImage(new Robot().createScreenCapture(new Rectangle(pos_lifebar_50, pos_lifebar_y, 1, 1)));
    image_lifebar_25 = new PImage(new Robot().createScreenCapture(new Rectangle(pos_lifebar_25, pos_lifebar_y, 1, 1)));
    image_lifebar_0 = new PImage(new Robot().createScreenCapture(new Rectangle(pos_lifebar_0, pos_lifebar_y, 1, 1)));

    //Color in hexa
    String lifebar_75  = hex(image_lifebar_75.get(0, 0));
    String lifebar_50  = hex(image_lifebar_50.get(0, 0));
    String lifebar_25  = hex(image_lifebar_25.get(0, 0));
    String lifebar_0   = hex(image_lifebar_0.get(0, 0));
    
    //100
    if (lifebar_75.equals(lifeColor)) {
      if (lifeStatus != 100) {
        lifeStatus = 100;
        println(lifeStatus);
        send("0");
      }
    }

    //75
    if (lifebar_50.equals(lifeColor) && ! lifebar_75.equals(lifeColor)) {
      if (lifeStatus != 75) {
        lifeStatus = 75; 
        println(lifeStatus);
        send("3");
      }
    }

    //50
    if (lifebar_25.equals(lifeColor) && ! lifebar_50.equals(lifeColor)) {
      if (lifeStatus != 50) {
        lifeStatus = 50;           
        println(lifeStatus);
        send("5");
      }
    }

    //25
    if (lifebar_0.equals(lifeColor) && ! lifebar_25.equals(lifeColor)) {
      if (lifeStatus != 25) {
        lifeStatus = 25;
        println(lifeStatus);
        send("2");
      }
    }

    //0
    if (lifebar_75.equals(deadColor) && ! lifebar_0.equals(lifeColor)) {
      if (lifeStatus != 0) {
        lifeStatus = 0;
        println(lifeStatus);
        send("4");
      }
    }
    
    if (lifebar_50.equals(nexusColor) && ! lifebar_25.equals(lifeColor)){
      if (lifeStatus != -2) {
        lifeStatus = -2;
        println(lifeStatus);
        send("7");
      }
    }

    if (debug) {
      print(lifebar_75 + ";");
      print(lifebar_50 + ";");
      println(lifebar_25);
    }
  } 
  catch (AWTException e) {
    println("Processing Pixels ERROR -----------");
    println(e);
  }
}