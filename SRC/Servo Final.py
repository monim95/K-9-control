#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

import cgitb
cgitb.enable(1,'/var/log/apache2/')

try:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(21,GPIO.OUT)
	p = GPIO.PWM(21,50)
	p.start(0)

	p.ChangeDutyCycle(10)
	time.sleep(4)
	p.ChangeDutyCycle(6.8)
	time.sleep(0.5)


	p.stop()
	GPIO.cleanup()

	print("\nContent-Type: text/html;charset=utf-8\n")
	print("Sirviendo alimento!!!")
except Exception:
	print("\nContent-Type: text/html;charset=utf-8\n\n")
	print("No hay alimento!!! :-s")

