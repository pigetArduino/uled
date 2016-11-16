Universal Led Test
-------------------
![ULed python app](https://github.com/pigetArduino/universalLed/raw/master/doc/ul_app.png)

This application doesn't do much things right now    
It allows you to test the leds   
This is a good example to autodetect specific arduino (this was tested with multiples serial devices/arduino plugged)
There are still a lot of room for improvements   

Next version will implement 
* websocket
* pixel detection for custom HUD in games
* file modification trigger (share leds as file using samba/windows share)
* Whatever you want!

SCREENSHOT

You can easily improve it to do anything 
Download link: LINK

# Build it yourself!

# Download
* Download python 3 : https://www.python.org/downloads/
* You need to add python in your PATH during install!


# Dependencies
* Open a command prompt (Windows Key + cmd)
tkinter (used gui) is bundled with python
```
pip install pyserial
```

# Start application
python ul.py

# Compile application
You will need pyinstaller to create an executable
Don't forget to add the icon file with it in /dist
```
pip install pyinstaller
```
You can use compile.bat or 
```
pyinstaller --onefile --noconsole --icon=ul.ico ul.py 
```
If you want to debug the application
```
pyinstaller --onefile ul.py 
```

# Licences
Icon by jpapun
Creative Commons Attribution (by)
Link : http://findicons.com/icon/158595/device_and_hardware

Software by Rémi Sarrailh (madnerd.org)
Licence: MIT
