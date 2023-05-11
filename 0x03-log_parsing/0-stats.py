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
    format = ip_re + ' - ' + '[' + date_re + ']' + "GET /projects/260 HTTP/1.1" + ' ' + status_re + ' ' + size_re
    i = 0
    size = 0
    status = [200, 301, 400, 401, 403, 404, 405, 500]
    code = {i: 0 for i in status}

    with open(sys.stdin) as file:
        line = file.readline()
        i += 1

        if re.search(format, line) != line:
            continue

        size += int(line[-1])
        if line[-2] in status:
            code[line[-2]] += 1

        if i % 10 == 0:
            print("File size: {}".format(size))
            for key, val in code.items():
                print(f"{key}: {val}")
