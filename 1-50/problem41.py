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

def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def set_of_first_n_digits(n):
    s = set()
    for i in range(1, n+1):
        s.add(str(i))
    return s

for i in range(9, 3, -1):
    s = set_of_first_n_digits(i)
    candidates = [int(c) for c in get_pandigital_candidates(s)]
    candidates.sort(reverse=True)
    for c in candidates:
        if is_prime(c):
            print(c)
            exit(0)
