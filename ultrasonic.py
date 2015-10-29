import grovepi

class Ultrasonic(port):
  
  def handle(self):
    
    while True:
      try:
        print (grovepi.ultrasonicRead(port))

      except TypeError:
        print ("Error")
      except IOError:
        print ("Error")

ultrasonic = new Ultrasonic(8)
ultrasonic.handle()
