import pytest
from src.learning.spelling_game import SpellingGame
from src.interaction.interaction_module import Interaction


@pytest.mark.timeout(10)
def test_lesson():
    i = Interaction(testing=True)
    i.mute()

    quiz = SpellingGame(interaction_object=i, spelling_word="")

    assert 1 == 1
