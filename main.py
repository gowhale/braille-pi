from character import BrailleCharacter
from time import sleep
from alphabet import Alphabet

current_char = BrailleCharacter()
braille_alphabet = Alphabet

for _ in range (100):
    current_dots_hash = (current_char.get_current_dots_hash())

    sleep(0.1)