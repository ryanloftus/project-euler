NUM = 600851475143

factor = 2
largest_prime_factor = 1
while NUM > 1:
    while NUM % factor == 0:
        NUM //= factor
        largest_prime_factor = factor
    factor += 1
    if factor * factor > NUM:
        largest_prime_factor = max(NUM, largest_prime_factor)
        break
print(largest_prime_factor)
