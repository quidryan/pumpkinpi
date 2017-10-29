# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO
import webcolors

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

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
    
def mouth_small(pixels, mouthcolor):
    pixels.set_pixel(pixels.count() - 2, mouthcolor)

def face(pixels, lefteye, righteye, mouth):
    mouthcolor = Adafruit_WS2801.RGB_to_color(mouth[0], mouth[1], mouth[2])
    for i in range(0, pixels.count()-2):
        pixels.set_pixel(i, mouthcolor)
    pixels.set_pixel(pixels.count()-1, Adafruit_WS2801.RGB_to_color(lefteye[0], lefteye[1], lefteye[2]))
    pixels.set_pixel(pixels.count()-2, Adafruit_WS2801.RGB_to_color(righteye[0], righteye[1], righteye[2]))


    pixels.show()

def iterate(pixels):
    colorRGB = webcolors.name_to_rgb('red')
    color = Adafruit_WS2801.RGB_to_color(colorRGB[0], colorRGB[1], colorRGB[2])

    for i in range(1, pixels.count()):
        pixels.clear()
        pixels.show()
        pixels.set_pixel(i, color)
        pixels.show()
        time.sleep(2)


if __name__ == "__main__":
    # Clear all the pixels to turn them off.
    pixels.clear()

    red = webcolors.name_to_rgb('red')
    orange = webcolors.name_to_rgb('orange')

    #flash_face(pixels, red, red, orange)
    iterate(pixels)
    #flash_face(pixels, (255, 0, 0), (255, 0, 0), (0, 255, 255))
