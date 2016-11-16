Universal Led is an USB device to easily control 5 leds with a computer

![Photo ULed](https://github.com/pigetArduino/universalLed/raw/master/doc/universalLed_photo.jpg)

You can choose 6 color for each leds.
All the controls are managed with applications which will be added in this repo.

As for now the application is only compatible with Windows, but it shouldn't be hard   
to convert it into a Linux/MacOSx application   

* Download Arduino nano clone drivers : http://nano.madnerd.org/

# Applications available
* Test your device : LINK
* A prototype for network control of the led with files and Health bar HUD for Heroes of the storm : LINK  

# Components
* Arduino nano CH340G: 2€
* 30 leds WS2812B : 4.50€ ( 5 leds :0.75€)
* Total : 6.5€ (2.75€)

# Wiring
Warning : Do not connect more than 5 leds or the arduino won't be able to power them correctly   
I test it with 30 leds and now they are unable to correctly change the color.   
* D6 --> RESISTOR (470Ohm) DI
* +5V --> 5V
* GND --> GND

![Wiring_uled](https://github.com/pigetArduino/universalLed/raw/master/doc/universalLed_wiring.png)

# Commands available
You can test the device in Arduino software   
Baudrate : 115200 / No Line Ending   

* UL --------> Check if device is correct
* X:Y -------> (Where X is the led and Y the color)
* 1:3 -------> (led 1 Green)
* X  --------> (Where X is the led) Turn off led

# Color
* 0 : OFF
* 1 : White/ON
* 2 : Red
* 3 : Green
* 4 : Blue
* 5 : Yellow
* 6 : Orange
* 7 : Purple

Do not used more than 5 leds without a dedicated power supply or this can damage the leds   
(I tried it and now I have 15 leds that won't change to the correct color)    

