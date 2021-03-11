# Essential Imports
import time
from time import sleep
from src.braille.alphabet import Alphabet


class Lesson():

    a_to_z_converstions = Alphabet()

    activity_map = {
        1: "000000",
        2: "100000",
        3: "001000",
        4: "000010",
        5: "010000",
        6: "000100",
        7: "000001",
        8: a_to_z_converstions.translate_alphabet_to_braille("b"),
        9: a_to_z_converstions.translate_alphabet_to_braille("c"),
        10: a_to_z_converstions.translate_alphabet_to_braille("d"),
        11: a_to_z_converstions.translate_alphabet_to_braille("e"),
        12: a_to_z_converstions.translate_alphabet_to_braille("f"),
        13: a_to_z_converstions.translate_alphabet_to_braille("g"),
        14: a_to_z_converstions.translate_alphabet_to_braille("h"),
        15: a_to_z_converstions.translate_alphabet_to_braille("i"),
        16: a_to_z_converstions.translate_alphabet_to_braille("j"),
    }

    def start_activity(self, activity_id):

        fetched_assertion = self.activity_map[activity_id]
        translated_dothash = self.a_to_z_converstions.translate_braille_to_alphabet(
            fetched_assertion)

        print("-"*60)
        print("STARTING ACTIVITY {} -> Letter {} -> Match the dot hash of {}.".format(
            activity_id, translated_dothash, fetched_assertion))
        print("-"*60)

        self.assert_answer(fetched_assertion, translated_dothash)

    def simulate_events(self):

        if self.test_content != None:

            all_simulations = set(self.test_content)
            simulations_executed = set(self.simulations_executed)
            simulations_to_go = sorted(list(all_simulations - simulations_executed))

            if len(simulations_to_go) > 0:


                print(self.time_since_start)
                print(simulations_to_go)
                print("ALL GOOD?")
                next_event = simulations_to_go[0]
                print("EXECUTING: {}".format(next_event))

                if next_event < self.time_since_start:

                    self.simulations_executed.append(next_event)

                    keys_to_press = self.test_content[next_event]

                    for key in keys_to_press:
                        new_event = self.pygame.event.Event(
                            self.pygame.KEYDOWN, unicode=key, key=ord(key))
                        print('Adding event:', new_event)
                        self.pygame.event.post(new_event)
                
            else:
                print("ALL SIMULATIONS COMPLETE")

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
                self.time_since_start = time_since_start

                self.simulate_events()

                text_to_say, expired_events = self.check_timings(
                    expired_events, time_since_start)

                if isinstance(text_to_say, int):

                    self.start_activity(text_to_say)

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

    def __init__(self, interaction_object, content, test_content):

        self.test_content = test_content

        self.time_since_start = 0

        self.timeline = content

        self.ordered_timings = list(self.timeline.keys()).sort()

        self.simulations_executed = []

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

    def assert_answer(self, asserted_answer, fetched_letter):
        current_dots_hash = "INIT"
        letter_to_learn = fetched_letter + "?"

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
                        current_dots_hash, letter_to_learn)

        # speech.say("Awesome. it looks like you are ready to begin")

        self.graphical_user_interface.draw_dot_hash(
            asserted_answer, letter_to_learn)
