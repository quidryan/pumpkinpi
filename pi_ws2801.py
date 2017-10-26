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

def face(pixels, lefteye, righteye, mouth):
    pixels.set_pixel(0, Adafruit_WS2801.RGB_to_color(lefteye[0], lefteye[1], lefteye[2]))
    pixels.set_pixel(1, Adafruit_WS2801.RGB_to_color(righteye[0], righteye[1], righteye[2]))

    mouthcolor = Adafruit_WS2801.RGB_to_color(mouth[0], mouth[1], mouth[2])
    for i in range(2, pixels.count()):
        pixels.set_pixel(i, mouthcolor)

    pixels.show()
 
if __name__ == "__main__":
    # Clear all the pixels to turn them off.
    pixels.clear()

    red = webcolors.name_to_rgb('red')
    blue = webcolors.name_to_rgb('blue')

    flash_face(pixels, red, red, blue)
    #flash_face(pixels, (255, 0, 0), (255, 0, 0), (0, 255, 255))
