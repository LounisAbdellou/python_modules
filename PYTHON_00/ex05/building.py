import sys


def error(message):
    print(f"{AssertionError.__name__}: {message}")
    sys.exit(1)


def check_text(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    space_count = sum(1 for char in text if char.isspace())
    digit_count = sum(1 for char in text if char.isdigit())

    punctuation_cnt = sum(
        1 for char in text if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    )

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_cnt} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    if len(sys.argv) > 2:
        error("more than one argument is provided")
    elif len(sys.argv) < 2:
        text = "No one hears a word they say !!!"
        print(text)
        check_text(text)
    else:
        check_text(sys.argv[1])


if __name__ == "__main__":
    main()
