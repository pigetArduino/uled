#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example application for Universal Led 
# http://github.com/pigetArduino/UniversalLed
# Author : Rémi Sarrailh (madnerd.org)
# Licence : MIT

from tkinter import *
import serial
from serial.tools import list_ports
import time
from threading import Thread
from functools import partial

global arduino
global isconnected
global status

#Change device_name to detect another device
# Device name CH340 is arduino nano clone
# Device type is sent to the arduino and it should answer return_string
# Baudrate : Should be 9600 or 115200
device_name = "CH340"
device_type = "ULed"
return_string = "OK"
baudrate = 115200

status_text = "Searching..."
color_dict = { "off":0, "white":1, "red":2, "green":3, "blue":4, "yellow":5, "orange":6, "purple":7}
inv_color_dict = {v: k for k, v in color_dict.items()}

# Improvement for ui
bg_windows = "#ffffff"
bg_button = "#f3f3f3"
fg_button = "#757575"

######################
# Open USB Led       #
######################
def change_color(nb_led, color):
	message = str(nb_led)+":"+str(color_dict[color])
	print(message)
	write(message)

#################
#  Arduino      #
#################

# Write to Arduino
def write(string):
	global arduino
	try:
		arduino.write(string.encode())
	except:
		print("Error cannot write to arduino")


# Manage arduino connection in a thread
def arduino_manager():
	global arduino
	arduino = search_arduino()
	#print(arduino)

# Detect Arduino Nano Clone 
def search_arduino():
	global arduino
	devices = list(list_ports.grep(device_name))
	#devices = list(list_ports.comports())
	
	#We search each serial ports with CH340g chip
	for device in devices:
		print("Connected to " + str(device[0]))
		change_status("Searching : " + device[0])

		print(device[0])
		print(device[1])
		print(device[2])

		arduino = get_arduino_type(device[0])

		# If we found the correct arduino we return the serial connection
		if arduino:
			change_status("Connected")
			print("Connected to " + device_type)
			return arduino
			break;

	change_status("No device founded")

# Check if arduino is the droids humm the arduino you're looking for
def get_arduino_type(port):
	global arduino
	arduino = serial.Serial(port,baudrate,timeout=1)
	#print(arduino)
	
	#(workaround for windows, this slow down detection a lot)
	#But without this the connection will not be established
	time.sleep(0.9)
	arduino.setDTR(False)
	time.sleep(0.9)

	#Write device type to arduino
	write(device_type)
	#We flush the arduino so it won't send multiples times OK
	arduino.flush()

	#We get the answer
	answer = arduino.readline()
	if answer.decode() == return_string:
		return arduino
	else:
		#If the answer isn't correct close the serial connection.
		print("Serial device answer is " + answer.decode())
		arduino.close()
		return False

#####################
# GUI               #
#####################

# Change the status label
def change_status(string):
	try:
		status.config(text=string)
	except:
		print("Label wasn't ready when updated")

# We use a callback when we quit the application so 
# we can correctly close the arduino connection
def quit_callback():
	global arduino
	print("Application is stopped")
	try:
		arduino.close()
	except:
		print("Arduino was not gracefully closed")
	root.destroy()

# This function generate buttons and commands with arguments
# We need to use partial to programatically create the commands
def generate_led_buttons(row):
	# Common Design for buttons 
	border=3
	relief="sunken"
	w=2
	h=1
	# We used the color scheme of bootstrap
	bg=["BLACK","WHITE","#d9534f","#5cb85c","#428bca",'#FFFF9D','#f0ad4e','#9b59b6']
	Label(frame_commands,bg=bg_button,fg=fg_button,text=str(row+1)).grid(row=row,column=0)
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

	
# Create interface
root = Tk()
root.title(device_type)

#Background color
root.configure(background=bg_button) 
#Icon
root.iconbitmap('ul.ico')

# Callback when application is closed
root.protocol("WM_DELETE_WINDOW", quit_callback)

# GUI

# Led control
frame_commands = Frame(root)
frame_commands.grid(row=0)

generate_led_buttons(0) 
generate_led_buttons(1)
generate_led_buttons(2)
generate_led_buttons(3)
generate_led_buttons(4)

# Status label
frame_status = Frame(root)
frame_status.grid(row=1)
status = Label(frame_status,bg=bg_button,fg="red",text=status_text)
status.grid()

# Search arduino as soon as the gui is created
# We use a thread or the gui will be blocked by the function
search_thread = Thread(target = arduino_manager)
# Avoid thread to prevent application from stopping
search_thread.daemon = True
search_thread.start()

# Start application
try:
	root.mainloop()
except:
	#If something go wrong we try to close the serial connection correctly
	try:
		arduino.close()
	except:
		print("Arduino Not gracefully closed")
		print("Application was forced to stop")
