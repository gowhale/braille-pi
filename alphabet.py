class Alphabet ():

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
        "l": "100010",
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

    def __init__(self):
        print("Alphabet Generated")

        braille_to_alphabet = {}

        for key in self.alphabet_to_braille:

            braille_to_alphabet[self.alphabet_to_braille[key]] = key

        self.braille_to_alphabet = braille_to_alphabet

    def get_braille_to_alphabet(self):
        return self.braille_to_alphabet

    def get_alphabet_to_braille(self):
        return self.alphabet_to_braille

    def translate_braille_to_alphabet(self, braille):
        try:
            return self.braille_to_alphabet[braille]
        except KeyError:
            return "NO CHAR FOUND"
