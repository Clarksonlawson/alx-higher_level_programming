#!/usr/bin/python3
"""
101-stats
"""

import sys

def print_stats(total_size, status_codes):
    """
    Print statistics based on total file size and status codes.

    :param total_size: Total file size.
    :type total_size: int
    :param status_codes: Dictionary containing status codes and their counts.
    :type status_codes: dict
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, status_codes):
    """
    Parse a log line and update total size and status codes count.

    :param line: Log line.
    :type line: str
    :param status_codes: Dictionary containing status codes and their counts.
    :type status_codes: dict
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]
        if status_code in ["200", "301", "400", "401", "403", "404", "405", "500"]:
            if status_code not in status_codes:
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1
        return size
    except Exception as e:
        return 0

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size += parse_line(line, status_codes)
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
