fprev = 1
fprevprev = 1
idx = 3
while True:
    next = fprev + fprevprev
    if len(str(next)) == 1000:
        print(idx)
        break
    fprevprev = fprev
    fprev = next
    idx += 1

