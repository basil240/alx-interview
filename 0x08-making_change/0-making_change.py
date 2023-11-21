#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each total from 0 to the given total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)
