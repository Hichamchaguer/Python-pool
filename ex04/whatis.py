import sys

def check_number(x) -> int:
    if (x % 2 == 0):
        print("i'm even")
    else:
        print("i'm odd")

try:
    assert len(sys.argv) == 2, "invalid args"
    assert isinstance(int(sys.argv[1]), int), "must be integer"
    check_number(int(sys.argv[1]))
except (AssertionError, ValueError) as msg:   
    print(msg)
    sys.exit()

        