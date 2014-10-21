#!/usr/bin/python
import cwiid
import time

# Connect to the Wii Remote. 

class Wiimote:

	wiimote = ""

	def connect_wiimote():
		try:
			print 'Press 1 + 2 on your Wii Remote now ...'
			time.sleep(1)
			wiimote = cwiid.Wiimote()
		except RuntimeError:
			return connect_wimote()

		print 'Wii Remote connected...\n'
		wiimote.led = 6
		wiimote.rpt_mode = cwiid.RPT_BTN

	def validate_connection():
		try:
			wiimote.request_status()
		except RuntimeError:
			print "Disconnected - reconnecting"
			wiimote = connect_wimote()

	def connection_fun():
		time.sleep(1)
		for i in range(4):
			wiimote.rumble = True
			time.sleep(.1)
			wiimote.rumble = False
			time.sleep(.1)
		wiimote.led = 0
		time.sleep(1)
		for i in [1, 2, 4, 8, 4, 2, 1, 2, 4, 8, 4, 2, 1, 2, 4, 8, 4, 2, 1, 0]:
			wiimote.led = i
			time.sleep(.1)
		wiimote.led = 6
		wiimote.rpt_mode = cwiid.RPT_BTN

	def get_buttons():
		return wiimote.state['buttons']