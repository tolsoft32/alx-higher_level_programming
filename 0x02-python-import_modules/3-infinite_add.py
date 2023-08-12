#!/usr/bin/python3

from sys import argv

def add_all_arg():
    argc = len(argv)
    j = 1
    sum = 0
    while j < argc:
        sum += int(argv[j])
        j += 1
    print("{:d}".format(sum))

if __name__ == "__main__":
    add_all_arg()
