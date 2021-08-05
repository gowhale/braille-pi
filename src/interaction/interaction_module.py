# Essential Imports
import time
import pygame

from src.interaction.speech import Speech
from src.interaction.gui import Gui
from src.braille.alphabet import Alphabet
from src.error_reporting.error_logger import ErrorLogger


class Interaction ():
    """A class which allows software to interact with the users enviroment. I.e. via audio, visuals and haptics.

    Attributes:

        pygame                      (Pygame) Module used to display things to the screen 
        error_log                   (ErrorLogger) object used to log errors to a file
        show_gui                    (Boolean) Whether or not the code is able to access a screen
        graphical_user_interface    (Gui) Object regarding drawing objects to a screen
        speech                      (Speech) Object regarding speaking out loud strings
        braille_alphabet            (Alphabet) Object which can convert letters to braille codes
        using_raspberry_pi          (Boolean) Marks whether or not a Pi is being used to run code
        current_char                (BrailleCharacter) Used if Pi is hooked up to custom hardware
        key_presses                 (dict) Dictionary which counts amount of times keys pressed
        check_keys                  (Func) Checks which keys have been pressed and dothash which is created
    """

    def __init__(self, testing):
        """Initialises object's attributes.

        Parameters:
            testing (Boolean) States whether a test is being mocked."""

        error_log = ErrorLogger()
        using_raspberry_pi = True

        try:
            # Attempting to acces the GPIO Pins Module
            if testing == True:
                # Makes system use keys as this is how the BDD tests test system
                print("TESTING SO NOT USING KEYS")
                raise ModuleNotFoundError

            # Imports modules needed for hardware
            import RPi.GPIO as GPIO
            from src.interaction.character import BrailleCharacter

        except ModuleNotFoundError as e:
            # If the system is unable to import the module it will revert to using the SDFJKL keys
            print("KEYBOARD MODE ACTIVATED")
            print(e)
            from src.interaction.keyboard_interface import check_keys
            using_raspberry_pi = False
            error_log.log_error(e)
            key_presses = {
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

        # Sets objects attributes
        self.pygame = pygame
        self.error_log = error_log
        self.show_gui = show_gui
        if show_gui:
            self.graphical_user_interface = graphical_user_interface
            self.graphical_user_interface.show_welcome_screen()

        self.speech = speech
        self.braille_alphabet = braille_alphabet

        self.using_raspberry_pi = using_raspberry_pi
        if using_raspberry_pi:
            self.current_char = current_char
        else:
            self.key_presses = key_presses
            self.check_keys = check_keys

        

    def mute(self):
        self.speech.set_mute()
