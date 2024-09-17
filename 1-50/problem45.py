def triangle_num(i):
    return i * (i+1) // 2

def pentagon_num(i):
    return i * (3 * i - 1) // 2

def hexagon_num(i):
    return i * (2 * i - 1)

ti = 286
pi = 166
hi = 144

t = triangle_num(ti)
p = pentagon_num(pi)
h = hexagon_num(hi)
while True:
    if t == p and t == h:
        print(t)
        exit(0)
    while t < p:
        ti += 1
        t = triangle_num(ti)
    while p < h:
        pi += 1
        p = pentagon_num(pi)
    while h < t:
        hi += 1
        h = hexagon_num(hi)
