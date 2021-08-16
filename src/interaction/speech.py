from subprocess import call
from sys import platform
try:
    from os import system
except ModuleNotFoundError:
    "OS Note found"
import string
import os
import fnmatch
from playsound import playsound
from string import punctuation
import pygame


class Speech:
    """The purpose of this class it to verbally speak out strings.

    Attributes:
        operating_system    (String)    text which defines what OS the code is running on.
        cmd_start           (String)    start of the linux speak command.
        cmd_finish          (String)    end of the linux speak command.
    """

    operating_system = ""
    cmd_start = 'espeak '
    cmd_finish = '>/dev/null'

    sound_effects_directory = 'sounds/sound_effects'
    sound_effects_file_names = []

    voice_file_directory = 'sounds/voice_files'
    voice_file_file_names = []

    sound_file_extension = ".mp3"

    mute = False

    def __init__(self):
        """Sets the operating system of the object."""
        print("""Speech object initiated!'""")

        # Finds all sound and voiceover files matching sound file extension
        pattern = "*" + self.sound_file_extension

        sound_effects = os.listdir(self.sound_effects_directory)
        for entry in sound_effects:
            if fnmatch.fnmatch(entry, pattern):
                self.sound_effects_file_names.append(entry)

        voice_files = os.listdir(self.voice_file_directory)
        for entry in voice_files:
            if fnmatch.fnmatch(entry, pattern):
                self.voice_file_file_names.append(entry)

        self.operating_system = platform

    def convert_to_file_name(self, text):
        sentence = str(text).replace(" ", "_")
        my_punctuation = punctuation.replace("_", "")
        sentence = (sentence.translate(
            str.maketrans("", "", my_punctuation))).lower()
        file_name = sentence + self.sound_file_extension
        return (file_name)

    def play_sound(self, sound):
        """Plays a sound effect."""
        current_os = self.operating_system
        sound_file_name = sound + self.sound_file_extension
        if sound_file_name in self.sound_effects_file_names:
            sound_file_address = "{}/{}".format(
                self.sound_effects_directory, sound_file_name)

            if current_os == "linux" or current_os == "linux2":
                # Raspberry Pi
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file_address)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

            elif current_os == "darwin":
                # OS X (Macbook)
                playsound(sound_file_address)
            elif current_os == "win32":
                # Windows...
                print("Windows edition coming soon.")
        else:
            print("SOUND FILE NEEDED")

    def say(self, text):
        """This method says the text which is passed through the function.

        Arguments:
            text    (String)    text which will be spoken."""

        print("SAYING -> {}".format(text))

        if (not self.mute):

            current_os = self.operating_system

            snake_case_text = text.replace(" ", "_")

            file_name = self.convert_to_file_name(snake_case_text)

            if file_name in self.voice_file_file_names:
                # If sound file available play it

                voice_file_address = "{}/{}".format(
                    self.voice_file_directory, file_name)

                if current_os == "linux" or current_os == "linux2":
                    # Raspberry Pi
                    pygame.mixer.init()
                    pygame.mixer.music.load(voice_file_address)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue

                elif current_os == "darwin":
                    # OS X (Macbook)
                    playsound(voice_file_address)
                elif current_os == "win32":
                    # Windows...
                    print("Windows edition coming soon.")

            else:
                print("VOICE FILE NEEDED")

                # with open("voice_files_needed.txt", "a") as myfile:
                #     myfile.write("-{}\n".format(text))

                # Narrating the passed text
                if current_os == "linux" or current_os == "linux2":
                    call([self.cmd_start+snake_case_text+self.cmd_finish], shell=True)
                elif current_os == "darwin":
                    # OS X (Macbook)
                    system('say {}'.format(snake_case_text))
                elif current_os == "win32":
                    # Windows...
                    print("Windows edition coming soon.")

    def set_mute(self):
        self.mute = True
