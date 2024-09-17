n = 1
pentagonal_numbers = set()
while True:
    sn = n * (3 * n - 1) // 2
    for pi in pentagonal_numbers:
        pj = sn - pi
        if pj in pentagonal_numbers and abs(pi - pj) in pentagonal_numbers:
            print(abs(pi - pj))
            exit(0)
    pentagonal_numbers.add(sn)
    n += 1
