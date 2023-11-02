#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Unlock a list of boxes with a key same as the index of the box"""

    # Initially, we have the key to the first box (box 0).
    keys = [0]
    # A list to keep track of visited boxes.
    visited = [False] * len(boxes)
    # Mark the first box as visited.
    visited[0] = True
    # Start with the first box (box 0).
    current_box = 0

    # While there is a key to an unopened box
    while keys:
        if all(visited):
            # If all boxes have been visited, return True.
            return True
        # Get the current box from the keys list.
        current_box = keys.pop()

        # Get the keys in the current box.
        current_keys = boxes[current_box]

        for key in current_keys:
            if not visited[key]:
                # Mark the box as visited.
                visited[key] = True
                # Add the box's key to the keys list.
                keys.append(key)

    # If we run out of keys and haven't visited all boxes, return False.
    return all(visited)

# Test cases
# boxes1 = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes1))  # Should return True

# boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes2))  # Should return True

# boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes3))  # Should return False
# boxes_random = [
#     [7, 5],
#     [1, 10, 7],
#     [9, 6, 10],
#     [7, 9],
#     [2],
#     [7, 3],
#     [7, 9, 10, 10, 8, 9, 2, 5],
#     [7, 2, 2, 4, 4, 2, 4, 8, 7],
#     [4, 2, 9, 6, 6, 5, 5],
# ]
# print(canUnlockAll(boxes_random))  # Expected: False (result may vary depending on specific arrangement)

# boxes_complex = [
#     [10, 3, 8, 9, 6, 5, 8, 1],
#     [8, 5, 3, 7, 1, 8, 6],
#     [5, 1, 9, 1],
#     [],
#     [6, 6, 9, 4, 3, 2, 3, 8, 5],
#     [9, 4],
#     [4, 2, 5, 1, 1, 6, 4, 5, 6],
#     [9, 5, 8, 8],
#     [6, 2, 8, 6]
# ]
# print(canUnlockAll(boxes_complex))  # Expected: True

boxes_1000 = [[] for _ in range(1000)]  # Create 1000 empty boxes
print(canUnlockAll(boxes_1000))  # Expected: True
