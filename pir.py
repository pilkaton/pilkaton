import grovepi
from threadPrinter import DigitalPrinter

class Pir:

  def __init__(self, port, subscribers):
    self.port = port
    self.subscribers = subscribers
    print self.limit
  
  def handle(self):
    while True:
      try:
        value = grovepi.ultrasonicRead(self.port)
        if value < self.limit: # GOAL!!
          print "gooooool!!!!!", value, self.limit
          for s in self.subscribers: # notify
            s.notify(2) 

      except TypeError:
        print ("Error")
      except IOError:
        print ("Error")


kogut = DigitalPrinter(2)
#buzz = DigitalPrinter(2)
goalkeeper1  = Ultrasonic(8,[kogut])
goalkeeper2  = Ultrasonic(7,[kogut])
goalkeeper1.handle()
goalkeeper2.handle()
