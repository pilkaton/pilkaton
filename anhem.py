#!/usr/bin/env python

import time
import grovepi
import threading

class Anhem(threading.Thread):
  def __init__(self, port):
    self.port = port

  def handle(self, seconds):
    try: 
      grovepi.pinMode(self.port, "OUTPUT")
      self.beep(.2)
      self.beep(.2)
      self.beep(.1)
      self.beep(.1)
      self.beep(.1)
      time.sleep(.1)
      self.beep(.1)
      self.beep(.1)
      self.beep(.1)
      self.beep(.1)
      time.sleep(.1)
      self.beep(.1)
      self.beep(.1)
     
    except IOError:
      print ("Error")
   
    grovepi.digitalWrite(self.port, 0)

  def notify(self, seconds):
    t = threading.Thread(target = self.handle, args = [seconds])
    t.daemon = True
    t.start()

  def beep(self, sec):
    grovepi.digitalWrite(self.port, 1)
    time.sleep(sec)
    grovepi.digitalWrite(self.port, 0)
    time.sleep(sec)

anhem = Anhem(4)
anhem.handle(666)


#kogut = DigitalPrinter(7)
#buzz = DigitalPrinter(2)

#kogut.notify(5)
#buzz.notify(5)
#time.sleep(10)

