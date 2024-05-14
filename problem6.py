"""
1^2 + 2^2 + ... + 100^2
(1 + 2 + ... + 100)^2 = (101 * 50)^2 = 25502500
"""

def calc_sum_of_squares():
    s = 0
    step = 1
    last = 0
    for i in range(1, 101):
        last += step
        s += last
        step += 2
    return s

def calc_square_of_sum():
    return (101 * 50) ** 2

sum_of_squares = calc_sum_of_squares()
square_of_sum = calc_square_of_sum()
print(square_of_sum - sum_of_squares)