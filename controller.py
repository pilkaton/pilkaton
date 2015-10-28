#!/usr/bin/env python

import time
import grovepi

# SIG,NC,VCC,GND
sensor = 8

grovepi.pinMode(sensor,"INPUT")

while True:
    try:
        # Sensor returns LOW and onboard LED lights up when the
        # received infrared light intensity exceeds the calibrated level
        if grovepi.digitalRead(sensor) == 0:
            print ("found something")
        else:
            print ("nothing")

        time.sleep(.5)

    except IOError:
        print ("Error")
