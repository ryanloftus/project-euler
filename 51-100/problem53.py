ONE_MILLION = 10 ** 6

fact = {0: 1}
for i in range(1, 101):
    fact[i] = fact[i-1] * i

over_mil = 0
for n in range(1, 101):
    for r in range(1, n):
        nCr = fact[n] / (fact[r] * fact[n-r])
        if nCr > ONE_MILLION:
            over_mil += 1
print(over_mil)
