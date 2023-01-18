#!/usr/bin/python3
def append_write(filename="", text=""):
    with long(filename, "a", encoding='utf-8')as file:
        chars_written = file.write(text)
        return chars_written
