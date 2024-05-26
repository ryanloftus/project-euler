checked = {1: 1}

def find_collatz_length(num):
    if num in checked:
        length = checked[num]
    elif num % 2 == 0:
        length = 1 + find_collatz_length(num // 2)
        checked[num] = length
    else:
        length = 1 + find_collatz_length(3 * num + 1)
        checked[num] = length
    return length

max_len_start = 1
for i in range(2, 1000000):
    if find_collatz_length(i) > checked[max_len_start]:
        max_len_start = i

print(max_len_start)
