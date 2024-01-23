#!/usr/bin/python3
""" Write a script that reads stdin line by line and computes metrics: """
import sys
import re

# Initialize hashtable
hashtable = {
             '200': 0, '301': 0, '400': 0,
             '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
counter = 0
total_size = 0

try:
    # Iterate through each line and extract status code and file size
    input_lines = sys.stdin.readlines()
    for line in input_lines:
        match = re.match(r'.* ".*" (\d+) (\d+)', line)

        if match:
            status_code = str(match.group(1))
            file_size = int(match.group(2))

            # Increment status code count
            if status_code in hashtable.keys():
                hashtable[status_code] += 1

            # Accumulate total file size
            total_size += file_size
            counter += 1

            # Check if it's time to print statistics
            if counter == 10:
                counter = 0
                print('File size: {}'.format(total_size))
                for key, value in sorted(hashtable.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))

                # Reset counters and hashtable for the next 10 lines

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(hashtable.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
