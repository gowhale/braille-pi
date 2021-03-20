from subprocess import call
from sys import platform
try:
    from os import system
except ModuleNotFoundError:
    "OS Note found"
import string

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

    def __init__(self):
        """Sets the operating system of the object."""
        print("""Speech object initiated!'""")
        self.operating_system = platform

    def say(self, text):
        """This method says the text which is passed through the function.

        Arguments:
            text    (String)    text which will be spoken."""

         
        sanitised_text = text.translate(str.maketrans('', '', string.punctuation))

        print("SAYING -> {}".format(sanitised_text))
        current_os = self.operating_system
        sanitised_text = sanitised_text.replace(" ", "_")
        if current_os == "linux" or current_os == "linux2":
            call([self.cmd_start+sanitised_text+self.cmd_finish], shell=True)
        elif current_os == "darwin":
            # OS X (Macbook)
            system('say {}'.format(sanitised_text))
        elif current_os == "win32":
            # Windows...
            print("Windows edition coming soon.")
