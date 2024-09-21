import math

MAX_PRIME = 10 ** 7
TARGET = 8

primes = [2]
for i in range(3, MAX_PRIME, 2):
    is_prime = True
    cuttoff = int(math.floor(math.sqrt(i)))
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
        elif p > cuttoff:
            break
    if is_prime:
        primes.append(i)

primes_set = set(primes)

def is_solution(n):
    s = str(n)
    for k in s:
        num_primes = 0
        min_p = n
        for i in range(10):
            si = s.replace(k, str(i))
            if si[0] == "0":
                continue
            sc = int(si)
            if sc in primes_set:
                num_primes += 1
                min_p = min(min_p, sc)
        if num_primes == TARGET:
            print(min_p)
            return True
    return False

for p in primes:
    if p < 50000:
        continue
    elif is_solution(p):
        exit(0)
