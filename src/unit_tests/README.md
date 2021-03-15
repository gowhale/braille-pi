# Unit Tests

In this folder there are unit tests for each class.

To run all of the unit tests enter the following command when in the braille-pi directory:

    pytest

Expected output:

    src/unit_tests/test_braille_alphabet.py .....            [ 29%]
    src/unit_tests/test_character.py s                       [ 35%]
    src/unit_tests/test_error_logger.py ..                   [ 47%]
    src/unit_tests/test_interaction_module.py ..             [ 58%]
    src/unit_tests/test_keyboard_interface.py ...            [ 76%]
    src/unit_tests/test_lesson.py .                          [ 82%]
    src/unit_tests/test_quiz.py .                            [ 88%]
    src/unit_tests/test_speech.py .                          [ 94%]
    src/unit_tests/test_translator.py s                      [100%]
    
    -- Docs: https://docs.pytest.org/en/stable/warnings.html
    ========== 15 passed, 2 skipped, 32 warnings in 4.18s ==========

Please note:

- warnings are not fatal and will hopefully be ironed out ASAP.
- if any test has failed there is a problem with the code and will not d=function as intended.
