"""
8 * 9! is a 7-digit number => we only need to check numbers that are 1-7 digits
in fact, we only need to check up to 7 * 9!
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def is_sum_of_fact_digs(n):
    s = 0
    for d in str(n):
        s += factorial(int(d))
    return s == n

t = 0
upper_bound = 7 * factorial(9)
for i in range(3, upper_bound+1):
    if is_sum_of_fact_digs(i):
        t += i
print(t)
