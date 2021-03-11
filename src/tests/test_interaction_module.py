import pytest
from src.interaction.interaction_module import Interaction
from src.interaction.speech import Speech

# To run this file execute the following:
# pytest --cov-report term-missing --cov=error_reporting .

def test_interaction_module():
    interaction = Interaction(testing=False)

    assert interaction.show_gui == True

def test_interaction_module_error_logger():
    interaction = Interaction(testing=False)

    assert type(interaction.speech) is Speech


