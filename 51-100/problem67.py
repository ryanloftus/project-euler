def max_path(rows):
    dp = [[0 for _ in rows[i]] for i in range(len(rows))]
    for c in range(len(rows[-1])):
        dp[-1][c] = rows[-1][c]
    for r in range(len(rows) - 2, -1, -1):
        for c in range(len(rows[r])):
            dp[r][c] = max(dp[r+1][c], dp[r+1][c+1]) + rows[r][c]
    return dp[0][0]

with open("51-100/input/0067.txt") as f:
    rows = [[int(x) for x in l.split(" ")] for l in f.readlines()]
    print(max_path(rows))
