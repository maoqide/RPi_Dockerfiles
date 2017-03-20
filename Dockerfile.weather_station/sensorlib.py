import RPi.GPIO as GPIO
import Adafruit_DHT
import sys
import time
import g3

# rain
def read_rain(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    res = GPIO.input(pin)
    GPIO.cleanup(pin)
    return res

# dht
def read_dht(sensor, pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        h=int(humidity)
        t=int(temperature)
        res=[h,t]
        return res
    else:
        print('Err!')
        sys.exit(1)

# dht return string
def read_dht_str(sensor, pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return '{0:0.1f},{1:0.1f}'.format(temperature, humidity)
    else:
        print('Err!')
        sys.exit(1)

# pm25
def read_pm():
    air = g3.g3sensor()
    return air.read("/dev/ttyAMA0")

# pm25 return str
def read_pm_str():
    air = g3.g3sensor()
    data=air.read("/dev/ttyAMA0")
    return ",".join(str(d) for d in data)

