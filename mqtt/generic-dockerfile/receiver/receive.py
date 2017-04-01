import sys
import time
import paho.mqtt.client as mqtt

if len(sys.argv) == 5:
    MQTT_BROKER = sys.argv[1]
    MQTT_PORT = int(sys.argv[2])
    MQTT_KEEPALIVE_INTERVAL = int(sys.argv[3])
    MQTT_TOPIC = sys.argv[4]
else:
    print "usage: sudo python receive.py MQTT_BROKER MQTT_PORT MQTT_KEEPALIVE_INTERVAL MQTT_TOPIC"
    sys.exit(1)

# Define Variables
#MQTT_BROKER = "192.168.10.245"
#MQTT_PORT = 1883
#MQTT_KEEPALIVE_INTERVAL = 45
#MQTT_TOPIC = "test/#"

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	#Subscribe to a the Topic
	mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"

# Define on_message event Handler
def on_message(mosq, obj, msg):
	print msg.topic, ": ", msg.payload
        sys.stdout.flush()

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue the network loop
mqttc.loop_forever()
