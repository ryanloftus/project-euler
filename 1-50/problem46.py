import math

primes = set()
primes.add(2)

def is_prime(n):
    for d in primes:
        if n % d == 0:
            return False
    return True

def is_counter_example(n):
    s = 1
    i = 1
    bound = n//2
    while s <= bound:
        if n - 2 * s in primes:
            return False
        i += 2
        s += i
    return True

n = 3
while True:
    if is_prime(n):
        primes.add(n)
    elif is_counter_example(n):
        print(n)
        exit(0)
    n += 2
