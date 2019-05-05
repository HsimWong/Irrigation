from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24)

while True:
    print("The distance to nearest object is ", sensor.distance, 'm')
    sleep(1)
