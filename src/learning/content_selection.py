import time


class ContentSelection():
    """ 
    This class is used to start enable the use to select content using the 6 dots.

    Extended description of function. 

    Attributes: 
        interaction_object  (Interaction): The interaction object which tells the system how the user will interact.
        possible_choices    (dict): This varibale dictates the choices a user can make.
        test_content        (dict): This parameter dictates whether simulated events will be executed.
        max_timeout         (int): This is the maximum amount of seconds before the lesson is terminated.
    """
    chosen_option = -1

    def __init__(self, interaction_object, possible_choices, test_content, max_timeout):

        # Testing variables
        self.test_failed = False
        self.test_content = test_content
        self.max_timeout = max_timeout
        self.simulations_executed = []

        # Content selection varibales
        self.time_since_start = 0
        self.possible_choices = possible_choices

        # Initiation of interaction elements
        self.speech = interaction_object.speech
        self.using_raspberry_pi = interaction_object.using_raspberry_pi
        self.braille_alphabet = interaction_object.braille_alphabet
        self.pygame = interaction_object.pygame
        if self.test_content != None:
            self.using_raspberry_pi = False
        if not self.using_raspberry_pi:
            self.current_char = ""
            self.check_keys = interaction_object.check_keys
            self.key_presses = interaction_object.key_presses
        else:
            self.current_char = interaction_object.current_char
        self.show_gui = interaction_object.show_gui
        if interaction_object.show_gui:
            self.graphical_user_interface = interaction_object.graphical_user_interface
            self.graphical_user_interface.show_welcome_screen()

        self.choose()

    def choose(self):
        """This method starts process of choosing a choice."""

        self.speech.say("Please choose the content you wish to play.")

        for dot_hash in self.possible_choices:
            msg = self.possible_choices[dot_hash]["message"]
            self.speech.say(msg)

        self.speech.say("Please choose the content you wish to play.")

        current_dots_hash = "INIT"
        asserted_answer = "Test"

        now = time.time()
        self.start_time = now
        self.previous_time = now
        
        # while loop until a possible choice is selected.
        while current_dots_hash not in self.possible_choices:
            now = time.time()
            difference = float(now-self.previous_time)

            if difference > 0.1:
                print(current_dots_hash)
                now = time.time()
                self.previous_time = now

                if self.using_raspberry_pi:
                    # Get dot hash from pins
                    current_dots_hash = (
                        self.current_char.get_current_dots_hash())
                else:
                    # Get dot hash from keyboard
                    current_dots_hash = self.check_keys(
                        self.pygame, self.key_presses)

                if self.show_gui:
                    self.graphical_user_interface.draw_dot_hash(
                        current_dots_hash, "")

                if self.max_timeout != None and (now - self.start_time) > self.max_timeout:
                    self.test_failed = True
                    current_dots_hash = asserted_answer

        self.graphical_user_interface.draw_dot_hash(
            asserted_answer, "")

        self.speech.play_sound("correct")

        option = self.possible_choices[current_dots_hash]["option"]
        description = self.possible_choices[current_dots_hash]["description"]
        self.speech.say(description)
        self.chosen_option = option

    def get_choice(self):
        """Returns the value of the chosen option"""
        return self.chosen_option
