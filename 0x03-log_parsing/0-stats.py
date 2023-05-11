#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys
import re


def parsing():
    """
    return : none
    """
    lines = []
    ip_re = r"^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])"
    date_re = r"(\d+/\d+/\d+)"
    status_re = r"(200|301|400|401|403|404|405|500)"
    size_re = r"(\d+)$"
    i = 0
    size = 0
    status = [200, 301, 400, 401, 403, 404, 405, 500]
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
                if stat in status:
                    code[stat] += 1
            except Exception:
                pass

            if i % 10 == 0:
                print("File size: {}".format(size))
                for key, val in code.items():
                    print(f"{key}: {val}")
    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key, val in code.items():
            print(f"{key}: {val}")

if __name__ == '__main__':
    parsing()
