digit_to_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

tens_digit_to_word = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

tens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

def num_to_words(num):
    digits = [int(x) for x in reversed(str(num))]
    words = ""
    if num >= 1000:
        words += digit_to_word[digits[3]] + "thousand"
    if num >= 100 and digits[2] != 0:
        words += digit_to_word[digits[2]] + "hundred"
        if num % 100 > 0:
            words += "and"
    if num >= 20 and digits[1] >= 2:
        words += tens_digit_to_word[digits[1]]
    if num >= 10 and digits[1] == 1:
        words += tens[num % 100]
    elif digits[0] != 0:
        words += digit_to_word[digits[0]]
    return words

total = 0
for i in range(1, 1001):
    total += len(num_to_words(i))
print(total)
