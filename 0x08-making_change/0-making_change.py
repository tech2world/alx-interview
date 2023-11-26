#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (List[int]): List of coin values.
        total (int): The target amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Loop through each coin value
    for coin in coins:
        # Update the dp array for each possible amount
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), no combination of coins can make the total
    return dp[total] if dp[total] != float('inf') else -1
