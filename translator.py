# Essential Imports
import time
from time import sleep


class Translator():
    """Translates inputs into braille characters A-Z.
    """

    def __init__(self, interaction_module):

        previous_time = time.time()
        start_time = time.time()

        # Forever loop which will ONLY exit if the program is ended
        expired_events = []
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
                previous_time = now

                time_since_start = float(now - start_time)
                print(difference, time_since_start)
                if interaction_module.using_raspberry_pi:
                    # Get dot hash from pins
                    current_dots_hash = (
                        interaction_module.current_char.get_current_dots_hash())
                else:
                    # Get dot hash from keyboard
                    current_dots_hash = interaction_module.check_keys(
                        interaction_module.pygame, interaction_module.dot_has_test)
                braille_translation = interaction_module.braille_alphabet.translate_braille_to_alphabet(
                    current_dots_hash)
                previous_time = now
                if interaction_module.show_gui:
                    interaction_module.graphical_user_interface.draw_dot_hash(
                        current_dots_hash, braille_translation)

                if braille_translation != previous_letter:
                    previous_letter = braille_translation
                    interaction_module.speech.say(braille_translation)
