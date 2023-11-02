#!/usr/bin/python3
"""
Usage: nqueens N
If the user called the program with the wrong number of arguments
print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a specific position on the board.

    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nqueens(board, col, n, solutions):
    """
    Solve the N Queens problem using backtracking.

    """
    if col == n:
        result = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    result.append([i, j])
        solutions.append(result)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = nqueens(board, col + 1, n, solutions) or res
            board[i][col] = 0

    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for j in range(n)] for i in range(n)]
    solutions = []
    nqueens(board, 0, n, solutions)

    for solution in solutions:
        print(solution)
