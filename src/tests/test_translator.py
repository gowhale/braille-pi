import pytest
from src.learning.translator import Translator
from src.interaction.interaction_module import Interaction

@pytest.mark.timeout(5)
def test_translator():
    i = Interaction()
    Translator(i)