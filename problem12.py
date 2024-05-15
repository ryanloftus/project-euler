import math

def num_factors(num):
    f = 0
    for i in range(1, int(math.sqrt(num))):
        if num % i == 0:
            f += 1 if num // i == i else 2
    return f

triangle_num = 1
for i in range(2, 100000):
    triangle_num += i
    if num_factors(triangle_num) > 500:
        break
    i += 1

print(i, triangle_num)