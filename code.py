import busio
import digitalio
import time
import board
from board import *
from adafruit_max7219 import matrices
from adafruit_onewire.bus import OneWireBus
import adafruit_ds18x20
from adafruit_ds18x20 import DS18X20
import pwmio
# https://github.com/adafruit/Adafruit_CircuitPython_MAX7219/tree/main/examples
# https://learn.adafruit.com/adafruit-led-backpack/downloads?view=all

mosi = GP7
clk = GP6
cs = digitalio.DigitalInOut(GP5)
spi = busio.SPI(clk, MOSI=mosi)

fan = digitalio.DigitalInOut(GP15)
# fan.direction = digitalio.Direction.OUTPUT
# fan.value = False


print("Hello World")

# ow_bus = OneWireBus(board.GP17);
# devices = ow_bus.scan()
fan = pwmio.PWMOut(board.GP14, frequency=1000)
# value = 65535
# fanTwo = pwmio.PWMOut(board.GP15, frequency=1000)

# ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])
# ds18b20 = DS18X20(ow_bus, ow_bus.scan()[0])

# matrix = matrices.Matrix8x8(spi, cs)

# matrix.brightness = 1

while True:
    fan.led.duty_cycle = 65535
    
#     RightEye = "."
#     LeftEye = "."
#     RightEyeClosed = "'"
#     LeftEyeClosed = "`"
#     MouthHappy = ")"
#     MouthSad = "("
#     MouthNeut = "|"
#     Tear = "."
#     Temp = str(round(ds18b20.temperature))  + "'C"
#     Motivation = "Good Job"
#     fanStatus = "Fan On"
#     fan.value = True

#     while round(ds18b20.temperature) < 28:
#         print('Temperature: {0:0.3f} °C'.format(ds18b20.temperature))
#         print('happy')
#         for i in range(20):
#             matrix.fill(0)
#             matrix.text(LeftEye, -1, 0)
#             matrix.text(RightEye, -1, -4)
#             matrix.text(MouthHappy, 3, 1)
#             matrix.show()
#             time.sleep(0.5)
#             matrix.fill(0)
#             matrix.text(LeftEye, 0, 0)
#             matrix.text(RightEye, 0, -4)
#             matrix.text(MouthHappy, 3, 1)
#             matrix.show()
#             time.sleep(0.5)
#             if i == (round(ds18b20.temperature) * 2) + 2:
#                 for pixel_position in range(len(Motivation) * 8):
#                     matrix.fill(0)
#                     matrix.text(Motivation, -pixel_position, 0)
#                     matrix.show()
#                     time.sleep(0.1)
#         for pixel_position in range(len(Motivation) * 8):
#                 matrix.fill(0)
#                 matrix.text(str(round(ds18b20.temperature))  + "'C", -pixel_position, 0)
#                 matrix.show()
#                 time.sleep(0.10)


#     while round(ds18b20.temperature) > 22:
#         print('Temperature: {0:0.3f} °C'.format(ds18b20.temperature))
#         print('sad')
#         for i in range(20):
#             matrix.fill(0)
#             matrix.text(LeftEye, 0, 1)
#             matrix.text(RightEye, 0, -3)
#             matrix.text(MouthSad, 4, 1)
#             matrix.text(Tear, -2, -6)
#             matrix.show()
#             time.sleep(0.7)
#             matrix.fill(0)
#             matrix.text(LeftEye, 0, -1)
#             matrix.text(RightEye, 0, -5)
#             matrix.text(MouthSad, 4, 1)
#             matrix.text(Tear, -2, 2)
#             matrix.show()
#             time.sleep(0.7)
#             matrix.fill(0)
#         for pixel_position in range(len(Motivation) * 8):
#             matrix.fill(0)
#             matrix.text(fanStatus, -pixel_position, 0)
#             matrix.show()
#             time.sleep(0.1)
#         for pixel_position in range(len(Motivation) * 8):
#             matrix.fill(0)
#             matrix.text(str(round(ds18b20.temperature))  + "'C", -pixel_position, 0)
#             matrix.show()
#             time.sleep(0.1)
    # scroll a string across the display

