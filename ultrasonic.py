import grovepi

class Ultrasonic:

  def __init__(self, port, subscribers):
    self.port = port
    self.subscribers = subscribers
  
  def handle(self):
    while True:
      try:
        value = grovepi.ultrasonicRead(self.port)
        #if value < 10: # GOAL!!
        print "SSS", value
        for s in self.subscribers: # notify
          s.notify(value) 

      except TypeError:
        print ("Error")
      except IOError:
        print ("Error")

#t = threading.Thread(target=ultrasonic.handle)
#t.start()

