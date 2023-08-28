#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    x_to = 0

    try:
        for i in my_list:
            if x_to < x:
                print("{}".format(my_list[x_to]), end="")
                x_to += 1
    except IndexError:
        pass
    finally:
        return (x_to)
