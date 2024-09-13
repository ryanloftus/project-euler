five_pows = []
for i in range(10):
    five_pows.append(i ** 5)

def digit_five_pow_sum(n):
    s = 0
    while n > 0:
        s += five_pows[n % 10]
        n //= 10
    return s

t = 0
for i in range(2, 500000):
    if i == digit_five_pow_sum(i):
        t += i
print(t)
