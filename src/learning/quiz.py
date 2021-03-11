import random
import time
from src.braille.alphabet import Alphabet


class Quiz():

    a_to_z_converstions = Alphabet()
    # time_until_hint = 30
    no_incorrect_answers = 0
    no_correct_answers = 0
    incorrect_characters = []
    correct_characters = []
    test_failed = False

    def __init__(self, interaction_object, content, time_until_hint, simulations):

        self.simulations_to_go = simulations

        self.quiz_start_time = time.time()

        self.simulations_executed = []

        self.quiz_characters = content
        self.time_until_hint = time_until_hint

        self.speech = interaction_object.speech
        self.using_raspberry_pi = interaction_object.using_raspberry_pi
        self.braille_alphabet = interaction_object.braille_alphabet
        self.pygame = interaction_object.pygame
        self.error_log = interaction_object.error_log

        if not interaction_object.using_raspberry_pi:
            self.current_char = ""
            self.check_keys = interaction_object.check_keys
            self.dot_has_test = interaction_object.dot_has_test
        else:
            self.current_char = interaction_object.current_char

        self.show_gui = interaction_object.show_gui
        if interaction_object.show_gui:
            self.graphical_user_interface = interaction_object.graphical_user_interface

        print("Quizzing the user on the following: {}".format(content))

        # self.start_quiz(5)

    def start_quiz(self, n_of_characters_to_test):
        print(n_of_characters_to_test)

        self.previous_time = time.time()

        possible_characters = self.quiz_characters

        len_of_quiz_characters = len(possible_characters)

        if len_of_quiz_characters < n_of_characters_to_test:

            n_of_characters_to_test = len_of_quiz_characters

        if n_of_characters_to_test > 0:

            # for _ in range(10):

            # quiz_chars = random.sample(
            #     possible_characters, n_of_characters_to_test)
            quiz_chars = self.quiz_characters

            print(quiz_chars)

            for question in quiz_chars:
                print(question)
                wanted_dot_hash = self.a_to_z_converstions.translate_alphabet_to_braille(
                    question)
                print("Character to be quizzed is {} the dothash is {}".format(
                    question, wanted_dot_hash))
                self.assert_answer(wanted_dot_hash, question)

        else:

            self.error_log.log_error("NOT ENOUGH CHARS")

        self.speech.say("Awesome you scored {} out of {}. Keep it up.".format(
            self.no_correct_answers, len(self.quiz_characters)))

        print(self.no_correct_answers)
        print(self.no_incorrect_answers)
        print("CORRECT answers: {}".format(self.correct_characters))
        print("WRONG answers: {}".format(self.incorrect_characters))

    def assert_answer(self, asserted_answer, fetched_letter):

        self.speech.say(
            "Enter the combination for the character {}".format(fetched_letter))

        self.start_time = time.time()

        current_dots_hash = "INIT"
        letter_to_learn = fetched_letter + "?"

        while current_dots_hash != asserted_answer:
            now = time.time()
            difference = float(now-self.previous_time)

            if difference > 0.5:
                now = time.time()
                self.previous_time = now

                self.time_since_start = float(now-self.start_time)
                self.simulate_events()
                # print("TIME SINCE START {}".format(time_since_start))
                if self.time_since_start > self.time_until_hint:

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
                        self.pygame, self.dot_has_test)

                if self.show_gui:
                    self.graphical_user_interface.draw_dot_hash(
                        current_dots_hash, letter_to_learn)
        # self.no_correct_answers += 1

        # speech.say("Awesome. it looks like you are ready to begin")

        self.graphical_user_interface.draw_dot_hash(
            asserted_answer, letter_to_learn)

        self.speech.say(
            "Congratulations that is the correct answer for letter {}".format(fetched_letter))

        if fetched_letter not in self.incorrect_characters:
            self.correct_characters.append(fetched_letter)
            self.no_correct_answers += 1

    def reveal_answer(self, answer, letter):

        reveal_start_time = time.time()

        self.speech.say("You were so close.")

        self.speech.say(
            "The letter {} goes by the following dot combination".format(letter))

        dots_to_say = []

        remap_hash = {
            1: 1,
            2: 4,
            3: 2,
            4: 5,
            5: 3,
            6: 6,
        }

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
            else:
                print("ALL SIMULATIONS COMPLETE")
