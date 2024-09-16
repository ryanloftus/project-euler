upper_bound = 10 ** 6

prod = 1    # the final answer
i = 1       # next number in sequence
n = 1       # index of digit
target = 1  # the next power of 10

while n <= upper_bound:
    si = str(i)
    if target < n + len(si):
        prod *= int(si[target-n])
        target *= 10
    n += len(si)
    i += 1

print(prod)
