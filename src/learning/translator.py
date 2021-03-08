# Essential Imports
import time
from time import sleep


class Translator():
    """Translates inputs into braille characters A-Z.
    """

    def __init__(self, interaction_object):

        previous_time = time.time()
        start_time = time.time()

        # Forever loop which will ONLY exit if the program is ended
        previous_letter = "_"

        # if the lesson is still live then this loop will continue
        lesson_live = True
        while lesson_live:
            # Check if enough time has passed to update GUI
            now = time.time()
            difference = float(now-previous_time)

            # Checks timelines every 0.5 seconds
            if difference > 0.5:
                print(difference)
                # speech.say(current_dots_hash)

                time_since_start = float(now - start_time)
                print(difference, time_since_start)
                if interaction_object.using_raspberry_pi:
                    # Get dot hash from pins
                    current_dots_hash = (
                        interaction_object.current_char.get_current_dots_hash())
                else:
                    # Get dot hash from keyboard
                    current_dots_hash = interaction_object.check_keys(
                        interaction_object.pygame, interaction_object.dot_has_test)
                braille_translation = interaction_object.braille_alphabet.translate_braille_to_alphabet(
                    current_dots_hash)
                previous_time = now
                if interaction_object.show_gui:
                    interaction_object.graphical_user_interface.draw_dot_hash(
                        current_dots_hash, braille_translation)

                if braille_translation != previous_letter:
                    previous_letter = braille_translation
                    interaction_object.speech.say(braille_translation)
