import pytest
from src.interaction.speech import Speech

def test_speech_initialise():
    s = Speech()
    s.say("Testing 1 2 3")

def test_speech_string_using_symbols():
    s = Speech()
    s.say("'/.;,Hello ' did this work? ''' ")