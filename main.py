# Functional Imports
from src.learning.translator import Translator
from src.learning.lesson import Lesson
from src.interaction.interaction_module import Interaction

# Lesson Content Imports
from src.lesson_content.lesson_introduction import lesson_0_introduction
from src.lesson_content.lesson_tutorial import lesson_0_tutorial


def main():

    # TODO: this option value should be entered by the user in the future

    interaction_module = Interaction()

    option = 2

    if option == 1:
        Translator(interaction_module)

    if option == 2:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_introduction)

    if option == 3:
        Lesson(interaction_object=interaction_module,
               content=lesson_0_tutorial)


if __name__ == "__main__":
    main()
