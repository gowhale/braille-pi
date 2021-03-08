import pytest
from src.learning.lesson import Lesson
from src.interaction.interaction_module import Interaction

# @pytest.mark.timeout(5)
@pytest.mark.skip(reason="No way of mocking inputs yet.")
def test_lesson():
    i = Interaction()
    Lesson(i)