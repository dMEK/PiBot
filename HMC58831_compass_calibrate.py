# Based on
#
# http://blog.bitify.co.uk/2013/11/connecting-and-calibrating-hmc5883l.html
#

import smbus
import time
import math

bus = smbus.SMBus(1)
address = 0x1e

def write_byte(adr, value):
    bus.write_byte_data(address, adr, value)


def read_signed_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    if val > 32767:
       val = (65536-val)*-1.0
    return val*1.0

write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
write_byte(2, 0b00000000) # Continuous sampling

scale = 1.0
conv = 180/3.141529

minx = 0
maxx = 0
miny = 0
maxy = 0

for i in range(0,300):

    x = read_signed_word(3) * scale
    z = read_signed_word(5) * scale
    y = read_signed_word(7) * scale

    print i, x, y, z

    if (x < minx):
       minx = x
    if (x > maxx):
       maxx = x
    if (y < miny):
       miny = y
    if (y > maxy):
       maxy = y
    
    time.sleep(0.1)

print "x offset =",(minx+maxx)/2
print "y offset =",(miny+maxy)/2

print "**** DONE ****"



