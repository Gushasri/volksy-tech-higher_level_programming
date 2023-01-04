#!/usr/bin/python3
if __name__ ==" __main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add()))
    print("{:d} - {:d} = {:d}".format(a, b, sub()))
    print("{:d} * {:d} = {:d}".format(a, b, mul()))
    print("{:d} / {:d} = {:d}".format(a, b, div()))
