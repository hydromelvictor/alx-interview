#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys
import re

def printer(size, code):
    """
    printer function
    """
    print("File size: {}".format(size))
    for key, val in sorted(code.items()):
        if val:
            print(f"{key}: {val}")


def parsing():
    """
    return : none
    """
    size = 0
    i = 0
    status = ["200", "301", "400", "401", "403", "404", "405", "500"]
    code = {i: 0 for i in status}
    try:
        for url in sys.stdin:
            line = url.split()
            i += 1

            try:
                size += int(line[-1])
            except Exception:
                pass

            try:
                stat = line[-2]
                if stat in code:
                    code[stat] += 1
            except Exception:
                pass

            if i % 10 == 0:
                printer(size, code)
        printer(size, code)
    except KeyboardInterrupt:
        printer(size, code)


if __name__ == '__main__':
    parsing()
