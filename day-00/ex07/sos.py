import sys

NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", " ": "/",
}

def encode_morse(message):
    """Encode message into Morse code"""
    encoded_message = ""
    for char in message:
        if char in NESTED_MORSE:
            encoded_message += NESTED_MORSE[char]
    return encoded_message

def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        for char in sys.argv[1]:
            if not char.isspace() and not char.isalnum():
                raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    message = sys.argv[1].upper()
    print(encode_morse(message))



if __name__ == "__main__":
    main()