UPPER_BOUND = 10 ** 6

ordered_primes = list()
for n in range(2, UPPER_BOUND):
    is_prime = True
    for p in ordered_primes:
        if n % p == 0:
            is_prime = False
            break
    if is_prime:
        ordered_primes.append(n)

primes = set(ordered_primes)

longest = 0
best_p = 0
for i in range(len(ordered_primes)):
    if i + longest >= len(ordered_primes):
        break
    l = longest
    s = 0
    for j in range(i, i + l):
        s += ordered_primes[j]
    while s < UPPER_BOUND and i+l < len(ordered_primes):
        s += ordered_primes[i+l]
        l += 1
        if s in primes:
            longest = l
            best_p = s
print(best_p, longest)