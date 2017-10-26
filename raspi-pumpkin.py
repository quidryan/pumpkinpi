#!/usr/bin/env python
 
import os
from time import sleep
from time import strftime
 
import RPi.GPIO as GPIO
 
SENSOR_PORT = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PORT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

sensor_current = False
sensor_previous = False

os.system('mpg123 -q Beep.mp3 &')

while True:
    sensor_previous = sensor_current
    sensor_current = GPIO.input(SENSOR_PORT)
    print(strftime("%I:%M:%S") + " - GPIO pin %s is %s" % (SENSOR_PORT, sensor_current))
    if (sensor_current==GPIO.HIGH and sensor_previous==GPIO.LOW):
        # Start sequence
        #os.system('mpg123 -q Beep.mp3 &')
        os.system('aplay police_s.wav &')
 
    sleep(0.5);
