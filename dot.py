
import RPi.GPIO as GPIO
from random import randrange


class Dot ():
    gpio_pin = 0  # gpio pin each dot is connected to
    braille_dot = 0  # which dot out of 6 this object represents
    value = False       # whether the dot is active or not

    def __init__(self, dot, gpio_pin):
        self.braille_dot = dot
        self.gpio_pin = gpio_pin

        
        GPIO.setup(gpio_pin, GPIO.OUT)
        GPIO.output(gpio_pin, GPIO.LOW)

        self.update_value()

    def get_value(self):
        return self.value

    def update_value(self):
        # TODO : Read from the specified GPIO pin
        current_val = GPIO.input(self.gpio_pin)

        # print("Checking GPIO Pin {}".format(self.gpio_pin))

        if current_val:
             self.value = 1
        else:
             self.value = 0
        

    def get_current_value(self):
        self.update_value()
        return self.get_value()
