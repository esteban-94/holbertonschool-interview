#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning: Total file size
and number of lines by status code.
excecute: ./0-generator.py | ./0-stats.py
"""


import sys
import re

def print_metrics():
    """Method to print the statistics from the beginning"""
    patron_log = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+-\s+\[\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{6}\]\s+"GET\s+/projects/260\s+HTTP/1\.1"\s+\d{3}\s+\d+$'
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    i = 0
    counter = 0
    while True:
        entrada = sys.stdin.readline()
        if re.match(patron_log, entrada):
            current_status_code = int(entrada.split(" ")[7])
            if current_status_code in status_codes:
                status_codes[current_status_code] = status_codes[current_status_code] + 1
                file_size = entrada.split(" ")[8]
                counter = counter + int(file_size)
                i = i + 1
                if i == 10:
                    i = 0
                    print(f"File size: {counter}")
                    for key, value in status_codes.items():
                        if value != 0:
                            print(f"{key}: {value}")

print_metrics()
