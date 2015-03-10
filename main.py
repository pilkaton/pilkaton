#!/usr/bin/env python

import time
import grovepi
from pir import *
from lcd import Lcd
from stats import GoalCounter
from anhem import Anhem

class Logger:
  def notify(self, event):
    print "GOAL!"

logger = Logger()
lcd = Lcd()
kogut = DigitalPrinter(8)
anhem = Anhem(4)

leftGoals = GoalCounter()
rightGoals = GoalCounter()

leftPir = Pir(5, [logger, leftGoals, kogut, anhem])
rightPir = Pir(6, [logger, rightGoals, kogut, anhem])

leftPir.start()
rightPir.start()

while True:
  time.sleep(1)
  lcd.notify(str(leftGoals.goals()) + " - " + str(rightGoals.goals()))

