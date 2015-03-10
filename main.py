#!/usr/bin/env python

import time
import grovepi
from ultrasonic import *
from lcd import Lcd
from stats import GoalCounter

class Printer:
  def notify(self, event):
    print event

printer = Printer()
lcd = Lcd()

leftGoals = GoalCounter()
rightGoals = GoalCounter()

left = Pir(5, [printer, leftGoals])
right = Pir(6, [printer, rightGoals])
#right = Ultrasonic(9, [printer])

#left.handle()

