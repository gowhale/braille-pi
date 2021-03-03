# Essential Imports
from translator import Translator
from lesson_one import LessonOne


def main():

    # TODO: this option value should be entered by the user in the future

    option = 2

    if option == 1:
        translator = Translator()

    if option == 2:
        lesson_one = LessonOne()


if __name__ == "__main__":
    main()
