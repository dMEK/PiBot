# compass.py
#
# HMC8553L+ADXL345 based tilt compensated library
#
# William Henning from http://Mikronauts.com
#
# Based on
#
# http://blog.bitify.co.uk/2013/11/connecting-and-calibrating-hmc5883l.html
#

import smbus
import time
import math
import adxl345

bus = smbus.SMBus(1)
address = 0x1e

bus.write_byte_data(address, 0, 0b01110000) # Set to 8 samples @ 15Hz
bus.write_byte_data(address, 1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
bus.write_byte_data(address, 2, 0b00000000) # Continuous sampling

adxl = adxl345.ADXL345()

def read_signed_word(adr):   
    high = bus.read_byte_data(address, adr)
    low  = bus.read_byte_data(address, adr+1)
    val  = (high << 8) + low
    if val > 32767:
       val = (65536-val)*-1.0
    return val*1.0

def heading(decl):

    axes = adxl.getAxes(True)   

    x = axes['x']
    y = axes['y']
    z = axes['z']
                     
    roll  = math.asin( axes['y'])
    pitch = math.asin(-axes['x'])

    if ((roll>0.78) or (roll<-0.78) or (pitch>0.78) or (pitch<-0.78)):
        print "Pitch/Roll error"
        return -1000
        
    scale = 1.0

    x = read_signed_word(3) * scale - 2      # use calibrate.py to compute the x/y calibration for compass
    y = read_signed_word(7) * scale + 115
    z = read_signed_word(5) * scale

    xh = x * math.cos(pitch) + z * math.sin(pitch)
    yh = x * math.sin(roll) * math.sin(pitch) + y * math.cos(roll) - z * math.sin(roll) * math.cos(pitch)

    heading = math.atan2(yh, xh)

    if (heading < 0):
       heading = heading + 2*3.141529
       
    return (math.degrees(heading) + 360 - decl) % 360

def avg_heading(decl,samples):
    h = 0;
    for i in range(0,samples):
        h = h + heading(decl) 
    return h / samples
    
if __name__ == "__main__":
    
    print "True Heading =",avg_heading(16,5)

