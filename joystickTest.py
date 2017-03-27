# this is a wifi joystck testing script
# it used jstest-gtk for testing
# sudo apt-get install jstest-gtk for pi
# and jsLib https//gist.github.com/rdb/8864666

import PDALib2 as hobbit
import jsLib
import time

hobbit.RoboPiInit("/dev/ttyAMA0", 115200)

js = jsLib.joystick()
print "Device is: ",js.Name()

hobbit.motors()

hobbit.pinMode(0, hobbit.SERVO)
hobbit.servoWrite(0, 1500)

lfrac = 1
rfrac = 1

while True:
  got = js.Read()
  
  if got[0] == "LY":
    speed = int(got[1] * -255)
    hobbit.writeMotors(speed, speed)
    
  if got[0] = "RX":
    steer = got[1]
    print "Right joystick X = ",steer
    
  if steer < -0.9:
    hobbit.writeMotors(-speed, speed)
  elif steer < -0.1:
    hobbit.writeMotors(0, speed)
  elif steer > 0.9:
    hobbit.writeMotors(speed, -speed)
  elif steer > 0.1:
    hobbit.writeMotors(speed, 0)
  else:
    hobbit.writeMotors(speed, speed)
