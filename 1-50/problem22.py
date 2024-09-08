with open("1-50/input/0022.txt") as f:
    input = f.read()

names = [name.strip("\"") for name in input.split(",")]
names.sort()

total_score = 0
for i in range(len(names)):
    pos_score = i + 1
    name_score = sum(map(lambda c: ord(c) - ord("A") + 1, names[i]))
    total_score += pos_score * name_score

print(total_score)
