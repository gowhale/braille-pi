import random
import time
from src.braille.alphabet import Alphabet
from src.results_logging.results_logger import ResultsLogger


class Quiz():
    """ 
    This class is used to start a qiuz on specified quiz content.

    Extended description of function. 

    Attributes:: 
        interaction_object  (Interaction): The interaction object which tells the system how the user will interact.
        content             (dict): This varibale dictates a timeline of content for the quiz
        simulations         (dict): This parameter dictates whether simulated events will be executed
        time_until_hint     (int): This is the amount of seconds before a hint on a character is given
        a_to_z_converstions (Alphabet) Alphabet object which can be used to convert letters to braille codes
        no_incorrect_answers(Integer) Count for amount of incorrect chars
        no_correct_answers  (Integer) Count for amount of correct answers
        correct_characters  (List) List of characaters answered correctly
        incorrect_characters  (List) List of characaters answered incorrectly
        test_failed         (Boolean) Check used by automated tests to ensure BDD tests have passed
    """

    a_to_z_converstions = Alphabet()
    no_incorrect_answers = 0
    no_correct_answers = 0
    incorrect_characters = []
    correct_characters = []
    test_failed = False
    results_logger = ResultsLogger()
    encouraging_phrases = ["So close",
                           "Unlucky you are getting there",
                           "Better luck next time",
                           "Almost",
                           "Let us try again",
                           "I am afraid thats not quite right"]

    def __init__(self, interaction_object, content, time_until_hint, simulations):
        """The constructor for the Quiz class.

        Parameters: 
            interaction_object (Interaction):  The interaction object which tells the system how the user will interact.
            content            (dict):         This varibale dictates a timeline of content for the quiz
            simulations        (dict):         This parameter dictates whether simulated events will be executed
            time_until_hint    (int):          The amount of seconds until a hint is given"""

        # Initialisation of quiz varibales
        self.simulations_to_go = simulations
        self.simulations_executed = []
        self.quiz_start_time = time.time()
        self.quiz_characters = content
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

    def start_quiz(self):
        """Starts the quiz."""

        self.previous_time = time.time()
        possible_characters = self.quiz_characters
        len_of_quiz_characters = len(possible_characters)

        if len_of_quiz_characters > 0:
            quiz_chars = self.quiz_characters

            for question in quiz_chars:
                wanted_dot_hash = self.a_to_z_converstions.translate_alphabet_to_braille(
                    question)
                print("Character to be quizzed is {} the dothash is {}".format(
                    question, wanted_dot_hash))
                self.assert_answer(wanted_dot_hash, question)

        else:
            self.error_log.log_error("NOT ENOUGH CHARS")

        self.speech.say("Awesome you scored {} out of {}. Keep it up.".format(
            self.no_correct_answers, len(self.quiz_characters)))

        self.log_results()

    def assert_answer(self, asserted_answer, fetched_letter):
        """This method checks if the user has completed the activity.

        Parameters:
            asserted_answer (String) the braille code for the correct answer.
            fetched_letter  (String) the letter for the braille code."""

        self.speech.say(
            "Enter the combination for {}".format(fetched_letter))

        self.start_time = time.time()
        current_dots_hash = "INIT"
        letter_to_learn = fetched_letter + "?"

        while current_dots_hash != asserted_answer:
            now = time.time()
            difference = float(now-self.previous_time)

            if difference > 0.1:
                now = time.time()
                self.previous_time = now
                self.time_since_start = float(now-self.start_time)
                self.simulate_events()

                if self.time_since_start > self.time_until_hint:
                    self.speech.play_sound("incorrect")
                    self.reveal_answer(asserted_answer, fetched_letter)
                    now = time.time()
                    self.start_time = now

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

        self.graphical_user_interface.draw_dot_hash(
            asserted_answer, letter_to_learn)

        self.speech.play_sound("correct")

        self.speech.say(
            "Congratulations that is the correct answer for {}".format(fetched_letter))

        if fetched_letter not in self.incorrect_characters:
            self.correct_characters.append(fetched_letter)
            self.no_correct_answers += 1

    def reveal_answer(self, answer, letter):
        """Speaks out the required dothash in a user friendly way."""

        reveal_start_time = time.time()
        dots_to_say = []

        encouragement_string = random.choice(self.encouraging_phrases)

        self.speech.say(encouragement_string)

        if letter in self.braille_alphabet.custom_hints.keys():
            self.speech.say(self.braille_alphabet.custom_hints[letter])
        else:

            self.speech.say(
                "{} goes by the following dot combination".format(letter))

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
        self.start_time = self.start_time - reveal_duration

        if letter not in self.incorrect_characters:
            self.incorrect_characters.append(letter)
            self.no_incorrect_answers += 1

    def simulate_events(self):
        """simulate_events simulates remaining expected actions."""

        if self.simulations_to_go != None:
            all_simulations = set(self.simulations_to_go)
            simulations_executed = set(self.simulations_executed)
            simulations_to_go = sorted(
                list(all_simulations - simulations_executed))

            if len(simulations_to_go) > 0:
                now = time.time()
                timeline_duration = now - self.quiz_start_time
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
