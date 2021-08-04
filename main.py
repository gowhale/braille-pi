# Additional modules
import random

# Functional Imports
from src.learning.translator import Translator
from src.learning.lesson import Lesson
from src.learning.quiz import Quiz
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


def main():

    # TODO: this option value should be entered by the user in the future

    interaction_module = Interaction(testing=False)

    # The below object lets the user select what they wish to do i.e. take a lesson or quiz
    # For testing purposes it is best to comment this out and state the option value (Line 33)
    # content_selection = ContentSelection(interaction_object=interaction_module,
    #                                      possible_choices=initial_menu,
    #                                      test_content=None,
    #                                      max_timeout=None)

    # option = content_selection.get_choice()
    option = 12  # Option Override

    # TRANSLATOR OPTION -> Translates entered dots to A-Z chars
    if option == 1:
        Translator(interaction_object=interaction_module)

    # INTROCUTORY LESSON -> Introduces the Braille Pi and the importance of learning braille
    if option == 2:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_introduction,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)

    # TUTORIAL -> Goes through each dot
    if option == 3:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_tutorial,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)

    # LESSON 1 -> A, B. C's in braille
    if option == 4:
        Lesson(interaction_object=interaction_module,
               content=lesson_1_timeline,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)

    # LESSON 2 -> A-J lesson. These characters are the building blocks of braille
    if option == 5:
        Lesson(interaction_object=interaction_module,
               content=lesson_2_timeline,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)

    # QUIZ 2 -> A-J QUIZ.
    if option == 6:
        q = Quiz(interaction_object=interaction_module,
                 content=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
                 time_until_hint=10,
                 simulations=None)
        q.start_quiz()

    # LESSON 3 -> K-T lesson.
    if option == 7:
        Lesson(interaction_object=interaction_module,
               content=lesson_3_timeline,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)

    # Quiz 3: K to T
    if option == 10:
        q = Quiz(interaction_object=interaction_module,
                 content=list("klmnopqrst"),
                 time_until_hint=5,
                 simulations=None)
        q.start_quiz()

    # LESSON 4 -> U-Z lesson.
    if option == 8:
        Lesson(interaction_object=interaction_module,
               content=lesson_4_timeline,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)

    # QUIZ 3 -> U-Z QUIZ.
    if option == 15:
        q = Quiz(interaction_object=interaction_module,
                 content=[list("uvwxyz")],
                 time_until_hint=10,
                 simulations=None)
        q.start_quiz()

    # QUIZ Using learning algorithm.
    if option == 9:

        amount_of_characters = 5

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
                     time_until_hint=10,
                     simulations=None)
            q.start_quiz()

    # Voice actor demonstration
    # Currently Dot tutorial and Lesson 2 contains voice over
    if option == 11:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_tutorial,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)
        Lesson(interaction_object=interaction_module,
               content=lesson_2_timeline,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)

    # User Testing Sequence Option
    if option == 12:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_tutorial,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)
        quiz_content = ["Dot 1", "Dot 2", "Dot 3", "Dot 4", "Dot 5", "Dot 6", ]
        random.shuffle(quiz_content)
        q = Quiz(interaction_object=interaction_module,
                 content=quiz_content,
                 time_until_hint=10,
                 simulations=None)
        q.start_quiz()
        Lesson(interaction_object=interaction_module,
               content=lesson_2_timeline,
               test_content=None,
               max_timeout=None,
               time_until_hint=20)
        q = Quiz(interaction_object=interaction_module,
                 content=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
                 time_until_hint=10,
                 simulations=None)
        q.start_quiz()

    # QUIZ 4 -> SEQUENTIAL Quiz on dots.
    if option == 16:
        quiz_content = ["Dot 1", "Dot 2", "Dot 3", "Dot 4", "Dot 5", "Dot 6", ]
        q = Quiz(interaction_object=interaction_module,
                 content=quiz_content,
                 time_until_hint=10,
                 simulations=None)
        q.start_quiz()

    # QUIZ 5 -> RANDOM Quiz on dots.
    if option == 17:
        quiz_content = ["Dot 1", "Dot 2", "Dot 3", "Dot 4", "Dot 5", "Dot 6", ]
        random.shuffle(quiz_content)
        q = Quiz(interaction_object=interaction_module,
                 content=quiz_content,
                 time_until_hint=10,
                 simulations=None)
        q.start_quiz()


# Main loop starts
if __name__ == "__main__":
    main()
