primes = set()

"""
We just store the primes of the first 100,000 numbers because we can assume that
n <= 80, a <= 1000, b <= 1000, so:
n**2 + a*n + b < 87,400
"""

print("finding primes")
for i in range(2, 100000):
    p = True
    for d in range(2, i//2):
        if i % d == 0:
            p = False
            break
    if p:
        primes.add(i)
print("done finding primes")

def is_prime(k):
    return k in primes

b_candidates = []
for b in range(-1000, 1001):
    if is_prime(abs(b)):
        b_candidates.append(b)

best_a = 1
best_b = 41
max_primes = 40
for a in range(-999, 1000):
    for b in b_candidates:
        n = 1
        while True:
            if not is_prime(n**2 + a*n + b):
                break
            n += 1
        if n > max_primes:
            max_primes = n
            best_a = a
            best_b = b

print(best_a, best_b, max_primes)
print(best_a * best_b)
