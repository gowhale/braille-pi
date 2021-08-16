import time
import random
from src.results_logging.results_logger import ResultsLogger


class LearningTool():
    """ 
    This class contains common code used by both Quiz and Lesson Classes.
    """

    encouraging_phrases = ["So close",
                           "Unlucky you are getting there",
                           "Better luck next time",
                           "Almost",
                           "Let us try again",
                           "I am afraid thats not quite right"]


    no_incorrect_answers = 0
    no_correct_answers = 0
    incorrect_characters = []
    correct_characters = []
    results_logger = ResultsLogger()

    def __init__(self, interaction_object, time_until_hint, simulations):
        """Initialised essential things need for both a lesson or quiz"""

        self.time_until_hint = time_until_hint

        # Initialisation of interaction elementes
        self.speech = interaction_object.speech
        self.using_raspberry_pi = interaction_object.using_raspberry_pi
        self.braille_alphabet = interaction_object.braille_alphabet
        self.pygame = interaction_object.pygame
        self.error_log = interaction_object.error_log
        if not interaction_object.using_raspberry_pi:
            self.current_char = ""
            self.check_keys = interaction_object.check_keys
            self.key_presses = interaction_object.key_presses
        else:
            self.current_char = interaction_object.current_char
        self.show_gui = interaction_object.show_gui
        if interaction_object.show_gui:
            self.graphical_user_interface = interaction_object.graphical_user_interface
        self.a_to_z_converstions = interaction_object.braille_alphabet

        # Test varibales
        self.test_failed = False
        self.simulations_executed = []
        self.simulations_to_go = simulations

        self.tool_start_time = time.time()

    def reveal_answer(self, answer, letter):
        """Speaks out the required dothash in a user friendly way."""

        reveal_start_time = time.time()
        dots_to_say = []

        encouragement_string = random.choice(self.encouraging_phrases)

        self.speech.say(encouragement_string)

        if letter in self.braille_alphabet.custom_hints.keys():
            self.speech.say(self.braille_alphabet.custom_hints[letter])
        else:

            self.speech.say("{}".format(letter))
            self.speech.say("goes by the following dot combination")

            remap_hash = {
                1: 1,
                2: 4,
                3: 2,
                4: 5,
                5: 3,
                6: 6,
            }

            # Iterates throught dothas and converts to dothash i.e. 100000 -> Dot 1
            for index, dot in enumerate(answer, start=1):
                if dot == "1":
                    dots_to_say.append(remap_hash[index])

            dots_to_say = sorted(dots_to_say)

            if len(dots_to_say) == 1:
                self.speech.say("Dot {}".format(dots_to_say[0]))

            elif len(dots_to_say) > 1:
                for dot in dots_to_say[:-1]:
                    self.speech.say("Dot {}".format(dot))
                self.speech.say("and Dot {}".format(dots_to_say[-1]))

        reveal_duration = float(time.time() - reveal_start_time)
        self.activity_start_time = self.activity_start_time - reveal_duration

    def simulate_events(self):
        """simulate_events simulates remaining expected actions."""
        if self.simulations_to_go != None:

            all_simulations = set(self.simulations_to_go)
            simulations_executed = set(self.simulations_executed)
            simulations_to_go = sorted(
                list(all_simulations - simulations_executed))

            if len(simulations_to_go) > 0:
                next_event = simulations_to_go[0]
                now = time.time()
                timeline_duration = now - self.tool_start_time
                next_event = simulations_to_go[0]

                if next_event < timeline_duration:
                    self.simulations_executed.append(next_event)
                    keys_to_press = self.simulations_to_go[next_event]

                    for key in keys_to_press:
                        new_event = self.pygame.event.Event(
                            self.pygame.KEYDOWN, unicode=key, key=ord(key))
                        print('Adding event:', new_event)
                        self.pygame.event.post(new_event)

    def log_results(self):
        print("CORRECT answers: {}".format(self.correct_characters))
        print("WRONG answers: {}".format(self.incorrect_characters))
        self.results_logger.log_results(
            correct_answers=self.correct_characters, wrong_answers=self.incorrect_characters)
