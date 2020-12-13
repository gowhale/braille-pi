import RPi.GPIO as GPIO
from character import BrailleCharacter
from time import sleep

GPIO.setmode(GPIO.BCM)  

current_char = BrailleCharacter()


for _ in range (100):
    print(current_char.get_current_dots_hash())
    sleep(0.1)
