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


def test_translation_key_error():
    alphabet = Alphabet()

    assert (alphabet.translate_braille_to_alphabet("222222")) == "_"

def test_returns_alphabet_key_dictionary():
    expected_output = {
        "a": "100000",
        "b": "101000",
        "c": "110000",
        "d": "110100",
        "e": "100100",
        "f": "111000",
        "g": "111100",
        "h": "101100",
        "i": "011000",
        "j": "011100",
        "k": "100010",
        "l": "101010",
        "m": "110010",
        "n": "110110",
        "o": "100110",
        "p": "111010",
        "q": "111110",
        "r": "101110",
        "s": "011010",
        "t": "011110",
        "u": "100011",
        "v": "101011",
        "w": "011101",
        "x": "110011",
        "y": "110111",
        "z": "100111",
    }

    alphabet = Alphabet()

    assert alphabet.get_alphabet_to_braille() == expected_output

def test_returns_braille_key_dictionary():
    expected_output = {
        "100000" : "a",
        "101000" : "b",
        "110000" : "c",
        "110100" : "d",
        "100100" : "e",
        "111000" : "f",
        "111100" : "g",
        "101100" : "h",
        "011000" : "i",
        "011100" : "j",
        "100010" : "k",
        "101010" : "l",
        "110010" : "m",
        "110110" : "n",
        "100110" : "o",
        "111010" : "p",
        "111110" : "q",
        "101110" : "r",
        "011010" : "s",
        "011110" : "t",
        "100011" : "u",
        "101011" : "v",
        "011101" : "w",
        "110011" : "x",
        "110111" : "y",
        "100111" : "z",
    }

    alphabet = Alphabet()

    assert alphabet.get_braille_to_alphabet() == expected_output
