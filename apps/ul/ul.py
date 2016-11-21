#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example application for Universal Led 
# Doc : http://github.com/pigetArduino/UniversalLed
# Author : Rémi Sarrailh (madnerd.org)
# Licence : MIT

# Arduino communication is completely managed by arduino module
# If connection is lost it will try to reconnect

from tkinter import *
import time
from threading import Thread
from functools import partial

from lib import USB

# Change device_name to detect another device
# Device name CH340 is arduino nano clone
# Device type is sent to the arduino and it should answer return_string
# Baudrate : Should be 9600 or 115200
device_name = "CH340"
device_type = "ULed"
device_return_string = "OK"
device_baudrate = 115200

# Bootstrap color for ui
bg_grey = "#f3f3f3"

######################
# Universal Led      #
######################
color_dict = { "off":0, "white":1, "red":2, "green":3, "blue":4, "yellow":5, "orange":6, "purple":7}
inv_color_dict = {v: k for k, v in color_dict.items()}

def change_color(nb_led, color):
	message = str(nb_led)+":"+str(color_dict[color])
	print(message)
	usb.write(message)

def animate_leds():
	for nb in range(1,6): 
		change_color(nb,"white")
	for nb in range(1,6): 
		change_color(nb,"off")

def animate_leds2():
	for nb in range(1,6): 
		change_color(nb,"red")
	for nb in range(1,6): 
		change_color(nb,"off")
	for nb in range(1,6): 
		change_color(nb,"green")
	for nb in range(1,6): 
		change_color(nb,"blue")
	for nb in range(1,6): 
		change_color(nb,"yellow")
	for nb in range(1,6): 
		change_color(nb,"off")

#####################
# GUI Functions     #
#####################
# We use a callback when we quit the application so 
# we can correctly close the arduino connection
def quit_callback():
	try:
		usb.close()
	except:
		print("Arduino was not gracefully closed")
	root.destroy()

# This function generate buttons and commands with arguments
# We need to use partial to programatically create the commands
def generate_led_buttons(row):
	# Common Design for buttons 
	border=3
	relief="sunken"
	fg_button = "#757575"
	w=2
	h=1
	# We used the color scheme of bootstrap
	bg=["BLACK","WHITE","#d9534f","#5cb85c","#428bca",'#FFFF9D','#f0ad4e','#9b59b6']
	Label(frame_commands,bg=bg_grey,fg=fg_button,text=str(row+1)).grid(row=row,column=0)
	for nb in range(8):
		nb_without0 = nb+1
		Button(frame_commands,
			text='', 
			relief=relief,
			fg=fg_button,
			bg=bg[nb],
			borderwidth=border,
			width=w,height=h,
			font=("Helvetica",11),
			command=partial(change_color,(row+1),inv_color_dict[nb])).grid(row=row,column=(nb+1))


# GUI

# Create interface
root = Tk()
root.title(device_type) #Title
root.configure(background=bg_grey) #Background color
root.iconbitmap('ul.ico') #Icon

# Callback when application is closed
root.protocol("WM_DELETE_WINDOW", quit_callback)

#################
# Buttons Frame #
#################
frame_commands = Frame(root)
frame_commands.grid(row=0)

generate_led_buttons(0) 
generate_led_buttons(1)
generate_led_buttons(2)
generate_led_buttons(3)
generate_led_buttons(4)

####################
# Custom buttons   #
####################

frame_animate = Frame(root)
frame_animate.grid(row=1)

Button(frame_animate,
			text='Animation', 
			relief="sunken",
			fg="grey",
			bg="white",
			borderwidth=3,
			font=("Helvetica",11),
			command=animate_leds).grid(row=1,column=0)

Button(frame_animate,
			text='Animation 2', 
			relief="sunken",
			fg="grey",
			bg="white",
			borderwidth=3,
			font=("Helvetica",11),
			command=animate_leds2).grid(row=1,column=1)

#################
# Status Frame  #
#################

frame_status = Frame(root)
frame_status.grid(row=2)
status = Label(frame_status,bg=bg_grey,fg="red",text="Searching...")
status.grid()

# Search arduino as soon as the gui is created
# We use a thread or the gui will be blocked by the function
# We passed the status label object, you can remove this if you don't want to
usb = USB.Device(device_name,device_type,device_return_string,device_baudrate,status)

# Start application (if something bad happens close arduino connection)
try:
	root.mainloop()
except:
	print("Application was forced to stop")
	try:
		#If something go wrong we try to close the serial connection correctly
		usb.close()
	except:
		print("Arduino Not gracefully closed")
