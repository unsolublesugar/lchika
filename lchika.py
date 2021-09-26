#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

COUNT = 3
PIN = 11
SLEEP = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.OUT)
for _ in range(COUNT):
    GPIO.output(PIN,True)
    time.sleep(SLEEP)
    GPIO.output(PIN,False)
    time.sleep(SLEEP)
GPIO.cleanup()