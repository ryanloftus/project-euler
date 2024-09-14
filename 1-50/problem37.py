primes_list = [2,3,5,7]
primes_set = set(primes_list)

def is_prime(i):
    if i == 1:
        return False
    for p in primes_list:
        if i % p == 0:
            return False
        elif p >= i // 2:
            return True
    return True

def is_truncatable(p):
    n = p // 10
    while n > 0:
        if n not in primes_set:
            return False
        n //= 10
    s = str(p)[1:]
    while len(s) > 0:
        if int(s) not in primes_set:
            return False
        s = s[1:]
    return True

truncatable = []
i = 11
while len(truncatable) < 11:
    if is_prime(i):
        primes_list.append(i)
        primes_set.add(i)
        if is_truncatable(i):
            truncatable.append(i)
            print(i)
    i += 1

print("Answer:", sum(truncatable))
