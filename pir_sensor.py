#!/usr/bin/env python

# PIR Sensor
# 25/04/2014

# Import RPi.GPIO libary as 'IO'
import RPi.GPIO as IO

# Define GPIO pin on Raspberry Pi
PIR=7

IO.setmode(IO.BCM)
IO.setup(PIR, IO.IN)

# Define 'motion_sense' function to detect movement
def motion_sense(PIR):
	print "Motion detected.."

# Main Program start
try:
	IO.add_event_detect(PIR, IO.RISING, callback=motion_sense)
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	print "\nQuitting.."
finally:
	IO.cleanup()

