import RPi.GPIO as GPIO
import sys
import time

if len(sys.argv) == 2:
    pir = int(sys.argv[1])
else:
    print "usage: sudo python sr501.py pinNum"
    sys.exit(1)
GPIO.setmode(GPIO.BCM)
#pir = 10
GPIO.setup(pir, GPIO.IN)                       
#print "Waiting for sensor to settle"
time.sleep(2)
#print "Detecting motion"
#while True:
#   if GPIO.input(pir):
#      print 1,
#      #time.sleep(3)
#   else:
#      print 0,
#   time.sleep(0.5)
if GPIO.input(pir):
    print 1
else:
    print 0
time.sleep(0.1)
