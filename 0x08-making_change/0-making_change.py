#!/usr/bin/python3
""" making change using dynamic approach """


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the fewest number of
    # coins for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    # Iterate through each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            # Update dp[i] with the fewest number
            # of coins needed to make total i
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
