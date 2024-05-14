prevprev = 1
prev = 2
even_sum = 2
END = 4000000
while prev + prevprev <= END:
    next_term = prev + prevprev
    if next_term % 2 == 0:
        even_sum += next_term
    prevprev = prev
    prev = next_term
print(even_sum)
