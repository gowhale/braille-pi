# Functional Imports
from src.learning.translator import Translator
from src.learning.lesson import Lesson
from src.interaction.interaction_module import Interaction

# Lesson Content Imports
from src.lesson_content.lesson_introduction import lesson_0_introduction
from src.lesson_content.lesson_tutorial import lesson_0_tutorial
from src.lesson_content.lesson_1 import lesson_1_timeline
from src.lesson_content.lesson_2 import lesson_2_timeline


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

    simulated_input = {
        1.5: ["f"],
        3: ["d"],
        4.5: ["d", "j"],
        6: ["k"],
        7.5: ["j"],
        9: ["d", "j", "k"],
        10.5: ["k"],
        12: ["j"],
        13.5: ["f", "j", "k"],
        15: ["k"],
    }

    context.lesson = Lesson(context.interaction_module,
                            test_content, simulated_input, max_timeout=20)


@when(u'An K-T lesson is completed correctly')
def step_impl(context):

    CORRECT_ANSWER = "Correct"
    test_content = {
        0: "EMPTY CELL",
        0.5: 1,
        1: CORRECT_ANSWER,
        1.5: "K.",
        2: 17,
        2.5: CORRECT_ANSWER,
        3: "L.",
        3.5: 18,
        4: CORRECT_ANSWER,
        4.5: "M.",
        5: 19,
        5.5: CORRECT_ANSWER,
        6: "N.",
        6.5: 20,
        7: CORRECT_ANSWER,
        7.5: "O.",
        8: 21,
        8.5: CORRECT_ANSWER,
        9: "P.",
        9.5: 22,
        10: CORRECT_ANSWER,
        10.5: "Q.",
        11: 23,
        11.5: CORRECT_ANSWER,
        12: "R.",
        12.5: 24,
        13: CORRECT_ANSWER,
        13.5: "S.",
        14: 25,
        14.5: CORRECT_ANSWER,
        15: "T.",
        15.5: 26,
        16: CORRECT_ANSWER,
    }

    simulated_input = {
        1.5: ["f", "s"],
        3: ["d"],
        4.5: ["d", "j"],
        6: ["k"],
        7.5: ["j"],
        9: ["d", "j", "k"],
        10.5: ["k"],
        12: ["j"],
        13.5: ["f", "j", "k"],
        15: ["k"],
    }

    context.lesson = Lesson(context.interaction_module,
                            test_content, simulated_input, max_timeout=20)

@when(u'An U-Z lesson is completed correctly')
def step_impl(context):

    CORRECT_ANSWER = "Correct"
    test_content = {
        0: "EMPTY CELL",
        0.5: 1,
        1: CORRECT_ANSWER,
        1.5: "K.",
        2: 27,
        2.5: CORRECT_ANSWER,
        3: "L.",
        3.5: 28,
        4: CORRECT_ANSWER,
        4.5: "M.",
        5: 29,
        5.5: CORRECT_ANSWER,
        6: "N.",
        6.5: 30,
        7: CORRECT_ANSWER,
        7.5: "O.",
        8: 31,
        8.5: CORRECT_ANSWER,
        9: "P.",
        9.5: 32,
        10: CORRECT_ANSWER,
    }

    simulated_input = {
        1.5: ["f", "s", "l"],
        3: ["d"],
        4.5: ["d", "j"],
        6: ["k"],
        7.5: ["j"],
        9: ["d", "j","f","s"],
        
    }

    context.lesson = Lesson(context.interaction_module,
                            test_content, simulated_input, max_timeout=20)


@when(u'Lesson 0 completed correctly')
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
        3.5: 3,
        4: CORRECT_ANSWER,
        4.5: "C.",
        5: 4,
        5.5: CORRECT_ANSWER,
        6: "D.",
        6.5: 5,
        7: CORRECT_ANSWER,
        7.5: "E.",
        8: 6,
        8.5: CORRECT_ANSWER,
        9: "F.",
        9.5: 7,
        10: CORRECT_ANSWER,
    }

    simulated_input = {
        1.5: ["f"],
        3: ["f", "d"],
        4.5: ["d", "s"],
        6: ["s", "j"],
        7.5: ["j", "k"],
        9: ["k", "l"],
    }

    context.lesson = Lesson(context.interaction_module,
                            test_content, simulated_input, max_timeout=60)


@when(u'An A-C lesson is completed correctly')
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
        3.5: 3,
        4: CORRECT_ANSWER,
        4.5: "C.",
        5: 4,
        5.5: CORRECT_ANSWER,
    }

    simulated_input = {
        1.5: ["f"],
        3: ["f", "d"],
        4.5: ["d", "s"],
    }

    context.lesson = Lesson(context.interaction_module,
                            test_content, simulated_input, max_timeout=60)


@then(u'The lesson is completed succesfully')
def step_impl(context):
    assert context.lesson.test_failed == False
