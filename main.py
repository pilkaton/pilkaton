#!/usr/bin/env python

import time
import grovepi
from ultrasonic import *
from lcd import Lcd

class Printer:
  def notify(self, event):
    print event

printer = Printer()
lcd = Lcd()

left = Ultrasonic(8, [printer, lcd])
#right = Ultrasonic(9, [printer])

left.handle()

