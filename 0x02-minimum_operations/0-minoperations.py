#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0  

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')

        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    
    if dp[n] == float('inf'):
        return 0

    return dp[n]

n = 10
result = minOperations(n)
print(f"Minimum operations to achieve {n} H characters: {result}")
