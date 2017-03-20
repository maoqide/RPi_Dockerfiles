import sensorlib
import sys

DHT_TYPE=22
print sensorlib.read_dht_str(DHT_TYPE, int(sys.argv[1]))
