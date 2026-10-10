import sys


def main():
    """Print whether the integer given as argument is odd or even."""
    args = sys.argv[1:]
    try:
        if len(args) == 0:
            return
        assert len(args) == 1, "more than one argument is provided"
        try:
            number = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
