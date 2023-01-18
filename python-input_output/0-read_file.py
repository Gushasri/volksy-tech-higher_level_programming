#!/usr/bin/python3
'''ushahsdifiles reading'''


def read_file(filename=""):
    '''reading usha file'''
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
