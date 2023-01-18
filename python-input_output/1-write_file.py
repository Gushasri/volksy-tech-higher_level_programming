#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, encoding='utf-8')as file:
        ccount = 0
        for line in f:
        ccount = ccount+len(line)
    return ccount
        
