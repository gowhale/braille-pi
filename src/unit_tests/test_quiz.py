import pytest
from src.learning.quiz import Quiz
from src.interaction.interaction_module import Interaction


@pytest.mark.timeout(10)
def test_lesson():
    i = Interaction(testing=True)

    i.speech.say = print

    simulated_input = {
        1.5: ["f"],
        3: ["d"],
    }

    quiz = Quiz(interaction_object=i, content="a",
                time_until_hint=10, simulations=simulated_input)
    quiz.start_quiz()

    assert 1 == 1
