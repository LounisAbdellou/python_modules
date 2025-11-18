import sys
from morse import morse_map


def assertion_error(message):
    print(f"{AssertionError.__name__}: {message}")
    sys.exit(1)


def is_valid(text):
    return sum(1 for char in text if not char.isalnum() or not char.isspace()) == 0


def main():
    if len(sys.argv) != 2 or is_valid(sys.argv[1]):
        assertion_error("the arguments are bad")

    res = [morse_map[char.upper()] for char in sys.argv[1]]

    print(" ".join(res))


if __name__ == "__main__":
    main()
