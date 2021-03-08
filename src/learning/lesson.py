# Essential Imports
import time
from time import sleep
from src.braille.alphabet import Alphabet


class Lesson():

    a_to_z_converstions = Alphabet()

    def play(self):
        previous_time = time.time()

        self.previous_time = previous_time

        self.start_time = time.time()

        # Forever loop which will ONLY exit if the program is ended
        expired_events = []

        # if the lesson is still live then this loop will continue
        self.lesson_live = True
        while self.lesson_live:
            # Check if enough time has passed to update GUI
            now = time.time()
            difference = float(now-previous_time)

            # Checks timelines every 0.5 seconds
            if difference > 0.5:
                # speech.say(current_dots_hash)
                previous_time = now

                time_since_start = float(now - self.start_time)
                # print(difference, time_since_start)

                text_to_say, expired_events = self.check_timings(
                    expired_events, time_since_start)

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

                elif text_to_say == 8:

                    print("ACTIVITY 8 -> Representing the letter B.")

                    letter_b_braille_code = self.get_expected_braille_code("b")
                    self.assert_answer(letter_b_braille_code)

                elif text_to_say == 9:

                    print("ACTIVITY 9 -> Representing the letter C.")

                    letter_c_braille_code = self.get_expected_braille_code("c")
                    self.assert_answer(letter_c_braille_code)

                else:

                    self.say_text_event(text_to_say)

                self.check_if_lesson_over(expired_events)

    def check_if_lesson_over(self, expired_events):
        if len(expired_events) == len(list(self.timeline.keys())):
            print("Lesson over...")
            self.lesson_live = False

    def get_expected_braille_code(self, letter):
        return self.a_to_z_converstions.translate_alphabet_to_braille(letter)

    def say_text_event(self, text_to_say):
        if text_to_say != "":
            # Currently the timings don't include time it takes to say thigns
            # This is useful as different computers will speak at different times
            start_pause_timer = time.time()
            self.speech.say(text_to_say)
            end_pause_timer = time.time()
            elapsed_speech_time = end_pause_timer - start_pause_timer
            print("It took {} seconds to say that.".format(
                elapsed_speech_time))
            self.start_time += elapsed_speech_time

    def __init__(self, interaction_object, content):

        self.timeline = content

        self.ordered_timings = list(self.timeline.keys()).sort()

        self.speech = interaction_object.speech
        self.using_raspberry_pi = interaction_object.using_raspberry_pi
        self.braille_alphabet = interaction_object.braille_alphabet
        self.pygame = interaction_object.pygame

        if not interaction_object.using_raspberry_pi:
            self.current_char = ""
            self.check_keys = interaction_object.check_keys
            self.dot_has_test = interaction_object.dot_has_test
        else:
            self.current_char = interaction_object.current_char

        self.show_gui = interaction_object.show_gui
        if interaction_object.show_gui:
            self.graphical_user_interface = interaction_object.graphical_user_interface

        self.play()

    # The following function checks to see what events in the timeline have executed and what need to be executed

    def check_timings(self, events_executed, time_elapsed):
        timeline_keys = set(self.timeline.keys())
        events_to_go = list(timeline_keys - set(events_executed))

        if len(events_to_go) > 0:

            sorted_events = sorted((events_to_go))
            # print(sorted_events, time_elapsed)

            first_event = sorted_events[0]

            if time_elapsed > first_event:
                # print("{} is executing...".format(first_event))

                new_expired_events = events_executed
                new_expired_events.append(first_event)

                return self.timeline[first_event], new_expired_events

            else:

                return "", events_executed

        else:
            return "", events_executed

    def assert_answer(self, asserted_answer):
        current_dots_hash = "INIT"

        while current_dots_hash != asserted_answer:
            now = time.time()
            difference = float(now-self.previous_time)

            if difference > 0.5:
                now = time.time()
                self.previous_time = now

                if self.using_raspberry_pi:
                    # Get dot hash from pins
                    current_dots_hash = (
                        self.current_char.get_current_dots_hash())
                else:
                    # Get dot hash from keyboard
                    current_dots_hash = self.check_keys(
                        self.pygame, self.dot_has_test)

                if self.show_gui:
                    self.graphical_user_interface.draw_dot_hash(
                        current_dots_hash, "")

        # speech.say("Awesome. it looks like you are ready to begin")

        self.graphical_user_interface.draw_dot_hash(
            current_dots_hash, "")
