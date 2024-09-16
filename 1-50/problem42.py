"""
Using:
```
ml = 0
for word in input:
    ml = max(len(word), ml)
print(ml)
```
We determine that the longest word is 14 characters.
The largest char value is 26.
So, the word values are upperbounded by 26*14=364.
"""

triangle_numbers = set()
i = 1
while True:
    tri_num = i * (i+1) // 2
    triangle_numbers.add(tri_num)
    if tri_num > 364:
        break
    i += 1

def is_triangle_word(word):
    s = 0
    for c in word:
        s += (ord(c) - ord("A")) + 1
    return s in triangle_numbers

with open("./1-50/input/0042.txt") as f:
    input = f.read()

input = [word.strip("\"") for word in input.split(",")]

triangle_words = 0
for word in input:
    if is_triangle_word(word):
        triangle_words += 1
print(triangle_words)
