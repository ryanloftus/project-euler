UPPER_LIMIT = 28123


def is_abundant(n):
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum > n


abundant_numbers = set()

for i in range(1, UPPER_LIMIT + 1):
    if is_abundant(i):
        abundant_numbers.add(i)

running_sum = 0
for n in range(1, UPPER_LIMIT + 1):
    can_write_as_sum_of_two_abundant = False
    for m in abundant_numbers:
        if (n - m) in abundant_numbers:
            can_write_as_sum_of_two_abundant = True
            break
    if not can_write_as_sum_of_two_abundant:
        running_sum += n

print(running_sum)
