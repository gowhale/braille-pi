from src.learning.learning_tool import LearningTool
import time


class SpellingGame(LearningTool):
    """This class provides objects acting as fun spelling games"""


    def __init__(self, interaction_object, spelling_word, time_until_hint=20, simulations=None, max_timeout=None):
        super().__init__(interaction_object, time_until_hint, simulations)

        self.no_incorrect_answers = 0
        self.no_correct_answers = 0
        self.incorrect_characters = []
        self.correct_characters = []
        self.spelling_word = spelling_word
        self.max_timeout = max_timeout


    def play(self):

        self.speech.say("In this round we will spell out {}".format(self.spelling_word))
        # self.speech.say("I will take you through the letters one by one")
        # self.speech.say("If you cannot remember how the dot combination goes I will give you a hint")

        self.speech.say(
            "hints will be given after {} seconds".format(self.time_until_hint))

        for letter in self.spelling_word:
            lowercase_letter = letter.lower()
            self.speech.say(
                "Enter the combination for {}".format(lowercase_letter))
            fetched_dothash_combination = self.braille_alphabet.translate_alphabet_to_braille(
                lowercase_letter)
            self.assert_answer(fetched_dothash_combination, lowercase_letter)

        self.log_results()

        self.speech.say("Awesome you scored {} out of {}. Keep it up.".format(
            self.no_correct_answers, len(self.spelling_word)))

        self.no_incorrect_answers = 0
        self.no_correct_answers = 0
        self.incorrect_characters = []
        self.correct_characters = []

    def assert_answer(self, asserted_answer, fetched_letter):
        """This method checks if the user has completed the activity.

        Parameters:
            asserted_answer (String) the braille code for the correct answer.
            fetched_letter  (String) the letter for the braille code."""

        self.previous_time = time.time()

        self.activity_start_time = time.time()
        current_dots_hash = "INIT"
        letter_to_learn = fetched_letter + "?"

        while current_dots_hash != asserted_answer:
            now = time.time()
            difference = float(now-self.previous_time)
            self.simulate_events()
            if difference > 0.1:
                now = time.time()
                self.previous_time = now
                self.time_since_start = float(now-self.activity_start_time)
                

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

                if self.max_timeout != None and (now - self.tool_start_time) > self.max_timeout:
                    self.test_failed = True
                    current_dots_hash = asserted_answer

        self.graphical_user_interface.draw_dot_hash(
            asserted_answer, letter_to_learn)

        self.speech.play_sound("correct")
        print(self.test_failed)

        # self.speech.say(
        #     "Congratulations that is the correct answer for {}".format(fetched_letter))

        if fetched_letter not in self.incorrect_characters:
            self.correct_characters.append(fetched_letter)
            self.no_correct_answers += 1

    def reveal_answer(self, answer, letter):
        """Speaks out the required dothash in a user friendly way."""

        super(SpellingGame, self).reveal_answer(answer, letter)

        if letter not in self.incorrect_characters:
            self.incorrect_characters.append(letter)
            self.no_incorrect_answers += 1
