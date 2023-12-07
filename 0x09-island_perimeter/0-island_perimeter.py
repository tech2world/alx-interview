#!/usr/bin/python3
"""
Module: island_perimeter
Description: Provides a function to calculate the perimeter
of an island in  2D grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A 2D grid representing an island.

    Returns:
        int: The perimeter of the island.

    Example:
        grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        island_perimeter(grid)  # Output: 12
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Calculate the contribution of the current land cell
                perimeter += 4

                # Check adjacent cells and subtract their contribution
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
