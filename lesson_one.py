# Essential Imports
import time
from speech import Speech
import pygame
from gui import Gui
from alphabet import Alphabet
from time import sleep
from error_logger import ErrorLogger


class LessonOne ():
    # def __init__(self):
    def __init__(self):
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

        # If the pi is being used initiate the pins
        if using_raspberry_pi:
            GPIO.setmode(GPIO.BCM)
            current_char = BrailleCharacter()

        # Initialising objects
        braille_alphabet = Alphabet()
        speech = Speech()

        # Introduction to Lesson 1 and the importance of Braile...
        speech.say("Welcome to your first Braille lesson!")
        speech.say("Braille changes lives. It gives thousands of people independence, learning, literacy, and the enjoyment of reading. Braille opens doors, and gives hope and inspiration.")
        speech.say("""Popular games (such as Bingo and Uno) are available in braille and others can be adapted by the addition of braille labels, enabling a blind or partially sighted individual to join in with family or friends in a wide range of leisure pursuits.""")
        # Content source: https://www.rnib.org.uk/braille-and-moon-%E2%80%93-tactile-codes-braille-past-present-and-future/modern-day-braille
        # Last accessed: 03/03/2021

        # Attempt to show GUI
        try:
            show_gui = True
            graphical_user_interface = Gui()
        except pygame.error:
            print("No gui available")
            show_gui = False
            error_log.log_error("No gui available")

        previous_letter = "_"
        previous_time = time.time()

        # Forever loop which will ONLY exit if the program is ended
        while 1:

            if using_raspberry_pi:
                # Get dot hash from pins
                current_dots_hash = (current_char.get_current_dots_hash())
            else:
                # Get dot hash from keyboard
                current_dots_hash = check_keys(pygame, dot_has_test)

            # Check if enough time has passed to update GUI
            now = time.time()
            difference = float(now-previous_time)
            if difference > 0.5:
                # speech.say(current_dots_hash)
                braille_translation = braille_alphabet.translate_braille_to_alphabet(
                    current_dots_hash)
                previous_time = now
                if show_gui:
                    graphical_user_interface.draw_dot_hash(
                        current_dots_hash, "")

                if previous_letter != braille_translation:
                    if braille_translation != "_":
                        speech.say(braille_translation)
                    previous_letter = braille_translation

                print("{} : {}".format(current_dots_hash, braille_translation))

        graphical_user_interface.close_gui()

    def play(self):
        print("Let's begin...")
