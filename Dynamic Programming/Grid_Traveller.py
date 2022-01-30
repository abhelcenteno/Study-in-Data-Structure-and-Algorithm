def grid_traveller_1(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1 and y == 1:
        return 0
    elif x == 1 or y == 1:
        return 1
    else:
        return grid_traveller_1(x-1, y) + grid_traveller_1(x, y-1)


def grid_traveller_2(x, y, memo={}):
    if (x, y) in memo:
        return memo[(x, y)]
    elif x == 0 or y == 0:
        memo[(x, y)] = 0
        memo[(y, x)] = 0
        return memo[(x, y)]
    elif x == 1 and y == 1:
        memo[(x, y)] = 0
        return memo[(x, y)]
    elif x == 1 or y == 1:
        memo[(x, y)] = 1
        memo[(y, x)] = 1
        return memo[(x, y)]
    else:
        memo[(x, y)] = grid_traveller_2(x-1, y, memo) + grid_traveller_2(x, y-1, memo)
        memo[(y, x)] = memo[(x, y)]
        return memo[(x, y)]


print(grid_traveller_1(0, 0))
print(grid_traveller_1(1, 0))
print(grid_traveller_1(0, 1))
print(grid_traveller_1(1, 1))
print(grid_traveller_1(1, 2))
print(grid_traveller_1(2, 1))
print(grid_traveller_1(2, 2))
print(grid_traveller_1(3, 2))
print(grid_traveller_1(10, 10))
print(grid_traveller_2(10, 10))
print(grid_traveller_2(500, 500))
