known_primes = []

def is_prime(num: int) -> bool:
    for p in known_primes:
        if num % p == 0:
            return False
        elif p * p > num:
            break
    return True

s = 0
for i in range(2, 2000000):
    if is_prime(i):
        s += i
        known_primes.append(i)
print(s)