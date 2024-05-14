def is_num_palindrome(num: int) -> bool:
    s = str(num)
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

max_prod = 0
for n1 in range(100, 1000):
    for n2 in range(n1, 1000):
        prod = n1 * n2
        if is_num_palindrome(prod):
            max_prod = max(max_prod, prod)

print(max_prod)
