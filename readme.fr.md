ULed
-----

[English](https://github.com/pigetArduino/uled/)

![Photo ULed](https://github.com/pigetArduino/uled/raw/master/doc/universalLed_photo.jpg)   
Universal Led est un périphérique USB crée à partir d'un Arduino nano (clone) tour contrôler facilement 5 leds sur Windows        
Démonstration : https://www.youtube.com/watch?v=hgvi46x4oaE

![ULed App](https://github.com/pigetArduino/uled/raw/master/doc/ul_app11.png)   
Vous pouvez choisir 6 couleurs pour chaque leds. (Blanc/Rouge/Vert/Bleu/Jaune/Orange/Violet)

# Utilisation
* Installer les pîlotes de l'arduino nano (clone ch340g) : http://nano.madnerd.org
* Télécharger le code arduino/python : http://uled.madnerd.org
* Téléverser le croquis **uled.ino**
* Télécharger l'application : http://uledapp.madnerd.org    

Comment installer les pilotes ?: https://www.youtube.com/watch?v=m3CsftsfiQU

# Composants
* Arduino nano CH340G: 2€
* 30 leds WS2812B : 4.50€ ( 5 leds :0.75€)
* Resistor pack 400pcs (3€) (1 resistor: 0.0071€)
* Total : 9.5€ (2.75€)

# Branchement
Explication du Branchement : https://www.youtube.com/watch?v=hgvi46x4oaE

N'utilisez pas plus de 5 leds sans une alimentation dédié, ou vous risquez d'endommager les leds
Chaque leds peuvent consommer jusqu'à **60ma** à pleine puissance   
Un Arduino peut fournir jusqu'à **500ma** (sur la broche 5v/Gnd pin)   
```5 leds = 5x60ma = 300ma ```  
Source:
https://learn.adafruit.com/adafruit-neopixel-uberguide/basic-connections

* D6 --> RESISTANCE (470Ohm) DI
* +5V --> 5V
* GND --> GND

![Wiring_uled](https://github.com/pigetArduino/uled/raw/master/doc/universalLed_wiring.png)

# Impression 3D
Ce modèle est un boitier utilisable pour de petits projects à base d'arduino nano   
Modèle par Olivier Sarrailh : https://github.com/pigetArduino/uled/tree/master/3D    
Vous devrez limer un trou pour faire passer les câbles du strip de led (voir Explications du Branchement)

# Créer sa propre application
* Aller voir ce tutoriel: https://github.com/pigetArduino/utest/blob/master/README.fr.MD
* Le code source est disponible dans **apps/utest**

# Commandes disponibles
Vous pouvez tester ce périphérique dans le moniteur série du logiciel Arduino
Baudrate : 115200 / No Line Ending   

* ULed --------> Vérifie si c'est le bon périphérique (et éteint les leds)
* X:Y -------> Où X est la led et Y la couleur)
* 1:3 -------> (led 1 Vert)

# Color
* 0 : OFF
* 1 : Blanc/ON
* 2 : Rouge
* 3 : Vert
* 4 : Bleu
* 5 : Jaune
* 6 : Orange
* 7 : Violet

# Licences
Icône par jpapun
License: Creative Commons Attribution (by)   
Lien : http://findicons.com/icon/158595/device_and_hardware

Logiciel par Rémi Sarrailh (madnerd.org)   
License: MIT

