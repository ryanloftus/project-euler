def is_pandigital_concatenated_product(sn):
    n = int(sn)
    for l in range(1, len(sn)//2 + 1):
        d = int(sn[:l])
        if n % d == 0:
            s = str(d)
            i = 2
            while len(s) < len(sn) and s == sn[:len(s)]:
                s += str(d * i)
                i += 1
                if s == sn:
                    return True
    return False


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


candidates = get_pandigital_candidates({"1","2","3","4","5","6","7","8","9"})
print(len(candidates), "candidates found.")
max_pandigital_concatenated_product = 0
for c in candidates:
    if is_pandigital_concatenated_product(c):
        max_pandigital_concatenated_product = max(max_pandigital_concatenated_product, int(c))

print(max_pandigital_concatenated_product)