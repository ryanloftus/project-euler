def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def to_bin_str(n):
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

s = 0
# no leading 0's implies palindromic bin str starts and ends w/ 1, so it must be odd
for i in range(1, 1000000, 2):
    if is_palindrome(str(i)) and is_palindrome(to_bin_str(i)):
        s += i

print(s)
