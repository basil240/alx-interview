def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def isWinner(x, nums):
    winner_count = {"Maria": 0, "Ben": 0}
    
    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        
        prime_count = len(primes)
        
        if prime_count % 2 == 1:
            winner_count["Maria"] += 1
        else:
            winner_count["Ben"] += 1
    
    max_wins = max(winner_count.values())
    if max_wins == 0:
        return None
    else:
        return max(winner_count, key=winner_count.get)


x = 3
nums = [10, 15, 20]
print(isWinner(x, nums))  