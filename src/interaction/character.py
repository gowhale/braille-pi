import RPi.GPIO as GPIO
from src.interaction.dot import Dot


class BrailleCharacter ():
    dots = []  # List of Dot objects
    dots_hash = "000000"  # dots values concatanted, 1 means high, 0 means low
    # hashmap maps out which gpio represents which pin
    dot_to_gpio_map = {1: 27,
                       2: 17,
                       3: 16,
                       4: 22,
                       5: 26,
                       6: 21
                       }

    def __init__(self):

        # Creates 6 dot objecets representing the braille char
        for d in range(1, 7):
            self.dots.append(Dot(d, self.dot_to_gpio_map[d]))

        self.update_dots_hash()

    def refresh_dots(self):
        for d in range(0, 6):
            self.dots[d].update_value()

    def update_dots_hash(self):
        new_dots_hash = ""
        for d in range(0, len(self.dots)):
            new_dots_hash += str((self.dots[d].get_value()))
        self.dots_hash = new_dots_hash

    def get_dots_hash(self):
        return self.dots_hash

    def get_current_dots_hash(self):
        self.refresh_dots()
        self.update_dots_hash()
        return self.dots_hash
