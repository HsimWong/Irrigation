import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

while True:
    if GPIO.input(21) == GPIO.LOW:
        print("wet")
    else:
        print("dry")
    time.sleep(1)

