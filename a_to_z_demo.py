# PROGRAM : CYCLES THROUGH FILES A-Z TO TEST SOFTWARE SIDE OF SYSTEM

from character import BrailleCharacter
from time import sleep
from alphabet import Alphabet
from gui import Gui
import pygame
from speech import Speech

braille_alphabet = Alphabet()

show_gui = True

speech = Speech()

try:
    display = Gui()

except pygame.error:
    print("No gui available")
    show_gui = False


chars = braille_alphabet.get_alphabet_to_braille()
chars_keys = list(chars.keys())
sorted(chars_keys)
for char in (chars_keys):
    current_dots_hash = (chars[char])

    if show_gui:
        display.draw_dot_hash(current_dots_hash)

    braille_translation = braille_alphabet.translate_braille_to_alphabet(
        current_dots_hash)

    speech.say(braille_translation)

    print("{} : {}".format(current_dots_hash, braille_translation))

