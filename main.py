# Functional Imports
from src.learning.translator import Translator
from src.learning.lesson import Lesson
from src.learning.quiz import Quiz
from src.learning.content_selection import ContentSelection
from src.interaction.interaction_module import Interaction
from src.learning.learning_algorithm import LearningAlgorithm

# Lesson Content Imports
from src.lesson_content.lesson_introduction import lesson_0_introduction
from src.lesson_content.lesson_tutorial import lesson_0_tutorial
from src.lesson_content.lesson_1 import lesson_1_timeline
from src.lesson_content.lesson_2 import lesson_2_timeline
from src.lesson_content.lesson_3 import lesson_3_timeline
from src.lesson_content.lesson_4 import lesson_4_timeline


def main():

    # TODO: this option value should be entered by the user in the future

    interaction_module = Interaction(testing=False)

    option = 5

    content_selection = ContentSelection(interaction_object=interaction_module,
                                         possible_choices=[
                                             "100000", "100000", "100000", "100000", "100000"],
                                         test_content=None,
                                         max_timeout=None)

    # TRANSLATOR OPTION -> Translates entered dots to A-Z chars
    if option == 1:
        Translator(interaction_object=interaction_module)

    # INTROCUTORY LESSON -> Introduces the Braille Pi and the importance of learning braille
    if option == 2:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_introduction,
               test_content=None,
               max_timeout=None)

    # TUTORIAL -> Goes through each dot
    if option == 3:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_tutorial,
               test_content=None,
               max_timeout=None)

    # LESSON 1 -> A, B. C's in braille
    if option == 4:
        Lesson(interaction_object=interaction_module,
               content=lesson_1_timeline,
               test_content=None,
               max_timeout=None)

    # LESSON 2 -> A-J lesson. These characters are the building blocks of braille
    if option == 5:
        Lesson(interaction_object=interaction_module,
               content=lesson_2_timeline,
               test_content=None,
               max_timeout=None)

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
               max_timeout=None)

    # LESSON 4 -> U-W lesson.
    if option == 8:
        Lesson(interaction_object=interaction_module,
               content=lesson_4_timeline,
               test_content=None,
               max_timeout=None)

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

    # Quiz 3: K to T
    if option == 10:
        q = Quiz(interaction_object=interaction_module,
                 content=list("klmnopqrst"),
                 time_until_hint=5,
                 simulations=None)
        q.start_quiz()

    # Voice actor demonstration
    # Currently Dot tutorial and Lesson 2 contains voice over
    if option == 11:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_tutorial,
               test_content=None,
               max_timeout=None)
        Lesson(interaction_object=interaction_module,
               content=lesson_2_timeline,
               test_content=None,
               max_timeout=None)


if __name__ == "__main__":
    main()
