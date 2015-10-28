import grovepi

class Ultrasonic:

  def __init__(self, port):
    self.port = port
  
  def handle(self):
    while True:
      try:
        print (grovepi.ultrasonicRead(self.port))

      except TypeError:
        print ("Error")
      except IOError:
        print ("Error")

#t = threading.Thread(target=ultrasonic.handle)
#t.start()

