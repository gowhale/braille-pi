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

    timeline = {
        1: "Welcome to your first Braille lesson!",
        2: "Braille changes lives. It gives thousands of people independence, learning, literacy, and the enjoyment of reading. Braille opens doors, and gives hope and inspiration.",
        3: "Braille is made up of 6 dots. Two Columns by Three rows",
        4: "Feel the Braille-Pi to get familiar with how you can interact with the system.",
        5: "You can press down on the six dots, they will lock in place.",
        6: "To get you familiar with the six dots we will go through a tutorial where we will press them one by one.",
        7: "Firstly, make sure all the dots have been pushed down. This is known as an empty cell.",
        8: 1,
        9: "Awesome. it looks like you are ready to begin",
        10: "The top left dot is known as dot 1. Please raise this dot now so that it is the only dot which is high.",
        11: 2,
        12: "Fantastic. This is dot 1.",
        13: "Now as we did previously make sure all the dots are pressed down. An empty cell.",
        14: 1,
        15: "Great. The next dot is dot 2. Dot 2 is located on the left column, second row down.",
        16: 3,
        17: "Well done, this is dot 2.",
        18: "Now as we did previously make sure all the dots are pressed down. An empty cell.",
        19: 1,
        20: "Great. The next dot is dot 3. Dot 3 is located at the bottum left of the cell.",
        21: 4,
        22: "Now as we did previously make sure all the dots are pressed down. An empty cell.",
        23: 1,
        24: "Great. The next dot is dot 4. Dot 4 is located at the top right of the cell.",
        25: 5,
        26: "Good work. Now as we did previously make sure all the dots are pressed down. An empty cell.",
        27: 1,
        28: "Great. The next dot is dot 5. Dot 5 is located on the right column, second row down.",
        29: 6,
        30: "Well done that was dot 5. Now as we did previously make sure all the dots are pressed down. An empty cell.",
        31: 1,
        32: "Well done thats the one. Last but not least is is dot 6. Dot 6 is located at the bottum right of the cell.",
        33: 7,
        34: "YOU DID IT. Your first braille lesson. Congratulations.",


    }

    ordered_timings = list(timeline.keys()).sort()

    def assert_answer(self, asserted_answer):
        current_dots_hash = "INIT"

        while current_dots_hash != asserted_answer:
            now = time.time()
            difference = float(now-self.previous_time)

            if difference > 0.5:
                now = time.time()
                difference = float(now-self.previous_time)
                self.previous_time = now

                if self.using_raspberry_pi:
                    # Get dot hash from pins
                    current_dots_hash = (
                        self.current_char.get_current_dots_hash())
                else:
                    # Get dot hash from keyboard
                    current_dots_hash = self.check_keys(
                        pygame, self.dot_has_test)
                braille_translation = self.braille_alphabet.translate_braille_to_alphabet(
                    current_dots_hash)
                previous_time = now
                if self.show_gui:
                    self.graphical_user_interface.draw_dot_hash(
                        current_dots_hash, "")

        # speech.say("Awesome. it looks like you are ready to begin")

        self.graphical_user_interface.draw_dot_hash(
            current_dots_hash, "")

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
        # speech.say("Welcome to your first Braille lesson!")
        # speech.say("Braille changes lives. It gives thousands of people independence, learning, literacy, and the enjoyment of reading. Braille opens doors, and gives hope and inspiration.")
        # speech.say("""Popular games (such as Bingo and Uno) are available in braille and others can be adapted by the addition of braille labels, enabling a blind or partially sighted individual to join in with family or friends in a wide range of leisure pursuits.""")
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
        start_time = time.time()

        # Forever loop which will ONLY exit if the program is ended
        expired_events = []

        # if the lesson is still live then this loop will continue
        lesson_live = True
        while lesson_live:
            # Check if enough time has passed to update GUI
            now = time.time()
            difference = float(now-previous_time)

            # Checks timelines every 0.5 seconds
            if difference > 0.5:
                print(difference)
                # speech.say(current_dots_hash)
                previous_time = now

                time_since_start = float(now - start_time)
                print(difference, time_since_start)

                text_to_say, expired_events = self.check_timings(
                    expired_events, time_since_start)

                self.previous_time = previous_time
                self.using_raspberry_pi = using_raspberry_pi
                self.current_char = ""
                self.check_keys = check_keys
                self.dot_has_test = dot_has_test
                self.braille_alphabet = braille_alphabet
                self.show_gui = show_gui
                self.graphical_user_interface = graphical_user_interface

                if text_to_say == 1:

                    print("ACTIVITY 1 -> Empty Cell activity")

                    self.assert_answer("000000")

                elif text_to_say == 2:

                    print("ACTIVITY 2 -> Dot 1 activity")

                    self.assert_answer("100000")

                elif text_to_say == 3:

                    print("ACTIVITY 3 -> Dot 2 activity")

                    self.assert_answer("001000")

                elif text_to_say == 4:

                    print("ACTIVITY 4 -> Dot 3 activity")

                    self.assert_answer("000010")

                elif text_to_say == 5:

                    print("ACTIVITY 5 -> Dot 4 activity")

                    self.assert_answer("010000")

                elif text_to_say == 6:

                    print("ACTIVITY 6 -> Dot 5 activity")

                    self.assert_answer("000100")

                elif text_to_say == 7:

                    print("ACTIVITY 7 -> Dot 6 activity")

                    self.assert_answer("000001")

                else:

                    if text_to_say != "":
                        # Currently the timings don't include time it takes to say thigns
                        # This is useful as different computers will speak at different times
                        start_pause_timer = time.time()
                        speech.say(text_to_say)
                        end_pause_timer = time.time()
                        elapsed_speech_time = end_pause_timer - start_pause_timer
                        print("It took this long to say that: {}".format(
                            elapsed_speech_time))
                        start_time += elapsed_speech_time

                    if len(expired_events) == len(list(self.timeline.keys())):
                        print("Lesson over...")
                        lesson_live = False

    def play(self):
        print("Let's begin...")

    # The following function checks to see what events in the timeline have executed and what need to be executed
    def check_timings(self, events_executed, time_elapsed):
        timeline_keys = set(self.timeline.keys())
        events_to_go = list(timeline_keys - set(events_executed))

        if len(events_to_go) > 0:

            sorted_events = sorted((events_to_go))
            print(sorted_events, time_elapsed)

            first_event = sorted_events[0]

            if time_elapsed > first_event:
                print("{} is executing...".format(first_event))

                new_expired_events = events_executed
                new_expired_events.append(first_event)

                return self.timeline[first_event], new_expired_events

            else:

                return "", events_executed

        else:
            return "", events_executed
