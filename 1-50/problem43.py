def get_pandigital_candidates(digits: set):
    if len(digits) == 1:
        return [list(digits)[0]]
    res = []
    for d in digits:
        rdigits = digits.difference([d])
        dres = get_pandigital_candidates(rdigits)
        for s in dres:
            s += d
            res.append(s)
    return res

primes = [2,3,5,7,11,13,17]

def is_special(sn):
    for i in range(len(primes)):
        if int(sn[i+1:i+4]) % primes[i] != 0:
            return False
    return True

candidates = get_pandigital_candidates({"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"})

s = 0
for c in candidates:
    if is_special(c):
        s += int(c)
print(s)
