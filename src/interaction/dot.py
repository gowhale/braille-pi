
import RPi.GPIO as GPIO
from random import randrange


class Dot ():
    """This class links the hardware's dots to the code's dots.

    Attributes:
        gpio_pin      (Int)     Value of the GPIO pin each dot is connected to.
        braille_dot   (Int)     Which dot out of 6 this object represents.
        value         (Boolean) Whether the dot is active or not."""

    gpio_pin = 0  
    braille_dot = 0  
    value = False       

    def __init__(self, dot, gpio_pin):
        """Initialises the Dot class.

        Parameters:
            dot         (Int)     Value of the GPIO pin each dot is connected to.
            gpio_pin    (Int)     Which dot out of 6 this object represents."""

        self.braille_dot = dot
        self.gpio_pin = gpio_pin

        GPIO.setup(gpio_pin, GPIO.OUT)
        GPIO.output(gpio_pin, GPIO.LOW)

        self.update_value()

    def get_value(self):
        """Gets the value of the physcical button. i.e. high or low"""

        return self.value

    def update_value(self):
        """Updates the Dot's registered value."""

        current_val = GPIO.input(self.gpio_pin)

        if current_val:
            self.value = 0
        else:
            self.value = 1

    def get_current_value(self):
        """Updates the Dot's value and then returns it."""

        self.update_value()
        return self.get_value()
