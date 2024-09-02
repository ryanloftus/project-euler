TARGET_FACTORIAL = 100

def add_to_digits(num, digits, exp):
    carry = 0
    num = reversed(str(num))
    for d in num:
        if exp >= len(digits):
            digits.append(0)
        n = digits[exp] + int(d) + carry
        digits[exp] = n % 10
        carry = n // 10
        exp += 1
    while carry != 0:
        if exp >= len(digits):
            digits.append(0)
        digits[exp] = (digits[exp] + carry) % 10
        carry = (digits[exp] + carry) // 10
        exp += 1

digits = [1]
for i in range(2, TARGET_FACTORIAL + 1):
    res = [0]
    for di in range(len(digits)):
        d = digits[di]
        add_to_digits(d * i, res, di)
    digits = res

digit_sum = sum(digits)
print(digit_sum)
