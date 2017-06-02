import RPi.GPIO as GPIO
import sys
import time
import paho.mqtt.client as mqtt

if len(sys.argv) == 7:
    pir = int(sys.argv[1])
    MQTT_BROKER = sys.argv[2]
    MQTT_PORT = int(sys.argv[3])
    MQTT_KEEPALIVE_INTERVAL = int(sys.argv[4])
    MQTT_TOPIC = sys.argv[5]
    SIGNAL_DO = int(sys.argv[6])
else:
    print "usage: sudo python subscribe.py GPIO_PIN MQTT_BROKER MQTT_PORT MQTT_KEEPALIVE_INTERVAL MQTT_TOPIC SIGNAL_DO"
    sys.exit(1)

# Define Variables
#MQTT_BROKER = "192.168.10.245"
#MQTT_PORT = 1883
#MQTT_KEEPALIVE_INTERVAL = 45
#MQTT_TOPIC = "test/#"
MSGS = {}

# GPIO settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.OUT)               #set relay output

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
    #Subscribe to a the Topic
    mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"

# Define on_message event Handler
def on_message(mosq, obj, msg):
    global MSGS
    action = 0
    print msg.topic, msg.payload
    if msg.payload != "1" and msg.payload != "0":
        print "error message: ", msg.payload 
        return
    MSGS[msg.topic] = int(msg.payload)
    for topic in MSGS:
        action = (MSGS[topic] | action)

    if SIGNAL_DO == 0:
        action = 1 ^ action

    print "action: ", action
    GPIO.output(pir, action)	#Turn ON/OFF relay

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue the network loop
try:
    mqttc.loop_forever()
finally:
    print "cleanup GPIO..."
    GPIO.cleanup(pir)
