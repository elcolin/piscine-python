import sys
import string

def ispunctuationmark(char):
    return char in string.punctuation

def analyzetext(user_input):
    print("The text contains", len(user_input), "characters")
    print(sum(1 for char in user_input if char.isupper()), "upper letters")
    print(sum(1 for char in user_input if char.islower()), "lower letters")
    print(sum(1 for char in user_input if ispunctuationmark(char)), "punctuation marks")
    print(sum(1 for char in user_input if char.isspace()), "spaces")
    print(sum(1 for char in user_input if char.isdigit()), "digits")

def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument provided"
    except AssertionError as e:
        print("Assertion Error:", e)
        return

    if len(sys.argv) != 2 or not sys.argv[1]:
        try:
            user_input = sys.stdin.readline()
        except EOFError:
            pass
    else:
        user_input = sys.argv[1]
    analyzetext(user_input)


if __name__ == "__main__":
    main()

