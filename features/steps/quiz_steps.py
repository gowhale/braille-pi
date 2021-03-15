from src.learning.quiz import Quiz


@when(u'An a quiz on letters is completed flawlessly')
def step_impl(context):
    simulated_input = {
        2: ["f"],
        3: ["d"],
        4: ["d", "j"],
        5: ["k"],
        6: ["j"],
        7: ["d", "j", "k"],
        8: ["k"],
        9: ["j"],
        10: ["f", "j", "k"],
        11: ["k"],
    }
    context.q = Quiz(interaction_object=context.interaction_module,
                     content=["a", "b", "c", "d", "e",
                              "f", "g", "h", "i", "j"],
                     time_until_hint=5,
                     simulations=simulated_input)
    context.q.start_quiz()


@then(u'The quiz is completed succesfully')
def step_impl(context):
    assert context.q.test_failed == False
