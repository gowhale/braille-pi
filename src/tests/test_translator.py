import pytest
from src.learning.translator import Translator
from src.interaction.interaction_module import Interaction

# @pytest.mark.timeout(5)
@pytest.mark.skip(reason="No way of mocking inputs yet.")
def test_translator():
    i = Interaction()
    Translator(i)