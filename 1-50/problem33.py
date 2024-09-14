def is_special_fraction(numerator, denominator):
    if numerator % 10 == 0 or denominator % 10 == 0:
        return False
    sn = str(numerator)
    sd = str(denominator)
    if sn[0] not in sd and sn[1] not in sd:
        return False
    
    quotient = numerator / denominator
    if sn[0] == sd[0] and quotient == int(sn[1]) / int(sd[1]):
        return True
    if sn[0] == sd[1] and quotient == int(sn[1]) / int(sd[0]):
        return True
    if sn[1] == sd[0] and quotient == int(sn[0]) / int(sd[1]):
        return True
    if sn[1] == sd[1] and quotient == int(sn[0]) / int(sd[0]):
        return True
    return False

def reduce(n, d):
    i = 2
    while i <= n and i <= d:
        if n % i == 0 and d % i == 0:
            n //= i
            d //= i
        else:
            i += 1
    return n, d

special_fractions = []

for numerator in range(10, 100):
    for denominator in range(numerator+1, 100):
        if is_special_fraction(numerator, denominator):
            special_fractions.append((numerator, denominator))

print(special_fractions)

product_numerator = 1
product_denominator = 1
for n, d in special_fractions:
    product_numerator *= n
    product_denominator *= d

product_numerator, product_denominator = reduce(product_numerator, product_denominator)

print("{n} / {d}".format(n=product_numerator, d=product_denominator))
