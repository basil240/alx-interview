def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def simulate_game(n):
    primes = find_primes(n)
    # If the number itself is prime, the starting player wins
    if n in primes:
        return "Maria"
    # If the number is even, the starting player loses
    if n % 2 == 0:
        return "Ben"
    # Otherwise, the starting player wins
    return "Maria"

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test the function with the given example
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "Ben"