def how_sum_1(target, num_list):
    if target == 0:
        return []

    for num in [x for x in num_list if x <= target]:
        remainder = target - num
        result = how_sum_1(remainder, num_list)
        if result is not None:
            return result + [num]


def how_sum_2(target, num_list, memo={}):
    if target == 0:
        return []

    if target in memo:
        return memo[target]

    for num in [x for x in num_list if x <= target]:
        remainder = target - num
        result = how_sum_2(remainder, num_list, memo)
        if result is not False:
            return result + [num]

    memo[target] = False
    return memo[target]


print(how_sum_1(7, [2, 3]))
print(how_sum_1(7, [5, 3, 4, 7]))
print(how_sum_1(7, [5, 4]))
print(how_sum_1(8, [2, 3, 5]))
print(how_sum_2(300, [7, 14]))
