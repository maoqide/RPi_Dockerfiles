import RPi.GPIO as GPIO
from time import sleep

class Moto():

    def __init__(self,out1,out2,out3,out4,ena,enb,freq=50):
        print "moto init..."
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.ena = ena
        self.enb = enb
        self.freq = freq
        self._setup()

    def _setup(self):
        GPIO.setup(self.out1, GPIO.OUT)
        GPIO.setup(self.out2, GPIO.OUT)
        GPIO.setup(self.out3, GPIO.OUT)
        GPIO.setup(self.out4, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.enb, GPIO.OUT)
        GPIO.output(self.ena, 1)
        GPIO.output(self.enb, 1)
        Moto._pa=GPIO.PWM(self.ena, self.freq)
        Moto._pb=GPIO.PWM(self.enb, self.freq)

    def stop(self):
        Moto._pa.stop()
        Moto._pb.stop()
        GPIO.output(self.out1, 0)
        GPIO.output(self.out2, 0)
        GPIO.output(self.out3, 0)
        GPIO.output(self.out4, 0)

    def forward(self, duty=50):
        Moto._pa.start(duty)
        Moto._pb.start(duty)
        GPIO.output(self.out1, 1)
        GPIO.output(self.out2, 0)
        GPIO.output(self.out3, 1)
        GPIO.output(self.out4, 0)

    def backward(self, duty=50):
        Moto._pa.start(duty)
        Moto._pb.start(duty)
        GPIO.output(self.out1, 0)
        GPIO.output(self.out2, 1)
        GPIO.output(self.out3, 0)
        GPIO.output(self.out4, 1)

    def right(self, duty=50):
        Moto._pb.start(duty)
        #_pb.ChangeDutyCycle(duty)
        GPIO.output(self.out1, 1)
        GPIO.output(self.out2, 0)
        GPIO.output(self.out3, 0)
        GPIO.output(self.out4, 0)

    def left(self, duty=50):
        Moto._pa.start(duty)
        #_pa.ChangeDutyCycle(duty)
        GPIO.output(self.out1, 0)
        GPIO.output(self.out2, 0)
        GPIO.output(self.out3, 1)
        GPIO.output(self.out4, 0)

    def cleanup(self):
        print "cleanup..."
        Moto._pa.stop()
        Moto._pb.stop()
        GPIO.cleanup()
