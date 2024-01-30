#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0

    # Initialize an array to store the minimum operations needed for each value from 1 to n
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    # Iterate from 2 to n to calculate minimum operations for each value
    for i in range(2, n + 1):
        # Check all possible factors of i
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n] if dp[n] != float('inf') else 0

# Example usage:
n = 9
result = minOperations(n)
print("Number of operations:", result)