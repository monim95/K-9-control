#!/usr/bin/env python
import RPi.GPIO as GPIO    
import time

import cgitb
cgitb.enable(1,'/var/log/apache2/')

GPIO.setmode(GPIO.BOARD)   
GPIO.setup(13,GPIO.OUT)   

GPIO.output(13, GPIO.HIGH)
time.sleep (15)
GPIO.output(13, GPIO.LOW)
time.sleep(1)

print("\nContent-Type: text/html;charset=utf-8\n")
print("Sirviendo agua!!!")
GPIO.cleanup()  
