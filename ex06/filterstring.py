import sys
from ft_filter import ft_filter


def main():
    """Print the list of words of S whose length is greater than N."""
    try:
        args = sys.argv[1:]
        assert len(args) == 2, "the arguments are bad"
        text = args[0]
        assert all(c.isalnum() or c == " " for c in text), \
            "the arguments are bad"
        try:
            length = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")
        words = [word for word in text.split()]
        print(list(ft_filter(lambda word: len(word) > length, words)))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
