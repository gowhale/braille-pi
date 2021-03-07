import pytest
from src.braille.alphabet import Alphabet

@pytest.mark.parametrize(
    "test_input,expected",
    [("100000", "a"),
     ("101000", "b")],
)
def test_eval(test_input, expected):
    alphabet = Alphabet()
    assert (alphabet.translate_braille_to_alphabet(test_input)) == expected
