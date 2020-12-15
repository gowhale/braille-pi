from subprocess import call


class Speech:

    cmd_start = 'espeak '
    cmd_finish = '>/dev/null'

    def __init__(self):
        print("""Pi will say 'Now we can begin!'""")
        self.say("""Now we can begin!""")

    def say(self, text):
        text = text.replace(" ", "_")
        call([self.cmd_start+text+self.cmd_finish], shell=True)

# speech = Speech()
# speech.say("This class makes the pi speak")
