import busio
import digitalio
from board import *
from adafruit_max7219 import matrices

# left eye open
matrix.pixel(1, 2, 1)	
matrix.pixel(2, 2, 1)
matrix.pixel(2, 1, 1)

# Right eye open
matrix.pixel(6, 1, 1)
matrix.pixel(6, 2, 1)	
matrix.pixel(5, 2, 1)
matrix.show()

#mouth
matrix.pixel(3, 6, 6)
matrix.pixel(4, 6, 6)	
matrix.pixel(5, 6, 6)
matrix.pixel(6, 5, 6)