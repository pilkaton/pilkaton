#!/usr/bin/env python

import time
import grovepi

class Led:
  def __init__(self, port):
    self.port = port

  def notify(self, seconds):
    grovepi.pinMode(self.port, "OUTPUT")
    time.sleep(1)
    i = 0

    while i < seconds * 2:
      try:
        grovepi.analogWrite(self.port, 255)
        time.sleep(.5)
        i += 1 

      except KeyboardInterrupt:
        grovepi.analogWrite(self.port, 0)
        break
      except IOError:
        print ("Error")
    grovepi.analogWrite(self.port, 0)

led1 = Led(3)
led2 = Led(4)

led1.notify(5)
led2.notify(5)

