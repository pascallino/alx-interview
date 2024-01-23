#!/usr/bin/python3
""" Write a script that reads stdin line by line and computes metrics: """
import sys
import re

# Initialize hashtable
hashtable = {
             200: 0, 301: 0, 400: 0,
             401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
counter = 0
file = 0

try:
    # Iterate through each line and extract status code and file size
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = int(line_list[-2])
            file_size = int(line_list[-1])

            # Increment status code count
            if status_code in hashtable:
                hashtable[status_code] += 1
            else:
                hashtable[status_code] = 1

            # Accumulate total file size
            file += file_size
            counter += 1

            # Check if it's time to print statistics
            if counter == 10:
                print('File size: {}'.format(file))
                for key, value in sorted(hashtable.items()):
                    if value > 0:
                        print('{}: {}'.format(key, value))

                # Reset counters and hashtable for the next 10 lines
                counter = 0

except KeyboardInterrupt:
    # Handle Ctrl+C interruption, print current statistics, and exit
    print('File size: {}'.format(file))
    for key, value in sorted(hashtable.items()):
        if value > 0:
            print('{}: {}'.format(key, value))

    sys.exit(0)
