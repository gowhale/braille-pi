import pytest
raspberry_pi_testing = True
try:
    import RPi.GPIO as GPIO
    from src.interaction.character import BrailleCharacter
except ModuleNotFoundError as e:
    raspberry_pi_testing = False

# To run this file execute the following:
# pytest --cov-report term-missing --cov=error_reporting .

# @pytest.mark.skip(reason="Only testable on raspberry-pi")
@pytest.mark.skipif(raspberry_pi_testing == False, reason="Platform is not raspberry pi")
def test_braille_character_class():
    GPIO.setmode(GPIO.BCM)
    BrailleCharacter()
