import pytest
from src.learning.lesson import Lesson
from src.interaction.interaction_module import Interaction

@pytest.mark.timeout(5)
def test_lesson():
    i = Interaction()
    Lesson(i)