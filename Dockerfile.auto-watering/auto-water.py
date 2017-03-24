import RPi.GPIO as GPIO
import time, sys

#GPIO_FLOW = 12
#GPIO_SOIL = 20

if len(sys.argv) == 3:
    GPIO_FLOW = int(sys.argv[1])
    GPIO_SOIL = int(sys.argv[2])
else:
    print "usage: sudo python auto-water.py GPIO_FLOW GPIO_SOIL"
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
#global soil_signal
#soil_signal = 0		# humid, need not water
global last_signal
last_signal = 1			# last one signal to pass to relay, 0 to start pump.

def countPulse(channel):
    global count
    global time_start
    global flow_signal
    count = count + 1
    count_time = (time.time() - time_start)

    if count_time  >= 10.0:

        # count = 98 * flow (L/min) * time (s)
        flow=int(count / 980)
        

        if flow > 2:
            flow_signal = 1
        else:
            flow_signal = 0
        
	# re initialization
        count = 0
        count_time = 0
        time_start = time.time()

GPIO.add_event_detect(GPIO_FLOW, GPIO.RISING, callback=countPulse)

while True:
    try:
        if (GPIO.input(GPIO_SOIL) and flow_signal):

            if last_signal:
                print 0					### 0 to tell relay to start pump
            last_signal = 0

        else:
            print 1					### 1 to stop
            last_signal = 1

        sys.stdout.flush()	#flush stdout buffer
        time.sleep(1)
    except:
        GPIO.cleanup([GPIO_FLOW, GPIO_SOIL])

