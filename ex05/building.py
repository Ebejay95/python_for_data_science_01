import sys
import string


def count_chars(text: str) -> dict:
    """Return the number of upper, lower, punctuation, space and digit
    characters contained in text."""
    return {
        "upper letters": sum(1 for c in text if c.isupper()),
        "lower letters": sum(1 for c in text if c.islower()),
        "punctuation marks": sum(1 for c in text if c in string.punctuation),
        "spaces": sum(1 for c in text if c.isspace()),
        "digits": sum(1 for c in text if c.isdigit()),
    }


def main():
    """Count and display the character categories of the text given as
    argument, or of the text read from stdin if no argument is given."""
    try:
        args = sys.argv[1:]
        assert len(args) <= 1, "more than one argument is provided"
        if len(args) == 0:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = args[0]
        print(f"The text contains {len(text)} characters:")
        for name, count in count_chars(text).items():
            print(f"{count} {name}")
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
