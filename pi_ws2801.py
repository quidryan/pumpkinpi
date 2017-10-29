# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO
import webcolors

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

import os
from time import sleep
from time import strftime
import RPi.GPIO as GPIO

SENSOR_PORT = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sensor_current = False
sensor_previous = False

# Configure the count of pixels:
PIXEL_COUNT = 9
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

def flash_face(pixels, lefteye, righteye, mouth, blink_times=20):
    for i in range(blink_times):
        # blink two times, then wait
        pixels.clear()
        face(pixels, lefteye, righteye, mouth)
        time.sleep(0.5)

        pixels.clear()
        pixels.show()
        time.sleep(0.5)

def speak(pixels, eyes, mouth):
    eyecolor = Adafruit_WS2801.RGB_to_color(eyes[0], eyes[1], eyes[2])
    pixels.set_pixel(pixels.count()-1, eyecolor)
    pixels.set_pixel(pixels.count()-2, eyecolor)

    mouthcolor = Adafruit_WS2801.RGB_to_color(mouth[0], mouth[1], mouth[2])
    # Speak
    
def mouth_big(pixels, color):
    lightup(pixels, color, [0, 1, 2, 3, 4, 5, 6, 7, 8])

def mouth_normal(pixels, color):
    lightup(pixels, color, [1, 2, 3, 4, 5, 7, 8])

def mouth_small(pixels, color):
    lightup(pixels, color, [2, 3, 4, 7, 8])

def mouth_tiny(pixels, color):
    lightup(pixels, color, [3, 7, 8])

def mouth_none(pixels, color):
    lightup(pixels, color, [7, 8])

def lightup(pixels, mouthcolor, mouthpixels):
    pixels.clear()
    for i in mouthpixels:
        pixels.set_pixel(i, mouthcolor)
    pixels.show()
        
def face(pixels, lefteye, righteye, mouth):
    mouthcolor = Adafruit_WS2801.RGB_to_color(mouth[0], mouth[1], mouth[2])
    for i in range(0, pixels.count()-2):
        pixels.set_pixel(i, mouthcolor)
    pixels.set_pixel(pixels.count()-1, Adafruit_WS2801.RGB_to_color(lefteye[0], lefteye[1], lefteye[2]))
    pixels.set_pixel(pixels.count()-2, Adafruit_WS2801.RGB_to_color(righteye[0], righteye[1], righteye[2]))
    pixels.show()

def iterate(pixels):
    colorRGB = webcolors.name_to_rgb('orangered')
    color = Adafruit_WS2801.RGB_to_color(colorRGB[0], colorRGB[1], colorRGB[2])

    for i in range(0, pixels.count()):
        pixels.clear()
        pixels.show()
        pixels.set_pixel(i, color)
        print("Showing ", i)
        pixels.show()
        time.sleep(2)
    pixels.clear()
    pixels.show()

def hey(delay = 0.5):
    mouth_none(pixels, orange)
    time.sleep(delay)
    mouth_tiny(pixels, orange)
    time.sleep(delay * 0.9)
    mouth_small(pixels, orange)
    time.sleep(delay * 0.8)
    mouth_normal(pixels, orange)
    time.sleep(delay * 0.7)

    mouth_big(pixels, orange)
    time.sleep(delay * 0.6)

    mouth_normal(pixels, orange)
    time.sleep(delay * 0.7)
    mouth_small(pixels, orange)
    time.sleep(delay)
    mouth_tiny(pixels, orange)
    time.sleep(delay)
    mouth_none(pixels, orange)
    time.sleep(delay)

orange = webcolors.name_to_rgb('orange')

def scram():
    os.system('mpg123 -q HeyThereScram.mp3 &')
    hey(0.05)
    hey(0.1)
    hey(0.15)

    flash_face(pixels, red, red, red, 5)

if __name__ == "__main__":
    # Clear all the pixels to turn them off.
    pixels.clear()

    red = webcolors.name_to_rgb('red')
    orangeRGB = webcolors.name_to_rgb('orange')
    orange = Adafruit_WS2801.RGB_to_color(orangeRGB[0], orangeRGB[1], orangeRGB[2])

    #flash_face(pixels, red, red, orange)
    #iterate(pixels)
    #flash_face(pixels, (255, 0, 0), (255, 0, 0), (0, 255, 255))

    os.system('mpg123 -q Beep.mp3 &')

    while True:
        sensor_previous = sensor_current
        sensor_current = GPIO.input(SENSOR_PORT)
        print(strftime("%I:%M:%S") + " - GPIO pin %s is %s" % (SENSOR_PORT, sensor_current))
        if (sensor_current == GPIO.HIGH and sensor_previous == GPIO.LOW):
            scram()

        sleep(0.5);
