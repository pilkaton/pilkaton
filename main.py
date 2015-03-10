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
lcd = Lcd()

leftGoals = GoalCounter()
rightGoals = GoalCounter()

leftPir = Pir(5, [printer, leftGoals])
rightPir = Pir(6, [printer, rightGoals])

leftPir.start()
rightPir.start()

while True:
  time.sleep(1)
  lcd.notify(str(leftGoals.goals()) + " - " + str(rightGoals.goals()))

