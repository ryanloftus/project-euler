longest = 0
dmax = 0

def repeat_length(d):
    l = 1
    while True:
        s = str(10**(10+l*4) // d)
        p1 = l + 2
        p2 = 2 * l + 2
        p3 = 3 * l + 2
        p4 = 4 * l + 2
        if s[p1:p2] == s[p2:p3] and s[p2:p3] == s[p3:p4]:
            return l
        else:
            l += 1

for d in range(2, 1000):
    dlen = repeat_length(d)
    if dlen > longest:
        dmax = d
        longest = dlen

print(dmax)
