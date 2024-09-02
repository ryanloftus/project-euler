from math import floor

def get_div_sum(n, memo):
    if n in memo:
        return memo[n]
    s = 0
    for i in range(1, floor(n/2) + 1):
        if n % i == 0:
            s += i
    memo[n] = s
    return s

def is_amicable(n, memo):
    sn = get_div_sum(n, memo)
    sm = get_div_sum(sn, memo)
    return sm == n and sn != n

memo = dict()

running_sum = 0
for i in range(1, 10000):
    if is_amicable(i, memo):
        running_sum += i
        print(i)
    

print(running_sum)
