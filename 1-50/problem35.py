primes = list()

for i in range(2, 1000000):
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

primes = set(primes)

def is_circular(p):
    s = str(p)
    while True:
        s = s[-1] + s[:-1]
        if s == str(p):
            return True
        if int(s) not in primes:
            return False

n = 0
for p in primes:
    if is_circular(p):
        n += 1

print(n)
