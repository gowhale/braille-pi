import pytest
# from ..alphabet import Alphabet

@pytest.mark.parametrize(
    "test_input,expected",
    [("100000", "a"),
     ("101000", "b")],
)
def test_eval(test_input, expected):
    alphabet = Alphabet()
    assert eval(alphabet.translate_braille_to_alphabet(test_input)) == expected
