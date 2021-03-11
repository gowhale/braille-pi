# Functional Imports
from src.learning.translator import Translator
from src.learning.lesson import Lesson
from src.learning.quiz import Quiz
from src.interaction.interaction_module import Interaction

# Lesson Content Imports
from src.lesson_content.lesson_introduction import lesson_0_introduction
from src.lesson_content.lesson_tutorial import lesson_0_tutorial
from src.lesson_content.lesson_1 import lesson_1_timeline
from src.lesson_content.lesson_2 import lesson_2_timeline


def main():

    # TODO: this option value should be entered by the user in the future

    interaction_module = Interaction(testing=False)

    option = 5

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
                 content=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        q.start_quiz(5)


if __name__ == "__main__":
    main()
