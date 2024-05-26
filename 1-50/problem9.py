TARGET = 1000

for a in range(1, TARGET):
    for b in range(a+1, TARGET):
        c = TARGET - a - b
        if c ** 2 == a ** 2 + b ** 2:
            print(a*b*c)
            exit(0)
