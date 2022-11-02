import time
import board
import pwmio
import max7219
from adafruit_max7219 import matrices
# import json
from board import *
# import adafruit_requests as requests
# import adafruit_espatcontrol.adafruit_espatcontrol_socket as socket
# from adafruit_espatcontrol import adafruit_espatcontrol
from adafruit_onewire.bus import OneWireBus
import adafruit_ds18x20
from adafruit_ds18x20 import DS18X20

# spi = busio.SPI(board.GP13);
# cs = digitalio.DigitalInOut(board.GP13)

# display = max7219.Matrix8x8(spi, digitalio.DigitalInOut(board.GP11), 1)


# ow_bus = OneWireBus(board.GP16)
# devices = ow_bus.scan()
# fan = pwmio.PWMOut(board.GP14, frequency=1000)
# value = 65535
# fanTwo = pwmio.PWMOut(board.GP15, frequency=1000)


# for device in devices:
#     print("ROM = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code));

# ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])
# ds18b20 = DS18X20(ow_bus, ow_bus.scan()[0])


while True:
    print('Temperature: {0:0.3f} °C'.format(ds18b20.temperature))
    print(ds18b20.temperature)
    fan.duty_cycle = value
    fanTwo.duty_cycle = value
    time.sleep(0.4)








    # all lit up
    matrix.fill(True)
    matrix.show()
    time.sleep(0.5)

#     # all off
    matrix.fill(False)
    matrix.show()
    time.sleep(0.5)

    for i in range(8):
        matrix.pixel(1, i, 1)
        matrix.show()
        time.sleep(0.5)
#     # now scroll the column to the right
    for j in range(8):
        matrix.scroll(1, 0)
        matrix.show()
        time.sleep(0.5)

#     # show a string one character at a time
    adafruit = "Adafruit"
    for char in adafruit:
        matrix.fill(0)
        matrix.text(char, 0, 0)
        matrix.show()
        time.sleep(1.0)

#    # scroll the last character off the display
    for i in range(8):
        matrix.scroll(-1, 0)
        matrix.show()
        time.sleep(0.5)

#     # scroll a string across the display
    for pixel_position in range(len(adafruit) * 8):
        matrix.fill(0)
        matrix.text(adafruit, -pixel_position, 0)
        matrix.show()
        time.sleep(0.25)
