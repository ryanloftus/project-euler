def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def is_lychrel(n):
    for _ in range(50):
        r = int("".join(reversed(str(n))))
        next_n = r + n
        if is_palindrome(str(next_n)):
            return False
        n = next_n
    return True

num_lychrels = 0
for n in range(10000):
    if is_lychrel(n):
        num_lychrels += 1
print(num_lychrels)