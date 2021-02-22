import RPi.GPIO as GPIO
from character import BrailleCharacter
from time import sleep
from alphabet import Alphabet
from gui import Gui
import pygame
from speech import Speech
from error_logger import ErrorLogger
import time

GPIO.setmode(GPIO.BCM)

current_char = BrailleCharacter()
braille_alphabet = Alphabet()

speech = Speech()

error_log = ErrorLogger()

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
    current_dots_hash = (current_char.get_current_dots_hash())

    braille_translation = braille_alphabet.translate_braille_to_alphabet(
        current_dots_hash)

    now = time.time()
    difference = float(now-previous_time)
    print(difference)
    if difference > 0.1:
        previous_time = now
        if show_gui:
            display.draw_dot_hash(current_dots_hash, braille_translation)

        if previous_letter != braille_translation:
            speech.say(braille_translation)
            previous_letter = braille_translation

        print("{} : {}".format(current_dots_hash, braille_translation))
        # sleep(0.1)


display.close_gui()
