import RPi.GPIO as GPIO
import sys
import time

if len(sys.argv) == 3:
    pir = int(sys.argv[1])
    action = int(sys.argv[2])
    print action
else:
    print "usage: sudo python laser.py pinGPIO# action#"
    sys.exit(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pir, GPIO.OUT)               #set relay output
GPIO.output(pir, action)		#Turn ON/OFF relay
