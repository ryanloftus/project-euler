"""
to be a pandigital product, the product, multiplicand, and multiplier must have a total num of digits adding to 9

99 * 99 = 9801
=> no product of two 2-digit numbers will work because they will never get enough digits in the product

100 * 100 = 10000
=> no product of two 3-digit numbers will work because they will always have too many digits in the product

9 * 999 = 8991
=> no product of a 1-digit number and (1,2,or 3)-digit number will work because there won't be enough digits

So, we either have a 1-digit number multiplied by a 4-digit number or a 2-digit multiplied by a 3-digit number
"""


def is_pandigital(a, b):
    prod = a * b
    s = str(prod) + str(a) + str(b)
    if len(s) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in s:
            return False
    return True
    

pandigital_products = set()

for i in range(1, 10):
    for j in range(1000, 10000):
        if is_pandigital(i, j):
            pandigital_products.add(i*j)

for i in range(10, 100):
    for j in range(100, 1000):
        if is_pandigital(i, j):
            pandigital_products.add(i*j)

print(sum(pandigital_products))
