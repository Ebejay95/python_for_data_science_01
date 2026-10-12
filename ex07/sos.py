import sys


def to_morse(text: str) -> str:
    """Encode text (spaces and alphanumeric characters) into Morse Code.

    Raise an AssertionError if text contains an unsupported character.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
        "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
        "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. ",
    }
    assert all(c.upper() in NESTED_MORSE for c in text), \
        "the arguments are bad"
    return "".join(NESTED_MORSE[c.upper()] for c in text).rstrip(" ")


def main():
    """Print the Morse Code of the string given as argument."""
    try:
        args = sys.argv[1:]
        assert len(args) == 1, "the arguments are bad"
        print(to_morse(args[0]))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
