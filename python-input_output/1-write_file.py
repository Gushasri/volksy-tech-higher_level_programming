#!/usr/bin/python3
'''ushasri'''


def write_file(filename="", text=""):
    '''ushasri'''
    with open(filename, encoding='utf-8')as file:
        ccount = 0
        line = file.readline()
        for line in f: 
            if not line:
                break
            ccount = ccount+len(line)
    return ccount
