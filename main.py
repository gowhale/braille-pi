# Essential Imports
from translator import Translator
from lesson import Lesson
from interaction_module import Interaction


def main():

    # TODO: this option value should be entered by the user in the future

    interaction_module = Interaction()

    option = 2

    if option == 1:
        Translator(interaction_module)

    if option == 2:
        Lesson(interaction_module)


if __name__ == "__main__":
    main()
