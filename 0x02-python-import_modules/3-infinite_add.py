#!/usr/bin/python3

import sys

if __name__ == "__main__":
    agv = sys.argv
    l_agv = len(agv)
    sum = 0

    if l_agv > 1:
        for i in range(1, l_agv):
            sum += int(agv[i])

        print(sum)
