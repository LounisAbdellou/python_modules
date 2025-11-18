import sys


def error(message):
    print(f"{AssertionError.__name__}: {message}")
    sys.exit(1)


if len(sys.argv) > 2:
    error("more than one argument is provided")
elif len(sys.argv) == 2:
    if not sys.argv[1].lstrip("-+").isdigit():
        error("argument is not an integer")

    number = int(sys.argv[1])

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
