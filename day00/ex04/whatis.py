import sys

def check_number(x) -> int:
    if (x % 2 == 0):
        print("i'm even")
    else:
        print("i'm odd")

try:
    assert len(sys.argv) == 2, "invalid args"
    check_number(int(sys.argv[1]))
except ValueError as msg:
    print("must be integer")
    sys.exit()
except AssertionError as msg:
    print(msg)
    sys.exit()

        