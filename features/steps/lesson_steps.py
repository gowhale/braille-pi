# Functional Imports
from src.learning.translator import Translator
from src.learning.lesson import Lesson
from src.learning.quiz import Quiz
from src.interaction.interaction_module import Interaction

# Lesson Content Imports
from src.lesson_content.lesson_introduction import lesson_0_introduction
from src.lesson_content.lesson_tutorial import lesson_0_tutorial
from src.lesson_content.lesson_1 import lesson_1_timeline
from src.lesson_content.lesson_2 import lesson_2_timeline


@given(u'an interaction module has been created')
def step_impl(context):

    context.interaction_module = Interaction()


@when(u'An A-J lesson is completed correctly')
def step_impl(context):

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
        4.5: "C.",
        5: 9,
        5.5: CORRECT_ANSWER,
        6: "D.",
        6.5: 10,
        7: CORRECT_ANSWER,
        7.5: "E.",
        8: 11,
        8.5: CORRECT_ANSWER,
        9: "F.",
        9.5: 12,
        10: CORRECT_ANSWER,
        10.5: "G.",
        11: 13,
        11.5: CORRECT_ANSWER,
        12: "H.",
        12.5: 14,
        13: CORRECT_ANSWER,
        13.5: "I.",
        14: 15,
        14.5: CORRECT_ANSWER,
        15: "J.",
        15.5: 16,
        16: CORRECT_ANSWER,
    }

    context.interaction_module.speech.say = print

    simulated_input = {
        1.5: ["f"],
        3: ["d"],
        4.5: ["d","j"],
        6: ["k"],
        7.5: ["j"],
        9: ["d","j","k"],
        10.5: ["k"],
        12: ["j"],
        13.5: ["f","j","k"],
        15: ["k"],
    }

    context.lesson = Lesson(context.interaction_module,
                            test_content, simulated_input, max_timeout=20)


@then(u'The lesson is completed succesfully')
def step_impl(context):
    assert context.lesson.test_failed == False
