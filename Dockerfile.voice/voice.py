import RPi.GPIO as GPIO
import sys
import time

if len(sys.argv) == 2:
    pir = int(sys.argv[1])
else:
    print "usage: sudo python voice.py pinGPIO#"
    sys.exit(1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)

if GPIO.input(pir):
    print 1
else:
    print 0
GPIO.cleanup(pir)

