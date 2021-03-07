# Essential Imports
import time
import pygame
from time import sleep

from src.interaction.speech import Speech
from src.interaction.gui import Gui
from src.braille.alphabet import Alphabet
from src.error_reporting.error_logger import ErrorLogger

class Interaction ():
    """A class which allows software to interact with the users enviroment. I.e. via audio, visuals and haptics.
    """

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
            from src.interaction.keyboard_interface import check_keys
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

        # Attempt to show GUI
        try:
            show_gui = True
            graphical_user_interface = Gui()
        except pygame.error:
            print("No gui available")
            show_gui = False
            error_log.log_error("No gui available")

        self.pygame = pygame
        self.error_log = error_log
        self.show_gui = show_gui
        if show_gui:
            self.graphical_user_interface = graphical_user_interface

        self.speech = speech
        self.braille_alphabet = braille_alphabet

        self.using_raspberry_pi = using_raspberry_pi

        if using_raspberry_pi:
            self.current_char = current_char
        else:
            self.dot_has_test = dot_has_test
            self.check_keys = check_keys

# test = Interaction()
