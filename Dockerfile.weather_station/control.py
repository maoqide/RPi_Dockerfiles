import sensorlib
import sys

if len(sys.argv) == 5:
    pin_dht = int(sys.argv[1])
    pin_rain = int(sys.argv[2])
    PM25_THRESHOLD = int(sys.argv[3])
    TEMP_THRESHOLD = int(sys.argv[4])
else:
    print "usage: sudo python control.py pin_dht pin_rain PM25_THRESHOLD TEMP_THRESHOLD"
    sys.exit(1)

#print sensorlib.read_rain(17)
#print sensorlib.read_dht(22, 4)
#print sensorlib.read_pm()

DHT_TYPE=22
#rain=sensorlib.read_rain(17)
temp=sensorlib.read_dht(DHT_TYPE, 4)[1]
pm25=sensorlib.read_pm()[2]

if temp is not None and pm25 is not None:
#    print temp,pm25
    if (pm25 > PM25_THRESHOLD) or (temp > TEMP_THRESHOLD):
        print 1
    else:
        print 0
