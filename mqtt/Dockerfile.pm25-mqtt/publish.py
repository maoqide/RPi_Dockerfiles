import sys
import paho.mqtt.client as mqtt

if len(sys.argv) == 6:
    MQTT_BROKER = sys.argv[1]
    MQTT_PORT = int(sys.argv[2])
    MQTT_KEEPALIVE_INTERVAL = int(sys.argv[3])
    MQTT_TOPIC = sys.argv[4]
    MQTT_MSG = sys.argv[5]
else:
    print "usage: sudo python publish.py MQTT_BROKER MQTT_PORT MQTT_KEEPALIVE_INTERVAL MQTT_TOPIC MQTT_MSG"
    sys.exit(1)

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


