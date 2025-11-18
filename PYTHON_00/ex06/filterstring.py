import sys
from ft_filter import ft_filter


def assertion_error(message):
    print(f"{AssertionError.__name__}: {message}")
    sys.exit(1)


def main():
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        assertion_error("the arguments are bad")

    res = ft_filter(lambda word: len(word) >= int(sys.argv[2]), sys.argv[1])

    print(res)


if __name__ == "__main__":
    main()
