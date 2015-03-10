import grovepi
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

      except TypeError:
        print ("Error")
      except IOError:
        print ("Error")


#kogut = DigitalPrinter(2)
#buzz = DigitalPrinter(2)
#goalkeeper1  = Pir(5, [kogut])
#goalkeeper2  = Pir(6, [kogut])
#goalkeeper1.handle()
#goalkeeper2.handle()

