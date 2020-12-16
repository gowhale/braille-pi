import RPi.GPIO as GPIO
from character import BrailleCharacter
from time import sleep
from alphabet import Alphabet
from gui import Gui
import pygame
from speech import Speech

GPIO.setmode(GPIO.BCM)

current_char = BrailleCharacter()
braille_alphabet = Alphabet()

show_gui = True

speech = Speech()

try:
    display = Gui()

except pygame.error:
    print("No gui available")
    show_gui = False

for _ in range(1000):
    current_dots_hash = (current_char.get_current_dots_hash())

    if show_gui:
        display.draw_dot_hash(current_dots_hash)

    braille_translation = braille_alphabet.translate_braille_to_alphabet(
        current_dots_hash)

    speech.say(braille_translation)

    print("{} : {}".format(current_dots_hash, braille_translation))
    sleep(1)
