sum_last_10 = 0
last_10_modulus = 10 ** 10
for i in range(1, 1001):
    sum_last_10 += (i ** i) % last_10_modulus
print(sum_last_10 % last_10_modulus)
