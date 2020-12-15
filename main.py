import RPi.GPIO as GPIO
from character import BrailleCharacter
from time import sleep
from alphabet import Alphabet

GPIO.setmode(GPIO.BCM)

current_char = BrailleCharacter()
braille_alphabet = Alphabet()


for _ in range(1000):
    current_dots_hash = (current_char.get_current_dots_hash())
    braille_translation = braille_alphabet.translate_braille_to_alphabet(
        current_dots_hash)
    print("{} : {}".format(current_dots_hash, braille_translation))
    sleep(1)
