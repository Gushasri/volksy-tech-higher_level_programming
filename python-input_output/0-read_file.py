#!/usr/bin/python3
'''ushahsdifiles reading'''


def read_file(filename=""):
    '''reading usha file'''
    with open("filename", "r") as file:
        print(file.read(), end=' ')
