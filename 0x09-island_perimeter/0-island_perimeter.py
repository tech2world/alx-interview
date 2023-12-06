#!/usr/bin/python3

def island_perimeter(grid):
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
