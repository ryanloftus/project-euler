"""
Permutation has one of each of:
0,1,2,3,4,5,6,7,8,9

How many permuations start with 0?
9! = 362,880 < 1 million

Similarly, 362,880 start with 1.

Since 2(362880) < 1 million and 3(362880) > 1 million,
The target permutation must start with 2.

We can apply this idea recursively to figure out all the digits:
"""

target_idx = 1000000 - 1

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

target_num = ""
digits = [0,1,2,3,4,5,6,7,8,9]
for pos in range(9, -1, -1):
    posf = factorial(pos)
    next_dig = digits[target_idx // posf]
    target_num += str(next_dig)
    digits.remove(next_dig)
    target_idx = target_idx % posf

print(target_num)
