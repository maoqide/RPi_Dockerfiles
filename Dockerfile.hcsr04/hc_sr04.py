import RPi.GPIO as GPIO
import time
import sys

if len(sys.argv) == 3:
    TRIG = int(sys.argv[1])
    ECHO = int(sys.argv[2])
else:
    print "usage: sudo python hc_sr04.py pinGPIO_TRIG# pinGPIO_ECHO#"
    sys.exit(1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#TRIG = 23
#ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

#print "Waitng For Sensor To Settle"
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150
distance = round(distance, 2)

if distance > 2 and distance < 400:
    print distance - 0.5
else:
    print -1
