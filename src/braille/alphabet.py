class Alphabet ():

    """The Alphabet class contains information about braille to A_Z characters.
    
    Attributes:
        alphabet_to_braille (Dict)    Letters identify thier own braille values.
    """

    alphabet_to_braille = {
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

    dots_to_braille = {
        "Dot 1": "100000",
        "Dot 2": "001000",
        "Dot 3": "000010",
        "Dot 4": "010000",
        "Dot 5": "000100",
        "Dot 6": "000001",
    }

    custom_chars_to_braille = {
        "_" : "000000",
    }

    custom_hints = {
        "Dot 1": "Raise the left top dot only",
        "Dot 2": "Raise the left middle dot only",
        "Dot 3": "Raise the left bottum dot only",
        "Dot 4": "Raise the right top dot only",
        "Dot 5": "Raise the right middle dot only",
        "Dot 6": "Raise the rigth bottum dot only",
        "_": "Please make sure all dots are flat with the board or lowered"
    }

    braille_to_alphabet = {
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

    all_chars_to_braille = {**alphabet_to_braille, **dots_to_braille , **custom_chars_to_braille}


    def __init__(self):
        """Initialises the Alphabet Object to have the inverse of the braille alphabet.
        
        The unique identifier will be the dothash rather than the letter."""



    def get_braille_to_alphabet(self):
        """Returns the braille_to_alphabet dictionary."""

        return self.braille_to_alphabet

    def get_alphabet_to_braille(self):
        """Returns the alphabet_to_braille dictionary."""

        return self.alphabet_to_braille

    def translate_braille_to_alphabet(self, braille):
        """Translate a braille hash into a letter."""

        try:
            return self.braille_to_alphabet[braille]
        except KeyError:
            return "_"

    def translate_alphabet_to_braille(self, letter):
        """Translate an A-Z letter into a braille hash."""
        try:
            return self.alphabet_to_braille[letter]
        except KeyError as e:
            print(e)
            return "000000"

    def translate_char_to_braille(self, char):
        """Translate ANY char into a braille hash."""
        try:
            return self.all_chars_to_braille[char]
        except KeyError as e:
            print(e)
            return "000000"
