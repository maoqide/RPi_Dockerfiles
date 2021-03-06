import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time, sys

#GPIO_FLOW = 12
#GPIO_SOIL = 20

if len(sys.argv) == 8:
    GPIO_FLOW = int(sys.argv[1])
    GPIO_SOIL = int(sys.argv[2])
    MQTT_BROKER = sys.argv[3]
    MQTT_PORT = int(sys.argv[4])
    MQTT_KEEPALIVE_INTERVAL = int(sys.argv[5])
    MQTT_TOPIC = sys.argv[6]
    FLOW_MIN = int(sys.argv[7])
else:
    print "usage: sudo python auto-water.py GPIO_FLOW GPIO_SOIL MQTT_BROKER MQTT_PORT MQTT_KEEPALIVE_INTERVAL MQTT_TOPIC FLOW_MIN"
    sys.exit(1)

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_FLOW, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GPIO_SOIL, GPIO.IN)

# set up 
global count
count = 0
global time_start
global count_time
time_start= time.time()
count_time = 0

global flow_signal
flow_signal = 1		# enough water, can start pump
#global last_signal
#last_signal = 1			# last one signal to pass to relay, 0 to start pump.

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
    print "Connected to MQTT Broker"

# Define on_publish event Handler
def on_publish(client, userdata, mid):
    print "Message Published..."

def countPulse(channel):
    global count
    global time_start
    global flow_signal
    count = count + 1
    count_time = (time.time() - time_start)

    if count_time  >= 10.0:

        # count = 98 * flow (L/min) * time (s)
        flow=int(count / 980 * 1000 / 60)
        print flow, "ml/s"
        sys.stdout.flush()

        if flow > FLOW_MIN:
            flow_signal = 1
        elif flow > 0:
            flow_signal = 0
        
	# re initialization
        count = 0
        count_time = 0
        time_start = time.time()

GPIO.add_event_detect(GPIO_FLOW, GPIO.RISING, callback=countPulse)

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

while True:
    try:
        soil = GPIO.input(GPIO_SOIL)
        print 'soil: ', soil, "flow: ", flow_signal
        if (soil and flow_signal):
            print 0					### 0 to tell relay to start pump
            MQTT_MSG=0
#            last_signal = 0

        else:
            print 1
            MQTT_MSG=1					### 1 to stop
#            last_signal = 1

        sys.stdout.flush()	#flush stdout buffer

        # Publish message to MQTT Topic
        mqttc.publish(MQTT_TOPIC,MQTT_MSG)

        time.sleep(1)
    except:
        print "exceptions.."
        GPIO.cleanup([GPIO_FLOW, GPIO_SOIL])
        # Disconnect from MQTT_Broker
        mqttc.disconnect()
        break
