from collections import defaultdict

perfect_squares = dict()
for i in range(1000):
    perfect_squares[i**2] = i

p_map = defaultdict(int)
for a in range(1, 334):
    for b in range(a, 500):
        c2 = a**2 + b**2
        if c2 in perfect_squares:
            p = a + b + perfect_squares[c2]
            p_map[p] += 1

maximal_p = 0
max_solutions = 0
for p, n in p_map.items():
    if n > max_solutions:
        max_solutions = n
        maximal_p = p
print(maximal_p)
