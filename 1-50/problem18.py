def max_path(rows, r, c, current_sum):
    return max(max_path(rows, r + 1, c, current_sum + rows[r][c]), max_path(rows, r + 1, c + 1, current_sum + rows[r][c])) if r < len(rows) else current_sum

with open("1-50/input/0018_triangle.txt") as f:
    rows = [[int(x) for x in l.split(" ")] for l in f.readlines()]
    print(max_path(rows, 0, 0, 0))
