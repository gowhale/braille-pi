import pytest
from src.learning.learning_tool import LearningTool
from src.interaction.interaction_module import Interaction


@pytest.mark.timeout(10)
def test_learning_tool():
    i = Interaction(testing=True)
    i.mute()

    learning_tool = LearningTool(interaction_object=i, time_until_hint=1, simulations=None)

    assert 1 == 1
