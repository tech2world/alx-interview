#!/usr/bin/python3

"""
Prime game
"""


def isPrime(num):
    """
    Check if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str or None: Name of the player that won the most rounds
        (Maria, Ben, or None if winner cannot be determined).
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n <= 1:
            # If there's no prime number, Ben wins
            ben_wins += 1
        else:
            # Check if Maria can pick a prime number
            prime = isPrime(n)
            if prime:
                maria_wins += 1
            else:
                # If there's no prime number left, Ben wins
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
