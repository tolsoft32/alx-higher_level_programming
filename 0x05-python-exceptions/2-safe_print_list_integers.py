#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    prints = 0

    for i  in range(x):
        try:
            if type(my_list[i]) is int and prints != x:
                print('{:d}'.format(my_list[i]), end='')
                prints += 1
        except TypeError:
            continue
        print()

        return (prints)
