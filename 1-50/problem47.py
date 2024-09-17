primes = set()
primes.add(2)

def num_prime_factors(n):
    pfactors = 0
    for p in primes:
        if n % p == 0:
            pfactors += 1
    return pfactors

consec = 0
n = 3
while True:
    pfactors = num_prime_factors(n)
    if pfactors == 4:
        consec += 1
        if consec == 4:
            print(n - 3)
            exit(0)
    else:
        consec = 0
    if pfactors == 0:
        primes.add(n)
    n += 1