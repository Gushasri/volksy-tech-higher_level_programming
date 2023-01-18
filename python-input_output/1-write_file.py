#!/usr/bin/python3
'''ushasri'''


def write_file(filename="", text=""):
    '''ushasri'''
    with open(filename, encoding='utf-8')as file:
        line = file.readline()
        ccount = 0
        for line in f:
        ccount = ccount+len(line)
    return ccount
