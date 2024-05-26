"""
Must move right 20 units and down 20 units.
Can represent as a string of d's and r's (binary string).
Ordering 40 characters, with 2 kinds each repeated 20 times:
    40! / (20! * 20!) = (40 * 39 * 38 * ... * 21) / (20 * 19 * 18 * ... * 1)
"""

answer = 1
for i in range(21, 41):
    answer *= i

for i in range(1, 21):
    answer //= i

print(answer)
