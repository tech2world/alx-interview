#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing 1 byte of data each
    :return: True if data is a valid UTF-8 encoding,else return False
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the first byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # If no UTF-8 character is under processing
        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

        # 1-byte characters or characters with more than 4 bytes are not valid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte starts with the right bit pattern (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
        # Decrement the count for the bytes left in the current character
        num_bytes -= 1

    # True if all characters have been properly processed
    return num_bytes == 0
