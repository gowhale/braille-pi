import pytest
from src.interaction.speech import Speech

def test_speech():
    s = Speech()
    s.say("Testing 1 2 3")