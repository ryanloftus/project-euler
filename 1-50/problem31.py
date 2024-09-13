coins = [1, 2, 5, 10, 20, 50, 100, 200]

def ways_to_calc_using_first_n_coins(target, n):
    if n == 1:
        return 1 if target >= 0 else 0
    c = coins[n-1]
    ways_to_calc = 0
    nc = 0
    while target - c * nc >= 0:
        ways_to_calc += ways_to_calc_using_first_n_coins(target - c * nc, n-1)
        nc += 1
    return ways_to_calc

print(ways_to_calc_using_first_n_coins(200, len(coins)))
