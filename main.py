#!/usr/bin/env python

import time
import grovepi
from pir import *
from lcd import Lcd
from stats import GoalCounter

class Printer:
  def notify(self, event):
    print event

printer = Printer()
#lcd = Lcd()

leftGoals = GoalCounter()
#rightGoals = GoalCounter()

left = Pir(5, [printer, leftGoals])
#right = Pir(6, [printer, rightGoals])

left.handle()
#right.handle()

