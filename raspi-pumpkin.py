#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
SENSOR_PORT = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PORT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

sensor_current = False
sensor_previous = False
while True:
    sensor_previous = sensor_current
    sensor_current = GPIO.input(SENSOR_PORT)
    if (sensor_current != sensor_previous):
        os.system('mpg123 -q binary-language-moisture-evaporators.mp3 &')
 
    sleep(0.1);
