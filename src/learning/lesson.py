# Essential Imports
import time
from src.braille.alphabet import Alphabet
from src.learning.learning_tool import LearningTool


class Lesson(LearningTool):
    """ 
    This class is used to start a lesson on specified learning content.

    Extended description of function. 

    Attributes:: 
        interaction_object  (Interaction): The interaction object which tells the system how the user will interact.
        content             (dict): This varibale dictates a timeline of content for the lesson
        test_content        (dict): This parameter dictates whether simulated events will be executed
        max_timeout         (int): This is the maximum amount of seconds before the lesson is terminated
        activity_map        (dict): maps different integers to different activities
        a_to_z_converstions (Alphabet) Alphabet object which can be used to convert letters to braille codes
    """

    activity_map = {
        1: "_",
        2: "Dot 1",
        3: "Dot 2",
        4: "Dot 3",
        5: "Dot 4",
        6: "Dot 5",
        7: "Dot 6",
        8: "b",
        9: "c",
        10: "d",
        11: "e",
        12: "f",
        13: "g",
        14: "h",
        15: "i",
        16: "j",
        17: "k",
        18: "l",
        19: "m",
        20: "n",
        21: "o",
        22: "p",
        23: "q",
        24: "r",
        25: "s",
        26: "t",
        27: "u",
        28: "v",
        29: "x",
        30: "y",
        31: "z",
        32: "w",
        33: "a",
    }

    def __init__(self, interaction_object, content, simulations=None, time_until_hint=20, max_timeout=None):
        """The constructor for the Lesson class.

        Parameters: 
            interaction_object  (Interaction):  The interaction object which tells the system how the user will interact.
            content             (dict):         This varibale dictates a timeline of content for the lesson
            test_content        (dict):         This parameter dictates whether simulated events will be executed
            max_timeout         (int):          This is the maximum amount of seconds before the lesson is terminated"""

        super(Lesson, self).__init__(
            interaction_object=interaction_object,
            time_until_hint=time_until_hint,
            simulations=simulations)

        # Testing variables
        self.max_timeout = max_timeout

        # Lesson varibales
        self.time_since_start = 0
        self.timeline = content
        self.ordered_timings = list(self.timeline.keys()).sort()

        self.play()

    def play(self):
        """Starts the lesson's loop."""

        self.previous_time = time.time()
        self.start_time = time.time()

        # Forever loop which will ONLY exit if the program is ended
        expired_events = []

        # if the lesson is still live then this loop will continue
        self.lesson_live = True
        while self.lesson_live:
            # Check if enough time has passed to update GUI
            now = time.time()
            difference = float(now-self.previous_time)

            # Checks timelines every 0.5 seconds
            if difference > 0.1:
                self.previous_time = now
                time_since_start = float(now - self.start_time)
                self.time_since_start = time_since_start
                self.simulate_events()
                text_to_say, expired_events = self.check_timings(
                    expired_events, time_since_start)

                if isinstance(text_to_say, int):
                    self.start_activity(text_to_say)

                else:
                    self.say_text_event(text_to_say)

                self.check_if_lesson_over(expired_events)

    def start_activity(self, activity_id):
        """This method starts the next activity. i.e. enter the dots for letter A.

        Parameters:
            activity_id (int) the unique identifier to fetch an activity from activity_map."""

        fetched_letter = self.activity_map[activity_id]
        fetched_dothash = self.a_to_z_converstions.translate_char_to_braille(
            fetched_letter)

        print("-"*60)
        print("STARTING ACTIVITY {} -> Letter {} -> Match the dot hash of {}.".format(
            activity_id, fetched_letter, fetched_dothash))
        print("-"*60)

        self.assert_answer(fetched_dothash, fetched_letter)

    def check_if_lesson_over(self, expired_events):
        """Checks if there are any remaining events.

        Parameters: 
            expired_events (list) : list of all expired events."""

        if len(expired_events) == len(list(self.timeline.keys())):
            print("Lesson over...")
            self.lesson_live = False

    def say_text_event(self, text_to_say):
        """Makes the system speak out an event and subtracts time taken to speak the string."""
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

    def check_timings(self, events_executed, time_elapsed):
        """check_timings checks to see what events in the timeline have executed and what need to be executed.

        Parameters:
            events_executed (list)  A list of all the identifiers from the lesson content which have executed.
            time_elapsed    (float) The amount of seconds elapsed since the start of the lesson."""

        timeline_keys = set(self.timeline.keys())
        events_to_go = list(timeline_keys - set(events_executed))

        if len(events_to_go) > 0:
            sorted_events = sorted((events_to_go))
            first_event = sorted_events[0]

            if time_elapsed > first_event:
                new_expired_events = events_executed
                new_expired_events.append(first_event)

                return self.timeline[first_event], new_expired_events

            else:
                return "", events_executed

        else:
            return "", events_executed

    def assert_answer(self, asserted_answer, fetched_letter):
        """This method checks if the user has completed the activity.

        Parameters:
            asserted_answer (String) the braille code for the correct answer.
            fetched_letter  (String) the letter for the braille code."""

        self.activity_start_time = time.time()
        current_dots_hash = "INIT"
        letter_to_learn = fetched_letter + "?"

        while current_dots_hash != asserted_answer:
            now = time.time()
            difference = float(now-self.previous_time)

            if difference > 0.1:
                # print(current_dots_hash)
                now = time.time()
                self.previous_time = now
                self.time_since_start_of_activity = float(
                    now-self.activity_start_time)

                if self.time_since_start_of_activity > self.time_until_hint:
                    self.speech.play_sound("incorrect")
                    self.reveal_answer(asserted_answer, fetched_letter)
                    now = time.time()
                    self.activity_start_time = now

                if self.using_raspberry_pi:
                    # Get dot hash from pins
                    current_dots_hash = (
                        self.current_char.get_current_dots_hash())
                else:
                    # Get dot hash from keyboard
                    current_dots_hash = self.check_keys(
                        self.pygame, self.key_presses)

                if self.show_gui:
                    self.graphical_user_interface.draw_dot_hash(
                        current_dots_hash, letter_to_learn)

                if self.max_timeout != None and (now - self.start_time) > self.max_timeout:
                    self.test_failed = True
                    current_dots_hash = asserted_answer

        self.graphical_user_interface.draw_dot_hash(
            asserted_answer, letter_to_learn)

        self.speech.play_sound("correct")
