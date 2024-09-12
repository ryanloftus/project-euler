s = 1
dim = 3
last_num = 1
while dim <= 1001:
    for i in range(4):
        last_num += dim-1
        s += last_num
    dim += 2
print(s)
