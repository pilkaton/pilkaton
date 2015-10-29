#!/usr/bin/env python

import time
import grovepi

# Digital ports that support Pulse Width Modulation (PWM)
# D3, D5, D6

# Digital ports that do not support PWM
# D2, D4, D7, D8

class Kogut:
  def __init__(self, port):
    self.port = port

  def notify(self, seconds):
    grovepi.pinMode(self.port, "OUTPUT")
    time.sleep(1)
    i = 0

    while i < seconds * 2:
      try:
        grovepi.digitalWrite(self.port, 1)
        time.sleep(.5)
        i += 1 

      except KeyboardInterrupt:
        grovepi.digitalWrite(self.port, 0)
        break
      except IOError:
        print ("Error")
   
    grovepi.digitalWrite(self.port, 0)

kogut = Kogut(7)
#led2 = Led(4)

kogut.notify(5)
#led2.notify(12)

