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

    def __init__(self):
        """Sets the operating system of the object."""
        print("""Speech object initiated!'""")

        sound_effects = os.listdir(self.sound_effects_directory)
        pattern = "*.wav"
        for entry in sound_effects:
            if fnmatch.fnmatch(entry, pattern):
                self.sound_effects_file_names.append(entry)

        voice_files = os.listdir(self.voice_file_directory)
        pattern = "*.wav"
        for entry in voice_files:
            if fnmatch.fnmatch(entry, pattern):
                self.voice_file_file_names.append(entry)

        print("Voice actor files:")
        for name in self.voice_file_file_names:
            print(name)
        print()

        print("Sound files:")
        for name in self.sound_effects_file_names:
            print(name)
        print()

        self.operating_system = platform

        self.say("test_sound.wav")

    def say(self, text):
        """This method says the text which is passed through the function.

        Arguments:
            text    (String)    text which will be spoken."""

        print("SAYING -> {}".format(text))

        current_os = self.operating_system
        text = text.replace(" ", "_")

        if text in self.voice_file_file_names:
            voice_file_address = "{}/{}".format(
                self.voice_file_directory, text)
            playsound(voice_file_address)

        else:
            sanitised_text = text.translate(
                str.maketrans('', '', string.punctuation))
            if current_os == "linux" or current_os == "linux2":
                call([self.cmd_start+sanitised_text+self.cmd_finish], shell=True)
            elif current_os == "darwin":
                # OS X (Macbook)
                system('say {}'.format(sanitised_text))
            elif current_os == "win32":
                # Windows...
                print("Windows edition coming soon.")
