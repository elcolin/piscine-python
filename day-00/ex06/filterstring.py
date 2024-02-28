import ft_filter
import sys


def main():
    try:
        assert len(sys.argv) == 3 and sys.argv[2].isdigit(), "the arguments are bad"
        for char in sys.argv[1]:
            if not char.isspace() and not char.isalpha():
                raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    parsed_input = sys.argv[1].split()
    islonger = lambda input: len(input) > int(sys.argv[2])
    print(list(ft_filter.ft_filter(islonger, parsed_input)))



if __name__ == "__main__":
    main()