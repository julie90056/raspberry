#!/usr/bin/python3
#https://sites.google.com/site/rasberrypintust/raspberry-pi-shu-mei-pai-shi-qian-zhun-bei/python-gipo-an-zhuang
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
print("17 27亮")
GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)