import RPi.GPIO as GPIO
import sys
import time
import paho.mqtt.client as mqtt

#MQTT_BROKER = "192.168.10.245"
#MQTT_PORT = 1883
#MQTT_KEEPALIVE_INTERVAL = 30
#MQTT_TOPIC = "test/sensorname"

if len(sys.argv) == 7:
    pir = int(sys.argv[1])
    MQTT_BROKER = sys.argv[2]
    MQTT_PORT = int(sys.argv[3])
    MQTT_KEEPALIVE_INTERVAL = int(sys.argv[4])
    MQTT_TOPIC = sys.argv[5]
    SIGNAL_DO = int(sys.argv[6])
else:
    print "usage: sudo python publish.py GPIO_PIN MQTT_BROKER MQTT_PORT MQTT_KEEPALIVE_INTERVAL MQTT_TOPIC SIGNAL_DO"
    sys.exit(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)

if GPIO.input(pir):
    print 1
    MQTT_MSG = 0 ^ SIGNAL_DO
else:
    print 0
    MQTT_MSG = 1 ^ SIGNAL_DO
print "MQTT_MSG: ", MQTT_MSG

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
    print "Connected to MQTT Broker"

# Define on_publish event Handler
def on_publish(client, userdata, mid):
    print "Message Published..."

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

# Publish message to MQTT Topic
mqttc.publish(MQTT_TOPIC,MQTT_MSG)

# Disconnect from MQTT_Broker
mqttc.disconnect()

GPIO.cleanup(pir)

