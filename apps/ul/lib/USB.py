###########################
#  Arduino Management     #
###########################

import serial
from serial.tools import list_ports
from threading import Thread
import time


class Device:
	# Change the status label if it is sent to the manager
	def __init__(self,device_name,device_type,device_return_string,device_baudrate,label=False):
		self.name = device_name
		self.type = device_type
		self.baudrate = device_baudrate
		self.return_string = device_return_string
		self.status = label
		self.arduino = False
		self.isConnected = False

		search_thread = Thread(target = self.manager)
		search_thread.daemon = True #If thread is not a daemon application could crashed
		search_thread.start()


	def change_status(self,string):
		if self.status:
			try:
				self.status.config(text=string)
			except:
				print("Label wasn't ready when updated")
		else:
			print(string)

	# Manage arduino connection in a thread
	def manager(self):
		self.arduino = self.search()
		#print(arduino)

	# Write to Arduino
	def write(self,string):
		try:
			if self.isConnected:
				self.arduino.write(string.encode())
				time.sleep(0.020)
			else:
				print("Waiting for connection dismissed message...")
		except:
			#If message was not send correctly we try to reconnect
			if self.isConnected:
				self.isConnected = False
				print("Error cannot write to arduino")
				search_thread = Thread(target = self.manager)
				search_thread.daemon = True #If thread is not a daemon application could crashed
				search_thread.start()

	def close(self):
		self.arduino.close()

	# Detect Arduino Nano Clone and automatically reconnect
	def search(self):
		if not self.isConnected:
			devices = list(list_ports.grep(self.name))
			#devices = list(list_ports.comports())
		
			#We search each serial ports with CH340g chip
			for device in devices:
				print("Connected to " + str(device[0]))
				self.change_status("Searching : " + device[0])

				print(device[0])
				print(device[1])
				print(device[2])

				self.arduino = self.get_type(device[0])

				# If we found the correct arduino we return the serial connection
				if self.arduino:
					self.change_status("Connected")
					print("Connected to " + self.type)
					self.isConnected = True
					break;
			if not self.isConnected:
				self.change_status("No device founded")
		time.sleep(1)
		self.search()	


	# Check if arduino is the droids humm the arduino you're looking for
	def get_type(self,port):
		try:
			self.arduino = serial.Serial(port,self.baudrate,timeout=2)
		except:
			print("Arduino wasn't opened correctly")
		#print(arduino)
		
		if self.arduino:
			#(workaround for windows, this slow down detection a lot)
			#But without this the connection will not be established
			time.sleep(1)
			
			self.arduino.setDTR(False)
			#We flush the arduino so it won't send multiples times OK
			self.arduino.flush()
			time.sleep(1)
		
			#Write device type to arduino
			try:
				self.arduino.write(self.type.encode())
				answer = self.arduino.read(2)
				print("Serial: " + answer.decode())
				if answer.decode() == self.return_string:
					return self.arduino
				else:
					#If the answer isn't correct close the serial connection.
					self.arduino.close()
					return False
			except:
				print("Error writing to arduino")
				return False

			#We get the answer		
		else:
			return False