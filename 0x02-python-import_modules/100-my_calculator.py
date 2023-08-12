#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    """
    Handles basic operation

    Perform basic operation like addition, subtraction
    multiplication and division between two numbers

    The program will executes an operation between two numbers
    selected by operator sent to the program
    """

    l_agv = len(argv) - 1

    if l_agv == 3:
        operators = argv[2]
        number_a = int(argv[1])
        number_b = int(argv[3])
        if operators == '+':
            res_out = add(number_a, number_b)
            print("{:d} + {:d} = {:d}".format(number_a, number_b, res_out))
            exit(0)
        elif operators == '-':
            res_out = sub(number_a, number_b)
            print("{:d} - {:d} = {:d}".format(number_a, number_b, res_out))
            exit(0)
        elif operators == '*':
            res_out = mul(number_a, number_b)
            print("{:d} * {:d} = {:d}".format(number_a, number_b, res_out))
            exit(0)
        elif operators == '/':
            res_out = div(number_a, number_b)
            print("{:d} / {:d} = {:d}".format(number_a, number_b, res_out))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <a> operators> <b>")
        exit(1)
