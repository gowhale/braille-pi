from src.learning.spelling_game import SpellingGame

@when(u'a Spelling Game using the word John is completed correctly')
def step_impl(context):
    simulated_input = {
        1.1: ["d","j","k"],
        3: ["s","d","f","j"],
        4.5: ["s", "d"],
        6: ["j","d","s"],
    }

    context.spelling_game = SpellingGame(interaction_object=context.interaction_module,
    simulations=simulated_input,
    spelling_word="john",
    time_until_hint=40,
    max_timeout=10
    )
    context.spelling_game.play()


@then(u'The Spelling Game is completed succesfully')
def step_impl(context):
    assert context.spelling_game.test_failed == False