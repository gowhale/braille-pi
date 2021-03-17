import pytest
from src.learning.quiz import Quiz
from src.interaction.interaction_module import Interaction


@pytest.mark.timeout(10)
def test_lesson():
    i = Interaction(testing=True)

    i.speech.say = print

    quiz = Quiz(interaction_object=i, content=[],
                time_until_hint=1, simulations={})
    quiz.start_quiz()

    assert 1 == 1
