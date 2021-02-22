from subprocess import call
from sys import platform
try:
    from os import system
except ModuleNotFoundError:
    "OS Note found"


class Speech:

    operating_system = ""

    cmd_start = 'espeak '
    cmd_finish = '>/dev/null'

    def __init__(self):
        print("""Pi will say 'Now we can begin!'""")

        self.operating_system = platform

        self.say("""Now we can begin!""")

    def say(self, text):
        current_os = self.operating_system
        text = text.replace(" ", "_")
        if current_os == "linux" or current_os == "linux2":
            call([self.cmd_start+text+self.cmd_finish], shell=True)
        elif current_os == "darwin":
            system('say {}'.format(text))
            # OS X
        elif current_os == "win32":
            # Windows...
            print("WINDOWS OS NOT FI=OUND")

# speech = Speech()
# speech.say("This class makes the pi speak")
