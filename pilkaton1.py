#!/usr/bin/env python
import skywriter
import signal
import time
import grovepi
from digitalPrinter import DigitalPrinter

some_value = 5000


kogut = DigitalPrinter(7)

@skywriter.move()
def move(x, y, z):
  print('goooooooool!')
  kogut.notify(5)

#@skywriter.flick()
#def flick(start,finish):
#  print('Got a flick!', start, finish)
#  grovepi.digitalWrite(relay,0)
#
#@skywriter.airwheel()
#def spinny(delta):
#  global some_value
#  some_value += delta
#  if some_value < 0:
#  	some_value = 0
#  if some_value > 10000:
#    some_value = 10000
#  print('Airwheel:', some_value/100)
#  grovepi.digitalWrite(relay,1)
#
#@skywriter.double_tap()
#def doubletap(position):
#  print('Double tap!', position)
#
#@skywriter.tap()
#def tap(position):
#  print('Tap!', position)
#
#@skywriter.touch()
#def touch(position):
#  print('Touch!', position)

signal.pause()
