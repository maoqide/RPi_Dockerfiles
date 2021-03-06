import RPi.GPIO as GPIO
import motoctl_pwm
import ocr
import paho.mqtt.client as mqtt
import sys,time

if len(sys.argv) == 5:
    MQTT_BROKER = sys.argv[1]
    MQTT_PORT = int(sys.argv[2])
    MQTT_KEEPALIVE_INTERVAL = int(sys.argv[3])
    MQTT_TOPIC = sys.argv[4]
else:
    print "usage: sudo python control.py MQTT_BROKER MQTT_PORT MQTT_KEEPALIVE_INTERVAL MQTT_TOPIC"
    sys.exit(1)

led=16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)               #led pin


# set pin header, (IN1, IN2, IN3, IN4, ENA, ENB)
moto = motoctl_pwm.Moto(6, 13, 19, 26, 21, 20)

#MQTT_BROKER = "192.168.10.245"
#MQTT_PORT = 1883
#MQTT_KEEPALIVE_INTERVAL = 30
#MQTT_TOPIC = "test"

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
    #Subscribe to a the Topic
    mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"

# Define on_message event Handler
def on_message(mosq, obj, msg):
    print msg.topic, msg.payload
    sys.stdout.flush()			#flush stdout buffer
    if msg.payload == "1":
        #time.sleep(1)
        action()

def action():
    img=ocr.capture()
    try:
        text=ocr.tesseract(img).encode("ascii")	# the instruction get from camera
    except:
        return
    instruction=filter(str.isalpha, text).lower()	# trim error ocr characters.

    # fuzzy match instruction for higher success rate
    if (instruction in "forward" and len(instruction) > 3 and instruction != "ward"):
        print "action: ", text, instruction
        GPIO.output(led, 1)
        moto.forward()
        time.sleep(1)
        moto.stop()
        GPIO.output(led, 0)
    elif (instruction in "backward" and len(instruction) > 3 and instruction != "ward"):
        print "action: ", text, instruction
        GPIO.output(led, 1)
        moto.backward()
        time.sleep(1)
        moto.stop()
        GPIO.output(led, 0)
    elif (instruction in "left" and len(instruction) > 2):
        print "action: ", text, instruction
        GPIO.output(led, 1)
        moto.left()
        time.sleep(1)
        moto.stop()
        GPIO.output(led, 0)
    elif (instruction in "right" and len(instruction) > 2):
        print "action: ", text, instruction
        GPIO.output(led, 1)
        moto.right()
        time.sleep(1)
        moto.stop()
        GPIO.output(led, 0)
    else:
        print text, ", action not allowed."

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
    GPIO.cleanup()

