Heroes of the Storm Led HUD
---------------------------

This is a prototype, don't expect it to works out of the box.   
This will be deprecated for a better version that doesn't require processing    

# Usage
There is two applications, you need to use both to use it with Heroes of the storm   
UniversalFile2Led can be used alone.   

You will need processing : https://processing.org/download/

## UniversalFile2led
This application will read the text file in Z:\leds (you can change easily change this)
You need to create 1.txt/2.txt/3.txt/4.txt/5.txt
Each file represents a led, each times a file is modify the led will change color

## hots_life2file
This application will modify the text file to display your health status on 1 led in Heroes of the storm   
We detect specific pixel to do this on the screen   

* You need to change graphics settings as it won't work on fullscreen
* You need to have the application running on each computer and modify the led ID
* You need to share your folder to make it available to others player on your local network

Color : 
* Off ---> Full life
* Purple ---> Menu
* Green ---> 75%
* Yellow --> 50% 
* Red ---> 25%
* Blue ---> 0



