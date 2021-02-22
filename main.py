import time
from speech import Speech
import pygame
from gui import Gui
from alphabet import Alphabet
from time import sleep
from error_logger import ErrorLogger
error_log = ErrorLogger()
using_raspberry_pi = True

try:
    # Attempting to acces the GPIO Pins Module
    import RPi.GPIO as GPIO
    from character import BrailleCharacter
except ModuleNotFoundError as e:
    # If the system is unable to import the module it will revert to using the SDFJKL keys
    print("KEYBOARD MODE ACTIVATED")
    from keyboard_interface import check_keys
    using_raspberry_pi = False
    error_log.log_error(e)
    dot_has_test = {
        "F": 0,
        "D": 0,
        "S": 0,
        "J": 0,
        "K": 0,
        "L": 0
    }


if using_raspberry_pi:
    GPIO.setmode(GPIO.BCM)
    current_char = BrailleCharacter()

braille_alphabet = Alphabet()

speech = Speech()


show_gui = True

speech = Speech()

try:
    display = Gui()

except pygame.error:
    print("No gui available")
    show_gui = False
    error_log.log_error("No gui available")

previous_letter = "_"
previous_time = time.time()


while 1:

    if using_raspberry_pi:
        current_dots_hash = (current_char.get_current_dots_hash())
    else:
        current_dots_hash = "000000"
        current_dots_hash = check_keys(pygame, dot_has_test)

    now = time.time()
    difference = float(now-previous_time)
    # print(difference)
    if difference > 0.5:
        braille_translation = braille_alphabet.translate_braille_to_alphabet(
            current_dots_hash)
        previous_time = now
        if show_gui:
            display.draw_dot_hash(current_dots_hash, braille_translation)

        if previous_letter != braille_translation:
            if braille_translation != "_":
                speech.say(braille_translation)
            previous_letter = braille_translation

        print("{} : {}".format(current_dots_hash, braille_translation))
        # sleep(0.1)


display.close_gui()
