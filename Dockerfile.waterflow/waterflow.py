import RPi.GPIO as GPIO
import time, sys

if len(sys.argv) == 2:
    GPIO_FLOW = int(sys.argv[1])
else:
    print "usage: sudo python waterflow.py GPIO_FLOW"
    sys.exit(1)

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_FLOW, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# set up 
global count
count = 0
global time_start
global count_time
time_start= time.time()
count_time = 0
global flow

def countPulse(channel):
    global count
    global flow
    global time_start
    count = count + 1
    count_time = (time.time() - time_start)

    if count_time  >= 10.0:

        # count = 98 * flow (L/min) * time (s)
        flow=int(count / 980 * 1000 / 60)		# ml/s

        # print
        #print flow
        #sys.stdout.flush()      #flush stdout buffer

        # write to /var/log/waterflow.txt
        file= "/var/log/waterflow.txt"
	wstr=time.strftime("%s") + "," + str(flow)

        with open(file, "w") as f:
            f.write(wstr)

	# re initialization
        count = 0
        count_time = 0
        time_start = time.time()

GPIO.add_event_detect(GPIO_FLOW, GPIO.RISING, callback=countPulse)

while True:
    try:

        time.sleep(1)
    except:
        GPIO.cleanup(GPIO_FLOW)

