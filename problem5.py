import numpy as np

factors = np.arange(start=1, stop=21, step=1)
prime_factors = {
    2: 1,
    3: 1,
    5: 1,
    7: 1,
    11: 1,
    13: 1,
    17: 1,
    19: 1,
}

for factor in factors:
    for k in prime_factors:
        power = 1
        while factor % (k ** power) == 0:
            prime_factors[k] = max(prime_factors[k], power)
            power += 1

prod = 1
for k in prime_factors:
    prod *= k ** prime_factors[k]
print(prod)
