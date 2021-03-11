from src.interaction.interaction_module import Interaction


@given(u'an interaction module has been created')
def step_impl(context):

    context.interaction_module = Interaction(testing=True)
    context.interaction_module.speech.say = print
