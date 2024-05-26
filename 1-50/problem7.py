TARGET = 10001
known_primes = []

def is_prime(num: int) -> bool:
    for p in known_primes:
        if num % p == 0:
            return False
    return True

cur = 2
while True:
    if is_prime(cur):
        known_primes.append(cur)
        if len(known_primes) == TARGET:
            break
    cur += 1

print(known_primes[-1])
