#!/usr/bin/python3
""" Write a script that reads stdin line by line and computes metrics: """
import sys
import re

# Initialize hashtable
hashtable = {"file_size": 0, "counter": 0,
             200: 0, 301: 0, 400: 0,
             401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    # Iterate through each line and extract status code and file size
    for line in sys.stdin:
        match = re.match(r'.* ".*" (\d+) (\d+)', line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Increment status code count
            if status_code in hashtable:
                hashtable[status_code] += 1
            else:
                hashtable[status_code] = 1

            # Accumulate total file size
            hashtable["file_size"] += file_size
            hashtable['counter'] += 1

            # Check if it's time to print statistics
            if hashtable['counter'] == 10:
                print('File size: {}'.format(hashtable["file_size"]))
                for s in [200, 301, 400, 401, 403, 404, 405, 500]:
                    if s in hashtable and hashtable[s] > 0:
                        print('{}: {}'.format(s, hashtable[s]))

                # Reset counters and hashtable for the next 10 lines
                hashtable['counter'] = 0

except KeyboardInterrupt:
    # Handle Ctrl+C interruption, print current statistics, and exit
    print('File size: {}'.format(hashtable["file_size"]))
    for status in [200, 301, 400, 401, 403, 404, 405, 500]:
        if status in hashtable and hashtable[status] > 0:
            print('{}: {}'.format(status, hashtable[status]))

    sys.exit(0)
