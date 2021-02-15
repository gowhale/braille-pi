#Program Name: gpio_test_all.py
#Description: This program tests all the GPIO input beens to see whether they are able to read a signal


import RPi.GPIO as GPIO
import time

pins = [
    27,
    17,
    16,
    22,
    26,
    21]

TIME_BETWEEN_READINGS = 0.1


GPIO.setmode(GPIO.BCM)
# Setup your channel

for gpio_pin in pins:
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)


# GPIO.setup(20, GPIO.OUT)
# GPIO.output(20, GPIO.HIGH)


for i in range(1000):

    time.sleep(TIME_BETWEEN_READINGS)
    for pin_id in range (0,len(pins)):
        if GPIO.input(pins[pin_id]):
            print("{} Pin {} is HIGH".format(pin_id, pins[pin_id]))
        else:
            print(pins[pin_id], "Low")


print("Reading temp")
