class LearningTool():
    """ 
    This class contains common code used by both Quiz and Lesson Classes.
    """

    def __init__(self, interaction_object, content, time_until_hint) -> None:
        print("LearningTool Created")
        self.time_until_hint = time_until_hint
        # Initialisation of interaction elementes
        self.speech = interaction_object.speech
        self.using_raspberry_pi = interaction_object.using_raspberry_pi
        self.braille_alphabet = interaction_object.braille_alphabet
        self.pygame = interaction_object.pygame
        self.error_log = interaction_object.error_log
        if not interaction_object.using_raspberry_pi:
            self.current_char = ""
            self.check_keys = interaction_object.check_keys
            self.key_presses = interaction_object.key_presses
        else:
            self.current_char = interaction_object.current_char
        self.show_gui = interaction_object.show_gui
        if interaction_object.show_gui:
            self.graphical_user_interface = interaction_object.graphical_user_interface
