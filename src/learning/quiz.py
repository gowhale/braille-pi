import random
from src.learning.learning_tool import LearningTool
import time
from src.braille.alphabet import Alphabet
from src.results_logging.results_logger import ResultsLogger


class Quiz(LearningTool):
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

    no_incorrect_answers = 0
    no_correct_answers = 0
    incorrect_characters = []
    correct_characters = []
    results_logger = ResultsLogger()

    def __init__(self, interaction_object, content, time_until_hint, simulations):
        """The constructor for the Quiz class.

        Parameters: 
            interaction_object (Interaction):  The interaction object which tells the system how the user will interact.
            content            (dict):         This varibale dictates a timeline of content for the quiz
            simulations        (dict):         This parameter dictates whether simulated events will be executed
            time_until_hint    (int):          The amount of seconds until a hint is given"""

        super(Quiz, self).__init__(
            interaction_object, time_until_hint)

        # Initialisation of quiz varibales
        self.simulations_to_go = simulations
        self.quiz_start_time = time.time()
        self.quiz_characters = content

    def start_quiz(self):
        """Starts the quiz."""

        self.previous_time = time.time()
        possible_characters = self.quiz_characters
        len_of_quiz_characters = len(possible_characters)

        if len_of_quiz_characters > 0:
            quiz_chars = self.quiz_characters

            for question in quiz_chars:
                wanted_dot_hash = self.a_to_z_converstions.translate_char_to_braille(
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

        self.activity_start_time = time.time()
        current_dots_hash = "INIT"
        letter_to_learn = fetched_letter + "?"

        while current_dots_hash != asserted_answer:
            now = time.time()
            difference = float(now-self.previous_time)

            if difference > 0.1:
                now = time.time()
                self.previous_time = now
                self.time_since_start = float(now-self.activity_start_time)
                self.simulate_events()

                if self.time_since_start > self.time_until_hint:
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

        super(Quiz, self).reveal_answer(answer, letter)

        if letter not in self.incorrect_characters:
            self.incorrect_characters.append(letter)
            self.no_incorrect_answers += 1

    def log_results(self):
        print("CORRECT answers: {}".format(self.correct_characters))
        print("WRONG answers: {}".format(self.incorrect_characters))
        self.results_logger.log_results(
            correct_answers=self.correct_characters, wrong_answers=self.incorrect_characters)
