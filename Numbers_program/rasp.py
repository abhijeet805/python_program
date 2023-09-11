import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

l0=14
l1=15
l2=18
l3=23
l4=24
l5=25
l6=8
l7=7

GPIO.setup(l0,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(l3,GPIO.OUT)
GPIO.setup(l3,GPIO.OUT)
GPIO.setup(l4,GPIO.OUT)
GPIO.setup(l5,GPIO.OUT)
GPIO.setup(l6,GPIO.OUT)
GPIO.setup(l7,GPIO.OUT)

while True:

    GPIO.output(l0,True)
    time.sleep(1)

    GPIO.output(l1,True)
    time.sleep(1)
    
    GPIO.output(l3,False)
    time.sleep(1)

    GPIO.output(l4,False)
    time.sleep(1)
     
    GPIO.output(l5,True)
    time.sleep(1)

    GPIO.output(l6,True)
    time.sleep(1)
    
