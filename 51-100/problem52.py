from collections import Counter

def is_special(n):
    if len(str(n)) < len(str(6*n)):
        return False
    counters = []
    for i in range(1, 7):
        counters.append(Counter(str(i * n)))
    for k in counters[0]:
        for c in counters:
            if c[k] != counters[0][k]:
                return False
    return True

i = 1
while not is_special(i):
    i += 1

print(i)
