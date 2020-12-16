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

speech = Speech()

show_gui = True

try:
    display = Gui()

except pygame.error:
    print("No gui available")
    show_gui = False
    
previous_letter = "_"
for _ in range(600):
    current_dots_hash = (current_char.get_current_dots_hash())

    braille_translation = braille_alphabet.translate_braille_to_alphabet(
        current_dots_hash)


    if show_gui:
        display.draw_dot_hash(current_dots_hash, braille_translation)



    if previous_letter != braille_translation:
        speech.say(braille_translation)
        previous_letter = braille_translation

    print("{} : {}".format(current_dots_hash, braille_translation))
    sleep(0.1)

display.close_gui()
