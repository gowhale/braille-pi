# Additional modules
import random
from time import time

# Functional Imports
from src.learning.translator import Translator
from src.learning.lesson import Lesson
from src.learning.quiz import Quiz
from src.learning.spelling_game import SpellingGame
from src.learning.content_selection import ContentSelection
from src.interaction.interaction_module import Interaction
from src.learning.learning_algorithm import LearningAlgorithm

# Lesson Content Imports
from src.lesson_content.content_map import initial_menu
from src.lesson_content.lesson_introduction import lesson_0_introduction
from src.lesson_content.lesson_tutorial import lesson_0_tutorial
from src.lesson_content.lesson_1 import lesson_1_timeline
from src.lesson_content.lesson_2 import lesson_2_timeline
from src.lesson_content.lesson_3 import lesson_3_timeline
from src.lesson_content.lesson_4 import lesson_4_timeline
from src.lesson_content.simple_spelling_words import spelling_words

TIME_UNTIL_HINT = 5

def main():

    interaction_module = Interaction(testing=False)
    # interaction_module.mute() #Mutes audio for faster testing

    option = 1  # Option Override

    # MAIN SEQUENCE
    if option == 1:

        # # Dot tutorial and quiz
        # Lesson(interaction_object=interaction_module,
        #        content=lesson_0_tutorial,
        #        time_until_hint=TIME_UNTIL_HINT)

        # quiz_content = ["Dot 1", "Dot 2", "Dot 3", "Dot 4", "Dot 5", "Dot 6", ]
        # random.shuffle(quiz_content)
        # q = Quiz(interaction_object=interaction_module,
        #          content=quiz_content,
        #          time_until_hint=TIME_UNTIL_HINT)
        # q.start_quiz()

        # # A-J lesson and quiz
        # Lesson(interaction_object=interaction_module,
        #        content=lesson_2_timeline,
        #        time_until_hint=TIME_UNTIL_HINT)

        # q = Quiz(interaction_object=interaction_module,
        #          content=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        #          time_until_hint=TIME_UNTIL_HINT)
        # q.start_quiz()

        # spelling_game = SpellingGame(
        #     interaction_object=interaction_module,
        #     spelling_word="dad",
        #     time_until_hint=TIME_UNTIL_HINT)
        # spelling_game.play()

        # # K-T lesson and quiz
        # Lesson(interaction_object=interaction_module,
        #        content=lesson_3_timeline,
        #        time_until_hint=TIME_UNTIL_HINT)

        # q = Quiz(interaction_object=interaction_module,
        #          content=list("klmnopqrst"),
        #          time_until_hint=TIME_UNTIL_HINT)
        # q.start_quiz()

        # spelling_game = SpellingGame(
        #     interaction_object=interaction_module,
        #     spelling_word="tail",
        #     time_until_hint=TIME_UNTIL_HINT)
        # spelling_game.play()

        # # U-Z lesson and quiz
        # Lesson(interaction_object=interaction_module,
        #        content=lesson_4_timeline,
        #        time_until_hint=TIME_UNTIL_HINT)

        # q = Quiz(interaction_object=interaction_module,
        #          content=list("uvwxyz"),
        #          time_until_hint=TIME_UNTIL_HINT)
        # q.start_quiz()

        # # Spelling game using a new word
        # spelling_game = SpellingGame(
        #     interaction_object=interaction_module, 
        #     spelling_word="umbrella", 
        #     time_until_hint=TIME_UNTIL_HINT)
        # spelling_game.play()

        # Final Quiz using the learning algorithm
        amount_of_characters = 10

        learning_algorithm = LearningAlgorithm()
        learning_algorithm.process_results()

        user_tailored_content = learning_algorithm.get_weighted_n_characters(
            amount_of_characters)

        print("-"*100)
        print("Quiz will be on the following characters: {}".format(
            user_tailored_content))
        print("-"*100)

        if len(user_tailored_content) == 0:
            interaction_module.speech.say(
                "Try another quiz so I can tailor a quiz to your strenghts and weakenesses")
        else:
            q = Quiz(interaction_object=interaction_module,
                     content=user_tailored_content,
                     time_until_hint=TIME_UNTIL_HINT)
            q.start_quiz()


# Main loop starts
if __name__ == "__main__":
    main()
