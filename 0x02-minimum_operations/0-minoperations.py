#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to  result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => \
    HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """returns the min num to reach n"""

    # Initializing the array to store minimum operations
    min_operations_array = [0] * (n + 1)

    for i in range(2, n + 1):
        min_operations_array[i] = i  # Option 1: Copy all

        for j in range(2, i):
            if i % j == 0:
                # Option 2: Copy 'j' characters and paste 'i/j' times
                min_operations_array[i] = min(
                    min_operations_array[i], min_operations_array[j] + i // j)

    return min_operations_array[n]
