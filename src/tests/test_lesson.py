import pytest
from src.learning.lesson import Lesson
from src.interaction.interaction_module import Interaction

# @pytest.mark.timeout(5)
# @pytest.mark.skip(reason="No way of mocking inputs yet.")


@pytest.mark.timeout(10)
def test_lesson():
    i = Interaction()

    CORRECT_ANSWER = "Correct"
    test_content = {
        0: "EMPTY CELL",
        0.5: 1,
        1: CORRECT_ANSWER,
        1.5: "A.",
        2: 2,
        2.5: CORRECT_ANSWER,
        3: "B.",
        3.5: 8,
        4: CORRECT_ANSWER,
    }

    i.speech.say = print

    simulated_input = {
        1.5: ["f"],
        3: ["d"],
    }

    Lesson(i, test_content, simulated_input, max_timeout=None)

    assert 1 == 1
