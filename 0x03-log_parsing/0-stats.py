#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
 <status code> <file size>
(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size> where <total size>
is the sum of all previous <file size>

Number of lines by status code:
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
If a status code doesnt appear or is not an integer,
do not print anything for this status code.
Format: <status code>: <number>
Status codes should be printed in ascending order.
"""

import sys


def compute_metrics():
    """
    Compute metrics from input log data.

    This function reads input log data from the standard input line by line,
    computes the total file size and the count of different status codes,
    and prints the corresponding statistics.

    Args:
        None

    Returns:
        None
    """

    total_size = 0
    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    lines_processed = 0

    try:
        for line in sys.stdin:
            lines_processed += 1

            if lines_processed % 10 == 0:
                print(f"Total file size: {total_size}")

                for code in sorted(status_counts.keys()):
                    if status_counts[code] != 0:
                        print(f"{code}: {status_counts[code]}")

            data = line.split()
            if len(data) >= 9 and data[8].isdigit():
                size = int(data[8])
                total_size += size

                code = int(data[8])
                if code in status_counts:
                    status_counts[code] += 1
    except KeyboardInterrupt:
        pass
    

    print(f"Total file size: {total_size}")

    for code in sorted(status_counts.keys()):
        if status_counts[code] != 0:
            print(f"{code}: {status_counts[code]}")


if __name__ == "__main__":
    compute_metrics()
