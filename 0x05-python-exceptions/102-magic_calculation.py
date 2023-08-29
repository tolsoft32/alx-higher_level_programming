#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    res = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Eception("Too far")

            res += a ** b / i
        except:
            res = b + a
            break
    return res
