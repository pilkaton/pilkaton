import grovepi
import time
import threading
from threadPrinter import DigitalPrinter

class Pir:

  def __init__(self, port, subscribers):
    self.port = port
    self.subscribers = subscribers
  
  def handle(self):
    grovepi.pinMode(self.port, "INPUT")
    while True:
      try:
        value = grovepi.digitalRead(self.port)
        if value: # GOAL!!
          print "gooooool!!!!!", value
          for s in self.subscribers: # notify
            s.notify(1)
        time.sleep(.2)
      except TypeError:
        print ("Error")
      except IOError:
        print ("Error")

  def start(self):
    t = threading.Thread(target = self.handle)
    t.daemon = True
    t.start()

