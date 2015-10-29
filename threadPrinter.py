#!/usr/bin/env python

import time
import grovepi
import threading

class DigitalPrinter(threading.Thread):
  def __init__(self, port):
    self.port = port

  def handle(self, seconds):
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

  def notify(self, seconds):
    t = threading.Thread(target = self.handle, args = [seconds])
    t.daemon = True
    t.start()


#kogut = DigitalPrinter(7)
#buzz = DigitalPrinter(2)

#kogut.notify(5)
#buzz.notify(5)
#time.sleep(10)

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

