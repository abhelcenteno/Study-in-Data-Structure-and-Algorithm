def can_sum_1(target_sum, num_list):
    if target_sum == 0:
        return True

    for num in [x for x in num_list if x <= target_sum]:
        remainder = target_sum - num
        if can_sum_1(remainder, num_list):
            return True

    return False


def can_sum_2(target_sum, num_list, memo={}):
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True

    for num in [x for x in num_list if x <= target_sum]:
        remainder = target_sum - num
        if can_sum_2(remainder, num_list, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum_1(7, [2, 3]))  # True
print(can_sum_1(7, [5, 3, 4, 7]))  # True
print(can_sum_1(7, [2, 4]))  # False
print(can_sum_1(8, [2, 3, 5]))  # True
print(can_sum_2(300, [7, 14]))  # False
print(can_sum_2(1000, [7, 14, 1]))  # True
