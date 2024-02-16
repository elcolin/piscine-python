import sys
try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    try:
        input_integer = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument should be an integer")

    if input_integer % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except AssertionError as e:
    print("AssertionError:", e)