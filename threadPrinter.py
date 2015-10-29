#!/usr/bin/env python

import time
import grovepi
import threading

# Digital ports that support Pulse Width Modulation (PWM)
# D3, D5, D6

# Digital ports that do not support PWM
# D2, D4, D7, D8

class DigitalPrinter(threading.Thread):
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

  def print(self, seconds):
    t = threading.Thread(target = notify, args = (seconds))
    t.daemon = True
    t.start()


kogut = DigitalPrinter(2)
buzz = DigitalPrinter(7)

kogut.print(5)
buzz.print(5)
time.sleep(10)


#t1 = threading.Thread(target=kogut.notify, args = (5))
#t1.daemon = True
#t1.start()

#t2 = threading.Thread(target=buzz.notify, args = (5))
#t2.daemon = True
#t2.start()

#time.sleep(10)

#kogut.notify(5)
#buzz.notify(5)
#led2.notify(12)

