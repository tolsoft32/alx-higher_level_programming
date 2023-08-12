#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    counta = len(sys.argv) - 1
    if counta == 0:
        print("0 arguments.")
    elif counta == 1:
        print("1 arguments.")
    else:
        print("{:d} arguments:".format(counta))
    for i in range(counta):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
