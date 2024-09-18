primes = set()
for n in range(2, 10000):
    is_prime = True
    for p in primes:
        if n % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.add(n)

def dig_count_dict():
    res = dict()
    for i in range(10):
        res[str(i)] = 0
    return res

def are_perms(n1, n2, n3):
    n1_count = dig_count_dict()
    n2_count = dig_count_dict()
    n3_count = dig_count_dict()
    for d in str(n1):
        n1_count[d] += 1
    for d in str(n2):
        n2_count[d] += 1
    for d in str(n3):
        n3_count[d] += 1
    for i in range(10):
        si = str(i)
        if n1_count[si] != n2_count[si] or n1_count[si] != n3_count[si]:
            return False
    return True

for s1 in primes:
    for diff in range(1, (10000 - s1) // 2):
        s2 = s1 + diff
        s3 = s2 + diff
        if s2 in primes and s3 in primes and are_perms(s1, s2, s3):
            print(s1, s2, s3)
        