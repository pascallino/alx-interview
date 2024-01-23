#!/usr/bin/python3
""" Write a script that reads stdin line by line and computes metrics: """
import sys
import re

if __name__ == "__main__":
    # Initialize hashtable
    hashtable = {"file_size": 0, "counter": 0, "status_counts": {}}

    try:
        # Iterate through each line and extract status code and file size
        for line in sys.stdin:
            match = re.match(r'.* ".*" (\d+) (\d+)', line)
            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                # Increment status code count
                if status_code in hashtable["status_counts"]:
                    hashtable["status_counts"][status_code] += 1
                else:
                    hashtable["status_counts"][status_code] = 1

                # Accumulate total file size
                hashtable["file_size"] += file_size
                hashtable['counter'] += 1

                # Check if it's time to print statistics
                if hashtable['counter'] == 10:
                    print(f'File size: {hashtable["file_size"]}')
                    for status in [200, 301, 400, 401, 403, 404, 405, 500]:
                        if status in hashtable["status_counts"] and\
                           hashtable["status_counts"][status] > 0:
                            print(\
                                f'{status}: {hashtable["status_counts"][status]}')

                    # Reset counters and hashtable for the next 10 lines
                    hashtable['counter'] = 0

    except KeyboardInterrupt:
        # Handle Ctrl+C interruption, print current statistics, and exit
        print(f'File size: {hashtable["file_size"]}')
        for status in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status in hashtable["status_counts"] and\
               hashtable["status_counts"][status] > 0:
                print(f'{status}: {hashtable["status_counts"][status]}')

        sys.exit(0)
