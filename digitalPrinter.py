#!/usr/bin/env python

import time
import grovepi
import threading

class DigitalPrinter(threading.Thread):
  def __init__(self, port):
    self.port = port

  def handle(self, seconds):
    try: 
      grovepi.pinMode(self.port, "OUTPUT")
      #time.sleep(1)

      grovepi.digitalWrite(self.port, 1)
      time.sleep(seconds)

    except IOError:
      print ("Error")
   
    grovepi.digitalWrite(self.port, 0)

  def notify(self, seconds):
    t = threading.Thread(target = self.handle, args = [seconds])
    t.daemon = True
    t.start()

#kogut = DigitalPrinter(8)
#buzz = DigitalPrinter(2)

#kogut.notify(5)
#buzz.notify(5)
#time.sleep(10)

